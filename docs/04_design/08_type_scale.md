## 8. Type Scale

Fluid type is allowed through `clamp()` for major display roles. UI and body sizes remain predictable.

| Role/token | Family | Weight | Compact size | Wide size | Line height | Tracking | Usage |
|---|---|---:|---:|---:|---:|---:|---|
| `display-1` | Cormorant | 600 | 48 px | 76 px | 0.98–1.02 | -0.025em | Home H1 only |
| `display-2` | Cormorant | 600 | 42 px | 64 px | 1.00–1.05 | -0.02em | destination/journey hero H1 |
| `heading-1` | Cormorant | 600 | 38 px | 52 px | 1.05 | -0.018em | interior H1 |
| `heading-2` | Cormorant | 600 | 32 px | 44 px | 1.10 | -0.015em | major section H2 |
| `heading-3` | Cormorant | 600 | 27 px | 34 px | 1.15 | -0.01em | editorial H3/card feature |
| `heading-4` | Inter | 600 | 20 px | 22 px | 1.30 | -0.01em | compact headings |
| `title-lg` | Inter | 600 | 18 px | 20 px | 1.35 | -0.008em | cards/form groups |
| `title-md` | Inter | 600 | 16 px | 18 px | 1.35 | 0 | UI heading |
| `body-lg` | Inter | 400 | 18 px | 20 px | 1.65 | 0 | lead/editorial intro |
| `body-md` | Inter | 400 | 16 px | 17 px | 1.65 | 0 | default body |
| `body-sm` | Inter | 400 | 14 px | 15 px | 1.55 | 0 | supporting text |
| `label-lg` | Inter | 600 | 16 px | 16 px | 1.25 | 0 | large button/form label |
| `label-md` | Inter | 600 | 14 px | 14 px | 1.25 | 0.005em | standard UI label |
| `label-sm` | Inter | 600 | 12 px | 12 px | 1.25 | 0.015em | compact metadata |
| `caption` | Inter | 400 | 12 px | 13 px | 1.45 | 0.01em | image caption/credit |
| `eyebrow` | Inter | 600 | 12 px | 13 px | 1.25 | 0.09em | short uppercase section cue |
| `quote` | Cormorant | 500 | 28 px | 40 px | 1.22 | -0.01em | editorial highlight |

### 8.1 Typography rules

- One H1 per page.
- Display sizes may scale down earlier for Greek text where wrapping becomes visually poor.
- Do not force headings into one line.
- Avoid all-caps Greek for long text. Uppercase is limited to short eyebrows and metadata.
- Body paragraphs should usually remain between **55 and 72 characters** per line.
- Editorial lead text may use a narrower measure of 48–62 characters.
- Legal content should not use the display family for body text.
- Button labels should not use Cormorant.
- Links in prose remain visibly distinguishable through underline or another non-color-only treatment.
- Widows/orphans should be reviewed in prominent headings but not solved with hard-coded nonbreaking spaces across languages.

### 8.2 Greek localization rules

- Test accented uppercase and lowercase Greek in every role.
- Greek body text may require slightly more line height than English; allow up to +0.05.
- Do not reduce font size to force Greek labels into English dimensions.
- Navigation must switch to compact mode when labels no longer fit.
- Avoid aggressive negative tracking in Greek.
- Use language-appropriate punctuation and quotation marks in content.
- Never transliterate Greek as a visual workaround.
- Validate numerals, dates, currency placeholders, names, and mixed Greek/Latin proper nouns.

---


