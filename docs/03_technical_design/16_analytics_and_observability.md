## 16. Analytics and Observability

Analytics and formal monitoring are deferred from this client prototype. Do not install a tracker, session replay, advertising pixel, error-tracking SDK, or dashboard merely to satisfy a checklist.

The code should retain lightweight, provider-neutral hook points for future events: `primary_cta_click`, `form_start`, `form_step_complete`, `form_validation_error` (code only), `form_submit_success`, `form_submit_failure`, `language_switch`, and direct-contact clicks. These hooks must not transmit data until a future analytics provider, consent model, data-retention policy, and event specification are approved.

For prototype debugging, use Vercel function logs and Resend’s delivery dashboard manually. Neither may receive or expose a full raw form payload through application logging. Production requires the PRD’s observability and analytics requirements to be reintroduced.

---

