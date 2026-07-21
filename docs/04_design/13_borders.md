## 13. Borders

### 13.1 Default rules

- Standard border width: 1 px.
- Use low-contrast neutral border tokens.
- Strong borders are reserved for active/selected/focus/error states.
- Avoid border-heavy layouts.
- Section separators should usually be whitespace, not rules.
- Decorative dividers are distinct from structural borders and must remain rare.

### 13.2 State borders

| State | Border |
|---|---|
| Default input | `border-input` |
| Hover input | slightly stronger neutral |
| Focus | neutral border plus visible teal ring |
| Selected | accent/primary border plus surface tint |
| Invalid | error border plus error text/icon |
| Disabled | muted border and surface |
| Card hover | optional border-strength increase; no mandatory shadow |

---


