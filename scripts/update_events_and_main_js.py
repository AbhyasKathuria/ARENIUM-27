import re

events_code = """      events: [
        // 1. Tech Odyssey (Technical Event)
        {
          id: "tech-odyssey",
          name: "TECH ODYSSEY",
          tagline: "Follow the Clues. Crack the Code. Claim the Victory",
          category: "Technical Event",
          group: "technical",
          prize: "₹15,000",
          venue: "SOIS Block & Central Campus",
          date: "Day 1 (4 February 2027)",
          time: "10:45 AM – 01:00 PM",
          description: "Follow the Clues. Crack the Code. Claim the Victory. A 3-stage intellectual quest testing technical acumen, cryptic discovery, and algorithmic error detection across Presidency University campus.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Kaushal Kumar Singh",
            phone: "+91 91087 40761",
            photo: "images/coord-kaushal.svg"
          },
          rulebook: {
            overview: "Follow the Clues. Crack the Code. Claim the Victory. High-energy technical treasure hunt featuring Kahoot riddles, clue discovery within file properties, and rapid code error detection.",
            eligibility: "Teams of 2 to 3 members. Participants must bring their own laptops. No AI tools permitted.",
            teamSize: "2 - 3 Members per team",
            rounds: [
              "Round 1: Kahoot Quiz (20 questions covering riddles, logical puzzles, and technical reasoning).",
              "Round 2: Pickathon Clue Quest (Finding hidden clues embedded in file properties, metadata, and directory trees).",
              "Round 3: Code Error Spotting (Inspecting code blocks and identifying syntax/logic errors without compiling)."
            ],
            rules: [
              "Participants must carry their own charged laptops; charging stations available at checkpoints.",
              "Strict proctoring against AI tools (ChatGPT, Copilot, etc.). Tampering leads to disqualification.",
              "Fastest accurate submission takes the podium."
            ],
            judging: "Aggregate score from Kahoot accuracy (30%), clue resolution speed (40%), and syntax bug spotting (30%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Trophies & Merit Certificates"
          }
        },

        // 2. ShadowCode (Technical Event)
        {
          id: "shadow-code",
          name: "SHADOWCODE",
          tagline: "Think Fast. Code Smart. Debug in the Dark",
          category: "Technical Event",
          group: "technical",
          prize: "₹15,000",
          venue: "SOIS Lab 01",
          date: "Day 1 (4 February 2027)",
          time: "11:00 AM – 01:00 PM",
          description: "Think Fast. Code Smart. Debug in the Dark. The ultimate blind programming challenge where developers write code with their monitors turned OFF.",
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
              "Round 1: Code Debugging Sprint (Fix faulty algorithmic scripts against strict clock).",
              "Round 2: Blind Coding (Screens turned OFF; write algorithms from memory).",
              "Round 3: Optic Code Golf (Solve the master problem in the minimum possible lines of code)."
            ],
            rules: [
              "Supported languages: C, C++, Java, Python 3.",
              "Monitors must remain completely powered off during Round 2 until time is called.",
              "Code that compiles and passes the maximum hidden test cases wins."
            ],
            judging: "Compilation success, test case coverage, execution time, and line count efficiency.",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Accredited Certificates"
          }
        },

        // 3. DesignNova (Technical Event)
        {
          id: "design-nova",
          name: "DESIGNNOVA",
          tagline: "Imagine the Experience. Design the Future",
          category: "Technical Event",
          group: "technical",
          prize: "₹15,000",
          venue: "Design Studio (Ground Floor)",
          date: "Day 1 (4 February 2027)",
          time: "02:00 PM – 04:30 PM",
          description: "Imagine the Experience. Design the Future. Fast-paced UI/UX design sprint, user journey mapping, and interactive prototyping tackling modern digital product challenges.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Vimal Raj",
            phone: "+91 96201 92249",
            photo: "images/coord-vimal.svg"
          },
          rulebook: {
            overview: "Participants receive an on-the-spot problem statement to craft an intuitive mobile/web product interface, user journey map, and clickable prototype.",
            eligibility: "Solo or teams of 2 members. Bring laptops with Figma / Adobe XD installed.",
            teamSize: "1 - 2 Participants",
            rounds: [
              "Phase 1: Briefing & UX Research (30 minutes user journey formulation).",
              "Phase 2: High-Fidelity Wireframing & Prototyping (2 hours Figma design sprint).",
              "Phase 3: Jury Presentation & Interactive Product Walkthrough."
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

        // 4. TechTalk (Technical Event)
        {
          id: "tech-talk",
          name: "TECHTALK",
          tagline: "Research Today. Transform Tomorrow",
          category: "Technical Event",
          group: "technical",
          prize: "₹10,000",
          venue: "Seminar Hall 1",
          date: "Day 1 (4 February 2027)",
          time: "04:30 PM – 06:00 PM",
          description: "Research Today. Transform Tomorrow. Academic and industrial tech symposium where student researchers present breakthrough papers, emerging tech analyses, and architectural solutions.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Ashlin Siddharth",
            phone: "+91 87976 86786",
            photo: "images/coord-ashlin.svg"
          },
          rulebook: {
            overview: "A prestigious keynote and research presentation arena celebrating innovative computing breakthroughs, artificial intelligence architectures, and cloud distributed paradigms.",
            eligibility: "Solo or teams of 2 members.",
            teamSize: "1 - 2 Participants",
            rounds: [
              "Round 1: Research Paper Abstract & Slide Deck Review.",
              "Round 2: Live 8-Minute Stage Presentation + 3-Minute Technical Jury Defence."
            ],
            rules: [
              "Original research or novel synthesis required. Plagiarism > 15% leads to disqualification.",
              "Presentation slides must be submitted in PDF format prior to session start.",
              "Jury decision on technical depth and clarity is conclusive."
            ],
            judging: "Technical Rigour (35%), Innovation (30%), Presentation Delivery (20%), Q&A Defence (15%).",
            cashPrize: "Winner: ₹5,500 | Runner-up: ₹3,000 | 2nd Runner-up: ₹1,500 + Certificates of Merit"
          }
        },

        // 5. DataChronicles (Technical Event)
        {
          id: "data-chronicles",
          name: "DATACHRONICLES",
          tagline: "Discover the Story. Decode the Data. Deliver the Insight.",
          category: "Technical Event",
          group: "technical",
          prize: "₹15,000",
          venue: "SOIS Lab 03",
          date: "Day 2 (5 February 2027)",
          time: "09:30 AM – 11:30 AM",
          description: "Discover the Story. Decode the Data. Deliver the Insight. End-to-end data pipeline championship: ingest complex raw datasets, perform machine learning modeling, and deliver compelling visual narratives.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Kaushal Kumar Singh",
            phone: "+91 91087 40761",
            photo: "images/coord-kaushal.svg"
          },
          rulebook: {
            overview: "End-to-end data intelligence challenge from exploratory data analysis (EDA) to predictive modeling and executive storytelling dashboards.",
            eligibility: "Teams of 2 participants. Must bring laptops configured with Python/R, Jupyter, and visualization tools.",
            teamSize: "2 Participants",
            rounds: [
              "Stage 1: Raw Dataset Release & Cleaning / Feature Engineering.",
              "Stage 2: Model Training & Predictive Performance Benchmarking.",
              "Stage 3: Interactive Dashboard Storytelling & Business Insight Pitch."
            ],
            rules: [
              "All code must be written during the competition window in a fresh repository.",
              "Pre-trained weights or external labels strictly forbidden.",
              "Submissions evaluated on hold-out validation dataset."
            ],
            judging: "Data Preprocessing (25%), Model Robustness (35%), Dashboard UI (20%), Storytelling Impact (20%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Merit Certificates"
          }
        },

        // 6. Founders' Arena (Technical Event)
        {
          id: "founders-arena",
          name: "FOUNDERS' ARENA",
          tagline: "Think Big. Pitch Bold. Build What's Next",
          category: "Technical Event",
          group: "technical",
          prize: "₹18,000",
          venue: "Seminar Hall 1",
          date: "Day 1 (4 February 2027)",
          time: "04:30 PM – 06:30 PM",
          description: "Think Big. Pitch Bold. Build What's Next. Shark Tank style startup pitching and tech venture showcase before venture evaluators, angel investors, and industry executives.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Vimal Raj",
            phone: "+91 96201 92249",
            photo: "images/coord-vimal.svg"
          },
          rulebook: {
            overview: "A business-meets-technology pitching battle where student founders showcase disruptive software/hardware startups, market research, revenue models, and MVP prototypes.",
            eligibility: "Teams of 2 to 4 members. Cross-college teams permitted.",
            teamSize: "2 - 4 Participants",
            rounds: [
              "Round 1: Pitch Deck & Executive Summary Pre-Screening.",
              "Round 2: Live 7-Minute Pitch + 5-Minute Investor Grilling on Dais."
            ],
            rules: [
              "Pitch deck must cover: Problem, Solution, Tech Architecture, Market Size, Revenue Model, and Team.",
              "Working software MVP or hardware demonstration carries significant bonus weightage.",
              "Judges' investment allocation determines final podium standings."
            ],
            judging: "Market Feasibility (30%), Technological Innovation (30%), Financial Viability (20%), Pitch Poise (20%).",
            cashPrize: "Winner: ₹10,000 | Runner-up: ₹5,000 | 2nd Runner-up: ₹3,000 + Incubation Fast-Track"
          }
        },

        // 7. TechNova '27 (Technical Event - 24H Hackathon)
        {
          id: "technova-27",
          name: "TECHNOVA '27",
          tagline: "24 Hours. One Mission. Limitless Innovation",
          category: "Technical Event",
          group: "technical",
          prize: "₹22,500",
          venue: "Central Computing Lab (24-Hour Facility)",
          date: "4–5 February 2027 (Overnight 24H)",
          time: "Day 1 10:30 AM Kickoff to Day 2 10:30 AM Submissions",
          description: "24 Hours. One Mission. Limitless Innovation. Presidency University's flagship overnight national hackathon solving high-impact problem statements with food, stay, and mentors provided.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Abhyas Kathuria",
            phone: "+91 85958 48421",
            photo: "images/coord-abhyas.svg"
          },
          rulebook: {
            overview: "A non-stop 24-hour innovation sprint bringing collegiate developers together to build production-grade web, mobile, blockchain, or AI solutions.",
            eligibility: "Teams of strictly 4 members. ₹1,500 registration per team includes meals, stay, and energy supplies.",
            teamSize: "Strictly 4 Members per team",
            rounds: [
              "Kickoff: Problem statement reveal at 10:30 AM Day 1.",
              "Checkpoint 1: Mentorship review at 04:00 PM Day 1.",
              "Checkpoint 2: Midnight code architecture audit at 12:00 AM.",
              "Final Demos: 10:30 AM – 01:00 PM Day 2 before industry jury panel."
            ],
            rules: [
              "All code must be written during the 24-hour window; fresh Git commit history strictly enforced.",
              "Open-source libraries permitted with proper attribution; no turnkey templates.",
              "Teams must observe common break rules (13:00–14:00 lunch clock pause)."
            ],
            judging: "Technical Innovation (35%), Product Completion (30%), UI/UX (20%), Pitch Demo (15%).",
            cashPrize: "Winner: ₹12,000 | Runner-up: ₹7,000 | Best Tech Prototype: ₹3,500 + Trophies & Medals"
          }
        },

        // 8. Quad Damage (Non-Technical Event)
        {
          id: "quad-damage",
          name: "QUAD DAMAGE",
          tagline: "Lock In. Level Up. Dominate",
          category: "Non-Technical Event",
          group: "non-technical",
          prize: "₹20,000",
          venue: "Classroom DJL01 & SH4 (SOIS Gaming Hub)",
          date: "Day 1 & Day 2 (4–5 February 2027)",
          time: "Day 1 02:00 PM Qualifiers | Day 2 01:00 PM Finals",
          description: "Lock In. Level Up. Dominate. High-octane collegiate LAN esports championship featuring Valorant (PC 5v5), BGMI (Mobile Squads), and Call of Duty with live big-screen casting.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Ashlin Siddharth",
            phone: "+91 87976 86786",
            photo: "images/coord-ashlin.svg"
          },
          rulebook: {
            overview: "Collegiate esports championship played across dedicated low-latency tournament LAN networks with official tournament referees.",
            eligibility: "Teams of 1 to 4 members. Must carry college IDs and personal mobile/peripherals.",
            teamSize: "1 - 4 Players per squad",
            rounds: [
              "Stage 1: Custom Room Knockout Qualifiers (Single Elimination).",
              "Stage 2: Semi-Finals & Grand Finals cast live on stage displays."
            ],
            rules: [
              "Strict anti-cheat policy. Any emulation, macros, or mods cause instant team disqualification.",
              "Campus high-speed LAN provided; players may also utilize personal hotspots.",
              "Unsportsmanlike conduct or toxicity leads to immediate forfeit."
            ],
            judging: "Official in-game tournament scoreboard verified by match referees.",
            cashPrize: "Valorant Champion: ₹8,000 | BGMI Champion: ₹7,000 | COD Champion: ₹5,000 + Trophies"
          }
        },

        // 9. Biochroma (Non-Technical Event)
        {
          id: "biochroma",
          name: "BIOCHROMA",
          tagline: "Where Nature Meets Innovation, Style Becomes the Future",
          category: "Non-Technical Event",
          group: "non-technical",
          prize: "₹15,000",
          venue: "Main Open Stage",
          date: "Day 2 (5 February 2027)",
          time: "03:30 PM – 05:00 PM",
          description: "Where Nature Meets Innovation, Style Becomes the Future. A flagship runway spectacle fusing avant-garde fashion, wearable electronics, smart LEDs, and organic sustainable materials.",
          poster: "images/events-poster.svg",
          coordinator: {
            name: "Vimal Raj",
            phone: "+91 96201 92249",
            photo: "images/coord-vimal.svg"
          },
          rulebook: {
            overview: "A themed fashion runway experience where futuristic cyber aesthetics blend with nature-inspired elements, smart textiles, microcontrollers, and recyclable tech fabrics.",
            eligibility: "Teams of 5 to 10 members (models, designers, and audio-visual support).",
            teamSize: "5 - 10 Members per team",
            rounds: [
              "Runway Round: 8-minute choreographed team walk with music and thematic narration.",
              "Concept Defence: 2-minute Q&A with fashion and tech judges explaining material sustainability."
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

        // 10. APL (Arenium Premier League) (Non-Technical Event)
        {
          id: "apl-auction",
          name: "APL (ARENIUM PREMIER LEAGUE)",
          tagline: "Bid Smart. Think Big. Build Your Business Empire",
          category: "Non-Technical Event",
          group: "non-technical",
          prize: "₹15,000",
          venue: "Management Amphitheatre",
          date: "Day 2 (5 February 2027)",
          time: "02:00 PM – 03:30 PM",
          description: "Bid Smart. Think Big. Build Your Business Empire. An IPL-style strategic corporate auction and business simulation where teams manage virtual capital, acquire brands, and deliver growth portfolios.",
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
              "Round 3: Final Valuation & Executive Board Pitch."
            ],
            rules: [
              "Each team starts with a fixed virtual purse of ₹100 Crores.",
              "Auctioneer rulings on bids, penalties, and lot allocation are final.",
              "Exceeding purse limits leads to immediate forfeiture of assets."
            ],
            judging: "Portfolio Market Valuation (40%), Strategic Synergy (30%), Crisis Handling (30%).",
            cashPrize: "Winner: ₹8,000 | Runner-up: ₹4,500 | 2nd Runner-up: ₹2,500 + Corporate Citations"
          }
        }
      ],"""

