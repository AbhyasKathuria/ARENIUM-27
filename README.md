# ARENIUM'27 — Official Tech Fest Website

> **School of Information Science (SOIS)**  
> **Presidency University, Itgalpura, Rajanukunte, Bengaluru, Karnataka 560064**  
> **Aesthetic:** Cyberpunk / Neon-Terminal / High-Tech Grid

---

## 📁 Project Directory Structure

```text
ARENIUM 27/
├── index.html            # Complete Home Page (Hero, Glitch Title, Countdown, About, Events Preview, Poster, Team, QR Scanner, Footer)
├── events.html           # Events Matrix (Pre-events & Main events grid with filter chips)
├── schedule.html         # Day-wise Timeline Schedule (Vertical neon line & Day tabs)
├── gallery.html          # Interactive Cyber Lightbox Gallery (Fullscreen modal & keyboard nav)
├── sponsors.html         # Sponsor Tiers & Partnership Portal
├── contact.html          # Contact Directory, Team Cards & Google Map
├── rulebook.pdf          # Official Event Rulebook & Guidelines
├── css/
│   └── style.css         # Master Cyberpunk Design System & Responsive Stylesheet
├── js/
│   └── main.js           # Fest Engine: Countdown, Canvas, Navigation, Event Data & Schedule
├── images/
│   ├── favicon.svg       # Glowing A'27 Hexagonal Cyber Favicon
│   ├── logo.svg          # SOIS Presidency University / ARENIUM'27 Brand Crest
│   ├── qrcode.svg        # Cyberpunk Vector QR Code (Master registration)
│   ├── qrcode.png        # Cyberpunk Raster QR Code
│   ├── main-poster.svg   # Official Fest Poster ("The Neon Ascent")
│   └── events-poster.svg # Events Lineup Matrix Showcase Poster
└── README.md             # Developer documentation & deployment guide
```

---

## ⚡ How to Customize & Configure

All primary configuration switches are consolidated at the top of [`js/main.js`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/js/main.js) and [`css/style.css`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/css/style.css).

### 1. Update the Event Date & Countdown
In [`js/main.js`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/js/main.js), locate line 13:
```javascript
const EVENT_DATE = "2027-03-26T09:00:00+05:30";
```
- Change this ISO 8601 timestamp to the exact fest start date.
- The countdown on the homepage automatically calculates days, hours, minutes, and seconds. When this date arrives, it automatically switches to display `⚡ EVENT IS LIVE NOW ⚡`.

### 2. Update the Master Registration URL
In [`js/main.js`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/js/main.js), locate line 19:
```javascript
const REGISTER_URL = "https://your-registration-portal-or-google-form-link.com";
```
- Replace `#` with your actual Google Form, Unstop, or custom portal URL.
- All "REGISTER NOW" buttons across the header, hero, cards, scanner section, and mobile drawer automatically bind to this URL.

### 3. Update the 3-Part Tagline
In [`js/main.js`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/js/main.js), locate line 25:
```javascript
const TAGLINE = "DISRUPT THE MATRIX // IGNITE THE FUTURE // ASCEND THE GRID";
```
You can also change the headline spans in [`index.html`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/index.html).

### 4. Adding or Editing Events
In [`js/main.js`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/js/main.js), find the `EVENTS_DATA` array:
```javascript
{
  id: "main-quiz",
  name: "TECH MATRIX QUIZ",
  category: "Tech Quiz",
  group: "main", // 'pre' or 'main'
  description: "Rapid-fire MCQ qualifiers leading into a buzzer round...",
  poster: "images/events-poster.svg"
}
```
Simply add, remove, or edit objects in this array.

### 5. Modifying the Neon Cyberpunk Color Palette
In [`css/style.css`](file:///c:/Users/kathu/Desktop/projects/ARENIUM%2027/css/style.css), edit `:root` CSS variables:
```css
:root {
  --bg-core: #07060f;           /* Deep dark cyber background */
  --neon-cyan: #00f0ff;          /* Primary futuristic cyan */
  --neon-pink: #ff0055;          /* High-voltage action magenta */
  --neon-purple: #9d4edd;        /* Electric violet */
  --neon-yellow: #ffe600;        /* Warning terminal amber */
  --font-display: 'Orbitron', 'Rajdhani', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

---

## 📋 Checklist of Placeholders to Replace Before Launch

1. **Registration Link (`REGISTER_URL`)**: Set in `js/main.js` (currently `#`).
2. **Official Rulebook PDF (`rulebook.pdf`)**: Replace the placeholder `rulebook.pdf` with the finalized student handbook/rulebook.
3. **Registration QR Code (`images/qrcode.png`)**: Replace with the actual QR code pointing to your Google Form or Unstop link.
4. **Official Fest Posters (`images/main-poster.svg`, `images/events-poster.svg`)**: Swap with the final creative artwork designed by the graphics team.
5. **Coordinator Phone Numbers**: Defined in `index.html` and `contact.html`. Match individual names to each phone number.
6. **Social Media URLs**: Replace placeholder links (`https://instagram.com`, `https://youtube.com`, `https://linkedin.com`) in the footer with official handles.
7. **Google Maps Embed / Link**: Update Presidency University location link if specific gate/auditorium coords are preferred.
8. **Credit Line**: Change `Designed & Developed by <Arenium Web Operations>` in the footer to your name or development committee.

---

## 🚀 Deployment Instructions

### Option 1: GitHub Pages (Recommended)
1. Initialize a git repository (already initialized):
   ```bash
   git add .
   git commit -m "feat: ARENIUM 27 tech fest initial release"
   ```
2. Create a repository on GitHub (e.g. `arenium-2027`).
3. Push your repository:
   ```bash
   git remote add origin https://github.com/<your-username>/arenium-2027.git
   git branch -M main
   git push -u origin main
   ```
4. Go to **Settings** > **Pages** in GitHub.
5. Under **Branch**, select `main` and root `/`, then click **Save**.
6. Your site will be live instantly at `https://<your-username>.github.io/arenium-2027/`.

### Option 2: Netlify
1. Go to [Netlify](https://www.netlify.com/).
2. Drag and drop the `ARENIUM 27` root folder into Netlify's **Deploy** zone.
3. Site goes live immediately with SSL enabled.

---

## 🏛️ Event Leadership & Committee

- **Host School:** School of Information Science (SOIS)
- **Institution:** Presidency University, Bengaluru
- **Patron / Dean:** Mahalaxmi (Dean, SOIS)
- **Head of Department:** Vertimani Elgonva (HOD, SOIS)
- **Programme Organiser:** Keren Lios Daniel
- **Student Coordinators:** Kaushal Kumar, Ashlin, Abhyas Kathuria, Vimal
- **Contact Lines:**
  - `+91 91087 40761`
  - `+91 87976 86786`
  - `+91 85958 48421`
  - `+91 96201 92249`
