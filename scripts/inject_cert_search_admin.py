import os

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update initAdminPanel to include renderAdminCertificates(db)
if 'renderAdminCertificates(db);' not in js:
    js = js.replace(
        '  renderAdminWinners(db);\n  renderAdminSponsors(db);',
        '  renderAdminWinners(db);\n  renderAdminCertificates(db);\n  renderAdminSponsors(db);'
    )

# 2. Add admin certificate rendering and CRUD functions
admin_cert_code = '''
function renderAdminCertificates(db) {
  const publishToggle = document.getElementById("admin-publish-certs-toggle");
  if (publishToggle) {
    publishToggle.checked = !!db.settings.certificatesPublished;
    publishToggle.addEventListener("change", () => {
      db.settings.certificatesPublished = publishToggle.checked;
      FestDB.saveData(db);
      alert(publishToggle.checked ? "Participant Certificate Downloads are now ENABLED on certificate.html!" : "Participant Certificate Downloads are now DISABLED.");
    });
  }

  const container = document.getElementById("admin-certs-table-body");
  if (!container) return;
  container.innerHTML = "";

  const certs = db.certificates || [];
  if (certs.length === 0) {
    container.innerHTML = `<tr><td colspan="6" style="text-align:center; color:var(--text-muted); padding:1.5rem;">No issued certificates uploaded yet. Click "Add New Certificate" above.</td></tr>`;
    return;
  }

  certs.forEach((c) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td><strong style="color:var(--neon-cyan); font-family:var(--font-mono);">${c.id}</strong></td>
      <td><strong>${c.recipient}</strong></td>
      <td>${c.event}</td>
      <td><span class="event-category-badge" style="font-size:0.7rem;">${c.award}</span></td>
      <td>${c.college || 'Presidency University'}</td>
      <td>
        <button class="btn btn-ghost" style="padding:0.25rem 0.5rem; font-size:0.75rem;" onclick="editAdminCertificate('${c.id}')">✏️ Edit</button>
        <button class="btn btn-ghost" style="padding:0.25rem 0.5rem; font-size:0.75rem; color:var(--neon-pink); border-color:var(--neon-pink);" onclick="deleteAdminCertificate('${c.id}')">🗑️ Delete</button>
      </td>
    `;
    container.appendChild(tr);
  });
}

window.addNewAdminCertificate = function() {
  const db = FestDB.getData();
  const recipient = prompt("Recipient Student or Team Name:");
  if (!recipient) return;
  const eventName = prompt("Event Name (e.g. TECHVERSE ’27, TECH TRAIL, CODE IN THE DARK):") || "TECHVERSE ’27";
  const award = prompt("Award / Tier (e.g. CHAMPION // FIRST PLACE, RUNNER UP, PARTICIPATION):") || "CERTIFICATE OF MERIT & PARTICIPATION";
  const college = prompt("College / University:", "Presidency University, Bengaluru") || "Presidency University, Bengaluru";
  const id = prompt("Certificate ID (e.g. AR27-CRT-" + Math.floor(100 + Math.random() * 900) + "):") || ("AR27-CRT-" + Date.now().toString().slice(-4));
  const issueDate = prompt("Issue Date (e.g. 5 February 2027):", "5 February 2027") || "5 February 2027";

  if (!db.certificates) db.certificates = [];
  db.certificates.push({
    id,
    recipient,
    event: eventName,
    award,
    college,
    issueDate,
    verified: true
  });

  FestDB.saveData(db);
  alert(`Certificate ${id} for "${recipient}" added successfully!`);
  location.reload();
};

window.editAdminCertificate = function(id) {
  const db = FestDB.getData();
  const c = (db.certificates || []).find(x => x.id === id);
  if (!c) return;

  const recipient = prompt("Edit Recipient Name:", c.recipient);
  if (recipient) c.recipient = recipient;

  const eventName = prompt("Edit Event Name:", c.event);
  if (eventName) c.event = eventName;

  const award = prompt("Edit Award / Tier:", c.award);
  if (award) c.award = award;

  const college = prompt("Edit College:", c.college || "Presidency University");
  if (college) c.college = college;

  FestDB.saveData(db);
  alert("Certificate updated!");
  location.reload();
};

window.deleteAdminCertificate = function(id) {
  const db = FestDB.getData();
  if (confirm(`Are you sure you want to delete certificate ${id}?`)) {
    db.certificates = (db.certificates || []).filter(x => x.id !== id);
    FestDB.saveData(db);
    location.reload();
  }
};
'''

