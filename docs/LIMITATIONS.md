# Limitations of ACCB B2 v0.1

1. **n=1 per model × load condition.** No variance, confidence interval or significance estimate is available.
2. **Inference regimes are not fully normalized across vendors.** The final GLM row uses a fixed high-reasoning 32,768-token budget.
3. **One task family.** B2 evaluates reconstruction of evolving structured state and should not be generalized directly to coding, mathematics, open-ended research or other task classes.
4. **Five load levels only.** The experiment cannot localize precise transition points or establish monotonicity.
5. **Composite metric granularity differs by component.** CSS has 72 primitive checks; GAS 9; TIS 3; MCS 7; DCS and SAS are binary.
6. **Raw historical model outputs were not retained.** The deterministic generator/scorer and public fixtures are auditable, but historical response-level rescoring is not possible.
7. **Provider evolution.** New executions may not reproduce historical outputs if providers update model weights, routing or inference policies.

The B2 campaign should therefore be interpreted as a hypothesis-generating pilot establishing a measurement framework and identifying candidate long-context degradation regions.
