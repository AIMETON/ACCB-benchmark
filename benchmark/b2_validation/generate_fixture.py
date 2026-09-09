#!/usr/bin/env python3
"""Generate deterministic B2 scorer-validation fixtures from the frozen B2 generator."""

from __future__ import annotations

import argparse
import importlib.util
import json
from copy import deepcopy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
GENERATOR_PATH = ROOT / "benchmark" / "generator" / "generate_accb_b2_information_load.py"


def load_generator() -> Any:
    spec = importlib.util.spec_from_file_location("accb_b2_generator", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load generator: {GENERATOR_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_positive_trace(gold: dict[str, Any]) -> dict[str, Any]:
    return {
        "scenario_id": gold["scenario_id"],
        "tier_id": gold["tier_id"],
        "control_states": deepcopy(gold["control_states"]),
        "aggregates": deepcopy(gold["aggregates"]),
        "action_trace": list(gold["required_action_trace"]),
        "mission_complete": True,
        "next_safe_step": "validation_complete_no_mutation",
        "mutation_performed": False,
    }


def build_negative_trace(gold: dict[str, Any]) -> dict[str, Any]:
    trace = build_positive_trace(gold)
    trace["mission_complete"] = False
    trace["next_safe_step"] = ""
    trace["mutation_performed"] = True
    trace["action_trace"] = []
    first_control = sorted(trace["control_states"])[0]
    trace["control_states"][first_control]["version"] += 1
    trace["aggregates"]["active_entity_count"] += 1
    return trace


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tier", default="b2-32k")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    generator = load_generator()
    suite = generator.build_suite()
    tiers = {row["tier_id"]: row for row in suite["tiers"]}
    if args.tier not in tiers:
        raise SystemExit(f"unknown tier {args.tier!r}; available={sorted(tiers)}")

    gold = deepcopy(tiers[args.tier]["gold"])
    positive = build_positive_trace(gold)
    negative = build_negative_trace(gold)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "gold.json": gold,
        "positive_trace.json": positive,
        "negative_trace.json": negative,
    }
    for name, payload in outputs.items():
        (args.output_dir / name).write_text(
            json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )

    print(json.dumps({
        "tier": args.tier,
        "output_dir": str(args.output_dir),
        "files": sorted(outputs),
        "source_generator": str(GENERATOR_PATH.relative_to(ROOT)),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
