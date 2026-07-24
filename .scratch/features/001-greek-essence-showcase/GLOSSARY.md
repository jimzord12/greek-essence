# Greek Essence Showcase Glossary

Feature-specific terms only. Add entries when a term is introduced, renamed, disambiguated, or rejected.

## Language

**Showcase**: The bounded Tier-2 client-demo prototype consisting of localized Home, Paros & Antiparos, Plan My Trip, and confirmation routes plus the demonstrated submission flow. It is not the complete product or a production launch.
_Avoid_: MVP, production site, full website

**Plan My Trip**: The site-wide CTA label that opens the four-step request flow, optionally carrying editable destination context.
_Avoid_: Book now, booking form

**Request a Custom Itinerary**: The page title inside the Plan My Trip flow; it asks for enough information for later human follow-up and does not create a booking.
_Avoid_: Checkout, reservation

**Demo request**: A prototype trip-planning submission accepted by the server route and sent through Resend to a controlled recipient.
_Avoid_: Booking, confirmed itinerary

**Draft**: The privacy-conscious `localStorage` record used to restore incomplete Plan My Trip progress after refresh or equivalent-language route switching.
_Avoid_: Account, saved trip

**Foundational token system**: The complete centrally defined reusable visual foundation from `docs/04_design`—primitive and semantic colors, typography, spacing, layout, shape, elevation, motion, focus, and shared states—mapped through Tailwind CSS v4. It excludes unused component implementations and speculative component-specific APIs for the wider product.
_Avoid_: Full component library, theme object
