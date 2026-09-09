# ACCB Benchmark

**AIMETON Cognitive Continuity Benchmark (ACCB)** is a public research benchmark for studying how large language models preserve a coherent evolving state under increasing semantic information load.

This repository is the canonical public source for the ACCB B2 pilot/diagnostic campaign conducted on 2026-09-08.

## Author and contact

**Marareskul D.I. / Марарескул Д.И.**  
AIMETON Research  
Email: **marareskuldi@aimeton.tu**  
Website: https://www.aimeton.ru

## What is published

- frozen B2 generator;
- deterministic scorer used by the experiment;
- preregistered methodology and amendments;
- JSON schemas;
- public development fixtures with positive and negative examples;
- final descriptive result tables;
- sanitized execution provenance;
- Russian and English paper drafts.

## What is not published

Raw model prompts, raw completions, and raw hidden reasoning traces were **not retained by design** in the original evidence contract. They therefore cannot be retrospectively published. This is a reproducibility limitation of the B2 pilot and is stated explicitly in the papers.

The benchmark logic, reference fixtures, frozen input hashes, scoring code, aggregate model telemetry, and exact execution provenance are published so the deterministic portions of the experiment can be independently audited.

## Papers

- [Russian paper](papers/ru/ACCB_B2_paper_ru.md)
- [English paper](papers/en/ACCB_B2_paper_en.md)

## Reproducibility

- [Context generation](docs/CONTEXT_GENERATION.md)
- [Metric definitions](docs/METRIC_DEFINITIONS.md)
- [Reproducibility statement](docs/REPRODUCIBILITY.md)
- [Scorer validation walkthrough](docs/SCORER_VALIDATION.md)
- [Limitations](docs/LIMITATIONS.md)
- [Execution evidence](evidence/EXECUTION_SUMMARY.md)

## Status

B2 is a **pilot diagnostic study**, not a confirmatory statistical benchmark. Each model × load condition contains one generation (n=1). The public results are descriptive observations and hypothesis-generating evidence.

A future confirmatory campaign should preregister repeated trials, normalized reasoning-compute regimes, and richer event-level component scores.

## License

See [LICENSE](LICENSE).


## Collaboration and support

ACCB welcomes independent replication, methodological collaboration, additional model/provider coverage, API credits, compute contributions, research grants, and voluntary donations supporting future experiments.

The immediate funding priority is a confirmatory campaign with repeated trials per model × load cell, which would allow variance estimates and statistically interpretable confidence intervals.

Scientific independence is a condition of support: sponsors or donors do not receive authority to alter protocols, suppress results, or control interpretation. Material support used in a specific experimental campaign should be disclosed publicly.

See [SUPPORT.md](SUPPORT.md) for current priorities and contact details.
