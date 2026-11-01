import os, re

# 1. UPDATE ADMIN.HTML
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

# Add sidebar button if not present
if 'data-tab="tab-certificates"' not in admin_html:
    admin_html = admin_html.replace(
        '<button type="button" class="admin-nav-btn" data-tab="tab-winners">\n        🏆 Winners &amp; Results\n      </button>',
        '<button type="button" class="admin-nav-btn" data-tab="tab-winners">\n        🏆 Winners &amp; Results\n      </button>\n      <button type="button" class="admin-nav-btn" data-tab="tab-certificates">\n        📜 Uploaded Certificates\n      </button>'
    )

# Add tab pane if not present
if 'id="tab-certificates"' not in admin_html:
    cert_pane = '''      <!-- --------------------------------------------------------------------
           TAB: UPLOADED CERTIFICATES & DOWNLOAD MANAGER
           -------------------------------------------------------------------- -->
      <div id="tab-certificates" class="admin-tab-pane" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
          <div>
            <span class="section-tag">[ACCREDITATION REPOSITORY]</span>
            <h2 style="font-family: var(--font-display); font-size: 1.6rem; color: #fff;">MANAGE PARTICIPANT CERTIFICATES</h2>
            <p style="color: var(--text-secondary); font-size: 0.85rem;">
              Upload, add, or edit event participation and merit certificates for online verification and student download.
            </p>
          </div>
          <button class="btn btn-primary" onclick="addNewAdminCertificate()">➕ ADD NEW CERTIFICATE</button>
        </div>

        <!-- Publish Certificates Toggle Box -->
        <div class="cyber-card" style="padding: 1.2rem; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: space-between; border-color: var(--neon-cyan);">
          <div>
            <strong style="color: #fff; font-size: 1rem; display: block;">ENABLE CERTIFICATE DOWNLOADS ON PUBLIC PORTAL</strong>
            <span style="font-size: 0.8rem; color: var(--text-secondary);">
              When active, participants can search and download their verified certificates on certificate.html.
            </span>
          </div>
          <label style="display: flex; align-items: center; gap: 0.5rem; font-family: var(--font-mono); color: var(--neon-cyan); cursor: pointer;">
            <input type="checkbox" id="admin-publish-certs-toggle" style="width: 20px; height: 20px; cursor: pointer;">
            <span>ACTIVE</span>
          </label>
        </div>

        <div style="overflow-x: auto;">
          <table class="admin-table">
            <thead>
              <tr>
                <th>Certificate ID</th>
                <th>Recipient / Team</th>
                <th>Event Name</th>
                <th>Award / Tier</th>
                <th>College</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="admin-certs-table-body">
              <!-- Rendered via renderAdminCertificates() -->
            </tbody>
          </table>
        </div>
      </div>
'''
    admin_html = admin_html.replace('      <!-- --------------------------------------------------------------------\n           TAB 6: ANNOUNCEMENTS & TICKER', cert_pane + '\n      <!-- --------------------------------------------------------------------\n           TAB 6: ANNOUNCEMENTS & TICKER')

# Update dates / names in admin.html
admin_html = admin_html.replace('Dr. Mahalaxmi', 'Dr. C. Kalaiarasan')
admin_html = admin_html.replace('Dr. Vertimani Elgovan', 'Dr. K. G. Mohan')
admin_html = admin_html.replace('Keren Lios Daniel', 'Ms. Keren Lois Daniel')
admin_html = admin_html.replace('2027-03-26T09:00:00+05:30', '2027-02-04T08:30:00+05:30')

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

print('admin.html updated successfully.')


# 2. UPDATE CERTIFICATE.HTML
with open('certificate.html', 'r', encoding='utf-8') as f:
    cert_html = f.read()

