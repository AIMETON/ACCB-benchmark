# ACCB B2 — GPT-5.6 Sol reasoning-control scope clarification v0.1

Status: **POST-EXECUTION EVIDENCE CLARIFICATION**  
Date: 2026-09-09

## Why this clarification exists

The frozen methodology amendment `ACCB_B2_REASONING_CONTROL_AMENDMENT_v0.1.md` records a pre-execution finding:

> The historical OpenRouter Responses helper for GPT-5.6 Sol explicitly sent `reasoning.effort=low`.

That finding referred to an **earlier helper implementation** and motivated the rule that the B2 scored execution must not force low reasoning effort.

It does **not** describe the request body used by the primary 25-cell B2 execution.

## Executed primary B2 evidence

Primary run:

- run: `34216143208`;
- exact Site Auditor SHA: `390e279549f2c9ec4a6fd8700e7dce9274252c88`.

At that exact SHA, `scripts/accb_b2_live_execution.py::openrouter_sol_call` constructed the Sol payload with:

- `model`;
- `input`;
- `max_output_tokens`;
- pinned OpenAI provider routing;
- fallback disabled.

The payload did **not** contain a `reasoning` object and did **not** contain `reasoning.effort=low`.

The execution receipt field was:

`reasoning_effort_sent: null`

and the run manifest explicitly recorded:

`forced_low_reasoning_effort: false`.

The exact-head contract test additionally asserted that the execution script did not contain:

- `"effort": "low"`;
- an equivalent low-reasoning payload.

## Scientific interpretation

Therefore the reviewer inference

> the published GPT-5.6 Sol B2 row was generated under forced `reasoning.effort=low`

is not supported by the exact executed source.

No compensating Sol rerun is required to remove a forced-low-effort confound, because that control was not sent in the published primary run.

A broader limitation **does remain**: inference-time reasoning compute was not normalized to an equal hard budget across all vendors. Sol therefore remains a model × provider-route × provider-default-reasoning-regime observation, not a weight-only comparison at equal reasoning compute.

This clarification does not alter any historical score or experimental result.
