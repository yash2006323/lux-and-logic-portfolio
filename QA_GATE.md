# Portfolio QA gate

Owner: CTO. Nothing points live outbound at this site until every line is green.

## Reproduce locally

`python3 scripts/qa_check.py` from the repo root (Python 3, no dependencies). The same check runs in GitHub Actions on every PR and push, on any base branch.

## Automated checks

- No unapproved prices or commercial figures in rendered copy (₹25,000 floor and ₹1,000/hr revisions are user-approved and pass).
- No proof/result claims unless clearly labelled 'coming soon' or placeholder.
- Complete HTML: doctype, lang, viewport, h1, alt on images.
- Scans index.html, 404.html, out/**/*.html and concepts/**/*.html.

## Manual before sign-off

- Static build on the locked stack; no paid services, no API.
- CI green; one reviewer who is not the author; `main` not directly written.
- Accessibility and performance basics checked by product UI/quality.
- Message matches CMO copy v0.1; README has run and deploy steps.

## Current status

GREEN on PR #2 (head 6787c6f, CTO re-check 2026-11-19): 4 HTML files — no unapproved prices/figures, proof claims labelled "Case studies coming soon", a11y basics OK, `concepts/` stripped from the branch.

Outstanding: the page does not yet show the user-approved pricing (₹25,000 first website, ₹1,000/hr revisions) — WEBDEV is to add it to PR #2; the gate treats those as approved when they land. The live Pages URL still publishes the old unapproved prices — it stays not-yet-green until merge + live recheck. Nothing points live outbound at this site until CTO sign-off.

## Re-gate checklist

1. PR #1 and PR #2 merged; no priced pages anywhere in the tree.
2. QA gate green on main and on the live Pages URL.
3. CTO re-checks the live URL and posts sign-off here.
4. Only then may outbound point at the site.
