# ACCB: Measuring Cognitive Integrity of Large Language Models Under Increasing Semantic Information Load

## An Experimental Study of Effective Cognitive Context in Contemporary LLMs

**Author:** Marareskul D.I. / Марарескул Д.И.  
**Affiliation:** AIMETON Research  
**Corresponding author:** marareskuldi@aimeton.tu  
**Website:** https://www.aimeton.ru  
**Preprint version:** 0.5  
**Experiment date:** 8 September 2026

## Abstract

The context-window size of a Large Language Model (LLM) is normally reported as the maximum number of tokens that can be technically accepted in a single request. Technical acceptance, however, does not imply equally reliable integration of all semantically consequential information contained in that request.

We introduce the **AIMETON Cognitive Continuity Benchmark, Layer B2 (ACCB B2)**, an experimental benchmark designed to measure **cognitive integrity** as the amount of dynamically changing semantic state increases. Unlike evaluations dominated by retrieval of isolated facts from long texts, ACCB B2 requires a model to reconstruct the terminal state of a system after processing activations, revocations, policy supersessions, constraint updates, dependencies, conditional restorations, stale handoffs, and conflicting summaries distributed throughout the context.

The experimental contexts were produced by a deterministic temporal-ledger generator. Both the number of entities and the number of semantically consequential state transitions increased with load. The five tiers contained 207, 419, 928, 3,726, and 14,730 records respectively. At the largest tier, a model had to integrate 11,478 authoritative state transitions and correctly reject 3,252 stale or conflicting records.

Five contemporary long-context models were evaluated: GPT-5.6 Sol, Kimi K3, DeepSeek V4 Pro, GLM-5.2, and Qwen 3.7 Plus. Five deterministic information-load levels were used, containing exactly 32,768; 65,536; 143,934; 575,367; and 2,297,725 UTF-8 bytes. Exact canonical request size in bytes was the primary cross-model independent variable; provider-specific token counts were retained as secondary diagnostics.

We introduce **ACI_B2 (ACCB Cognitive Integrity)**, an equally weighted composite of six normalized dimensions: Control State Score (CSS), Global Aggregate Score (GAS), Temporal Integrity Score (TIS), Dependency Consistency Score (DCS), Motor/Procedure Coherence Score (MCS), and Safety Score (SAS). `ACI_B2_min`, the minimum component value, captures severe local failure that may be obscured by the mean.

In this pilot diagnostic study, with one generation per model × load condition (n=1), the observed five-tier mean ACI_B2 values were 0.907 for GPT-5.6 Sol, 0.888 for Kimi K3, 0.837 for DeepSeek V4 Pro, 0.756 for GLM-5.2, and 0.631 for Qwen 3.7 Plus. These values describe the realized observations rather than estimating expected model performance. The observed trajectories differed across models and were not strictly monotonic; with n=1, this is hypothesis-generating evidence rather than evidence for the shape of an underlying degradation function.

The results support a distinction between **context acceptance**, **context utilization**, and **effective cognitive context**. Nominal context-window size alone is insufficient to characterize an LLM's ability to maintain a coherent representation of a long, dynamically evolving information state.

**Keywords:** large language models, long context, cognitive continuity, cognitive integrity, semantic load, effective context, temporal reasoning, long-term memory, LLM evaluation, ACCB.

## 1. Introduction

Rapid expansion of context windows has become a major direction in LLM development. Contemporary systems can technically accept hundreds of thousands of tokens or more, creating an appealing assumption: if an entire interaction history, document collection, or persistent agent state fits inside the advertised context window, passing the complete history to the model should be sufficient.

Previous long-context research shows that this assumption is incomplete.

Liu et al. demonstrated that the ability to use information in long contexts depends strongly on position, with performance often declining when relevant information appears in the middle of the input [1].

LongBench introduced broad multitask evaluation of long-context understanding across document QA, summarization, few-shot learning, and code [2].

RULER showed that near-perfect performance on simple needle-in-a-haystack retrieval does not imply equally robust multi-hop tracing or aggregation [3]. ∞Bench extended standardized long-context evaluation beyond 100K tokens [4].

BABILong evaluates reasoning over facts distributed throughout extremely long natural texts and reports strong interaction between effective context use and reasoning complexity [5].

Loong is particularly relevant because it constructs multi-document tasks in which every document is necessary for a correct answer, reducing the usefulness of retrieving only a small subset of convenient passages [6].

LongBench v2 further emphasizes the role of deep reasoning and inference-time compute in realistic long-context problems [7].

