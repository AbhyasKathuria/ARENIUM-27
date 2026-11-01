import os

def make_avatar_svg(filename, title_text, neon_color1, neon_color2, label_name):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad_{title_text}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080a14"/>
      <stop offset="100%" stop-color="#141728"/>
    </linearGradient>
    <linearGradient id="neonGrad_{title_text}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{neon_color1}"/>
      <stop offset="100%" stop-color="{neon_color2}"/>
    </linearGradient>
    <filter id="glow_{title_text}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <rect width="400" height="400" fill="url(#bgGrad_{title_text})"/>
  
  <g stroke="rgba(255, 255, 255, 0.06)" stroke-width="1">
    <line x1="0" y1="80" x2="400" y2="80"/>
    <line x1="0" y1="160" x2="400" y2="160"/>
    <line x1="0" y1="240" x2="400" y2="240"/>
    <line x1="0" y1="320" x2="400" y2="320"/>
    <line x1="80" y1="0" x2="80" y2="400"/>
    <line x1="160" y1="0" x2="160" y2="400"/>
    <line x1="240" y1="0" x2="240" y2="400"/>
    <line x1="320" y1="0" x2="320" y2="400"/>
  </g>

  <polygon points="200,30 350,116 350,284 200,370 50,284 50,116" fill="rgba(10, 12, 26, 0.85)" stroke="url(#neonGrad_{title_text})" stroke-width="3.5" filter="url(#glow_{title_text})"/>
  <polygon points="200,45 335,123 335,277 200,355 65,277 65,123" fill="none" stroke="{neon_color1}" stroke-width="1" stroke-dasharray="6,4" opacity="0.4"/>

  <path d="M120 340 C120 275, 150 255, 200 255 C250 255, 280 275, 280 340 Z" fill="#171c33" stroke="{neon_color1}" stroke-width="2"/>
  <path d="M140 340 L165 270 L235 270 L260 340 Z" fill="#222a4d"/>
  
  <ellipse cx="200" cy="180" rx="52" ry="65" fill="#171c33" stroke="{neon_color2}" stroke-width="2"/>
  <path d="M148 170 C145 130, 165 110, 200 110 C235 110, 255 130, 252 170 C240 140, 160 140, 148 170 Z" fill="{neon_color2}" opacity="0.85"/>
  <path d="M158 175 L242 175 L235 192 L165 192 Z" fill="{neon_color1}" filter="url(#glow_{title_text})"/>
  <line x1="150" y1="183" x2="250" y2="183" stroke="#ffffff" stroke-width="1.5"/>
  
  <circle cx="200" cy="270" r="5" fill="{neon_color1}"/>
  <line x1="180" y1="270" x2="220" y2="270" stroke="{neon_color1}" stroke-width="2"/>
  
  <path d="M 20 50 L 20 20 L 50 20" fill="none" stroke="{neon_color1}" stroke-width="2"/>
  <path d="M 380 50 L 380 20 L 350 20" fill="none" stroke="{neon_color1}" stroke-width="2"/>
  <path d="M 20 350 L 20 380 L 50 380" fill="none" stroke="{neon_color1}" stroke-width="2"/>
  <path d="M 380 350 L 380 380 L 350 380" fill="none" stroke="{neon_color1}" stroke-width="2"/>
  
  <rect x="45" y="348" width="310" height="28" rx="4" fill="#080a14" stroke="{neon_color1}" stroke-width="1.5"/>
  <text x="200" y="367" font-family="'Orbitron', monospace, sans-serif" font-size="11" font-weight="800" fill="{neon_color1}" text-anchor="middle" letter-spacing="1.5">{label_name}</text>
</svg>'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'Wrote {filename}')

if __name__ == '__main__':
    make_avatar_svg('images/leader-provc.svg', 'PRO_VC', '#e6a100', '#B81D42', 'DR. VIDYA SHETTY')
    make_avatar_svg('images/leader-vc.svg', 'VC', '#ffd700', '#00f0ff', 'DR. S. J. THIRUVENGADAM')
    make_avatar_svg('images/leader-dean.svg', 'DEAN', '#00f0ff', '#B81D42', 'DR. C. KALAIARASAN')
    make_avatar_svg('images/leader-hod.svg', 'HOD', '#9d4edd', '#00f0ff', 'DR. K. G. MOHAN')
    make_avatar_svg('images/leader-ug.svg', 'UG', '#00f0ff', '#304EC2', 'DR. VETRIMANI ELANGOVAN')
