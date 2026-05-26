# Reproducibility Specification — Sovereign Runtime Public Evidence Package v0.2

## 1. Purpose

This document defines the reproducibility model for the Sovereign Runtime Public Evidence Package.

The objective is to enable independent verification of published evaluation results using deterministic tooling, structured datasets, and integrity-verified execution traces.

This repository does not require reproduction of internal runtime logic. Only observable outputs and validation artifacts are in scope.

---

## 2. Reproducibility Scope

Reproducibility applies to:

- dataset integrity verification
- evaluation harness execution
- result trace validation
- cryptographic hash verification
- structured output validation
- summary generation consistency

Reproducibility does not apply to:

- internal orchestration logic
- agent implementation details
- runtime memory systems
- hidden execution policies
- proprietary runtime behavior

---

## 3. Required Environment

Reproducibility assumes a standard execution environment:

- Python 3.9+
- standard JSON / CSV parsing libraries
- file system access to repository artifacts
- no external runtime dependencies required for validation scripts

No GPU, distributed infrastructure, or specialized hardware is required.

---

## 4. Artifact Integrity Model

All published artifacts are validated through integrity mechanisms including:

- SHA256 hashes (embedded in result logs or metadata files)
- timestamped execution records
- append-only JSONL trace logs
- dataset manifests

Integrity verification ensures that:

- datasets have not been modified post-publication
- execution traces correspond to recorded runs
- results match recorded evaluation outputs

---

## 5. Reproducibility Procedure

To reproduce evaluation validation locally:

### Step 1 — Verify dataset integrity

```bash
python scripts/verify_hashes.py
