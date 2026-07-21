## 13. Accessibility Implementation

The prototype targets WCAG 2.2 AA as required by the PRD/Prototype.

- One H1 per page; semantic landmarks; skip link; logical heading hierarchy.
- Keyboard-accessible header/menu/submenus, accordion, gallery, language switcher, and every form control.
- Visible non-color-only focus state; predictable focus order; Escape/return-focus behavior.
- Text/control contrast tested against all image overlays; information never depends solely on color, imagery, hover, or motion.
- Target size aims for 44×44 CSS pixels; no swipe-only or drag-only interaction.
- Labels, `fieldset`/`legend`, descriptions, inline errors, error summary, live status, and success focus for forms.
- Localized `lang` attributes and reviewed English/Greek label lengths; no critical truncation.
- Alt text, captions/transcripts for meaningful media, decorative media hidden appropriately, reduced-motion support.
- 200% text zoom and reflow at narrow widths without loss of functionality or horizontal page scrolling.

shadcn/Base UI primitives are a starting point, not proof of accessibility. Every composed component is tested in the actual Greek Essence layout.

---