with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update storage key to v4
text = text.replace('STORAGE_KEY: "arenium_fest_db_v3"', 'STORAGE_KEY: "arenium_fest_db_v4"')

# 2. Update events array in getDefaults()
pat_events = re.compile(r'events:\s*\[[\s\S]*?\n\s*\],\s*winners:', re.MULTILINE)
text = pat_events.sub(events_code + '\n      winners:', text)

# 3. Update sample winners
old_winners = re.compile(r'winners:\s*\[[\s\S]*?\n\s*\],\s*certificates:', re.MULTILINE)
new_winners = """winners: [
        {
          id: "win-technova",
          event: "TECHNOVA '27 (24H HACKATHON)",
          category: "Technical Event",
          date: "5 February 2027",
          prizePool: "₹22,500",
          tiers: [
            { rank: 1, team: "Team NeuralForge", college: "Presidency University, Bengaluru", prize: "₹12,000", members: ["Aarav Sharma", "Neha Gupta", "Vikram Sen", "Pooja Hegde"] },
            { rank: 2, team: "CyberSentinels", college: "BMS College of Engineering", prize: "₹7,000", members: ["Rohan K", "Aditi Rao", "Karthik N", "Deepak V"] },
            { rank: 3, team: "ByteShift AI", college: "RV College of Engineering", prize: "₹3,500", members: ["Siddharth M", "Ananya P", "Varun T", "Meera S"] }
          ]
        },
        {
          id: "win-shadowcode",
          event: "SHADOWCODE",
          category: "Technical Event",
          date: "4 February 2027",
          prizePool: "₹15,000",
          tiers: [
            { rank: 1, team: "Kiran R (Solo)", college: "PES University, Bengaluru", prize: "₹8,000", members: ["Kiran R"] },
            { rank: 2, team: "Tanvi Deshmukh", college: "Presidency University, Bengaluru", prize: "₹4,500", members: ["Tanvi Deshmukh"] },
            { rank: 3, team: "Rahul Menon", college: "MSRIT Bengaluru", prize: "₹2,500", members: ["Rahul Menon"] }
          ]
        },
        {
          id: "win-techodyssey",
          event: "TECH ODYSSEY",
          category: "Technical Event",
          date: "4 February 2027",
          prizePool: "₹15,000",
          tiers: [
            { rank: 1, team: "CipherKnights", college: "Presidency University, Bengaluru", prize: "₹8,000", members: ["Gautam V", "Shreya Sen", "Akash Nair"] },
            { rank: 2, team: "HexHunters", college: "Dayananda Sagar College", prize: "₹4,500", members: ["Manish B", "Kavya S"] },
            { rank: 3, team: "RootAccess", college: "New Horizon College", prize: "₹2,500", members: ["Naveen K", "Priya D"] }
          ]
        },
        {
          id: "win-quaddamage",
          event: "QUAD DAMAGE",
          category: "Non-Technical Event",
          date: "5 February 2027",
          prizePool: "₹20,000",
          tiers: [
            { rank: 1, team: "Phantom Apex", college: "Presidency University, Bengaluru", prize: "₹8,000", members: ["Aditya Joshi", "Tarun G", "Sanjay R", "Sameer K"] },
            { rank: 2, team: "Viper Squad", college: "Christ University, Bengaluru", prize: "₹7,000", members: ["Pranav M", "Aayush C", "Nikhil T", "Dev B"] },
            { rank: 3, team: "RedLine Esports", college: "Jain University", prize: "₹5,000", members: ["Kunal S", "Rishi P"] }
          ]
        },
        {
          id: "win-designnova",
          event: "DESIGNNOVA",
          category: "Technical Event",
          date: "4 February 2027",
          prizePool: "₹15,000",
          tiers: [
            { rank: 1, team: "PixelCraft Duo", college: "National Institute of Design / PU", prize: "₹8,000", members: ["Diya Roy", "Abhinav C"] },
            { rank: 2, team: "VectorPulse", college: "Presidency University, Bengaluru", prize: "₹4,500", members: ["Sneha M", "Karan J"] },
            { rank: 3, team: "AuraStudio", college: "BMSCE Bengaluru", prize: "₹2,500", members: ["Harish V"] }
          ]
        },
        {
          id: "win-biochroma",
          event: "BIOCHROMA",
          category: "Non-Technical Event",
          date: "5 February 2027",
          prizePool: "₹15,000",
          tiers: [
            { rank: 1, team: "Atelier Synthesis", college: "Presidency University (SOIS & SOD)", prize: "₹8,000", members: ["Rhea Kapoor & Team"] },
            { rank: 2, team: "NeonFlora Runway", college: "Mount Carmel College", prize: "₹4,500", members: ["Zoya Sheikh & Team"] },
            { rank: 3, team: "EcoTech Collective", college: "Presidency University", prize: "₹2,500", members: ["Alok N & Team"] }
          ]
        },
        {
          id: "win-apl",
          event: "APL (ARENIUM PREMIER LEAGUE)",
          category: "Non-Technical Event",
          date: "5 February 2027",
          prizePool: "₹15,000",
          tiers: [
            { rank: 1, team: "Titan Conglomerate", college: "Presidency University, Bengaluru", prize: "₹8,000", members: ["Naman Singhal", "Ritika Jain"] },
            { rank: 2, team: "Apex Ventures", college: "St. Joseph's College of Commerce", prize: "₹4,500", members: ["Aryan Khurana", "Devika S"] },
            { rank: 3, team: "Monopoly Masters", college: "Christ University", prize: "₹2,500", members: ["Rajesh V", "Preeti K"] }
          ]
        }
      ],\n      certificates:"""
