import os, re

# 1. UPDATE INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Replace hero tagline & theme badge
old_hero_badge = '''        <!-- Fest Theme Pill -->
        <div class="hero-theme-badge">
          <span class="pulse-dot" aria-hidden="true"></span>
          <span>SOIS · PRESIDENCY UNIVERSITY · BENGALURU</span>
        </div>

        <!-- Giant Glitch Fest Title -->
        <h1 class="glitch-title" data-text="ARENIUM'27">ARENIUM'27</h1>

        <!-- 3-Part Tagline -->
        <p class="hero-tagline">
          <span class="tag-part">DISRUPT THE MATRIX</span>
          <span class="tag-sep">//</span>
          <span class="tag-part">IGNITE THE FUTURE</span>
          <span class="tag-sep">//</span>
          <span class="tag-part">ASCEND THE GRID</span>
        </p>'''

new_hero_badge = '''        <!-- Official 3D Crystal Logo Emblem -->
        <div style="display: flex; justify-content: center; margin-bottom: 1.2rem;">
          <img src="images/logo.jpg" alt="ARENIUM'27 Official Logo" style="width: 120px; height: 120px; border-radius: 24px; border: 2px solid var(--neon-cyan); box-shadow: 0 0 30px rgba(0, 240, 255, 0.45), 0 0 60px rgba(112, 0, 255, 0.35); object-fit: cover;">
        </div>

        <!-- Fest Theme Pill -->
        <div class="hero-theme-badge">
          <span class="pulse-dot" aria-hidden="true"></span>
          <span>PRESIDENCY SCHOOL OF INFORMATION SCIENCE (SOIS)</span>
        </div>

        <!-- Giant Glitch Fest Title -->
        <h1 class="glitch-title" data-text="ARENIUM'27">ARENIUM'27</h1>

        <!-- Official Tagline -->
        <p class="hero-tagline" style="letter-spacing: 4px;">
          <span class="tag-part" style="color: var(--neon-cyan);">THE ARENA OF INNOVATION</span>
        </p>
        <p style="font-family: var(--font-mono); color: var(--text-secondary); font-size: 0.85rem; letter-spacing: 2px; margin-top: -0.5rem; margin-bottom: 1.5rem;">
          INTER-COLLEGE TECH FEST · 4–5 FEBRUARY 2027 · ~500 PARTICIPANTS
        </p>'''

idx = idx.replace(old_hero_badge, new_hero_badge)

# Date badge in index.html
idx = idx.replace(
    '<span>MARCH 26 – 27, 2027 · MAIN AUDITORIUM &amp; LAB BLOCKS</span>',
    '<span>4–5 FEBRUARY 2027 · MAIN AUDITORIUM, OLD PRAYER HALL &amp; SEMINAR HALLS</span>'
)

# Update leadership & coordinators in index.html
idx = idx.replace('Dr. Mahalaxmi', 'Dr. C. Kalaiarasan')
idx = idx.replace('Dr. Vertimani Elgovan', 'Dr. K. G. Mohan')
idx = idx.replace('Keren Lios Daniel', 'Ms. Keren Lois Daniel')

# Update student coordinator designations in index.html
old_kaushal_card = '''          <div class="cyber-card team-card">
            <div class="team-photo-wrap">
              <img src="images/coord-kaushal.svg" alt="Kaushal Kumar" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">LEAD COORDINATOR</div>
            <h4 class="team-name">Kaushal Kumar</h4>
            <div class="team-role">Student Coordinator · SOIS</div>
            <a href="tel:+919108740761" class="team-phone-link" aria-label="Call Kaushal Kumar">
              <span>📞</span> +91 91087 40761
            </a>
          </div>'''

new_kaushal_card = '''          <div class="cyber-card team-card">
            <div class="team-photo-wrap">
              <img src="images/coord-kaushal.svg" alt="Kaushal Kumar Singh" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">FINANCE &amp; REGISTRATION MANAGER</div>
            <h4 class="team-name">Kaushal Kumar Singh</h4>
            <div class="team-role">5BCA01 (20241BCA0051) · SOIS</div>
            <a href="tel:+919108740761" class="team-phone-link" aria-label="Call Kaushal Kumar Singh">
              <span>📞</span> +91 91087 40761
            </a>
          </div>'''

idx = idx.replace(old_kaushal_card, new_kaushal_card)

