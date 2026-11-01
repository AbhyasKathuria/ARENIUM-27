import re, os

# -----------------------------------------------------------------------------
# 1. UPDATE CSS/STYLE.CSS
# -----------------------------------------------------------------------------
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css_rules = '''
/* ==========================================================================
   USER EDITS: 3-TIER TEAM HIERARCHY, PU BRAND LOGO & HERO BADGES
   ========================================================================== */
.team-tier-block {
  margin-bottom: var(--space-2xl);
}

.team-tier-header {
  text-align: center;
  margin-bottom: var(--space-xl);
}

.team-tier-badge {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  letter-spacing: 2px;
  color: var(--neon-cyan);
  background: rgba(0, 240, 255, 0.08);
  border: 1px solid rgba(0, 240, 255, 0.3);
  padding: 0.25rem 0.8rem;
  border-radius: 20px;
  text-transform: uppercase;
}

[data-theme="light"] .team-tier-badge {
  color: #304EC2;
  background: rgba(48, 78, 194, 0.08);
  border-color: rgba(48, 78, 194, 0.3);
}

.team-tier-desc {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--text-secondary);
  letter-spacing: 1px;
  margin-top: 0.3rem;
}

.team-grid-leadership {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1.2rem;
}

@media (max-width: 1200px) {
  .team-grid-leadership {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .team-grid-leadership {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .team-grid-leadership {
    grid-template-columns: 1fr;
  }
}

.team-card-desc {
  font-size: 0.78rem;
  color: var(--text-secondary);
  margin-top: 0.5rem;
  line-height: 1.4;
}

.committee-members-box {
  margin-top: 0.75rem;
  padding: 0.6rem 0.8rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 6px;
  border-left: 2px solid var(--neon-cyan);
  text-align: left;
}

[data-theme="light"] .committee-members-box {
  background: rgba(48, 78, 194, 0.06);
  border-left-color: #304EC2;
}

.committee-label {
  display: block;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--neon-cyan);
  letter-spacing: 1px;
  margin-bottom: 0.25rem;
}

[data-theme="light"] .committee-label {
  color: #304EC2;
}

.committee-members-box p {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  color: var(--text-secondary);
  line-height: 1.4;
  margin: 0;
}

/* Header Navbar PU Logo & Divider */
.header-pu-logo {
  height: clamp(22px, 2.2vw, 30px);
  width: auto;
  max-width: 130px;
  object-fit: contain;
  transition: opacity 0.3s ease;
}

.brand-divider {
  width: 1px;
  height: 22px;
  background: rgba(255, 255, 255, 0.25);
  margin: 0 0.15rem;
  flex-shrink: 0;
}

[data-theme="light"] .brand-divider {
  background: rgba(0, 0, 0, 0.25);
}

.hero-subtagline {
  font-family: var(--font-mono);
  color: var(--text-secondary);
  font-size: 0.88rem;
  letter-spacing: 3px;
  margin-top: -0.5rem;
  margin-bottom: 1.5rem;
  font-weight: 600;
}

[data-theme="light"] .hero-subtagline {
  color: #3a4b78;
}

@media (max-width: 1140px) {
  .header-pu-logo {
    max-width: 110px;
    height: 24px;
  }
}

@media (max-width: 480px) {
  .header-pu-logo {
    max-width: 90px;
    height: 20px;
  }
  .brand-divider {
    height: 18px;
  }
}
'''

if 'USER EDITS: 3-TIER TEAM HIERARCHY' not in css:
    css += new_css_rules
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated css/style.css with 3-tier team & brand styles.")
else:
    print("css/style.css already has 3-tier team styles.")

# -----------------------------------------------------------------------------
# 2. UPDATE NAVBAR BRAND IN ALL HTML FILES
# -----------------------------------------------------------------------------
old_brand_markup = '''      <!-- Brand Logo & Wordmark -->
      <a href="index.html" class="brand-link" aria-label="ARENIUM 27 Home">
        <img src="images/logo.svg" alt="ARENIUM'27 Logo" class="brand-logo-img" width="160" height="40">
      </a>'''

