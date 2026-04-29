/* ===== COUNTDOWN (SAFE CHECK) ===== */

const timer = document.getElementById("countdown");

if (timer) {
    const eventDate = new Date("Feb 5, 2026 09:30:00").getTime();

    setInterval(() => {
        const now = new Date().getTime();
        const diff = eventDate - now;

        if (diff > 0) {
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            timer.innerHTML = days + " Days Remaining";
        } else {
            timer.innerHTML = "Event Live";
        }
    }, 1000);
}

/* ===== PARALLAX LOGO ===== */

const logo = document.querySelector(".parallax-logo");

if (logo) {
    window.addEventListener("mousemove", (e) => {
        const x = (window.innerWidth / 2 - e.clientX) / 25;
        const y = (window.innerHeight / 2 - e.clientY) / 25;
        logo.style.transform = `translate(${x}px, ${y}px)`;
    });
}

/* ===== REGISTRATION SUCCESS TRANSITION ===== */

function handleSubmit(event) {
    event.preventDefault();

    const overlay = document.getElementById("successOverlay");
    overlay.classList.add("active");

    setTimeout(() => {
        window.location.href = "index.html";
    }, 1800);
}
