# Sovereignty Test Matrix

This document turns sovereign-runtime claims into testable experiments for an offline-first edge agent system. The goal is to prove that domain ownership, policy supremacy, tamper detection, verifiable continuity, and recovery are enforced under real failure conditions rather than merely asserted.

## Purpose

- Use controlled chaos experiments to validate steady-state behavior under disruption, because chaos engineering begins with a measurable system behavior and then injects faults to test whether that behavior holds.
- Focus on offline-first critical infrastructure and industrial digital twin scenarios, where continued operation during disconnection and safe recovery afterward are central operational requirements.
- Capture evidence that can survive technical scrutiny: logs, hashes, refusal records, checkpoint outcomes, recovery timing, and replayable test steps.

## Sovereign claims

| Claim | What must remain true | Evidence |
|---|---|---|
| Domain ownership | Local actor state cannot be mutated by unauthorized commands. | Refusal log, unchanged state hash, unchanged checkpoint hash. |
| Policy supremacy | Local policy engine overrides external or conflicting requests. | Decision log, refusal event, policy evaluation output. |
| Tamper detection | Modified state or logs are detected before unsafe execution continues. | Hash mismatch record, safe-mode transition, rejected load. |
| Verifiable continuity | Identity and audit continuity survive restart, checkpoint restore, or migration. | Stable identity chain, checkpoint lineage, Merkle/audit validation. |
| Recovery | After crash, corruption, or partition, system restores safely or fails closed. | Recovery timestamp, restore logs, preserved invariants. |
| Simulation grounding | Offline prediction loop continues using local simulation anchors. | Prediction outputs, continuity of simulation cycle, baseline comparison. |
| Resource governance | Under stress, runtime degrades safely rather than corrupting state. | Throttle event, preserved logs, bounded latency or safe refusal. |

## Steady state before chaos

Record these baseline metrics before any test begins. Chaos engineering requires a known steady state before fault injection.

- Actor identity hash.
- Checkpoint hash.
- Current policy version hash.
- Audit root or Merkle root for the current log chain.
- Mean message latency.
- Mean checkpoint write time.
- Mean recovery time from clean restart.
- Refusal accuracy on a known unauthorized command set.
- Simulation accuracy against a small baseline scenario set.
- CPU, memory, and file-descriptor usage in normal operation.

## Test matrix

| ID | Claim under test | Fault injection | Procedure | Expected pass condition | Evidence to save |
|---|---|---|---|---|---|
| T01 | Domain ownership | Unauthorized external command | Send command that requests forbidden state mutation. | Command refused, state hash unchanged, refusal logged. | Before/after state hash, refusal log, command transcript. |
| T02 | Policy supremacy | Conflicting peer command | Send local-allowed and peer-conflicting commands in sequence. | Local policy wins, peer override blocked and logged. | Policy evaluation output, decision log. |
| T03 | Tamper detection | Checkpoint byte corruption | Modify saved checkpoint before load. | Hash validation fails, runtime enters safe mode, no unsafe load. | Corrupted file hash, mismatch log, safe-mode flag. |
| T04 | Tamper detection | Log chain edit | Delete or modify one audit entry. | Audit root mismatch detected, chain rejected. | Merkle root before/after, validation failure log. |
| T05 | Verifiable continuity | Process death | Kill one actor during operation and restart it. | Identity continuity preserved, checkpoint lineage valid, no silent divergence. | Restart log, identity hash continuity, checkpoint lineage. |
| T06 | Recovery | Disk write failure | Force checkpoint write failure or read-only storage. | Runtime fails closed or retries safely, logs the failure, keeps last valid checkpoint. | I/O error log, surviving checkpoint hash. |
| T07 | Recovery | Memory file corruption | Corrupt memory.json and attempt restore. | Corruption detected, restore refused or fallback checkpoint loaded. | Hash mismatch log, chosen recovery path. |
| T08 | Offline autonomy | Network partition | Disconnect selected actors or drop messages. | Local simulation and policy enforcement continue offline, reconciliation later preserves audit consistency. | Partition start/end times, offline decisions, reconciliation log. |
| T09 | Resource governance | CPU limit | Constrain CPU and continue workload. | Self-throttling or degraded mode activates without state corruption. | CPU cap config, throttle logs, state hash continuity. |
| T10 | Resource governance | Memory pressure | Limit memory or trigger pressure. | Runtime preserves safety invariants, drops noncritical work first, logs degradation. | Memory profile, degradation log. |
| T11 | Resource governance | File-descriptor exhaustion | Restrict open handles and run load. | Runtime fails safely, no silent write loss, clear error logging. | FD limit config, error log, checkpoint status. |
| T12 | Simulation grounding | Latency injection | Add delay to model inputs, actor messaging, or storage. | Simulation loop remains ordered and auditable; policy decisions still follow valid data lineage. | Timing traces, audit log order, prediction outputs. |
| T13 | Reliability | Random handler exceptions | Randomly raise exceptions in selected handlers. | Supervisor or runtime recovers without invalid mutation; error is logged. | Exception log, restart log, state hash. |
| T14 | Replay defense | Replayed command | Re-send previously valid signed message. | Replay detected or refused under nonce/timestamp policy. | Replay detection log, unchanged state hash. |
| T15 | Stale-state defense | Stale checkpoint load | Attempt to load older snapshot than current policy permits. | Load refused or isolated with explicit warning. | Policy log, checkpoint metadata, refusal event. |
| T16 | Migration continuity | Device migration | Move checkpoint/identity from phone to server to second device. | Identity continuity preserved, validation chain holds, no duplicate authority accepted. | Migration log, device IDs, continuity proof. |

