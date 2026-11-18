# Portfolio QA gate

Owner: CTO. Nothing points live outbound at this site until every line is green.

## Reproduce locally

`python3 scripts/qa_check.py` from the repo root (Python 3, no dependencies). The same check runs in GitHub Actions on every PR and push, on any base branch.

## Automated checks

- No unapproved prices or commercial figures in rendered copy.
- No proof/result claims unless clearly labelled 'coming soon' or placeholder.
- Complete HTML: doctype, lang, viewport, h1, alt on images.
- Scans index.html, out/**/*.html and concepts/**/*.html.

## Manual before sign-off

- Static build on the locked stack; no paid services, no API.
- CI green; one reviewer who is not the author; `main` not directly written.
- Accessibility and performance basics checked by product UI/quality.
- Message matches CMO copy v0.1; README has run and deploy steps.

## Current status

RED. Decision recorded: unapproved INR prices are replaced with 'pricing on request'. PR #2 still contains `concepts/` with the original priced pages, so the gate fails. Strip `concepts/` from the PR, keep `main` untouched, then re-run the gate.

## Re-gate checklist

1. PR #1 and PR #2 merged; no priced pages anywhere in the tree.
2. QA gate green on main and on the live Pages URL.
3. CTO re-checks the live URL and posts sign-off here.
4. Only then may outbound point at the site.
