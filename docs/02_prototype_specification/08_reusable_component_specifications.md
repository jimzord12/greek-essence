## 8. Reusable Component Specifications

The following specifications apply across page types. Each component must preserve its semantic purpose even when visual composition changes.

### 8.1 Global components (C-01–C-04)

#### Global Header (C-01)

**Purpose/content:** Logo, primary navigation, language access, primary CTA, and mobile menu control.  
**Variants:** Overlay, solid, compact sticky, mobile.  
**States:** Default, scrolled, menu/submenu open, current section, focus.  
**Responsive:** Full navigation only while labels and CTA fit without compression; otherwise use the mobile pattern.  
**Accessibility:** Landmark label, logical focus order, no hover-only access, 44 × 44 CSS-pixel target goal for touch controls.  
**Acceptance:** Navigation and CTA remain understandable at 200% zoom and with Greek labels.

#### Global Footer (C-02)

**Purpose/content:** Secondary navigation, contact, language, legal access, reassurance.  
**Variants:** Full and compact form/confirmation footer.  
**States:** Channel available/unavailable.  
**Responsive:** Multi-column becomes grouped single-column sections without hiding links.  
**Accessibility:** Descriptive group headings; contact labels include channel and value.

#### Language Switcher (C-03)

**Purpose/content:** Move between equivalent English and Greek context.  
**Variants:** Header, mobile menu, footer.  
**States:** Current, alternate, unavailable equivalent.  
**Acceptance:** Never uses flags or silently loses page context.

#### Breadcrumbs (C-04)

**Purpose/content:** Show hierarchy on deeper content.  
**States:** Standard and compact overflow.  
**Accessibility:** Navigation label; current item marked semantically; separators ignored by assistive technology.

### 8.2 Narrative and inspiration (C-05–C-10)

#### Hero (C-05)

**Variants:** Home immersive; destination; experience; journey with metadata; standard interior.  
**Required:** One page heading, concise proposition, relevant media, primary action where appropriate.  
**States:** Image loaded, image pending, image unavailable, optional video paused/playing.  
**Rules:** Text remains useful without media; one H1; contrast is robust across crops; no essential autoplay.  
**Responsive:** Art-directed crop and content-safe focal area; action stack on compact.

#### Editorial Introduction (C-06)

**Required:** Specific framing, optional short lead, optional fact/fit cues.  
**Rules:** Not a second hero; avoid generic promotional prose; readable text measure.

#### Section Header (C-07)

**Required:** Heading; optional eyebrow, description, and one related link.  
**Variants:** Centered, left editorial, compact.  
**Accessibility:** Heading level follows page outline rather than visual size.

#### Rich Story Section (C-08)

**Variants:** Image left/right, full-width editorial, text-led.  
**Rules:** Alternation supports narrative pacing, not arbitrary decoration. Stacked order remains logical.

#### Image Gallery (C-09)

**Variants:** Editorial grid, compact strip, optional modal viewer.  
**States:** Loaded, progressive loading, unavailable item, viewer open.  
**Rules:** Captions identify place/context when useful; no auto-advancing carousel.  
**Accessibility:** Labeled controls, keyboard navigation, focus management, meaningful alternatives.

#### Quote / Editorial Highlight (C-10)

**Variants:** Brand belief, planner insight, destination fact.  
**Rules:** Attribution shown when quoting a person/source; styling must not imply traveler testimony unless verified.

### 8.3 Discovery (C-11–C-16)

#### Destination Card (C-11)

**Required:** Accurate image, destination name, concise differentiator, destination link.  
**Optional:** Fit cues and experience tags.  
**Variants:** Featured, standard, compact related.  
**States:** Default, hover/focus, image unavailable, content unavailable.  
**Rules:** Whole-card activation may be used if nested links are avoided; no price/availability badges.  
**Acceptance:** A user can distinguish cards without relying on imagery alone.

#### Destination Collection (C-12)

