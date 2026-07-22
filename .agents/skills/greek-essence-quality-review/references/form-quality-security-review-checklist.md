# Form quality and security review checklist

Read the relevant sections before review:

- [PRD offer and service definition](../../../../docs/01_prd/11_offer_and_service_definition.md) and [MVP acceptance criteria](../../../../docs/01_prd/31_mvp_acceptance_criteria.md)
- [Prototype custom-trip form interaction specification](../../../../docs/02_prototype_specification/09_custom_trip_form_interaction_specification.md) and [prototype flows and scenarios](../../../../docs/02_prototype_specification/13_prototype_flows_and_scenarios.md)
- [Technical Design custom-trip form design and architecture](../../../../docs/03_technical_design/10_custom_trip_form_design_and_architecture.md), [short contact form and direct contact](../../../../docs/03_technical_design/11_short_contact_form_and_direct_contact.md), [privacy, consent, and security](../../../../docs/03_technical_design/12_privacy_consent_and_security.md), and [error, loading, empty, unavailable, and success states](../../../../docs/03_technical_design/15_error_loading_empty_unavailable_and_success_states.md)
- [Design QA workflow](../../../../docs/04_design/40_workflow.md)

When affected, use Playwright CLI evidence to exercise navigation into the flow, context, keyboard and focus, validation, error summaries, loading, success, unavailable/failure, confirmation, and honest no-booking/no-availability representation. Do not include personal data in evidence.
