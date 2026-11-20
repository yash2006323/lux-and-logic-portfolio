#!/usr/bin/env python3
"""Generate the CMO-approved 1200x630 social share cards (home + 10 demos + index).

Usage: python3 scripts/gen_og_images.py <output-dir>
Purely local: real system fonts, approved copy only, no client proof, no prices
on demo cards. The Swift renderer is scripts/gen_og_images.swift.
"""
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from gen_samples import NICHES  # single source of truth for accents and niche names

INDIGO, VIOLET = "#4F46E5", "#7C3AED"

cards = [
    dict(out="home.png", kicker="Lux and Logic",
         title="Websites that ship on time,\nload fast, and convert",
         sub="Fast, accessible websites on one standardised stack, with a written QA gate.",
         chip="FIRST SITE Rs 25,000 · PAYABLE ON HANDOVER",
         accent=INDIGO, accent2=VIOLET, demo=False),
    dict(out="samples.png", kicker="Lux and Logic",
         title="Ten niches. Ten starting points.",
         sub="Labelled web design concept samples — concept demos, not client work.",
         chip="CONCEPT SAMPLES — NOT CLIENT WORK",
         accent=INDIGO, accent2=VIOLET, demo=True),
]
for n in NICHES:
    cards.append(dict(
        out=f"{n['slug']}.png",
        kicker="Lux and Logic",
        title=f"{n['niche']} website concept",
        sub="A labelled design demo — clear next steps, accessible motion, no client work.",
        chip="LUX AND LOGIC · CONCEPT SAMPLE",
        accent=n["accent"], accent2=n["accent2"], demo=True,
    ))


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: gen_og_images.py <output-dir>")
    out = pathlib.Path(sys.argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        manifest = pathlib.Path(tmp) / "og-manifest.json"
        manifest.write_text(json.dumps(cards, ensure_ascii=False), encoding="utf-8")
        subprocess.run(
            ["swift", str(ROOT / "scripts" / "gen_og_images.swift"), str(manifest), str(out)],
            check=True,
        )
    print(f"Generated {len(cards)} cards in {out}")


if __name__ == "__main__":
    main()