new_brand_markup = '''      <!-- Brand Logo & Wordmark -->
      <a href="index.html" class="brand-link" aria-label="ARENIUM 27 Home">
        <img src="images/presidency-university-logo-dark.png" alt="Presidency University" class="header-pu-logo pu-logo-dark" width="130" height="26">
        <img src="images/presidency-university-logo-light.png" alt="Presidency University" class="header-pu-logo pu-logo-light" width="130" height="26">
        <span class="brand-divider" aria-hidden="true"></span>
        <img src="images/logo.svg" alt="ARENIUM'27 Logo" class="brand-logo-img" width="135" height="36">
      </a>'''

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_brand_markup in content:
        content = content.replace(old_brand_markup, new_brand_markup)
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated navbar brand in {hf}")
    elif 'header-pu-logo' not in content and 'class="brand-link"' in content:
        # Regex replacement if whitespace slightly differs
        content = re.sub(
            r'<a href="index\.html" class="brand-link"[^>]*>\s*<img src="images/logo\.svg"[^>]*>\s*</a>',
            new_brand_markup.strip(),
            content
        )
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated navbar brand (regex) in {hf}")

# -----------------------------------------------------------------------------
# 3. UPDATE INDEX.HTML HERO, ABOUT, AND 3-TIER TEAM SECTION
# -----------------------------------------------------------------------------
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Hero emblem: use clean transparent emblem
idx = re.sub(
    r'<img src="images/logo\.jpg" alt="ARENIUM\'27 Official Logo" class="hero-emblem-img">',
    r'<img src="images/logo-emblem-clean.png" alt="ARENIUM\'27 Official Logo Emblem" class="hero-emblem-img">',
    idx
)

# Hero subtagline: Remove ~500 participants and date
old_subtagline = '''        <p style="font-family: var(--font-mono); color: var(--text-secondary); font-size: 0.85rem; letter-spacing: 2px; margin-top: -0.5rem; margin-bottom: 1.5rem;">
          INTER-COLLEGE TECH FEST · 4–5 FEBRUARY 2027 · ~500 PARTICIPANTS
        </p>'''

new_subtagline = '''        <p class="hero-subtagline">
          INTER-COLLEGE TECH FEST
        </p>'''

idx = idx.replace(old_subtagline, new_subtagline)

# Hero date badge: Remove emoji, replace location with Presidency University
old_date_badge = '''        <!-- Event Date Badge -->
        <div class="hero-date-badge">
          <span aria-hidden="true">📅</span>
          <span>4–5 FEBRUARY 2027 · MAIN AUDITORIUM, OLD PRAYER HALL &amp; SEMINAR HALLS</span>
        </div>'''

new_date_badge = '''        <!-- Event Date & University Badge -->
        <div class="hero-date-badge">
          <span>4–5 FEBRUARY 2027 · PRESIDENCY UNIVERSITY</span>
        </div>'''

idx = idx.replace(old_date_badge, new_date_badge)

# About the fest: Rename section & update text
old_about_block = '''    <!-- ----------------------------------------------------------------------
         2. ABOUT SECTION
         ---------------------------------------------------------------------- -->
    <section class="about-section" id="about" aria-labelledby="about-heading">
      <div class="container">
        <div class="section-header reveal-on-scroll">
          <span class="section-tag">[01 // PROTOCOL]</span>
          <h2 class="section-title" id="about-heading">ABOUT THE FESTIVAL</h2>
          <p class="section-subtitle">Where cutting-edge technology converges with collegiate creativity and competition.</p>
        </div>

        <div class="cyber-card about-card reveal-on-scroll">
          <p class="about-text">
            <strong>ARENIUM'27</strong> is the premier annual national tech festival presented by the School of Information Science (SOIS) at Presidency University, Bengaluru. Designed as a high-octane proving ground, Arenium brings together coders, gamers, designers, innovators, and tech visionaries from across the nation to test their intellect and ignite digital transformation.
          </p>
          <p class="about-text">
            Immerse yourself in two adrenaline-fueled days of competitive coding battles, strategic LAN esports arenas, live cryptic treasure hunts, robotics and tech quizzes, creative design showdowns, and hands-on workshops guided by industry stalwarts. Whether you come to claim victory in the arenas or collaborate on revolutionary ideas, Arenium'27 is your portal to the next frontier of computing.
          </p>'''

