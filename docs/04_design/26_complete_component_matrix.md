
# Part XI — Component Visual Mapping C-01 to C-30

## 26. Complete Component Matrix

| ID | Visual responsibility | Variants/states | Responsive behavior | Accessibility concern | Implementation location |
|---|---|---|---|---|---|
| C-01 Header | transparent/solid surfaces, logo, nav, CTA, menu trigger | overlay, solid, scrolled, submenu open, mobile | full nav only while fit allows; compact menu otherwise | contrast, focus, active state, target size | `components/layout` |
| C-02 Footer | warm grouped surface, column hierarchy, contact/legal | full, compact, unavailable channel | columns collapse into labeled groups | heading structure, descriptive contacts | `components/layout` |
| C-03 Language Switcher | text-led compact selector | header, menu, footer, unavailable translation | remains visible without crowding | current language non-color cue | `components/layout` |
| C-04 Breadcrumbs | quiet orientation line | standard, overflow/wrap | wrap/scroll without viewport overflow | semantic current item | `components/layout` |
| C-05 Hero | cinematic media, display type, scrim, CTA | home, destination, experience, journey, interior | crop/focal shift; content stacks | text contrast, reduced motion | `components/sections` |
| C-06 Editorial Intro | narrow prose, lead type, optional fit cues | standard, centered, split | remains narrow/readable | heading order, text measure | `components/sections` |
| C-07 Section Header | eyebrow, heading, description, link | left, centered, compact | links stack where needed | correct heading level | `components/sections` |
| C-08 Rich Story | text/media composition | image left/right/full width | semantic stacking | reading order and alt text | `components/sections` |
| C-09 Gallery | editorial grid/viewer | grid, strip, modal, failure | grid simplifies; controls visible | keyboard, focus trap, captions | `components/sections` |
| C-10 Quote | display quote, subtle frame/motif | brand belief, planner insight, fact | narrower measure on compact | not mistaken for testimonial | `components/sections` |
| C-11 Destination Card | image-led editorial card | featured, standard, related | 1–4 columns by width | link clarity, image alternative | `components/sections` |
| C-12 Destination Collection | hierarchy and grid rhythm | priority, secondary, related | priority order preserved | section heading and grouping | `components/sections` |
| C-13 Experience Card | outcome-led card | featured, standard, related | stacks; icon remains secondary | label not icon-only | `components/sections` |
| C-14 Journey Card | route, duration, fit, image | featured, standard, related | metadata remains adjacent | route readable as text | `components/sections` |
| C-15 Route Summary | ordered route line/stops | compact, horizontal, vertical | vertical on compact | sequence in text | `components/sections` |
| C-16 Related Content | concise curated recommendations | 1–4 items | omit empty slots | meaningful relationship labels | `components/sections` |
| C-17 Brand Promise | editorial value statement | compact, full | stacks cleanly | clarity without imagery | `components/sections` |
| C-18 How It Works | numbered process | 3-step, 5-step | vertical sequence compact | ordered structure | `components/sections` |
| C-19 Trust Credentials | restrained evidence presentation | narrative, list, attributed mark | no dense logo wall | clear ownership/attribution | `components/sections` |
| C-20 Team Profile | portrait and biography | compact, expanded | portrait/text stack | name/role association | `components/sections` |
| C-21 Benefit Grid | concise outcome items | 3–5 items | 1–3 columns | icon not sole meaning | `components/sections` |
| C-22 FAQ | soft disclosure rows | accordion, open list | full-width compact | focus, expanded state | `components/sections` |
| C-23 Primary CTA Block | contextual high-confidence conversion | general, destination, journey, recovery | actions stack primary first | hierarchy and contrast | `components/sections` |
| C-24 Contact Options | monitored channel list | cards/list, unavailable channel | 1–2 columns | recognizable labels | `components/sections` |
| C-25 Trip Request | form shell, stepper, fields, state feedback | steps 1–4, failure, recovery | single-column primary | labels/errors/focus/zoom | `components/forms` |
| C-26 Contact Form | compact field system | initial/error/loading/success | single-column compact | no duplicated qualification | `components/forms` |
| C-27 Confirmation | calm success surface and next step | success/recovery | centered narrow composition | focus to heading, non-color success | `components/forms/sections` |
| C-28 Privacy Notice | quiet legal context | inline, boxed | remains near collection point | readable contrast, links | `components/sections` |
| C-29 Status Message | semantic feedback | info/warning/error/loading/success | full width within context | live-region discipline | `components/sections` |
| C-30 Unavailable State | neutral recovery composition | translation/content/media | narrow and direct | no silent redirect | `components/sections` |

---