# Add Search & Instant Download section if not present
if 'id="cert-search-section"' not in cert_html:
    search_section = '''    <!-- ====================================================================
         VERIFIED CERTIFICATE SEARCH & DOWNLOAD SECTION
         ==================================================================== -->
    <section id="cert-search-section" style="padding: 0 0 2rem;">
      <div class="container">
        <div class="cyber-card" style="padding: 1.8rem; border-color: var(--neon-cyan); box-shadow: 0 0 25px rgba(0, 240, 255, 0.12);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.2rem;">
            <div>
              <span class="section-tag">[ACCREDITATION REPOSITORY]</span>
              <h2 style="font-family: var(--font-display); font-size: 1.35rem; color: #fff; margin: 0.3rem 0;">
                SEARCH &amp; DOWNLOAD EVENT CERTIFICATES
              </h2>
              <p style="color: var(--text-secondary); font-size: 0.85rem; max-width: 650px; line-height: 1.5;">
                Event certificates uploaded! Search by your <strong>Full Name</strong>, <strong>Team Name</strong>, or <strong>Certificate ID</strong> (e.g. <code>AR27-HCK-001</code>) to retrieve your official verified accreditation and download it instantly in 300 DPI high resolution.
              </p>
            </div>
            <div id="cert-published-badge" style="background: rgba(0, 240, 255, 0.1); border: 1px solid var(--neon-cyan); color: var(--neon-cyan); padding: 0.4rem 0.8rem; border-radius: 4px; font-family: var(--font-mono); font-size: 0.78rem;">
              ⚡ CERTIFICATES REPOSITORY LIVE
            </div>
          </div>

          <div style="display: flex; gap: 0.8rem; flex-wrap: wrap; margin-bottom: 1rem;">
            <input type="text" id="cert-search-input" class="admin-input" placeholder="Search by recipient name, team name, or certificate ID..." style="flex: 2; min-width: 260px;">
            <button type="button" id="cert-search-btn" class="btn btn-primary" style="flex: 1; min-width: 160px; justify-content: center;">
              🔍 SEARCH CERTIFICATE
            </button>
          </div>

          <div id="cert-search-results" style="display: none; margin-top: 1.2rem; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 1.2rem;">
            <!-- Populated dynamically via search -->
          </div>
        </div>
      </div>
    </section>
'''
    cert_html = cert_html.replace('    <!-- Certificate Studio Layout -->', search_section + '\n    <!-- Certificate Studio Layout -->')

# Update signatures in preview
cert_html = cert_html.replace('<div class="cert-sig-line">Dr. Mahalaxmi</div>\n                    <div class="cert-sig-role">Patron / Dean, SOIS</div>', '<div class="cert-sig-line">Dr. C. Kalaiarasan</div>\n                    <div class="cert-sig-role">Patron / Dean, SOIS</div>')
cert_html = cert_html.replace('<div class="cert-sig-line">Dr. Vertimani Elgovan</div>\n                    <div class="cert-sig-role">Head of Dept, SOIS</div>', '<div class="cert-sig-line">Dr. K. G. Mohan</div>\n                    <div class="cert-sig-role">Head of Dept, SOIS</div>')
cert_html = cert_html.replace('<div class="cert-sig-line">Keren Lios Daniel</div>\n                    <div class="cert-sig-role">Programme Organiser</div>', '<div class="cert-sig-line">Ms. Keren Lois Daniel</div>\n                    <div class="cert-sig-role">Overall Fest Coordinator</div>')

# Update date in preview
cert_html = cert_html.replace('March 26 &amp; 27, 2027', 'February 4 &amp; 5, 2027')
cert_html = cert_html.replace('March 26-27, 2027', 'February 4–5, 2027')

# Update certificate crest to official logo.jpg
cert_html = cert_html.replace('<img src="images/logo.svg" alt="ARENIUM 27 Brand Crest" class="cert-logo-seal" style="width: 140px; height: auto;">', '<img src="images/logo.jpg" alt="ARENIUM 27 Brand Crest" class="cert-logo-seal" style="width: 80px; height: 80px; border-radius: 12px; border: 1.5px solid var(--neon-cyan); object-fit: cover; margin-bottom: 0.6rem;">')

with open('certificate.html', 'w', encoding='utf-8') as f:
    f.write(cert_html)

print('certificate.html updated successfully.')
