
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

``media.json`` is the sole mapping from a stable asset ID to a physical source
file and its media metadata. Page content and components reference the stable
ID only. Replacing an image therefore changes one manifest record rather than
every content record that presents it.


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

Generated prototype media may enter the manifest with a pending approval
status, but it must not be rendered until its focal point, localized alt text,
source/rights record, and visual review are complete. Keep prompt-planning
records separate from this runtime-facing manifest so their historic planning
status remains intact.


- optimized;
- `currentColor` where possible;
- no embedded raster assets;
- no inline scripts;
- descriptive title only if meaningful;
- otherwise `aria-hidden`.

---


