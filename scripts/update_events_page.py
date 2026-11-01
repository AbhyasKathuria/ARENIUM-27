import os

# 1. Update events.html
with open('events.html', 'r', encoding='utf-8') as f:
    events_html = f.read()

# Update subtitle and chips in events.html
old_chips_block = '''        <!-- Filter Chips -->
        <div class="filter-chips-container" role="toolbar" aria-label="Event Categories Filter">
          <button class="filter-chip active" data-filter="all">[ALL ARENAS]</button>
          <button class="filter-chip" data-filter="pre">[PRE-EVENTS]</button>
          <button class="filter-chip" data-filter="main">[MAIN EVENTS]</button>
        </div>'''

new_chips_block = '''        <!-- Filter Chips -->
        <div class="filter-chips-container" role="toolbar" aria-label="Event Categories Filter">
          <button class="filter-chip active" data-filter="all">[ALL ARENAS (11)]</button>
          <button class="filter-chip" data-filter="day1">[DAY 01 // 4 FEB]</button>
          <button class="filter-chip" data-filter="day2">[DAY 02 // 5 FEB]</button>
          <button class="filter-chip" data-filter="hackathon">[24H HACKATHON &amp; CODING]</button>
          <button class="filter-chip" data-filter="gaming">[GAMING &amp; ESPORTS]</button>
          <button class="filter-chip" data-filter="flagship">[VENTURE &amp; FLAGSHIP]</button>
        </div>'''

events_html = events_html.replace(old_chips_block, new_chips_block)
events_html = events_html.replace(
    'Challenge your intellect, precision, and agility across our diverse pre-events and on-campus flagship championships.',
    'The Arena of Innovation · 4–5 February 2027 · ₹1,50,000 Total Prize Pool across 11 official competitive tracks.'
)

# Update layout blocks to single responsive grid
old_blocks = '''        <!-- Pre-events Block -->
        <div class="events-group-block" id="pre-events-block">
          <h2 class="events-group-heading">
            <span style="color: var(--neon-pink);">[01]</span> PRE-EVENTS &amp; DIGITAL SUBMISSIONS
          </h2>
          <div class="events-grid" id="pre-events-container">
            <!-- Dynamically populated via main.js from EVENTS_DATA -->
          </div>
        </div>

        <!-- Main Events Block -->
        <div class="events-group-block" id="main-events-block">
          <h2 class="events-group-heading">
            <span style="color: var(--neon-cyan);">[02]</span> ON-CAMPUS MAIN ARENAS
          </h2>
          <div class="events-grid" id="main-events-container">
            <!-- Dynamically populated via main.js from EVENTS_DATA -->
          </div>
        </div>'''

new_blocks = '''        <!-- All Competitions Grid -->
        <div class="events-group-block" id="main-events-block">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.8rem;">
            <h2 class="events-group-heading" style="margin: 0;">
              <span style="color: var(--neon-cyan);">[FLAGSHIP MATRIX]</span> OFFICIAL ARENIUM '27 ARENAS
            </h2>
            <div style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--neon-yellow);">
              ⚡ ₹1.5 LAKHS TOTAL CASH PRIZE POOL
            </div>
          </div>
          <div class="events-grid" id="main-events-container">
            <!-- Dynamically populated via main.js from FestDB.events -->
          </div>
        </div>'''

events_html = events_html.replace(old_blocks, new_blocks)

with open('events.html', 'w', encoding='utf-8') as f:
    f.write(events_html)

print('events.html updated.')


