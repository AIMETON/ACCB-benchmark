# ACCB Benchmark

**AIMETON Cognitive Continuity Benchmark (ACCB)** is a public research benchmark for studying how large language models preserve a coherent evolving state under increasing semantic information load.

This repository is the canonical public source for the ACCB B2 pilot/diagnostic campaign conducted on 2026-09-08.

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
