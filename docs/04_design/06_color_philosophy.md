
# Part III — Color System

## 6. Color Philosophy

The palette is inspired by the Aegean at natural depth, limestone architecture, warm plaster, sun-softened sand, restrained vegetation, and deep slate shadow.

Photography should provide most saturated color. Interface colors remain calm and controlled.

### 6.1 Primitive palette

| Primitive token | Value | Character |
|---|---:|---|
| `--ge-ivory-50` | `#FFFCF6` | brightest warm canvas |
| `--ge-ivory-100` | `#FAF6ED` | primary background |
| `--ge-limestone-100` | `#F1EDE3` | subtle section surface |
| `--ge-limestone-200` | `#E6DFD2` | borders and separators |
| `--ge-sand-200` | `#D8C8AD` | restrained warm accent |
| `--ge-sand-500` | `#9B7C55` | captions/decorative detail |
| `--ge-blue-950` | `#0B2433` | deepest brand/overlay |
| `--ge-blue-900` | `#103348` | primary active |
| `--ge-blue-800` | `#17475F` | primary brand |
| `--ge-blue-700` | `#215B72` | primary hover alternative |
| `--ge-blue-100` | `#DCEAF0` | primary tint |
| `--ge-teal-800` | `#275F63` | accent active |
| `--ge-teal-700` | `#34767A` | accent |
| `--ge-teal-100` | `#DCEBE8` | accent tint |
| `--ge-olive-700` | `#5D684B` | limited editorial accent |
| `--ge-olive-100` | `#E7E9DE` | olive tint |
| `--ge-slate-950` | `#172126` | strongest text |
| `--ge-slate-800` | `#2D393E` | primary text |
| `--ge-slate-600` | `#59666B` | secondary text |
| `--ge-slate-500` | `#707C80` | muted text |
| `--ge-slate-300` | `#BFC7C8` | disabled/border |
| `--ge-white` | `#FFFFFF` | controlled white |
| `--ge-black` | `#000000` | scrim base only |
| `--ge-success-700` | `#2F6B4F` | success foreground |
| `--ge-success-100` | `#E1EFE7` | success surface |
| `--ge-warning-800` | `#7A5725` | warning foreground |
| `--ge-warning-100` | `#F4E8CF` | warning surface |
| `--ge-error-700` | `#A13B39` | error foreground |
| `--ge-error-100` | `#F7E3E1` | error surface |
| `--ge-info-700` | `#2E607A` | information foreground |
| `--ge-info-100` | `#E0EDF3` | information surface |

### 6.2 Semantic color tokens

