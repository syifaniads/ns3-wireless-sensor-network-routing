# Reproducibility Notes

## Current status
This repository is an evidence-based reconstruction from the retained final report, not a complete executable reproduction of the original simulator workspace.

The uploaded report preserves:
- scenario definitions;
- four complete OLSR QoS result sets;
- OLSR trace excerpts;
- AODV trace excerpts;
- high-level simulation specifications.

The report does **not** preserve the complete original NS-3 source tree or all raw outputs.

## Minimum artifacts needed for full reproduction
A reproducible follow-up should retain:

```text
simulation/
├── wsn-routing.cc
├── scripts/
│   └── run-matrix.sh
├── config/
│   └── scenarios.csv
├── raw/
│   ├── traces/
│   └── flowmonitor/
├── processed/
│   └── qos-results.csv
└── plots/
```

## Parameters to pin
- NS-3 release/version
- compiler/toolchain
- RNG seed and run number
- node positions
- area size
- channel / propagation model
- Wifi PHY standard and actual data mode
- transmit power
- traffic interval / offered load
- source/sink mapping
- packet size
- simulation duration
- routing protocol

## Recommended experiment workflow
1. Encode each scenario as a parameter set.
2. Run OLSR and AODV with identical non-routing parameters.
3. Repeat each scenario with multiple deterministic seeds.
4. Export FlowMonitor data and routing-control counters.
5. Compute mean, standard deviation, and confidence intervals.
6. Preserve raw outputs separately from processed CSV.
7. Plot delay, jitter, packet loss/PDR, throughput, and routing overhead.

## Why this matters
A protocol comparison is only credible if workload and radio conditions are controlled. The current report is useful historical evidence, but this repository deliberately avoids claiming reproducibility beyond what the retained artifacts support.
