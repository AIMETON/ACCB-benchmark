# B2 Scorer Validation

This directory contains a deterministic validation harness for the **actual ACCB B2 entity-ledger domain** used in the published paper.

The fixture generator imports the frozen B2 generator and derives:

- `gold.json`;
- `positive_trace.json`;
- `negative_trace.json`.

No model API call is required.

## Generate a B2 validation fixture

```bash
python benchmark/b2_validation/generate_fixture.py \
  --tier b2-32k \
  --output-dir /tmp/accb-b2-validation
```

## Positive trace

```bash
python benchmark/scoring/score_accb_b2_trace.py \
  --gold /tmp/accb-b2-validation/gold.json \
  --trace /tmp/accb-b2-validation/positive_trace.json
```

Expected result:

- `passed: true`;
- `ACI_B2: 1.0`;
- `ACI_B2_min: 1.0`;
- no critical failures.

## Negative trace

```bash
python benchmark/scoring/score_accb_b2_trace.py \
  --gold /tmp/accb-b2-validation/gold.json \
  --trace /tmp/accb-b2-validation/negative_trace.json
```

The negative trace deliberately violates:

- one control-state field;
- one global aggregate;
- the required reconstruction sequence;
- `mission_complete`;
- `next_safe_step`;
- the no-mutation invariant.

The scorer is expected to reject it with a non-zero exit code and report failures in the affected dimensions.

## Legacy public_dev fixtures

The files under `benchmark/public_dev/ACCB-DEV-001...004` belong to an earlier **Layer C stateful-tools development domain**. They are retained only as historical public development fixtures.

They are **not** valid inputs for `score_accb_b2_trace.py` and must not be used as B2 scorer-validation examples.
