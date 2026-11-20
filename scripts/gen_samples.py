#!/usr/bin/env python3
"""Generate clearly-labelled concept sample pages for Lux and Logic.

Every page is a CONCEPT DEMO, not client work: no client names, no results,
no prices. Output lands in concepts/ so the QA gate checks it.
"""
from pathlib import Path
import html
from urllib.parse import quote as urlquote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "concepts"
BASE = "/lux-and-Logic.github.io/concepts"
MAIL = "syashvardhan00714@gmail.com"
LABEL = "Concept sample — not client work"

NICHES = [
    dict(slug="cafe", niche="Café", accent="#9a3412", accent2="#ea580c", bg="#fff7ed",
         headline="A warm first impression, before the first sip.",
         lede="A concept for a neighbourhood café: the day's menu, seasonal specials and a clear path to book a table, with motion that suggests warmth rather than noise.",
         feature="Built for the morning rush",
         cards=["Menu and specials that update without a developer",
                "Tap-to-call and map directions above the fold",
                "Gentle motion that keeps the focus on the coffee"]),
    dict(slug="salon", niche="Salon", accent="#9d174d", accent2="#db2777", bg="#fdf2f8",
         headline="Bookings that feel as good as the service.",
         lede="A concept for a salon and spa: services, stylists and availability made simple, with a calm visual rhythm that puts the client at ease.",
         feature="A calmer way to book",
         cards=["Service menu with clear, plain-language descriptions",
                "Appointment request in a couple of taps",
                "Soft transitions that echo the treatment room"]),
    dict(slug="bakery", niche="Bakery", accent="#b45309", accent2="#f59e0b", bg="#fffbeb",
         headline="Fresh daily. Beautiful online.",
         lede="A concept for a bakery: what is in the case today, a pre-order path and opening hours, with motion that feels like the start of a good morning.",
         feature="Made for the daily bake",
         cards=["Today's bakes featured first",
                "Pre-order without a phone tree",
                "Warm palette with restrained animation"]),
    dict(slug="boutique", niche="Boutique retail", accent="#4338ca", accent2="#7c3aed", bg="#f5f3ff",
         headline="A storefront that matches the collection.",
         lede="A concept for an independent boutique: lookbooks, new arrivals and a simple enquiry path, with editorial motion that gives the pieces room to breathe.",
         feature="Editorial by default",
         cards=["Lookbook-style layout for each collection",
                "New arrivals with lightweight reveals",
                "Enquiry button always within reach"]),
    dict(slug="fitness", niche="Fitness studio", accent="#b91c1c", accent2="#f43f5e", bg="#fef2f2",
         headline="Energy that signs up members.",
         lede="A concept for a fitness studio: classes, coaches and a trial-class request, with punchy motion that carries the energy of a session without slowing the page.",
         feature="Built around the first class",
         cards=["Class timetable that is easy to scan",
                "Trial-class request in one short step",
                "Confident motion with a fast first paint"]),
    dict(slug="dental", niche="Dental clinic", accent="#0f766e", accent2="#14b8a6", bg="#f0fdfa",
         headline="Calm, clear, and easy to book.",
         lede="A concept for a dental clinic: treatments, reassurance and appointment requests, with slow, steady motion designed to lower the temperature.",
         feature="Reassurance before the visit",
         cards=["Treatment pages in plain language",
                "Appointment request with clear next steps",
                "Low-key motion that never startles"]),
    dict(slug="realestate", niche="Real estate", accent="#1d4ed8", accent2="#0ea5e9", bg="#eff6ff",
         headline="Listings that deserve a better frame.",
         lede="A concept for a property team: featured listings, neighbourhood guides and viewing requests, with smooth reveals that let the photography do the work.",
         feature="Let the property lead",
         cards=["Listing grid with a strong image treatment",
                "Viewing request on every listing",
                "Subtle depth, never at the cost of readability"]),
    dict(slug="homeservices", niche="Home services", accent="#c2410c", accent2="#f97316", bg="#fff7ed",
         headline="Trust before the first visit.",
         lede="A concept for a home-services company: services covered, areas served and a quote request, with direct motion that gets to the point.",
         feature="Clear from the first scroll",
         cards=["Services and areas up front",
                "Quote request that takes very little time",
                "Direct animation with no empty flourishes"]),
    dict(slug="photography", niche="Photography studio", accent="#7e22ce", accent2="#a855f7", bg="#faf5ff",
         headline="Your work, given the stage it deserves.",
         lede="A concept for a photography studio: galleries, session types and an enquiry path, with slow fades and generous space around every frame.",
         feature="A gallery first, a website second",
         cards=["Wide galleries with light reveals",
                "Session types explained simply",
                "Dark presentation with strong contrast"]),
    dict(slug="restaurant", niche="Restaurant", accent="#be123c", accent2="#e11d48", bg="#fff1f2",
         headline="The table is set. So is the site.",
         lede="A concept for a restaurant: the menu, the room and a reservation request, with motion that sets the mood without getting between the guest and the booking.",
         feature="From first look to reservation",
         cards=["Menu highlights above the fold",
                "Reservation request that is obvious",
                "Atmospheric motion that stays out of the way"]),
]