old_ashlin_card = '''          <div class="cyber-card team-card">
            <div class="team-photo-wrap">
              <img src="images/coord-ashlin.svg" alt="Ashlin" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">COORDINATOR</div>
            <h4 class="team-name">Ashlin</h4>
            <div class="team-role">Student Coordinator · SOIS</div>
            <a href="tel:+918797686786" class="team-phone-link" aria-label="Call Ashlin">
              <span>📞</span> +91 87976 86786
            </a>
          </div>'''

new_ashlin_card = '''          <div class="cyber-card team-card">
            <div class="team-photo-wrap">
              <img src="images/coord-ashlin.svg" alt="Ashlin Siddharth" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">MARKETING &amp; REGISTRATION MANAGER</div>
            <h4 class="team-name">Ashlin Siddharth</h4>
            <div class="team-role">5BCADS01 · SOIS</div>
            <a href="tel:+918797686786" class="team-phone-link" aria-label="Call Ashlin Siddharth">
              <span>📞</span> +91 87976 86786
            </a>
          </div>'''

idx = idx.replace(old_ashlin_card, new_ashlin_card)

old_abhyas_card = '''          <div class="cyber-card team-card">
            <div class="team-photo-wrap">
              <img src="images/coord-abhyas.svg" alt="Abhyas Kathuria" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">COORDINATOR</div>
            <h4 class="team-name">Abhyas Kathuria</h4>
            <div class="team-role">Student Coordinator · SOIS</div>
            <a href="tel:+918595848421" class="team-phone-link" aria-label="Call Abhyas Kathuria">
              <span>📞</span> +91 85958 48421
            </a>
          </div>'''

new_abhyas_card = '''          <div class="cyber-card team-card">
            <div class="team-photo-wrap">
              <img src="images/coord-abhyas.svg" alt="Abhyas Kathuria" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">TECHNICAL MANAGER</div>
            <h4 class="team-name">Abhyas Kathuria</h4>
            <div class="team-role">5BCAAIML01 · SOIS</div>
            <a href="tel:+918595848421" class="team-phone-link" aria-label="Call Abhyas Kathuria">
              <span>📞</span> +91 85958 48421
            </a>
          </div>'''

idx = idx.replace(old_abhyas_card, new_abhyas_card)

old_vimal_card = '''          <div class="cyber-card team-card">
            <div class="team-photo-wrap">
              <img src="images/coord-vimal.svg" alt="Vimal" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">COORDINATOR</div>
            <h4 class="team-name">Vimal</h4>
            <div class="team-role">Student Coordinator · SOIS</div>
            <a href="tel:+919620192249" class="team-phone-link" aria-label="Call Vimal">
              <span>📞</span> +91 96201 92249
            </a>
          </div>'''

new_vimal_card = '''          <div class="cyber-card team-card">
            <div class="team-photo-wrap">
              <img src="images/coord-vimal.svg" alt="Vimal Raj" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">EVENT MANAGER</div>
            <h4 class="team-name">Vimal Raj</h4>
            <div class="team-role">5BCADS02 · SOIS</div>
            <a href="tel:+919620192249" class="team-phone-link" aria-label="Call Vimal Raj">
              <span>📞</span> +91 96201 92249
            </a>
          </div>'''

idx = idx.replace(old_vimal_card, new_vimal_card)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print('index.html updated.')


# 2. UPDATE CONTACT.HTML
with open('contact.html', 'r', encoding='utf-8') as f:
    cnt = f.read()

cnt = cnt.replace('Dr. Mahalaxmi', 'Dr. C. Kalaiarasan')
cnt = cnt.replace('Dr. Vertimani Elgovan', 'Dr. K. G. Mohan')
cnt = cnt.replace('Keren Lios Daniel', 'Ms. Keren Lois Daniel')
cnt = cnt.replace('Kaushal Kumar', 'Kaushal Kumar Singh')
cnt = cnt.replace('Ashlin', 'Ashlin Siddharth')
cnt = cnt.replace('Vimal', 'Vimal Raj')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(cnt)

print('contact.html updated.')


# 3. UPDATE SCHEDULE.HTML TABS
with open('schedule.html', 'r', encoding='utf-8') as f:
    sch = f.read()

sch = sch.replace('[DAY 01 // MARCH 26]', '[DAY 01 // 4 FEB 2027]')
sch = sch.replace('[DAY 02 // MARCH 27]', '[DAY 02 // 5 FEB 2027]')

with open('schedule.html', 'w', encoding='utf-8') as f:
    f.write(sch)

print('schedule.html updated.')
