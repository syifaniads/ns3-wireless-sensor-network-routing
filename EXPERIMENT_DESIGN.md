# Experiment Design

## Goal
The project studies how routing strategy and traffic conditions affect Quality of Service in a simulated wireless sensor network.

## Retained design variables
The final report documents the following intended experiment dimensions:

| Variable | Values / description |
|---|---|
| Simulator | NS-3 |
| Wireless area | 2000 × 2000 m² |
| Mobility | Static |
| Routing | OLSR, AODV |
| Node count | 25, 50 |
| Packet size | 100 B, 1000 B |
| Number of sources | 1, 5 |
| Traffic pattern | CBR |
| Nominal data-rate choices | 2 Mbps, 5.5 Mbps |
| QoS metrics | Delay, jitter, packet loss |

## Retained complete numerical subset
The report preserves full QoS values for four **OLSR / 25-node** scenarios:

1. 100 B, 1 source
2. 100 B, 5 sources
3. 1000 B, 1 source
4. 1000 B, 5 sources

This subset is the basis of the numerical conclusions in this portfolio.

## Routing comparison intent
The report selected:
- **OLSR** to represent proactive routing.
- **AODV** to represent reactive routing.

The intent was to compare their behavior under different WSN loads. However, the retained report does not include a complete numerical AODV result table equivalent to the OLSR table. Therefore, this repository does not manufacture a protocol winner.

## Experimental reasoning
The four retained OLSR scenarios allow two direct comparisons:

### Source-count effect
Compare S1 vs S2 and S3 vs S4 while holding packet size constant.

### Packet-size effect
Compare S1 vs S3 and S2 vs S4 while holding the number of sources constant.

## What a stronger follow-up experiment would add
For a reproducible research-grade comparison, future work should retain:
- the exact NS-3 source files;
- simulator version;
- random seeds / run numbers;
- PHY and MAC configuration;
- propagation and loss models;
- offered traffic rate;
- simulation duration;
- source/destination placement;
- complete FlowMonitor output;
- routing overhead;
- throughput / packet delivery ratio;
- repeated runs and confidence intervals.

The current repository deliberately distinguishes the original design from these proposed improvements.