SECTIONS = {
    "cafe": [
        dict(title="On the menu", tag="Menu", intro="A layout for what is served today. Dishes and rates are supplied by the business.",
             items=[("Coffee & filter", "A short list with milk alternatives"), ("Bakes & pastries", "What is in the case this morning"), ("Seasonal special", "One rotating feature, kept simple")]),
        dict(title="Plan your visit", tag="Location", intro="The details a visitor needs before they walk in.",
             items=[("Opening hours", "Clear at a glance"), ("Find us", "Map link and directions"), ("Book a table", "One obvious next step")]),
    ],
    "salon": [
        dict(title="Price list", tag="Rates", intro="A ready-made layout for your rates. No figures are invented here — the salon supplies its own prices before publishing.",
             label="Placeholder · rates supplied by the salon",
             items=[("Cut & finish", "Rate supplied by the salon"), ("Colour", "Rate supplied by the salon"), ("Treatments", "Rate supplied by the salon")]),
        dict(title="Services", tag="Booking", intro="What is on offer, and how to book it.",
             items=[("Hair", "Services described in plain language"), ("Nails & beauty", "A second group of treatments"), ("Appointment request", "A short form with clear next steps")]),
    ],
    "bakery": [
        dict(title="Baked today", tag="Counter", intro="A place for the daily range, written and supplied by the bakery.",
             items=[("Bread", "The everyday loaves"), ("Pastries", "What comes out of the oven first"), ("Cakes", "Celebration and slice options")]),
        dict(title="Pre-orders", tag="Orders", intro="How a customer reserves ahead without a phone tree.",
             items=[("Choose your bakes", "A simple selection step"), ("Pick a date", "Collection day made clear"), ("Confirm", "One short confirmation form")]),
    ],
    "boutique": [
        dict(title="Collections", tag="Lookbook", intro="Editorial space for the pieces, with imagery supplied by the shop.",
             kind="showcase",
             items=[("New arrivals", "Photography supplied by the business"), ("Seasonal edit", "Photography supplied by the business"), ("Accessories", "Photography supplied by the business")]),
        dict(title="Visit us", tag="Store", intro="The practical details under the lookbook.",
             items=[("Opening hours", "When the door is open"), ("Location", "Map and directions"), ("Enquiry", "Ask about a piece")]),
    ],
    "fitness": [
        dict(title="Class timetable", tag="Schedule", intro="A scannable weekly layout, filled in by the studio.",
             items=[("Strength", "Session times and coaches"), ("Conditioning", "Session times and coaches"), ("Recovery", "Session times and coaches")]),
        dict(title="First class", tag="Join", intro="The route from interested to booked.",
             items=[("Try a session", "A single request step"), ("What to bring", "Answered before the visit"), ("Membership", "Options described plainly")]),
    ],
    "dental": [
        dict(title="Treatments", tag="Care", intro="Plain-language treatment pages with details supplied by the practice.",
             items=[("Check-ups", "What to expect at a visit"), ("Hygiene", "A simple explanation"), ("Cosmetic", "Options without jargon")]),
        dict(title="Your visit", tag="Booking", intro="Reassurance and a clear way to arrange an appointment.",
             items=[("Before you arrive", "What happens first"), ("Appointment request", "A short form"), ("Location & hours", "The practical details")]),
    ],
    "realestate": [
        dict(title="Property showcase", tag="Showcase", intro="Cards ready for your photography and listing details. No addresses, prices or results are invented.",
             kind="showcase",
             items=[("Featured home", "Photography and details supplied by the business"), ("New listing", "Photography and details supplied by the business"), ("Letting", "Photography and details supplied by the business")]),
        dict(title="Find a property", tag="Search", intro="A simple way for a visitor to narrow the search.",
             items=[("Location", "Areas covered"), ("Property type", "The main categories"), ("Viewing request", "One clear next step")]),
    ],
    "homeservices": [
        dict(title="Services covered", tag="Services", intro="What the team does, described by the business.",
             items=[("Installations", "Work type one"), ("Repairs", "Work type two"), ("Maintenance", "Work type three")]),
        dict(title="Areas & quotes", tag="Coverage", intro="Where the team works and how to get a quote.",
             items=[("Areas served", "Towns and neighbourhoods"), ("How it works", "The steps from call to visit"), ("Quote request", "A short form")]),
    ],
    "photography": [
        dict(title="Gallery", tag="Portfolio", intro="Wide space for the work, with all imagery supplied by the photographer.",
             kind="showcase",
             items=[("Portraits", "Photography supplied by the business"), ("Weddings", "Photography supplied by the business"), ("Products", "Photography supplied by the business")]),
        dict(title="Sessions", tag="Book", intro="How a client chooses and enquires.",
             items=[("Session types", "What each one includes"), ("What happens", "A simple timeline"), ("Enquiry", "A short contact form")]),
    ],
    "restaurant": [
        dict(title="The menu", tag="Menu", intro="A layout for courses and dishes. The restaurant supplies its own items and rates.",
             items=[("Starters", "A few seasonal options"), ("Mains", "The core of the menu"), ("Desserts", "A short, sweet finish")]),
        dict(title="Book a table", tag="Reservations", intro="The fastest route from browsing to a booking.",
             items=[("Date & time", "A simple selection"), ("Party size", "One short field"), ("Reservation request", "A clear confirmation step")]),
    ],
}