new_about_block = '''    <!-- ----------------------------------------------------------------------
         2. ABOUT THE FEST SECTION
         ---------------------------------------------------------------------- -->
    <section class="about-section" id="about" aria-labelledby="about-heading">
      <div class="container">
        <div class="section-header reveal-on-scroll">
          <span class="section-tag">[01 // PROTOCOL]</span>
          <h2 class="section-title" id="about-heading">ABOUT THE FEST</h2>
          <p class="section-subtitle">The Arena of Innovation // Annual National Inter-College Tech Fest</p>
        </div>

        <div class="cyber-card about-card reveal-on-scroll">
          <p class="about-text">
            <strong>ARENIUM'27</strong> is the premier annual national tech festival presented by the <strong>Presidency School of Information Science (PSIS / SOIS)</strong> at <strong>Presidency University, Bengaluru</strong>. Designed as a high-octane proving ground under the theme <em>"The Arena of Innovation"</em>, Arenium convenes coders, innovators, developers, gamers, and tech visionaries from across the nation to test their intellect and ignite digital transformation.
          </p>
          <p class="about-text">
            Taking place on <strong>4–5 February 2027</strong> at the Presidency University campus, the fest features 10 dynamic competitive arenas including the flagship 24-Hour Hackathon, Blind Coding (Code in the Dark), Technical Treasure Hunt (Tech Trail), UI/UX DesignX, Data to Deployment (Data Tales), Prompt to Prototype, Startup Pitchthon (TechTalk), Gaming Arena (Valorant, BGMI, COD), Arenium Premier League (APL), and the Techno-Organic Synthesis Fashion Show.
          </p>'''

idx = idx.replace(old_about_block, new_about_block)

# Replace entire Section 5 Team in index.html
old_team_regex = r'<!-- -+\s*5\. TEAM STRIP SECTION\s*-+ -->\s*<section class="team-section" id="team"[\s\S]*?</section>'

