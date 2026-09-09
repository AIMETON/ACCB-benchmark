# Scorer Validation and Public Examples

The deterministic B2 scorer is published at:

`benchmark/scoring/score_accb_b2_trace.py`

Four public development fixtures are provided under `benchmark/public_dev/`.

Each fixture includes:

- `*.scenario.json` — public scenario definition;
- `*.initial-state.json` — initial state;
- `*.gold-ledger.json` — deterministic reference state used for scoring;
- `*.reference-trace.json` — a trace intended to satisfy the reference contract;
- `*.negative-trace.json` — a deliberately incorrect trace.

## Reproducing a positive scoring example

Example:

```bash
python benchmark/scoring/score_accb_b2_trace.py \
  --gold benchmark/public_dev/ACCB-DEV-001.gold-ledger.json \
  --trace benchmark/public_dev/ACCB-DEV-001.reference-trace.json
```

The output is a JSON score report containing:

- CSS;
- GAS;
- TIS;
- DCS;
- MCS;
- SAS;
- ACI_B2;
- ACI_B2_min;
- critical failure list.

## Reproducing a negative scoring example

```bash
python benchmark/scoring/score_accb_b2_trace.py \
  --gold benchmark/public_dev/ACCB-DEV-001.gold-ledger.json \
  --trace benchmark/public_dev/ACCB-DEV-001.negative-trace.json
```

The scorer returns a non-zero exit status when critical failures are present and reports the affected metric dimensions.

The same procedure can be repeated for ACCB-DEV-002 through ACCB-DEV-004.

## What this validates

These fixtures allow independent inspection of:

- exact field comparison for control states;
- exact aggregate comparison;
- temporal aggregate scoring;
- binary dependency scoring;
- ordered reconstruction-subsequence scoring;
- no-mutation safety scoring;
- critical output-contract checks.

They do **not** validate the stochastic historical model generations themselves because raw historical model outputs were not retained in the B2 pilot.

## Historical response-level examples

No raw production model completions are published because they were not retained under the frozen evidence policy. Publishing synthetic text while presenting it as historical model output would be misleading, so the public package instead provides explicit reference and negative traces for deterministic scorer validation.
