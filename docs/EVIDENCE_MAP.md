# Evidence Map

This document maps recruiter-facing statements to the strongest retained evidence in the final report.

| Claim | Evidence | Confidence |
|---|---|---|
| Project used NS-3 | Chapter IV states NS-3 implementation | High |
| OLSR was used | Routing-protocol section + OLSR trace headers | High |
| AODV was used | Routing-protocol section + AODV RREP trace headers | High |
| OLSR represented proactive routing | Project explanation of periodic HELLO/TC and pre-built routing tables | High |
| AODV represented reactive routing | Project explanation of RREQ/RREP/RERR | High |
| Four OLSR 25-node QoS scenarios were measured | Complete numerical scenario outputs | High |
| 100 B and 1000 B packets were tested in those OLSR runs | Scenario configuration blocks | High |
| 1 and 5 source workloads were tested | Scenario configuration blocks | High |
| Delay rose as concurrent-source load increased | S1→S2 and S3→S4 values | High for retained runs |
| Larger packet size raised delay | S1→S3 and S2→S4 values | High for retained runs |
| OLSR retained runs had 0% packet loss | Four scenario outputs | High for retained runs |
| 50-node experiments existed in the broader design | Specification; AODV trace references node index 48 | Medium |
| Complete 25-vs-50 QoS comparison | Not retained | Unsupported |
| 2-vs-5.5 Mbps performance comparison | Design says 2/5.5 Mbps, trace says DsssRate1Mbps | Conflicted / unsupported |
| OLSR outperformed AODV overall | No complete comparable AODV table retained | Unsupported |

## Evidence discipline
The portfolio uses three labels:

- **Verified numerically** — complete values are preserved.
- **Trace-verified** — protocol activity is visible in trace output.
- **Documented design** — experiment configuration appears in the report but full results are not retained.

Anything outside these categories is not presented as an implementation fact.