**Variants:** Priority, More of Greece, related.  
**Rules:** Section heading explains editorial logic; priority is evident through order and presentation.

#### Experience Card (C-13)

**Required:** Experience name, traveler outcome, relevant media/icon, link.  
**Variants/states:** Featured, standard, related; unavailable content omitted.  
**Rules:** Outcome-led, not an inventory item.

#### Journey Card (C-14)

**Required:** Title, route, duration, traveler/mood cue, image, customization statement, link.  
**Optional:** Selected highlights.  
**Variants:** Featured, standard, related.  
**Rules:** No fixed-price, availability, booking, or package treatment.

#### Route Summary (C-15)

**Required:** Ordered destinations and duration/allocation where approved.  
**Variants:** Compact card route, detailed horizontal, detailed vertical.  
**Accessibility:** Ordered textual sequence; visual line is decorative support.

#### Related Content Module (C-16)

**Required:** Descriptive section heading and two to four editorially relevant items.  
**States:** Populated; single recommendation; none—omit module rather than show an empty grid.  
**Rules:** Explain relationship through labels or summaries; no random recommendations.

### 8.4 Trust and service (C-17–C-22)

#### Brand Promise (C-17)

Combines emotional promise, practical value, and reason to believe. Variants are compact and editorial. It must avoid unsupported claims.

#### How It Works (C-18)

Uses numbered, plainly labeled steps with concise descriptions. Variants are 3-step summary and approved 5-step full process. It must not imply automation or commitments absent from operations.

#### Trust Credentials (C-19)

**Required per item:** Claim/credential, owning entity, relationship to Greek Essence, source where appropriate, and approved mark only with permission.  
**Variants:** Hospitality background narrative, relationship list, attributed credentials.  
**States:** Approved; pending items remain absent from public prototype screens.  
**Acceptance:** No reasonable user could attribute a related entity’s award/review to Greek Essence.

#### Team / Founder Profile (C-20)

Includes approved portrait, full name, role, concise relevant biography, and optional specific expertise. Avoids inflated credentials. Compact and expanded variants must retain identity and accountability.

#### Service Benefit Grid (C-21)

Explains outcomes such as saved time, coherent routing, trusted relationships, personalization, and support. Three to five items are preferred; each uses a clear heading and short explanation.

#### FAQ Accordion / List (C-22)

Uses an accessible disclosure pattern. Deep links to questions may be supported. Motion is brief and non-essential. Answers containing legal/commercial facts require approval.

### 8.5 Conversion and utility (C-23–C-30)

#### Primary CTA Block (C-23)

Includes contextual heading, concise reassurance, `Plan My Trip`, and optional lower-emphasis consultation action. Variants reflect destination, experience, journey, general brand, and form recovery contexts.

#### Contact Options (C-24)

Shows only monitored channels, with recognizable labels, availability/service hours where approved, and expected behavior. Direct channels remain secondary to the trip request.

#### Multi-Step Trip Request (C-25)

Specified fully in §9. It includes progress, step content, preserved values, navigation, consent, validation, submission, recovery, and confirmation.

#### Short Contact Form (C-26)

Uses persistent labels, clear optional markers, concise privacy context, and explicit submit language. It does not request trip qualification fields.

#### Submission Confirmation (C-27)

Uses an unambiguous heading, next step, timing when approved, correction route, and optional onward content. It appears only after confirmed success.

#### Privacy and Consent Notice (C-28)

Explains purpose at the point of collection, links to the Privacy Policy, separates required acknowledgement from optional communications consent, and never uses preselected optional consent.

#### Status and Feedback Message (C-29)

**Variants:** Informational, validation warning, recoverable error, blocking error, loading/submitting, and success.  
**Rules:** Uses icon, heading/label, message, and recovery action as needed; meaning is not color-only; status announcements are timely but not repetitive.

#### Empty / Unavailable Content State (C-30)

Explains what is unavailable, avoids blame, preserves language/context, and provides one or two relevant routes. It never invents substitute content or shows a broken empty shell.

---

