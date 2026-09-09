# Scorer Validation

The deterministic B2 scorer is:

`benchmark/scoring/score_accb_b2_trace.py`

The validation procedure below uses fixtures generated from the **same frozen B2 entity-ledger generator** used by the published benchmark.

## Generate a true B2 validation fixture

```bash
python benchmark/b2_validation/generate_fixture.py \
  --tier b2-32k \
  --output-dir /tmp/accb-b2-validation
```

This produces:

- `gold.json`;
- `positive_trace.json`;
- `negative_trace.json`.

No provider API call is required.

## Reproduce a positive scoring example

```bash
python benchmark/scoring/score_accb_b2_trace.py \
  --gold /tmp/accb-b2-validation/gold.json \
  --trace /tmp/accb-b2-validation/positive_trace.json
```

Expected:

- `passed=true`;
- `ACI_B2=1.0`;
- `ACI_B2_min=1.0`;
- `critical_failure_count=0`.

## Reproduce a negative scoring example

```bash
python benchmark/scoring/score_accb_b2_trace.py \
  --gold /tmp/accb-b2-validation/gold.json \
  --trace /tmp/accb-b2-validation/negative_trace.json
```

The negative trace is deliberately corrupted and must produce a non-zero scorer exit status and one or more critical failures.

## Continuous integration

`.github/workflows/validate-b2-scorer.yml` executes both checks automatically:

1. generate a B2 fixture from the frozen generator;
2. require the positive trace to score perfectly;
3. require the negative trace to fail.

This makes the public scorer-validation contract executable rather than descriptive.

## Historical ACCB-DEV fixtures

`benchmark/public_dev/ACCB-DEV-001...004` are retained only for provenance.

They belong to a separate historical **Layer C stateful-tools development domain** and use a different data model. They are **not inputs for the B2 entity-ledger scorer**.

The previous version of this document incorrectly presented those Layer C fixtures as B2 scorer-validation examples. That documentation error is corrected here.

## Scope of validation

The B2 validation harness exercises:

- 72 control-state field comparisons;
- nine global aggregates;
- temporal aggregate scoring;
- dependency consistency scoring;
- ordered reconstruction-subsequence scoring;
- no-mutation safety scoring;
- critical output-contract checks.

It validates the deterministic benchmark/scorer mechanics.

It does not reproduce the historical stochastic model completions because raw production completions were not retained under the original B2 evidence policy.
