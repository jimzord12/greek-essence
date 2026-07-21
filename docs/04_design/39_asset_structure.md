
# Part XVI — Assets and File Conventions

## 39. Asset Structure

```text
public/
  images/
    destinations/
    experiences/
    journeys/
    people/
    brand/
    decorative/
  icons/
    brand/
  fonts/                    # only if self-hosted and licensed

content/shared/
  media.json                # IDs, dimensions, focal points, rights, source
```

### 39.1 File naming

Use lowercase kebab-case:

```text
paros-naousa-evening-01.webp
athens-acropolis-dawn-01.avif
journey-cyclades-couple-01.webp
founder-firstname-lastname-01.webp
```

Avoid:

- `IMG_1234.jpg`;
- filenames containing unverified claims;
- spaces;
- language-specific filenames when one asset serves both locales.

### 39.2 Media metadata

Each asset record should include:

- stable ID;
- source file;
- width/height;
- aspect ratio;
- focal point;
- alt text per locale or decorative status;
- caption per locale where needed;
- location;
- creator/source;
- license/permission status;
- approval status;
- expiry/review date where applicable.

### 39.3 Decorative SVG

- optimized;
- `currentColor` where possible;
- no embedded raster assets;
- no inline scripts;
- descriptive title only if meaningful;
- otherwise `aria-hidden`.

---


