import type { ArchmapConfig } from "./config.js";
import { matchOverride } from "./config.js";
import type { Topology } from "./graph.js";

export type Klass = "leaf" | "branch" | "hub";

export interface Classification {
  file: string;
  class: Klass;
  ca: number;
  instability: number;
  reason: string;
  overridden: boolean;
}

export function classifyFile(
  file: string,
  topology: Topology,
  config: ArchmapConfig
): Classification {
  const override = matchOverride(file, config.overrides);
  if (override) {
    const node = topology.files[file];
    const ca = node?.ca ?? 0;
    const ce = node?.ce ?? 0;
    const total = ca + ce;
    return {
      file,
      class: override.classification,
      ca,
      instability: total === 0 ? 0 : ce / total,
      reason: override.reason,
      overridden: true,
    };
  }

  const node = topology.files[file];
  if (!node) {
    process.stderr.write(
      `warning: "${file}" not found in dependency graph — treating as leaf\n`
    );
    return {
      file,
      class: "leaf",
      ca: 0,
      instability: 0,
      reason: "not in dependency graph",
      overridden: false,
    };
  }

  const { ca, ce } = node;
  const total = ca + ce;
  const instability = total === 0 ? 0 : ce / total;

  let klass: Klass;
  if (ca <= config.thresholds.leaf) {
    klass = "leaf";
  } else if (ca <= config.thresholds.junction) {
    klass = "branch";
  } else {
    klass = "hub";
  }

  return {
    file,
    class: klass,
    ca,
    instability,
    reason: `Ca=${ca} (${ca} dependent${ca === 1 ? "" : "s"})`,
    overridden: false,
  };
}
