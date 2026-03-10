# PRAVAAH C4I

**A dual-use AI governance framework for national security and humanitarian management.**

**Live:** [pravaah-c4i.vercel.app](https://pravaah-c4i.vercel.app)

---

## What This Is

PRAVAAH C4I is a research-grade reference architecture exploring what accountable, auditable AI governance would require where national security mandates and humanitarian obligations meet — specifically in the context of India's policy vacuum around refugee and displacement management.

The core argument: AI systems operating at the intersection of security and humanitarian protection require governance architectures that don't yet exist in policy. This is what one would look like.

It is **not** a live system, **not** connected to classified data, and **not** an official deployment. All operational data is illustrative. The architecture demonstrates governance mechanisms — restraint indexing, fairness auditing, humanitarian safeguards, conflict resolution protocols, and legal accountability chains — as a reference for how such systems could and should be governed.

Built entirely through AI-assisted development. Domain knowledge and governance instincts, not traditional coding, are the core competencies this project represents.

---

## The Problem

India has porous borders, active security imperatives, complex regional displacement dynamics, and no formal refugee legislation. AI systems are increasingly deployed in border management contexts globally — but the governance frameworks that should constrain them are absent, especially in legal vacuums like India's.

PRAVAAH C4I asks: if such a system were deployed, what would accountability require? What mechanisms would hold security and humanitarian mandates in genuine tension rather than collapsing one into the other?

---

## Core Innovations

### 1. AI Restraint Index
A transparent composite score across four governance dimensions — civilian harm potential (0.40), uncertainty (0.25), legal exposure (0.20), and bias risk (0.15). When the index exceeds **0.60**, the system enters advisory-only posture: no autonomous action, no auto-escalation, all outputs flagged for human review. Formula and weights are visible and auditable — the scoring methodology is an expandable panel, not a black box. Civilian harm is weighted as lexically prior and cannot be traded off against improved confidence scores.

### 2. Joint Review Mode
When the security stream and humanitarian stream reach conflicting classifications for the same movement event — one flagging infiltrators, the other identifying displaced civilians — the conflict triggers mandatory Joint Review. Neither stream's recommendation can proceed without Governance Officer review and documented rationale. The conflict is logged as a governance exception and included in the Legal Bundle. This is the core governance contribution: making stream conflict visible, mandatory, and auditable rather than resolved silently by the AI.

### 3. Dynamic Rules of Engagement
A status indicator that shifts system behaviour based on operational context: Standard Monitoring, Active Crisis, or Humanitarian Emergency. In Humanitarian Emergency mode, the restraint threshold tightens, enforcement actions are suspended pending humanitarian assessment, and non-harmful default posture activates. The ROE state is a configurable governance parameter — any change is logged.

### 4. Fairness-Humanitarian Conflict Resolution
When demographic parity optimisation conflicts with an active protection mandate, the protection mandate takes precedence. This is explicit, not assumed. Demographic parity is a statistical property of model outputs. Non-refoulement is a legal obligation with individual, irreversible consequences. They are not equivalent constraints, and the architecture treats them accordingly. Conflicts are logged as governance exceptions.

### 5. Legal Bundle Generator
Every incident generates a cryptographically sealed, court-ready evidence package: sensor snapshots, model versions and parameter states, complete human decision chains with hashed role IDs, alternatives considered, and active policy context. Designed to function as prima facie evidence for courts, oversight bodies, and independent auditors.

### 6. Humanitarian Parallel Channel
A structurally independent advisory stream operating under a separate mandate and reporting line. Its outputs are not filtered by the security chain of command before reaching the AI Governance Officer. Independence is architectural — it cannot be suppressed by operational pressure.

### 7. Demographic Fairness Auditing
Real-time parity tracking across nationality and demographic groups. Bias flags with root cause analysis. Geographic fairness correction coefficients applied at model layer. Group C parity gap (0.81, below 0.85 threshold) is flagged with intervention logged and retraining scheduled — the correction mechanism and its rationale are both visible.

### 8. Role-Based Human Action Logs
Pseudonymised hashed role IDs (e.g. H-9f3a) preserve individual privacy while maintaining complete, reconstructible accountability chains. Human oversight is not a checkbox — it is a timestamped, role-attributed, rationale-documented record.

---

## Dashboard Tabs

| Tab | Contents |
|-----|----------|
| **Operations** | Governance-Constrained Actions, ROE Status, Live Anomaly Strip, Commander's Status Board, Incident Queue with Joint Review trigger |
| **Oversight & Audit** | Fairness Index, Demographic Parity Breakdown, Root Cause Analysis, Audit PDF/JSON Export |
| **Climate Intel** | Seasonal Risk Timeline, 90-Day Forecast, Sensor Degradation Windows, Monsoon Restraint Posture |
| **Humanitarian** | Displacement Early Warning, Cox's Bazar Surge Alert, Dual-Use Framework, Parallel Channel, Fairness-Humanitarian Conflict Resolution Principle |
| **AI Governance** | Restraint Index with Scoring Methodology, Decision Context, Human Action Log, Legal Bundle Generator, Risk Register, Live Detection Panel |
| **About** | Architecture explanation, governance frameworks, design principles |
| **Joint Review** | Activated on stream conflict — shows security vs. humanitarian assessments, conflict resolution principle, Governance Officer action log |

---

## Governance Frameworks Applied

- EU AI Act — High-Risk System Provisions (Annex III, Article 14 Human Oversight)
- Digital Personal Data Protection Act 2023 (India)
- UN Guiding Principles on Business and Human Rights — Pillar II
- UNHCR Data Protection Standards & Digital SORA Framework
- International Humanitarian Law — Distinction Principle
- 1951 Refugee Convention — Non-Refoulement
- NITI Aayog Responsible AI Framework
- NIST AI Risk Management Framework

---

## Architecture

**Frontend:** Single-file HTML/CSS/JavaScript. No dependencies, no build process, no external APIs. Fully self-contained. Deployable to any static host.

**Detection logic:** Client-side multimodal sensor fusion simulation. Satellite, thermal, and acoustic inputs feed a weighted anomaly score with live fairness parity calculation and restraint state output.

**Deployment:** GitHub → Vercel (automatic on push to `main`).

```bash
git clone https://github.com/OpalSonoma/border-security-dashboard.git
cd border-security-dashboard
# Open index.html in any modern browser — no server required
```

---

## Why India

India's conditions make this architecture both necessary and adoptable at scale:

- **Policy vacuum** — no formal refugee legislation means AI systems operating in this space face no governance guardrails. This architecture proposes what those guardrails should look like.
- **Active judiciary** — higher courts already engage with digital forensics and constitutional rights. Cryptographic audit trails are familiar evidentiary objects.
- **RTI culture** — public sector transparency norms make logging and documentation expectations high.
- **DPDP enforcement** — the Ministry of Data Protection will require fairness audits, consent trails, and demonstrable safeguards. This architecture provides them.

---

## License

MIT License — See LICENSE file for details.

---

*Reference architecture. All operational data is illustrative and does not represent real intelligence, real incidents, or real individuals. Last updated: March 2026.*
