import { notFound } from "next/navigation"
import { getRequestConfig } from "next-intl/server"

import { routing, type Locale } from "./routing"

export default getRequestConfig(async ({ requestLocale }) => {
  const locale = await requestLocale

  if (!locale || !routing.locales.includes(locale as Locale)) {
    notFound()
  }

  return {
    locale,
    messages: (await import(`../messages/${locale}.json`)).default,
  }
})
