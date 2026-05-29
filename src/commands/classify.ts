import { loadConfig } from "../config.js";
import { classifyFile } from "../classify.js";
import { getFreshTopology } from "../cache.js";
import { buildTopology } from "../graph.js";
import type { Classification } from "../classify.js";

export async function classifyCommand(
  file: string,
  opts: { json?: boolean; config?: string }
): Promise<void> {
  const config = loadConfig(opts.config);
  const entry = config.analyzers.find((a) => a.lang === "typescript")?.entry ?? "src/";
  const { topology, cacheHit } = await getFreshTopology(entry, buildTopology);

  if (!opts.json) {
    process.stderr.write(cacheHit ? "(cache hit)\n" : "(topology rebuilt)\n");
  }

  const result: Classification = classifyFile(file, topology, config);

  if (opts.json) {
    console.log(JSON.stringify(result, null, 2));
  } else {
    const instPct = (result.instability * 100).toFixed(0);
    console.log(`${result.file}`);
    console.log(`  class:       ${result.class}${result.overridden ? " (overridden)" : ""}`);
    console.log(`  ca:          ${result.ca}`);
    console.log(`  instability: ${instPct}%`);
    console.log(`  reason:      ${result.reason}`);
  }
}
