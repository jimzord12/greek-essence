## 4. Project and File Architecture

The repository is one application. It is feature-oriented but intentionally shallow: routing composes pages, components render UI, content owns facts, and `lib` owns reusable non-visual logic.

```text
greek-essence/
├── app/
│   ├── [locale]/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── destinations/
│   │   │   ├── page.tsx
│   │   │   └── [slug]/page.tsx
│   │   ├── experiences/
│   │   │   ├── page.tsx
│   │   │   └── [slug]/page.tsx
│   │   ├── journeys/
│   │   │   ├── page.tsx
│   │   │   └── [slug]/page.tsx
│   │   ├── about/ faq/ contact/ plan-my-trip/
│   │   ├── privacy/ cookies/ terms/
│   │   └── not-found.tsx
│   ├── api/trip-request/route.ts
│   ├── sitemap.ts
│   ├── robots.ts
│   └── globals.css
├── components/
│   ├── ui/                 # shadcn/Base UI primitives; no business content
│   ├── layout/             # C-01–C-04
│   ├── sections/           # C-05–C-24, C-27–C-30
│   ├── forms/              # C-25/C-26, fields, steps, draft/review states
│   └── motion/             # small reduced-motion-aware helpers
├── content/
│   ├── en/{pages,destinations,experiences,journeys}/
│   ├── el/{pages,destinations,experiences,journeys}/
│   ├── shared/             # locale-neutral IDs, relationships, media manifest
│   └── schemas/            # Zod content schemas
├── emails/
│   ├── trip-request-notification.tsx
│   └── trip-request-received.tsx
├── i18n/
│   ├── routing.ts
│   ├── request.ts
│   └── navigation.ts
├── messages/{en.json,el.json}
├── lib/
│   ├── content.ts
│   ├── seo.ts
│   ├── trip-request-schema.ts
│   ├── form-draft.ts
│   ├── resend.ts
│   ├── rate-limit.ts        # lightweight prototype guard only
│   ├── constants.ts
│   └── utils.ts
├── public/{images,icons,fonts}/
├── tests/{e2e,fixtures}/
├── middleware.ts
├── next.config.ts
├── tailwind.config.ts
└── package.json
```

### 4.1 Boundary rules

- `app/` handles route params, metadata, data loading, and page composition; it does not hold large UI blocks or raw JSON parsing.
- `components/ui/` contains only vendor-derived primitives and local wrappers. It never imports Greek Essence content.
- `components/sections/` receives typed props and maps directly to Prototype components C-01–C-30.
- `content/` contains facts. Its JSON must never contain React, HTML, API secrets, untrusted scripts, or hard-coded render behavior.
- `messages/` is only for small interface translations: buttons, validation errors, navigation, status text. Editorial copy stays in `content/`.
- `lib/content.ts` is the only public content-loading entry point. Replacing JSON with a CMS later changes this layer, not page components.
- `app/api/trip-request` is the sole server-side business endpoint. It has no browser-importable secrets.
- `emails/` renders email templates only; sending happens in `lib/resend.ts`.

---

