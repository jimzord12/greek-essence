
# Part XIV — Tailwind CSS v4 Implementation

## 36. Theme Structure

Tailwind CSS v4 exposes theme variables through `@theme`. Greek Essence should define raw values and semantic utilities centrally.

Suggested structure:

```css
/* app/globals.css */
@import "tailwindcss";

:root {
  --ge-ivory-100: #faf6ed;
  --ge-blue-800: #17475f;
  --ge-blue-900: #103348;
  --ge-teal-700: #34767a;
  --ge-slate-950: #172126;
  --ge-slate-600: #59666b;
  --ge-limestone-100: #f1ede3;
  --ge-limestone-200: #e6dfd2;

  --background: var(--ge-ivory-100);
  --foreground: var(--ge-slate-950);
  --card: #fffcf6;
  --card-foreground: var(--ge-slate-950);
  --popover: #ffffff;
  --popover-foreground: var(--ge-slate-950);
  --primary: var(--ge-blue-800);
  --primary-foreground: #ffffff;
  --secondary: var(--ge-limestone-100);
  --secondary-foreground: var(--ge-slate-950);
  --muted: var(--ge-limestone-100);
  --muted-foreground: var(--ge-slate-600);
  --accent: #dcebe8;
  --accent-foreground: var(--ge-slate-950);
  --destructive: #a13b39;
  --border: var(--ge-limestone-200);
  --input: var(--ge-limestone-200);
  --ring: var(--ge-teal-700);
  --radius: 0.625rem;
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);

  --font-display: var(--font-cormorant);
  --font-sans: var(--font-inter);

  --radius-sm: 0.5rem;
  --radius-md: 0.625rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  --radius-2xl: 1.25rem;

  --shadow-xs: 0 1px 2px rgb(11 36 51 / 0.05);
  --shadow-sm: 0 6px 18px rgb(11 36 51 / 0.08);
  --shadow-md: 0 12px 32px rgb(11 36 51 / 0.12);
  --shadow-lg: 0 24px 64px rgb(11 36 51 / 0.18);
}
```

### 36.1 Naming conventions

Use:

- `bg-background`
- `text-foreground`
- `text-muted-foreground`
- `bg-primary`
- `text-primary-foreground`
- `border-border`
- `ring-ring`
- `font-display`
- `font-sans`

Avoid in page components:

- raw hex values;
- arbitrary Tailwind colors such as `blue-700`;
- repeated arbitrary spacing values;
- arbitrary shadow strings;
- duplicated component state formulas.

### 36.2 Arbitrary values

Allowed only for:

- art-directed grid placement;
- rare exact aspect ratios;
- safe-area calculations;
- crop positioning;
- documented hero height constraints.

Do not use arbitrary values to bypass missing design tokens.

---


