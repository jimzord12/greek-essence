## 15. Error, Loading, Empty, Unavailable, and Success States

| State | Implementation |
|---|---|
| Static content | Render actual content directly; avoid decorative page loaders |
| Form client initialization | Preserve layout; show only a short disabled/loading state if truly needed |
| Validation | C-29 error summary plus inline messages; never clear values |
| Submission pending | Disable only the submit action; clear text status; retain draft |
| Submission failure | No false success; preserve draft; retry with same current submission ID; offer direct contact fallback |
| Submission success | Clear draft after response; focus and announce C-27 confirmation |
| Missing content/translation | C-30 with concise explanation and relevant alternative/index link |
| Image/media failure | Preserve meaningful text/action and layout; use neutral fallback |
| Not found | Localized 404, recovery links, noindex |

No client component waits for animation before exposing content or an action. A form retry is user initiated; the prototype does not perform background retries that could create surprise duplicate messages.

---

