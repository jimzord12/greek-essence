## 3. Technology Stack and Version Policy

| Layer | Decision | Responsibility |
|---|---|---|
| Application | Latest stable Next.js App Router | Routes, static rendering, metadata, route handler |
| Language | TypeScript 6, strict mode | Compile-time contracts and safer refactoring |
| i18n | `next-intl` | Locale routing, UI messages, navigation, request locale |
| Styling | Tailwind CSS v4+ | Tokens, responsive utilities, layout and state styles |
| UI primitives | shadcn/ui + Base UI | Accessible unstyled/low-style control primitives, then brand styling |
| Form state | React Hook Form + Zod | Four-step state, client validation, field registration |
| Content validation | Zod | Local JSON data and relation validation at build time |
| Email | Resend SDK + React Email | Gmail lead notification and visitor acknowledgement |
| Hosting | Vercel Hobby | Prototype deploys, CDN, route handler, previews |
| Tests | Playwright | High-value browser flows and responsive smoke tests |
| Code quality | ESLint, TypeScript, Prettier | Fast local/CI checks |

Pin exact package versions in `package.json` and the committed `pnpm-lock.yaml`; use the latest stable releases only when implementation begins, not a floating version range. Patch/minor updates may be grouped. Framework, `next-intl`, Tailwind, shadcn/Base UI, or React major changes require a manual update, build, and Playwright run.

No package is added merely because it is popular. Client bundle size, accessibility, security maintenance, and actual UI value are the admission criteria.

---

