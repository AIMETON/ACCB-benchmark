# ACCB B2 Provider-Max Compute Policy v0.1

Status: FROZEN METHODOLOGY AMENDMENT
Date: 2026-09-08

## Principle

Scientific ACCB runs must not impose an AIMETON generation or reasoning ceiling below the selected endpoint's advertised maximum.

## Execution rule

For every scored B2 cell:

1. select and pin one healthy endpoint using a fresh no-generation capability census;
2. require an explicit endpoint output/completion maximum;
3. set the request allowance to that endpoint-advertised maximum;
4. do not replace it with a common cross-model cap;
5. do not force low/reduced reasoning effort or equivalent compute controls;
6. do not use local tokenizers as an execution gate;
7. use one provider generation per cell, with no automatic retry and no fallback.

Only the intrinsic limits of the selected model/provider endpoint may bound generation.

## Interpretation

Different models may have different intrinsic output maxima. Report those maxima and actual reasoning/output usage alongside cognitive scores.

If a model reaches its own selected endpoint maximum before producing a valid final answer, classify the cell as:

MODEL_ENDPOINT_COMPUTE_LIMIT_REACHED

This is a tested model/endpoint capability boundary and is not assigned synthetic ACI=0.

## Cost governance

Cost control must use pre-call conservative pricing, explicit tranche authorization, and a bounded number of cells. It must not be implemented by lowering model compute below the selected endpoint maximum.

If the conservative tranche guard exceeds the currently authorized spend ceiling, execution is blocked pending explicit owner authorization.

## Historical status

The legacy global 8192 cap and the later common 128000 B2 cap remain immutable historical evidence but are deprecated for future scientific execution.

This amendment authorizes no paid provider generation by itself.
