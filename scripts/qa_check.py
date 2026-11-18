#!/usr/bin/env python3
"""Lux and Logic pre-publish QA gate for the static portfolio.

Fails when the site contains an unapproved commercial figure or is not a
complete HTML document. No external dependencies; free to run anywhere.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "index.html"] + sorted((ROOT / "out").glob("**/*.html"))
TARGETS = [p for p in TARGETS if p.exists()]

PRICE = re.compile(r"(?:₹|\$|€|£)\s?\d|\b\d[\d,.]*\s*(?:INR|USD|EUR|GBP)\b", re.I)

problems = []
if not TARGETS:
    problems.append("No HTML found (expected index.html or out/**/*.html).")

for path in TARGETS:
    text = path.read_text(encoding="utf-8", errors="ignore")
    body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", text, flags=re.I | re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    if PRICE.search(body):
        problems.append(f"{path.name}: contains a price/figure the user has not approved.")
    if "<title>" not in text or "</html>" not in text:
        problems.append(f"{path.name}: not a complete HTML document.")

if problems:
    print("QA GATE: FAIL")
    for item in problems:
        print(" -", item)
    sys.exit(1)

print(f"QA GATE: PASS ({len(TARGETS)} HTML file(s) checked)")