# 2. Update initEventsPage in js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_event_render = '''function initEventsPage(db) {
  try {
    const preContainer = document.getElementById("pre-events-container");
    const mainContainer = document.getElementById("main-events-container");
    if (!preContainer && !mainContainer) return;

    if (preContainer) preContainer.innerHTML = "";
    if (mainContainer) mainContainer.innerHTML = "";

    const regUrl = db.settings.registerUrl || "#";

    db.events.forEach(ev => {
      const card = document.createElement("article");
      card.className = "cyber-card event-card reveal-on-scroll is-visible";
      card.setAttribute("data-group", ev.group);
      card.setAttribute("data-event-id", ev.id);

      const coord = ev.coordinator || { name: "SOIS Coordinator", phone: "+91 91087 40761", photo: "images/coord-generic.svg" };

      card.innerHTML = `
        <div class="event-poster-wrapper">
          <img src="${ev.poster || 'images/events-poster.svg'}" alt="${ev.name} Poster" class="event-poster-img" loading="lazy">
          <span style="position: absolute; top: 12px; right: 12px; background: rgba(7,6,15,0.9); border: 1px solid var(--neon-yellow); color: var(--neon-yellow); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 800; padding: 0.3rem 0.6rem; border-radius: 4px; box-shadow: 0 0 10px rgba(255,230,0,0.3);">
            ${ev.prize ? 'PRIZE: ' + ev.prize : '₹1.5L POOL'}
          </span>
        </div>
        <div class="event-body">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span class="event-category-badge">${ev.category}</span>
            <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted);">${ev.venue || 'SOIS Block'}</span>
          </div>
          <h3 class="event-title">${ev.name}</h3>
          <p class="event-desc">${ev.description}</p>
          
          <!-- Event Coordinator Mini Card with Photo & Direct Phone -->
          <div class="event-coord-mini">
            <img src="${coord.photo || 'images/coord-generic.svg'}" alt="${coord.name}" class="event-coord-thumb">
            <div class="event-coord-details">
              <div class="event-coord-name">${coord.name}</div>
              <a href="tel:${coord.phone.replace(/[^0-9+]/g, '')}" class="event-coord-phone">
                📞 ${coord.phone}
              </a>
            </div>
          </div>

          <div class="event-action-footer" style="display: flex; gap: 0.6rem; flex-wrap: wrap;">
            <button type="button" class="btn btn-ghost open-rulebook-btn" data-event-id="${ev.id}" style="flex: 1; padding: 0.7rem 0.8rem; font-size: 0.78rem;">
              📖 RULEBOOK
            </button>
            <a href="${regUrl}" class="btn btn-register" style="flex: 1.2; padding: 0.7rem 0.8rem; font-size: 0.78rem; text-align: center;" data-register-btn>
              REGISTER
            </a>
          </div>
        </div>
      `;

      if (ev.group === "pre" && preContainer) {
        preContainer.appendChild(card);
      } else if (ev.group === "main" && mainContainer) {
        mainContainer.appendChild(card);
      }
    });

    // Attach click listeners to all Rulebook buttons
    document.querySelectorAll(".open-rulebook-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const evId = btn.getAttribute("data-event-id");
        openRulebookModal(evId);
      });
    });

    // Filter Chips
    const chips = document.querySelectorAll(".filter-chip");
    const preBlock = document.getElementById("pre-events-block");
    const mainBlock = document.getElementById("main-events-block");

    chips.forEach(chip => {
      chip.addEventListener("click", () => {
        chips.forEach(c => c.classList.remove("active"));
        chip.classList.add("active");
        const filter = chip.getAttribute("data-filter");

        if (filter === "all") {
          if (preBlock) preBlock.style.display = "block";
          if (mainBlock) mainBlock.style.display = "block";
        } else if (filter === "pre") {
          if (preBlock) preBlock.style.display = "block";
          if (mainBlock) mainBlock.style.display = "none";
        } else if (filter === "main") {
          if (preBlock) preBlock.style.display = "none";
          if (mainBlock) mainBlock.style.display = "block";
        }
      });
    });
  } catch (err) {
    console.error("Error initializing events page:", err);
  }
}'''

new_event_render = '''function initEventsPage(db) {
  try {
    const mainContainer = document.getElementById("main-events-container") || document.getElementById("pre-events-container");
    if (!mainContainer) return;

    mainContainer.innerHTML = "";
    const regUrl = db.settings.registerUrl || "#";

    db.events.forEach(ev => {
      const card = document.createElement("article");
      card.className = "cyber-card event-card reveal-on-scroll is-visible";
      
      // Determine day category for filtering
      let dayCat = "day1";
      if (ev.date && ev.date.includes("Day 2")) dayCat = "day2";
      if (ev.id.includes("hackathon")) dayCat = "hackathon";

      card.setAttribute("data-event-id", ev.id);
      card.setAttribute("data-day", dayCat);
      card.setAttribute("data-category", ev.category.toLowerCase());

      const coord = ev.coordinator || { name: "Kaushal Kumar Singh", phone: "+91 91087 40761", photo: "images/coord-kaushal.svg" };

      card.innerHTML = `
        <div class="event-poster-wrapper">
          <img src="${ev.poster || 'images/events-poster.svg'}" alt="${ev.name} Poster" class="event-poster-img" loading="lazy">
          <span style="position: absolute; top: 12px; right: 12px; background: rgba(7,6,15,0.9); border: 1px solid var(--neon-yellow); color: var(--neon-yellow); font-family: var(--font-mono); font-size: 0.75rem; font-weight: 800; padding: 0.3rem 0.6rem; border-radius: 4px; box-shadow: 0 0 10px rgba(255,230,0,0.3);">
            ${ev.prize ? 'PRIZE: ' + ev.prize : '₹15,000'}
          </span>
          <span style="position: absolute; bottom: 10px; left: 10px; background: rgba(0, 0, 0, 0.75); color: var(--neon-cyan); font-family: var(--font-mono); font-size: 0.72rem; padding: 0.2rem 0.5rem; border-radius: 3px; border: 1px solid rgba(0,240,255,0.3);">
            📍 ${ev.venue || 'SOIS Campus'}
          </span>
        </div>
        <div class="event-body">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span class="event-category-badge">${ev.category}</span>
            <span style="font-family: var(--font-mono); font-size: 0.72rem; color: var(--neon-pink); font-weight: 700;">${ev.date || '4-5 Feb'}</span>
          </div>
          <h3 class="event-title">${ev.name}</h3>
          <p class="event-desc">${ev.description}</p>
          
          <!-- Event Coordinator with Photo & Direct Phone Call -->
          <div class="event-coord-mini">
            <img src="${coord.photo || 'images/coord-generic.svg'}" alt="${coord.name}" class="event-coord-thumb">
            <div class="event-coord-details">
              <div class="event-coord-name">${coord.name}</div>
              <a href="tel:${coord.phone.replace(/[^0-9+]/g, '')}" class="event-coord-phone">
                📞 ${coord.phone}
              </a>
            </div>
          </div>

          <div class="event-action-footer" style="display: flex; gap: 0.6rem; flex-wrap: wrap;">
            <button type="button" class="btn btn-ghost open-rulebook-btn" data-event-id="${ev.id}" style="flex: 1; padding: 0.7rem 0.8rem; font-size: 0.78rem;">
              📖 RULEBOOK
            </button>
            <a href="${regUrl}" class="btn btn-register" style="flex: 1.2; padding: 0.7rem 0.8rem; font-size: 0.78rem; text-align: center;" data-register-btn>
              REGISTER
            </a>
          </div>
        </div>
      `;

      mainContainer.appendChild(card);
    });

    // Attach click listeners to all Rulebook buttons
    document.querySelectorAll(".open-rulebook-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const evId = btn.getAttribute("data-event-id");
        openRulebookModal(evId);
      });
    });

    // Filter Chips
    const chips = document.querySelectorAll(".filter-chip");
    const cards = mainContainer.querySelectorAll(".event-card");

    chips.forEach(chip => {
      chip.addEventListener("click", () => {
        chips.forEach(c => c.classList.remove("active"));
        chip.classList.add("active");
        const filter = chip.getAttribute("data-filter");

        cards.forEach(card => {
          const day = card.getAttribute("data-day");
          const cat = card.getAttribute("data-category");

          if (filter === "all") {
            card.style.display = "flex";
          } else if (filter === "day1") {
            card.style.display = (day === "day1" || day === "hackathon") ? "flex" : "none";
          } else if (filter === "day2") {
            card.style.display = (day === "day2" || day === "hackathon") ? "flex" : "none";
          } else if (filter === "hackathon") {
            card.style.display = (day === "hackathon" || cat.includes("coding") || cat.includes("blind")) ? "flex" : "none";
          } else if (filter === "gaming") {
            card.style.display = (cat.includes("esports") || cat.includes("gaming")) ? "flex" : "none";
          } else if (filter === "flagship") {
            card.style.display = (cat.includes("startup") || cat.includes("fashion") || cat.includes("brand") || cat.includes("auction") || cat.includes("expo")) ? "flex" : "none";
          }
        });
      });
    });
  } catch (err) {
    console.error("Error initializing events page:", err);
  }
}'''

js = js.replace(old_event_render, new_event_render)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('js/main.js events page renderer updated.')
