# ACCB Generation Budget Policy Amendment v0.2

Status: **FROZEN METHODOLOGY AMENDMENT — supersedes v0.1 section 2 rule 3**  
Date: 2026-09-08

## 1. Reason for amendment

A fresh B2 endpoint census showed materially different advertised output maxima across the five selected model routes, including approximately 128K for GPT-5.6 Sol and more than 1M for Kimi K3.

Using each endpoint's absolute maximum would give different models radically different compute/reasoning budgets and would make the cross-model cognitive-integrity comparison less controlled. It would also create an unnecessarily extreme worst-case cost envelope.

The legacy 8192-token ceiling remains invalid and prohibited.

## 2. Common high-ceiling rule

For a scored multi-model ACCB tranche:

1. fresh endpoint census selects and pins one healthy endpoint per model;
2. every selected endpoint MUST advertise a concrete maximum output/completion capacity;
3. define `C_common = min(max_output_capacity(model_i))` across the frozen model matrix;
4. every scored cell in the tranche receives the same generation ceiling `C_common`;
5. `C_common` MUST be materially above the known historical binding ceiling and MUST exceed 8192;
6. if `C_common <= 8192`, the tranche is not admitted;
7. changing the model matrix or endpoint pins requires recomputing `C_common`.

For the 2026-09-08 B2 census, the observed minimum endpoint maximum is approximately **128,000 tokens**, set by the selected GPT-5.6 Sol route. The exact admitted value must be frozen from the execution-side census receipt before paid execution.

## 3. Why this is preferable

This policy:

- removes the demonstrated 8192-token reasoning bottleneck;
- gives all models the same high compute/output allowance;
- avoids granting one model an order-of-magnitude larger reasoning budget merely because its provider permits it;
- keeps output-budget exhaustion observable rather than silently converting it into a cognition score;
- preserves cost governance without using a low cap to force the budget down.

## 4. Exhaustion handling

If a model consumes the common ceiling without producing a valid final answer:

- retain sanitized usage and finish/incomplete metadata;
- classify `OUTPUT_BUDGET_EXHAUSTED`;
- do not score the cell as ACI=0;
- do not silently retry with a higher limit inside the frozen tranche.

Such an event is evidence that the common compute allowance is potentially binding and requires a separately preregistered follow-up.

## 5. Final answer vs reasoning

The required scored JSON remains compact. The common high output ceiling is intended to leave ample room for internal reasoning where the provider counts reasoning inside the generation allowance.

Raw reasoning content remains prohibited from retention.

## 6. Cost governance

The no-paid census MUST price every cell using `C_common`, not the per-provider maximum and not the legacy 8192 cap.

No paid execution is authorized by this amendment.
