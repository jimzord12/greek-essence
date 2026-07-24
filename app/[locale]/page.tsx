import type { Metadata } from "next"
import { setRequestLocale } from "next-intl/server"

import { SiteFooter } from "@/components/layout/site-footer"
import { SiteHeader } from "@/components/layout/site-header"
import { HomeSections } from "@/components/sections/home-sections"
import { routing, type Locale } from "@/i18n/routing"
import { getShowcaseContent, resolveMedia } from "@/lib/content"
import { getLocalizedHref } from "@/lib/routes"

type LocalePageProps = { params: Promise<{ locale: string }> }

export async function generateMetadata({
  params,
}: LocalePageProps): Promise<Metadata> {
  const { locale: rawLocale } = await params
  const locale = rawLocale as Locale
  const { metadata } = getShowcaseContent(locale).home
  return {
    title: metadata.title,
    description: metadata.description,
    alternates: {
      canonical: getLocalizedHref("home", locale),
      languages: { en: "/en", el: "/el", "x-default": "/en" },
    },
    robots: { index: false, follow: false },
  }
}

export default async function HomePage({ params }: LocalePageProps) {
  const { locale: rawLocale } = await params
  const locale = routing.locales.includes(rawLocale as Locale)
    ? (rawLocale as Locale)
    : "en"
  setRequestLocale(locale)
  const content = getShowcaseContent(locale).home
  return (
    <>
      <a className="skip-link" href="#main-content">
        {locale === "en" ? "Skip to content" : "Μετάβαση στο περιεχόμενο"}
      </a>
      <SiteHeader locale={locale} />
      <HomeSections
        content={content}
        heroMedia={resolveMedia(content.hero.mediaId!, locale)}
        locale={locale}
        parosMedia={resolveMedia(content.parosFeature.mediaId, locale)}
      />
      <SiteFooter locale={locale} />
    </>
  )
}
