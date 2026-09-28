(() => {
  const LOGO_PATHS = `<rect x="1" y="1" width="10" height="10" fill="#F25022"/><rect x="12" y="1" width="10" height="10" fill="#7FBA00"/><rect x="1" y="12" width="10" height="10" fill="#00A4EF"/><rect x="12" y="12" width="10" height="10" fill="#FFB900"/>`;

  const CONFIG = {
    pt: { path: '', label: 'PT', code: 'pt-BR' },
    en: { path: 'en/', label: 'EN', code: 'en' },
    es: { path: 'es/', label: 'ES', code: 'es' }
  };

  const body = document.body;
  const app = document.getElementById('app');
  const pageLang = body.dataset.lang || 'pt-BR';
  const basePath = body.dataset.base || '';
  const contentPath = body.dataset.content || `${basePath}content.json`;
  const shouldAutodetect = body.dataset.autodetect === 'true';

  function detectBrowserLanguage() {
    const raw = (navigator.languages && navigator.languages[0]) || navigator.language || '';
    const lang = raw.toLowerCase();
    if (lang.startsWith('es')) return 'es';
    if (lang.startsWith('en')) return 'en';
    return 'pt-BR';
  }

  function toShortLang(lang) {
    if (lang === 'pt-BR' || lang === 'pt') return 'pt';
    if (lang === 'en') return 'en';
    if (lang === 'es') return 'es';
    return 'pt';
  }

  function languageHref(langCode) {
    const short = toShortLang(langCode);
    return `${basePath}${CONFIG[short].path || ''}` || './';
  }

  function maybeRedirectToPreferredLanguage() {
    if (!shouldAutodetect) return;
    const params = new URLSearchParams(window.location.search);
    const forced = params.get('lang');
    const stored = localStorage.getItem('aiMaturityLang');
    const target = forced || stored || detectBrowserLanguage();
    if (target && target !== pageLang) {
      window.location.replace(languageHref(target));
    }
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function resolveAsset(path) {
    if (/^https?:\/\//.test(path)) return path;
    return `${basePath}${path}`;
  }

  function logoSvg(label, title) {
    return `<svg viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${escapeHtml(label)}"><title>${escapeHtml(title)}</title>${LOGO_PATHS}</svg>`;
  }

  function renderLanguageLinks(currentLang) {
    return Object.values(CONFIG).map((language) => {
      if (language.code === currentLang) {
        return `<strong class="lang-pill is-active">${language.label}</strong>`;
      }
      return `<a class="lang-pill" href="${languageHref(language.code)}" data-lang-choice="${language.code}">${language.label}</a>`;
    }).join('');
  }

  function renderChrome(content) {
    const navItems = Object.entries(content.nav).map(([id, label]) => `<a class="top-link" href="#${id}">${escapeHtml(label)}</a>`).join('');
    return `
      <header class="meta-bar">
        <a href="#main" class="brand">
          ${logoSvg('Microsoft', 'Microsoft')}
          <div class="brand__text">
            <div class="brand__title">AI Maturity Kit</div>
            <div class="brand__sub">by ${escapeHtml(content.brand.name)}</div>
          </div>
        </a>
        <div class="top-tools">
          <nav class="top-nav" aria-label="Primary navigation">
            ${navItems}
          </nav>
          <span class="top-lang" aria-label="Language selector">${renderLanguageLinks(pageLang)}</span>
          <button class="tool-btn" id="theme-toggle" type="button" title="Toggle theme" aria-label="Toggle theme">
            <svg class="theme-icon theme-icon--sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
            <svg class="theme-icon theme-icon--moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          </button>
        </div>
      </header>`;
  }

  function renderHero(content) {
    const rows = content.hero.cardRows.map((row) => `
      <div class="hero__card-row">
        <div class="hero__card-icon hero__card-icon--${escapeHtml(row.iconClass)}">${escapeHtml(row.icon)}</div>
        <div><strong>${escapeHtml(row.title)}</strong><br><span class="hero__card-copy">${escapeHtml(row.subtitle)}</span></div>
        <span class="hero__card-num">${escapeHtml(row.metric)}</span>
      </div>`).join('');

    return `
      <section class="hero">
        <div class="hero__inner">
          <div>
            <div class="hero__eyebrow"><span class="hero__eyebrow-dot"></span>${escapeHtml(content.hero.eyebrow)}</div>
            <h1 class="hero__title">${escapeHtml(content.hero.titleBefore)} <span class="accent">${escapeHtml(content.hero.titleAccent)}</span>${content.hero.titleAfter ? ` ${escapeHtml(content.hero.titleAfter)}` : ''}</h1>
            <p class="hero__lede">${escapeHtml(content.hero.lede)}</p>
            <div class="hero__ctas">
              <a class="btn btn--primary" href="#download">${escapeHtml(content.hero.primaryCta)}</a>
              <a class="btn btn--secondary" href="#quickstart">${escapeHtml(content.hero.secondaryCta)}</a>
            </div>
          </div>
          <aside class="hero__card">
            <div class="hero__card-title">${escapeHtml(content.hero.cardTitle)}</div>
            <div class="hero__card-rows">${rows}</div>
          </aside>
        </div>
      </section>`;
  }

  function renderPipeline(content) {
    const steps = content.pipeline.steps.map((step) => `
      <div class="pipe-step pipe-step--${escapeHtml(step.kind)}">
        <div class="pipe-step__num">${escapeHtml(step.num)}</div>
        <div class="pipe-step__name">${escapeHtml(step.name)}</div>
        <div class="pipe-step__hint">${escapeHtml(step.hint)}</div>
      </div>`).join('');
    return `
      <section class="pipeline" id="pipeline">
        <div class="container">
          <div class="section__eyebrow">${escapeHtml(content.pipeline.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.pipeline.title)}</h2>
          <p class="section__lede">${escapeHtml(content.pipeline.lede)}</p>
          <div class="pipeline__chain">${steps}</div>
        </div>
      </section>`;
  }

  function renderSurveys(content) {
    const cards = content.surveys.cards.map((card) => {
      const meta = card.meta.map((item) => `<div><strong>${escapeHtml(item.value)}</strong>${escapeHtml(item.label)}</div>`).join('');
      const list = card.items.map((item) => `<li>${escapeHtml(item)}</li>`).join('');
      return `
        <article class="card card--${escapeHtml(card.variant)}">
          <div class="card__badge"><span class="card__badge-dot"></span>${escapeHtml(card.badge)}</div>
          <h3 class="card__title">${escapeHtml(card.title)}</h3>
          <div class="card__subtitle">${escapeHtml(card.subtitle)}</div>
          <div class="card__meta">${meta}</div>
          <ul class="card__list">${list}</ul>
        </article>`;
    }).join('');

    return `
      <section id="surveys">
        <div class="container">
          <div class="section__eyebrow">${escapeHtml(content.surveys.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.surveys.title)}</h2>
          <p class="section__lede">${escapeHtml(content.surveys.lede)}</p>
          <div class="cards">${cards}</div>
        </div>
      </section>`;
  }

  function renderQuickstart(content) {
    const steps = content.quickstart.steps.map((step) => `
      <div class="step">
        <div class="step__num">${escapeHtml(step.num)}</div>
        <h3 class="step__title">${escapeHtml(step.title)}</h3>
        <p class="step__body">${escapeHtml(step.body)}</p>
        <code class="step__cmd">${escapeHtml(step.command)}</code>
      </div>`).join('');
    return `
      <section id="quickstart" class="section--paper">
        <div class="container">
          <div class="section__eyebrow">${escapeHtml(content.quickstart.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.quickstart.title)}</h2>
          <p class="section__lede">${escapeHtml(content.quickstart.lede)}</p>
          <div class="steps">${steps}</div>
        </div>
      </section>`;
  }

  function renderSkills(content) {
    const skills = content.skills.items.map((skill) => `
      <div class="skill-pill"><div><div class="skill-pill__cmd">${escapeHtml(skill.cmd)}</div><div class="skill-pill__desc">${escapeHtml(skill.desc)}</div></div></div>`).join('');
    return `
      <section id="skills">
        <div class="container">
          <div class="section__eyebrow">${escapeHtml(content.skills.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.skills.title)}</h2>
          <p class="section__lede">${escapeHtml(content.skills.lede)}</p>
          <div class="skills-grid">${skills}</div>
        </div>
      </section>`;
  }

  function renderFaq(content) {
    const items = content.faq.items.map((item) => `
      <details class="faq__item">
        <summary>${escapeHtml(item.summary)}</summary>
        <p>${item.answerHtml}</p>
      </details>`).join('');
    return `
      <section id="faq" class="section--paper section--faq">
        <div class="container faq-container">
          <div class="section__eyebrow">${escapeHtml(content.faq.eyebrow)}</div>
          <h2 class="section__title">${escapeHtml(content.faq.title)}</h2>
          <p class="section__lede">${escapeHtml(content.faq.lede)}</p>
          <div class="faq">${items}</div>
        </div>
      </section>`;
  }

  function renderDownload(content, data) {
    const shortLang = toShortLang(pageLang);
    const downloadUrl = resolveAsset(data.downloads[pageLang] || data.downloads[shortLang] || data.downloads['pt-BR']);
    const panelItems = content.download.panelItems.map((item) => `<li>${escapeHtml(item.label)}<code>${escapeHtml(item.code)}</code></li>`).join('');
    return `
      <section class="download" id="download">
        <div class="container">
          <div class="download__inner">
            <div>
              <div class="section__eyebrow">${escapeHtml(content.download.eyebrow)}</div>
              <h2 class="section__title">${escapeHtml(content.download.title)}</h2>
              <p class="section__lede">${escapeHtml(content.download.lede)}</p>
              <div class="download__cta">
                <a class="btn btn--primary" href="${escapeHtml(downloadUrl)}">${escapeHtml(content.download.primaryCta)}</a>
              </div>
            </div>
            <div class="download__panel">
              <div class="download__panel-title">${escapeHtml(content.download.panelTitle)}</div>
              <ul>${panelItems}</ul>
            </div>
          </div>
        </div>
      </section>`;
  }

  function renderAbout(content, data) {
    const about = content.about;
    if (!about) return '';

    const [statement = '', ...bodyParagraphs] = about.paragraphs || [];
    const body = bodyParagraphs.map((paragraph) => `<p>${escapeHtml(paragraph)}</p>`).join('');
    const contactUrl = data.contactLinkedIn || '#';
    const profileImage = resolveAsset(data.profileImage || 'assets/paula-about.jpg');
    const connectLinks = [
      { icon: 'in', title: 'LinkedIn', meta: '/paulanunes', href: contactUrl },
      { icon: 'gh', title: 'GitHub Projects', meta: '@paulasilvatech', href: 'https://github.com/paulasilvatech' },
      { icon: 'gh', title: 'GitHub Personal', meta: '@paulanunes85', href: 'https://github.com/paulanunes85' }
    ].map((link) => `
      <li class="about-connect__item">
        <a class="about-connect__link" href="${escapeHtml(link.href)}" target="_blank" rel="noopener noreferrer">
          <span class="about-connect__icon" aria-hidden="true">${escapeHtml(link.icon)}</span>
          <span class="about-connect__copy">
            <span class="about-connect__title">${escapeHtml(link.title)}</span>
            <span class="about-connect__meta">${escapeHtml(link.meta)}</span>
          </span>
        </a>
      </li>`).join('');

    return `
      <section class="about section--paper" id="about">
        <div class="container">
          <div class="about__inner">
            <div class="about__portrait">
              <img src="${escapeHtml(profileImage)}" alt="${escapeHtml(content.brand.name)} portrait">
            </div>
            <div class="about__content">
              <div class="section__eyebrow">${escapeHtml(about.eyebrow)}</div>
              <h2 class="section__title">${escapeHtml(about.title)}</h2>
              <div class="about__statement"><p>${escapeHtml(statement)}</p></div>
              <div class="about__body">${body}</div>
              <div class="about-connect">
                <div class="about-connect__label">${escapeHtml(about.connectLabel || 'Connect')}</div>
                <ul class="about-connect__grid">${connectLinks}</ul>
              </div>
            </div>
          </div>
        </div>
      </section>`;
  }

  function renderFooter(content, data) {
    const footer = content.footer || {};
    const navItems = Object.entries(content.nav).map(([id, label]) => `<a href="#${id}">${escapeHtml(label)}</a>`).join('');
    const contactUrl = data.contactLinkedIn || '#';
    const footerLegal = footer.legal ? `<p class="footer__legal">${escapeHtml(footer.legal)}</p>` : '';
    return `
      <footer class="footer">
        <div class="footer__stripe" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
        <div class="container">
          <section class="footer__hub" aria-label="AI Maturity Kit hub">
            <div class="footer__kicker">${escapeHtml(content.brand.name)} | ${escapeHtml(footer.roleTagline || 'Global Developer Solutions Advisor')}</div>
            <h2 class="footer__headline">${escapeHtml(footer.headlineBefore || 'Building the future of software with')} <span class="footer__headline-accent">${escapeHtml(footer.headlineAccent || 'AI.')}</span></h2>
            <p class="footer__summary">${escapeHtml(footer.summary || 'Everything here comes from practical field work with enterprise AI transformation: assessment kits, survey flows, scoring models, executive reports, and implementation guides built to help teams adopt AI with evidence.')}</p>
            <a class="footer__hub-link" href="${escapeHtml(data.hubUrl || 'https://agenticdevopsplatform.ai/')}">
              <span class="footer__hub-icon" aria-hidden="true">&#8599;</span>
              <span>
                <span class="footer__hub-kicker">${escapeHtml(footer.hubKicker || 'Visit the complete site')}</span>
                <span class="footer__hub-title">${escapeHtml(footer.hubTitle || 'Agentic DevOps Platform')}</span>
              </span>
            </a>
          </section>
          <div class="footer__grid">
            <div>
              <h5>${escapeHtml(footer.aboutTitle || content.title)}</h5>
              <p>${escapeHtml(footer.aboutText || content.brand.tagline)}</p>
            </div>
            <div>
              <h5>${escapeHtml(footer.linksTitle || 'Navigation')}</h5>
              <div class="footer__links">${navItems}</div>
            </div>
            <div>
              <h5>${escapeHtml(footer.contactTitle || 'Contact')}</h5>
              <div class="footer__author">${escapeHtml(content.brand.role)}</div>
              <div class="footer__links">
                <a href="${escapeHtml(contactUrl)}" target="_blank" rel="noopener noreferrer">${escapeHtml(footer.contactLabel || 'LinkedIn')}</a>
                <a href="${escapeHtml(data.repositoryUrl || '#')}" target="_blank" rel="noopener noreferrer">${escapeHtml(footer.repositoryLabel || 'Repository')}</a>
              </div>
            </div>
          </div>
          ${footerLegal}
        </div>
      </footer>`;
  }

  function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem('aiMaturityTheme', theme);
  }

  function initThemeToggle() {
    const storedTheme = localStorage.getItem('aiMaturityTheme');
    const prefersDark = globalThis.matchMedia?.('(prefers-color-scheme: dark)').matches;
    applyTheme(storedTheme || (prefersDark ? 'dark' : 'light'));

    const button = document.getElementById('theme-toggle');
    if (!button) return;
    button.addEventListener('click', () => {
      const nextTheme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      applyTheme(nextTheme);
    });
  }

  function render(content, data) {
    document.documentElement.lang = content.htmlLang;
    document.title = content.title;
    const description = document.querySelector('meta[name="description"]');
    if (description) description.setAttribute('content', content.description);

    app.innerHTML = [
      renderChrome(content),
      '<main id="main">',
      renderHero(content),
      renderPipeline(content),
      renderSurveys(content),
      renderQuickstart(content),
      renderSkills(content),
      renderFaq(content),
      renderDownload(content, data),
      renderAbout(content, data),
      '</main>',
      renderFooter(content, data)
    ].join('');

    document.querySelectorAll('[data-lang-choice]').forEach((link) => {
      link.addEventListener('click', () => localStorage.setItem('aiMaturityLang', link.dataset.langChoice));
    });
    initThemeToggle();
  }

  function renderLoadError() {
    app.innerHTML = `
      <main class="loading loading--error">
        <h1>AI Maturity Assessment Kit</h1>
        <p>Unable to load <code>${escapeHtml(contentPath)}</code>. For local preview, run <code>cd docs && python3 -m http.server 8000</code> and open <code>http://localhost:8000</code>.</p>
      </main>`;
  }

  async function boot() {
    maybeRedirectToPreferredLanguage();
    try {
      const response = await fetch(contentPath, { cache: 'no-cache' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      const content = data.i18n[pageLang] || data.i18n['pt-BR'];
      render(content, data);
    } catch (error) {
      console.error(error);
      renderLoadError();
    }
  }

  boot();
})();
