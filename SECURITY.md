# Security Policy

## Supported Versions

This repository publishes a public evidence package for the Sovereign Runtime.

Supported public versions are defined through repository tags and release notes.

Security guidance applies to:
- the current public release
- any actively maintained public evidence package versions

Older versions may be archived and may not receive updates or security review.

---

## Reporting a Vulnerability

If you believe you have discovered a security vulnerability in this repository, please report it privately and do not open a public issue.

### Preferred reporting channels:

- GitHub Security Advisory (if enabled for this repository)
- Private email: kaiven2342025@proton.me

---

## What to include

Please include as much detail as possible:

- Clear description of the issue
- Affected dataset, harness, or artifact
- Steps to reproduce the issue
- Relevant logs, traces, or proof-of-concept material
- Expected vs observed behavior
- Assessment of potential impact

---

## Responsible Disclosure

To protect users, maintainers, and the integrity of evaluation artifacts, we request that you:

- Do not disclose vulnerabilities publicly before review and remediation
- Do not exploit the issue beyond what is required for demonstration
- Do not share exploit details with third parties prior to coordination
- Allow reasonable time for investigation and remediation

---

## Response Expectations

Upon receiving a valid report, we aim to:

- Acknowledge receipt in a timely manner
- Assess severity and scope of the issue
- Investigate affected datasets, harnesses, or result artifacts
- Reproduce and validate the reported issue
- Develop and validate a fix if required
- Coordinate disclosure after remediation is complete

---

## Scope

This policy applies only to the public evidence package, including:

- evaluation datasets
- chaos testing suites
- runtime execution traces
- live API evaluation results
- harness scripts and reproducibility tools
- metadata and integrity manifests
- documentation files

---

## Out of Scope

The following are explicitly outside the security boundary:

- private sovereign runtime core
- internal orchestration logic
- agent coordination mechanisms
- proprietary runtime behavior
- deployment infrastructure
- non-public experimental systems
- NDA-restricted components

---

## Live API & External Dependency Note

This repository includes evaluation artifacts that may interact with external services under controlled testing conditions.

Any external dependency behavior observed in this repository:

- is part of synthetic evaluation workflows
- is not a live production integration contract
- does not guarantee stability, availability, or security of external systems

---

## Safe Reporting Note

If your report involves adversarial payloads, exploit simulations, or sensitive test cases, please provide only the minimum necessary information required for validation and keep disclosure private until the issue is resolved.

---

## Thank You

We appreciate responsible security research and structured reporting that helps improve the integrity, reproducibility, and resilience of this evaluation framework.
