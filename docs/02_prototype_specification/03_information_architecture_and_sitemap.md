## 3. Information Architecture and Sitemap

### 3.1 MVP sitemap

```text
Home
├── Destinations
│   ├── Athens
│   ├── Paros & Antiparos
│   ├── Mykonos
│   ├── Santorini
│   └── More of Greece
│       ├── Naxos
│       ├── Milos
│       ├── Syros
│       ├── Crete
│       ├── Peloponnese
│       └── Meteora & Delphi
├── Experiences
│   ├── Tailor-Made Greece
│   ├── Island Hopping
│   ├── Honeymoons & Romantic Travel
│   ├── Family Travel
│   ├── Culture & Gastronomy
│   └── VIP Concierge & Travel Planning
├── Journeys
│   ├── Sample / Signature Itineraries
│   └── Multi-Destination Greece
├── About
│   ├── Brand Story
│   ├── Local Expertise & Hospitality Network
│   └── How We Plan Your Trip
├── FAQ
├── Contact
├── Plan My Trip / Request a Custom Itinerary
└── Legal
    ├── Privacy Policy
    ├── Cookie Information
    └── Terms / Travel Conditions, when approved
```

`How It Works` is a reusable content pattern and may not require a dedicated MVP route. Secondary destinations may be sections or anchored entries within `More of Greece` until page-quality content exists.

### 3.2 Primary navigation

The main navigation contains, in order:

1. Destinations
2. Experiences
3. Journeys
4. About
5. FAQ
6. `Plan My Trip` as the visually distinct primary action

Contact and language access remain available through utility or footer navigation. Contact must not compete as an equal main-navigation destination.

### 3.3 Navigation behavior

- The logo always returns to Home and has an accessible text alternative.
- The current top-level section is visibly and non-color-dependently indicated.
- Destinations, Experiences, and Journeys may expose a curated submenu on wide viewports; it must not become a dense mega-menu.
- Submenus open by explicit activation, remain keyboard operable, communicate expanded state, and close with Escape, outside activation, or navigation.
- A submenu must include an `View all…` route before or after selected featured links.
- The header may transition from transparent-over-media to a solid surface only when contrast remains reliable. Content meaning and CTA access must not depend on this effect.
- A sticky header is permitted after initial scroll; it should become compact and must not obscure anchor targets or consume disproportionate mobile height.

### 3.4 Mobile menu

- At compact widths, primary navigation is replaced by a clearly labeled menu control.
- Opening the menu presents a full-height or near-full-height navigation surface with the current page, language choice, and `Plan My Trip` visible without requiring deep scrolling.
- Nested groups expand inline rather than opening hover-dependent flyouts.
- Background page interaction is suspended while the menu is open.
- Focus moves into the menu on open, remains within it, and returns to the trigger on close.
- Menu state closes after successful navigation and on Escape.

### 3.5 Breadcrumbs

Breadcrumbs appear on destination, experience, journey, More of Greece detail, and legal pages where hierarchy aids orientation. They:

- begin with Home;
- end with the current page as non-interactive text;
- remain concise and horizontally scroll or wrap cleanly on compact screens;
- appear before the page title or immediately below the header;
- never replace a clear page heading.

### 3.6 Language switching

- English and Greek are presented as text labels (`EN` / `EL` or full language names), not flags.
- The current language is evident without relying only on color.
- Switching preserves the equivalent page and, where practical, the relevant form step and entered non-sensitive data.
- If an equivalent translation is unavailable, the user sees an honest localized unavailable state with actions to stay in the current language, visit the translated parent page, or return to Home. Silent redirection is prohibited.
- The control remains available in the wide header, mobile menu, and footer.
- Greek text expansion and different line lengths must not break hierarchy, controls, or cards.

### 3.7 Footer

The footer contains:

- concise brand statement;
- Destinations, Experiences, Journeys, About, FAQ, Contact, and Plan My Trip links;
- monitored email, WhatsApp, phone, and Viber only if approved;
- language access;
- Privacy, Cookie Information, and approved Terms / Travel Conditions;
- copyright and business identification required by approved legal content;
- optional approved social links and attributed partner references.

Newsletter controls must not appear until a genuine recurring content and consent strategy exists.

---

