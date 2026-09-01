# Frontend Experience and Performance

## Design before code

Define information architecture, primary journeys, route boundaries, rendering strategy, state ownership, API contracts, accessibility, responsive behavior, and analytics.

For every data-dependent surface design loading, empty, success, partial, validation error, permission denied, offline, timeout, and unexpected error states.

## Defaults

- Prefer server rendering and Server Components.
- Add client boundaries only for interaction or browser APIs.
- Keep local state local; use URL state for shareable navigation and filters.
- Dynamically load heavy optional interfaces.
- Optimize images and fonts.
- Keep secrets and privileged data on the server.
- Test keyboard, screen-reader, touch, and small-screen flows.

## Performance budgets

- LCP below 2.5 seconds at p75
- INP below 200 milliseconds at p75
- CLS below 0.1
- Explicit JavaScript, image, and API p95 budgets

## Exit gate

- [ ] All user-visible states exist.
- [ ] Keyboard and mobile journeys work.
- [ ] Client JavaScript has a documented reason.
- [ ] Errors are actionable and safe.
- [ ] Analytics exclude sensitive data.
- [ ] Core Web Vitals and bundle size are measured.
- [ ] Critical journeys have end-to-end coverage.
