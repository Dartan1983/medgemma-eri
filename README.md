# NovaMedX — Executable Reference Implementation (ERI)
Med‑Gemma + NovaDNA / FuseID

A governed EMS risk‑extraction system producing identity‑bound, auditable clinical artifacts under real‑world constraints.

---

## Quick Start (Fast Path)

```bash
docker run novamedx:medgemma-eri
````

Running the Executable Reference Implementation produces **two deterministic outcomes**:

*   ✅ A valid EMS handoff → released Risk Assessment artifact
*   ⛔ A high‑uncertainty or integrity‑violating input → intentional refusal with audit record

All inputs are synthetic.  
No network access is required.

***

## Reproducible Build (Exact Submission Version)

To reproduce the **exact version evaluated by judges**, use the tagged release:

*   **Tag:** `v1.0.0-medgemma-eri`
*   **Commit:** `a38117f`

```bash
git clone https://github.com/Dartan1983/medgemma-eri
cd medgemma-eri
git checkout tags/v1.0.0-medgemma-eri

docker build -t novamedx:medgemma-eri .
docker run --rm novamedx:medgemma-eri
```

This guarantees deterministic behavior identical to the competition submission.

***

## What This Repository Is

This repository contains an **Executable Reference Implementation (ERI)** of NovaMedX.

The ERI demonstrates a **single, bounded clinical micro‑task**:
extracting predefined risk signals from EMS handoff transcripts and releasing them **only** when identity, scope, and uncertainty constraints are satisfied.

The implementation is intentionally constrained for:

*   clarity
*   auditability
*   reproducibility

***

## Core Execution Model

*   **Bounded Model Use (Med‑Gemma)**  
    Med‑Gemma is used strictly to propose candidate clinical signals.

*   **Governed Execution**  
    All outputs pass through a runtime governance layer enforcing task scope, uncertainty thresholds (3‑Sigma coherence), and integrity checks.

*   **Identity‑Bound Provenance (NovaDNA / FuseID)**  
    Each execution cryptographically binds identity, input, governance decision, model provenance, and outcome into a verifiable record.

Refusal under uncertainty is an intentional, logged safety outcome.

***

## Expected Outputs

Structured artifacts are written to `outputs/`:

*   `released.json` — schema‑validated risk assessment with identity‑bound provenance
*   `refused.json` — logged safety refusal with audit metadata

Outputs are deterministic for identical inputs.

***

## Out of Scope (By Design)

This ERI does **not**:

*   diagnose or recommend treatment
*   operate autonomously
*   require internet access
*   represent the full NovaMedX platform

It is a **reference execution** intended to demonstrate governed behavior under controlled conditions.

***

## Documentation

The authoritative project narrative, evaluation context, threat model, and FAQ are maintained on the GitHub Release page:

<https://github.com/Dartan1983/medgemma-eri/releases/tag/v1.0.0-medgemma-eri>

***

## License

Licensed under the **Apache License 2.0**.  
See LICENSE.

***
