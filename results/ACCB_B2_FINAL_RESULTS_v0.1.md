# ACCB B2 — final cognitive-integrity scaling results v0.1

**Status:** COMPLETE DIAGNOSTIC RESULT  
**Date:** 2026-09-08  
**Canonical execution evidence:** `AIMETON/AIMETON_site_auditor`, issue #798  
**Primary scored run:** `34216143208`  
**GLM reasoning-normalized rerun:** `34249034069`

## Executive result

ACCB B2 measured cognitive integrity as a function of exact UTF-8 semantic payload size across five current long-context models.

Primary cross-model x-axis:

- 32,768 bytes
- 65,536 bytes
- 143,934 bytes
- 575,367 bytes
- 2,297,725 bytes

Provider token counts are model-specific telemetry and are not the primary cross-model axis.

The experiment found that nominal context-window capacity is not equivalent to cognitive continuity. All tested models accepted large payloads, but their ability to preserve temporal supersession, revocation, dependency state and final-state coherence differed materially as semantic load increased.

The experiment also identified a methodological confounder: provider-default reasoning allocation can dominate latency, cost and even prevent a final answer. GLM-5.2 was therefore rerun across all five tiers under a frozen explicit reasoning policy.

## Final ACI_B2 matrix

The GLM row below uses the reasoning-normalized rerun. The historical provider-default GLM row is retained only as diagnostic evidence and is not used for the final cognitive curve.

| Model | 32k | 64k | 140k | 562k | 2191k | Mean |
|---|---:|---:|---:|---:|---:|---:|
| GPT-5.6 Sol | 1.000000 | 0.925926 | 1.000000 | 1.000000 | 0.608796 | 0.906944 |
| Kimi K3 | 1.000000 | 0.810185 | 1.000000 | 0.814815 | 0.814815 | 0.887963 |
| DeepSeek V4 Pro | 1.000000 | 0.740741 | 1.000000 | 0.814815 | 0.629630 | 0.837037 |
| GLM-5.2 reasoning-normalized | 1.000000 | 0.814815 | 0.925926 | 0.560185 | 0.479167 | 0.756019 |
| Qwen 3.7 Plus | 0.759259 | 0.407407 | 0.925926 | 0.555556 | 0.504629 | 0.630556 |

## ACI_B2_min matrix

| Model | 32k | 64k | 140k | 562k | 2191k |
|---|---:|---:|---:|---:|---:|
| GPT-5.6 Sol | 1.000000 | 0.666667 | 1.000000 | 1.000000 | 0.000000 |
| Kimi K3 | 1.000000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 |
| DeepSeek V4 Pro | 1.000000 | 0.000000 | 1.000000 | 0.000000 | 0.000000 |
| GLM-5.2 reasoning-normalized | 1.000000 | 0.000000 | 0.666667 | 0.000000 | 0.000000 |
| Qwen 3.7 Plus | 0.222222 | 0.000000 | 0.666667 | 0.000000 | 0.000000 |

## Large-context comparison

Mean ACI_B2 over the two largest semantic loads:

| Model | Mean of 562k + 2191k |
|---|---:|
| Kimi K3 | 0.814815 |
| GPT-5.6 Sol | 0.804398 |
| DeepSeek V4 Pro | 0.722223 |
| Qwen 3.7 Plus | 0.530093 |
| GLM-5.2 reasoning-normalized | 0.519676 |

GPT-5.6 Sol has the highest mean over the complete five-tier range. Kimi K3 has the highest mean over the two largest tiers.

## Execution integrity

### Main five-model run

- run: `34216143208`
- exact Site Auditor SHA: `390e279549f2c9ec4a6fd8700e7dce9274252c88`
- evidence comment: `5586594799`
- planned/completed: 25/25
- scored: 23
- GLM common-output-ceiling exclusions: 2
- harness failures: 0
- model-output contract failures: 0
- retries: 0
- fallbacks: false
- accounted spend: 3419.368657 RUB

The two unscored cells were GLM-5.2 at 575,367 and 2,297,725 bytes. Both consumed the full 128,000-token common completion ceiling as reasoning and emitted no final answer.

### Provider-max GLM diagnostic

- run: `34240242865`
- exact Site Auditor SHA: `04f9dd1795fde4bb52349d6479f0d4d84e600465`
- evidence comment: `5587941916`

Both large GLM cells reproduced the same behavior at the selected endpoint advertised maximum:

- 562k: 131,072 output / 131,072 reasoning / 0 final
- 2191k: 131,072 output / 131,072 reasoning / 0 final

Both were correctly classified as `MODEL_ENDPOINT_COMPUTE_LIMIT_REACHED`, not as cognitive ACI=0.

### GLM reasoning-normalized rerun

- run: `34249034069`
- exact Site Auditor SHA: `29bff813c09a8bebdeea572eda61673c5c68aa55`
- evidence comment: `5588800356`
- planned/completed/scored: 5/5/5
- endpoint-compute-limit cells: 0
- integration cells: 0
- harness failures: 0
- retries: 0
- fallbacks: false
- accounted spend: 124.278493 RUB

Frozen GLM reasoning policy:

