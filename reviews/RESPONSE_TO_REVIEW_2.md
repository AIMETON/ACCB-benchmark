# Response to Second Scientific Review

Date: 2026-09-09  
Target paper revision: v0.6

This document records the disposition of the second external review of the ACCB B2 preprint.

## 1. Malformed display-math block around ACI_B2_min

**Reviewer finding:** accepted.

The `ACI_B2_min` display-math block in both RU and EN papers was missing its immediate closing `$$`, causing section 7.8 prose to fall inside the math block.

**Resolution:** fixed in both papers. The formula now closes immediately after the definition and section 7.8 is normal Markdown prose.

## 2. public_dev fixtures incompatible with the B2 scorer

**Reviewer finding:** accepted.

The reviewer correctly identified that `ACCB-DEV-001...004` belong to the historical Layer C stateful-tools domain and do not exercise the B2 entity-ledger fields expected by `score_accb_b2_trace.py`.

The previous `docs/SCORER_VALIDATION.md` incorrectly presented those fixtures as B2 positive/negative validation examples.

**Resolution:**

- added `benchmark/b2_validation/generate_fixture.py`;
- the fixture generator imports the frozen B2 generator and derives a true B2 gold state, perfect positive trace, and deliberately corrupted negative trace;
- added `benchmark/b2_validation/README.md`;
- added CI workflow `.github/workflows/validate-b2-scorer.yml`;
- CI requires the positive trace to return `passed=true`, `ACI_B2=1.0`, `ACI_B2_min=1.0`;
- CI requires the negative trace to fail;
- marked `benchmark/public_dev/ACCB-DEV-001...004` explicitly as historical Layer C fixtures;
- replaced the incorrect examples in `docs/SCORER_VALIDATION.md`.

## 3. Alleged forced-low reasoning confound for GPT-5.6 Sol

**Reviewer finding:** not supported by the exact executed source.

The frozen methodology amendment correctly states that an **older historical OpenRouter Responses helper** had explicitly sent `reasoning.effort=low`. This was a pre-execution finding that motivated the rule forbidding forced-low reasoning in B2.

However, the published primary B2 run did not execute that helper behavior.

Primary B2 evidence:

- run: `34216143208`;
- exact Site Auditor SHA: `390e279549f2c9ec4a6fd8700e7dce9274252c88`.

At that exact SHA, `scripts/accb_b2_live_execution.py::openrouter_sol_call` constructed the Sol request using `model`, `input`, `max_output_tokens`, and pinned provider routing. It did not include a `reasoning` object or `reasoning.effort=low`.

The code recorded:

- `reasoning_effort_sent: None`;
- `forced_low_reasoning_effort: False`.

The exact-head contract test also asserted that the execution script did not contain `"effort": "low"`.

**Resolution:**

- added `methodology/ACCB_B2_SOL_REASONING_SCOPE_CLARIFICATION_v0.1.md`;
- added the exact-run evidence to RU/EN papers, reproducibility documentation, limitations, and final-results interpretation;
- no compensating Sol rerun is required to remove a forced-low confound because no forced-low control was sent in the published run.

**Remaining limitation:** reasoning compute was not normalized to an equal hard budget across all vendors. Sol remains a model × route × provider-default-reasoning-regime observation.

## 4. Author metadata / affiliation

**Reviewer finding:** stale relative to the current main branch.

After the reviewed v0.4 snapshot, paper v0.5 added:

- author: Marareskul D.I. / Марарескул Д.И.;
- affiliation: AIMETON Research;
- corresponding email: marareskuldi@aimeton.ru;
- website: https://www.aimeton.ru;
- funding, affiliation and conflict-of-interest statement;
- `CITATION.cff`;
- collaboration/support disclosure.

No further correction was required for this review item.

## 5. n=1 statistical limitation

**Reviewer finding:** accepted and remains a real limitation.

No additional paid provider generations were performed as part of this revision.

B2 remains explicitly labeled a pilot/diagnostic study. Comparative means are described as observed descriptive summaries rather than expected performance estimates or statistical rankings.

A future confirmatory campaign remains the correct place for:

- repeated independent generations per cell;
- confidence intervals;
- variance decomposition;
- reasoning-budget normalization;
- richer TIS/DCS scoring.

## Final disposition

The second review identified two genuine publication defects that were corrected:

1. malformed math-block pairing;
2. invalid B2 scorer-validation documentation/fixtures.

It also raised a Sol forced-low-reasoning concern that was resolved by checking the exact executed source and found not to apply to the published run.

No historical B2 scores were changed by this revision.
