/* textual-themes / GitHub Pages carousel
   Vanilla JS. Theme list mirrors RETRO_THEMES order in themes.py. */
(function () {
  "use strict";

  const THEMES = [
    { slug: "c64",            name: "C64 — Commodore 64",            dark: true  },
    { slug: "amiga",          name: "Amiga Workbench 1.3",                 dark: true  },
    { slug: "atari-st",       name: "Atari ST GEM Desktop",                dark: false },
    { slug: "ibm-terminal",   name: "IBM Terminal — Phosphor Green",  dark: true  },
    { slug: "nextstep",       name: "NeXTSTEP",                            dark: true  },
    { slug: "beos",           name: "BeOS",                                dark: true  },
    { slug: "ubuntu",         name: "Ubuntu",                              dark: true  },
    { slug: "macos",          name: "macOS",                               dark: false },
    { slug: "windows-xp",     name: "Windows XP — Luna",              dark: true  },
    { slug: "msdos",          name: "Norton Commander",                    dark: true  },
    { slug: "plan9",          name: "Plan 9 — Bell Labs",             dark: false },
    { slug: "solaris-cde",    name: "Solaris CDE",                         dark: true  },
    { slug: "os2-warp",       name: "OS/2 Warp",                           dark: true  },
    { slug: "opensuse",       name: "openSUSE",                            dark: true  },
    { slug: "linux-mint",     name: "Linux Mint",                          dark: true  },
    { slug: "red-hat",        name: "Red Hat Linux",                       dark: true  },
    { slug: "raspberry-pi",   name: "Raspberry Pi OS",                     dark: true  },
    { slug: "freebsd",        name: "FreeBSD",                             dark: true  },
    { slug: "tudor",          name: "Tudor — Black Bay 58",           dark: true  },
    { slug: "bluesy",         name: "Bluesy — Rolex Gold",            dark: true  },
    { slug: "goldfinger",     name: "Goldfinger — James Bond (1964)", dark: true  },
    { slug: "hulk",           name: "Hulk — Marvel's Incredible Hulk",dark: true  },
    { slug: "batman",         name: "Batman — DC's Dark Knight",      dark: true  },
    { slug: "classic-navy",   name: "Classic Navy",                        dark: true  },
    { slug: "gameboy",        name: "Game Boy — Nintendo DMG-01",     dark: false },
    { slug: "pan-am",         name: "Pan Am — Pan American World Airways", dark: false },
    { slug: "synthwave",      name: "Synthwave — 80s Retro-Futurism", dark: true  },
    { slug: "miami-vice",     name: "Miami Vice — Pastel 80s",        dark: true  },
    { slug: "martini-racing", name: "Martini Racing",                      dark: true  },
    { slug: "metropolis",     name: "Metropolis — Bold Blue, Crimson & Sun Yellow", dark: true },
    { slug: "spiderman",      name: "Spiderman — Marvel's Web-Slinger", dark: true },
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
