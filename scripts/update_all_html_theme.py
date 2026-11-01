import os
import re

anti_fouc_script = """  <script>
    (function() {
      try {
        var t = localStorage.getItem('arenium_theme') || 'dark';
        document.documentElement.setAttribute('data-theme', t);
        document.documentElement.classList.add(t + '-theme');
      } catch (e) {}
    })();
  </script>
"""

desktop_toggle_html = """        <button class="theme-toggle-btn" id="theme-toggle-desktop" aria-label="Toggle light and dark mode" title="Switch Theme">
          <span class="theme-toggle-track">
            <span class="theme-toggle-thumb">
              <span class="theme-toggle-icon icon-sun">☀️</span>
              <span class="theme-toggle-icon icon-moon">🌙</span>
            </span>
          </span>
          <span class="theme-toggle-label">DARK</span>
        </button>"""

mobile_group_html = """      <!-- Mobile Navigation & Theme Toggle -->
      <div class="header-mobile-group">
        <button class="theme-toggle-btn theme-toggle-btn-compact" id="theme-toggle-mobile" aria-label="Toggle light and dark mode" title="Switch Theme">
          <span class="theme-toggle-track">
            <span class="theme-toggle-thumb">
              <span class="theme-toggle-icon icon-sun">☀️</span>
              <span class="theme-toggle-icon icon-moon">🌙</span>
            </span>
          </span>
        </button>
        <button class="nav-toggle-btn" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="primary-navigation">
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
        </button>
      </div>"""

mobile_drawer_toggle = """        <!-- Mobile Drawer Theme Switch -->
        <div class="nav-item mobile-only" style="margin-top: 0.5rem; width: 100%;">
          <button class="theme-toggle-btn" id="theme-toggle-drawer" style="width: 100%; justify-content: space-between; padding: 0.6rem 1rem;">
            <span style="font-family: var(--font-mono); font-size: 0.8rem;">THEME MATRIX</span>
            <span style="display: flex; align-items: center; gap: 0.5rem;">
              <span class="theme-toggle-track">
                <span class="theme-toggle-thumb">
                  <span class="theme-toggle-icon icon-sun">☀️</span>
                  <span class="theme-toggle-icon icon-moon">🌙</span>
                </span>
              </span>
              <span class="theme-toggle-label">DARK</span>
            </span>
          </button>
        </div>"""

def update_main_html_files():
    main_files = [
        'index.html', 'events.html', 'schedule.html', 'winners.html',
        'certificate.html', 'gallery.html', 'sponsors.html', 'contact.html'
    ]

    for fname in main_files:
        if not os.path.exists(fname):
            continue
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Anti-FOUC script
        if "localStorage.getItem('arenium_theme')" not in content:
            content = content.replace("<head>", "<head>\n" + anti_fouc_script)

        # 2. Desktop Toggle Button
        if 'id="theme-toggle-desktop"' not in content:
            content = re.sub(
                r'(<div class="header-action-desktop"[^>]*>)\s*(<a href="admin\.html")',
                r'\1\n' + desktop_toggle_html + r'\n        \2',
                content
            )

        # 3. Mobile Group Button
        if 'class="header-mobile-group"' not in content:
            old_nav_toggle_pat = re.compile(
                r'<!-- Mobile Navigation Hamburger -->\s*<button class="nav-toggle-btn"[^>]*>[\s\S]*?</button>',
                re.MULTILINE
            )
            if old_nav_toggle_pat.search(content):
                content = old_nav_toggle_pat.sub(mobile_group_html, content)
            else:
                old_nav_toggle_fallback = re.compile(
                    r'<button class="nav-toggle-btn" aria-label="Toggle navigation menu"[^>]*>[\s\S]*?</button>',
                    re.MULTILINE
                )
                content = old_nav_toggle_fallback.sub(mobile_group_html, content)

        # 4. Mobile Drawer Theme Switch
        if 'id="theme-toggle-drawer"' not in content:
            content = re.sub(
                r'(<!-- Mobile Register Button in Drawer -->)',
                mobile_drawer_toggle + r'\n\n        \1',
                content
            )

        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname} successfully!")

def update_admin_html():
    if not os.path.exists('admin.html'):
        return
    with open('admin.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Anti-FOUC
    if "localStorage.getItem('arenium_theme')" not in content:
        content = content.replace("<head>", "<head>\n" + anti_fouc_script)

    # 2. Lock screen toggle
    lock_toggle = """    <div style="position: absolute; top: 1.5rem; right: 1.5rem; z-index: 100000;">
      <button class="theme-toggle-btn" id="theme-toggle-lock" aria-label="Toggle light and dark mode" title="Switch Theme">
        <span class="theme-toggle-track">
          <span class="theme-toggle-thumb">
            <span class="theme-toggle-icon icon-sun">☀️</span>
            <span class="theme-toggle-icon icon-moon">🌙</span>
          </span>
        </span>
        <span class="theme-toggle-label">DARK</span>
      </button>
    </div>"""

    if 'id="theme-toggle-lock"' not in content:
        content = re.sub(
            r'(<div id="admin-lock-screen"[^>]*>)',
            r'\1\n' + lock_toggle,
            content
        )

    # 3. Admin bar toggle
    admin_bar_toggle = """          <button class="theme-toggle-btn" id="theme-toggle-admin" aria-label="Toggle light and dark mode" title="Switch Theme">
            <span class="theme-toggle-track">
              <span class="theme-toggle-thumb">
                <span class="theme-toggle-icon icon-sun">☀️</span>
                <span class="theme-toggle-icon icon-moon">🌙</span>
              </span>
            </span>
            <span class="theme-toggle-label">DARK</span>
          </button>"""

    if 'id="theme-toggle-admin"' not in content:
        content = re.sub(
            r'(<div style="display: flex; gap: 0\.8rem; align-items: center;">)\s*(<a href="index\.html")',
            r'\1\n' + admin_bar_toggle + r'\n          \2',
            content
        )

    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated admin.html successfully!")

if __name__ == '__main__':
    update_main_html_files()
    update_admin_html()
