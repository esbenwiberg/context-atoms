import { cruise } from "dependency-cruiser";

export interface FileNode {
  ca: number;
  ce: number;
  dependents: string[];
}

export interface Topology {
  files: Record<string, FileNode>;
}

export async function buildTopology(entry: string): Promise<Topology> {
  const result = await cruise([entry], {
    doNotFollow: { path: "node_modules" },
    exclude: { path: "\\.(test|spec)\\.tsx?$" },
  });

  const modules = (result.output as any).modules as Array<{
    source: string;
    dependencies: Array<{ resolved: string; coreModule?: boolean }>;
    dependents?: string[];
  }>;

  const files: Topology["files"] = {};
  for (const m of modules) {
    const ce = m.dependencies.filter((d) => !d.coreModule).length;
    // dependency-cruiser provides dependents[] directly
    const deps = m.dependents ?? [];
    files[m.source] = { ca: deps.length, ce, dependents: deps };
  }
  return { files };
}
