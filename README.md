# NovaMedX — Governed Medical AI for EMS Risk Extraction **Med‑Gemma + NovaDNA / FuseID** *(Executable Reference Implementation · Kaggle MedGemma Impact Challenge Submission)*

**Subtitle**

A cyber‑safe EMS risk‑extraction system that produces identity‑bound, auditable clinical artifacts under real‑world constraints.

**Overview**

NovaMedX is a governed medical AI system built on Med‑Gemma for emergency medical services (EMS). It transforms unstructured EMS handoff transcripts into structured, machine‑verifiable clinical risk artifacts designed for real‑world emergency workflows.

This repository contains an Executable Reference Implementation (ERI) of a single, bounded EMS micro‑task. The scope is intentionally constrained to ensure clarity, reproducibility, and auditability.

Rather than expanding model autonomy, NovaMedX constrains execution.

Med‑Gemma proposes candidate clinical signals; governance determines whether those signals are safe to release.

**What This ERI Demonstrates**

This Executable Reference Implementation shows one governed execution path:

Structured clinical risk extraction from EMS handoff transcripts

The system:

- Extracts predefined clinical risk indicators
(e.g., airway compromise, sepsis risk, cardiovascular instability)
- Emits a strict, schema‑validated Risk Assessment Artifact
- Or intentionally refuses output when safety conditions are not met

The system does not diagnose, recommend treatment, or operate as a conversational agent.

**Core Principles**

1. Bounded Model Use (Med‑Gemma)
Med‑Gemma is used strictly as a clinical signal extractor.
Its outputs are treated as candidate hypotheses, not final answers.

2. Governed Execution
All Med‑Gemma outputs pass through a governance layer that enforces:

- task scope constraints
- uncertainty thresholds (3‑Sigma coherence)
- integrity and admissibility checks

If conditions are satisfied, output is released.
If not, the system constrains or refuses output.

Refusal is an intentional, logged safety outcome.

3. Identity‑Bound Provenance (NovaDNA / FuseID)
Each execution is bound locally using NovaDNA / FuseID, which cryptographically fuses:

- requesting medic identity (synthetic)
- input transcript
- governance decision
- model provenance
- final outcome (artifact or refusal)

This produces a verifiable execution record suitable for audit without re‑execution.

**Governed Execution Flow**

EMS Transcript + Medic Identity
↓
Input & Identity Verification
↓
Med‑Gemma Signal Extraction
↓
Governance Evaluation
↓
NovaDNA / FuseID Binding
↓
┌────────────────┬────────────────┐
│ Released │ Refused │
│ Risk Artifact │ (Logged Safety) │
└────────────────┴────────────────┘

**Safety & Failure Handling**

NovaMedX is designed to fail safely:

✅ Valid context + sufficient confidence
→ Risk Assessment Artifact released with audit record
⚠️ Rising uncertainty
→ Output constrained or clarification required
⛔ Integrity or safety violation
→ Output refused with audit record

In regulated clinical environments, refusal is a required behavior.

**Execution Characteristics**

- Deterministic: identical inputs produce identical artifacts and hashes
- Offline‑capable: no external network access required
- CPU‑only: suitable for edge and tablet‑class hardware
- Schema‑validated: outputs are machine‑verifiable, not free text

All inputs used in this ERI are synthetic or de‑identified.

## Quick Start

```bash
docker run novamedx:medgemma-eri
```

Running the Executable Reference Implementation produces:

- A valid EMS handoff → released Risk Assessment Artifact
- A high-uncertainty or integrity-violating input → intentional refusal with audit record

All inputs are synthetic. No network access is required.

**Impact**

This ERI demonstrates that clinical AI viability depends on governance embedded inside the execution path, not applied after generation.

It shows how Med‑Gemma can be deployed responsibly in EMS workflows, producing durable, identity‑bound clinical artifacts rather than ephemeral text — under realistic operational constraints.

**Links

Required Video (≤ 3 min):
`https://www.youtube.com/watch?v=ChY1IBMrSxA`

Public Code Repository:
`https://github.com/Dartan1983/medgemma-eri/releases/tag/v1.0.0-medgemma-eri`

**Closing**

Intelligence proposes.
Governance decides.
Med‑Gemma provides the signal.
NovaMedX determines whether it is safe to release.

**Final Confirmation**

This README:

✔️ Is suitable as the Kaggle submission write‑up
✔️ Doubles cleanly as the repository README
✔️ Avoids “demo,” “prototype,” or “POC” language
✔️ Matches the scope you intentionally chose
✔️ Reads as serious, executable, and governed