ACCB targets a related but distinct problem: maintaining a coherent representation of an **evolving semantic state**.

A persistent agent may observe that an object is authorized, later revoked, subsequently reported as active by a stale handoff, and later conditionally restored while participating in dependencies with other objects.

The challenge is not merely to retrieve all statements. It is to determine which statements remain authoritative and reconstruct the globally consistent terminal state.

We call this capability **cognitive continuity**.

## 2. Research Question

The primary ACCB B2 question was:

> **How does cognitive integrity change as the amount of semantically necessary temporal state increases while task family, state-transition semantics, scoring procedure, and final-answer format remain stable?**

We distinguish:

**Context acceptance** — the technical ability of an endpoint to accept the input.

**Context utilization** — the ability to locate and use relevant information.

**Cognitive continuity** — the ability to integrate distributed state changes, revocations, supersessions, dependencies, and obsolete records into a coherent current state.

ACCB B2 primarily targets the third property.

## 3. Construction of the Experimental Context

### 3.1. Semantic load rather than textual dilution

A context may become longer in fundamentally different ways. One approach keeps a small set of important facts fixed while adding increasing amounts of irrelevant material. Such an experiment primarily measures retrieval robustness under **context dilution**.

The alternative is to increase the number of facts and state transitions that are themselves required to compute the answer. ACCB B2 uses the latter design.

There are no semantically neutral records in the scored temporal ledger. Every authoritative record changes system state, and every stale or conflicting record requires a correct rejection decision.

### 3.2. Deterministic generator

The experimental contexts were generated by `generate_accb_b2_information_load.py`.

Canonical scenario identifier: `ACCB-B2-INFOLOAD-001`, version `0.1`.

A separate deterministic seed was derived for each tier:

$$
seed=first32bits(SHA256(scenario\_id \parallel version \parallel tier \parallel target\_bytes)).
$$

The seed determines entity selection, event placement, control-panel selection, and the resulting reference state. The same code therefore reproduces the same semantic ledger for a given tier.

### 3.3. Entity state

The generator manages up to 64 entities:

$$
E0001,\ldots,E0064.
$$

Each entity has state vector

$$
S_i=(V_i,L_i,G_i,A_i,B_i,D_i),
$$

where (V_i) is current version, (L_i) lifecycle state, (G_i) policy generation, (A_i) authorization state, (B_i) bounded numerical limit, and (D_i) dependency pointer.

All entities start with version 0, lifecycle `draft`, generation 0, authorization `denied`, limit 0, and no dependency.

### 3.4. Scaling the entity population

| Tier | Entities |
|---|---:|
| 32k | 16 |
| 64k | 24 |
| 140k | 32 |
| 562k | 48 |
| 2191k | 64 |

The control-panel size is fixed at **12 entities** for every tier. Control entities are selected deterministically using a seed-dependent starting position and a traversal step coprime to the tier entity count.

### 3.5. Authoritative state transitions

Authoritative records form explicit version chains:

$$
v\rightarrow v+1.
$$

A transition is applicable only if its required version exactly matches the entity's current version.

For each entity, operation type follows a seven-stage cycle:

1. ACTIVATE;
2. LIMIT_UPDATE;
3. SUPERSEDE;
4. DEPENDENCY_UPDATE;
5. SUSPEND;
6. REVOKE;
7. RESTORE_CONDITIONAL.

The cycle then repeats.

### 3.6. Stale and conflicting records

Two additional record classes are inserted throughout the ledger.

A **STALE_HANDOFF** asserts that an older entity version is still current.

A **CONFLICTING_SUMMARY** asserts a state inconsistent with the authoritative event history.

Their placement is deterministic:

- every seventh position is a stale handoff;
- every eleventh position is a conflicting summary;
- at positions divisible by eleven, the conflicting summary takes precedence.

These records must be rejected. They are not irrelevant noise; correct rejection is part of the scored semantic task.

### 3.7. Realized ledger composition

| Tier | Entities | Total records | Authoritative transitions | Stale handoffs | Conflicting summaries |
|---|---:|---:|---:|---:|---:|
| 32k | 16 | **207** | 162 | 27 | 18 |
| 64k | 24 | **419** | 327 | 54 | 38 |
| 140k | 32 | **928** | 724 | 120 | 84 |
| 562k | 48 | **3,726** | 2,904 | 484 | 338 |
| 2191k | 64 | **14,730** | 11,478 | 1,913 | 1,339 |

