# Portfolio QA gate

Owner: CTO. Nothing points live outbound at this site until every line is green.

## Automated (every PR and push to main)

- No unapproved prices or commercial figures in rendered page copy.
- Complete HTML document(s) in `index.html` and/or `out/**/*.html`.

## Manual before sign-off

- Locked stack only: TypeScript + Next.js/React + Tailwind, static export; no paid services.
- CI green; one reviewer who is not the author; `main` not directly written.
- Accessibility basics (semantics, contrast, keyboard paths) and performance basics checked.
- Proof points are either user-supplied real wins or clearly labelled placeholders; no invented names, metrics or testimonials.
- Message matches the approved CMO story; README has run and deploy steps.

## Current status

RED. The existing `index.html` publishes package prices (INR figures) and revision rates that the user has not approved. @CEO / @user must decide: approve, remove, or replace with a pricing-on-request line. WEBDEV rebuild should land on a branch from the CMO story, not overwrite `main`.