| Semantic token | Value / primitive | Intended use | Required pairing | Status | Tailwind mapping |
|---|---|---|---|---|---|
| `--color-background` | ivory-100 | default page canvas | foreground | Confirmed direction | `bg-background` |
| `--color-foreground` | slate-950 | primary text | background/card | Confirmed | `text-foreground` |
| `--color-surface` | ivory-50 | raised/contained surfaces | foreground | Confirmed | `bg-surface` |
| `--color-surface-subtle` | limestone-100 | purposeful grouped section | foreground | Confirmed | `bg-surface-subtle` |
| `--color-card` | ivory-50 | cards | card-foreground | Confirmed | `bg-card` |
| `--color-card-foreground` | slate-950 | card text | card | Confirmed | `text-card-foreground` |
| `--color-popover` | white | menus/popovers | popover-foreground | Confirmed | `bg-popover` |
| `--color-popover-foreground` | slate-950 | overlay text | popover | Confirmed | `text-popover-foreground` |
| `--color-primary` | blue-800 | dominant CTA and key controls | primary-foreground | Confirmed | `bg-primary` |
| `--color-primary-hover` | blue-900 | primary hover | primary-foreground | Provisional exact value | custom state |
| `--color-primary-active` | blue-950 | primary active | primary-foreground | Provisional | custom state |
| `--color-primary-foreground` | white | text/icons on primary | primary | Confirmed | `text-primary-foreground` |
| `--color-primary-subtle` | blue-100 | highlighted informational area | blue-950 | Confirmed | `bg-primary-subtle` |
| `--color-accent` | teal-700 | secondary highlight, selected accent | accent-foreground | Confirmed | `bg-accent` |
| `--color-accent-hover` | teal-800 | accent hover | white | Provisional | custom state |
| `--color-accent-subtle` | teal-100 | selected/subtle accent surface | slate-950 | Confirmed | `bg-accent-subtle` |
| `--color-accent-foreground` | slate-950 | text on accent tint | accent-subtle | Confirmed | `text-accent-foreground` |
| `--color-muted` | limestone-100 | quiet UI background | muted-foreground | Confirmed | `bg-muted` |
| `--color-muted-foreground` | slate-600 | helper/caption text | background/muted | Confirmed | `text-muted-foreground` |
| `--color-border` | limestone-200 | standard soft border | adjacent surfaces | Confirmed | `border-border` |
| `--color-border-strong` | sand-200 | emphasized divider | light surfaces | Provisional | `border-border-strong` |
| `--color-input` | limestone-200 | input border | input background | Confirmed | `border-input` |
| `--color-ring` | teal-700 | keyboard focus ring | light surfaces | Confirmed | `ring-ring` |
| `--color-link` | blue-800 | inline links | background | Confirmed | `text-link` |
| `--color-link-hover` | blue-950 | inline link hover | background | Provisional | custom state |
| `--color-disabled-bg` | limestone-100 | disabled controls | disabled-fg | Confirmed | custom |
| `--color-disabled-fg` | slate-500 | disabled content | disabled-bg | Confirmed | custom |
| `--color-success` | success-700 | success text/icon | success-subtle | Confirmed | custom |
| `--color-success-subtle` | success-100 | success message | success | Confirmed | custom |
| `--color-warning` | warning-800 | warning text/icon | warning-subtle | Confirmed | custom |
| `--color-warning-subtle` | warning-100 | warning message | warning | Confirmed | custom |
| `--color-destructive` | error-700 | destructive/error action | destructive-subtle/white | Confirmed | `text-destructive` |
| `--color-destructive-subtle` | error-100 | error message | destructive | Confirmed | custom |
| `--color-info` | info-700 | information text/icon | info-subtle | Confirmed | custom |
| `--color-info-subtle` | info-100 | information message | info | Confirmed | custom |
| `--color-overlay` | black / alpha | modal/gallery backdrop | white | Confirmed | custom |
| `--color-hero-foreground` | white | text over approved hero | hero scrim/image | Confirmed | custom |
| `--color-hero-scrim` | black alpha gradient | contrast support | hero foreground | Confirmed | custom |

### 6.3 Contrast rules

- Normal body text must meet at least **4.5:1** contrast.
- Large text must meet at least **3:1**, though 4.5:1 is preferred for important content.
- UI component boundaries and focus indicators must meet at least **3:1** against adjacent colors.
- Muted text must not be used for critical instructions, field labels, errors, or required legal context.
- White text over `--color-primary` must be checked after any primary-color adjustment.
- Text-over-image contrast must be tested against the final crop at compact, medium, and wide sizes.
- A scrim must be added when image contrast is unreliable; text shadow alone is insufficient.
- Status must use iconography, text, and/or structure in addition to color.
- Disabled styling must remain legible but must not be mistaken for enabled state.

### 6.4 Color usage limits

- Olive is editorial support only; it is not a second CTA color.
- Teal is used for focus, selected accents, subtle highlights, and selected decorative details.
- Sand and limestone support warmth and structure.
- Deep blue owns the dominant action.
- Bright white should be reserved for overlays, email-like surfaces, and controlled contrast—not the full page canvas.
- Gradients are permitted only as functional image scrims, not decorative backgrounds.

### 6.5 Appearance policy

The prototype supports **light appearance only**. No `dark:` variants, dark token set, appearance toggle, or system-theme logic should be added.

---


