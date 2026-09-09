# ACCB B2 Context Generation

ACCB B2 uses a deterministic temporal event ledger rather than a fixed set of needles embedded in neutral filler.

The frozen generator is:

`benchmark/generator/generate_accb_b2_information_load.py`

Canonical scenario: `ACCB-B2-INFOLOAD-001`, version `0.1`.

## Tier scaling

| Tier | UTF-8 bytes | Entities | Total records | Authoritative | Stale handoffs | Conflicting summaries |
|---|---:|---:|---:|---:|---:|---:|
| b2-32k | 32,768 | 16 | 207 | 162 | 27 | 18 |
| b2-64k | 65,536 | 24 | 419 | 327 | 54 | 38 |
| b2-140k | 143,934 | 32 | 928 | 724 | 120 | 84 |
| b2-562k | 575,367 | 48 | 3,726 | 2,904 | 484 | 338 |
| b2-2191k | 2,297,725 | 64 | 14,730 | 11,478 | 1,913 | 1,339 |

Every authoritative transition participates in a contiguous per-entity version chain. Removing an authoritative transition changes the terminal state or invalidates a subsequent version precondition. Rejected stale/conflicting records are also scored through the global rejected-record aggregate.

## Deterministic seed

For each tier, the generator derives a seed from scenario id, version, tier id and target byte size using SHA-256. The same frozen code therefore recreates the same ledger for a given tier.

## Event families

Authoritative operations cycle through activation, bounded-limit update, policy supersession, dependency update, suspension, revocation and conditional restoration.

Non-authoritative records are inserted deterministically:
- every seventh position: stale handoff;
- every eleventh position: conflicting summary;
- conflicting summary takes precedence when both schedules coincide.

## Exact byte targets and fixed overhead

The temporal ledger is embedded in a fixed request envelope containing instruction, mission, rules and output contract.

| Tier | Semantic-event bytes | Fixed instruction/schema overhead | Terminal padding | Total |
|---|---:|---:|---:|---:|
| 32k | 30,882 | 1,781 | 105 | 32,768 |
| 64k | 63,612 | 1,781 | 143 | 65,536 |
| 140k | 142,111 | 1,782 | 41 | 143,934 |
| 562k | 573,445 | 1,782 | 140 | 575,367 |
| 2191k | 2,295,887 | 1,783 | 55 | 2,297,725 |

The terminal padding is space-only, outside the semantic ledger, and capped at 256 bytes. The apparent difference between event bytes and total bytes is therefore mostly the fixed request envelope, not hidden filler.

## Cross-model axis

Exact UTF-8 request bytes are the primary cross-model input axis. Provider token counts are retained as diagnostics because tokenizers differ across model families.
