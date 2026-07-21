
# Part VIII — Imagery and Media

## 18. Photography Art Direction

Photography is the primary visual identity carrier.

### 18.1 Subject balance

The image library should include:

- landscapes and coastlines;
- lived-in villages and urban texture;
- food, craft, and cultural details;
- boutique hospitality and interiors;
- genuine human moments;
- varied traveler ages and party types;
- transport and route context where useful;
- less obvious local experiences alongside iconic locations.

### 18.2 Visual character

Prefer:

- natural Mediterranean light;
- controlled highlights;
- authentic color;
- moderate contrast;
- human texture;
- calm composition;
- visible sense of place;
- editorial framing;
- candid interaction.

Avoid:

- excessive saturation;
- turquoise-water manipulation;
- generic stock smiles;
- staged champagne/luxury symbolism;
- empty villas as the sole premium cue;
- drone imagery everywhere;
- repetitive sunset imagery;
- misleading location imagery;
- overprocessed HDR;
- crowds cropped to imply exclusivity.

### 18.3 Crops and aspect ratios

| Use | Preferred ratio |
|---|---|
| Home hero | 16:9 to 3:2, art-directed |
| Destination hero | 16:9 or 3:2 |
| Journey hero | 16:9 |
| Editorial split | 4:5, 3:4, or 4:3 |
| Destination card | 4:3 |
| Journey card | 3:2 |
| Portrait/team | 4:5 |
| Gallery landscape | source-led, grouped consistently |
| Gallery portrait | 4:5 |

Every important image requires:

- intrinsic width and height;
- focal-point metadata;
- localized alt text or decorative status;
- location/context caption where useful;
- rights/source/permission record;
- crop review at all responsive modes.

### 18.4 Hero imagery

**Direction:** Cinematic Editorial.

- Image occupies roughly 50–70% of the opening viewport depending on page type.
- Home hero may approach 65–70%.
- Destination/journey heroes use approximately 55–65%.
- Interior/editorial heroes use approximately 45–55%.
- Text placement follows a safe focal zone rather than default centering.
- A controlled scrim supports text contrast.
- No floating glass card.
- No heavy overlay gradient unrelated to readability.
- Hero content remains understandable if media fails.

### 18.5 Scrim tokens

Suggested scrims:

```css
--hero-scrim-soft:
  linear-gradient(
    90deg,
    rgb(11 36 51 / 0.58) 0%,
    rgb(11 36 51 / 0.26) 48%,
    transparent 78%
  );

--hero-scrim-bottom:
  linear-gradient(
    0deg,
    rgb(11 36 51 / 0.58) 0%,
    rgb(11 36 51 / 0.10) 55%,
    transparent 82%
  );
```

Scrims are crop-dependent and may be adjusted only to maintain contrast. Do not use them as a brand effect on every image.

### 18.6 Captions and credits

- Captions use `caption` typography.
- Captions should identify location/context, not describe the obvious.
- Credits appear only where licensing or editorial practice requires them.
- Caption color must remain readable.
- Credits must not overlap essential image content.

### 18.7 Image failure

- Preserve aspect ratio and layout.
- Use a warm neutral fallback surface.
- Keep title, summary, and CTA usable.
- Do not display broken-image icons.
- If the image carries essential content, expose the fallback explanation in text.

---