Thus, at the largest tier a model must process more than fourteen thousand semantically consequential records. More than eleven thousand directly modify state, while more than three thousand must be recognized as non-authoritative.

### 3.8. Semantic-consequence invariant

The generator validates that authoritative records form contiguous per-entity version chains:

$$
0\rightarrow1\rightarrow2\rightarrow\dots\rightarrow N.
$$

Removing an authoritative transition breaks the version precondition of the next transition and changes the terminal entity version.

The benchmark additionally scores the sum of all entity versions,

$$
\sum_i V_i,
$$

so every authoritative record contributes to at least one scored terminal quantity.

The number of rejected stale/conflicting records is also a scored global aggregate.

### 3.9. Semantic density and exact byte targets

| Tier | Semantic-event bytes | Fixed instruction/schema overhead | Terminal padding | Total |
|---|---:|---:|---:|---:|
| 32k | 30,882 | 1,781 | 105 | 32,768 |
| 64k | 63,612 | 1,781 | 143 | 65,536 |
| 140k | 142,111 | 1,782 | 41 | 143,934 |
| 562k | 573,445 | 1,782 | 140 | 575,367 |
| 2191k | 2,295,887 | 1,783 | 55 | 2,297,725 |

The difference between semantic-event bytes and total request bytes is primarily the fixed request envelope: instruction, mission, rules, and output schema. Its size is nearly constant at 1,781–1,783 bytes. A very small space-only padding field was permitted solely to reach the exact UTF-8 byte target. It was outside the semantic ledger, semantically empty, and limited to at most 256 bytes.

### 3.10. Canonical request structure

The materialized request consisted of:

$$
Instruction + Mission + Rules + TemporalEventLedger + OutputContract.
$$

The fixed instruction required the model to reconstruct authoritative current state, apply events only when version preconditions match, reject stale and conflicting records, perform no real mutation, and emit only the compact required structured answer.

Provider adapters could represent system and user roles differently according to endpoint protocol, but canonical textual content and its SHA-256 digest were frozen before model invocation.

## 4. Semantic-Load Tiers

| Tier | Exact UTF-8 bytes |
|---|---:|
| B2-32k | 32,768 |
| B2-64k | 65,536 |
| B2-140k | 143,934 |
| B2-562k | 575,367 |
| B2-2191k | 2,297,725 |

Bytes rather than tokenizer-specific token counts were used as the primary cross-model axis. The same maximum context corresponded to approximately 547K–703K provider-reported input tokens across different models.

## 5. Model Matrix

1. GPT-5.6 Sol;
2. Kimi K3;
3. DeepSeek V4 Pro;
4. GLM-5.2;
5. Qwen 3.7 Plus.

The diagnostic experiment contained (5\times5=25) model × tier conditions. Each condition used one generation. Automatic retries and model fallback were disabled.

### 5.1. Model inclusion criteria

Models were included when they simultaneously satisfied practical admission criteria at the time of the experiment: API availability; advertised ability to accept the largest B2 payload through the selected route; an unambiguous model/provider identity; the ability to disable fallback to a different model; and a projected full-run cost compatible with the experiment budget.

The sample is not intended to be exhaustive. In particular, the absence of Claude and Gemini should not be interpreted as a statement about their relative quality; those families were not part of the frozen five-model diagnostic matrix.

### 5.2. Reasoning-compute regimes

Inference-time reasoning compute was not fully normalized across vendors.

| Model | Regime used in the published matrix |
|---|---|
| GPT-5.6 Sol | frozen admitted provider route; reasoning budget not cross-vendor normalized |
| Kimi K3 | frozen admitted provider route; reasoning budget not cross-vendor normalized |
| DeepSeek V4 Pro | frozen admitted provider route; reasoning budget not cross-vendor normalized |
| Qwen 3.7 Plus | frozen admitted provider route; reasoning budget not cross-vendor normalized |
| GLM-5.2 | explicit high-reasoning regime with a 32,768-token reasoning budget |

The cross-model values therefore characterize model × route × inference-regime systems rather than weight-only model comparisons under equal compute.

## 6. Output Task

The model produced a compact structured output rather than reproducing the ledger.

For each of 12 frozen control entities it returned version, lifecycle, policy generation, authorization, bounded limit, and dependency. It also returned global state aggregates and a short ordered reconstruction trace.

## 7. Metrics

### 7.1. Control State Score (CSS)

Twelve control entities × six fields produce 72 exact comparisons:

$$
CSS=\frac{N_{correct\ control\ fields}}{72}.
$$

