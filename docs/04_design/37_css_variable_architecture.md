## 37. CSS Variable Architecture

Recommended files:

```text
app/
  globals.css

styles/                     # optional if globals becomes too large
  tokens.css
  base.css
  utilities.css

components/
  ui/                       # shadcn/Base UI source-owned primitives
  layout/
  sections/
  forms/
  motion/
```

Rules:

- tokens are centralized;
- base element styles remain minimal;
- component-specific rules live with components or controlled variant definitions;
- no runtime CSS-in-JS;
- no second theme object in TypeScript;
- email templates may mirror tokens using safe email-compatible values but must not become the source of truth.

---


