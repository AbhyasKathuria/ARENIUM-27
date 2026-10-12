/**
 * ARENIUM'27 — Master Client Script
 * School of Information Science (SOIS), Presidency University, Bengaluru
 * Cyberpunk / Neon-Terminal Interactive Fest Engine
 */

// ==========================================================================
// 1. GLOBAL CONFIGURATION & EVENT CONSTANTS
// ==========================================================================

/**
 * Single fest launch date constant (ISO 8601).
 * Edit this date to update the countdown across the site.
 */
const EVENT_DATE = "2027-03-26T09:00:00+05:30";

/**
 * Universal Registration URL placeholder.
 * Used by all "Register Now" buttons across pages.
 */
const REGISTER_URL = "#";

/**
 * 3-part Fest Tagline in the "A // B // C" rhythm.
 * Easily modifiable in one place.
 */
const TAGLINE = "DISRUPT THE MATRIX // IGNITE THE FUTURE // ASCEND THE GRID";

// ==========================================================================
// 2. DATA ARRAYS (For Events, Schedule & Future Pages)
// ==========================================================================

const EVENTS_DATA = [
  // --- PRE-EVENTS ---
  {
    id: "pre-photo",
    name: "CYBERPUNK LENS",
    category: "Photography",
    group: "pre",
    description: "Capture the urban twilight and neon aesthetics of everyday architecture. Frame the futuristic contrast of technology and humanity.",
    poster: "images/events-poster.svg"
  },
  {
    id: "pre-reel",
    name: "NEON REEL RUNNER",
    category: "Short-Reel Making",
    group: "pre",
    description: "A 60-second high-octane creative video challenge. Showcase editing speed, transitions, visual storytelling, and cyberpunk vibes.",
    poster: "images/events-poster.svg"
  },
  {
    id: "pre-art",
    name: "DIGITAL CANVAS 2027",
    category: "Digital Art & 3D",
    group: "pre",
    description: "Unleash concept art, futuristic UI renders, and sci-fi illustrations exploring the apex of artificial intelligence.",
    poster: "images/events-poster.svg"
  },

  // --- MAIN EVENTS ---
  {
    id: "main-quiz",
    name: "TECH MATRIX QUIZ",
    category: "Tech Quiz",
    group: "main",
    description: "Rapid-fire MCQ qualifiers leading into a high-stakes buzzer round testing algorithmic thinking, cybersecurity, and tech history.",
    poster: "images/events-poster.svg"
  },
  {
    id: "main-lan",
    name: "LAN ARENA CHAMPIONSHIP",
    category: "LAN Gaming",
    group: "main",
    description: "Zero-ping competitive showdown in Valorant, BGMI, and Tekken. Squad up, coordinate tactics, and conquer the leaderboard.",
    poster: "images/events-poster.svg"
  },
  {
    id: "main-hunt",
    name: "CAMPUS QR TREASURE HUNT",
    category: "Cryptic Hunt",
    group: "main",
    description: "Decipher encrypted riddles hidden across Presidency University campus. Scan geo-tagged QR nodes before opposing teams beat the clock.",
    poster: "images/events-poster.svg"
  },
  {
    id: "main-racing",
    name: "RETRO APEX RACER",
    category: "Sim Racing",
    group: "main",
    description: "Synthwave time-trials on retro simulator rigs. High precision turns and maximum drift scores determine the track champion.",
    poster: "images/events-poster.svg"
  },
  {
    id: "main-charades",
    name: "EMOJI CIPHER CHARADES",
    category: "Team Game",
    group: "main",
    description: "Translate complex tech concepts, code libraries, and sci-fi pop culture using only emoji sequences and rapid team gestures.",
    poster: "images/events-poster.svg"
  },
  {
    id: "main-ewaste",
    name: "E-WASTE SCULPTOR",
    category: "Upcycled Tech Art",
    group: "main",
    description: "Transform discarded motherboards, chips, and cables into cyberpunk sculptures. Innovation meets sustainable technology.",
    poster: "images/events-poster.svg"
  },
  {
    id: "main-meme",
    name: "AI PROMPT MEME BATTLE",
    category: "Prompt & Humor",
    group: "main",
    description: "Craft prompts under time pressure to generate the most hilarious, relatable tech memes judged live by the crowd.",
    poster: "images/events-poster.svg"
  }
];