- reasoning enabled
- effort: `high`
- thinking budget: 32,768 tokens
- final-answer reserve policy: endpoint maximum minus thinking budget

Observed split:

| Tier | output / reasoning / final | ACI_B2 | ACI_B2_min |
|---|---:|---:|---:|
| 32k | 12,651 / 12,081 / 570 | 1.000000 | 1.000000 |
| 64k | 18,272 / 17,686 / 586 | 0.814815 | 0.000000 |
| 140k | 21,494 / 20,932 / 562 | 0.925926 | 0.666667 |
| 562k | 33,700 / 32,768 / 932 | 0.560185 | 0.000000 |
| 2191k | 33,365 / 32,768 / 597 | 0.479167 | 0.000000 |

At the two largest loads GLM reaches the frozen reasoning budget exactly and then emits a valid final answer. This demonstrates that the original 128k/131072 behavior was an inference-policy/output-allocation failure rather than proof that the model could not process the payload.

## Interpretation

### 1. Context acceptance is not cognitive continuity

A model can technically accept a multi-hundred-thousand-token request while still losing part of the temporal or semantic state required for a correct final reconstruction.

Therefore context capability should be separated into at least:

1. context acceptance;
2. context utilization;
3. cognitive continuity.

ACCB B2 directly targets the third property.

### 2. No universal degradation curve was observed

The models show materially different profiles.

**GPT-5.6 Sol** remains effectively flat through 562k and then drops sharply at 2191k. This is consistent with a plateau followed by a threshold-like transition.

**Kimi K3** loses some integrity earlier but remains almost perfectly flat between 562k and 2191k. It is the strongest model in the two-largest-tier average, while its zero ACI_min values show local critical failures despite a strong mean.

**DeepSeek V4 Pro** remains strong but non-monotonic. Its maximum-tier ACI is materially below its small-context values.

**GLM-5.2** under normalized reasoning shows increasing compute demand and then saturation of the 32,768-token thinking budget. Once saturated, ACI falls strongly at 562k and 2191k.

**Qwen 3.7 Plus** shows the lowest overall mean and substantial variation between tiers.

### 3. Reasoning policy is part of experimental state

GLM demonstrated that an unspecified provider-default reasoning policy can dominate the result.

Under provider defaults the selected endpoint spent 128k-131072 tokens entirely on hidden reasoning and produced no final answer. Under an explicit high-reasoning 32,768-token thinking budget, all five cells became scoreable.

Thus a reasoning-model benchmark must retain, where supported:

- reasoning enabled/disabled state;
- reasoning effort;
- explicit reasoning/thinking budget;
- final-answer reserve;
- observed reasoning tokens;
- observed final-answer tokens.

A benchmark that omits these variables can accidentally compare provider inference defaults rather than model cognition.

### 4. Latency is not explained by input size alone

The GLM diagnostic also showed that long latency was largely generation compute rather than merely request transport or queueing. The 131k-reasoning calls ran for roughly half an hour, while the normalized calls terminated after substantially fewer generated tokens.

For production routing, latency modelling therefore needs to include reasoning-token demand as well as input length.

### 5. Reasoning demand may be a useful additional observable

For normalized GLM the observed reasoning usage was:

- 12,081
- 17,686
- 20,932
- 32,768
- 32,768

The largest two cells saturate the imposed compute budget.

This suggests a useful future diagnostic quantity:

`reasoning demand / semantic load`

and motivates a more general capability model:

`Cognitive Integrity = f(semantic load, reasoning compute, model, inference policy)`.

## What this experiment supports

1. Cognitive continuity is not equivalent to nominal context-window size.
2. Multi-megabyte semantic payloads can remain usefully processable, but integrity varies materially by model.
3. GPT-5.6 Sol is the strongest overall model in this five-tier diagnostic.
4. Kimi K3 is the strongest on average across the two largest tiers.
5. Reasoning allocation can materially alter scoreability, latency and cost.
6. Transport/integration/output-budget failures must remain separate from cognitive failures.
7. Exact request bytes are a viable vendor-neutral primary x-axis for this experiment.

## What this experiment does not establish

This is a diagnostic experiment with one provider generation per model × tier cell. It does not establish:

- a universal model ranking;
- confidence intervals or stochastic variance;
- a universal maximum safe context;
- a smooth dose-response function;
- invariance across different tasks, languages or fact-placement patterns;
- that reasoning policies are fully normalized across all five models.

The GLM reasoning policy was explicitly normalized after its provider-default behavior was shown to be a confounder. Other reasoning-capable models retain the policies used in the primary run. A future confirmatory campaign should preregister explicit model-specific reasoning controls before execution.

## Closure

ACCB B2 is complete as a diagnostic campaign.

The scientifically meaningful next stage, if opened, is a new preregistered experiment with:

- repeated independent generations per cell;
- explicit reasoning-control contracts for every reasoning model;
- additional semantic-load levels around observed transition regions;
- confidence intervals and variance decomposition;
- separate analysis of semantic-load effects and reasoning-compute effects.

The completed B2 execution harness is not required for normal Site Auditor operation and may be removed from the execution repository after this report and issue evidence are retained.
