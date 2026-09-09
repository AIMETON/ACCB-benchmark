# Legacy public development fixtures

`ACCB-DEV-001` through `ACCB-DEV-004` are historical public development fixtures from the **Layer C stateful-tools domain**.

They use fields such as `claims`, `claim_statuses`, `reused_resources`, `created_resources`, and a Layer C action trace.

They are intentionally retained for provenance, but they are **not compatible with the B2 entity-ledger scorer**:

`benchmark/scoring/score_accb_b2_trace.py`

For B2 scorer validation, use:

`benchmark/b2_validation/generate_fixture.py`

and follow:

`benchmark/b2_validation/README.md`.
