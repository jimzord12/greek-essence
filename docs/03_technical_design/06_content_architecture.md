## 6. Content Architecture

### 6.1 Local JSON model

Use simple, human-editable JSON files with Zod validation. Avoid a generic page builder. Content is deliberately constrained to maintain the approved page hierarchy and quality.

Core types:

- `SiteSettings`, `Navigation`, `Footer`, `PageMetadata`;
- `Destination`, `Experience`, `Journey`;
- `Hero`, `EditorialSection`, `Gallery`, `Quote`, `RouteStop`, `RelatedContent`;
- `TrustCredential`, `PersonProfile`, `FaqItem`, `ContactChannel`, `Cta`.

Entities carry an immutable `id`, locale-specific `slug`, `title`, `summary`, `body`, SEO fields, image references, publication flag, and relationship IDs. Image references are stable IDs from `content/shared/media.json`, never physical paths; the manifest owns file selection, intrinsic dimensions, crop/focal metadata, source/rights status, and localized media text. A journey includes duration, route, mood, traveller fit, highlights, and explicit customizable wording; it never contains booking price, availability, or inventory fields.

### 6.2 Content validation

`pnpm validate:content` must run before `next build` and in CI. It rejects:

- malformed JSON or a schema mismatch;
- duplicated IDs/slugs;
- a broken relationship or relation to unpublished content;
- missing required English/Greek structural fields;
- invalid localized URL/canonical values;
- missing image dimensions, alt text, rights/source status, or required focal metadata;
- an unapproved trust credential, missing ownership/attribution, or expired permission;
- forbidden price/availability/review claims in structured fields.

The prototype may use representative copy/assets only when visibly marked in source as provisional and never presented as a real business fact.

### 6.3 Editorial versus interface localization

| Content kind | Location | Ownership |
|---|---|---|
| Destination/journey/about/editorial text | `content/en` and `content/el` | Content/localization owner |
| Form options and explanatory labels | Content/config or messages according to whether they are editorial | Product/content owner |
| Buttons, nav, error/status text | `messages/en.json`, `messages/el.json` | Development/design with localization review |
| Emails | React Email template plus locale messages | Development/content review |

Translation is not a last-minute machine conversion. Both locale structures must remain aligned. Exact translation ownership and final content approval remain a release dependency.

---

