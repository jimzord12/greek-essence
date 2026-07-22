import { getTranslations, setRequestLocale } from "next-intl/server"

import { Link } from "@/i18n/navigation"

export default async function LocaleFixturePage({
  params,
}: PageProps<"/[locale]">) {
  const { locale } = await params
  setRequestLocale(locale)
  const t = await getTranslations("Fixture")

  return (
    <main>
      <h1>{t("title")}</h1>
      <nav aria-label={t("languageNavigation")}>
        <Link href="/" locale="en">
          EN
        </Link>
        {" | "}
        <Link href="/" locale="el">
          EL
        </Link>
      </nav>
    </main>
  )
}