new_team_section = '''<!-- ----------------------------------------------------------------------
         5. TEAM STRIP SECTION (ALIGNMENTS: TOP / MIDDLE / END)
         ---------------------------------------------------------------------- -->
    <section class="team-section" id="team" aria-labelledby="team-heading">
      <div class="container">
        <div class="section-header reveal-on-scroll">
          <span class="section-tag">[04 // CORE CREW]</span>
          <h2 class="section-title" id="team-heading">ORGANISING COMMITTEE</h2>
          <p class="section-subtitle">The visionary leadership, coordinators, and faculty organisation orchestrating ARENIUM'27.</p>
        </div>

        <!-- ==========================================
             1. TOP: UNIVERSITY LEADERSHIP & PATRONS
             ========================================== -->
        <div class="team-tier-block reveal-on-scroll">
          <div class="team-tier-header">
            <span class="team-tier-badge">TIER 01 // PATRONS</span>
            <h3 class="team-group-title" style="margin: 0.4rem 0;">UNIVERSITY LEADERSHIP</h3>
            <p class="team-tier-desc">Pro VC · VC · Dean · HOD · Head of UG Programmes</p>
          </div>
          
          <div class="team-grid team-grid-leadership" data-leadership-grid>
            <!-- 1. Pro VC -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/leader-provc.svg" alt="Dr. Vidya Shetty" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">PATRON / PRO VC</div>
              <h4 class="team-name">Dr. Vidya Shetty</h4>
              <div class="team-role">Pro Vice-Chancellor · Presidency University</div>
              <p class="team-card-desc">
                Guiding institutional growth, research initiatives, and academic excellence.
              </p>
            </div>

            <!-- 2. VC -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/leader-vc.svg" alt="Dr. S. J. Thiruvengadam" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">CHIEF PATRON / VC</div>
              <h4 class="team-name">Dr. S. J. Thiruvengadam</h4>
              <div class="team-role">Vice-Chancellor · Presidency University</div>
              <p class="team-card-desc">
                Leading Presidency University's strategic vision, global partnerships, and innovation.
              </p>
            </div>

            <!-- 3. Dean -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/leader-dean.svg" alt="Dr. C. Kalaiarasan" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">PATRON / DEAN</div>
              <h4 class="team-name">Dr. C. Kalaiarasan</h4>
              <div class="team-role">Dean · School of Information Science</div>
              <p class="team-card-desc">
                Guiding academic innovation, faculty research, and technical symposiums at SOIS.
              </p>
            </div>

            <!-- 4. HOD -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/leader-hod.svg" alt="Dr. K. G. Mohan" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">HEAD OF DEPARTMENT</div>
              <h4 class="team-name">Dr. K. G. Mohan</h4>
              <div class="team-role">HOD · School of Information Science</div>
              <p class="team-card-desc">
                Fostering competitive coding, student development, and technical curriculum standards.
              </p>
            </div>

            <!-- 5. UG Head -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/leader-ug.svg" alt="Dr. Vetrimani Elangovan" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">HEAD - UG PROGRAMMES</div>
              <h4 class="team-name">Dr. Vetrimani Elangovan</h4>
              <div class="team-role">Head of UG Programmes · PSIS</div>
              <p class="team-card-desc">
                Directing undergraduate computing specializations, student mentoring, and fest operations.
              </p>
            </div>
          </div>
        </div>

        <!-- ==========================================
             2. MIDDLE: COORDINATION & STUDENT MANAGEMENT
             ========================================== -->
        <div class="team-tier-block reveal-on-scroll" style="margin-top: var(--space-2xl);">
          <div class="team-tier-header">
            <span class="team-tier-badge">TIER 02 // OPERATIONS</span>
            <h3 class="team-group-title" style="margin: 0.4rem 0;">COORDINATION &amp; STUDENT LEADERSHIP</h3>
            <p class="team-tier-desc">Faculty Co-ordinator &amp; Programme Lead and Student Coordinators</p>
          </div>

          <!-- Faculty Coordinator & Program Lead Showcase -->
          <div class="cyber-card team-card" style="max-width: 520px; margin: 0 auto 1.5rem;">
            <div class="team-photo-wrap" style="height: 190px;">
              <img src="images/leader-organiser.svg" alt="Ms. Keren Lois Daniel" class="team-avatar-img" loading="lazy">
            </div>
            <div class="team-card-tag">FACULTY CO-ORDINATOR &amp; PROGRAMME LEAD</div>
            <h4 class="team-name" style="font-size: 1.25rem;">Ms. Keren Lois Daniel</h4>
            <div class="team-role">Assistant Professor &amp; Programme Organiser · Arenium'27</div>
            <p class="team-card-desc">
              Directing overall festival choreography, academic liaison, and student committee execution.
            </p>
          </div>

          <!-- Student Coordinators Grid -->
          <div class="team-grid" data-student-coords-grid>
            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/coord-kaushal.svg" alt="Kaushal Kumar Singh" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">FINANCE &amp; REGISTRATION MANAGER</div>
              <h4 class="team-name">Kaushal Kumar Singh</h4>
              <div class="team-role">5BCA01 (20241BCA0051) · SOIS</div>
              <a href="tel:+919108740761" class="team-phone-link" aria-label="Call Kaushal Kumar Singh">
                <span>📞</span> +91 91087 40761
              </a>
            </div>

            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/coord-vimal.svg" alt="Vimal Raj" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">EVENT MANAGER</div>
              <h4 class="team-name">Vimal Raj</h4>
              <div class="team-role">5BCADS02 · SOIS</div>
              <a href="tel:+919620192249" class="team-phone-link" aria-label="Call Vimal Raj">
                <span>📞</span> +91 96201 92249
              </a>
            </div>

            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/coord-ashlin.svg" alt="Ashlin Siddharth" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">MARKETING &amp; REGISTRATION MANAGER</div>
              <h4 class="team-name">Ashlin Siddharth</h4>
              <div class="team-role">5BCADS01 · SOIS</div>
              <a href="tel:+918797686786" class="team-phone-link" aria-label="Call Ashlin Siddharth">
                <span>📞</span> +91 87976 86786
              </a>
            </div>

            <div class="cyber-card team-card">
              <div class="team-photo-wrap">
                <img src="images/coord-abhyas.svg" alt="Abhyas Kathuria" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">TECHNICAL MANAGER</div>
              <h4 class="team-name">Abhyas Kathuria</h4>
              <div class="team-role">5BCAAIML01 · SOIS</div>
              <a href="tel:+918595848421" class="team-phone-link" aria-label="Call Abhyas Kathuria">
                <span>📞</span> +91 85958 48421
              </a>
            </div>
          </div>
        </div>

        <!-- ==========================================
             3. END: FACULTY ORGANISATIONS & FACULTY LEADS
             ========================================== -->
        <div class="team-tier-block reveal-on-scroll" style="margin-top: var(--space-2xl);">
          <div class="team-tier-header">
            <span class="team-tier-badge">TIER 03 // COMMITTEES</span>
            <h3 class="team-group-title" style="margin: 0.4rem 0;">FACULTY ORGANISATIONS &amp; FACULTY LEADS</h3>
            <p class="team-tier-desc">Faculty Committee Leads &amp; Student Teams</p>
          </div>

          <div class="team-grid" data-sois-committee-grid>
            <!-- 1. Marketing & PR -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap" style="height: 160px;">
                <img src="images/leader-neha.svg" alt="Ms. Neha Arora" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">MARKETING &amp; PR LEAD</div>
              <h4 class="team-name">Ms. Neha Arora</h4>
              <div class="team-role">Assistant Professor · SOIS</div>
              <div class="committee-members-box">
                <span class="committee-label">STUDENT TEAM:</span>
                <p>Anjani Soni M (5BCADS01), Rohit Roy (5BCA01), Saswata Chatterjee (5BCA02), Manas Kumar (5BCA02)</p>
              </div>
            </div>

            <!-- 2. Discipline -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap" style="height: 160px;">
                <img src="images/leader-sois.svg" alt="Mr. Krishna Mishra &amp; Mr. Dinesh N" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">DISCIPLINE &amp; SECURITY LEADS</div>
              <h4 class="team-name">Mr. Krishna Mishra &amp; Mr. Dinesh N</h4>
              <div class="team-role">Assistant Professors · SOIS</div>
              <div class="committee-members-box">
                <span class="committee-label">STUDENT TEAM:</span>
                <p>Hritik Raj (5BCA02), Vinayak Rathod (5BCA03), Kawatilya (5BCA01), Ayush Ranjan</p>
              </div>
            </div>

            <!-- 3. Decoration -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap" style="height: 160px;">
                <img src="images/leader-sois.svg" alt="Ms. Asha Hegde" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">DECORATION &amp; AMBIANCE LEAD</div>
              <h4 class="team-name">Ms. Asha Hegde</h4>
              <div class="team-role">Assistant Professor · SOIS</div>
              <div class="committee-members-box">
                <span class="committee-label">STUDENT TEAM:</span>
                <p>Ruchitha G (5BCADS01), Kavya Shree P M (5BCADS01), Nithyashree (5BCADS02), Bindu (5BCADS02)</p>
              </div>
            </div>

            <!-- 4. Hospitality & Refreshment -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap" style="height: 160px;">
                <img src="images/leader-sois.svg" alt="Ms. Nagma Fariyal &amp; Ms. Anjana" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">HOSPITALITY &amp; REFRESHMENT LEADS</div>
              <h4 class="team-name">Ms. Nagma Fariyal &amp; Ms. Anjana</h4>
              <div class="team-role">Assistant Professors · SOIS</div>
              <div class="committee-members-box">
                <span class="committee-label">STUDENT TEAM:</span>
                <p>Deepanita (5BCADS02), Arati Rai (5BCADS02), Manya Suresh (5BCA01), Harshita Periwal (5BCA03)</p>
              </div>
            </div>

            <!-- 5. Media -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap" style="height: 160px;">
                <img src="images/leader-sois.svg" alt="Ms. Ghazala Zameer &amp; Ms. Akasatha G R" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">MEDIA &amp; DOCUMENTATION LEADS</div>
              <h4 class="team-name">Ms. Ghazala Zameer &amp; Ms. Akasatha G R</h4>
              <div class="team-role">Assistant Professors · SOIS</div>
              <div class="committee-members-box">
                <span class="committee-label">STUDENT TEAM:</span>
                <p>Vidyanshi Jain (5BCAAIML01), Tanmayee L (5BCADS01), Kiran Kurien (5BCADS02)</p>
              </div>
            </div>

            <!-- 6. Registration -->
            <div class="cyber-card team-card">
              <div class="team-photo-wrap" style="height: 160px;">
                <img src="images/leader-sois.svg" alt="Ms. Devi S, Ms. Kalpana K &amp; Mr. Sudharshan" class="team-avatar-img" loading="lazy">
              </div>
              <div class="team-card-tag">REGISTRATION &amp; TICKETING LEADS</div>
              <h4 class="team-name">Ms. Devi S, Ms. Kalpana K &amp; Mr. Sudharshan</h4>
              <div class="team-role">Assistant Professors · SOIS</div>
              <div class="committee-members-box">
                <span class="committee-label">STUDENT TEAM:</span>
                <p>Shubham Kumar, Anchal Rodrigues, Naneshwaran, Rehana</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>'''