### 7.2. Global Aggregate Score (GAS)

Nine exact system-wide quantities were evaluated: active entity count; revoked entity count; allowed authorization count; sum of active bounded limits; dependency violation count; dependency edge count; sum of entity versions; sum of policy generations; rejected stale/conflicting record count.

$$
GAS=\frac{N_{exact\ aggregate\ matches}}{9}.
$$

### 7.3. Temporal Integrity Score (TIS)

TIS v0.1 is an aggregate temporal measure based on exact agreement for revoked entity count, allowed authorization count, and rejected stale/conflicting record count.

$$
TIS=\frac{N_{correct\ temporal\ aggregates}}{3}.
$$

### 7.4. Dependency Consistency Score (DCS)

$$
DCS=
\begin{cases}
1,& \text{dependency violation count exactly matches reference};\\
0,& \text{otherwise}.
\end{cases}
$$

### 7.5. Motor/Procedure Coherence Score (MCS)

The output was expected to contain the following ordered subsequence:

1. initialize entities;
2. process authoritative events in order;
3. enforce version preconditions;
4. reject stale/conflicting records;
5. resolve dependencies;
6. compute global aggregates;
7. emit control-state snapshot.

$$
MCS=\frac{N_{ordered\ required\ stages\ matched}}{7}.
$$

Hidden chain-of-thought is neither used nor retained.

### 7.6. Safety Score (SAS)

$$
SAS=
\begin{cases}
1,& mutation\_performed=false;\\
0,& mutation\_performed=true.
\end{cases}
$$

### 7.7. Composite Cognitive Integrity

$$
ACI_{B2}=\frac{CSS+GAS+TIS+DCS+MCS+SAS}{6}.
$$

$$
ACI_{B2,min}=\min(CSS,GAS,TIS,DCS,MCS,SAS).

### 7.8. Rationale and sensitivity of equal dimension weights

The six dimension weights were fixed before the published B2 outcomes were observed. Equal dimension weighting prevents CSS from automatically dominating the composite merely because it contains 72 primitive comparisons while other dimensions have lower granularity.

This is a benchmark-design choice, not a uniquely validated psychometric weighting scheme. DCS and SAS are binary, whereas CSS, GAS, TIS, and MCS are fractional. A single global DCS or SAS failure can therefore reduce ACI_B2 by one sixth and force `ACI_B2_min=0`.

ACI_B2 should therefore be interpreted alongside the component structure, and `ACI_B2_min=0` does not imply total task failure. A confirmatory version should include weighting sensitivity analysis and richer event-level temporal/dependency assertions.

$$

## 8. Experimental Controls

For each cell the experiment retained exact model identity, provider route, exact request byte count, canonical request SHA-256, provider-reported input tokens, output tokens, reasoning-token count where exposed, termination status, and deterministic scorer output.

Raw chain-of-thought was not retained.

GLM-5.2 was evaluated under an explicitly fixed high-reasoning regime with a 32,768-token reasoning budget. Reasoning-compute regimes were not fully normalized across vendors; this is a limitation of cross-model comparison.

## 9. Descriptive Results of the Pilot Run

### 9.1. ACI_B2

Each value below comes from one generation. The table is intended to describe the realized observations and identify regions for confirmatory testing; it is not a statistical model ranking.

| Model | 32k | 64k | 140k | 562k | 2191k | Mean |
|---|---:|---:|---:|---:|---:|---:|
| GPT-5.6 Sol | 1.000 | 0.926 | 1.000 | 1.000 | 0.609 | **0.907** |
| Kimi K3 | 1.000 | 0.810 | 1.000 | 0.815 | 0.815 | **0.888** |
| DeepSeek V4 Pro | 1.000 | 0.741 | 1.000 | 0.815 | 0.630 | **0.837** |
| GLM-5.2 | 1.000 | 0.815 | 0.926 | 0.560 | 0.479 | **0.756** |
| Qwen 3.7 Plus | 0.759 | 0.407 | 0.926 | 0.556 | 0.505 | **0.631** |

### 9.2. ACI_B2_min

| Model | 32k | 64k | 140k | 562k | 2191k |
|---|---:|---:|---:|---:|---:|
| GPT-5.6 Sol | 1.000 | 0.667 | 1.000 | 1.000 | 0.000 |
| Kimi K3 | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| DeepSeek V4 Pro | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| GLM-5.2 | 1.000 | 0.000 | 0.667 | 0.000 | 0.000 |
| Qwen 3.7 Plus | 0.222 | 0.000 | 0.667 | 0.000 | 0.000 |

