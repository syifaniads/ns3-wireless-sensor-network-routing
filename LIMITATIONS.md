# Limitations

This repository is intentionally conservative about what the retained academic report can prove.

## 1. Incomplete OLSR-vs-AODV numerical comparison
The report explains both protocols and includes traces for both, but the complete QoS table is preserved only for four OLSR scenarios. Therefore, no protocol winner is claimed.

## 2. Partial 25-vs-50 node evidence
The experiment design includes 25 and 50 nodes, and AODV trace output references node indices up to `NodeList/48`. However, the final report does not retain complete, directly comparable QoS results for both node counts.

## 3. Data-rate inconsistency
The written specification lists nominal data-rate choices of **2 Mbps / 5.5 Mbps**, but retained trace excerpts show `DsssRate1Mbps`. This mismatch prevents a defensible 2-vs-5.5 Mbps performance claim.

## 4. Missing original simulation source
The uploaded report does not contain the full original NS-3 `.cc` source, configuration scripts, or complete `.tr` files. The public portfolio therefore documents the experiment and retained evidence rather than pretending to be a fully reproducible source release.

## 5. No repeated-run statistics
The report gives single retained measurements rather than repeated runs with random-seed control, mean/variance, or confidence intervals. Results should be read as scenario observations, not statistical guarantees.

## 6. Limited metric set
The retained QoS metrics are delay, jitter, and packet loss. The report does not preserve complete values for:
- throughput;
- packet delivery ratio;
- routing overhead;
- energy consumption;
- convergence time;
- retransmission count.

## 7. Static topology
The experiment specification uses a static mobility model. Conclusions therefore do not directly generalize to mobile MANET/WSN conditions.

## 8. Packet loss interpretation
All four retained OLSR runs report 0% packet loss. This is not evidence that OLSR is inherently lossless; it is only the observed result for those specific simulation runs.

## 9. Team-level artifact
This was collaborative coursework. The report verifies the team roster but does not map every code/configuration artifact to a specific individual. This repository does not claim sole authorship.
