"""Thin wrapper around the `claude` CLI in headless (`-p`) mode.

The whole experiment rides the user's existing Claude auth via this CLI rather
than a metered API key. Two usage shapes:

  text_call()    single-shot transform, no tools, --output-format json
  agent_run()    multi-turn agent with tools, --output-format stream-json,
                 returns full transcript for telemetry (see runner.py)
"""
from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

CLAUDE_BIN = "claude"


@dataclass
class TextResult:
    text: str
    cost_usd: float
    duration_ms: int
    is_error: bool
    raw: dict[str, Any] = field(default_factory=dict)


def text_call(
    prompt: str,
    *,
    model: str = "sonnet",
    cwd: str | Path = "/tmp",
    timeout: int = 180,
) -> TextResult:
    """Single-shot text transform. No tools, single turn. Prompt via stdin."""
    args = [
        CLAUDE_BIN, "-p",
        "--model", model,
        "--max-turns", "1",
        "--output-format", "json",
        "--allowedTools", "",  # no tools: pure transform
    ]
    try:
        proc = subprocess.run(
            args, input=prompt, capture_output=True, text=True,
            cwd=str(cwd), timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return TextResult("", 0.0, 0, True, {"error": f"timeout after {timeout}s"})
    if proc.returncode != 0:
        return TextResult("", 0.0, 0, True, {"stderr": proc.stderr[:500]})
    try:
        d = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return TextResult("", 0.0, 0, True, {"stdout": proc.stdout[:500]})
    return TextResult(
        text=d.get("result", "") or "",
        cost_usd=float(d.get("total_cost_usd") or 0.0),
        duration_ms=int(d.get("duration_ms") or 0),
        is_error=bool(d.get("is_error")),
        raw=d,
    )


def extract_json_block(text: str) -> Any:
    """Pull the first JSON array/object out of a model response (handles ```json fences)."""
    s = text.strip()
    if "```" in s:
        # take content between first ``` fence pair
        parts = s.split("```")
        for part in parts:
            p = part.strip()
            if p.startswith("json"):
                p = p[4:].strip()
            if p[:1] in "[{":
                try:
                    return json.loads(p)
                except json.JSONDecodeError:
                    continue
    # fall back: find first [ or { and parse to matching end greedily
    for opener, closer in (("[", "]"), ("{", "}")):
        i, j = s.find(opener), s.rfind(closer)
        if 0 <= i < j:
            try:
                return json.loads(s[i : j + 1])
            except json.JSONDecodeError:
                continue
    raise ValueError("no JSON block found in model response")
