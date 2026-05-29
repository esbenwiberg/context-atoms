---
kind: rationale
claim: The Python SQL executor is intentionally not designed for performance; its
  purpose is unit testing and running SQL natively over Python dicts, with its architecture
  intended as a foundation for integration with fast compute kernels such as Arrow
  or Pandas.
anchors:
- sqlglot/executor/python.py
- sqlglot/executor/__init__.py
- sqlglot/executor/context.py
- sqlglot/executor/table.py
tags:
- executor
- performance
- design-intent
- testing
source: doc-import:README.md#examples
status: active
---
The Python SQL executor is intentionally not designed for performance; its purpose is unit testing and running SQL natively over Python dicts, with its architecture intended as a foundation for integration with fast compute kernels such as Arrow or Pandas. Tables are represented as plain Python dictionaries. Do not benchmark or optimize the executor for throughput — that is out of scope. If fast execution is needed, the correct path is to integrate the executor's planner/context abstractions with a vectorized compute backend, not to accelerate the pure-Python row-iteration engine itself.
