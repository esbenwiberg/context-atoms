---
kind: rationale
claim: Warm container pools (repos pre-cloned, deps pre-installed, caches pre-warmed)
  are the target architecture for fast spinup; Autopod currently provisions fresh
  each time, which is the primary gap versus Stripe's <10-second benchmark.
anchors:
- packages/daemon/src/containers/docker-container-manager.ts
- packages/daemon/src/images/dockerfile-generator.ts
- packages/daemon/src/images/image-builder.ts
tags:
- containers
- performance
- warm-pool
- spinup
source: doc-import:docs/ai-coding-agent-patterns-research-v2.md#5-container-isolation-environment-design
status: active
---
Warm container pools (repos pre-cloned, deps pre-installed, caches pre-warmed) are the target architecture for fast spinup; Autopod currently provisions fresh each time, which is the primary gap versus Stripe's <10-second benchmark. The `StackTemplate` concept and image-builder infrastructure exist as a foundation, but pre-warmed images with dependency caches are not yet in use. Closing this gap requires baking repo clone + dep install into image layers at build time, then drawing from a live pool rather than provisioning on demand. Stripe uses AWS EC2 warm pools; ACI and Docker equivalents exist but require explicit pool management.