REVIEWS = dict(
    title="Reviews",
    tag="Feedback",
    intro="Placeholder — real customer feedback is added here by the business. No review is invented for these concept samples.",
    items=[("Review placeholder", "A real quote goes here once supplied"), ("Review placeholder", "A real quote goes here once supplied"), ("Review placeholder", "A real quote goes here once supplied")],
)

CSS = """\
:root{--accent:#4f46e5;--accent2:#7c3aed;--bg:#f7f8fb;--ink:#16181d}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit}
.skip{position:absolute;left:-9999px;top:0;background:var(--accent);color:#fff;padding:10px 16px;z-index:50;border-radius:0 0 8px 0}
.skip:focus{left:0}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:4px}
.topbar{display:flex;justify-content:space-between;align-items:center;gap:12px;max-width:1100px;margin:0 auto;padding:18px 20px}
.brand{text-decoration:none;font-weight:800;letter-spacing:-.02em}
.badge{background:rgba(0,0,0,.06);border:1px solid rgba(0,0,0,.09);padding:6px 12px;border-radius:999px;font-size:12px;font-weight:700}
.hero{position:relative;overflow:hidden;max-width:1100px;margin:0 auto;padding:64px 20px 88px;min-height:420px}
.orb{position:absolute;border-radius:50%;pointer-events:none;opacity:.4;animation:llFloat 14s ease-in-out infinite}
.orb-a{width:340px;height:340px;background:radial-gradient(circle at 30% 30%,var(--accent2),transparent 70%);top:-90px;right:-40px}
.orb-b{width:260px;height:260px;background:radial-gradient(circle at 70% 70%,var(--accent),transparent 70%);bottom:-70px;left:-30px;animation-delay:-6s}
@keyframes llFloat{0%,100%{transform:translate3d(0,0,0) scale(1)}50%{transform:translate3d(26px,-18px,0) scale(1.15)}}
.hero-mark{position:absolute;right:8%;top:70px;width:160px;height:160px;color:var(--accent);animation:llSpin 22s linear infinite;opacity:.85}
.hero-mark .pulse{animation:llPulse 3s ease-in-out infinite;transform-origin:center}
@keyframes llSpin{to{transform:rotate(360deg)}}
@keyframes llPulse{0%,100%{opacity:.25}50%{opacity:1}}
.eyebrow{position:relative;text-transform:uppercase;letter-spacing:.16em;font-size:12px;font-weight:800;color:var(--accent)}
h1{position:relative;font-size:clamp(2.2rem,5vw,4rem);line-height:1.06;letter-spacing:-.035em;max-width:17ch;margin:14px 0 18px}
.lede{position:relative;font-size:1.08rem;max-width:60ch;opacity:.82}
.actions{position:relative;display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.btn{display:inline-block;background:var(--accent);color:#fff;padding:13px 20px;border-radius:12px;text-decoration:none;font-weight:700;transition:transform .2s ease,box-shadow .2s ease}
.btn:hover{transform:translateY(-2px);box-shadow:0 12px 24px rgba(0,0,0,.16)}
.btn.ghost{background:transparent;color:var(--accent);border:2px solid var(--accent)}
.strip{background:var(--accent);color:#fff;overflow:hidden;padding:12px 0;transform:rotate(-1deg)}
.marquee{display:flex;width:max-content;animation:llMarquee 28s linear infinite}
.marquee span{padding:0 28px;font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;white-space:nowrap}
@keyframes llMarquee{to{transform:translateX(-50%)}}
.features,.gridwrap{max-width:1100px;margin:0 auto;padding:80px 20px}
h2{font-size:clamp(1.7rem,3.4vw,2.5rem);letter-spacing:-.025em;margin:0 0 10px}
.cards,.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin-top:28px}
.card{display:block;background:#fff;border:1px solid rgba(0,0,0,.07);border-radius:18px;padding:24px;box-shadow:0 8px 30px rgba(20,20,40,.05);text-decoration:none;transition:transform .25s ease,box-shadow .25s ease}
a.card:hover{transform:translateY(-6px);box-shadow:0 18px 40px rgba(20,20,40,.11)}
.card .num{color:var(--accent);font-weight:800;font-size:13px;letter-spacing:.1em}
.card h3{margin:10px 0 6px;font-size:1.06rem}
.card p{margin:0;opacity:.76;font-size:.95rem}
.cta{max-width:1100px;margin:0 auto 80px;padding:56px 28px;border-radius:24px;background:var(--ink);color:#fff;text-align:center}
.cta p{opacity:.78;max-width:55ch;margin:12px auto 24px}
.cta .btn{background:var(--accent2)}
.note{max-width:1100px;margin:0 auto;padding:0 20px 24px;font-size:14px;opacity:.75}
footer{border-top:1px solid rgba(0,0,0,.08);text-align:center;padding:26px 20px;font-size:13px;opacity:.72}
.niche{max-width:1100px;margin:0 auto;padding:0 20px 62px}
.niche h2{margin-bottom:6px}
.niche-intro{max-width:70ch;opacity:.78;margin:0 0 22px}
.tag{display:inline-block;font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}
.niche-grid,.showcase-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}
.niche-item{background:#fff;border:1px solid rgba(0,0,0,.07);border-radius:16px;padding:20px}
.niche-item h3,.showcase-card h3{margin:0 0 6px;font-size:1.02rem}
.niche-item p,.showcase-card p{margin:0;font-size:.92rem;opacity:.76}
.showcase-card{background:#fff;border:1px solid rgba(0,0,0,.07);border-radius:16px;overflow:hidden}
.showcase-art{height:150px;background:linear-gradient(135deg,var(--accent),var(--accent2));position:relative;opacity:.9}
.showcase-art span{position:absolute;left:12px;bottom:10px;color:#fff;font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}
.showcase-card .body{padding:18px}
.review-note{border-left:3px solid var(--accent);padding:10px 14px;background:rgba(0,0,0,.035);border-radius:0 10px 10px 0;margin-bottom:20px;font-size:14px;max-width:70ch}
.placeholder-tag{display:inline-block;background:rgba(0,0,0,.05);border:1px solid rgba(0,0,0,.1);border-radius:999px;padding:7px 13px;font-size:12px;font-weight:800;letter-spacing:.04em;margin:0 0 20px}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.8,.2,1)}
.reveal.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}.reveal{opacity:1;transform:none}}
"""