text = old_winners.sub(new_winners, text)

# 4. Update sample certificates to match new event names
old_certs = re.compile(r'certificates:\s*\[[\s\S]*?\n\s*\],\s*sponsors:', re.MULTILINE)
new_certs = """certificates: [
        {
          id: "AR27-HCK-001",
          recipient: "Team NeuralForge",
          event: "TECHNOVA '27",
          award: "CHAMPION // FIRST PLACE",
          college: "Presidency University, Bengaluru",
          issueDate: "5 February 2027",
          verified: true
        },
        {
          id: "AR27-HCK-002",
          recipient: "CyberSentinels",
          event: "TECHNOVA '27",
          award: "RUNNER UP // SECOND PLACE",
          college: "BMS College of Engineering",
          issueDate: "5 February 2027",
          verified: true
        },
        {
          id: "AR27-COD-001",
          recipient: "Kiran R",
          event: "SHADOWCODE",
          award: "CHAMPION // FIRST PLACE",
          college: "PES University, Bengaluru",
          issueDate: "5 February 2027",
          verified: true
        },
        {
          id: "AR27-TRL-001",
          recipient: "CipherKnights",
          event: "TECH ODYSSEY",
          award: "CHAMPION // FIRST PLACE",
          college: "Presidency University, Bengaluru",
          issueDate: "5 February 2027",
          verified: true
        },
        {
          id: "AR27-LAN-001",
          recipient: "Phantom Apex",
          event: "QUAD DAMAGE",
          award: "CHAMPION // FIRST PLACE",
          college: "Presidency University, Bengaluru",
          issueDate: "5 February 2027",
          verified: true
        },
        {
          id: "AR27-DSN-001",
          recipient: "PixelCraft Duo",
          event: "DESIGNNOVA",
          award: "CHAMPION // FIRST PLACE",
          college: "National Institute of Design / PU",
          issueDate: "5 February 2027",
          verified: true
        },
        {
          id: "AR27-FSH-001",
          recipient: "Atelier Synthesis",
          event: "BIOCHROMA",
          award: "CHAMPION // FIRST PLACE",
          college: "Presidency University (SOIS)",
          issueDate: "5 February 2027",
          verified: true
        },
        {
          id: "AR27-APL-001",
          recipient: "Titan Conglomerate",
          event: "APL (ARENIUM PREMIER LEAGUE)",
          award: "CHAMPION // FIRST PLACE",
          college: "Presidency University, Bengaluru",
          issueDate: "5 February 2027",
          verified: true
        },
        {
          id: "AR27-PRT-042",
          recipient: "Kaushal Kumar Singh",
          event: "TECHNOVA '27",
          award: "CERTIFICATE OF MERIT & PARTICIPATION",
          college: "Presidency University, Bengaluru",
          issueDate: "5 February 2027",
          verified: true
        }
      ],\n      sponsors:"""
