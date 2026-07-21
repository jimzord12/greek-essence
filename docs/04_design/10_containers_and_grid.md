## 10. Containers and Grid

### 10.1 Container tokens

| Token | Maximum width | Use |
|---|---:|---|
| `container-prose` | 720 px | long-form text |
| `container-narrow` | 880 px | FAQ, form, legal intro |
| `container-content` | 1120 px | standard editorial sections |
| `container-wide` | 1280 px | collections, galleries |
| `container-hero` | 1440 px / full bleed | cinematic hero composition |
| `container-full` | none | controlled full-bleed media |

### 10.2 Gutters

| Mode | Viewport | Page gutter |
|---|---:|---:|
| Compact | 320–767 px | 20 px; 16 px only at extreme 320 px constraints |
| Medium | 768–1199 px | 32–48 px |
| Wide | 1200 px+ | 64–80 px |
| Very wide | 1600 px+ | content remains capped; outer space grows |

Use fluid gutters where useful:

```css
--page-gutter: clamp(1.25rem, 3.5vw, 5rem);
```

### 10.3 Grid

- Compact: 4 conceptual columns.
- Medium: 8 conceptual columns.
- Wide: 12 conceptual columns.
- Use CSS Grid and `minmax()` rather than device-specific logic.
- Prose never expands to the full collection width.
- Full-bleed media must maintain safe internal alignment with the page grid.
- Collection cards should use intrinsic widths and content-aware wrapping.
- Do not force uniform card heights when it harms text hierarchy.

---