JS = """\
(function(){
  var items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    items.forEach(function(el){ el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  items.forEach(function(el, i){ el.style.transitionDelay = Math.min(i % 4, 3) * 70 + 'ms'; io.observe(el); });
})();
"""

MARK = """\
<svg class="hero-mark" viewBox="0 0 160 160" fill="none" aria-hidden="true">
  <circle cx="80" cy="80" r="62" stroke="currentColor" stroke-width="2" stroke-dasharray="4 12" opacity=".7"/>
  <circle class="pulse" cx="80" cy="80" r="42" stroke="currentColor" stroke-width="3"/>
  <rect x="70" y="70" width="20" height="20" rx="5" transform="rotate(45 80 80)" fill="currentColor" opacity=".55"/>
  <circle cx="80" cy="18" r="5" fill="currentColor"/>
</svg>
"""


def render_section(sec, uid, e):
    """Render one niche-specific block plus the shared reviews block."""
    items = sec["items"]
    if sec.get("kind") == "showcase":
        body = "\n".join(
            f'        <article class="showcase-card reveal"><div class="showcase-art" aria-hidden="true"><span>Photo placeholder</span></div>'
            f'<div class="body"><h3>{e(name)}</h3><p>{e(desc)}</p></div></article>'
            for name, desc in items
        )
        grid = "showcase-grid"
    else:
        body = "\n".join(
            f'        <article class="niche-item reveal"><h3>{e(name)}</h3><p>{e(desc)}</p></article>'
            for name, desc in items
        )
        grid = "niche-grid"
    note = ""
    if sec is REVIEWS:
        note = f'    <p class="review-note">{e(sec["intro"])}</p>\n'
        intro = "Reviews are shown as a labelled placeholder on every concept sample."
    else:
        intro = sec["intro"]
    return f"""  <section class="niche" id="{uid}" aria-labelledby="{uid}-title">
    <span class="tag">{e(sec['tag'])}</span>
    <h2 id="{uid}-title" class="reveal">{e(sec['title'])}</h2>
{note}    <p class="niche-intro reveal">{e(intro)}</p>
{f'    <p class="placeholder-tag reveal">{e(sec["label"])}</p>' + chr(10) if sec.get("label") else ''}    <div class="{grid}">
{body}
    </div>
  </section>
"""


