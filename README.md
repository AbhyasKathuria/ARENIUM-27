# ARENIUM'27 — Official Tech Fest Website

> **School of Information Science (SOIS)**  
> **Presidency University, Itgalpura, Rajanukunte, Bengaluru, Karnataka 560064**  
> **Aesthetic:** Cyberpunk / Neon-Terminal / High-Tech Grid

---

## 📁 Project Directory Structure

```text
ARENIUM 27/
├── index.html            # Complete Home Page (Hero, Glitch Title, 1.5L Ticker, Countdown, About, Events Preview, Team Photos, QR Scanner)
├── events.html           # Events Matrix (Pre & Main arenas, coordinator photo/contact, inside Rulebook modal)
├── schedule.html         # Day-wise Timeline Schedule (Day 1 & Day 2 chronological agenda)
├── winners.html          # Hall of Champions (Podiums, 1st/2nd/3rd places, prize money, certificate links)
├── certificate.html      # Certificate Framing & 300 DPI High-Res Download Studio
├── admin.html            # Superadmin Panel (Live CRUD for events, coordinators, leadership, winners, sponsors, gallery, ticker)
├── gallery.html          # Interactive Cyber Lightbox Gallery (Fullscreen modal & keyboard nav)
├── sponsors.html         # Sponsor Tiers & Partnership Portal
├── contact.html          # Contact Directory, 4 Coordinators with photos, Dean, HOD & Full SOIS Faculty, Google Map
├── rulebook.pdf          # Official Event Rulebook & Guidelines
├── start.bat             # 1-Click launcher (starts local server & opens browser)
├── css/
│   └── style.css         # Master Cyberpunk Design System & Responsive Stylesheet
├── js/
│   └── main.js           # Fest Engine: FestDB state, Countdown, Canvas, Rulebook Modal, Cert Studio, Admin Sync
├── images/
│   ├── favicon.svg       # Glowing A'27 Hexagonal Cyber Favicon
│   ├── logo.svg          # SOIS Presidency University / ARENIUM'27 Brand Crest
│   ├── coord-kaushal.svg # Lead Coordinator Kaushal Kumar cyber portrait
│   ├── coord-ashlin.svg  # Coordinator Ashlin cyber portrait
│   ├── coord-abhyas.svg  # Coordinator Abhyas Kathuria cyber portrait
│   ├── coord-vimal.svg   # Coordinator Vimal cyber portrait
│   ├── leader-dean.svg   # Patron / Dean Dr. Mahalaxmi portrait
│   ├── leader-hod.svg    # HOD Dr. Vertimani Elgovan portrait
│   ├── leader-organiser.svg # Programme Organiser Keren Lios Daniel portrait
│   ├── leader-sois.svg   # SOIS Faculty Mentors & Organizing Committee
│   ├── qrcode.svg        # Cyberpunk Vector QR Code (Master registration)
│   ├── qrcode.png        # Cyberpunk Raster QR Code
│   ├── main-poster.svg   # Official Fest Poster ("The Neon Ascent")
│   └── events-poster.svg # Events Lineup Matrix Showcase Poster
└── README.md             # Developer documentation & deployment guide
```

---

## ⚡ Quick Start (Run in 1 Go)

Simply **double-click [`start.bat`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/start.bat)** or run it from terminal:

```cmd
start.bat
```

- **Automatic Server:** Detects Python or Node.js to spin up an HTTP server with clean CORS/asset loading.
- **Auto-Browser Launch:** Opens `http://localhost:8000` in your default web browser instantly.
- **Port Auto-Discovery:** Automatically finds an open port if port 8000 is occupied.
- **Zero-Dependency Fallback:** If neither Python nor Node is installed, it automatically falls back to launching `index.html` directly in your default browser.

---

## ⚡ How to Customize & Configure

All primary configuration switches are consolidated at the top of [`js/main.js`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/js/main.js) and [`css/style.css`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/css/style.css).

### 1. Update the Event Date & Countdown
In [`js/main.js`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/js/main.js) (or directly via the Superadmin Panel `admin.html`), locate `FestDB.settings`:
```javascript
eventDate: "2027-02-04T08:30:00+05:30" // 4–5 February 2027
```
- The countdown on the homepage automatically calculates days, hours, minutes, and seconds. When this date arrives, it automatically switches to display `⚡ EVENT IS LIVE NOW ⚡`.

### 2. Superadmin Control Panel (`admin.html`)
- **Access URL:** [`admin.html`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/admin.html)
- **Master Security Passkey:** `PUSOIS27`
- **Features:**
  - Full CRUD operations for all 11 official competitions (edit names, categories, prize pools, venues, and posters).
  - Manage Core Coordinators and Faculty Leadership.
  - Publish / Unpublish official results and configure winner podiums.
  - Upload, verify, edit, and delete participant certificates.
  - Manage Sponsors across Title, Platinum, Gold, and Tech Partner tiers.
  - Update continuous ₹1.5L moving banner ticker and instant flash notices.
  - Change Registration QR Code scanner and registration URL.
  - Full JSON database export, restore, and reset.

### 3. Light & Dark Dual-Theme Matrix (`ThemeEngine`)
- **Interactive Cyber Toggle Switch:** Available in the desktop navbar header, mobile header group, mobile drawer navigation, and the Superadmin portal.
- **Persistent State:** Saves user preference in `localStorage` (`arenium_theme`) with zero-flash instantaneous startup.
- **Light Theme Palette:**
  - Background Core: `#F3EFEF`
  - Surface & Cards: `#E3EEF8`
  - Lavender Accent & Glow: `#D6C7FF`
  - Primary Electric Cobalt: `#5B7FFF`
  - Deep Obsidian Navy Text: `#1B2342`
- **Dark Theme Palette:**
  - Background Core: `#1F080A`
  - Surface & Cards: `#3B0E14`
  - Crimson Accent & Glow: `#7A0026`
  - Vivid Ruby Neon: `#B81D42`
  - Frosted Ivory Text: `#F8E8EB`
- **Dynamic Assets:** Switches SVG logo seamlessly (`images/logo-light.svg` / `images/logo-dark.svg`) and adjusts the interactive HTML5 hero canvas particle physics in real-time.

---

## 🏛️ Event Leadership & Committee

- **Host School:** School of Information Science (SOIS)
- **Institution:** Presidency University, Bengaluru
- **Patron / Dean:** Dr. C. Kalaiarasan (Dean, SOIS)
- **Head of Department:** Dr. K. G. Mohan (HOD, SOIS)
- **Overall Fest Coordinator:** Ms. Keren Lois Daniel
- **Marketing & PR Lead:** Ms. Neha Arora
- **Core Student Managers:**
  - **Kaushal Kumar Singh:** Finance & Registration Manager (5BCA01 / 20241BCA0051) — `+91 91087 40761`
  - **Vimal Raj:** Event Manager (5BCADS02) — `+91 96201 92249`
  - **Ashlin Siddharth:** Marketing & Registration Manager (5BCADS01) — `+91 87976 86786`
  - **Abhyas Kathuria:** Technical Manager (5BCAAIML01) — `+91 85958 48421`
- **SOIS Organizing Committees:** Marketing & Promotion, Discipline & Security, Decoration & Ambiance, Hospitality & Refreshment, Media & Documentation, Registration & Ticketing.
