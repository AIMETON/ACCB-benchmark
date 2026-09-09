# Reproducibility Statement

## Publicly available

This repository publishes the deterministic scientific core of ACCB B2:

- frozen context generator;
- frozen deterministic scorer;
- preregistration and methodological amendments;
- schemas;
- executable B2 scorer-validation fixture generator derived from the frozen B2 entity-ledger generator;
- historical Layer C public development fixtures retained separately for provenance;
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

## B2 scorer validation

The actual B2 scorer-validation path is:

`benchmark/b2_validation/generate_fixture.py`

It imports the frozen B2 generator and deterministically creates:
- a B2 gold state;
- a perfect positive trace;
- a deliberately corrupted negative trace.

`.github/workflows/validate-b2-scorer.yml` requires the positive trace to score `ACI_B2=1.0`, `ACI_B2_min=1.0`, `passed=true`, and requires the negative trace to fail.

The files under `benchmark/public_dev/ACCB-DEV-001...004` belong to a historical Layer C stateful-tools development domain. They are retained for provenance and are not valid inputs for the B2 entity-ledger scorer.

## Provider conditions

B2 is an operational model × route × inference-regime study, not a weight-only laboratory evaluation.

Reasoning compute was not fully normalized across vendors. GLM-5.2's final reported row uses an explicitly fixed high-reasoning regime with a 32,768-token reasoning budget. Other model rows reflect their frozen admitted routes and provider behavior used in the primary run.

For GPT-5.6 Sol, the exact primary-run source SHA `390e279549f2c9ec4a6fd8700e7dce9274252c88` did **not** send `reasoning.effort=low`; it sent no explicit reasoning-effort control and recorded `reasoning_effort_sent=null`. The historical low-effort helper mentioned in the frozen amendment predated the published B2 execution. See `methodology/ACCB_B2_SOL_REASONING_SCOPE_CLARIFICATION_v0.1.md`.

## Statistical status

Each model × load condition contains one generation (n=1).

Accordingly B2 is a pilot/diagnostic study. The published values are descriptive observations, not estimates of expected model performance or statistically significant differences.
