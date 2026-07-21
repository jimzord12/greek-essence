## 7. Design System, Components, Responsive Behavior, and Motion

### 7.1 Styling architecture

Tailwind v4 implements the approved token system: semantic colors, typography roles, spacing, radii, shadows, layers, container widths, focus rings, target sizes, and motion values. Global CSS contains reset/base/font declarations and token definitions only. Component-specific variants use Tailwind utilities and `cva`/shadcn patterns where that improves consistency.

shadcn/ui is a source-owned component pattern, not a black-box design system. Base UI primitives provide accessible control behavior; Greek Essence styles, labels, spacing, motion, and composition remain local. Never modify generated primitive code casually; wrap it when brand behavior differs.

### 7.2 Component implementation map

| Prototype ID | Implementation family | Essential implementation responsibility |
|---|---|---|
| C-01–C-04 | `components/layout` | Header/nav, footer, language switch, breadcrumbs; route-derived active state and keyboard behavior |
| C-05–C-10 | `components/sections/narrative` | Hero/editorial sections/gallery/quote; semantic headings, media fallbacks, reduced motion |
| C-11–C-16 | `components/sections/discovery` | Destination/experience/journey cards, route summary, related content; typed local relations |
| C-17–C-22 | `components/sections/trust` | Promise, process, credentials, team, benefits, FAQ; approved-content-only rendering |
| C-23–C-24 | `components/sections/conversion` | Contextual Plan My Trip CTA and approved contact actions |
| C-25–C-27 | `components/forms` | Multi-step trip request, short contact form if included, accepted/error confirmation states |
| C-28–C-30 | `components/sections/utility` | Privacy notice, status feedback, empty/unavailable recovery |

The table assigns code ownership; layout, variants, interactions, and CTA hierarchy remain governed by Prototype §8.

### 7.3 Responsive implementation

Implement mobile first and validate 320 px, 390 px, 834 px, 1440 px, intermediate widths, landscape, and 200% text zoom. Use CSS Grid/Flexbox, intrinsic sizing, `minmax`, `clamp`, and content-driven Tailwind breakpoints—never viewport/device sniffing.

- Compact navigation is an explicit, keyboard-accessible menu; desktop submenus do not rely on hover.
- Cards reflow to readable columns without horizontal page scrolling.
- Forms remain a single logical reading/keyboard sequence; short related fields may align on wider screens only.
- Galleries always have visible button controls; swipe is an enhancement, never the sole interaction.
- No sticky mobile CTA is assumed until prototype testing shows value without obstruction.
- Greek strings, long labels, and localized dates are tested at each critical mode.

### 7.4 Motion

Use CSS-first, short, restrained opacity/transform transitions for navigation, disclosure, card feedback, image reveal, and form state changes. JavaScript animation libraries are not a default dependency. All non-essential movement is disabled or reduced under `prefers-reduced-motion`; motion never carries meaning, delays action, moves focus unexpectedly, auto-advances a carousel, or shifts content after targeting.

---

