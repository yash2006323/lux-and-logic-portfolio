# Lux and Logic — Portfolio site

Static marketing site built from **CMO — Portfolio Story v0.1**. All proof points are
clearly labelled placeholders; there are no client names, figures, or prices, and no
outbound points at this site until the site owner supplies real wins and the CTO
signs off the gate.

## Stack

TypeScript · Next.js (App Router, static export) · React · Tailwind CSS.
No runtime services, no database, no paid tooling. Hosted on free GitHub Pages.

## Run locally

```bash
npm install
npm run dev      # http://localhost:3000
```

## Build the static export

```bash
npm run build    # writes the export to out/
```

The committed site at the repository root (`index.html`, `_next/`, `404.html`,
`.nojekyll`) is the `out/` export copied to root so GitHub Pages' legacy
`main:/` source serves it directly. `basePath` is `/lux-and-logic-portfolio` so
asset URLs resolve on the project Pages subpath. To refresh the published root
after a source change:

```bash
npm run build
cp out/index.html index.html
cp out/404.html 404.html
rm -rf _next && cp -R out/_next ./_next
```

## Deploy

No deploy job required: push to `main` and GitHub Pages serves the root files.
(CTO's additive `qa-gate` workflow runs on PRs and pushes to `main`.)

## QA gate

```bash
npm run qa       # python3 scripts/qa_check.py
```

Gate passes when there are no unapproved commercial figures and every target is a
complete HTML document. Manual sign-off (a11y, contrast, keyboard paths, reviewer,
real-or-labelled proof) stays with the CTO per `QA_GATE.md`.

## Content owner

CMO owns the story and tone. WEBDEV owns the build. Replace the labelled
placeholder proof panel only with real, owner-supplied client data.
