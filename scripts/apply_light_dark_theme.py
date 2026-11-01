import re

def update_style_css():
    with open('css/style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. New theme variables definition
    theme_vars = """/* --------------------------------------------------------------------------
   1. CSS Custom Properties / Theme Variables
   -------------------------------------------------------------------------- */
:root,
[data-theme="dark"] {
  /* DARK THEME PALETTE: (#1F080A | #3B0E14 | #7A0026 | #B81D42 | #F8E8EB) */
  --theme-mode: 'dark';

  --bg-core: #1F080A;
  --bg-surface: rgba(59, 14, 20, 0.88);
  --bg-surface-elevated: rgba(75, 18, 26, 0.95);
  --bg-card: rgba(59, 14, 20, 0.78);
  --bg-card-hover: rgba(88, 22, 31, 0.92);

  --theme-primary: #B81D42;
  --theme-secondary: #7A0026;
  --theme-primary-glow: rgba(184, 29, 66, 0.55);
  --theme-secondary-glow: rgba(122, 0, 38, 0.55);

  --neon-cyan: #B81D42;
  --neon-cyan-glow: rgba(184, 29, 66, 0.55);
  --neon-cyan-subtle: rgba(184, 29, 66, 0.16);

  --neon-pink: #7A0026;
  --neon-pink-glow: rgba(122, 0, 38, 0.55);
  --neon-pink-subtle: rgba(122, 0, 38, 0.18);

  --neon-purple: #7A0026;
  --neon-purple-glow: rgba(122, 0, 38, 0.45);

  --neon-yellow: #ffb833;
  --neon-yellow-glow: rgba(255, 184, 51, 0.4);

  --border-neon: 1px solid rgba(184, 29, 66, 0.45);
  --border-pink: 1px solid rgba(122, 0, 38, 0.45);
  --border-color: rgba(184, 29, 66, 0.35);
  --border-glow-cyan: 0 0 15px rgba(184, 29, 66, 0.4);
  --border-glow-pink: 0 0 15px rgba(122, 0, 38, 0.4);

  --text-primary: #F8E8EB;
  --text-secondary: #d9b8be;
  --text-muted: #a3727b;
  --text-highlight: #ff3864;

  --btn-primary-bg: rgba(184, 29, 66, 0.12);
  --btn-primary-border: #B81D42;
  --btn-primary-color: #B81D42;
  --btn-primary-hover-bg: #B81D42;
  --btn-primary-hover-color: #F8E8EB;

  --btn-register-bg: linear-gradient(135deg, #B81D42, #7A0026);
  --btn-register-hover-bg: linear-gradient(135deg, #d82451, #960030);

  --btn-ghost-bg: rgba(255, 255, 255, 0.04);
  --btn-ghost-border: rgba(184, 29, 66, 0.35);

  --header-bg: rgba(31, 8, 10, 0.88);
  --header-shadow: 0 4px 20px rgba(0, 0, 0, 0.6), 0 1px 15px rgba(184, 29, 66, 0.15);
  --card-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(184, 29, 66, 0.2);

  --bg-radial-1: rgba(184, 29, 66, 0.18);
  --bg-radial-2: rgba(122, 0, 38, 0.15);
  --bg-grid: rgba(184, 29, 66, 0.05);

  --hero-overlay-1: rgba(31, 8, 10, 0.4);
  --hero-overlay-2: rgba(31, 8, 10, 0.85);
  --hero-overlay-3: rgba(31, 8, 10, 0.9);

  /* Typography */
  --font-display: 'Orbitron', 'Rajdhani', -apple-system, sans-serif;
  --font-heading: 'Rajdhani', 'Orbitron', sans-serif;
  --font-mono: 'JetBrains Mono', 'Share Tech Mono', monospace;

  /* Spacing Scale */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2.5rem;
  --space-2xl: 4rem;
  --space-3xl: 6rem;

  /* Layout */
  --container-max: 1240px;
  --nav-height: 76px;
  --transition-fast: 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-base: 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="light"] {
  /* LIGHT THEME PALETTE: (#F3EFEF | #E3EEF8 | #D6C7FF | #5B7FFF | #1B2342) */
  --theme-mode: 'light';

  --bg-core: #F3EFEF;
  --bg-surface: rgba(227, 238, 248, 0.88);
  --bg-surface-elevated: rgba(255, 255, 255, 0.95);
  --bg-card: rgba(227, 238, 248, 0.78);
  --bg-card-hover: rgba(255, 255, 255, 0.98);

  --theme-primary: #5B7FFF;
  --theme-secondary: #D6C7FF;
  --theme-primary-glow: rgba(91, 127, 255, 0.45);
  --theme-secondary-glow: rgba(214, 199, 255, 0.55);

  --neon-cyan: #5B7FFF;
  --neon-cyan-glow: rgba(91, 127, 255, 0.4);
  --neon-cyan-subtle: rgba(91, 127, 255, 0.12);

  --neon-pink: #7A5CFA;
  --neon-pink-glow: rgba(214, 199, 255, 0.5);
  --neon-pink-subtle: rgba(214, 199, 255, 0.2);

  --neon-purple: #D6C7FF;
  --neon-purple-glow: rgba(214, 199, 255, 0.4);

  --neon-yellow: #d97706;
  --neon-yellow-glow: rgba(217, 119, 6, 0.25);

  --border-neon: 1px solid rgba(91, 127, 255, 0.35);
  --border-pink: 1px solid rgba(214, 199, 255, 0.8);
  --border-color: rgba(91, 127, 255, 0.25);
  --border-glow-cyan: 0 0 15px rgba(91, 127, 255, 0.2);
  --border-glow-pink: 0 0 15px rgba(214, 199, 255, 0.35);

  --text-primary: #1B2342;
  --text-secondary: #323e61;
  --text-muted: #5e6b8f;
  --text-highlight: #3a5ce0;

  --btn-primary-bg: rgba(91, 127, 255, 0.1);
  --btn-primary-border: #5B7FFF;
  --btn-primary-color: #5B7FFF;
  --btn-primary-hover-bg: #5B7FFF;
  --btn-primary-hover-color: #ffffff;

  --btn-register-bg: linear-gradient(135deg, #5B7FFF, #4060db);
  --btn-register-hover-bg: linear-gradient(135deg, #446bf7, #304ec2);

  --btn-ghost-bg: rgba(27, 35, 66, 0.04);
  --btn-ghost-border: rgba(91, 127, 255, 0.3);

  --header-bg: rgba(243, 239, 239, 0.9);
  --header-shadow: 0 4px 20px rgba(27, 35, 66, 0.08), 0 1px 15px rgba(91, 127, 255, 0.08);
  --card-shadow: 0 10px 30px rgba(27, 35, 66, 0.08), 0 0 20px rgba(91, 127, 255, 0.1);

  --bg-radial-1: rgba(91, 127, 255, 0.12);
  --bg-radial-2: rgba(214, 199, 255, 0.18);
  --bg-grid: rgba(91, 127, 255, 0.06);

  --hero-overlay-1: rgba(243, 239, 239, 0.3);
  --hero-overlay-2: rgba(243, 239, 239, 0.8);
  --hero-overlay-3: rgba(243, 239, 239, 0.85);
}"""

    # Replace :root section
    root_pat = re.compile(r'/\* -+\s*1\. CSS Custom Properties[\s\S]*?--transition-base:[^}]+}', re.MULTILINE)
    content = root_pat.sub(theme_vars, content)

    # 2. Update html & body styles
    old_html_body = """html {
  font-size: 16px;
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--nav-height) + 20px);
  background-color: var(--bg-core);
  color: var(--text-primary);
  color-scheme: dark;
}

body {
  font-family: var(--font-mono);
  line-height: 1.6;
  background-color: var(--bg-core);
  background-image: 
    radial-gradient(circle at 50% 0%, rgba(165, 42, 42, 0.18) 0%, transparent 50%),
    radial-gradient(circle at 90% 40%, rgba(108, 64, 62, 0.15) 0%, transparent 45%),
    linear-gradient(rgba(165, 42, 42, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(165, 42, 42, 0.05) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
  background-attachment: fixed;
  overflow-x: hidden;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}"""

    new_html_body = """html {
  font-size: 16px;
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--nav-height) + 20px);
  background-color: var(--bg-core);
  color: var(--text-primary);
  color-scheme: dark;
  transition: background-color var(--transition-base), color var(--transition-base);
}

html[data-theme="light"] {
  color-scheme: light;
}

html[data-theme="dark"] {
  color-scheme: dark;
}

body {
  font-family: var(--font-mono);
  line-height: 1.6;
  background-color: var(--bg-core);
  background-image: 
    radial-gradient(circle at 50% 0%, var(--bg-radial-1) 0%, transparent 50%),
    radial-gradient(circle at 90% 40%, var(--bg-radial-2) 0%, transparent 45%),
    linear-gradient(var(--bg-grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--bg-grid) 1px, transparent 1px);
  background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
  background-attachment: fixed;
  overflow-x: hidden;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  transition: background-color var(--transition-base), color var(--transition-base);
}"""
    content = content.replace(old_html_body, new_html_body)

    # 3. Add Theme Toggle Styles
    toggle_styles = """
/* --------------------------------------------------------------------------
   Theme Toggle Cyber Switch
   -------------------------------------------------------------------------- */
.theme-toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  padding: 0.35rem 0.75rem;
  border-radius: 20px;
  cursor: pointer;
  color: var(--text-primary);
  font-family: var(--font-display);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  transition: all var(--transition-base);
  box-shadow: 0 0 10px var(--neon-cyan-subtle);
  user-select: none;
}

.theme-toggle-btn:hover {
  border-color: var(--theme-primary);
  box-shadow: 0 0 15px var(--theme-primary-glow);
  transform: translateY(-1px);
}

.theme-toggle-track {
  position: relative;
  width: 38px;
  height: 20px;
  background: rgba(0, 0, 0, 0.25);
  border-radius: 12px;
  border: 1px solid var(--border-color);
  display: inline-flex;
  align-items: center;
  padding: 2px;
  box-sizing: border-box;
  transition: all var(--transition-base);
}

[data-theme="light"] .theme-toggle-track {
  background: #D6C7FF;
  border-color: #5B7FFF;
}

[data-theme="dark"] .theme-toggle-track {
  background: #1F080A;
  border-color: #7A0026;
}

.theme-toggle-thumb {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.3s;
}

[data-theme="dark"] .theme-toggle-thumb {
  transform: translateX(18px);
  background: #B81D42;
  box-shadow: 0 0 8px #B81D42;
}

[data-theme="light"] .theme-toggle-thumb {
  transform: translateX(0px);
  background: #5B7FFF;
  box-shadow: 0 0 8px #5B7FFF;
}

.theme-toggle-icon {
  font-size: 10px;
  line-height: 1;
  position: absolute;
  transition: opacity 0.2s ease, transform 0.3s ease;
}

[data-theme="dark"] .theme-toggle-icon.icon-sun {
  opacity: 0;
  transform: rotate(-90deg) scale(0.5);
}

[data-theme="dark"] .theme-toggle-icon.icon-moon {
  opacity: 1;
  transform: rotate(0) scale(1);
}

[data-theme="light"] .theme-toggle-icon.icon-sun {
  opacity: 1;
  transform: rotate(0) scale(1);
}

[data-theme="light"] .theme-toggle-icon.icon-moon {
  opacity: 0;
  transform: rotate(90deg) scale(0.5);
}

.theme-toggle-label {
  font-size: 0.72rem;
  letter-spacing: 0.1em;
}

/* Compact mobile version */
.theme-toggle-btn.theme-toggle-btn-compact {
  padding: 0.35rem 0.45rem;
}

.theme-toggle-btn.theme-toggle-btn-compact .theme-toggle-label {
  display: none;
}
"""

    if ".theme-toggle-btn" not in content:
        content = content.replace("/* Cyber Buttons */", toggle_styles + "\n/* Cyber Buttons */")

    # 4. Update Header styles
    content = content.replace(
        "background: rgba(7, 6, 15, 0.88);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);\n  border-bottom: 1px solid rgba(165, 42, 42, 0.25);\n  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6), 0 1px 15px rgba(165, 42, 42, 0.1);",
        "background: var(--header-bg);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);\n  border-bottom: 1px solid var(--border-color);\n  box-shadow: var(--header-shadow);"
    )

    # 5. Dropdown menu
    content = content.replace(
        "background: rgba(10, 8, 20, 0.96);\n  border: 1px solid rgba(165, 42, 42, 0.4);\n  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), 0 0 15px rgba(165, 42, 42, 0.2);",
        "background: var(--bg-surface-elevated);\n  border: 1px solid var(--border-color);\n  box-shadow: var(--card-shadow);"
    )

    # 6. Hero overlay
    content = content.replace(
        "background: \n    linear-gradient(to bottom, rgba(7,6,15,0.4) 0%, rgba(7,6,15,0.85) 90%),\n    radial-gradient(circle at 50% 50%, transparent 20%, rgba(7,6,15,0.9) 80%);",
        "background: \n    linear-gradient(to bottom, var(--hero-overlay-1) 0%, var(--hero-overlay-2) 90%),\n    radial-gradient(circle at 50% 50%, transparent 20%, var(--hero-overlay-3) 80%);"
    )

    # 7. Countdown box
    content = content.replace(
        "background: rgba(13, 11, 26, 0.85);\n  border: 1px solid rgba(165, 42, 42, 0.4);",
        "background: var(--bg-surface);\n  border: 1px solid var(--border-color);"
    )
    content = content.replace(
        ".countdown-box .count-num {\n  font-family: var(--font-display);\n  font-size: clamp(2rem, 4vw, 3.2rem);\n  font-weight: 900;\n  color: #ffffff;",
        ".countdown-box .count-num {\n  font-family: var(--font-display);\n  font-size: clamp(2rem, 4vw, 3.2rem);\n  font-weight: 900;\n  color: var(--text-primary);"
    )

    # 8. Stat item
    content = content.replace(
        "background: rgba(7, 6, 15, 0.7);\n  border: 1px solid rgba(165, 42, 42, 0.2);",
        "background: var(--bg-surface);\n  border: 1px solid var(--border-color);"
    )

    # 9. Site footer
    content = content.replace(
        "background: #040308;\n  border-top: 1px solid rgba(165, 42, 42, 0.25);",
        "background: var(--bg-surface-elevated);\n  border-top: 1px solid var(--border-color);"
    )

    # 10. Filter chip
    content = content.replace(
        "background: rgba(13, 11, 26, 0.8);\n  border: 1px solid rgba(165, 42, 42, 0.3);",
        "background: var(--bg-card);\n  border: 1px solid var(--border-color);"
    )

    # 11. Event poster wrapper
    content = content.replace(
        "background: #080713;\n  border-bottom: 1px solid rgba(165, 42, 42, 0.2);",
        "background: var(--bg-surface);\n  border-bottom: 1px solid var(--border-color);"
    )

    # 12. Cyber ticker
    content = content.replace(
        "background: rgba(10, 8, 22, 0.96);\n  border-top: 1px solid rgba(165, 42, 42, 0.25);\n  border-bottom: 1px solid rgba(255, 230, 0, 0.35);",
        "background: var(--bg-surface-elevated);\n  border-top: 1px solid var(--border-color);\n  border-bottom: 1px solid var(--border-color);"
    )
    content = content.replace(
        "color: #ffffff;\n  text-shadow: 0 0 8px rgba(165, 42, 42, 0.5);",
        "color: var(--text-primary);\n  text-shadow: 0 0 8px var(--neon-cyan-glow);"
    )

    # 13. Mobile nav drawer
    content = content.replace(
        "background: rgba(6, 5, 14, 0.98);\n    backdrop-filter: blur(20px);\n    -webkit-backdrop-filter: blur(20px);\n    flex-direction: column;\n    align-items: flex-start;\n    padding: var(--space-xl) var(--space-lg);\n    gap: 1.2rem;\n    overflow-y: auto;\n    transform: translateX(100%);\n    transition: transform var(--transition-base);\n    border-top: 1px solid rgba(165, 42, 42, 0.2);",
        "background: var(--bg-surface-elevated);\n    backdrop-filter: blur(20px);\n    -webkit-backdrop-filter: blur(20px);\n    flex-direction: column;\n    align-items: flex-start;\n    padding: var(--space-xl) var(--space-lg);\n    gap: 1.2rem;\n    overflow-y: auto;\n    transform: translateX(100%);\n    transition: transform var(--transition-base);\n    border-top: 1px solid var(--border-color);"
    )

    # 14. Buttons
    content = content.replace(
        "linear-gradient(135deg, #A52A2A, #6C403E)",
        "var(--btn-register-bg)"
    )
    content = content.replace(
        "border: 1px solid #A52A2A;",
        "border: 1px solid var(--theme-primary);"
    )
    content = content.replace(
        "linear-gradient(135deg, #c93b3b, #8a4845)",
        "var(--btn-register-hover-bg)"
    )

    # 15. Admin input, select, textarea
    content = content.replace(
        "background: rgba(7, 6, 15, 0.85);\n  border: 1px solid rgba(165, 42, 42, 0.3);\n  color: #ffffff;",
        "background: var(--bg-card);\n  border: 1px solid var(--border-color);\n  color: var(--text-primary);"
    )

    # 16. Rulebook modal header
    content = content.replace(
        "background: rgba(7, 6, 15, 0.6);",
        "background: var(--bg-surface);"
    )

    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Updated css/style.css successfully!")

if __name__ == '__main__':
    update_style_css()
