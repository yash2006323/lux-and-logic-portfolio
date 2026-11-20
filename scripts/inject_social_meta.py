#!/usr/bin/env python3
"""Add CMO-approved Open Graph / Twitter card metadata to built HTML.

Idempotent: pages that already declare og:title are left untouched.
Usage: python3 scripts/inject_social_meta.py <repo-root> [<repo-root> ...]
"""
import pathlib
import re
import sys

BASE = "https://yash2006323.github.io/lux-and-Logic.github.io"
HOME_TITLE = "Lux and Logic — Websites that ship on time, load fast, and convert"
HOME_DESC = (
    "Fast, accessible websites on one standardised stack, with a written QA gate. "
    "First site ₹25,000 payable on handover — nothing upfront, no lock-in."
)
NICHES = {
    "cafe": "Café", "salon": "Salon", "bakery": "Bakery", "boutique": "Boutique retail",
    "fitness": "Fitness studio", "dental": "Dental clinic", "realestate": "Real estate",
    "homeservices": "Home services", "photography": "Photography studio",
    "restaurant": "Restaurant",
}
LABEL = "Concept demo — not client work"


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def block(url, title, desc, image, alt):
    t, d, a = esc(title), esc(desc), esc(alt)
    lines = [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Lux and Logic">',
        f'<meta property="og:url" content="{esc(url)}">',
        f'<meta property="og:title" content="{t}">',
        f'<meta property="og:description" content="{d}">',
        f'<meta property="og:image" content="{esc(image)}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{a}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{t}">',
        f'<meta name="twitter:description" content="{d}">',
        f'<meta name="twitter:image" content="{esc(image)}">',
        f'<meta name="twitter:image:alt" content="{a}">',
    ]
    return "<!-- Social share metadata (CMO-approved v0.3 copy) -->\n" + "\n".join(lines) + "\n"


def canonical(text, fallback):
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', text, re.I)
    if m:
        return m.group(1)
    m = re.search(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', text, re.I)
    return m.group(1) if m else fallback


def process(path, root, changed):
    text = path.read_text(encoding="utf-8")
    if 'property="og:title"' in text:
        return
    rel = path.relative_to(root).as_posix()
    if rel == "index.html" or rel == "out/index.html":
        url = BASE + "/"
        title, desc = HOME_TITLE, HOME_DESC
        image, alt = BASE + "/og/home.png", HOME_TITLE
        # Align the on-page title/description with the approved copy on home.
        text = re.sub(r"<title>.*?</title>", f"<title>{esc(HOME_TITLE)}</title>", text, count=1, flags=re.I | re.S)
        text = re.sub(
            r'<meta name="description" content="[^"]*">',
            f'<meta name="description" content="{esc(HOME_DESC)}">',
            text, count=1, flags=re.I,
        )
    elif rel in ("concepts/index.html", "out/concepts/index.html"):
        url, image = canonical(text, BASE + "/concepts/"), BASE + "/og/samples.png"
        title = "Concept samples — Lux and Logic"
        desc = "Ten labelled web design concept samples across ten niches. " + LABEL + "."
        alt = "Ten labelled web design concept samples — " + LABEL
    else:
        m = re.search(r"concepts/([^/]+)/index\.html$", rel)
        slug = m.group(1) if m else "sample"
        niche = NICHES.get(slug, slug.replace("-", " ").title())
        url = canonical(text, f"{BASE}/concepts/{slug}/")
        title = f"{niche} website concept — Lux and Logic"
        desc = f"{LABEL}. See how a {niche} website could look, with clear next steps and accessible motion."
        image, alt = f"{BASE}/og/{slug}.png", f"{LABEL}: {niche} website preview"
    meta = block(url, title, desc, image, alt)
    if "</head>" in text:
        text = text.replace("</head>", meta + "</head>", 1)
    else:
        text = text.replace("</html>", meta + "</html>", 1)
    path.write_text(text, encoding="utf-8")
    changed.append(rel)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: inject_social_meta.py <repo-root> [<repo-root> ...]")
    for raw in sys.argv[1:]:
        root = pathlib.Path(raw).resolve()
        targets = [root / "index.html", root / "out/index.html", root / "concepts/index.html"]
        targets += sorted(root.glob("concepts/*/index.html"))
        changed = []
        for p in targets:
            if p.is_file():
                process(p, root, changed)
        print(f"{root}: updated {len(changed)} page(s)")
        for c in changed:
            print("  -", c)


if __name__ == "__main__":
    main()
