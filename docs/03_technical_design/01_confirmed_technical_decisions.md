## 1. Confirmed Technical Decisions

| Area | Decision | Status |
|---|---|---|
| Framework | Latest stable Next.js App Router with TypeScript 6 | Confirmed |
| Internationalization | `next-intl`; explicit English and Greek routes | Confirmed |
| Styling | Tailwind CSS v4+ | Confirmed |
| Component base | Latest shadcn/ui with Base UI | Confirmed |
| Content | Local JSON files in Git, schema-validated | Confirmed |
| Hosting | Vercel Hobby for private client prototype | Confirmed |
| Dynamic surface | One Vercel Route Handler for form submission | Confirmed |
| Email | Resend free tier | Confirmed |
| Lead recipient | Configured Greek Essence Gmail inbox | Confirmed |
| Visitor email | Branded acknowledgement: “We received your request” | Confirmed |
| Database/CMS/form service | None in this prototype | Confirmed |
| Form persistence | Browser `localStorage`, 72-hour expiry, manual clear | Confirmed |
| Testing | Lightweight, Playwright-led | Confirmed |
| Analytics/monitoring | Deferred beyond prototype | Confirmed |
| Performance | High-impact, low-complexity best practices and budgets | Confirmed |

### 1.1 Non-goals

The build must not add or imply booking, availability, payments, accounts, dashboards, itinerary management, CRM/Ezus integration, a back-office, dynamic inventory, price comparison, customer reviews, marketing automation, or a full operational lead platform. It is not a generic form-builder embed; the custom trip form is built in the Greek Essence UI.

### 1.2 Architecture principles

- **Static first.** All public pages and content render from local data at build time.
- **One dynamic boundary.** Only form submission runs server-side.
- **Premium interaction, minimal JavaScript.** Use client components only where interaction needs them.
- **Custom UI, managed email delivery.** The form belongs to Greek Essence; Resend handles email transport.
- **Future-replaceable content.** Page components depend on typed content models, not filesystem details.
- **Truth over polish.** No unapproved claim, service, price, availability, response promise, or trust asset ships.
- **Production gaps are visible.** Avoid prototype shortcuts becoming accidental production architecture.

---

