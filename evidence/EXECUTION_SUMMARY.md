# Sanitized B2 Execution Evidence

## Primary 25-cell run

- run: `34216143208`
- Site Auditor SHA: `390e279549f2c9ec4a6fd8700e7dce9274252c88`
- status: `ACCB_B2_EXECUTION_COMPLETE`
- planned/completed: 25/25
- scored in original run: 23
- output-budget exclusions: 2 GLM cells
- harness failures: 0
- retries: 0
- fallback: false
- raw prompt/completion/reasoning retained: false

## GLM reasoning-controlled five-cell run used for the final GLM paper row

- run: `34249034069`
- Site Auditor SHA: `29bff813c09a8bebdeea572eda61673c5c68aa55`
- planned/completed/scored: 5/5/5
- reasoning effort: high
- reasoning budget: 32,768 tokens
- retries: 0
- fallback: false

| tier | bytes | output | reasoning | final | ACI_B2 | ACI_min |
|---|---:|---:|---:|---:|---:|---:|
| b2-32k | 32,768 | 12,651 | 12,081 | 570 | 1.000000 | 1.000000 |
| b2-64k | 65,536 | 18,272 | 17,686 | 586 | 0.814815 | 0.000000 |
| b2-140k | 143,934 | 21,494 | 20,932 | 562 | 0.925926 | 0.666667 |
| b2-562k | 575,367 | 33,700 | 32,768 | 932 | 0.560185 | 0.000000 |
| b2-2191k | 2,297,725 | 33,365 | 32,768 | 597 | 0.479167 | 0.000000 |

The historical provider-debugging sequence is deliberately not part of the scientific narrative. This file records only provenance necessary to identify which validated execution produced the published GLM row.
