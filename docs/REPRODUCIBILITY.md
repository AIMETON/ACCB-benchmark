# Reproducibility Statement

## Publicly available

This repository publishes the deterministic scientific core of ACCB B2:

- frozen context generator;
- frozen deterministic scorer;
- preregistration and methodological amendments;
- schemas;
- public development scenarios, gold ledgers, positive traces and negative traces;
- frozen context hashes and descriptive results;
- sanitized execution provenance.

The frozen Site Auditor source SHA for the main B2 execution was:

`390e279549f2c9ec4a6fd8700e7dce9274252c88`

The frozen Architecture B2 source SHA was:

`d390b2f56c0b2dae4be0cc4810dcb86403f2dc26`

## Not available

Raw prompts, raw model completions and raw hidden reasoning traces were not retained under the original B2 evidence contract.

They therefore cannot be retrospectively released.

This means the exact historical provider generations cannot be replayed byte-for-byte from a saved response corpus. The deterministic benchmark construction and scorer can be audited and rerun, but reproducing model outputs requires new provider calls and may differ because model/provider versions can change.

## Public fixtures

`benchmark/public_dev/` contains frozen public examples with:
- scenario definitions;
- initial state;
- gold ledger;
- reference trace;
- negative trace.

These fixtures allow independent validation of parsing and scoring behavior without access to historical model outputs.

## Provider conditions

B2 is an operational model × route × inference-regime study, not a weight-only laboratory evaluation.

Reasoning compute was not fully normalized across vendors. GLM-5.2's final reported row uses an explicitly fixed high-reasoning regime with a 32,768-token reasoning budget. Other model rows reflect their frozen admitted routes and provider behavior used in the primary run.

## Statistical status

Each model × load condition contains one generation (n=1).

Accordingly B2 is a pilot/diagnostic study. The published values are descriptive observations, not estimates of expected model performance or statistically significant differences.
