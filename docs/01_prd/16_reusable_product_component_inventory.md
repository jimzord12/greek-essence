## 16. Reusable Product Component Inventory

This inventory defines reusable **product-level building blocks**. It does not prescribe code structure, styling, or final component APIs.

### 16.1 Component Philosophy

Every reusable component must contribute to at least one of the following outcomes:

- comprehension;
- inspiration;
- trust;
- orientation;
- qualification;
- conversion.

Components should be reusable across appropriate page types, maintain consistent semantics, and support content variation without becoming visually or behaviorally inconsistent.

### 16.2 Global Components

#### C-01 Global Header

**Purpose:** Provide orientation, primary navigation, language access, and persistent access to `Plan My Trip`.

**Required content:** logo, primary navigation, primary CTA, mobile navigation control.  
**Optional content:** language switch, compact utility contact action.  
**Rules:** primary CTA remains visually dominant; navigation must not become crowded.

#### C-02 Global Footer

**Purpose:** Provide secondary navigation, contact options, legal access, language access, and business reassurance.

**Required content:** key navigation, contact information, legal links, copyright.  
**Optional content:** social links, partner references, newsletter when operationally justified.

#### C-03 Language Switcher

**Purpose:** Allow movement between equivalent English and Greek content.  
**Rules:** preserve page context where an equivalent translation exists; avoid sending users to the homepage unnecessarily.

#### C-04 Breadcrumbs

**Purpose:** Support orientation within destination, experience, and journey hierarchies.  
**Usage:** deeper content pages; not required on Home.

### 16.3 Narrative and Inspiration Components

#### C-05 Hero

**Purpose:** Establish page meaning, emotional tone, and primary action immediately.

**Variants:** home, destination, experience, journey, standard interior.  
**Required content:** clear heading, concise supporting proposition, relevant media, primary action where appropriate.  
**Rules:** must communicate substance without relying only on imagery.

#### C-06 Editorial Introduction

**Purpose:** Explain why the page matters and frame the content that follows.  
**Rules:** concise, specific, and useful; avoid generic destination copy.

#### C-07 Section Header

**Purpose:** Create consistent content hierarchy.  
**Required content:** title.  
**Optional content:** eyebrow, description, text link.

#### C-08 Rich Story Section

**Purpose:** Combine text and imagery to explain place, culture, service, or philosophy.  
**Variants:** image-left, image-right, full-width editorial.

#### C-09 Image Gallery

**Purpose:** Build anticipation and communicate a genuine sense of place.  
**Rules:** only approved and properly licensed media; meaningful captions where useful.

#### C-10 Quote or Editorial Highlight

**Purpose:** Emphasize a brand belief, destination insight, or service promise.  
**Rules:** must not resemble a customer testimonial unless it is one.

### 16.4 Discovery Components

#### C-11 Destination Card

**Purpose:** Help users identify and compare relevant destinations.  
**Required content:** destination name, image, concise differentiator, link.  
**Optional content:** traveler fit, experience tags.  
**Rules:** no price or availability treatment in the MVP.

#### C-12 Destination Collection

**Purpose:** Group priority or secondary destinations with clear editorial logic.  
**Variants:** featured, more-of-Greece, related destinations.

#### C-13 Experience Card

**Purpose:** Help users explore by travel style or desired outcome.  
**Required content:** experience name, benefit-led summary, imagery or iconography, link.

#### C-14 Journey Card

**Purpose:** Turn abstract inspiration into a credible route.  
**Required content:** journey title, route, duration, traveler type or mood, image, customization statement, link.  
**Optional content:** selected highlights.  
**Rules:** no live price or availability unless supported.

#### C-15 Route Summary

**Purpose:** Explain destination sequence and duration clearly.  
**Usage:** journey detail pages and relevant destination combinations.

#### C-16 Related Content Module

**Purpose:** Continue useful exploration among destinations, experiences, and journeys.  
**Rules:** relations should be editorially meaningful, not random.

### 16.5 Trust and Service Components

#### C-17 Brand Promise Module

**Purpose:** Summarize the emotional and practical value of Greek Essence.

#### C-18 How It Works

**Purpose:** Reduce uncertainty by explaining the planning relationship.  
**Expected steps:** tell us how you want to travel; meet the planner; receive a proposal; refine and prepare; travel with support.  
**Rules:** final wording must match real operations.

#### C-19 Trust Credentials Module

**Purpose:** Present approved hospitality experience, relationships, awards, or certifications.  
**Rules:** all claims require accurate attribution and permission.

#### C-20 Team or Founder Profile

**Purpose:** Humanize the new brand and demonstrate expertise.  
**Required content:** approved biography, role, image, relevant experience.

#### C-21 Service Benefit Grid

**Purpose:** Explain what users gain from the planning relationship.  
**Examples:** time saved, route coherence, trusted partners, personalization, support.

#### C-22 FAQ Accordion or List

**Purpose:** Resolve recurring uncertainty using approved answers.  
**Rules:** interaction pattern belongs to the Prototype Specification; content must be accurate and accessible.

### 16.6 Conversion Components

#### C-23 Primary CTA Block

**Purpose:** Connect page context to `Plan My Trip`.  
**Required content:** contextual heading, concise reassurance, primary action.  
**Optional content:** consultation secondary action.

#### C-24 Contact Options Module

**Purpose:** Present secondary contact channels.  
**Rules:** indicate monitored channels and expected availability where defined.

#### C-25 Multi-Step Trip Request

**Purpose:** Qualify travelers while maintaining momentum and clarity.  
**Required capabilities:** progress, preserved input, validation, consent, reliable submission, confirmation.

#### C-26 Short Contact Form

**Purpose:** Handle general questions that do not require full trip qualification.  
**Rules:** must not duplicate the trip-request form.

#### C-27 Submission Confirmation

**Purpose:** Acknowledge the request, explain next steps, and prevent a dead end.  
**Required content:** confirmation, expected next step, response-time commitment when defined.  
**Optional content:** consultation action and relevant inspiration.

### 16.7 Utility Components

#### C-28 Privacy and Consent Notice

**Purpose:** Explain data use at the point of collection and obtain required consent.

#### C-29 Status and Feedback Message

**Purpose:** Communicate validation, errors, loading, success, and unavailable states clearly.

#### C-30 Empty or Unavailable Content State

**Purpose:** Handle missing translations, unavailable journeys, or temporarily unsupported content without misleading the user.

### Key Decisions

- The component inventory defines product purpose and required content, not code implementation.
- Components must remain semantically consistent across pages.
- New components require a clear product purpose rather than merely a visual justification.

---