def page(n):
    style = f"--accent:{n['accent']};--accent2:{n['accent2']};--bg:{n['bg']}"
    e = html.escape
    cards = "\n".join(
        f'        <article class="card reveal"><div class="num">DETAIL {i + 1}</div><h3>{e(c)}</h3>'
        f'<p>Part of this {e(n["niche"])} concept layout.</p></article>'
        for i, c in enumerate(n["cards"])
    )
    marquee = " · ".join([n["niche"], "Motion with purpose", "Clear next step", "Fast and accessible"] * 2)
    subject = urlquote(f"Website enquiry — {n['niche']} concept")
    all_sections = SECTIONS[n["slug"]] + [REVIEWS]
    sections = "\n".join(render_section(sec, f"{n['slug']}-{i}", e) for i, sec in enumerate(all_sections))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(n['niche'])} — {LABEL} | Lux and Logic</title>
<meta name="description" content="A {e(n['niche'])} concept website by Lux and Logic. {LABEL}.">
<link rel="icon" href="/lux-and-Logic.github.io/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{BASE}/assets/samples.css">
<noscript><style>.reveal{{opacity:1;transform:none}}</style></noscript>
</head>
<body style="{style}">
<a class="skip" href="#main">Skip to main content</a>
<header class="topbar">
  <a class="brand" href="{BASE}/">Lux and Logic · Samples</a>
  <span class="badge">{LABEL}</span>
