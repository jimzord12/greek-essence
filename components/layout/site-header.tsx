"use client"

import { useEffect, useRef, useState } from "react"

import { Link } from "@/i18n/navigation"
import type { Locale } from "@/i18n/routing"
import { getRoutePathname } from "@/lib/routes"

const labels = {
  en: {
    nav: "Primary navigation",
    menu: "Menu",
    home: "Home",
    paros: "Paros & Antiparos",
    plan: "Plan my trip",
    other: "Ελληνικά",
  },
  el: {
    nav: "Κύρια πλοήγηση",
    menu: "Μενού",
    home: "Αρχική",
    paros: "Πάρος & Αντίπαρος",
    plan: "Σχεδιάστε το ταξίδι μου",
    other: "English",
  },
} as const

export function SiteHeader({ locale }: { locale: Locale }) {
  const [open, setOpen] = useState(false)
  const trigger = useRef<HTMLButtonElement>(null)
  const nav = useRef<HTMLElement>(null)
  const l = labels[locale]
  const otherLocale = locale === "en" ? "el" : "en"

  useEffect(() => {
    if (!open) return
    const keydown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        setOpen(false)
        trigger.current?.focus()
      }
    }
    const outside = (event: PointerEvent) => {
      if (!nav.current?.contains(event.target as Node)) setOpen(false)
    }
    window.addEventListener("keydown", keydown)
    document.addEventListener("pointerdown", outside)
    return () => {
      window.removeEventListener("keydown", keydown)
      document.removeEventListener("pointerdown", outside)
    }
  }, [open])

  const close = () => setOpen(false)
  return (
    <header className="site-header">
      <nav ref={nav} aria-label={l.nav} className="site-nav">
        <Link aria-current="page" className="brand" href="/" locale={locale}>
          Greek Essence
        </Link>
        <button
          ref={trigger}
          className="menu-trigger"
          type="button"
          aria-expanded={open}
          aria-controls="primary-menu"
          onClick={() => setOpen((value) => !value)}
        >
          {l.menu}
        </button>
        <div
          className={open ? "nav-links is-open" : "nav-links"}
          id="primary-menu"
        >
          <Link aria-current="page" href="/" locale={locale} onClick={close}>
            {l.home}
          </Link>
          <Link
            href={getRoutePathname("paros")}
            locale={locale}
            onClick={close}
            prefetch={false}
          >
            {l.paros}
          </Link>
          <Link
            className="nav-cta"
            href={getRoutePathname("plan-my-trip")}
            locale={locale}
            onClick={close}
            prefetch={false}
          >
            {l.plan}
          </Link>
          <Link href="/" locale={otherLocale} onClick={close}>
            {l.other}
          </Link>
        </div>
      </nav>
    </header>
  )
}
