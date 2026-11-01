import re

def update_main_js():
    with open('js/main.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. ThemeEngine Implementation
    theme_engine_code = """// ==========================================================================
// 2. THEME ENGINE (LIGHT & DARK DUAL MATRIX)
// ==========================================================================
const ThemeEngine = {
  STORAGE_KEY: "arenium_theme",

  getTheme() {
    try {
      return localStorage.getItem(this.STORAGE_KEY) || "dark";
    } catch (e) {
      return "dark";
    }
  },

  setTheme(theme) {
    if (theme !== "light" && theme !== "dark") theme = "dark";
    try {
      localStorage.setItem(this.STORAGE_KEY, theme);
    } catch (e) {}

    document.documentElement.setAttribute("data-theme", theme);
    document.documentElement.classList.remove("light-theme", "dark-theme");
    document.documentElement.classList.add(theme + "-theme");

    // Update all toggle buttons
    const toggles = document.querySelectorAll(".theme-toggle-btn");
    toggles.forEach(btn => {
      btn.setAttribute("aria-checked", theme === "light");
      btn.setAttribute("title", theme === "light" ? "Switch to Dark Mode" : "Switch to Light Mode");
      const label = btn.querySelector(".theme-toggle-label");
      if (label) {
        label.textContent = theme.toUpperCase();
      }
    });

    // Update brand logos
    const brandLogos = document.querySelectorAll(".brand-logo-img");
    brandLogos.forEach(img => {
      if (theme === "light") {
        img.src = "images/logo-light.svg";
      } else {
        img.src = "images/logo.svg";
      }
    });

    // Dispatch custom event for canvas and other subscribers
    window.dispatchEvent(new CustomEvent("themechange", { detail: { theme } }));
  },

  toggleTheme() {
    const current = this.getTheme();
    const next = current === "light" ? "dark" : "light";
    this.setTheme(next);
  },

  init() {
    // 1. Ensure theme is applied
    const currentTheme = this.getTheme();
    this.setTheme(currentTheme);

    // 2. Ensure buttons exist on page
    this.ensureToggleButtons();

    // 3. Delegate click handler
    document.addEventListener("click", (e) => {
      const btn = e.target.closest(".theme-toggle-btn");
      if (btn) {
        e.preventDefault();
        this.toggleTheme();
      }
    });
  },

  ensureToggleButtons() {
    const theme = this.getTheme();

    // Desktop action container
    const desktopActions = document.querySelector(".header-action-desktop");
    if (desktopActions && !desktopActions.querySelector(".theme-toggle-btn")) {
      const toggleBtn = document.createElement("button");
      toggleBtn.className = "theme-toggle-btn";
      toggleBtn.id = "theme-toggle-desktop";
      toggleBtn.setAttribute("aria-label", "Toggle light and dark mode");
      toggleBtn.setAttribute("title", theme === "light" ? "Switch to Dark Mode" : "Switch to Light Mode");
      toggleBtn.innerHTML = `
        <span class="theme-toggle-track">
          <span class="theme-toggle-thumb">
            <span class="theme-toggle-icon icon-sun">☀️</span>
            <span class="theme-toggle-icon icon-moon">🌙</span>
          </span>
        </span>
        <span class="theme-toggle-label">${theme.toUpperCase()}</span>
      `;
      desktopActions.insertBefore(toggleBtn, desktopActions.firstChild);
    }

    // Mobile header group (next to hamburger)
    const headerContainer = document.querySelector(".header-container");
    const navToggle = document.querySelector(".nav-toggle-btn");
    if (headerContainer && navToggle && !headerContainer.querySelector(".header-mobile-group")) {
      const group = document.createElement("div");
      group.className = "header-mobile-group";
      navToggle.parentNode.insertBefore(group, navToggle);

      const mobileToggleBtn = document.createElement("button");
      mobileToggleBtn.className = "theme-toggle-btn theme-toggle-btn-compact";
      mobileToggleBtn.id = "theme-toggle-mobile";
      mobileToggleBtn.setAttribute("aria-label", "Toggle light and dark mode");
      mobileToggleBtn.setAttribute("title", theme === "light" ? "Switch to Dark Mode" : "Switch to Light Mode");
      mobileToggleBtn.innerHTML = `
        <span class="theme-toggle-track">
          <span class="theme-toggle-thumb">
            <span class="theme-toggle-icon icon-sun">☀️</span>
            <span class="theme-toggle-icon icon-moon">🌙</span>
          </span>
        </span>
      `;
      group.appendChild(mobileToggleBtn);
      group.appendChild(navToggle);
    }

    // Mobile nav drawer item
    const navMenu = document.querySelector(".nav-menu");
    if (navMenu && !navMenu.querySelector("#theme-toggle-drawer")) {
      const drawerItem = document.createElement("div");
      drawerItem.className = "nav-item mobile-only";
      drawerItem.style.cssText = "margin-top: 0.5rem; width: 100%;";
      drawerItem.innerHTML = `
        <button class="theme-toggle-btn" id="theme-toggle-drawer" style="width: 100%; justify-content: space-between; padding: 0.6rem 1rem;">
          <span style="font-family: var(--font-mono); font-size: 0.8rem;">THEME MATRIX</span>
          <span style="display: flex; align-items: center; gap: 0.5rem;">
            <span class="theme-toggle-track">
              <span class="theme-toggle-thumb">
                <span class="theme-toggle-icon icon-sun">☀️</span>
                <span class="theme-toggle-icon icon-moon">🌙</span>
              </span>
            </span>
            <span class="theme-toggle-label">${theme.toUpperCase()}</span>
          </span>
        </button>
      `;
      navMenu.appendChild(drawerItem);
    }

    // Admin header bar
    const adminHeader = document.querySelector(".site-header div[style*='align-items: center'] button#admin-export-btn");
    if (adminHeader && adminHeader.parentElement && !adminHeader.parentElement.querySelector(".theme-toggle-btn")) {
      const adminToggle = document.createElement("button");
      adminToggle.className = "theme-toggle-btn";
      adminToggle.id = "theme-toggle-admin";
      adminToggle.setAttribute("aria-label", "Toggle light and dark mode");
      adminToggle.setAttribute("title", theme === "light" ? "Switch to Dark Mode" : "Switch to Light Mode");
      adminToggle.innerHTML = `
        <span class="theme-toggle-track">
          <span class="theme-toggle-thumb">
            <span class="theme-toggle-icon icon-sun">☀️</span>
            <span class="theme-toggle-icon icon-moon">🌙</span>
          </span>
        </span>
        <span class="theme-toggle-label">${theme.toUpperCase()}</span>
      `;
      adminHeader.parentElement.insertBefore(adminToggle, adminHeader.parentElement.firstChild);
    }
  }
};
window.ThemeEngine = ThemeEngine;

// Immediately execute theme application to avoid any visual lag
try {
  ThemeEngine.setTheme(ThemeEngine.getTheme());
} catch(e) {}
"""

    # Insert ThemeEngine right before DOMContentLoaded
    if "const ThemeEngine =" not in content:
        content = content.replace(
            "// ==========================================================================\n// 2. CORE SYSTEM INITIALISATION\n// ==========================================================================",
            theme_engine_code + "\n// ==========================================================================\n// 2. CORE SYSTEM INITIALISATION\n// =========================================================================="
        )

    # Add ThemeEngine.init() to DOMContentLoaded
    if "ThemeEngine.init();" not in content:
        content = content.replace(
            "document.addEventListener(\"DOMContentLoaded\", () => {\n  const db = FestDB.getData();",
            "document.addEventListener(\"DOMContentLoaded\", () => {\n  ThemeEngine.init();\n  const db = FestDB.getData();"
        )

    # 2. Update initHeroCanvas with theme-aware colors
    old_hero_canvas = """function initHeroCanvas() {
  try {
    const canvas = document.getElementById("hero-canvas");
    if (!canvas) return;

    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReducedMotion) return;

    const ctx = canvas.getContext("2d");
    let width, height;
    let particles = [];
    let animationFrameId;
    let isVisible = true;

    function resize() {
      width = canvas.width = canvas.parentElement.offsetWidth || window.innerWidth;
      height = canvas.height = canvas.parentElement.offsetHeight || window.innerHeight;
      createParticles();
    }

    function createParticles() {
      particles = [];
      const count = Math.min(Math.floor(width / 24), 60);
      for (let i = 0; i < count; i++) {
        particles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -Math.random() * 0.7 - 0.2,
          radius: Math.random() * 2 + 1,
          color: Math.random() > 0.4 ? "rgba(165, 42, 42, " : "rgba(108, 64, 62, ",
          alpha: Math.random() * 0.7 + 0.2
        });
      }
    }

    function draw() {
      if (!isVisible) return;
      ctx.clearRect(0, 0, width, height);

      ctx.strokeStyle = "rgba(165, 42, 42, 0.06)";
      ctx.lineWidth = 1;
      const step = 45;
      for (let x = 0; x < width; x += step) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.stroke();
      }

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.y < 0) {
          p.y = height;
          p.x = Math.random() * width;
        }
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;

        ctx.fillStyle = p.color + p.alpha + ")";
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 85) {
            ctx.strokeStyle = `rgba(165, 42, 42, ${0.25 * (1 - dist / 85)})`;
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      }

      animationFrameId = requestAnimationFrame(draw);
    }

    window.addEventListener("resize", resize);
    resize();"""

    new_hero_canvas = """function initHeroCanvas() {
  try {
    const canvas = document.getElementById("hero-canvas");
    if (!canvas) return;

    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReducedMotion) return;

    const ctx = canvas.getContext("2d");
    let width, height;
    let particles = [];
    let animationFrameId;
    let isVisible = true;

    function getCanvasThemeColors() {
      const isLight = (document.documentElement.getAttribute("data-theme") || "dark") === "light";
      return {
        primary: isLight ? "rgba(91, 127, 255, " : "rgba(184, 29, 66, ",
        secondary: isLight ? "rgba(214, 199, 255, " : "rgba(122, 0, 38, ",
        grid: isLight ? "rgba(91, 127, 255, 0.08)" : "rgba(184, 29, 66, 0.06)",
        primaryRgb: isLight ? "91, 127, 255" : "184, 29, 66"
      };
    }

    function resize() {
      width = canvas.width = canvas.parentElement.offsetWidth || window.innerWidth;
      height = canvas.height = canvas.parentElement.offsetHeight || window.innerHeight;
      createParticles();
    }

    function createParticles() {
      particles = [];
      const colors = getCanvasThemeColors();
      const count = Math.min(Math.floor(width / 24), 60);
      for (let i = 0; i < count; i++) {
        particles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -Math.random() * 0.7 - 0.2,
          radius: Math.random() * 2 + 1,
          color: Math.random() > 0.4 ? colors.primary : colors.secondary,
          alpha: Math.random() * 0.7 + 0.2
        });
      }
    }

    function draw() {
      if (!isVisible) return;
      ctx.clearRect(0, 0, width, height);

      const colors = getCanvasThemeColors();
      ctx.strokeStyle = colors.grid;
      ctx.lineWidth = 1;
      const step = 45;
      for (let x = 0; x < width; x += step) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.stroke();
      }

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.y < 0) {
          p.y = height;
          p.x = Math.random() * width;
        }
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;

        ctx.fillStyle = p.color + p.alpha + ")";
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 85) {
            ctx.strokeStyle = `rgba(${colors.primaryRgb}, ${0.25 * (1 - dist / 85)})`;
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      }

      animationFrameId = requestAnimationFrame(draw);
    }

    window.addEventListener("resize", resize);
    window.addEventListener("themechange", () => {
      createParticles();
    });
    resize();"""

    content = content.replace(old_hero_canvas, new_hero_canvas)

    # 3. Replace dynamic card colors
    content = content.replace('color: #fff;', 'color: var(--text-primary);')
    content = content.replace('color: #ffffff;', 'color: var(--text-primary);')
    content = content.replace('color:#fff;', 'color: var(--text-primary);')

    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Updated js/main.js successfully!")

if __name__ == '__main__':
    update_main_js()
