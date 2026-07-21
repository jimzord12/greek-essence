## 8. Media, Assets, and Performance

### 8.1 Assets

- Store approved public images under `public/images` or import them from version-controlled assets; no hotlinked third-party images.
- Use `next/image` with declared dimensions, responsive `sizes`, appropriate crops, and lazy loading below the fold.
- Provide AVIF/WebP where supported with safe fallback behavior; preserve aspect ratio to avoid layout shift.
- Hero media is priority-loaded only when it is actually the LCP image. Never preload several images or autoplay video by default.
- Every image has localized alt text or is deliberately decorative; license/source/permission status remains in the local media manifest.
- Icons are an intentionally small SVG set. Decorative icons are hidden from assistive technology.
- Video remains optional. If used, it is poster-first, non-blocking, captioned/transcribed where meaningful, pausable, and has a still-image alternative.

### 8.2 Prototype performance budgets

These are release targets, not licenses to add weight:

| Metric | Budget/target |
|---|---:|
| LCP | ≤ 2.5 s at p75 after public launch measurement |
| INP | ≤ 200 ms at p75 |
| CLS | ≤ 0.1 at p75 |
| Initial critical route JavaScript | ≤ 150 KiB gzip |
| Form route JavaScript | ≤ 200 KiB gzip |
| Initial critical CSS | ≤ 40 KiB gzip |
| Cold mobile Home transfer | ≤ 1.8 MiB unless approved art direction needs more |
| Initial hero image | Normally ≤ 400 KiB |
| Fonts | Maximum two families and necessary weights only |

High-impact, low-complexity measures are mandatory: static generation, image sizing/optimization, limited client components, font subsetting/self-hosting where licensed, deferred non-critical scripts, no heavy carousel/video/parallax library, compression, semantic HTML, and bundle analysis before release. Advanced caching/observability work is deferred unless it becomes necessary.

---

