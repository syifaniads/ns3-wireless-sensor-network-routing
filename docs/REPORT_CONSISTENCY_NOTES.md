# Report Consistency Notes

This portfolio does not silently reconcile inconsistencies in the retained final report.

## 1. Intended data rate vs trace data mode
The simulation specification lists **2 Mbps / 5.5 Mbps** as data-rate choices. However, retained packet traces show:

```text
DsssRate1Mbps
```

Because those two pieces of evidence do not match, this repository does not present a validated 2-vs-5.5 Mbps comparison.

## 2. Planned comparisons vs completed numerical output
The report structure proposes analysis by:
- data rate;
- 25 vs 50 nodes;
- 1 vs 5 sources;
- packet size;
- OLSR vs AODV.

The complete numerical QoS output retained in the report covers four OLSR / 25-node cases varying source count and packet size. The other comparison headings do not contain an equivalent complete result matrix.

## 3. AODV evidence type
AODV is supported by routing-protocol documentation and packet-trace output containing RREP messages. This proves protocol activity, but it is not sufficient to infer a numerical QoS ranking against OLSR.

## 4. 50-node evidence
The written specification includes 50 nodes, and an AODV trace references `NodeList/48`, which is consistent with a larger simulation. However, the report does not retain a complete 50-node QoS table.

## Portfolio treatment
Rather than hiding these gaps, the repository explicitly marks each claim as:
- numerically verified;
- trace-verified;
- documented experiment design;
- unsupported by retained evidence.

This approach is intentional: technical credibility is more valuable than filling missing report sections with assumptions.