if 'function renderAdminCertificates' not in js:
    js = js.replace(
        'window.editAdminWinner = function(idx) {',
        admin_cert_code + '\nwindow.editAdminWinner = function(idx) {'
    )

# 3. Add certificate search in initCertificateStudio
search_cert_code = '''
    // Initialize Verified Certificate Search & Instant Download Section
    initCertificateSearch(db);
'''

if 'initCertificateSearch(db);' not in js:
    js = js.replace(
        '    if (printBtn) {\n      printBtn.addEventListener("click", () => {\n        window.print();\n      });\n    }',
        '    if (printBtn) {\n      printBtn.addEventListener("click", () => {\n        window.print();\n      });\n    }\n' + search_cert_code
    )

# 4. Add initCertificateSearch function implementation
search_func_code = '''
function initCertificateSearch(db) {
  const searchInput = document.getElementById("cert-search-input");
  const searchBtn = document.getElementById("cert-search-btn");
  const resultsDiv = document.getElementById("cert-search-results");
  const statusBadge = document.getElementById("cert-published-badge");

  if (!searchInput || !searchBtn || !resultsDiv) return;

  if (statusBadge) {
    if (db.settings.certificatesPublished) {
      statusBadge.textContent = "⚡ CERTIFICATES REPOSITORY LIVE";
      statusBadge.style.color = "var(--neon-cyan)";
      statusBadge.style.borderColor = "var(--neon-cyan)";
    } else {
      statusBadge.textContent = "🔒 CERTIFICATE UPLOADS IN PROGRESS";
      statusBadge.style.color = "var(--neon-yellow)";
      statusBadge.style.borderColor = "var(--neon-yellow)";
    }
  }

  function performSearch() {
    const q = searchInput.value.trim().toLowerCase();
    resultsDiv.style.display = "block";

    if (!db.settings.certificatesPublished) {
      resultsDiv.innerHTML = `
        <div style="background: rgba(255, 230, 0, 0.08); border: 1px solid var(--neon-yellow); padding: 1.2rem; border-radius: 4px; text-align: center;">
          <h4 style="color: var(--neon-yellow); margin-bottom: 0.4rem; font-family: var(--font-display);">⚡ CERTIFICATES UNDER VERIFICATION</h4>
          <p style="font-size: 0.85rem; color: var(--text-secondary); margin: 0;">
            Event coordinators and the fest committee are currently compiling and signing official participation certificates. They will be available for instant download shortly after results announcement!
          </p>
        </div>
      `;
      return;
    }

    if (!q) {
      resultsDiv.innerHTML = `
        <div style="padding: 1rem; color: var(--text-muted); font-size: 0.85rem; text-align: center;">
          Please enter your Full Name, Team Name, or Certificate ID to search.
        </div>
      `;
      return;
    }

    const certs = db.certificates || [];
    const matches = certs.filter(c => 
      c.recipient.toLowerCase().includes(q) || 
      c.id.toLowerCase().includes(q) || 
      c.event.toLowerCase().includes(q)
    );

    if (matches.length === 0) {
      resultsDiv.innerHTML = `
        <div style="padding: 1.5rem; background: rgba(7,6,15,0.7); border: 1px dashed rgba(255,255,255,0.15); border-radius: 4px; text-align: center;">
          <div style="color: var(--neon-pink); font-family: var(--font-display); font-size: 1.1rem; margin-bottom: 0.4rem;">
            NO DIRECT CERTIFICATE FOUND FOR "${searchInput.value.trim()}"
          </div>
          <p style="color: var(--text-secondary); font-size: 0.85rem; max-width: 500px; margin: 0 auto 1rem;">
            If your certificate was recently issued, verify your spelling or customize and download your personalized certificate directly using our Framing Studio below!
          </p>
          <button class="btn btn-primary" onclick="document.getElementById('cert-input-name').value='${searchInput.value.trim()}'; document.getElementById('cert-input-name').dispatchEvent(new Event('input')); document.querySelector('.cert-studio-layout').scrollIntoView({behavior:'smooth'});" style="font-size: 0.8rem; padding: 0.5rem 1rem;">
            🎨 Open In Framing Studio With This Name
          </button>
        </div>
      `;
      return;
    }

    let cardsHtml = matches.map(m => `
      <div class="cyber-card" style="padding: 1.2rem; margin-bottom: 0.8rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; border-color: rgba(0, 240, 255, 0.4);">
        <div>
          <div style="display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.3rem;">
            <span style="font-family: var(--font-mono); color: var(--neon-cyan); font-weight: 700; font-size: 0.85rem;">[${m.id}]</span>
            <span style="background: rgba(0,240,255,0.1); color: var(--neon-cyan); font-size: 0.68rem; padding: 0.15rem 0.4rem; border-radius: 3px; font-family: var(--font-mono);">VERIFIED ✓</span>
          </div>
          <h4 style="color: #fff; font-family: var(--font-display); font-size: 1.15rem; margin: 0 0 0.2rem;">${m.recipient}</h4>
          <div style="color: var(--neon-yellow); font-family: var(--font-mono); font-size: 0.8rem;">${m.award}</div>
          <div style="color: var(--text-secondary); font-size: 0.78rem;">Arena: <strong>${m.event}</strong> · ${m.college || 'Presidency University'}</div>
        </div>
        <div style="display: flex; gap: 0.6rem; flex-wrap: wrap;">
          <button class="btn btn-primary" onclick="downloadSpecificCertificate('${m.recipient}', '${m.event}', '${m.award}', '${m.college || 'Presidency University'}', '${m.id}')" style="font-size: 0.8rem; padding: 0.6rem 1rem;">
            ⚡ DOWNLOAD OFFICIAL CERTIFICATE
          </button>
          <button class="btn btn-ghost" onclick="loadCertIntoStudio('${m.recipient}', '${m.event}', '${m.award}', '${m.college || 'Presidency University'}')" style="font-size: 0.8rem; padding: 0.6rem 0.9rem;">
            🎨 Frame in Studio
          </button>
        </div>
      </div>
    `).join("");

    resultsDiv.innerHTML = `
      <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--neon-cyan); margin-bottom: 0.8rem;">
        FOUND ${matches.length} VERIFIED CERTIFICATE(S):
      </div>
      ${cardsHtml}
    `;
  }

  searchBtn.addEventListener("click", performSearch);
  searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") performSearch();
  });
}

window.downloadSpecificCertificate = function(name, eventName, award, college, certId) {
  const db = FestDB.getData();
  const nameInput = document.getElementById("cert-input-name");
  const eventSelect = document.getElementById("cert-input-event");
  const awardSelect = document.getElementById("cert-input-award");
  const collegeInput = document.getElementById("cert-input-college");

  if (nameInput) nameInput.value = name;
  if (eventSelect) eventSelect.value = eventName;
  if (awardSelect) awardSelect.value = award;
  if (collegeInput) collegeInput.value = college;

  generateHighResCertificate(db);
};

window.loadCertIntoStudio = function(name, eventName, award, college) {
  const nameInput = document.getElementById("cert-input-name");
  const eventSelect = document.getElementById("cert-input-event");
  const awardSelect = document.getElementById("cert-input-award");
  const collegeInput = document.getElementById("cert-input-college");

  if (nameInput) nameInput.value = name;
  if (eventSelect) eventSelect.value = eventName;
  if (awardSelect) awardSelect.value = award;
  if (collegeInput) collegeInput.value = college;

  if (nameInput) nameInput.dispatchEvent(new Event("input"));
  document.querySelector(".cert-studio-layout")?.scrollIntoView({ behavior: "smooth" });
};
'''

if 'function initCertificateSearch' not in js:
    js = js.replace(
        '// ==========================================================================\n// 15. GALLERY PAGE',
        search_func_code + '\n// ==========================================================================\n// 15. GALLERY PAGE'
    )

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('js/main.js updated with certificate admin & search capabilities.')
