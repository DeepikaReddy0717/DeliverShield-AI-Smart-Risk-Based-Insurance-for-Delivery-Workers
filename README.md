## Inspiration

Delivery workers face unpredictable risks due to extreme weather and pollution. Traditional insurance does not adapt to real-time conditions. This inspired us to build **DeliverShield AI**, a smarter and dynamic insurance system that protects gig workers based on real-world risks.

---

## What it does

**DeliverShield AI** analyzes:
- Temperature 🌡
- Weather 🌧
- Air Quality 🌫

It calculates a **risk score** and classifies workers into:
- Low Risk
- Medium Risk
- High Risk

This helps enable **dynamic insurance decisions** based on real-time environmental conditions.

---

## How we built it

We used:

- **Django** for backend
- **SQLite** for database
- **HTML, CSS, Bootstrap** for UI
- **OpenWeatherMap API** for real-time weather and pollution data

Example logic:

**Risk = Heat + Rain + Pollution**

---

## Challenges we ran into

- API integration issues and invalid key errors
- Handling real-time data inconsistencies
- Designing a clean and intuitive dashboard UI
- Mapping environmental data into meaningful risk scores

---

## Accomplishments that we're proud of

- Built a working end-to-end prototype
- Integrated live environmental APIs
- Designed a clean SaaS-style dashboard
- Implemented a dynamic risk calculation system
- Created a solution addressing real-world gig worker safety

---

## What we learned

- Working with real-time APIs and error handling
- Full-stack development using Django
- Designing user-friendly UI/UX
- Translating real-world problems into technical solutions

---

## What's next for DeliverShield AI

- AI/ML-based predictive risk modeling
- Real-time alerts for high-risk conditions
- Fraud detection and anti-spoofing mechanisms
- Multi-city and large-scale deployment
- Integration with insurance claim systems

---

## Adversarial Defense & Anti-Spoofing Strategy

To handle fraud scenarios like GPS spoofing and coordinated fake claims, DeliverShield AI uses multiple validation layers:

### Multi-Source Validation
- Cross-check GPS with IP and network patterns
- Detect unrealistic location jumps

### Environmental Verification
- Match claims with real-time weather and AQI data
- Reject mismatched environmental claims

### Behavioral Analysis
- Identify repeated claims from same users/devices
- Detect unusual claim frequency

### Fraud Ring Detection
- Detect clusters of claims from same region
- Identify synchronized claim timing patterns

### Trust Scoring
- Assign trust scores based on claim history
- Flag suspicious users for further verification

### Fairness Mechanism
- Flag suspicious claims instead of rejecting instantly
- Ensure genuine workers are not penalized

---

## Impact

DeliverShield AI enables a **fair, data-driven insurance system** that:
- Protects delivery workers in risky conditions
- Reduces fraudulent claims
- Helps insurance providers make smarter decisions

This creates a safer and more reliable ecosystem for gig workers.