text = old_certs.sub(new_certs, text)

# 5. Update timeline in FestDB
old_schedule = re.compile(r'schedule:\s*\[[\s\S]*?\n\s*\],\s*leadership:', re.MULTILINE)
new_schedule = """schedule: [
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "09:30 AM - 10:30 AM",
          title: "GRAND INAUGURAL CEREMONY & KEYNOTE",
          venue: "AUD (Main Auditorium)",
          category: "Official Ceremony",
          desc: "Grand lamp lighting, presidential keynote address by Dean Dr. C. Kalaiarasan and HOD Dr. K. G. Mohan, and formal opening of Arenium'27."
        },
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "10:30 AM (24 Hours)",
          title: "TECHNOVA '27 (24-HOUR HACKATHON) FLAGOFF",
          venue: "Central Computing Lab (24-Hour Facility)",
          category: "Technical Event",
          desc: "Release of official Smart India Hackathon & industry challenge problem statements. 24 hours of non-stop algorithmic sprint begins."
        },
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "10:45 AM - 01:00 PM",
          title: "TECH ODYSSEY (FOLLOW THE CLUES. CRACK THE CODE)",
          venue: "SOIS Block & Central Campus",
          category: "Technical Event",
          desc: "High-energy technical treasure hunt featuring Kahoot qualifiers, metadata clue quests in file properties, and rapid code bug detection."
        },
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "11:00 AM - 01:00 PM",
          title: "SHADOWCODE (THINK FAST. DEBUG IN THE DARK)",
          venue: "SOIS Lab 01",
          category: "Technical Event",
          desc: "Fast-paced blind programming battle with computer monitors turned completely OFF. Pure memory, syntax mastery, and algorithmic speed."
        },
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "01:00 PM - 02:00 PM",
          title: "OFFICIAL LUNCH & RECHARGE WINDOW",
          venue: "University Cafeteria & Food Concourse",
          category: "Pause",
          desc: "Scheduled festival pause across all tracks. Participants, jury, and hackathon teams recharge."
        },
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "02:00 PM - 05:30 PM",
          title: "QUAD DAMAGE (LOCK IN. LEVEL UP. DOMINATE)",
          venue: "Classroom DJL01 & SH4 (Gaming Hub)",
          category: "Non-Technical Event",
          desc: "High-octane collegiate LAN esports championship qualifiers featuring Valorant (5v5 PC), BGMI Squads, and Call of Duty."
        },
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "02:00 PM - 04:30 PM",
          title: "DESIGNNOVA (IMAGINE THE EXPERIENCE. DESIGN THE FUTURE)",
          venue: "Design Studio (Ground Floor)",
          category: "Technical Event",
          desc: "UI/UX design sprint and interactive product pitch. Rapid wireframing and high-fidelity Figma prototypes solving real user problems."
        },
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "04:30 PM - 06:00 PM",
          title: "TECHTALK (RESEARCH TODAY. TRANSFORM TOMORROW)",
          venue: "Seminar Hall 1",
          category: "Technical Event",
          desc: "Student research paper presentations and industrial emerging tech keynote symposium before academic jury evaluators."
        },
        {
          day: "Day 1",
          date: "4 Feb 2027",
          time: "04:30 PM - 06:30 PM",
          title: "FOUNDERS' ARENA (THINK BIG. PITCH BOLD)",
          venue: "Seminar Hall 1",
          category: "Technical Event",
          desc: "Shark Tank style venture pitch deck and startup showcase before corporate investors and innovation evaluators."
        },
        {
          day: "Day 2",
          date: "5 Feb 2027",
          time: "09:30 AM - 11:30 AM",
          title: "DATACHRONICLES (DISCOVER THE STORY. DECODE THE DATA)",
          venue: "SOIS Lab 03",
          category: "Technical Event",
          desc: "End-to-end data pipeline championship: dataset ingestion, predictive modeling, machine learning benchmarks, and executive visual storytelling."
        },
        {
          day: "Day 2",
          date: "5 Feb 2027",
          time: "10:30 AM",
          title: "TECHNOVA '27 HACKATHON CODE FREEZE & DEMOS",
          venue: "Central Computing Lab",
          category: "Technical Event",
          desc: "24-hour non-stop hackathon timer expires. Code repositories frozen for comprehensive jury walkthroughs."
        },
        {
          day: "Day 2",
          date: "5 Feb 2027",
          time: "01:00 PM - 02:00 PM",
          title: "OFFICIAL LUNCH PAUSE",
          venue: "Food Concourse",
          category: "Pause",
          desc: "Afternoon recharge pause prior to the grand stage finals and runway spectacle."
        },
        {
          day: "Day 2",
          date: "5 Feb 2027",
          time: "02:00 PM - 03:30 PM",
          title: "APL (ARENIUM PREMIER LEAGUE) - BRAND AUCTION",
          venue: "Management Amphitheatre",
          category: "Non-Technical Event",
          desc: "IPL-style corporate brand bidding war. Teams manage virtual ₹100 Crore purses, acquire conglomerates, and navigate business disruptions."
        },
        {
          day: "Day 2",
          date: "5 Feb 2027",
          time: "03:30 PM - 05:00 PM",
          title: "BIOCHROMA (WHERE NATURE MEETS INNOVATION)",
          venue: "Main Open Stage",
          category: "Non-Technical Event",
          desc: "Grand themed fashion runway fusing wearable smart tech, LED microcontrollers, fiber optics, and sustainable eco-fabrics."
        },
        {
          day: "Day 2",
          date: "5 Feb 2027",
          time: "05:00 PM - 06:30 PM",
          title: "GRAND VALEDICTORY & ₹1.5L PRIZE DISTRIBUTION",
          venue: "AUD (Main Auditorium)",
          category: "Award Ceremony",
          desc: "Official announcement of champion podiums, trophy distribution, presentation of ₹1,50,000 cash prizes, and closing address."
        }
      ],\n      leadership:"""
