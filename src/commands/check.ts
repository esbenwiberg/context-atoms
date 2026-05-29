import { loadConfig } from "../config.js";
import { classifyFile } from "../classify.js";
import { getFreshTopology } from "../cache.js";
import { buildTopology } from "../graph.js";
import type { Classification } from "../classify.js";

export async function checkCommand(
  files: string[],
  opts: { json?: boolean; config?: string }
): Promise<void> {
  const config = loadConfig(opts.config);
  const entry = config.analyzers.find((a) => a.lang === "typescript")?.entry ?? "src/";
  const { topology } = await getFreshTopology(entry, buildTopology);

  const results: Classification[] = files.map((f) =>
    classifyFile(f, topology, config)
  );
  const hubs = results.filter((r) => r.class === "hub");
  const hasHubs = hubs.length > 0;

  if (opts.json) {
    console.log(
      JSON.stringify({ hasHubs, hubs, all: results }, null, 2)
    );
  } else {
    if (hasHubs) {
      console.log(`load-bearing (hub) files detected:`);
      for (const h of hubs) {
        console.log(`  ${h.file}  Ca=${h.ca}  ${h.reason}`);
      }
    } else {
      console.log("No hub files in changeset.");
    }
  }

  if (hasHubs) process.exit(1);
}