idx = re.sub(old_team_regex, new_team_section, idx)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)
print("Updated index.html hero, about the fest, and 3-tier team alignments.")

# -----------------------------------------------------------------------------
# 4. UPDATE CONTACT.HTML TEAM STRIP (3 TIERS)
# -----------------------------------------------------------------------------
with open('contact.html', 'r', encoding='utf-8') as f:
    ctc = f.read()

old_ctc_team_regex = r'<h2 class="team-group-title" style="margin-top: 0;">STUDENT COORDINATORS</h2>[\s\S]*?<!-- Registration Scanner Block again'

new_ctc_team_content = '''<!-- ==========================================
             1. TOP: UNIVERSITY LEADERSHIP & PATRONS
             ========================================== -->
            <div class="team-tier-block">
              <span class="team-tier-badge">TIER 01 // PATRONS</span>
              <h2 class="team-group-title" style="margin: 0.4rem 0;">UNIVERSITY LEADERSHIP</h2>
              <p class="team-tier-desc">Pro VC · VC · Dean · HOD · Head of UG Programmes</p>
              
              <div style="display: grid; gap: 1rem; margin-bottom: var(--space-xl);" data-leadership-grid>
                <!-- 1. Pro VC -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/leader-provc.svg" alt="Dr. Vidya Shetty" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">PATRON / PRO VC</div>
                  <h3 class="team-name">Dr. Vidya Shetty</h3>
                  <div class="team-role">Pro Vice-Chancellor · Presidency University</div>
                </div>

                <!-- 2. VC -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/leader-vc.svg" alt="Dr. S. J. Thiruvengadam" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">CHIEF PATRON / VC</div>
                  <h3 class="team-name">Dr. S. J. Thiruvengadam</h3>
                  <div class="team-role">Vice-Chancellor · Presidency University</div>
                </div>

                <!-- 3. Dean -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/leader-dean.svg" alt="Dr. C. Kalaiarasan" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">PATRON / DEAN</div>
                  <h3 class="team-name">Dr. C. Kalaiarasan</h3>
                  <div class="team-role">Dean · School of Information Science</div>
                </div>

                <!-- 4. HOD -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/leader-hod.svg" alt="Dr. K. G. Mohan" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">HEAD OF DEPARTMENT</div>
                  <h3 class="team-name">Dr. K. G. Mohan</h3>
                  <div class="team-role">HOD · School of Information Science</div>
                </div>

                <!-- 5. UG Head -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/leader-ug.svg" alt="Dr. Vetrimani Elangovan" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">HEAD - UG PROGRAMMES</div>
                  <h3 class="team-name">Dr. Vetrimani Elangovan</h3>
                  <div class="team-role">Head of UG Programmes · PSIS</div>
                </div>
              </div>
            </div>

            <!-- ==========================================
                 2. MIDDLE: COORDINATION & STUDENT MANAGEMENT
                 ========================================== -->
            <div class="team-tier-block">
              <span class="team-tier-badge">TIER 02 // OPERATIONS</span>
              <h2 class="team-group-title" style="margin: 0.4rem 0;">COORDINATION &amp; STUDENT LEADERSHIP</h2>
              <p class="team-tier-desc">Faculty Co-ordinator &amp; Programme Lead and Student Coordinators</p>

              <!-- Faculty Coordinator & Program Lead Showcase -->
              <div class="cyber-card team-card" style="margin-bottom: 1rem;">
                <div class="team-photo-wrap" style="height: 180px;">
                  <img src="images/leader-organiser.svg" alt="Ms. Keren Lois Daniel" class="team-avatar-img" loading="lazy">
                </div>
                <div class="team-card-tag">FACULTY CO-ORDINATOR &amp; PROGRAMME LEAD</div>
                <h3 class="team-name">Ms. Keren Lois Daniel</h3>
                <div class="team-role">Assistant Professor &amp; Programme Organiser · Arenium'27</div>
              </div>

              <!-- Student Coordinators Grid -->
              <div style="display: grid; gap: 1rem; margin-bottom: var(--space-xl);" data-student-coords-grid>
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/coord-kaushal.svg" alt="Kaushal Kumar Singh" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">FINANCE &amp; REGISTRATION MANAGER</div>
                  <h3 class="team-name">Kaushal Kumar Singh</h3>
                  <div class="team-role">5BCA01 (20241BCA0051) · SOIS</div>
                  <a href="tel:+919108740761" class="team-phone-link" aria-label="Call Kaushal Kumar Singh">
                    <span>📞</span> +91 91087 40761
                  </a>
                </div>

                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/coord-vimal.svg" alt="Vimal Raj" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">EVENT MANAGER</div>
                  <h3 class="team-name">Vimal Raj</h3>
                  <div class="team-role">5BCADS02 · SOIS</div>
                  <a href="tel:+919620192249" class="team-phone-link" aria-label="Call Vimal Raj">
                    <span>📞</span> +91 96201 92249
                  </a>
                </div>

                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/coord-ashlin.svg" alt="Ashlin Siddharth" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">MARKETING &amp; REGISTRATION MANAGER</div>
                  <h3 class="team-name">Ashlin Siddharth</h3>
                  <div class="team-role">5BCADS01 · SOIS</div>
                  <a href="tel:+918797686786" class="team-phone-link" aria-label="Call Ashlin Siddharth">
                    <span>📞</span> +91 87976 86786
                  </a>
                </div>

                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 180px;">
                    <img src="images/coord-abhyas.svg" alt="Abhyas Kathuria" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">TECHNICAL MANAGER</div>
                  <h3 class="team-name">Abhyas Kathuria</h3>
                  <div class="team-role">5BCAAIML01 · SOIS</div>
                  <a href="tel:+918595848421" class="team-phone-link" aria-label="Call Abhyas Kathuria">
                    <span>📞</span> +91 85958 48421
                  </a>
                </div>
              </div>
            </div>

            <!-- ==========================================
                 3. END: FACULTY ORGANISATIONS & FACULTY LEADS
                 ========================================== -->
            <div class="team-tier-block">
              <span class="team-tier-badge">TIER 03 // COMMITTEES</span>
              <h2 class="team-group-title" style="margin: 0.4rem 0;">FACULTY ORGANISATIONS &amp; FACULTY LEADS</h2>
              <p class="team-tier-desc">Faculty Committee Leads &amp; Student Teams</p>

              <div style="display: grid; gap: 1rem;" data-sois-committee-grid>
                <!-- 1. Marketing & PR -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 150px;">
                    <img src="images/leader-neha.svg" alt="Ms. Neha Arora" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">MARKETING &amp; PR LEAD</div>
                  <h3 class="team-name">Ms. Neha Arora</h3>
                  <div class="team-role">Assistant Professor · SOIS</div>
                  <div class="committee-members-box">
                    <span class="committee-label">STUDENT TEAM:</span>
                    <p>Anjani Soni M (5BCADS01), Rohit Roy (5BCA01), Saswata Chatterjee (5BCA02), Manas Kumar (5BCA02)</p>
                  </div>
                </div>

                <!-- 2. Discipline -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 150px;">
                    <img src="images/leader-sois.svg" alt="Mr. Krishna Mishra &amp; Mr. Dinesh N" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">DISCIPLINE &amp; SECURITY LEADS</div>
                  <h3 class="team-name">Mr. Krishna Mishra &amp; Mr. Dinesh N</h3>
                  <div class="team-role">Assistant Professors · SOIS</div>
                  <div class="committee-members-box">
                    <span class="committee-label">STUDENT TEAM:</span>
                    <p>Hritik Raj (5BCA02), Vinayak Rathod (5BCA03), Kawatilya (5BCA01), Ayush Ranjan</p>
                  </div>
                </div>

                <!-- 3. Decoration -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 150px;">
                    <img src="images/leader-sois.svg" alt="Ms. Asha Hegde" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">DECORATION &amp; AMBIANCE LEAD</div>
                  <h3 class="team-name">Ms. Asha Hegde</h3>
                  <div class="team-role">Assistant Professor · SOIS</div>
                  <div class="committee-members-box">
                    <span class="committee-label">STUDENT TEAM:</span>
                    <p>Ruchitha G (5BCADS01), Kavya Shree P M (5BCADS01), Nithyashree (5BCADS02), Bindu (5BCADS02)</p>
                  </div>
                </div>

                <!-- 4. Hospitality & Refreshment -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 150px;">
                    <img src="images/leader-sois.svg" alt="Ms. Nagma Fariyal &amp; Ms. Anjana" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">HOSPITALITY &amp; REFRESHMENT LEADS</div>
                  <h3 class="team-name">Ms. Nagma Fariyal &amp; Ms. Anjana</h3>
                  <div class="team-role">Assistant Professors · SOIS</div>
                  <div class="committee-members-box">
                    <span class="committee-label">STUDENT TEAM:</span>
                    <p>Deepanita (5BCADS02), Arati Rai (5BCADS02), Manya Suresh (5BCA01), Harshita Periwal (5BCA03)</p>
                  </div>
                </div>

                <!-- 5. Media -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 150px;">
                    <img src="images/leader-sois.svg" alt="Ms. Ghazala Zameer &amp; Ms. Akasatha G R" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">MEDIA &amp; DOCUMENTATION LEADS</div>
                  <h3 class="team-name">Ms. Ghazala Zameer &amp; Ms. Akasatha G R</h3>
                  <div class="team-role">Assistant Professors · SOIS</div>
                  <div class="committee-members-box">
                    <span class="committee-label">STUDENT TEAM:</span>
                    <p>Vidyanshi Jain (5BCAAIML01), Tanmayee L (5BCADS01), Kiran Kurien (5BCADS02)</p>
                  </div>
                </div>

                <!-- 6. Registration -->
                <div class="cyber-card team-card">
                  <div class="team-photo-wrap" style="height: 150px;">
                    <img src="images/leader-sois.svg" alt="Ms. Devi S, Ms. Kalpana K &amp; Mr. Sudharshan" class="team-avatar-img" loading="lazy">
                  </div>
                  <div class="team-card-tag">REGISTRATION &amp; TICKETING LEADS</div>
                  <h3 class="team-name">Ms. Devi S, Ms. Kalpana K &amp; Mr. Sudharshan</h3>
                  <div class="team-role">Assistant Professors · SOIS</div>
                  <div class="committee-members-box">
                    <span class="committee-label">STUDENT TEAM:</span>
                    <p>Shubham Kumar, Anchal Rodrigues, Naneshwaran, Rehana</p>
                  </div>
                </div>
              </div>
            </div>

          </div>

        </div>

        <!-- Registration Scanner Block again'''

ctc = re.sub(old_ctc_team_regex, new_ctc_team_content, ctc)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(ctc)
print("Updated contact.html team directory with 3-tier alignments.")

print("All updates applied successfully!")
