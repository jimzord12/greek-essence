## 15. Shadows and Elevation

### 15.1 Philosophy

Whitespace, typography, surface color, and borders establish most hierarchy. Shadows are subtle and functional.

| Level | Token | Suggested shadow | Use |
|---|---|---|---|
| 0 | `shadow-none` | none | page sections |
| 1 | `shadow-xs` | `0 1px 2px rgb(11 36 51 / 0.05)` | select cards/controls |
| 2 | `shadow-sm` | `0 6px 18px rgb(11 36 51 / 0.08)` | scrolled header, lifted card |
| 3 | `shadow-md` | `0 12px 32px rgb(11 36 51 / 0.12)` | dropdown/popover |
| 4 | `shadow-lg` | `0 24px 64px rgb(11 36 51 / 0.18)` | modal/gallery viewer |

Rules:

- Standard cards do not automatically float.
- Hover elevation is optional and limited to 1–2 px visual lift.
- Avoid layered multi-color shadows.
- Do not use strong shadows around large editorial imagery.
- Elevation must never be the sole state indicator.

---