</header>
<main id="main">
  <section class="hero" aria-labelledby="hero-title">
    <div class="orb orb-a" aria-hidden="true"></div><div class="orb orb-b" aria-hidden="true"></div>
    {MARK}
    <p class="eyebrow reveal">{e(n['niche'])} · web design concept</p>
    <h1 id="hero-title" class="reveal">{e(n['headline'])}</h1>
    <p class="lede reveal">{e(n['lede'])}</p>
    <div class="actions reveal">
      <a class="btn" href="mailto:{MAIL}?subject={subject}">Talk about your website</a>
      <a class="btn ghost" href="{BASE}/">Browse all samples</a>
    </div>
  </section>
  <div class="strip" aria-hidden="true"><div class="marquee"><span>{e(marquee)}&nbsp;</span><span>{e(marquee)}&nbsp;</span></div></div>
  <section class="features" aria-labelledby="feature-title">
    <h2 id="feature-title" class="reveal">{e(n['feature'])}</h2>
    <p class="lede reveal">A look at how this niche could be presented — structure, motion and a clear route to getting in touch.</p>
    <div class="cards">
{cards}
    </div>
  </section>
{sections}  <section class="cta">
    <h2>Want something like this for your business?</h2>
    <p>These are concept demos, not client projects. Tell us what you need and we will scope it with you.</p>
    <a class="btn" href="mailto:{MAIL}?subject={subject}">Email Lux and Logic</a>
  </section>
</main>
<footer>{LABEL} · Built by Lux and Logic. <a href="/lux-and-Logic.github.io/">Back to the main site</a></footer>
<script src="{BASE}/assets/samples.js"></script>
</body>
</html>
"""


def index():
    e = html.escape
    cards = "\n".join(
        f'      <a class="card reveal" style="--accent:{n["accent"]}" href="{BASE}/{n["slug"]}/">'
        f'<div class="num">SAMPLE {i + 1:02d}</div><h3>{e(n["niche"])}</h3>'
        f'<p>{e(n["headline"])}</p></a>'
        for i, n in enumerate(NICHES)
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Concept samples — Lux and Logic</title>
<meta name="description" content="Ten web design concept samples across ten different niches. Concept demos, not client work.">
<link rel="icon" href="/lux-and-Logic.github.io/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{BASE}/assets/samples.css">
<noscript><style>.reveal{{opacity:1;transform:none}}</style></noscript>
</head>
<body style="--accent:#4f46e5;--accent2:#7c3aed;--bg:#f7f8fb">
<a class="skip" href="#main">Skip to main content</a>
<header class="topbar">
  <a class="brand" href="/lux-and-Logic.github.io/">Lux and Logic</a>
  <span class="badge">Concept demos — not client work</span>
</header>
<main id="main">
  <section class="hero" aria-labelledby="hero-title">
    <div class="orb orb-a" aria-hidden="true"></div><div class="orb orb-b" aria-hidden="true"></div>
    {MARK}
    <p class="eyebrow reveal">Portfolio · concept work</p>
    <h1 id="hero-title" class="reveal">Ten niches. Ten starting points.</h1>
    <p class="lede reveal">A set of concept samples showing how a website could look and feel for different kinds of business. Each one is a demo: no client names, results or claims are shown.</p>
    <div class="actions reveal">
      <a class="btn" href="mailto:{MAIL}?subject=Website%20enquiry">Start a project enquiry</a>
      <a class="btn ghost" href="/lux-and-Logic.github.io/">Back to the main site</a>
    </div>
  </section>
  <section class="gridwrap" aria-labelledby="grid-title">
    <h2 id="grid-title" class="reveal">Browse the samples</h2>
    <p class="note" style="padding-left:0">Every page below is a concept sample, not client work.</p>
    <div class="grid">
{cards}
    </div>
  </section>
  <section class="cta">
    <h2>See something you like?</h2>
    <p>We can shape a real site around your business, your goals and your budget.</p>
    <a class="btn" href="mailto:{MAIL}?subject=Website%20enquiry">Email Lux and Logic</a>
  </section>
</main>
<footer>Concept demos — not client work · Lux and Logic</footer>
<script src="{BASE}/assets/samples.js"></script>
</body>
</html>
"""


def main():
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    (OUT / "assets" / "samples.css").write_text(CSS, encoding="utf-8")
    (OUT / "assets" / "samples.js").write_text(JS, encoding="utf-8")
    (OUT / "index.html").write_text(index(), encoding="utf-8")
    for n in NICHES:
        d = OUT / n["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(n), encoding="utf-8")
    print(f"Wrote {len(NICHES)} samples + index to {OUT}")


if __name__ == "__main__":
    main()
