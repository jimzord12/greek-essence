import type { Metadata } from "next"
import { Cormorant_Garamond, Inter } from "next/font/google"
import { notFound } from "next/navigation"
import { NextIntlClientProvider } from "next-intl"
import { setRequestLocale } from "next-intl/server"
import type { ReactNode } from "react"

import { routing, type Locale } from "@/i18n/routing"

import "../globals.css"

const inter = Inter({
  subsets: ["latin", "greek"],
  variable: "--font-inter",
  display: "swap",
  preload: false,
})
const display = Cormorant_Garamond({
  subsets: ["latin"],
  weight: ["500", "600"],
  variable: "--font-display",
  display: "swap",
  preload: false,
})

export const metadata: Metadata = {
  metadataBase: new URL(
    process.env.NEXT_PUBLIC_SITE_URL ??
      (process.env.NODE_ENV === "production"
        ? "http://127.0.0.1:3101"
        : "http://localhost:3000")
  ),
}

export function generateStaticParams() {
  return routing.locales.map((locale) => ({ locale }))
}
export const dynamicParams = false

type LocaleLayoutProps = {
  children: ReactNode
  params: Promise<{ locale: string }>
}

export default async function LocaleLayout({
  children,
  params,
}: LocaleLayoutProps) {
  const { locale } = await params
  if (!routing.locales.includes(locale as Locale)) notFound()
  setRequestLocale(locale)
  const messages = (await import(`../../messages/${locale}.json`)).default
  return (
    <html
      lang={locale}
      className={`${inter.variable} ${display.variable}`}
      data-scroll-behavior="smooth"
    >
      <body>
        <NextIntlClientProvider locale={locale} messages={messages}>
          {children}
        </NextIntlClientProvider>
      </body>
    </html>
  )
}
