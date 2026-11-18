#!/usr/bin/env python3
"""Lux and Logic pre-publish QA gate. Run locally: python3 scripts/qa_check.py"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TARGETS = sorted({p for pat in ("index.html", "out/**/*.html", "concepts/**/*.html") for p in ROOT.glob(pat) if p.is_file()})

PRICE = re.compile(r"(?:₹|\$|€|£)\s?\d|\b\d[\d,.]*\s*(?:INR|USD|EUR|GBP)\b", re.I)
PROOF = re.compile(r"(?i)(case stud(?:y|ies)|testimonial|\bwe (?:helped|grew|delivered)\b|\b\d+\s*%|\b\d+x\b)")
LABEL = re.compile(r"(?i)(coming soon|pending real client data|placeholder)")
IMG = re.compile(r"<img\b[^>]*>", re.I)

problems = []
if not TARGETS:
    problems.append("No HTML found (index.html, out/, concepts/).")

for path in TARGETS:
    text = path.read_text(encoding="utf-8", errors="ignore")
    body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", text, flags=re.I | re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    name = path.relative_to(ROOT).as_posix()
    if PRICE.search(body):
        problems.append(f"{name}: price/figure not approved by the user.")
    if PROOF.search(body) and not LABEL.search(body):
        problems.append(f"{name}: proof/result claim without a 'coming soon' or placeholder label.")
    if "<!doctype" not in text.lower():
        problems.append(f"{name}: missing doctype.")
    if not re.search(r"<html[^>]+lang=", text, re.I):
        problems.append(f"{name}: missing lang attribute (a11y).")
    if not re.search(r"name=[\"']viewport[\"']", text, re.I):
        problems.append(f"{name}: missing viewport meta (mobile/perf).")
    if not re.search(r"<h1\b", text, re.I):
        problems.append(f"{name}: missing h1 (semantics).")
    if any(not re.search(r"\balt=", tag, re.I) for tag in IMG.findall(text)):
        problems.append(f"{name}: image without alt text (a11y).")

if problems:
    print("QA GATE: FAIL")
    for item in problems:
        print(" -", item)
    sys.exit(1)

print(f"QA GATE: PASS ({len(TARGETS)} HTML file(s) checked)")
