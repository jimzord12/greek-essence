## 2. Responsibilities of Each Approved Item

| Item | What it contributes | When agents should use it |
|---|---|---|
| `AGENTS.md` | Concise repository-wide rules, authority, required commands, architectural constraints, and definition of done | Before every repository task |
| Google Chrome Modern Web Guidance | Modern interoperable HTML, CSS, forms, accessibility, browser APIs, compatibility, privacy, security, and Baseline-aware guidance | When selecting or reviewing web-platform capabilities |
| Vercel `next-best-practices` | Next.js App Router conventions, framework APIs, routing, rendering boundaries, file conventions, and common implementation mistakes | When creating or reviewing Next.js routes, layouts, metadata, Server Components, Client Components, or framework-specific logic |
| Vercel `vercel-react-best-practices` | React rendering, client-work reduction, waterfall avoidance, bundle impact, and performance-sensitive component patterns | When creating or reviewing React component trees and client interactions |
| Playwright CLI skill | Correct and efficient use of Playwright CLI by coding agents | Before interactive browser inspection or debugging |
| `greek-essence-quality-review` | Project-specific visual, responsive, content, trust, accessibility, localization, SEO-presentation, and form-quality review | After implementing or materially changing pages, components, navigation, content presentation, or the trip-request flow |
| Playwright CLI | Interactive inspection of localhost and trusted previews | During implementation, debugging, visual review, and reproduction of browser defects |

### 2.1 Playwright CLI versus Playwright Test

These are separate tools with separate responsibilities:

- **Playwright CLI** is the interactive browser interface used by coding agents.
- **Playwright Test** is the permanent automated browser-testing framework defined by `03_TECHNICAL_DESIGN.md`.

Agents should convert recurring or release-critical defects discovered through Playwright CLI into durable Playwright Test coverage when practical.

---

