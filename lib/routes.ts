import type { Locale } from "@/i18n/routing"

export type ShowcaseRouteId = "home" | "paros" | "plan-my-trip" | "confirmation"

export const showcaseRoutes = {
  home: (locale: Locale) => `/${locale}` as const,
  paros: (locale: Locale) => `/${locale}/destinations/paros-antiparos` as const,
  "plan-my-trip": (locale: Locale) => `/${locale}/plan-my-trip` as const,
  confirmation: (locale: Locale) =>
    `/${locale}/plan-my-trip/confirmation` as const,
} satisfies Record<ShowcaseRouteId, (locale: Locale) => string>

export function getLocalizedHref(
  routeId: ShowcaseRouteId,
  locale: Locale
): string {
  return showcaseRoutes[routeId](locale)
}

export function getRoutePathname(routeId: ShowcaseRouteId): string {
  return getLocalizedHref(routeId, "en").replace(/^\/en(?=\/|$)/, "") || "/"
}