text = old_schedule.sub(new_schedule, text)

# 6. Update Hero Canvas Particle Colors to Auburn Crimson (#A52A2A) & Rosewood (#6C403E)
text = text.replace('color: Math.random() > 0.4 ? "rgba(0, 240, 255, " : "rgba(255, 0, 85, "', 'color: Math.random() > 0.4 ? "rgba(165, 42, 42, " : "rgba(108, 64, 62, "')
text = text.replace('ctx.strokeStyle = "rgba(0, 240, 255, 0.04)";', 'ctx.strokeStyle = "rgba(165, 42, 42, 0.06)";')
text = text.replace('ctx.strokeStyle = `rgba(0, 240, 255, ${0.15 * (1 - dist / 85)})`;', 'ctx.strokeStyle = `rgba(165, 42, 42, ${0.25 * (1 - dist / 85)})`;')

# 7. Update Certificate Canvas Generator colors
text = text.replace('ctx.fillStyle = "#00f0ff";', 'ctx.fillStyle = "#A52A2A";')
text = text.replace('ctx.strokeStyle = "rgba(0, 240, 255, 0.8)";', 'ctx.strokeStyle = "#A52A2A";')
text = text.replace('ctx.fillStyle = "rgba(0, 240, 255, 0.03)";', 'ctx.fillStyle = "rgba(165, 42, 42, 0.04)";')
text = text.replace('ctx.strokeStyle = "rgba(0, 240, 255, 0.2)";', 'ctx.strokeStyle = "rgba(108, 64, 62, 0.3)";')

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated js/main.js with Auburn #A52A2A & Rosewood #6C403E theme and 10 official events!")
