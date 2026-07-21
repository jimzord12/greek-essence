## 18. Custom Trip Request Product Requirements

### 18.1 Product Objective

The trip-request experience is the MVP's primary conversion product. It must capture enough information to qualify a request while feeling personal, manageable, and appropriate for mobile use.

### 18.2 Form Structure

The recommended structure is four concise steps.

#### Step 1 — Trip Basics

Required or conditionally required:

- desired destination or destinations;
- `Help me choose` option;
- estimated arrival and departure dates;
- date flexibility;
- approximate trip duration.

#### Step 2 — Travelers and Trip Type

- number of adults;
- number and ages of children when applicable;
- trip type: couple, honeymoon, family, friends, solo, other;
- first visit to Greece.

#### Step 3 — Preferences

- interests: beaches, culture, history, gastronomy, nightlife, nature, wellness, local life, luxury, relaxation, other;
- preferred pace: relaxed, balanced, active;
- accommodation preference if operationally useful;
- destinations or experiences already considered;
- optional additional preference context.

#### Step 4 — Budget and Contact

- approximate total trip budget or approved budget range;
- explicit explanation of whether international flights are included;
- full name;
- email;
- country of residence;
- phone or WhatsApp, optional unless business process requires it;
- preferred contact method;
- additional notes;
- required privacy acknowledgement or consent.

### 18.3 Functional Product Requirements

The form must:

- show progress and reasonable effort expectations;
- preserve entered data between steps;
- use plain-language labels and examples;
- explain why budget is requested;
- make optional fields visibly optional;
- validate without clearing valid input;
- work with keyboard and assistive technology;
- provide low-friction spam protection;
- capture relevant source and campaign information where legally appropriate;
- deliver the request reliably to the selected operational system;
- generate an accessible confirmation state;
- send an acknowledgement email if approved and operationally supported;
- explain what happens next;
- communicate the expected response window once defined.

### 18.4 Qualification Rules

The form should balance lead quality and completion. It should not require information the business does not actively use.

Budget may be required because it is central to trip feasibility, but the wording must explain that it helps create suitable recommendations rather than judge the traveler.

### 18.5 Validation and Error Requirements

- Errors must identify the problem and how to correct it.
- Valid input must remain intact after an error.
- Submission failures must not falsely show success.
- The user must have a safe way to retry.
- Duplicate submissions should be detectable or manageable operationally.

### 18.6 Confirmation Experience

After successful submission, the visitor must see:

- confirmation that the request was received;
- a summary of the next step;
- expected response timing when approved;
- a way to provide corrections or additional information;
- an optional consultation-booking action;
- relevant inspirational content or navigation.

### 18.7 Operational Ownership

Before launch, the business must define:

- destination system for requests;
- notification recipients;
- primary owner and backup owner;
- acknowledgement mechanism;
- lead status tracking;
- response-time commitment;
- failure monitoring and recovery;
- data retention and deletion rules.

### Key Decisions

- Multi-step structure is preferred over a single long form.
- The form is a qualification tool and must remain respectful and transparent.
- Reliable operational handling is part of the product requirement.

---