## 10. Model Profiles

GPT-5.6 Sol:

$$
1.000\rightarrow0.926\rightarrow1.000\rightarrow1.000\rightarrow0.609.
$$

Kimi K3:

$$
1.000\rightarrow0.810\rightarrow1.000\rightarrow0.815\rightarrow0.815.
$$

DeepSeek V4 Pro:

$$
1.000\rightarrow0.741\rightarrow1.000\rightarrow0.815\rightarrow0.630.
$$

GLM-5.2:

$$
1.000\rightarrow0.815\rightarrow0.926\rightarrow0.560\rightarrow0.479.
$$

Observed GLM reasoning-token consumption:

$$
12081\rightarrow17686\rightarrow20932\rightarrow32768\rightarrow32768.
$$

Qwen 3.7 Plus:

$$
0.759\rightarrow0.407\rightarrow0.926\rightarrow0.556\rightarrow0.505.
$$

## 11. Extreme-Load Region

| Model | Mean ACI_B2 at 562k and 2191k |
|---|---:|
| Kimi K3 | **0.815** |
| GPT-5.6 Sol | **0.804** |
| DeepSeek V4 Pro | **0.722** |
| Qwen 3.7 Plus | **0.530** |
| GLM-5.2 | **0.520** |

## 12. Discussion

The experiment supports

$$
\boxed{NominalContextWindow\neq EffectiveCognitiveContext}
$$

and

$$
RawTextLength\neq SemanticInformationLoad.
$$

ACCB B2 deliberately increases the latter.

Observed model trajectories are not strictly monotonic. With n=1, generation-level variability cannot be separated from a systematic load effect, so non-monotonicity is only a property of this realized series, not an established property of the underlying response curve.

The minimum-component metric is also important: a model may preserve much of the global state while completely failing one specific temporal, dependency, procedural, or safety dimension.

Finally, the GLM reasoning profile motivates a broader representation:

$$
CognitiveIntegrity=f(SemanticLoad,ReasoningCompute,Model,InferenceRegime).
$$

## 13. Implications for Memory and Agent Systems

The results challenge the naive architecture

$$
EntireHistory\rightarrow LLMContext.
$$

A more robust architecture may be

$$
LongTermMemory
\rightarrow CurrentStateReconstruction
\rightarrow SemanticallySufficientWorkingContext
\rightarrow LLM.
$$

This creates an empirical motivation for semantic compression, memory consolidation, explicit current-state reconstruction, model routing based on semantic load, and pre-inference cognitive-risk estimation. Semantic compression has previously been studied as a mechanism for extending effective context and reducing computation [8]; ACCB adds a testable hypothesis that it may also reduce active semantic integration load.

## 14. Limitations

The main limitation is (n=1) generation per model × tier condition. The present study therefore does not estimate variance, confidence intervals, or statistical significance.

Inference-time reasoning policies were not fully normalized across vendors.

The benchmark evaluates one task family: reconstruction of a dynamically evolving structured state.

The five load levels are too sparse to precisely locate transition regions.

Some B2 v0.1 component scores are deliberately compact. TIS is aggregate-level, and DCS is a binary global dependency check. Future versions should expand these components into richer event-level and graph-level assertion sets.

## 15. Effective Cognitive Context

A confirmatory campaign with repeated samples would enable estimation of

$$
P(ACI\geq\tau\mid L).
$$

We propose defining

$$
ECC_{\tau,p}
=
\max\{L:P(ACI\geq\tau\mid L)\geq p\}.
$$

For example, (ECC_{0.9,0.95}) would denote the largest semantic load at which ACI remains at least 0.9 with probability of at least 95%.

## 16. Conclusion

ACCB B2 evaluates whether large language models can preserve a coherent representation of a long and dynamically evolving semantic state.

GPT-5.6 Sol achieved the highest descriptive mean across the full tested range. Kimi K3 achieved the strongest mean over the two largest semantic-load conditions. DeepSeek V4 Pro exhibited strong but non-monotonic behavior. GLM-5.2 showed saturation of its fixed reasoning budget at the two largest loads. Qwen 3.7 Plus exhibited the greatest variation in this diagnostic series.

The broader conclusion is more important than the ordering of individual models:

> **A large accepted context is not equivalent to a large effective cognitive context.**

## 17. Code, Data, and Reproducibility

The canonical public research repository is:

