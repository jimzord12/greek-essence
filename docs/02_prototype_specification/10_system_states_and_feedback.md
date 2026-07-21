## 10. System States and Feedback

### 10.1 Loading

- Core text and navigation should not be hidden behind decorative loaders.
- Media may load progressively with stable reserved space; avoid layout shifts that move controls.
- Collection loading placeholders should approximate final geometry and include an accessible status only when waiting materially affects the user.
- Form submission uses a clear textual submitting state.

### 10.2 Empty and unavailable

- Empty search/filter results explain the active constraint and offer reset.
- Missing related content causes the module to be omitted or replaced with a curated parent link.
- Missing translation uses the language-unavailable pattern.
- An unapproved service, claim, channel, journey, policy, or credential is omitted—not represented with invented placeholder truth.

### 10.3 Errors

- Page/content errors explain the failure and offer retry or alternative navigation.
- Form input errors remain local and actionable.
- Submission errors explicitly say receipt was not confirmed.
- Broken media uses a stable neutral fallback and must not leave inaccessible text-on-image treatment.
- A global error message must not erase more specific field guidance.

### 10.4 Success

Success feedback confirms the completed action, explains what changes next, and avoids exaggerated celebration. Calm acknowledgement fits the brand better than confetti or intrusive animation.

---

