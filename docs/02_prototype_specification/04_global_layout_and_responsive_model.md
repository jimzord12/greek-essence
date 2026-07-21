## 4. Global Layout and Responsive Model

### 4.1 Layout principles

- Use a centered editorial content frame with controlled full-bleed media.
- Text measure must remain comfortable; long prose should not span the full page width.
- Page rhythm alternates immersive, editorial, discovery, trust, and conversion sections rather than repeating identical card grids.
- Section boundaries rely primarily on space, typography, imagery, and restrained surface shifts—not heavy borders or decoration.
- Important meaning must remain in text, not only imagery or layout position.

### 4.2 Prototype viewport modes

The following ranges are prototype reference modes, not production implementation mandates:

| Mode | Reference range | Required prototype frame | Layout behavior |
|---|---:|---:|---|
| Compact | 320–767 px | 390 × 844 | Single-column priority; mobile menu; stacked forms and cards |
| Medium | 768–1199 px | 834 × 1112 | Two-column where useful; condensed navigation or menu based on fit |
| Wide | 1200 px and above | 1440 × 1024 | Full navigation; editorial multi-column compositions |

The design must also be inspected at 320 px width, at 200% text zoom, and across intermediate widths to prevent breakpoint-only success.

### 4.3 Grid and spacing behavior

- Compact: one primary column; occasional two-up chips or small metadata only when labels remain readable.
- Medium: two-column card collections; text/media sections may use balanced split layouts.
- Wide: up to three or four cards depending on content density; prose remains narrower than the full grid.
- Section spacing should convey deliberate calm. Compact spacing may reduce proportionally but must not collapse hierarchy.
- Dense rows of more than four cards must wrap or become a clearly controlled carousel only where lateral discovery is demonstrably useful.

### 4.4 Reflow rules

- Content order must remain semantically meaningful when columns stack.
- In alternating text/media sections, mobile order defaults to heading, text, action, then supporting image unless the image is necessary to establish context first.
- Primary action precedes secondary action when stacked.
- Route diagrams reflow to a vertical sequence on compact screens.
- Tables used for legal or structured information must reflow or scroll with clear context; page content should not cause horizontal viewport scrolling.
- No essential action may be hover-only.

### 4.5 Fixed and sticky elements

- A sticky compact header may be used.
- A mobile sticky `Plan My Trip` action is optional and should be tested; it must not cover content, cookie controls, form navigation, or system UI.
- Within the trip request, Back and Continue controls may remain visible near the bottom of a compact viewport only if content and error messages remain unobscured.
- Do not stack multiple sticky layers.

### 4.6 Content density

- Opening screens communicate one proposition, one supporting thought, and one primary action.
- Cards show only decision-useful summary content; detailed descriptions remain on detail pages.
- Long pages use descriptive headings and visual pacing, not arbitrary truncation.
- Accordions are reserved for genuinely optional detail or FAQs, not to conceal primary content.

---

