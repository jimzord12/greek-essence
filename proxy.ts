import { type NextRequest, NextResponse } from "next/server"
import createMiddleware from "next-intl/middleware"

import { routing } from "./i18n/routing"

const handleI18nRouting = createMiddleware(routing)

export default function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl

  if (pathname === "/") {
    return NextResponse.redirect(new URL("/en", request.url))
  }

  const hasLocale = routing.locales.some(
    (locale) => pathname === `/${locale}` || pathname.startsWith(`/${locale}/`)
  )

  return hasLocale ? handleI18nRouting(request) : NextResponse.next()
}

export const config = {
  matcher: "/((?!api|_next|_vercel|.*\\..*).*)",
}