## Fault classes to implement

- **Latency injection:** intentionally slow message handling, checkpoint writes, or simulation steps to observe ordering, timeout, and throttling behavior.
- **Random exceptions:** make selected functions fail with a controlled probability to test containment and recovery.
- **Process death:** kill `Consensus`, `Healer`, or another critical actor during activity and observe restart integrity.
- 
- **Network disruption:** drop, delay, or partition actor communication to verify offline policy and later reconciliation.
- 
- **Disk and filesystem faults:** corrupt files, deny writes, or switch storage to read-only to test tamper detection and safe restore paths.
- **Resource exhaustion:** constrain CPU, memory, or file handles so the runtime must degrade safely rather than corrupting state.
- 
- **Adversarial data:** malformed commands, replayed messages, poisoned configuration, stale state, and conflicting instructions.

## Pass/fail rules

Every test should have a hard threshold, not a vague interpretation.

- Unauthorized mutation refusal rate: 100 percent.
- Tamper detection rate on modified checkpoint and log-chain tests: 100 percent.
- Silent corruption tolerance: zero incidents.
- Recovery after actor death: measured threshold chosen in advance, such as under 30 seconds.
- Identity continuity after restart or migration: 100 percent validation success.
- Audit-chain validation after partition or reconciliation: 100 percent.
- Resource-governed degradation: no unlogged state mutation and no unsafe checkpoint write.

## Run order

1. Establish baseline steady state and save hashes, logs, and timing metrics.
2. Run single-fault experiments first with small blast radius.
3. Repeat each single-fault test enough times to get stable failure and recovery numbers.
4. Add combined-fault experiments only after single faults pass, such as partition plus process death plus stale replay.
5. Build benchmark tables from repeated runs, because sovereignty claims need repeatable evidence rather than one successful demo.

## Suggested folder structure

```text
proof/
  plans/
    sovereignty_test_matrix.md
  baselines/
    steady_state.json
  runs/
    T01/
    T02/
    ...
  logs/
  hashes/
  checkpoints/
  videos/
  summaries/
```

## Per-test evidence checklist

- Test ID.
- Date and runtime version.
- Device or host identifier.
- Fault injected.
- Start state hash.
- End state hash.
- Checkpoint hash before and after.
- Audit root before and after.
- Decision and refusal logs.
- Recovery time.
- Final verdict: pass, fail, or unsafe behavior observed.

## Minimal execution contract for agents

Give every agent the same contract during testing:

- Start from a known checkpoint.
- Announce identity hash on boot.
- Log every command receipt, refusal, mutation, and checkpoint write.
- Validate state hash before restore.
- Enter safe mode on tamper mismatch.
- Preserve local policy precedence during partition or conflicting command input.
- Emit a final run summary with counts for processed messages, refusals, recoveries, and integrity failures.

## What this proves if it passes

Passing this matrix would not merely show that an actor has a snapshot; it would show that the runtime enforces sovereignty-like guarantees under controlled disruption. That is much closer to the kind of evidence needed for an offline-first critical infrastructure runtime, where digital twin continuity, resilience, and trustworthy recovery matter in real operations.