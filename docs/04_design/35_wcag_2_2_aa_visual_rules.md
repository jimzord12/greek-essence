
# Part XIII — Accessibility

## 35. WCAG 2.2 AA Visual Rules

### 35.1 Contrast

- Meet AA for all text.
- Aim above minimum for body and critical interface text.
- Validate final image overlays programmatically and visually.
- Do not use muted foreground for essential instructions.
- Ensure placeholder text remains legible without acting as the label.

### 35.2 Focus

- All interactive elements have visible focus.
- Focus is never clipped by overflow.
- Focus ring survives transparent header, image backgrounds, and selected states.
- Modal/gallery focus is contained and restored.

### 35.3 Target size

- Aim for 44 × 44 CSS px.
- Never go below 24 × 24 for a standalone pointer target.
- Provide spacing between adjacent compact controls.
- Text links in paragraphs rely on text height and adequate line spacing.

### 35.4 Text zoom and reflow

- Work at 200% zoom.
- No horizontal page scrolling at narrow widths except controlled tables/galleries where documented.
- No fixed-height text containers.
- Buttons and navigation labels wrap or change mode rather than truncate critical meaning.
- Greek expansion must be included in QA.

### 35.5 Text over images

- Use a tested scrim.
- Keep text away from high-detail regions.
- Preserve contrast across responsive crops.
- Do not rely on a text shadow.
- Provide a non-image fallback.

### 35.6 Forced colors

- Preserve system outlines.
- Do not disable `forced-color-adjust` globally.
- Ensure selected, current, and invalid states retain borders/icons/text.
- Decorative SVGs may disappear without affecting meaning.
- Test native/custom choice controls.

### 35.7 Motion

- Support reduced motion.
- No motion carries unique meaning.
- No auto-advancing media.
- No focus movement triggered by decoration.

### 35.8 Content structure

- Typography must reflect semantic headings rather than simulate them.
- One H1.
- Captions, helper text, and labels remain programmatically associated.
- Visual order matches reading/focus order.

---


