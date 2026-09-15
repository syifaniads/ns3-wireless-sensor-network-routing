# Verified Results

## Retained OLSR measurements

| Scenario | Nodes | Packet size | Sources | Avg. delay (ms) | Avg. jitter (ms) | Packet loss |
|---|---:|---:|---:|---:|---:|---:|
| S1 | 25 | 100 B | 1 | 0.957194 | 0.100327 | 0% |
| S2 | 25 | 100 B | 5 | 5.27994 | 2.59068 | 0% |
| S3 | 25 | 1000 B | 1 | 4.55978 | 0.106106 | 0% |
| S4 | 25 | 1000 B | 5 | 20.2444 | 8.97887 | 0% |

## Pairwise observations

### S1 → S2: more simultaneous sources
With packet size fixed at 100 B, raising active sources from 1 to 5 increased:
- delay by about **5.52×**;
- jitter by about **25.82×**.

The report attributes this to higher contention and queueing when several sources transmit concurrently.

### S1 → S3: larger packets
With one source, raising packet size from 100 B to 1000 B increased delay by about **4.76×**. Jitter changed only slightly (`0.100327 ms` → `0.106106 ms`).

The report interprets this as longer transmission time per hop without the extra contention introduced by multiple sources.

### S3 → S4: larger packets plus more sources
For 1000-byte packets, moving from 1 source to 5 sources increased:
- delay by about **4.44×**;
- jitter by about **84.62×**.

This was the highest-load retained OLSR case and also the case with the highest delay and jitter.

## Packet-loss observation
All four retained OLSR runs report **0% packet loss**. This demonstrates successful delivery in those specific runs only. It should not be generalized into a claim that OLSR is lossless.

## What cannot be concluded from the retained report
The report does not preserve enough complete numerical output to support:
- a rigorous OLSR-vs-AODV winner;
- a full 25-vs-50 node comparison;
- a full 2-vs-5.5 Mbps comparison;
- confidence intervals or statistical significance;
- throughput or packet-delivery-ratio ranking.

See [LIMITATIONS.md](LIMITATIONS.md) for the evidence boundary.
