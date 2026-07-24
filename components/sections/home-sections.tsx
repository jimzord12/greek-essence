import Image from "next/image"

import type { ShowcaseContent } from "@/content/schemas/showcase"
import { Link } from "@/i18n/navigation"
import type { Locale } from "@/i18n/routing"
import type { MediaResolution } from "@/lib/content"
import { getRoutePathname } from "@/lib/routes"

function Media({
  resolution,
  priority = false,
}: {
  resolution: MediaResolution
  priority?: boolean
}) {
  if (resolution.kind === "fallback")
    return <div aria-hidden="true" className="media-fallback" />
  const { media } = resolution
  return (
    <Image
      alt={media.alt}
      className="showcase-media"
      height={media.height}
      priority={priority}
      sizes="(max-width: 767px) 100vw, 50vw"
      src={media.src}
      style={{
        objectPosition: `${media.focalPoint.xPercent}% ${media.focalPoint.yPercent}%`,
      }}
      width={media.width}
    />
  )
}

function Cta({
  cta,
  locale,
  className = "text-link",
}: {
  cta: ShowcaseContent["home"]["finalCta"]
  locale: Locale
  className?: string
}) {
  const available = cta.routeId === "home"
  return (
    <Link
      className={className}
      href={getRoutePathname(cta.routeId)}
      locale={locale}
      prefetch={available ? undefined : false}
    >
      {cta.label}
    </Link>
  )
}

export function HomeSections({
  content,
  locale,
  heroMedia,
  parosMedia,
}: {
  content: ShowcaseContent["home"]
  locale: Locale
  heroMedia: MediaResolution
  parosMedia: MediaResolution
}) {
  return (
    <main id="main-content">
      <section className="hero section-pad">
        <Media priority resolution={heroMedia} />
        <div className="shell hero-copy">
          <p className="eyebrow">{content.hero.eyebrow}</p>
          <h1>{content.hero.title}</h1>
          <p className="lead">{content.hero.summary}</p>
          <div className="cta-row">
            <Cta
              cta={content.hero.primaryCta}
              locale={locale}
              className="button button-primary"
            />
            {content.hero.secondaryCta ? (
              <Cta
                cta={content.hero.secondaryCta}
                locale={locale}
                className="button button-secondary"
              />
            ) : null}
          </div>
        </div>
      </section>
      <section className="section-pad">
        <div className="shell editorial narrow">
          <p className="eyebrow">{content.promise.eyebrow}</p>
          <h2>{content.promise.heading}</h2>
          {content.promise.body.map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
        </div>
      </section>
      <section className="section-pad surface">
        <div className="shell split">
          <Media resolution={parosMedia} />
          <div>
            <p className="eyebrow">
              {locale === "en" ? "An island pairing" : "Δύο νησιά μαζί"}
            </p>
            <h2>{content.parosFeature.title}</h2>
            <p>{content.parosFeature.summary}</p>
            {content.parosFeature.cta ? (
              <Cta cta={content.parosFeature.cta} locale={locale} />
            ) : null}
          </div>
        </div>
      </section>
      <section className="section-pad">
        <div className="shell">
          <h2>{content.howItWorks.heading}</h2>
          <ol className="steps">
            {content.howItWorks.steps.map((step, index) => (
              <li key={step.title}>
                <span>{index + 1}</span>
                <h3>{step.title}</h3>
                <p>{step.summary}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>
      <section className="section-pad story">
        <div className="shell narrow">
          <p className="eyebrow">{content.trustStory.eyebrow}</p>
          <h2>{content.trustStory.heading}</h2>
          {content.trustStory.body.map((paragraph) => (
            <p key={paragraph}>{paragraph}</p>
          ))}
        </div>
      </section>
      <section className="section-pad final-cta">
        <div className="shell narrow">
          <h2>
            {locale === "en"
              ? "Your journey can begin here"
              : "Το ταξίδι σας μπορεί να ξεκινήσει εδώ"}
          </h2>
          <p>
            {locale === "en"
              ? "Tell us what you imagine, and take the first step towards a journey with your own rhythm."
              : "Μοιραστείτε όσα φαντάζεστε και κάντε το πρώτο βήμα για ένα ταξίδι στον δικό σας ρυθμό."}
          </p>
          <Cta
            cta={content.finalCta}
            locale={locale}
            className="button button-light"
          />
        </div>
      </section>
    </main>
  )
}
