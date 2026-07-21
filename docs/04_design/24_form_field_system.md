## 24. Form Field System

### 24.1 Visual language

The trip-request form is calm, clear, human, and mobile-first. It should not resemble a banking application, government form, or SaaS onboarding wizard.

### 24.2 Field anatomy

- persistent label;
- optional indicator where relevant;
- helper text;
- control surface;
- prefix/suffix/icon only when helpful;
- validation message;
- character guidance where needed.

### 24.3 Standard dimensions

- minimum control height: 48 px;
- multiline minimum height: 128 px;
- radius: 10 px;
- horizontal padding: 14–16 px;
- vertical padding: 12–14 px;
- label-to-control gap: 8 px;
- control-to-helper/error gap: 8 px;
- field-group gap: 24 px;
- major form-section gap: 32–40 px.

### 24.4 Default field

- surface: ivory/white controlled surface;
- border: `input`;
- foreground: `foreground`;
- placeholder: muted foreground with adequate contrast;
- no heavy inset shadow.

### 24.5 Hover/focus

- hover: slightly stronger neutral border;
- focus: primary/neutral border plus 2 px teal ring and offset;
- label remains visible;
- focus must not shift layout.

### 24.6 Invalid

- destructive border;
- destructive icon where helpful;
- inline message in body-sm;
- error summary for multiple errors;
- helper text remains where still relevant;
- do not use red placeholder text as the only error.

### 24.7 Choice cards and chips

Choice cards:

- 1 px soft border;
- 12 px radius;
- 16–20 px padding;
- selected state uses accent tint, stronger border, check mark;
- hover uses subtle surface;
- full control remains keyboard accessible.

Chips:

- pill radius;
- 36–44 px minimum height depending on context;
- selected check/icon;
- wrapping layout;
- avoid excessively small tag clouds.

### 24.8 Date fields

- use locale-appropriate presentation;
- calendar trigger is labeled;
- manual input remains understandable where supported;
- estimated/flexible date state is visually clear;
- date errors appear near the group;
- no ambiguous placeholder-only format.

### 24.9 Conditional child ages

- reveal beneath children count with clear group heading;
- maintain stable spacing;
- use numbered labels such as `Child 1 age`;
- avoid horizontal overflow;
- removal confirmation only when values would be discarded.

### 24.10 Budget and privacy

- budget helper text has normal readable contrast;
- privacy acknowledgement is a distinct checkbox group;
- optional marketing consent is separated and unchecked;
- legal links are visible and descriptive;
- no visual pressure or preselection.

---


