import re

def refine_css():
    with open('css/style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add RGB component variables
    if "--primary-rgb:" not in content:
        content = content.replace(
            "--theme-mode: 'dark';",
            "--theme-mode: 'dark';\n  --primary-rgb: 184, 29, 66;\n  --secondary-rgb: 122, 0, 38;"
        )
        content = content.replace(
            "--theme-mode: 'light';",
            "--theme-mode: 'light';\n  --primary-rgb: 91, 127, 255;\n  --secondary-rgb: 214, 199, 255;"
        )

    # Replace hardcoded rgba
    content = content.replace("rgba(165, 42, 42,", "rgba(var(--primary-rgb),")
    content = content.replace("rgba(108, 64, 62,", "rgba(var(--secondary-rgb),")

    # Replace remaining hex
    content = content.replace("#A52A2A", "var(--theme-primary)")
    content = content.replace("#6C403E", "var(--theme-secondary)")
    content = content.replace("#090505", "var(--bg-core)")
    content = content.replace("#05040a", "var(--bg-core)")

    # Mobile group in header
    mobile_group_css = """
.header-mobile-group {
  display: none;
}
"""
    if ".header-mobile-group {" not in content:
        content = content.replace("/* Desktop Navigation */", mobile_group_css + "\n/* Desktop Navigation */")

    # Mobile group display in media query
    if ".header-mobile-group {" not in content[content.find("@media (max-width: 768px)"):]:
        content = content.replace(
            "/* Mobile Navigation Drawer */\n  .nav-toggle-btn {",
            "/* Mobile Navigation Drawer */\n  .header-mobile-group {\n    display: flex !important;\n    align-items: center;\n    gap: 0.6rem;\n  }\n  .nav-toggle-btn {"
        )

    # Admin portal theming overrides
    admin_theme_css = """
/* Admin Portal Dynamic Theme Rules */
body#admin-app {
  background: var(--bg-core) !important;
  color: var(--text-primary) !important;
}

#admin-lock-screen.admin-lock-overlay {
  background: radial-gradient(circle at center, var(--bg-surface-elevated) 0%, var(--bg-core) 100%) !important;
}

.admin-lock-card {
  background: var(--bg-surface) !important;
  border: 2px solid var(--theme-primary) !important;
  box-shadow: 0 0 50px rgba(var(--primary-rgb), 0.25), inset 0 0 30px rgba(var(--primary-rgb), 0.06) !important;
  color: var(--text-primary) !important;
}

.admin-gateway-logo {
  background: radial-gradient(circle, rgba(var(--primary-rgb), 0.22) 0%, var(--bg-surface-elevated) 100%) !important;
  border: 2px solid var(--theme-primary) !important;
  box-shadow: 0 0 25px rgba(var(--primary-rgb), 0.45) !important;
}

.admin-gateway-title {
  color: var(--text-primary) !important;
  text-shadow: 0 0 15px rgba(var(--primary-rgb), 0.5) !important;
}

.admin-passkey-glow {
  color: var(--theme-primary) !important;
  background: var(--bg-card) !important;
  border: 2px solid var(--theme-primary) !important;
  box-shadow: 0 0 25px rgba(var(--primary-rgb), 0.35) !important;
  text-shadow: 0 0 12px var(--theme-primary-glow) !important;
}

.admin-passkey-glow::placeholder {
  color: rgba(var(--primary-rgb), 0.45) !important;
}

.admin-eye-btn {
  color: var(--theme-primary) !important;
}

.admin-unlock-btn {
  background: linear-gradient(135deg, var(--theme-primary) 0%, var(--theme-secondary) 100%) !important;
  color: #ffffff !important;
  box-shadow: 0 0 25px rgba(var(--primary-rgb), 0.4) !important;
}

.admin-quick-pill {
  background: rgba(var(--primary-rgb), 0.08) !important;
  border: 1px dashed rgba(var(--primary-rgb), 0.35) !important;
  color: var(--theme-primary) !important;
}

/* Light Theme Contrast Enhancements */
[data-theme="light"] .brand-name {
  color: #1B2342;
  text-shadow: 0 0 8px rgba(91, 127, 255, 0.3);
}

[data-theme="light"] .btn-primary {
  color: #5B7FFF;
  border-color: #5B7FFF;
}

[data-theme="light"] .btn-primary:hover {
  background: #5B7FFF;
  color: #ffffff;
}

[data-theme="light"] .btn-register {
  color: #ffffff !important;
}

[data-theme="light"] .countdown-box .count-num {
  color: #1B2342;
  text-shadow: 0 0 10px rgba(91, 127, 255, 0.25);
}

[data-theme="light"] .cyber-ticker-highlight {
  color: #d97706;
  text-shadow: 0 0 8px rgba(217, 119, 6, 0.3);
}
"""
    if "/* Admin Portal Dynamic Theme Rules */" not in content:
        content += admin_theme_css

    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Refined css/style.css successfully!")

if __name__ == '__main__':
    refine_css()
