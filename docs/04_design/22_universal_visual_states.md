## 22. Universal Visual States

### 22.1 Focus

- Use a 2 px teal focus ring with 2 px offset.
- Ring must meet 3:1 against adjacent colors.
- Focus remains visible on primary buttons, image links, cards, menus, accordions, form controls, and custom choices.
- Do not remove browser focus without a replacement.
- Use `:focus-visible` where appropriate.
- Forced-colors mode must preserve a visible system outline.

### 22.2 Hover

- Hover is enhancement, never the only cue.
- Use restrained color, underline, border, image-scale, or 1–2 px lift.
- Avoid simultaneous scale, shadow, color, and motion changes.
- Touch experiences must not depend on hover.

### 22.3 Active/pressed

- Reduce elevation.
- Darken or deepen the relevant semantic color.
- Use a subtle translate of at most 1 px only where appropriate.
- Keep label readable.

### 22.4 Selected

- Use a subtle tint plus stronger border/check/icon.
- Do not rely on tint alone.
- Selected chips should remain clearly distinct in forced colors.

### 22.5 Disabled

- Use muted surface and text.
- Preserve readable label.
- Do not show hover effects.
- Disabled controls are not the sole explanation of missing prerequisites.

### 22.6 Loading

- Preserve control dimensions.
- Use text such as `Sending…` with an optional spinner.
- Spinners use current color and respect reduced motion.
- Do not hide all page content behind skeletons.
- Avoid shimmer.

### 22.7 Error

- Error text uses destructive foreground.
- Error surfaces use destructive subtle background.
- Inputs receive destructive border and explicit message.
- Add icon/summary as appropriate.
- Do not clear valid input.

### 22.8 Success

- Calm confirmation using success color, icon, heading, and next action.
- No confetti or oversized celebration.
- Success appears only after confirmed operational success.

### 22.9 Empty/unavailable

- Use neutral illustration/icon only if useful.
- Explain what is unavailable.
- Provide one or two recovery actions.
- Do not display empty card shells.

---


