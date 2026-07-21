## 19. Deployment and Demo Workflow

1. Develop on a feature branch with local mock email delivery.
2. Push branch → Vercel Preview deployment with protected/test email behavior.
3. Run content/build/Playwright gates and review compact/wide English/Greek pages.
4. Merge approved work to `main` → Vercel prototype deployment.
5. Configure custom domain after confirming it is safe for the owner demo.
6. Add Resend domain DNS records, verify sender, test Gmail notification and acknowledgement.
7. Run a final owner-demo checklist with representative—not real customer—data.

Vercel’s deployment rollback may restore a prior application build, but there is no application data to migrate or restore in this prototype. Content rolls back through Git. Use a `DEMO_MODE`/test-recipient configuration where helpful to prevent accidental real lead handling.

GitHub Actions may run the lightweight checks on pull requests; Vercel supplies preview deployments. The repository uses protected `main`, code review for the route handler/content schemas, and secret scanning. This is sufficient for prototype collaboration without an enterprise release process.

---