const SCHEDULE_DATA = [
  {
    day: "Day 1",
    time: "09:00 AM - 10:30 AM",
    name: "Grand Opening & Keynote Ascendance",
    venue: "Main University Auditorium",
    note: "Inauguration ceremony by Dean, HOD & Faculty"
  },
  {
    day: "Day 1",
    time: "11:00 AM - 01:30 PM",
    name: "Tech Matrix Quiz (Prelims & Buzzer Finale)",
    venue: "SOIS Lab Block 3",
    note: "Top 8 teams qualify for stage finale"
  },
  {
    day: "Day 1",
    time: "02:00 PM - 05:00 PM",
    name: "Campus QR Treasure Hunt",
    venue: "Central Campus Grounds",
    note: "Encrypted QR checkpoints activate at 14:00"
  },
  {
    day: "Day 1",
    time: "02:30 PM - 06:00 PM",
    name: "LAN Arena: Group Stage Qualifiers",
    venue: "Advanced Gaming Hub, SOIS",
    note: "Valorant & BGMI brackets"
  },
  {
    day: "Day 2",
    time: "09:30 AM - 12:30 PM",
    name: "E-Waste Sculptor & AI Meme Battle",
    venue: "Exhibition Concourse",
    note: "Live showcase & prompt showdown"
  },
  {
    day: "Day 2",
    time: "01:00 PM - 04:00 PM",
    name: "LAN Arena Championship Finals",
    venue: "Main Stage Arena",
    note: "Live streamed on main projectors"
  },
  {
    day: "Day 2",
    time: "04:30 PM - 06:30 PM",
    name: "Valedictory & Prize Distribution",
    venue: "Main University Auditorium",
    note: "Trophies, cash prize pool & certs"
  }
];

// ==========================================================================
// 3. CORE LOGIC & INITIALISATION
// ==========================================================================

document.addEventListener("DOMContentLoaded", () => {
  initRegistrationButtons();
  initNavigation();
  initCountdown();
  initHeroCanvas();
  initScrollAnimations();
  initEventsPage();
  initSchedulePage();
  initGalleryPage();
});

/**
 * Connects all register buttons to the master REGISTER_URL constant
 */
function initRegistrationButtons() {
  try {
    const registerButtons = document.querySelectorAll(".btn-register, [data-register-btn]");
    registerButtons.forEach(btn => {
      if (btn.tagName.toLowerCase() === "a") {
        btn.setAttribute("href", REGISTER_URL);
        if (REGISTER_URL !== "#") {
          btn.setAttribute("target", "_blank");
          btn.setAttribute("rel", "noopener noreferrer");
        }
      }
    });
  } catch (err) {
    console.error("Error setting registration links:", err);
  }
}

/**
 * Mobile navigation toggle and dropdown accordion behaviour
 */
function initNavigation() {
  try {
    const navToggle = document.querySelector(".nav-toggle-btn");
    const navMenu = document.querySelector(".nav-menu");
    const dropdowns = document.querySelectorAll(".nav-dropdown");

    if (navToggle && navMenu) {
      navToggle.addEventListener("click", () => {
        const isOpen = navMenu.classList.toggle("is-open");
        navToggle.classList.toggle("is-active", isOpen);
        navToggle.setAttribute("aria-expanded", isOpen);
      });

      // Close menu when clicking outside
      document.addEventListener("click", (e) => {
        if (!navToggle.contains(e.target) && !navMenu.contains(e.target) && navMenu.classList.contains("is-open")) {
          navMenu.classList.remove("is-open");
          navToggle.classList.remove("is-active");
          navToggle.setAttribute("aria-expanded", "false");
        }
      });
    }

    // Dropdown toggle for mobile/keyboard
    dropdowns.forEach(drop => {
      const toggle = drop.querySelector(".dropdown-toggle");
      if (toggle) {
        toggle.addEventListener("click", (e) => {
          if (window.innerWidth <= 768) {
            e.preventDefault();
            drop.classList.toggle("open");
          }
        });
      }
    });

    // Close mobile menu when an internal link is clicked
    const links = document.querySelectorAll(".nav-link:not(.dropdown-toggle)");
    links.forEach(l => {
      l.addEventListener("click", () => {
        if (navMenu && navMenu.classList.contains("is-open")) {
          navMenu.classList.remove("is-open");
          if (navToggle) navToggle.classList.remove("is-active");
        }
      });
    });
  } catch (err) {
    console.error("Error initializing navigation:", err);
  }
}

/**
 * High-precision countdown timer based on EVENT_DATE
 */
