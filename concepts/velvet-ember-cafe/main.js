(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canvas = document.getElementById('atmosphere');
  const ctx = canvas && canvas.getContext ? canvas.getContext('2d') : null;
  let w = window.innerWidth, h = window.innerHeight, dpr = Math.min(window.devicePixelRatio || 1, 1.5);
  let particles = [], raf = null, scrollP = 0;

  function onScroll() {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    scrollP = max > 0 ? window.scrollY / max : 0;
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  function resize() {
    if (!ctx) return;
    w = window.innerWidth; h = window.innerHeight;
    canvas.width = Math.floor(w * dpr); canvas.height = Math.floor(h * dpr);
    canvas.style.width = w + 'px'; canvas.style.height = h + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const count = reduceMotion ? 18 : Math.min(42, Math.floor((w * h) / 50000));
    particles = Array.from({ length: count }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      r: Math.random() * 40 + 20,
      vx: (Math.random() - 0.5) * 0.08,
      vy: (Math.random() - 0.5) * 0.05,
      a: Math.random() * 0.08 + 0.03
    }));
  }

  function draw(t = 0) {
    if (!ctx) return;
    ctx.clearRect(0, 0, w, h);
    const bg = ctx.createLinearGradient(0, 0, 0, h);
    bg.addColorStop(0, 'rgba(40,28,22,0.35)');
    bg.addColorStop(1, 'rgba(18,15,13,0.05)');
    ctx.fillStyle = bg; ctx.fillRect(0, 0, w, h);
    for (const p of particles) {
      if (!reduceMotion) {
        p.x += p.vx; p.y += p.vy - scrollP * 0.02;
        if (p.x < -80) p.x = w + 80; if (p.x > w + 80) p.x = -80;
        if (p.y < -80) p.y = h + 80; if (p.y > h + 80) p.y = -80;
      }
      const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r);
      g.addColorStop(0, `rgba(201,122,74,${p.a})`);
      g.addColorStop(1, 'rgba(201,122,74,0)');
      ctx.fillStyle = g;
      ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
    }
    if (!reduceMotion) raf = requestAnimationFrame(draw);
  }

  if (ctx) {
    resize();
    window.addEventListener('resize', resize, { passive: true });
    draw();
    document.addEventListener('visibilitychange', () => {
      if (reduceMotion) return;
      if (document.hidden && raf) cancelAnimationFrame(raf);
      else if (!document.hidden) raf = requestAnimationFrame(draw);
    });
  }

  const showAll = () => document.querySelectorAll('.reveal').forEach(el => { el.style.opacity = 1; el.style.transform = 'none'; });
  if (reduceMotion || typeof gsap === 'undefined') { showAll(); return; }

  gsap.registerPlugin(ScrollTrigger);
  if (typeof Lenis !== 'undefined') {
    const lenis = new Lenis({ duration: 0.95, smoothWheel: true, wheelMultiplier: 0.9 });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add((time) => lenis.raf(time * 1000));
    gsap.ticker.lagSmoothing(0);
  }

  gsap.to('.hero-bg', { scale: 1.12, yPercent: 6, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
  gsap.utils.toArray('.hero .reveal').forEach((el, i) => gsap.to(el, { opacity: 1, y: 0, duration: 1.05, ease: 'power3.out', delay: 0.15 + i * 0.1 }));
  gsap.utils.toArray('.chapter .reveal').forEach((el) => {
    gsap.to(el, { opacity: 1, y: 0, duration: 0.9, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 82%' } });
  });
  gsap.utils.toArray('.parallax').forEach((el) => {
    const speed = parseFloat(el.dataset.speed || '0.06');
    gsap.to(el, { yPercent: -18 * speed * 10, ease: 'none', scrollTrigger: { trigger: el.closest('section'), start: 'top bottom', end: 'bottom top', scrub: true } });
  });
})();