---
kind: rationale
claim: The production Dockerfile uses a two-stage build (builder + production) to
  keep the final image small by excluding dev dependencies and build tooling.
anchors:
- Dockerfile
tags:
- docker
- build
- multi-stage
source: doc-import:CLAUDE.md#docker-production
status: active
---
The production Dockerfile uses a two-stage build (builder + production) to keep the final image small by excluding dev dependencies and build tooling. The `builder` stage installs all deps and runs `pnpm build`; the `production` stage is a fresh Alpine + Node 22 image that only copies compiled output. This pattern was chosen over a single-stage build to avoid shipping TypeScript source, test files, and large dev dependency trees into production, reducing attack surface and image size. The dev image (`Dockerfile.daemon.dev`) intentionally breaks this separation to support hot reload.
