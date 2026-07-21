
# Part IV — Typography

## 7. Font Families

### 7.1 Display family: Cormorant Garamond

Use for:

- H1 and major H2 headings;
- selected editorial pull quotes;
- journey/destination names;
- carefully controlled hero display text.

Do not use for:

- body copy;
- form labels;
- buttons;
- navigation;
- dense metadata;
- long legal content.

### 7.2 Body and interface family: Inter

Use for:

- body content;
- UI labels;
- navigation;
- buttons;
- form fields and errors;
- metadata;
- captions;
- cards;
- FAQ;
- legal content;
- email templates where supported.

### 7.3 Fallback stacks

```css
--font-display:
  "Cormorant Garamond",
  "Noto Serif",
  Georgia,
  "Times New Roman",
  serif;

--font-sans:
  "Inter",
  "Noto Sans",
  system-ui,
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  sans-serif;
```

### 7.4 Licensing, availability, and performance

Both selected families are available through Google Fonts. The implementation should use `next/font/google` or self-hosted files only where license and deployment requirements are confirmed.

Requirements:

- load only necessary weights;
- use variable font files where they provide a smaller practical payload and stable rendering;
- avoid italic files unless the design uses them;
- subset Latin and Greek where supported without breaking mixed-language content;
- use `font-display: swap`;
- preload only fonts required above the fold;
- do not exceed the Technical Design limit of two families;
- verify Greek glyph quality in real content, including tonos, dialytika, uppercase, and numerals.

### 7.5 Approved weights

| Family | Weight | Usage |
|---|---:|---|
| Cormorant Garamond | 500 | regular display headings |
| Cormorant Garamond | 600 | emphasized hero/H1 |
| Inter | 400 | body copy and normal UI |
| Inter | 500 | labels, metadata, medium emphasis |
| Inter | 600 | buttons, navigation emphasis, compact headings |
| Inter | 700 | rare strong UI emphasis |

Avoid Inter 300 and Cormorant 300 because thin strokes reduce readability and feel fragile on lower-quality displays.

---


