import os, json

# Read the existing js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate where getDefaults starts and where it ends
start_marker = "  getDefaults() {"
end_marker = "  getData() {"

idx_start = content.find(start_marker)
idx_end = content.find(end_marker)

if idx_start == -1 or idx_end == -1:
    print("Could not find markers in js/main.js")
    exit(1)

# Build the new authentic getDefaults content
new_defaults = '''  getDefaults() {
    return {
      settings: {
        eventDate: "2027-02-04T08:30:00+05:30",
        registerUrl: "https://presidencyuniversity.in/arenium27-register",
        tagline: "THE ARENA OF INNOVATION",
        prizePoolText: "⚡ TOTAL CASH PRIZE POOL: ₹1,50,000 (1.5 LAKHS) // ARENIUM '27 // 4–5 FEBRUARY 2027 // SCHOOL OF INFORMATION SCIENCE, PRESIDENCY UNIVERSITY ⚡",
        announcement: "⚡ ARENIUM ’27: THE ARENA OF INNOVATION // ₹1.5 LAKHS CASH PRIZE POOL // 24-HOUR HACKATHON, BLIND CODING, TREASURE HUNT, ESPORTS & FASHION SHOW // 4–5 FEB 2027 ⚡",
        qrCodeImg: "images/qrcode.png",
        logoImg: "images/logo.jpg",
        certificatesPublished: true,
        resultsPublished: true,
        adminPass: "PUSOIS27"
      },
      coordinators: [
        {
          id: "coord-1",
          name: "Kaushal Kumar Singh",
          role: "Finance & Registration Manager",
          dept: "5BCA01 (Reg: 20241BCA0051) · SOIS",
          phone: "+91 91087 40761",
          photo: "images/coord-kaushal.svg"
        },
        {
          id: "coord-2",
          name: "Vimal Raj",
          role: "Event Manager",
          dept: "5BCADS02 · SOIS",
          phone: "+91 96201 92249",
          photo: "images/coord-vimal.svg"
        },
        {
          id: "coord-3",
          name: "Ashlin Siddharth",
          role: "Marketing and Registration Manager",
          dept: "5BCADS01 · SOIS",
          phone: "+91 87976 86786",
          photo: "images/coord-ashlin.svg"
        },
        {
          id: "coord-4",
          name: "Abhyas Kathuria",
          role: "Technical Manager",
          dept: "5BCAAIML01 · SOIS",
          phone: "+91 85958 48421",
          photo: "images/coord-abhyas.svg"
        }
      ],
      leadership: [
        {
          id: "lead-dean",
          tag: "PATRON / DEAN",
          name: "Dr. C. Kalaiarasan",
          role: "Dean · School of Information Science",
          bio: "Guiding the academic vision, industry alliances, and innovation ecosystem of SOIS Presidency University.",
          photo: "images/leader-dean.svg"
        },
        {
          id: "lead-hod",
          tag: "HEAD OF DEPARTMENT",
          name: "Dr. K. G. Mohan",
          role: "HOD · School of Information Science",
          bio: "Fostering competitive coding culture, student research, and national collegiate hackathons across SOIS.",
          photo: "images/leader-hod.svg"
        },
        {
          id: "lead-org",
          tag: "OVERALL COORDINATOR",
          name: "Ms. Keren Lois Daniel",
          role: "Assistant Professor & Overall Coordinator · Arenium'27",
          bio: "Directing festival choreography, university operations, inter-departmental synergies, and student delegation.",
          photo: "images/leader-organiser.svg"
        },
        {
          id: "lead-pr",
          tag: "MARKETING & PR LEAD",
          name: "Ms. Neha Arora",
          role: "Assistant Professor & Marketing In-Charge · SOIS",
          bio: "Leading national collegiate outreach, digital campaigns, media partnerships, and corporate sponsorships.",
          photo: "images/leader-neha.svg"
        }
      ],
      soisFaculty: [
        {
          team: "Marketing & Promotion",
          faculty: "Ms. Neha Arora",
          students: "Anjani Soni M (5BCADS01), Rohit Roy (5BCA01), Saswata Chatterjee (5BCA02), Manas Kumar (5BCA02)",
          role: "Outreach & Social Media PR",
          photo: "images/leader-neha.svg"
        },
        {
          team: "Discipline & Campus Security",
          faculty: "Mr. Krishna Mishra & Mr. Dinesh N",
          students: "Hritik Raj (5BCA02), Vinayak Rathod (5BCA03), Kawatilya (5BCA01), Ayush Ranjan",
          role: "Campus Safety & Hall Control",
          photo: "images/leader-sois.svg"
        },
        {
          team: "Decoration & Ambiance",
          faculty: "Ms. Asha Hegde",
          students: "Ruchitha G (5BCADS01), Kavya Shree P M (5BCADS01), Nithyashree (5BCADS02), Bindu (5BCADS02)",
          role: "Aesthetics, Cyber Arena & Dais Decor",
          photo: "images/leader-sois.svg"
        },
        {
          team: "Hospitality & Refreshments",
          faculty: "Ms. Nagma Fariyal & Ms. Anjana",
          students: "Deepanita (5BCADS02), Arati Rai (5BCADS02), Manya Suresh (5BCA01), Harshita Periwal (5BCA03)",
          role: "Dignitary Care & Refreshment Counters",
          photo: "images/leader-sois.svg"
        },
        {
          team: "Media & Documentation",
          faculty: "Ms. Ghazala Zameer & Ms. Akasatha G R",
          students: "Vidyanshi Jain (5BCAAIML01), Tanmayee L (5BCADS01), Kiran Kurien (5BCADS02)",
          role: "Live Photography, Videography & Reels",
          photo: "images/leader-sois.svg"
        },
        {
          team: "Registration & Ticketing",
          faculty: "Ms. Devi S, Ms. Kalpana K, Mr. Sudharshan",
          students: "Shubham Kumar, Anchal Rodrigues, Naneshwaran, Rehana",
          role: "Helpdesk, Kits & Credentials Verification",
          photo: "images/leader-sois.svg"
        }
      ],
      events: [
        // 1. Tech Trail (Technical Treasure Hunt)
        {
          id: "tech-trail",
          name: "TECH TRAIL",
          category: "Technical Treasure Hunt",
          group: "main",
          prize: "₹15,000",
          venue: "AUD (Auditorium) & Campus",
          date: "Day 1 (4 February 2027)",
          time: "03:15 PM – 04:45 PM (2h 30m)",
          description: "Follow the clues, crack the code, and claim the victory. High-energy technical treasure hunt featuring Kahoot riddles, clue discovery within file properties, and rapid code error detection.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Kaushal Kumar Singh",
            phone: "+91 91087 40761",
            photo: "images/coord-kaushal.svg"
          },
          rulebook: {
            overview: "A 3-stage intellectual quest testing technical acumen, cryptic discovery, and algorithmic error detection across Presidency University campus.",
            eligibility: "Teams of 2 to 3 members. Participants must bring their own laptops. No AI tools permitted.",
            teamSize: "2 - 3 Members per team",
            rounds: [
              "Round 1: 20-minute Kahoot Quiz (20 questions covering riddles, logical puzzles, and technical reasoning).",
              "Round 2: Pickathon Clue Quest (45 minutes to find hidden clues embedded in file properties, metadata, and directory trees).",
              "Round 3: Code Error Detection (30 minutes to inspect code blocks and identify syntax/logic errors without compiling)."
            ],
            rules: [
              "Participants must carry their own charged laptops; charging points available at checkpoints.",
              "Strict proctoring against AI tools (ChatGPT, Copilot, etc.). Disqualification for tampering.",
              "Fastest accurate submission takes the podium."
            ],
            judging: "Aggregate score from Kahoot accuracy (30%), clue resolution speed (40%), and syntax bug spotting (30%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Trophies & Certificates"
          }
        },

        // 2. Code in the Dark
        {
          id: "code-dark",
          name: "CODE IN THE DARK",
          category: "Blind Coding Challenge",
          group: "main",
          prize: "₹15,000",
          venue: "SH3 (F Block)",
          date: "Day 1 (4 February 2027)",
          time: "R1: 11:30 AM | R2: 02:00 PM | Finals: 03:15 PM",
          description: "Think fast. Code smart. Debug in the dark. The ultimate blind programming challenge where developers write code with their monitors turned OFF.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Abhyas Kathuria",
            phone: "+91 85958 48421",
            photo: "images/coord-abhyas.svg"
          },
          rulebook: {
            overview: "Intense competitive programming event where contestants demonstrate pure muscle memory, algorithmic syntax mastery, and rapid debugging.",
            eligibility: "Solo participation. Open to all engineering and computer science undergraduates.",
            teamSize: "1 Participant",
            rounds: [
              "Round 1: Code Debugging Sprint (Fix 5 faulty algorithmic scripts in 25 minutes).",
              "Round 2: Blind Coding (Screens turned OFF; write algorithms for primes, palindromes, or math series from memory).",
              "Round 3: Optic Code Challenge (Solve the master problem in the minimum possible lines of code — code golf)."
            ],
            rules: [
              "Supported languages: C, C++, Java, Python 3.",
              "Monitors must remain completely powered off during Round 2 until time is called.",
              "Code that compiles and passes the maximum hidden test cases wins."
            ],
            judging: "Compilation success, test case coverage, execution time, and line count efficiency.",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Certificates"
          }
        },

        // 3. DesignX
        {
          id: "design-x",
          name: "DESIGNX",
          category: "UI/UX Design Challenge",
          group: "main",
          prize: "₹15,000",
          venue: "SH2 (E Block), Day 1",
          date: "Day 1 (4 February 2027)",
          time: "11:30 AM – 03:00 PM",
          description: "Imagine the experience. Design the future. Fast-paced UI/UX sprint and interactive paper/design presentation tackling modern digital product challenges.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Ashlin Siddharth",
            phone: "+91 87976 86786",
            photo: "images/coord-ashlin.svg"
          },
          rulebook: {
            overview: "Participants receive an on-the-spot problem statement to craft an intuitive mobile/web product interface, user journey map, and clickable prototype.",
            eligibility: "Solo or teams of 2 members. Bring laptops with Figma / Adobe XD installed.",
            teamSize: "1 - 2 Participants",
            rounds: [
              "Phase 1: Briefing & UX Research (30 minutes user journey formulation).",
              "Phase 2: High-Fidelity Wireframing & Prototyping (2 hours Figma design sprint).",
              "Phase 3: Jury Presentation & Live Interactive Defense (5 minutes per team)."
            ],
            rules: [
              "All component libraries and design assets must be created or customized on-site.",
              "Pre-built downloadable commercial UI kits will be penalized.",
              "Design must be responsive and follow accessibility guidelines (WCAG)."
            ],
            judging: "Usability (30%), Visual Aesthetics (30%), Innovation (25%), Pitch Presentation (15%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Trophies"
          }
        },

        // 4. TechTalk / STARTUPSTARS (Venture Arena)
        {
          id: "startup-stars",
          name: "TECHTALK / STARTUPSTARS",
          category: "Startup Pitching & Venture Arena",
          group: "main",
          prize: "₹15,000",
          venue: "SH2 (E Block), Day 2",
          date: "Day 2 (5 February 2027)",
          time: "09:30 AM – 01:00 PM",
          description: "Pitch the vision. Spark the enterprise. Shark Tank style startup pitching and paper presentation (PITCHTHON) before venture evaluators and industry experts.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Vimal Raj",
            phone: "+91 96201 92249",
            photo: "images/coord-vimal.svg"
          },
          rulebook: {
            overview: "A business-meets-technology pitching battle where founders showcase disruptive tech startups, market research, revenue models, and MVP prototypes.",
            eligibility: "Teams of 2 to 4 members. Cross-department and inter-college teams permitted.",
            teamSize: "2 - 4 Participants",
            rounds: [
              "Round 1: Pitch Deck & Executive Summary Submission (Pre-screening).",
              "Round 2: Live 7-Minute Pitch + 5-Minute Investor Q&A grilling on dais."
            ],
            rules: [
              "Pitch deck must cover: Problem, Solution, Tech Stack, Market Size, Revenue Model, and Team.",
              "Working software MVP or hardware demonstration carries extra weightage.",
              "Judges' investment allocation determines final ranking."
            ],
            judging: "Market Feasibility (30%), Technological Innovation (30%), Financial Model (20%), Pitch Delivery (20%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Incubation Support"
          }
        },

        // 5. Data Tales
        {
          id: "data-tales",
          name: "DATA TALES",
          category: "Data to Deployment Challenge",
          group: "main",
          prize: "₹15,000",
          venue: "SH3 (F Block), Day 2",
          date: "Day 2 (5 February 2027)",
          time: "09:30 AM – 01:00 PM",
          description: "Discover the story. Decode the data. Deliver the insight. A 3-stage data science challenge: ingest complex raw datasets, build machine learning models, and deploy executive dashboards.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Abhyas Kathuria",
            phone: "+91 85958 48421",
            photo: "images/coord-abhyas.svg"
          },
          rulebook: {
            overview: "End-to-end data pipeline championship from exploratory data analysis (EDA) to production deployment and business intelligence storytelling.",
            eligibility: "Teams of 2 participants. Must bring laptops configured with Python/R, Jupyter, and Streamlit/PowerBI.",
            teamSize: "2 Participants",
            rounds: [
              "Stage 1: Dataset Release & Exploratory Data Analysis (Cleaning & Feature Engineering).",
              "Stage 2: Model Training & Predictive Performance (Accuracy, F1-Score benchmarking).",
              "Stage 3: Deployment & Executive Storytelling (Interactive web dashboard presentation)."
            ],
            rules: [
              "All code must be versioned in a newly initialized Git repository during the event.",
              "Pre-trained custom weights or external leaked labels are forbidden.",
              "Submissions evaluated on test hold-out data split."
            ],
            judging: "Data Preprocessing (25%), Model Robustness (35%), Dashboard UI (20%), Storytelling Impact (20%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Merit Certificates"
          }
        },

        // 6. Prompt to Prototype
        {
          id: "prompt-prototype",
          name: "PROMPT TO PROTOTYPE",
          category: "Generative AI Project Expo",
          group: "main",
          prize: "₹15,000",
          venue: "SH4 (F Block), Day 1",
          date: "Day 1 (4 February 2027)",
          time: "11:30 AM – 04:30 PM",
          description: "Imagine it. Prompt it. Build it. Showcase generative AI applications, autonomous agents, and AI-accelerated prototypes solving real-world challenges.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Ashlin Siddharth",
            phone: "+91 87976 86786",
            photo: "images/coord-ashlin.svg"
          },
          rulebook: {
            overview: "Project expo and rapid prototype competition highlighting generative AI, multimodal agents, prompt engineering pipelines, and full-stack AI demos.",
            eligibility: "Teams of 2 to 3 members. Prototype must be operational for live demonstration.",
            teamSize: "2 - 3 Members",
            rounds: [
              "Phase 1: Booth Setup and Architecture Poster Display.",
              "Phase 2: Jury Inspection, Live Code Walkthrough, and Failure Handling Demo.",
              "Phase 3: Open Participant Viewing & Crowd Favorite Voting."
            ],
            rules: [
              "Working prototype must be demonstrated live on contestant laptops.",
              "Prompt engineering architecture and guardrails must be documented.",
              "Teams must justify utility, cost efficiency, and real-world viability."
            ],
            judging: "Originality (30%), Technological Depth (30%), Practical Impact (25%), Presentation (15%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Trophies"
          }
        },

        // 7. TechVerse ’27 (ByteBlitz 24-Hour Hackathon)
        {
          id: "techverse-hackathon",
          name: "TECHVERSE ’27 (BYTEBLITZ 24H HACKATHON)",
          category: "24-Hour National Hackathon",
          group: "main",
          prize: "₹22,500",
          venue: "Old Prayer Hall (E Block, 4th Floor)",
          date: "4–5 February 2027 (Overnight 24H)",
          time: "Day 1 11:30 AM Kickoff to Day 2 01:00 PM Demos",
          description: "24 Hours. One mission. Limitless innovation. Presidency University's flagship overnight hackathon with problem statements sourced from Smart India Hackathon and industry sponsors.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Abhyas Kathuria",
            phone: "+91 85958 48421",
            photo: "images/coord-abhyas.svg"
          },
          rulebook: {
            overview: "A non-stop 24-hour innovation sprint bringing top collegiate coders to build production-grade web, mobile, blockchain, or AI solutions.",
            eligibility: "Teams of strictly 4 members. Registration fee: ₹1,500 per team (includes breakfast, lunch, dinner, midnight snacks & stay).",
            teamSize: "Strictly 4 Members per team",
            rounds: [
              "Kickoff: Problem statement reveal at 11:30 AM Day 1.",
              "Checkpoint 1: Mentorship review at 04:00 PM Day 1.",
              "Checkpoint 2: Midnight architecture verification at 12:00 AM.",
              "Final Demos: 11:00 AM – 01:00 PM Day 2 before industry jury panel."
            ],
            rules: [
              "All code must be written during the 24-hour window; fresh Git commit history verified.",
              "Open-source libraries permitted with proper attribution; no turnkey templates.",
              "Teams must observe common break rules (13:00–14:00 lunch clock pause)."
            ],
            judging: "Technical Innovation (35%), Product Completion (30%), UI/UX (20%), Pitch Demo (15%).",
            cashPrize: "Winner: ₹12,000 | Runner-up: ₹7,000 | Best AI Prototype: ₹3,500 + Trophies & Medals"
          }
        },

        // 8. BrainByte
        {
          id: "brain-byte",
          name: "BRAINBYTE",
          category: "Technical Stage Quiz",
          group: "main",
          prize: "₹15,000",
          venue: "AUD (Auditorium)",
          date: "Day 1 (Prelims 2 PM) & Day 2 (Finals 10 AM)",
          time: "Day 1 02:00 PM – 03:00 PM | Day 2 10:00 AM – 11:30 AM",
          description: "Battle of the bytes. Master of logic. High-voltage technical stage quiz covering computing history, cryptography, hardware architectures, and AI trivia with live audience buzzers.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Kaushal Kumar Singh",
            phone: "+91 91087 40761",
            photo: "images/coord-kaushal.svg"
          },
          rulebook: {
            overview: "A battle of intellect testing computer science trivia, algorithms, tech pioneers, and cyber lore with electronic buzzers on the main auditorium stage.",
            eligibility: "Teams of 2 members. Open to all students.",
            teamSize: "2 Participants per team",
            rounds: [
              "Round 1: Written Prelims (30 questions in 30 minutes in Auditorium, top 6 teams qualify).",
              "Round 2: Grand Stage Finals (Audio-Visual, Code Output, Wager Round, and Rapid Buzzer Finale)."
            ],
            rules: [
              "No smart devices, phones, or notes allowed inside the testing hall.",
              "Negative points apply in the stage buzzer round for false triggers.",
              "Quizmaster's ruling is conclusive."
            ],
            judging: "Objective point tallies on electronic scoring display.",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Stage Felicitation"
          }
        },

        // 9. Squad Damage (Pixel Showdown)
        {
          id: "squad-damage",
          name: "SQUAD DAMAGE (PIXEL SHOWDOWN)",
          category: "Esports Championship",
          group: "main",
          prize: "₹15,000",
          venue: "SH4 / Classroom DJL01, Day 2",
          date: "Day 2 (5 February 2027)",
          time: "09:30 AM – 03:00 PM",
          description: "Lock in. Frag out. Rule the arena. Championship esports tournament featuring Valorant (PC 5v5), BGMI (Mobile Squads), and Call of Duty with live match broadcasts.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Ashlin Siddharth",
            phone: "+91 87976 86786",
            photo: "images/coord-ashlin.svg"
          },
          rulebook: {
            overview: "Collegiate esports championship played across custom dedicated rooms with tournament referee monitoring and caster stream.",
            eligibility: "Teams of 1 to 4 members. Must carry college IDs and own mobile/peripherals.",
            teamSize: "1 - 4 Players per squad",
            rounds: [
              "Stage 1: Custom Room Qualifiers (Single Elimination, 20-30 teams).",
              "Stage 2: Semi-Finals & Grand Finals projected on big screens."
            ],
            rules: [
              "Strict anti-cheat policy. Any emulation, macros, or mods cause instant disqualification.",
              "Stable campus Wi-Fi provided; players may also use personal cellular hotspots.",
              "Unsportsmanlike conduct or toxicity leads to team forfeiture."
            ],
            judging: "Official in-game match results verified by match referees.",
            cashPrize: "Valorant Champion: ₹6,000 | BGMI Champion: ₹5,000 | Call of Duty Champion: ₹4,000 + Trophies"
          }
        },

        // 10. TECHNO - Organic Synthesis
        {
          id: "techno-fashion",
          name: "TECHNO - ORGANIC SYNTHESIS",
          category: "Tech × Nature Themed Fashion Show",
          group: "main",
          prize: "₹15,000",
          venue: "AUD (Auditorium), Day 2",
          date: "Day 2 (5 February 2027)",
          time: "03:00 PM – 04:00 PM",
          description: "Where nature meets innovation, style becomes the future. A flagship themed fashion runway combining futuristic technology, wearable electronics, and sustainable organic materials.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Vimal Raj",
            phone: "+91 96201 92249",
            photo: "images/coord-vimal.svg"
          },
          rulebook: {
            overview: "A spectacular runway experience where futuristic cyber aesthetics blend with nature-inspired elements, smart textiles, wearable LEDs, and recyclable tech fabrics.",
            eligibility: "Teams of 5 to 10 members (models, designers, and backstage support).",
            teamSize: "5 - 10 Members per team",
            rounds: [
              "Runway Round: 8-minute choreographed team walk with music and thematic narration.",
              "Concept Defense: 2-minute Q&A with fashion and tech judges explaining material sustainability."
            ],
            rules: [
              "Outfits must reflect the 'Technology × Nature' theme (recyclable materials, microcontrollers, fibre optics).",
              "Soundtrack and visual backdrop must be submitted 2 hours before the event.",
              "Costume changes must happen within assigned green rooms."
            ],
            judging: "Theme Interpretation (30%), Design Creativity (30%), Stage Walk & Poise (25%), Material Innovation (15%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | Best Creative Ensemble: ₹2,500 + Trophies"
          }
        },

        // 11. Arenium Premier League (APL)
        {
          id: "apl-auction",
          name: "ARENIUM PREMIER LEAGUE (APL)",
          category: "Strategic Brand Auction & Simulation",
          group: "main",
          prize: "₹15,000",
          venue: "SH1 (E Block), Day 2",
          date: "Day 2 (5 February 2027)",
          time: "09:30 AM – 01:00 PM",
          description: "Bid the best. Build the empire. An IPL-style strategic corporate auction and business simulation where teams manage virtual capital, acquire brands, and deliver growth portfolios.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Kaushal Kumar Singh",
            phone: "+91 91087 40761",
            photo: "images/coord-kaushal.svg"
          },
          rulebook: {
            overview: "Tailored for business, commerce, and tech-strategy minds. Teams navigate an auction bidding war for iconic conglomerates, analyze market dynamics, and pitch expansion strategies.",
            eligibility: "Teams of 2 to 3 members.",
            teamSize: "2 - 3 Members per team",
            rounds: [
              "Round 1: Virtual Budget Bidding Auction (Acquiring brands like Tata, Reliance, Apple, Google).",
              "Round 2: Brand Strategy SWOT & Crisis Simulation (Overcoming competitive market disruption).",
              "Round 3: Executive Portfolio Defense (Presenting corporate turnaround deck to the jury)."
            ],
            rules: [
              "Teams operate within a strictly capped virtual purse limit; budget overruns incur penalties.",
              "Collusion between bidding teams is barred.",
              "Valuation calculations must be supported by sound financial logic."
            ],
            judging: "Auction Resource Management (35%), Strategic Analysis (35%), Presentation Delivery (30%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Merit Certificates"
          }
        }
      ],
      schedule: [
        // --- DAY 1: THURSDAY, 4 FEBRUARY 2027 ---
        {
          day: "Day 1",
          time: "08:30 AM – 10:00 AM",
          name: "Delegate Registration, ID Check & Kit Distribution",
          venue: "Auditorium Foyer & Central Desk",
          note: "Delegate badge issue, participant kits & breakfast distribution; guests received from 09:30 AM",
          category: "Registration"
        },
        {
          day: "Day 1",
          time: "10:00 AM – 11:30 AM",
          name: "Arena Ignition (Inauguration Ceremony)",
          venue: "AUD (Main Auditorium)",
          note: "Theme: Let the Games Begin. Lamp lighting, welcome address by Dean & HOD, curtain-raiser video, Chief Guest address & fest brochure release",
          category: "Ceremony"
        },
        {
          day: "Day 1",
          time: "11:30 AM – 01:00 PM",
          name: "Round 1 Multi-Venue Kickoff",
          venue: "AUD, Old Prayer Hall, SH2, SH3, SH4",
          note: "Arena Talks 1 (AUD) | ByteBlitz 24H Hackathon kickoff (Old Prayer Hall) | DesignX UI/UX (SH2) | Code in the Dark R1 (SH3) | Prompt to Prototype setup (SH4)",
          category: "Technical"
        },
        {
          day: "Day 1",
          time: "01:00 PM – 02:00 PM",
          name: "Common Lunch Break (Venues Paused)",
          venue: "University Dining Concourse",
          note: "Break Rule: All venues closed and ByteBlitz clock is strictly paused. Refreshment counters open for participants, judges & volunteers",
          category: "Break"
        },
        {
          day: "Day 1",
          time: "02:00 PM – 03:00 PM",
          name: "BrainByte Prelims & Technical Sprints",
          venue: "AUD, Old Prayer Hall, SH2, SH3, SH4",
          note: "BrainByte written prelims (AUD) | ByteBlitz build sprint resumes | DesignX presentations (SH2) | Code in the Dark R2 (SH3) | Prompt to Prototype open viewing (SH4)",
          category: "Technical"
        },
        {
          day: "Day 1",
          time: "03:00 PM – 03:15 PM",
          name: "Evening Tea Break (Venues Paused)",
          venue: "Central Refreshment Counters",
          note: "Break Rule: All events paused; participants take evening tea & refreshments",
          category: "Break"
        },
        {
          day: "Day 1",
          time: "03:15 PM – 04:15 PM",
          name: "Tech Trail Hunt & Arena Connect",
          venue: "Campus Grounds, AUD, SH3",
          note: "Tech Trail Kahoot & Pickathon clues | Arena Connect industry networking (AUD) | Code in the Dark Finals (SH3) | ByteBlitz sprint continues",
          category: "Technical"
        },
        {
          day: "Day 1",
          time: "04:15 PM – 04:45 PM",
          name: "Day 1 Shortlisting Window",
          venue: "SH1 (E Block - Judges' Chamber)",
          note: "Judges tally scores for DesignX, Code in the Dark, Prompt to Prototype and BrainByte; finalists verified",
          category: "Judging"
        },
        {
          day: "Day 1",
          time: "04:45 PM – 05:15 PM",
          name: "Day 1 Wrap-up & Day 2 Briefing",
          venue: "AUD (Main Auditorium)",
          note: "Finalist announcements, schedule overview for Day 2 finals & instructions for overnight hackathon squads",
          category: "Briefing"
        },
        {
          day: "Day 1",
          time: "05:15 PM – 05:45 PM",
          name: "Hall Reset & Security Locking",
          venue: "SH4 (F Block)",
          note: "SH4 converted from AI expo into the Squad Damage Gaming Arena; night security lock engaged",
          category: "Operations"
        },

        // --- DAY 2: FRIDAY, 5 FEBRUARY 2027 ---
        {
          day: "Day 2",
          time: "08:30 AM – 09:30 AM",
          name: "Reporting, Finalist Attendance & Breakfast",
          venue: "Auditorium Foyer & Venues",
          note: "Day 2 finalist check-in, ByteBlitz overnight sprint review & morning breakfast distribution",
          category: "Registration"
        },
        {
          day: "Day 2",
          time: "09:30 AM – 01:00 PM",
          name: "Grand Finals Morning Block",
          venue: "AUD, Old Prayer Hall, SH1, SH2, SH3, SH4",
          note: "BrainByte Finals stage quiz (10:00–11:30 AUD) | ByteBlitz demos & judging (11:00–13:00 Old Prayer Hall) | STARTUPSTARS Venture Arena (SH2) | Data Tales (SH3) | Squad Damage Esports (SH4) | APL Auction (SH1)",
          category: "Finals"
        },
        {
          day: "Day 2",
          time: "01:00 PM – 02:00 PM",
          name: "Common Lunch Break (Venues Paused)",
          venue: "University Dining Concourse",
          note: "Break Rule: All venues closed. Full lunch served to all delegates, faculty, and guests",
          category: "Break"
        },
        {
          day: "Day 2",
          time: "02:00 PM – 03:00 PM",
          name: "Arena Talks 2 & Esports Championship Finals",
          venue: "AUD & SH4",
          note: "Arena Talks 2: Alumni founders & startup stories (AUD) | Squad Damage Grand Finals casted on big screens (SH4)",
          category: "Finals"
        },
        {
          day: "Day 2",
          time: "03:00 PM – 04:00 PM",
          name: "TECHNO - Organic Synthesis (Fashion Runway)",
          venue: "AUD (Main Auditorium)",
          note: "Flagship runway show: Technology × Nature wearable electronics, LED fashion & sustainable materials",
          category: "Flagship"
        },
        {
          day: "Day 2",
          time: "03:00 PM – 04:30 PM",
          name: "Official 90-Minute Winner Selection Window",
          venue: "SH1 (E Block - Judges' Chamber)",
          note: "All events closed. Judges complete scoring sheets, tie-break verification with Fest Coordination Committee, and certificates preparation",
          category: "Judging"
        },
        {
          day: "Day 2",
          time: "04:30 PM – 04:45 PM",
          name: "Auditorium Seating & Sealed Results Handover",
          venue: "AUD (Main Auditorium)",
          note: "Participants, dignitaries & faculty take seats in AUD; sealed results envelopes delivered to stage emcee",
          category: "Ceremony"
        },
        {
          day: "Day 2",
          time: "04:45 PM – 05:45 PM",
          name: "Arena Crowning (Valedictory & Prize Distribution)",
          venue: "AUD (Main Auditorium)",
          note: "Official announcement of results, handover of ₹1.5 Lakhs cash prizes, trophies, medals, sponsor mementoes & vote of thanks",
          category: "Awards"
        },
        {
          day: "Day 2",
          time: "05:45 PM – 06:15 PM",
          name: "Closing Group Photo & Certificate Download Access",
          venue: "University Central Amphitheatre",
          note: "Grand fest photo with leadership, coordinators & participants; online certificate framing studio opened",
          category: "Ceremony"
        }
      ],
      winners: [
        {
          eventId: "techverse-hackathon",
          eventName: "TECHVERSE ’27 (BYTEBLITZ 24H HACKATHON)",
          category: "24-Hour Hackathon",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "Quantum Coders (4 Members)",
              college: "Presidency University (SOIS)",
              prize: "₹12,000",
              certId: "AR27-HCK-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "Neural Knights",
              college: "RV College of Engineering",
              prize: "₹7,000",
              certId: "AR27-HCK-002"
            },
            {
              rank: 3,
              title: "BEST AI PROTOTYPE",
              team: "Agentic Forge",
              college: "BMS College of Engineering",
              prize: "₹3,500",
              certId: "AR27-HCK-003"
            }
          ]
        },
        {
          eventId: "tech-trail",
          eventName: "TECH TRAIL",
          category: "Technical Treasure Hunt",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "Cipher Scavengers",
              college: "Presidency University",
              prize: "₹8,000",
              certId: "AR27-TRL-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "Binary Bloodhounds",
              college: "PES University",
              prize: "₹4,500",
              certId: "AR27-TRL-002"
            },
            {
              rank: 3,
              title: "2ND RUNNER UP (3RD PLACE)",
              team: "Node Seekers",
              college: "New Horizon College of Engg",
              prize: "₹2,500",
              certId: "AR27-TRL-003"
            }
          ]
        },
        {
          eventId: "code-dark",
          eventName: "CODE IN THE DARK",
          category: "Blind Coding",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "Rohan Varma",
              college: "Presidency University (SOIS)",
              prize: "₹8,000",
              certId: "AR27-CDK-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "Ananya Deshmukh",
              college: "Ramaiah Institute of Technology",
              prize: "₹4,500",
              certId: "AR27-CDK-002"
            },
            {
              rank: 3,
              title: "2ND RUNNER UP (3RD PLACE)",
              team: "Siddharth Rao",
              college: "Dayananda Sagar College",
              prize: "₹2,500",
              certId: "AR27-CDK-003"
            }
          ]
        },
        {
          eventId: "design-x",
          eventName: "DESIGNX",
          category: "UI/UX Design Challenge",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "Pixel Matrix (Aarav & Meera)",
              college: "Presidency University",
              prize: "₹8,000",
              certId: "AR27-DSX-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "Figma Wizards",
              college: "NIFT Bengaluru",
              prize: "₹4,500",
              certId: "AR27-DSX-002"
            },
            {
              rank: 3,
              title: "2ND RUNNER UP (3RD PLACE)",
              team: "Interface Labs",
              college: "Christ University",
              prize: "₹2,500",
              certId: "AR27-DSX-003"
            }
          ]
        },
        {
          eventId: "startup-stars",
          eventName: "TECHTALK / STARTUPSTARS",
          category: "Startup Pitching (PITCHTHON)",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "GreenGrid AI",
              college: "Presidency University",
              prize: "₹8,000",
              certId: "AR27-STP-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "MediPulse Robotics",
              college: "PES University",
              prize: "₹4,500",
              certId: "AR27-STP-002"
            },
            {
              rank: 3,
              title: "2ND RUNNER UP (3RD PLACE)",
              team: "KisanDrone Tech",
              college: "Jain University",
              prize: "₹2,500",
              certId: "AR27-STP-003"
            }
          ]
        },
        {
          eventId: "data-tales",
          eventName: "DATA TALES",
          category: "Data to Deployment",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "Data Dynamos (Karan & Priya)",
              college: "Presidency University (SOIS)",
              prize: "₹8,000",
              certId: "AR27-DTA-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "Vector Minds",
              college: "RVCE Bengaluru",
              prize: "₹4,500",
              certId: "AR27-DTA-002"
            },
            {
              rank: 3,
              title: "2ND RUNNER UP (3RD PLACE)",
              team: "Pandas Overload",
              college: "BMSIT Bengaluru",
              prize: "₹2,500",
              certId: "AR27-DTA-003"
            }
          ]
        },
        {
          eventId: "squad-damage",
          eventName: "SQUAD DAMAGE (PIXEL SHOWDOWN)",
          category: "Esports Championship",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "Team Shadow Protocol",
              college: "Presidency University",
              prize: "₹6,000",
              certId: "AR27-SQD-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "Cyber Strikers",
              college: "Dayananda Sagar College",
              prize: "₹5,000",
              certId: "AR27-SQD-002"
            },
            {
              rank: 3,
              title: "2ND RUNNER UP (3RD PLACE)",
              team: "Vortex Esports",
              college: "Presidency University (SOIS)",
              prize: "₹4,000",
              certId: "AR27-SQD-003"
            }
          ]
        },
        {
          eventId: "techno-fashion",
          eventName: "TECHNO - ORGANIC SYNTHESIS",
          category: "Fashion Runway",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "CyberFlora Couture",
              college: "Presidency University",
              prize: "₹8,000",
              certId: "AR27-FSH-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "BioLumino Squad",
              college: "Mount Carmel College",
              prize: "₹4,500",
              certId: "AR27-FSH-002"
            },
            {
              rank: 3,
              title: "2ND RUNNER UP (3RD PLACE)",
              team: "EcoSilicon Ensemble",
              college: "Presidency University (SOIS)",
              prize: "₹2,500",
              certId: "AR27-FSH-003"
            }
          ]
        },
        {
          eventId: "apl-auction",
          eventName: "ARENIUM PREMIER LEAGUE (APL)",
          category: "Brand Auction & Strategy",
          tiers: [
            {
              rank: 1,
              title: "CHAMPION (1ST PLACE)",
              team: "The Sovereign Tycoons",
              college: "Presidency University",
              prize: "₹8,000",
              certId: "AR27-APL-001"
            },
            {
              rank: 2,
              title: "RUNNER UP (2ND PLACE)",
              team: "Apex Investors",
              college: "Christ University",
              prize: "₹4,500",
              certId: "AR27-APL-002"
            },
            {
              rank: 3,
              title: "2ND RUNNER UP (3RD PLACE)",
              team: "Venture Sharks",
              college: "St. Joseph's University",
              prize: "₹2,500",
              certId: "AR27-APL-003"
            }
          ]
        }
      ],
      certificates: [
        { id: "AR27-HCK-001", recipient: "Quantum Coders", event: "TECHVERSE ’27 (BYTEBLITZ 24H HACKATHON)", award: "CHAMPION // FIRST PLACE", college: "Presidency University (SOIS)", issueDate: "5 February 2027", verified: true },
        { id: "AR27-TRL-001", recipient: "Cipher Scavengers", event: "TECH TRAIL", award: "CHAMPION // FIRST PLACE", college: "Presidency University", issueDate: "4 February 2027", verified: true },
        { id: "AR27-CDK-001", recipient: "Rohan Varma", event: "CODE IN THE DARK", award: "CHAMPION // FIRST PLACE", college: "Presidency University (SOIS)", issueDate: "4 February 2027", verified: true },
        { id: "AR27-DSX-001", recipient: "Pixel Matrix", event: "DESIGNX", award: "CHAMPION // FIRST PLACE", college: "Presidency University", issueDate: "4 February 2027", verified: true },
        { id: "AR27-STP-001", recipient: "GreenGrid AI", event: "TECHTALK / STARTUPSTARS", award: "CHAMPION // FIRST PLACE", college: "Presidency University", issueDate: "5 February 2027", verified: true },
        { id: "AR27-DTA-001", recipient: "Data Dynamos", event: "DATA TALES", award: "CHAMPION // FIRST PLACE", college: "Presidency University (SOIS)", issueDate: "5 February 2027", verified: true },
        { id: "AR27-SQD-001", recipient: "Team Shadow Protocol", event: "SQUAD DAMAGE (PIXEL SHOWDOWN)", award: "CHAMPION // FIRST PLACE", college: "Presidency University", issueDate: "5 February 2027", verified: true },
        { id: "AR27-FSH-001", recipient: "CyberFlora Couture", event: "TECHNO - ORGANIC SYNTHESIS", award: "CHAMPION // FIRST PLACE", college: "Presidency University", issueDate: "5 February 2027", verified: true },
        { id: "AR27-APL-001", recipient: "The Sovereign Tycoons", event: "ARENIUM PREMIER LEAGUE (APL)", award: "CHAMPION // FIRST PLACE", college: "Presidency University", issueDate: "5 February 2027", verified: true }
      ],
      sponsors: [
        {
          id: "sp-title",
          name: "PRESIDENCY UNIVERSITY",
          tier: "Host Institution",
          logo: "images/logo.jpg",
          url: "https://presidencyuniversity.in"
        },
        {
          id: "sp-1",
          name: "SMART INDIA HACKATHON PARTNER",
          tier: "Innovation Partner",
          logo: "images/sponsor-1.svg",
          url: "https://presidencyuniversity.in"
        },
        {
          id: "sp-2",
          name: "CYBER MATRIX TECH",
          tier: "Title Sponsor",
          logo: "images/sponsor-title.svg",
          url: "https://presidencyuniversity.in"
        },
        {
          id: "sp-3",
          name: "GLITCHWORKS GAMING",
          tier: "Esports & Gaming Partner",
          logo: "images/sponsor-2.svg",
          url: "https://presidencyuniversity.in"
        },
        {
          id: "sp-4",
          name: "SYNTH CLOUD SOLUTIONS",
          tier: "Cloud Infrastructure Partner",
          logo: "images/sponsor-3.svg",
          url: "https://presidencyuniversity.in"
        },
        {
          id: "sp-5",
          name: "CYBERPULSE ENERGY",
          tier: "Official Beverage Partner",
          logo: "images/sponsor-4.svg",
          url: "https://presidencyuniversity.in"
        }
      ],
      gallery: [
        { id: "g-1", src: "images/gallery-1.svg", title: "Arena Ignition Inauguration", tag: "Main Stage" },
        { id: "g-2", src: "images/gallery-2.svg", title: "ByteBlitz 24H Hackathon Sprint", tag: "Hackathon" },
        { id: "g-3", src: "images/gallery-3.svg", title: "Tech Trail Cryptic Clue Solvers", tag: "Treasure Hunt" },
        { id: "g-4", src: "images/gallery-4.svg", title: "Squad Damage Esports Battlegrounds", tag: "Gaming" },
        { id: "g-5", src: "images/gallery-5.svg", title: "TECHNO Fashion Runway", tag: "Fashion Show" },
        { id: "g-6", src: "images/gallery-6.svg", title: "Arena Crowning & ₹1.5L Prize Handover", tag: "Awards" }
      ]
    };
  },
'''

# Update storage key to v3
content_new = content.replace('STORAGE_KEY: "arenium_fest_db_v2",', 'STORAGE_KEY: "arenium_fest_db_v3",')

# Replace getDefaults block
idx_start = content_new.find(start_marker)
idx_end = content_new.find(end_marker)
content_new = content_new[:idx_start] + new_defaults + "\n" + content_new[idx_end:]

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(content_new)

print('js/main.js successfully updated with authentic official events, committee, and schedule!')
