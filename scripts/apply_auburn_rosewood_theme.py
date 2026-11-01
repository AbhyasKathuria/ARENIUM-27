import re

def update_style_css():
    with open('css/style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update :root
    new_root = """/* --------------------------------------------------------------------------
   1. CSS Custom Properties / Theme Variables
   -------------------------------------------------------------------------- */
:root {
  /* Auburn & Rosewood Theme Palette (#A52A2A & #6C403E) */
  --theme-primary: #A52A2A;
  --theme-secondary: #6C403E;
  --theme-primary-glow: rgba(165, 42, 42, 0.55);
  --theme-secondary-glow: rgba(108, 64, 62, 0.55);

  --bg-core: #090505;
  --bg-surface: rgba(22, 12, 12, 0.85);
  --bg-surface-elevated: rgba(32, 16, 16, 0.92);
  --bg-card: rgba(26, 14, 14, 0.75);
  --bg-card-hover: rgba(44, 22, 22, 0.9);

  /* Neon Accents mapped to Auburn Crimson (#A52A2A) & Rosewood (#6C403E) */
  --neon-cyan: #ff5252;
  --neon-cyan-glow: rgba(165, 42, 42, 0.55);
  --neon-cyan-subtle: rgba(165, 42, 42, 0.16);

  --neon-pink: #c9534e;
  --neon-pink-glow: rgba(108, 64, 62, 0.55);
  --neon-pink-subtle: rgba(108, 64, 62, 0.18);

  --neon-purple: #6C403E;
  --neon-purple-glow: rgba(108, 64, 62, 0.45);

  --neon-yellow: #ffb833;
  --neon-yellow-glow: rgba(255, 184, 51, 0.4);

  /* Borders & Grid */
  --border-neon: 1px solid rgba(165, 42, 42, 0.45);
  --border-pink: 1px solid rgba(108, 64, 62, 0.45);
  --border-glow-cyan: 0 0 15px rgba(165, 42, 42, 0.4);
  --border-glow-pink: 0 0 15px rgba(108, 64, 62, 0.4);

  /* Typography */
  --font-display: 'Orbitron', 'Rajdhani', -apple-system, sans-serif;
  --font-heading: 'Rajdhani', 'Orbitron', sans-serif;
  --font-mono: 'JetBrains Mono', 'Share Tech Mono', monospace;

  --text-primary: #fdf5f4;
  --text-secondary: #c9a7a5;
  --text-muted: #8d6f6d;
  --text-highlight: #ff5252;

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
}"""

    root_pat = re.compile(r'/\* -+\s*1\. CSS Custom Properties[\s\S]*?--transition-base:[^}]+}', re.MULTILINE)
    content = root_pat.sub(new_root, content)

    # 2. Update body background
    old_body_bg = """  background-image: 
    radial-gradient(circle at 50% 0%, rgba(112, 0, 255, 0.12) 0%, transparent 50%),
    radial-gradient(circle at 90% 40%, rgba(255, 0, 85, 0.08) 0%, transparent 45%),
    linear-gradient(rgba(0, 240, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 240, 255, 0.03) 1px, transparent 1px);"""

    new_body_bg = """  background-image: 
    radial-gradient(circle at 50% 0%, rgba(165, 42, 42, 0.18) 0%, transparent 50%),
    radial-gradient(circle at 90% 40%, rgba(108, 64, 62, 0.15) 0%, transparent 45%),
    linear-gradient(rgba(165, 42, 42, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(165, 42, 42, 0.05) 1px, transparent 1px);"""

    content = content.replace(old_body_bg, new_body_bg)

    # 3. Replace all remaining hardcoded rgba colors
    content = content.replace("rgba(0, 240, 255,", "rgba(165, 42, 42,")
    content = content.replace("rgba(255, 0, 85,", "rgba(108, 64, 62,")
    content = content.replace("#07060f", "#090505")

    # 4. Update button styles
    content = content.replace("linear-gradient(135deg, var(--neon-pink), #b3003b)", "linear-gradient(135deg, #A52A2A, #6C403E)")
    content = content.replace("border: 1px solid #ff4d88;", "border: 1px solid #A52A2A;")

    # 5. Update admin passkey glow
    content = content.replace("border: 2px solid var(--neon-cyan) !important;", "border: 2px solid #A52A2A !important;")
    content = content.replace("color: #00f0ff !important;", "color: #ff5252 !important;")

    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Updated css/style.css successfully!")

if __name__ == '__main__':
    update_style_css()