function initCountdown() {
  try {
    const daysEl = document.getElementById("count-days");
    const hoursEl = document.getElementById("count-hours");
    const minsEl = document.getElementById("count-mins");
    const secsEl = document.getElementById("count-secs");
    const gridEl = document.getElementById("countdown-grid");
    const liveEl = document.getElementById("countdown-live-banner");

    if (!daysEl || !hoursEl || !minsEl || !secsEl) return;

    const targetTime = new Date(EVENT_DATE).getTime();

    function update() {
      const now = new Date().getTime();
      const difference = targetTime - now;

      if (difference <= 0) {
        // Event has arrived or passed
        if (gridEl) gridEl.style.display = "none";
        if (liveEl) liveEl.style.display = "inline-block";
        return;
      }

      const days = Math.floor(difference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((difference % (1000 * 60)) / 1000);

      daysEl.textContent = String(days).padStart(2, "0");
      hoursEl.textContent = String(hours).padStart(2, "0");
      minsEl.textContent = String(minutes).padStart(2, "0");
      secsEl.textContent = String(seconds).padStart(2, "0");
    }

    update();
    setInterval(update, 1000);
  } catch (err) {
    console.error("Error initializing countdown:", err);
  }
}

/**
 * Interactive lightweight Hero Cyber Matrix Canvas
 */
function initHeroCanvas() {
  try {
    const canvas = document.getElementById("hero-canvas");
    if (!canvas) return;

    // Check user preference for reduced motion
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReducedMotion) return;

    const ctx = canvas.getContext("2d");
    let width, height;
    let particles = [];
    let animationFrameId;
    let isVisible = true;

    function resize() {
      width = canvas.width = canvas.parentElement.offsetWidth || window.innerWidth;
      height = canvas.height = canvas.parentElement.offsetHeight || window.innerHeight;
      createParticles();
    }

    function createParticles() {
      particles = [];
      const count = Math.min(Math.floor(width / 24), 60); // Responsive particle budget
      for (let i = 0; i < count; i++) {
        particles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -Math.random() * 0.7 - 0.2, // Float upwards
          radius: Math.random() * 2 + 1,
          color: Math.random() > 0.4 ? "rgba(0, 240, 255, " : "rgba(255, 0, 85, ",
          alpha: Math.random() * 0.7 + 0.2
        });
      }
    }

    function draw() {
      if (!isVisible) return;

      ctx.clearRect(0, 0, width, height);

      // Draw faint cyber grid horizon
      ctx.strokeStyle = "rgba(0, 240, 255, 0.04)";
      ctx.lineWidth = 1;
      const step = 45;
      for (let x = 0; x < width; x += step) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.stroke();
      }

      // Draw connected particles
      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];

        p.x += p.vx;
        p.y += p.vy;

        if (p.y < 0) {
          p.y = height;
          p.x = Math.random() * width;
        }
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;

        ctx.fillStyle = p.color + p.alpha + ")";
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();

        // Connect nearby nodes
        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 85) {
            ctx.strokeStyle = `rgba(0, 240, 255, ${0.15 * (1 - dist / 85)})`;
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      }

      animationFrameId = requestAnimationFrame(draw);
    }

    window.addEventListener("resize", resize);
    resize();
    draw();

    // IntersectionObserver to pause loop when scrolled out of view
    const observer = new IntersectionObserver(([entry]) => {
      isVisible = entry.isIntersecting;
      if (isVisible) {
        cancelAnimationFrame(animationFrameId);
        draw();
      }
    }, { threshold: 0.1 });

    observer.observe(canvas);
  } catch (err) {
    console.error("Error initializing hero canvas:", err);
  }
}

/**
 * Scroll reveal animations via IntersectionObserver
 */
function initScrollAnimations() {
  try {
    const revealElements = document.querySelectorAll(".reveal-on-scroll");
    if (!revealElements.length) return;

    if (!("IntersectionObserver" in window)) {
      revealElements.forEach(el => el.classList.add("is-visible"));
      return;
    }

    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.12,
      rootMargin: "0px 0px -40px 0px"
    });

    revealElements.forEach(el => observer.observe(el));
  } catch (err) {
    console.error("Error initializing scroll animations:", err);
  }
}

/**
 * Dynamic Events Page Renderer and Filtering
 */
