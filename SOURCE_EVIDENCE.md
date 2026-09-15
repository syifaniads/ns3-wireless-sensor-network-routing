# Source Evidence

## Primary source
The primary evidence for this portfolio is the team's final academic report:

**`FINAL PROJECT_JARINGAN SENSOR NIRKABEL-A_2026.pdf`**

The raw PDF is intentionally not republished in this public repository because it contains student identification numbers and course-submission formatting that are unnecessary for recruiter review.

## Evidence map by report section

| Portfolio claim | Source area in report |
|---|---|
| Five-person team roster | Cover page |
| NS-3 simulation | Chapter IV, section 4.1 |
| OLSR as proactive routing | Section 4.2 / 4.2.1 |
| AODV as reactive routing | Section 4.2 / 4.2.2 |
| 25/50 node design | Simulation specification section |
| 100/1000-byte packets | Simulation specification + QoS scenarios |
| 1/5 sources | QoS scenario descriptions |
| Delay / jitter / packet-loss metrics | QoS analysis section |
| OLSR scenario values | Section 4.3.5.1–4.3.5.4 |
| OLSR HELLO trace | Section 4.5 trace excerpts |
| AODV RREP trace | Section 4.5.4 trace excerpt |
| 2 / 5.5 Mbps nominal design | Simulation specification |
| `DsssRate1Mbps` trace discrepancy | Retained NS-3 trace excerpts |

## Evidence hierarchy used in this repository

### Level A — numerically verified
A value is explicitly preserved in the report, e.g.:
- `0.957194 ms` average delay for OLSR / 25 nodes / 100 B / 1 source;
- `20.2444 ms` average delay for OLSR / 25 nodes / 1000 B / 5 sources.

### Level B — trace verified
Protocol activity is directly visible in retained trace output, e.g.:
- OLSR `HELLO`;
- AODV `RREP`.

### Level C — documented design
A configuration is specified by the report, but complete comparable result output is not retained, e.g.:
- 25 vs 50 node comparison;
- 2 vs 5.5 Mbps data-rate comparison.

### Level D — not claimed
Claims that would require missing evidence are explicitly excluded, including a statistically supported OLSR-vs-AODV performance winner.

## Future source recovery
If the original NS-3 source code, trace files, FlowMonitor XML, CSV exports, or plotting scripts are recovered, they should be added under a provenance-preserving folder with documentation of where they came from and who authored them when known.
