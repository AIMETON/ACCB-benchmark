# ACCB B2 Reasoning-Control Amendment v0.1

Status: **FROZEN METHODOLOGY AMENDMENT**  
Date: 2026-09-08

## Finding

The historical OpenRouter Responses helper for GPT-5.6 Sol explicitly sent `reasoning.effort=low`.

For ACCB B2 Information Load Scaling this would be a second compute-budget confounder independent of the legacy 8192-token output cap.

## Rule

Future B2 scored execution MUST NOT force a low reasoning/thinking effort.

For the frozen five-model diagnostic:

- do not send `reasoning.effort=low`;
- do not send an equivalent provider-specific low-thinking control;
- when no cross-model equivalent effort control exists, omit the effort control and let the selected model/endpoint use its normal reasoning policy;
- retain the common high output ceiling as the shared explicit compute boundary;
- record which reasoning controls were actually sent;
- raw chain-of-thought remains unretained.

A provider/model that requires a mandatory effort parameter must be separately preregistered before execution.

This amendment authorizes no provider generation.


## Model-output contract failures

A non-empty provider final answer that cannot be parsed as the required JSON object is a **model-output contract failure**, not a transport/integration exclusion.

For B2 scoring it receives:

- `status=MODEL_OUTPUT_CONTRACT_FAILURE`;
- `ACI_B2=0.0`;
- `ACI_B2_min=0.0`.

This rule applies only when a non-empty final answer was actually delivered. Empty final content caused by output-budget exhaustion or provider/integration failure remains unscored and excluded from cognition metrics.
