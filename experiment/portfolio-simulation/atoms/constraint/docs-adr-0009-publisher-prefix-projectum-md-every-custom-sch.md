---
kind: constraint
claim: "Every custom schema component this repository contributes \u2014 tables, columns,\
  \ Web Resources, option-sets \u2014 must use the `pum_` prefix and be declared under\
  \ the Projectum publisher in `solution/src/Other/Solution.xml`."
anchors:
- solution/src/Other/Solution.xml
- solution/src/Other/Customizations.xml
- solution/src/WebResources/pum_portfoliosim_index_html/.gitkeep
tags:
- dataverse
- publisher
- prefix
- schema
- constraint
source: doc-import:docs/adr/0009-publisher-prefix-projectum.md
status: active
---
Every custom schema component this repository contributes — tables, columns, Web Resources, option-sets — must use the `pum_` prefix and be declared under the Projectum publisher in `solution/src/Other/Solution.xml`.

`solution/src/Other/Solution.xml` is the source of truth for the publisher block. Any change to it surfaces in the packed ZIP diff produced by `npm run pack:solution`.

The Web Resource path follows this rule: `pum_portfoliosim/index.html` (not `cas_portfoliosim/index.html`). Anyone adding new solution components must contribute them to the Projectum publisher; cross-publisher scenarios are handled via Dataverse solution layering, not prefix segregation.