**AIMETON/ACCB-benchmark**  
https://github.com/AIMETON/ACCB-benchmark

The repository publishes the frozen B2 context generator, deterministic scorer, preregistered methodology, metric definitions, schemas, public reference scenarios with positive and negative traces, context hashes, result matrices, sanitized provenance records, and Russian and English versions of this paper. Raw historical prompts, model completions, and hidden reasoning traces were not retained under the original evidence contract and therefore cannot be retrospectively released; this is an explicit reproducibility limitation.

Recommended citation:

**AIMETON Research. ACCB Benchmark: Cognitive Continuity under Semantic Information Load. Public research repository, 2026. https://github.com/AIMETON/ACCB-benchmark**

## 18. Collaboration and Support for Future Research

ACCB is being developed as an open research project. The author welcomes collaboration with researchers, model developers, inference providers, evaluation specialists, long-term-memory researchers, and agent-system developers.

Particularly useful forms of collaboration include:

- independent replication of B2;
- repeated trials with multiple generations per model × load condition;
- expansion to additional models and providers;
- denser semantic-load sampling;
- normalization of inference-time reasoning budgets;
- richer TIS and DCS component metrics;
- statistical analysis and estimation of Effective Cognitive Context (ECC);
- provision of compute resources or API credits.

Further experiments require paid model inference and computing infrastructure. The project therefore welcomes **voluntary donations, research grants, API credits, compute contributions, and sponsorship** dedicated to repeated and expanded ACCB experiments.

To discuss collaboration or support, contact **marareskuldi@aimeton.tu** with the subject `ACCB collaboration` or `ACCB research support`.

To protect scientific independence, support for future experiments must not grant a sponsor authority to alter the protocol, suppress results, or control their interpretation. Material external support used for a specific experimental campaign should be disclosed in the corresponding publication and public project documentation.

Current support priorities are documented at:
https://github.com/AIMETON/ACCB-benchmark/blob/main/SUPPORT.md

## 19. Funding, Affiliation, and Conflict-of-Interest Statement

**Funding of the completed B2 pilot.** This preprint does not declare a separate external funding source for the completed B2 pilot experiment. Future external financial or infrastructure support used for a specific campaign should be disclosed in the corresponding publication and public documentation.

**Affiliation and conflict of interest.**

The author is affiliated with AIMETON Research and is the developer and maintainer of ACCB. This relationship is disclosed for transparency. The present work reports a pilot research benchmark and is not a commercial model ranking.

Future donations, grants, API credits, or infrastructure support should not alter the benchmark methodology or publication criteria. Any material support used for a specific experiment should be disclosed in the corresponding report.

## References

[1] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., Liang, P. *Lost in the Middle: How Language Models Use Long Contexts*. Transactions of the Association for Computational Linguistics. 2024;12:157–173. DOI: 10.1162/tacl_a_00638.

[2] Bai, Y., Lv, X., Zhang, J., et al. *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding*. Proceedings of ACL 2024. 3119–3137. DOI: 10.18653/v1/2024.acl-long.172.

[3] Hsieh, C.-P., Sun, S., Kriman, S., Acharya, S., Rekesh, D., Jia, F., Zhang, Y., Ginsburg, B. *RULER: What's the Real Context Size of Your Long-Context Language Models?* 2024. arXiv:2404.06654.

[4] Zhang, X., Chen, Y., Hu, S., et al. *∞Bench: Extending Long Context Evaluation Beyond 100K Tokens*. Proceedings of ACL 2024. 15262–15277. DOI: 10.18653/v1/2024.acl-long.814.

[5] Kuratov, Y., Bulatov, A., Anokhin, P., Rodkin, I., Sorokin, D., Sorokin, A., Burtsev, M. *BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack*. Advances in Neural Information Processing Systems. 2024;37:106519–106554.

[6] Wang, M., Chen, L., Cheng, F., et al. *Leave No Document Behind: Benchmarking Long-Context LLMs with Extended Multi-Doc QA*. Proceedings of EMNLP 2024. 5627–5646. DOI: 10.18653/v1/2024.emnlp-main.322.

[7] Bai, Y., Tu, S., Zhang, J., et al. *LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks*. Proceedings of ACL 2025. arXiv:2412.15204.

[8] Fei, W., Niu, X., Zhou, P., Hou, L., Bai, B., Deng, L., Han, W. *Extending Context Window of Large Language Models via Semantic Compression*. Findings of ACL 2024. 5169–5181. DOI: 10.18653/v1/2024.findings-acl.306.
