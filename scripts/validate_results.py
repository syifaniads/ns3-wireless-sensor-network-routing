#!/usr/bin/env python3
"""Protect the retained WSN QoS dataset from accidental drift or overclaiming."""
from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "verified-results.csv"

EXPECTED = {
    "S1": {"packet": 100, "sources": 1, "delay": 0.957194, "jitter": 0.100327},
    "S2": {"packet": 100, "sources": 5, "delay": 5.27994, "jitter": 2.59068},
    "S3": {"packet": 1000, "sources": 1, "delay": 4.55978, "jitter": 0.106106},
    "S4": {"packet": 1000, "sources": 5, "delay": 20.2444, "jitter": 8.97887},
}


def close(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs(a - b) <= tol


def main() -> int:
    with DATA.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    if [r["scenario"] for r in rows] != list(EXPECTED):
        raise AssertionError("expected retained scenarios S1..S4 in order")

    for row in rows:
        scenario = row["scenario"]
        exp = EXPECTED[scenario]
        if row["protocol"] != "OLSR":
            raise AssertionError(f"{scenario}: retained numerical row must be OLSR")
        if int(row["nodes"]) != 25:
            raise AssertionError(f"{scenario}: expected 25 nodes")
        if int(row["packet_size_bytes"]) != exp["packet"]:
            raise AssertionError(f"{scenario}: packet-size drift")
        if int(row["sources"]) != exp["sources"]:
            raise AssertionError(f"{scenario}: source-count drift")
        if not close(float(row["avg_delay_ms"]), exp["delay"]):
            raise AssertionError(f"{scenario}: delay drift")
        if not close(float(row["avg_jitter_ms"]), exp["jitter"]):
            raise AssertionError(f"{scenario}: jitter drift")
        if float(row["packet_loss_percent"]) != 0.0:
            raise AssertionError(f"{scenario}: retained report records 0% packet loss")

    # Protect the evidence boundary: the numerical CSV intentionally contains
    # only OLSR rows. AODV evidence in this portfolio is trace-level only.
    if any(r["protocol"] == "AODV" for r in rows):
        raise AssertionError("do not add AODV numerical claims without retained measurements")

    print("WSN retained-result validation passed")
    print("- four OLSR/25-node scenarios match retained report values")
    print("- packet size and source-count matrix is intact")
    print("- delay/jitter values are unchanged")
    print("- all retained scenarios preserve 0% packet loss")
    print("- AODV remains trace-backed, not numerically overclaimed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
