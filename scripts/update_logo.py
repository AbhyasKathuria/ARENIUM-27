import base64

with open('images/logo_emblem.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 80" width="320" height="80">
  <defs>
    <filter id="logoGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Official 3D Isometric Crystal A Emblem -->
  <g transform="translate(8, 6)">
    <rect x="0" y="0" width="68" height="68" rx="14" fill="#0c0d15" stroke="rgba(0, 240, 255, 0.45)" stroke-width="1.5"/>
    <clipPath id="logoClip">
      <rect x="1" y="1" width="66" height="66" rx="13"/>
    </clipPath>
    <image href="data:image/png;base64,{b64}" x="-3" y="-3" width="74" height="74" clip-path="url(#logoClip)" preserveAspectRatio="xMidYMid slice"/>
  </g>

  <!-- Typography: ARENIUM '27 and The Arena of Innovation -->
  <g transform="translate(88, 20)">
    <text x="0" y="26" font-family="'Orbitron', 'Rajdhani', sans-serif" font-weight="900" font-size="26" letter-spacing="3" fill="#ffffff">
      ARENIUM<tspan fill="#00f0ff">'</tspan><tspan fill="#ff007f">27</tspan>
    </text>
    <text x="2" y="45" font-family="'JetBrains Mono', monospace" font-weight="600" font-size="8.5" letter-spacing="2" fill="#00f0ff" opacity="0.9">
      THE ARENA OF INNOVATION // SOIS
    </text>
  </g>
</svg>'''

with open('images/logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
print('images/logo.svg updated successfully.')
