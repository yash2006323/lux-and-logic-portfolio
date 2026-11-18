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

RED. Decision recorded 18 Nov: unapproved INR package/revision prices are removed and replaced with 'pricing on request'. The live Pages URL still publishes those prices, so the gate stays red until WEBDEV's branch (built from CMO's copy v0.1) is merged and CI passes. Case studies must render only as a labelled 'coming soon' panel until the user supplies real wins.

## Re-gate checklist

1. WEBDEV branch merged to main with CMO copy v0.1 (no 'cinematic' copy, no price figures).
2. QA_GATE workflow green on main.
3. Live Pages URL re-checked against this checklist.
4. CTO signs off and posts the URL in the room; only then may outbound point at it.
