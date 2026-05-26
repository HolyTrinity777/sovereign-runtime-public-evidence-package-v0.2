# Boundary Statement

## Purpose

This document defines the boundary between public and private components of the Sovereign Runtime public evidence package. The repository is designed to support independent review, reproducibility, and behavioral verification without exposing internal orchestration systems or proprietary runtime mechanisms.

## Public scope

The following components are public and included in this repository:

- High-level 7-agent architecture model and role definitions
- Public evaluation methodology and test categories
- Dataset files and dataset manifests
- Execution results and trace logs
- Aggregate summaries and evaluation outputs
- Integrity artifacts (hashes, timestamps, manifests)
- Reproducibility scripts and verification tooling
- Optional minimal observable runtime shell behavior (if included)

## Private scope

The following components are intentionally excluded:

- Internal 7-agent orchestration engine and control flow
- Policy arbitration and decision-resolution logic
- Internal scoring, weighting, or ranking systems
- Recovery, memory, and checkpoint implementation details
- Private defensive mechanisms and adversarial handling internals
- Attack payload construction logic and exploit generation systems
- Runtime secrets, credentials, or environment-specific configurations

## Reason for boundary

The boundary exists to separate observable system behavior from implementation-level mechanisms. The public package demonstrates how the system behaves under stress, not how those behaviors are internally implemented.

This enables:
- independent verification of results
- reproducible evaluation of behavior
- protection of proprietary system design

## Public claims

This repository supports the following observable claims:

- The runtime was evaluated under adversarial, degraded, and unstable conditions
- The runtime preserved continuity under defined test scenarios
- The runtime enforced policy and boundary constraints under stress
- The runtime preserved audit integrity across execution runs
- The runtime exhibited fail-closed behavior under uncertainty
- The runtime maintained bounded safe degradation under resource constraints

These claims are supported strictly by published datasets, execution traces, and integrity artifacts.

## Non-claims

This repository does NOT claim to expose:

- Full internal implementation of the runtime core
- Step-by-step internal decision reasoning paths
- Proprietary arbitration or defense logic
- Complete adversarial payload construction logic
- Undocumented runtime behaviors outside the evaluation scope

## Access model

The public repository is intended for verification of observable system behavior only.

Access to internal systems, orchestration logic, and proprietary mechanisms may be provided separately under NDA or formal agreement.

## Review guidance

Reviewers should focus on:

- Artifact integrity and hash consistency
- Dataset → execution → result alignment
- Reproducibility of published outputs
- Consistency between invariants and observed behavior
- Structural coherence of evaluation methodology

Reviewers should not expect access to internal runtime implementations or hidden execution logic.

## Summary

This repository defines a strict separation between observable evaluation evidence and private system implementation. The public layer demonstrates behavior under stress; the private layer contains the mechanisms that produce that behavior.