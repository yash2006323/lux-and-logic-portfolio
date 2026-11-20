const STAGES = [
  'Lead',
  'Qualify',
  'Scope & price',
  'Design + build',
  'QA',
  'Deliver',
  'Retro',
];

const SERVICES = [
  {
    title: 'Website builds',
    body: 'Fast, accessible sites on a standard, modern stack. Built to load quickly and work for everyone.',
  },
  {
    title: 'Conversion-focused design',
    body: 'The layout is shaped around what a visitor needs to do next, not just how it looks.',
  },
  {
    title: 'A predictable process',
    body: 'One Definition of Done, one QA gate, clear stages. You know what is happening and what comes next.',
  },
  {
    title: 'Support after launch',
    body: 'We stay on for maintenance and iteration. The relationship does not end at handover.',
  },
];

export default function Home() {
  return (
    <>
      <header className="sticky top-0 z-40 border-b border-line bg-canvas/90 backdrop-blur">
        <nav
          className="mx-auto flex max-w-5xl items-center justify-between px-5 py-4"
          aria-label="Primary"
        >
          <a href="#main" className="flex items-center gap-2 font-bold tracking-tight text-ink">
            <svg aria-hidden="true" width="22" height="22" viewBox="0 0 22 22" fill="none">
              <rect x="1" y="1" width="20" height="20" rx="5" stroke="#4f46e5" strokeWidth="2" />
              <path d="M6 15V7l5 5 5-5v8" stroke="#4f46e5" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            Lux and Logic
          </a>
          <div className="flex items-center gap-5 text-sm font-medium text-muted">
            <a className="hover:text-ink" href="#services">What we do</a>
            <a className="hidden hover:text-ink sm:inline" href="/lux-and-Logic.github.io/concepts/">Samples</a>
            <a className="hidden hover:text-ink sm:inline" href="#process">How we work</a>
            <a className="hidden hover:text-ink md:inline" href="#standards">Stack</a>
            <a className="rounded-lg bg-brand px-4 py-2 text-white hover:opacity-90" href="#contact">
              Book a fit call
            </a>
          </div>
        </nav>
      </header>

      <main id="main">
        {/* Hero */}
        <section className="relative mx-auto max-w-5xl overflow-hidden px-5 pb-16 pt-20 sm:pt-28" aria-labelledby="hero-title">
          <div className="ll-orb ll-orb-a" aria-hidden="true" />
          <div className="ll-orb ll-orb-b" aria-hidden="true" />
          <p className="ll-rise mb-4 text-sm font-semibold uppercase tracking-widest text-brand">
            A reliable web partner
          </p>
          <h1 id="hero-title" className="ll-rise ll-rise-2 max-w-3xl text-4xl font-extrabold leading-tight tracking-tight text-ink sm:text-6xl">
            Websites that are fast, accessible, and built to convert.
          </h1>
          <p className="ll-rise ll-rise-3 prose mt-6 text-lg text-muted">
            Lux and Logic builds on a standardised modern stack, ships predictably through a written
            QA gate, and stays on to maintain the site after launch — not just hand it over.
          </p>
          <div className="mt-8 flex flex-wrap items-center gap-4">
            <a className="rounded-xl bg-brand px-6 py-3 font-semibold text-white hover:opacity-90" href="#contact">
              Book a fit call
            </a>
            <a className="font-semibold text-ink underline decoration-line underline-offset-4 hover:decoration-brand" href="#services">
              See what we do
            </a>
            <a className="font-semibold text-brand underline decoration-line underline-offset-4 hover:decoration-brand" href="/lux-and-Logic.github.io/concepts/">
              See 10 concept samples
            </a>
          </div>
        </section>

        {/* What we do */}
        <section id="services" className="border-t border-line bg-white py-16" aria-labelledby="services-title">
          <div className="mx-auto max-w-5xl px-5">
            <h2 id="services-title" className="text-3xl font-bold tracking-tight text-ink">What we do</h2>
            <div className="mt-8 grid gap-6 sm:grid-cols-2">
              {SERVICES.map((s) => (
                <article key={s.title} className="rounded-2xl border border-line p-6">
                  <h3 className="text-lg font-bold text-ink">{s.title}</h3>
                  <p className="prose mt-2 text-muted">{s.body}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* Contract version — approved floor per CEO */}
        <section
          id="offers"
          className="mx-auto max-w-5xl px-5 py-16 border-t border-line bg-white"
          aria-labelledby="offers-title"
        >
          <h2 id="offers-title" className="text-3xl font-bold tracking-tight text-ink">Offers</h2>
          <p className="prose mt-3 text-muted">
            A first website is <strong>₹25,000</strong>, payable on handover — <strong>nothing upfront, no lock-in</strong>.
            Revisions after handover are <strong>₹1,000/hr</strong>. Flat offer — no extra change fees.
          </p>
        </section>

        {/* Proof */}
        <section className="py-16" aria-labelledby="proof-title">
          <div className="mx-auto max-w-5xl px-5">
            <h2 id="proof-title" className="text-3xl font-bold tracking-tight text-ink">Proof</h2>
            <p className="prose mt-3 text-muted">
              We are honest about what is ready. Real client results will appear here once supplied
              and approved.
            </p>
            <div className="mt-8 rounded-2xl border border-dashed border-line bg-white p-8 text-center">
              <p className="text-sm font-semibold uppercase tracking-widest text-brand">
                Case studies coming soon
              </p>
              <p className="prose mx-auto mt-3 text-muted">
                PLACEHOLDER — pending real client data. Client names, before-and-after results and
                testimonials will be added only when the site owner supplies them. Nothing here is a
                claim about past work.
              </p>
            </div>
          </div>
        </section>

        {/* How we work */}
        <section id="process" className="border-t border-line bg-white py-16" aria-labelledby="process-title">
          <div className="mx-auto max-w-5xl px-5">
            <h2 id="process-title" className="text-3xl font-bold tracking-tight text-ink">How we work</h2>
            <p className="prose mt-3 text-muted">
              A clear path from first contact to launch and beyond. Every stage has an owner and a
              written exit condition.
            </p>
            <ol className="mt-8 grid gap-3 sm:grid-cols-4">
              {STAGES.map((stage, i) => (
                <li key={stage} className="flex items-center gap-3 rounded-xl border border-line p-4">
                  <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-brand/10 text-sm font-bold text-brand" aria-hidden="true">
                    {i + 1}
                  </span>
                  <span className="font-medium text-ink">{stage}</span>
                </li>
              ))}
            </ol>
          </div>
        </section>

        {/* Stack & standards */}
        <section id="standards" className="py-16" aria-labelledby="standards-title">
          <div className="mx-auto max-w-5xl px-5">
            <h2 id="standards-title" className="text-3xl font-bold tracking-tight text-ink">Stack &amp; standards</h2>
            <p className="prose mt-3 text-muted">
              One standard stack across projects. Performance and accessibility are checked before
              ship, and every release passes a written Definition of Done.
            </p>
            <ul className="mt-6 flex flex-wrap gap-3" aria-label="Standard stack">
              {['TypeScript', 'Next.js / React', 'Tailwind', 'Node / TS API', 'PostgreSQL', 'GitHub Actions'].map((t) => (
                <li key={t} className="rounded-full border border-line bg-white px-4 py-2 text-sm font-medium text-ink">
                  {t}
                </li>
              ))}
            </ul>
          </div>
        </section>

        {/* CTA */}
        <section id="contact" className="border-t border-line bg-ink py-16 text-white" aria-labelledby="contact-title">
          <div className="mx-auto max-w-5xl px-5 text-center">
            <h2 id="contact-title" className="text-3xl font-bold tracking-tight">Have a site that needs to work harder?</h2>
            <p className="prose mx-auto mt-3 text-white/70">
              Send us an email and we will talk about what you need and whether we are the right partner.
            </p>
            <a
              href="mailto:syashvardhan00714@gmail.com?subject=Website%20enquiry"
              className="mt-6 inline-block rounded-xl bg-brand px-6 py-3 font-semibold text-white hover:opacity-90"
            >
              Email us about a website
            </a>
            <p className="mt-4 text-sm text-white/70">
              Or write directly to{' '}
              <a className="font-medium text-white underline decoration-white/40 underline-offset-4 hover:decoration-white" href="mailto:syashvardhan00714@gmail.com">
                syashvardhan00714@gmail.com
              </a>
            </p>
          </div>
        </section>
      </main>

      <footer className="border-t border-line bg-white py-8">
        <div className="mx-auto max-w-5xl px-5 text-center text-sm text-muted">
          Lux and Logic · Internal draft. Proof points are labelled placeholders pending real client data.
        </div>
      </footer>
    </>
  );
}
