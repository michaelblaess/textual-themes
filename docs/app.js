/* textual-themes / GitHub Pages carousel
   Vanilla JS. Theme list mirrors RETRO_THEMES order in themes.py. */
(function () {
  "use strict";

  const THEMES = [
    { slug: "brotkasten",       name: "Brotkasten — Light Blue on Royal Blue",         dark: true  },
    { slug: "boing",            name: "Boing — Blue/White/Orange Workbench",           dark: true  },
    { slug: "gemstone",         name: "Gemstone — Monochrome GEM Desktop",             dark: false },
    { slug: "classic-terminal", name: "Classic Terminal — Phosphor Green on Black",    dark: true  },
    { slug: "next",             name: "Next — Slate Gray with Magenta Accents",        dark: true  },
    { slug: "bebox",            name: "BeBox — Blue-Gray with Yellow Accent",          dark: true  },
    { slug: "bunty",            name: "Bunty — Aubergine with Warm Orange Accents",    dark: true  },
    { slug: "cupertino",        name: "Cupertino — Clean Light Gray with Blue Accents", dark: false },
    { slug: "luna",             name: "Luna — Sky Blue with Green Start Accent",       dark: true  },
    { slug: "commandr",         name: "Commandr — Blue/Cyan/Yellow File Manager",      dark: true  },
    { slug: "plan9",            name: "Plan 9 — Pulpy Yellow/Blue/Green",              dark: false },
    { slug: "motif",            name: "Motif — Beige Corporate Unix Toolkit",          dark: true  },
    { slug: "warp",             name: "Warp — Dark Blue with Teal Accents",            dark: true  },
    { slug: "geeko",            name: "Geeko — Dark Green with White",                 dark: true  },
    { slug: "minty",            name: "Minty — Warm Mint-Green on Charcoal",           dark: true  },
    { slug: "crimson",          name: "Crimson — Deep Red on Dark Charcoal",           dark: true  },
    { slug: "razzy",            name: "Razzy — Raspberry Red on Dark Slate",           dark: true  },
    { slug: "beastie",          name: "Beastie — Daemon Red on Dark Slate",            dark: true  },
    { slug: "fifty-eight",      name: "Fifty-Eight — Black Dial, Aged Gold Lume & Bezel Red", dark: true  },
    { slug: "bluesy",           name: "Bluesy — Royal Blue & Gold",                    dark: true  },
    { slug: "goldfinder",       name: "Goldfinder — Deep Black with 18K Gold Accents", dark: true  },
    { slug: "hulkula",          name: "Hulkula — Verdant Green with Steel Edges",      dark: true  },
    { slug: "flughund",         name: "Flughund — Midnight Black & Moonlit Blue",      dark: true  },
    { slug: "classic-navy",     name: "Classic Navy",                                  dark: true  },
    { slug: "brick",            name: "Brick — Olive-Green Handheld LCD",              dark: false },
    { slug: "clipper",          name: "Clipper — Globe Blue on Ivory",                 dark: false },
    { slug: "synthwave",        name: "Synthwave — 80s Retro-Futurism",                dark: true  },
    { slug: "miami",            name: "Miami — Twilight Teal, Flamingo Pink & Sunset Coral", dark: true  },
    { slug: "racing",           name: "Racing — Charcoal with Blue, Red & Silver Stripes",   dark: true  },
    { slug: "metropolis",       name: "Metropolis — Bold Blue, Crimson & Sun Yellow",  dark: true  },
    { slug: "spiderized",       name: "Spiderized — Red & Royal-Blue Hero Suit",       dark: true  },
  ];

  // ── DOM refs ────────────────────────────────────────────────────
  const heroImg     = document.getElementById("hero");
  const fullLink    = document.getElementById("full-link");
  const nameEl      = document.getElementById("theme-name");
  const positionEl  = document.getElementById("theme-position");
  const btnPrev     = document.getElementById("btn-prev");
  const btnNext     = document.getElementById("btn-next");
  const thumbList   = document.getElementById("thumb-list");
  const filterChips = document.querySelectorAll(".chip[data-filter]");
  const countEls    = document.querySelectorAll(".chip-count[data-count]");

  // ── State ──────────────────────────────────────────────────────
  let currentSlug = THEMES[0].slug;
  let activeFilter = "all";

  function visibleThemes() {
    if (activeFilter === "dark")  return THEMES.filter(t =>  t.dark);
    if (activeFilter === "light") return THEMES.filter(t => !t.dark);
    return THEMES;
  }

  // ── Render thumbnails (once) ────────────────────────────────────
  function buildThumbs() {
    const fragment = document.createDocumentFragment();
    THEMES.forEach((t) => {
      const li = document.createElement("li");
      li.className = "thumb";
      li.dataset.slug = t.slug;
      li.dataset.kind = t.dark ? "dark" : "light";

      const img = document.createElement("img");
      img.src = "screenshots/" + t.slug + ".svg";
      img.alt = t.name;
      img.loading = "lazy";

      const label = document.createElement("div");
      label.className = "thumb-label";
      const span = document.createElement("span");
      span.textContent = t.name.split(" — ")[0];
      const badge = document.createElement("span");
      badge.className = "badge " + (t.dark ? "dark" : "light");
      badge.textContent = t.dark ? "dark" : "light";
      label.appendChild(span);
      label.appendChild(badge);

      li.appendChild(img);
      li.appendChild(label);
      li.addEventListener("click", () => selectTheme(t.slug));
      fragment.appendChild(li);
    });
    thumbList.appendChild(fragment);
  }

  // ── Counts ──────────────────────────────────────────────────────
  function renderCounts() {
    const total = THEMES.length;
    const dark  = THEMES.filter(t => t.dark).length;
    const light = total - dark;
    countEls.forEach((el) => {
      const k = el.dataset.count;
      if (k === "all")   el.textContent = "(" + total + ")";
      if (k === "dark")  el.textContent = "(" + dark + ")";
      if (k === "light") el.textContent = "(" + light + ")";
    });
  }

  // ── Selection ──────────────────────────────────────────────────
  function selectTheme(slug, opts) {
    opts = opts || {};
    const theme = THEMES.find(t => t.slug === slug);
    if (!theme) return;
    currentSlug = slug;

    const path = "screenshots/" + slug + ".svg";
    heroImg.src = path;
    heroImg.alt = theme.name;
    fullLink.href = path;

    nameEl.textContent = theme.name;
    const visible = visibleThemes();
    const visibleIdx = visible.findIndex(t => t.slug === slug);
    if (visibleIdx >= 0) {
      positionEl.textContent = (visibleIdx + 1) + " / " + visible.length;
    } else {
      positionEl.textContent = "";
    }

    document.querySelectorAll(".thumb").forEach((el) => {
      el.classList.toggle("is-active", el.dataset.slug === slug);
    });

    if (!opts.silent) {
      const hash = "#" + slug;
      if (location.hash !== hash) {
        history.replaceState(null, "", hash);
      }
    }
  }

  // ── Navigation ─────────────────────────────────────────────────
  function step(delta) {
    const visible = visibleThemes();
    if (visible.length === 0) return;
    let idx = visible.findIndex(t => t.slug === currentSlug);
    if (idx === -1) idx = 0;
    const newIdx = (idx + delta + visible.length) % visible.length;
    selectTheme(visible[newIdx].slug);
  }

  // ── Filter ─────────────────────────────────────────────────────
  function applyFilter(kind) {
    activeFilter = kind;
    filterChips.forEach((chip) => {
      chip.classList.toggle("is-active", chip.dataset.filter === kind);
    });
    document.querySelectorAll(".thumb").forEach((el) => {
      const matches = kind === "all" || el.dataset.kind === kind;
      el.classList.toggle("is-hidden", !matches);
    });
    // If current theme is filtered out, jump to first visible
    const visible = visibleThemes();
    if (visible.length > 0 && !visible.some(t => t.slug === currentSlug)) {
      selectTheme(visible[0].slug);
    } else {
      // refresh counter
      selectTheme(currentSlug, { silent: true });
    }
  }

  // ── Wire up ────────────────────────────────────────────────────
  function init() {
    buildThumbs();
    renderCounts();

    btnPrev.addEventListener("click", () => step(-1));
    btnNext.addEventListener("click", () => step(+1));
    filterChips.forEach((chip) => {
      chip.addEventListener("click", () => applyFilter(chip.dataset.filter));
    });

    document.addEventListener("keydown", (ev) => {
      if (ev.target && /^(INPUT|TEXTAREA|SELECT)$/.test(ev.target.tagName)) return;
      if (ev.key === "ArrowLeft")  { step(-1); ev.preventDefault(); }
      if (ev.key === "ArrowRight") { step(+1); ev.preventDefault(); }
    });

    window.addEventListener("hashchange", () => {
      const slug = location.hash.replace(/^#/, "");
      if (slug && THEMES.some(t => t.slug === slug)) {
        selectTheme(slug, { silent: true });
      }
    });

    // Initial slug from URL hash, fall back to first theme
    const hashSlug = location.hash.replace(/^#/, "");
    const initial = THEMES.find(t => t.slug === hashSlug) ? hashSlug : THEMES[0].slug;
    selectTheme(initial, { silent: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
