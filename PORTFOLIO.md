# Portfolio Summary

## Project
**Wireless Sensor Network Routing Simulation — NS-3**

## One-line summary
Collaborative NS-3 simulation study of proactive OLSR and reactive AODV routing in a static wireless sensor network, with QoS evaluation using delay, jitter, packet loss, and packet-trace inspection.

## Portfolio owner
**Syifani Adillah Salsabila — Network Simulation Contributor**

This was a five-person academic project. The retained report verifies team membership but does not specify individual role ownership for every implementation artifact, so this repository avoids claiming sole authorship.

## Technical signals
- NS-3 network simulation
- Wireless multi-hop / ad-hoc networking
- OLSR proactive routing
- AODV reactive routing
- IEEE 802.11-style wireless simulation
- Constant Bit Rate traffic
- QoS measurement: delay, jitter, packet loss
- Packet-trace analysis
- Experimental design and workload comparison
- Evidence-driven technical documentation

## CV-ready bullets
- Collaborated on an **NS-3 wireless sensor network simulation** evaluating proactive **OLSR** and reactive **AODV** routing under varying traffic-load and packet-size conditions.
- Analyzed QoS using **delay, jitter, and packet loss**, with retained OLSR measurements ranging from `0.957 ms` to `20.244 ms` average delay as traffic intensity increased.
- Inspected NS-3 trace output to validate routing-control behavior, including **OLSR HELLO** messages and **AODV RREP** activity.
- Documented experimental limitations and separated numerically verified results from planned-but-incomplete comparisons to keep conclusions reproducible and defensible.

## Interview talking points
1. Why OLSR tends to have lower route-acquisition latency but incurs periodic control overhead.
2. Why AODV avoids continuous route updates but pays route-discovery cost on demand.
3. How more concurrent CBR sources can raise contention, queuing delay, and jitter.
4. Why larger packet sizes can increase per-hop transmission time.
5. Why `0% packet loss` in a limited simulation run is not evidence of universal reliability.
6. Why a mismatch between the written data-rate plan and trace output must be treated as an experiment-consistency issue.
7. How to improve the study: seed control, repeated runs, confidence intervals, FlowMonitor export, routing overhead, throughput, PDR, energy model, and automated plotting.

## Best-fit roles
- Network Engineer / NOC
- Infrastructure Engineer
- Network Research / Simulation
- IoT / Wireless Systems
- Cloud / Infrastructure Support roles requiring strong networking fundamentals
