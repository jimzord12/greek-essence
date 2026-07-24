import { Link } from "@/i18n/navigation"
import type { Locale } from "@/i18n/routing"

export function SiteFooter({ locale }: { locale: Locale }) {
  return (
    <footer className="site-footer">
      <div className="shell footer-inner">
        <p className="brand">Greek Essence</p>
        <p>
          {locale === "en"
            ? "Thoughtful journeys through Greece."
            : "Ταξίδια στην Ελλάδα με σκέψη και φροντίδα."}
        </p>
        <Link href="/" locale={locale}>
          {locale === "en" ? "Back to Home" : "Επιστροφή στην αρχική"}
        </Link>
      </div>
    </footer>
  )
}