function initEventsPage() {
  try {
    const preContainer = document.getElementById("pre-events-container");
    const mainContainer = document.getElementById("main-events-container");
    if (!preContainer && !mainContainer) return;

    if (preContainer) preContainer.innerHTML = "";
    if (mainContainer) mainContainer.innerHTML = "";

    EVENTS_DATA.forEach(ev => {
      const card = document.createElement("article");
      card.className = "cyber-card event-card reveal-on-scroll is-visible";
      card.setAttribute("data-group", ev.group);
      card.innerHTML = `
        <div class="event-poster-wrapper">
          <img src="${ev.poster}" alt="${ev.name} Poster" class="event-poster-img" loading="lazy">
        </div>
        <div class="event-body">
          <span class="event-category-badge">${ev.category}</span>
          <h3 class="event-title">${ev.name}</h3>
          <p class="event-desc">${ev.description}</p>
          <div class="event-action-footer">
            <a href="${REGISTER_URL}" class="btn btn-register" style="width: 100%;" data-register-btn>REGISTER NOW</a>
          </div>
        </div>
      `;

      if (ev.group === "pre" && preContainer) {
        preContainer.appendChild(card);
      } else if (ev.group === "main" && mainContainer) {
        mainContainer.appendChild(card);
      }
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
}

/**
 * Schedule Page Timeline Renderer and Tab Switching
 */
function initSchedulePage() {
  try {
    const timeline = document.getElementById("timeline-container");
    if (!timeline) return;

    timeline.innerHTML = "";

    SCHEDULE_DATA.forEach(item => {
      const entry = document.createElement("div");
      entry.className = "timeline-entry reveal-on-scroll is-visible";
      entry.setAttribute("data-day", item.day);
      entry.innerHTML = `
        <div class="timeline-node" aria-hidden="true"></div>
        <div class="timeline-card-wrapper">
          <div class="cyber-card timeline-card">
            <span class="timeline-time-badge">${item.time}</span>
            <h3 class="timeline-event-name">${item.name}</h3>
            <div class="timeline-venue">📍 ${item.venue}</div>
            <p class="timeline-note">${item.note}</p>
          </div>
        </div>
      `;
      timeline.appendChild(entry);
    });

    // Schedule Tabs
    const tabs = document.querySelectorAll(".schedule-tab-btn");
    tabs.forEach(tab => {
      tab.addEventListener("click", () => {
        tabs.forEach(t => t.classList.remove("active"));
        tab.classList.add("active");
        const selectedDay = tab.getAttribute("data-day");
        const entries = document.querySelectorAll(".timeline-entry");

        entries.forEach(entry => {
          if (selectedDay === "all" || entry.getAttribute("data-day") === selectedDay) {
            entry.style.display = "flex";
          } else {
            entry.style.display = "none";
          }
        });
      });
    });
  } catch (err) {
    console.error("Error initializing schedule page:", err);
  }
}

/**
 * Gallery Lightbox Viewer with Keyboard and Swipe Navigation
 */
function initGalleryPage() {
  try {
    const lightbox = document.getElementById("lightbox-modal");
    const lightboxImg = document.getElementById("lightbox-img");
    const lightboxCaption = document.getElementById("lightbox-caption");
    const closeBtn = document.getElementById("lightbox-close-btn");
    const prevBtn = document.getElementById("lightbox-prev-btn");
    const nextBtn = document.getElementById("lightbox-next-btn");
    const galleryCards = document.querySelectorAll(".gallery-card");

    if (!lightbox || !galleryCards.length) return;

    let currentIndex = 0;
    const galleryItems = Array.from(galleryCards).map(card => {
      const img = card.querySelector("img");
      const title = card.querySelector(".gallery-item-title");
      return {
        src: img ? img.getAttribute("src") : "",
        caption: title ? title.textContent : (img ? img.getAttribute("alt") : "")
      };
    });

    function showImage(index) {
      if (index < 0) index = galleryItems.length - 1;
      if (index >= galleryItems.length) index = 0;
      currentIndex = index;

      if (lightboxImg) lightboxImg.src = galleryItems[currentIndex].src;
      if (lightboxCaption) lightboxCaption.textContent = galleryItems[currentIndex].caption;
    }

    galleryCards.forEach((card, idx) => {
      card.addEventListener("click", () => {
        showImage(idx);
        lightbox.classList.add("is-active");
        document.body.style.overflow = "hidden";
      });
    });

    function closeLightbox() {
      lightbox.classList.remove("is-active");
      document.body.style.overflow = "";
    }

    if (closeBtn) closeBtn.addEventListener("click", closeLightbox);
    if (prevBtn) prevBtn.addEventListener("click", () => showImage(currentIndex - 1));
    if (nextBtn) nextBtn.addEventListener("click", () => showImage(currentIndex + 1));

    lightbox.addEventListener("click", (e) => {
      if (e.target === lightbox) closeLightbox();
    });

    document.addEventListener("keydown", (e) => {
      if (!lightbox.classList.contains("is-active")) return;
      if (e.key === "Escape") closeLightbox();
      if (e.key === "ArrowLeft") showImage(currentIndex - 1);
      if (e.key === "ArrowRight") showImage(currentIndex + 1);
    });
  } catch (err) {
    console.error("Error initializing gallery page:", err);
  }
}

