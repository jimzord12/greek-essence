import type { Metadata } from "next"
import { getTranslations, setRequestLocale } from "next-intl/server"

import { QualityLabToggle } from "@/components/quality-lab-toggle"
import { Link } from "@/i18n/navigation"

export async function generateMetadata({
  params,
}: PageProps<"/[locale]/quality-lab">): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: "Fixture" })

  return {
    title: t("metadataLabTitle"),
    description: t("metadataLabDescription"),
    alternates: {
      canonical: `/${locale}/quality-lab`,
      languages: {
        en: "/en/quality-lab",
        el: "/el/quality-lab",
        "x-default": "/en/quality-lab",
      },
    },
    robots: { index: false, follow: false },
  }
}

export default async function QualityLabPage({
  params,
}: PageProps<"/[locale]/quality-lab">) {
  const { locale } = await params
  setRequestLocale(locale)
  const t = await getTranslations({ locale, namespace: "Fixture" })

  return (
    <>
      <a
        className="sr-only min-h-11 items-center rounded px-4 py-3 font-medium focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-10 focus:inline-flex focus:bg-background focus:outline-2 focus:outline-offset-2 focus:outline-teal-700"
        href="#main-content"
      >
        {t("skipToContent")}
      </a>
      <header className="border-b border-border">
        <nav
          aria-label={t("primaryNavigation")}
          className="mx-auto flex max-w-3xl flex-wrap gap-3 px-4 py-4"
        >
          <Link
            className="inline-flex min-h-11 items-center rounded px-3 py-2 font-medium underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-700"
            href="/"
          >
            {t("homeLink")}
          </Link>
          <Link
            className="inline-flex min-h-11 items-center rounded px-3 py-2 font-medium underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-700"
            href="/quality-lab"
            locale={locale === "en" ? "el" : "en"}
          >
            {t("switchLocale")}
          </Link>
        </nav>
      </header>
      <main className="mx-auto max-w-3xl px-4 py-12" id="main-content">
        <h1 className="text-3xl font-semibold tracking-tight break-words">
          {t("labTitle")}
        </h1>
        <section aria-labelledby="primitive-heading" className="mt-8 space-y-4">
          <h2 className="text-xl font-semibold" id="primitive-heading">
            {t("primitiveHeading")}
          </h2>
          <QualityLabToggle
            label={t("toggleLabel")}
            selectedLabel={t("toggleSelectedLabel")}
            statusLabel={t("toggleStatus")}
          />
        </section>
      </main>
    </>
  )
}
