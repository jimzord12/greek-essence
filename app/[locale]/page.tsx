import type { Metadata } from "next"
import { getTranslations, setRequestLocale } from "next-intl/server"

import { Link } from "@/i18n/navigation"

export async function generateMetadata({
  params,
}: PageProps<"/[locale]">): Promise<Metadata> {
  const { locale } = await params
  const t = await getTranslations({ locale, namespace: "Fixture" })

  return {
    title: t("metadataHomeTitle"),
    description: t("metadataHomeDescription"),
    alternates: {
      canonical: `/${locale}`,
      languages: {
        en: "/en",
        el: "/el",
        "x-default": "/en",
      },
    },
    robots: { index: false, follow: false },
  }
}

export default async function LocaleFixturePage({
  params,
}: PageProps<"/[locale]">) {
  const { locale } = await params
  setRequestLocale(locale)
  const t = await getTranslations("Fixture")

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
          aria-label={t("languageNavigation")}
          className="mx-auto flex max-w-3xl flex-wrap gap-3 px-4 py-4"
        >
          <Link
            className="inline-flex min-h-11 items-center rounded px-3 py-2 font-medium underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-700"
            href="/"
            locale="en"
          >
            {t("english")}
          </Link>
          <Link
            className="inline-flex min-h-11 items-center rounded px-3 py-2 font-medium underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-700"
            href="/"
            locale="el"
          >
            {t("greek")}
          </Link>
        </nav>
      </header>
      <main className="mx-auto max-w-3xl px-4 py-12" id="main-content">
        <h1 className="text-3xl font-semibold tracking-tight break-words">
          {t("title")}
        </h1>
        <p className="mt-4 text-muted-foreground">{t("status")}</p>
        <Link
          className="mt-8 inline-flex min-h-11 items-center rounded px-3 py-2 font-medium underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-700"
          href="/quality-lab"
        >
          {t("labLink")}
        </Link>
      </main>
    </>
  )
}
