# Trace Analysis

## Why packet traces matter
Summary QoS metrics show end results, while NS-3 trace excerpts expose protocol activity at packet level. The retained report includes trace lines for both OLSR and AODV.

## OLSR trace evidence
Representative fields preserved in the report include:

```text
/ns3::WifiNetDevice/Phy/State/Tx
ns3::Ipv4Header (... protocol 17 ...)
ns3::UdpHeader (...)
ns3::olsr::PacketHeader
ns3::olsr::MessageHeader (type: HELLO ...)
```

The same OLSR HELLO packet is shown being received by multiple neighboring nodes (`RxOk`). This is consistent with proactive neighbor discovery/control dissemination.

### What can be verified
- OLSR packet headers exist in the trace.
- HELLO control messages are present.
- broadcast destination MAC `ff:ff:ff:ff:ff:ff` appears in the retained excerpt.
- multiple nodes receive the routing-control transmission.

### What is not derived from the excerpt alone
- total routing overhead;
- MPR selection efficiency;
- full routing convergence time;
- packet delivery ratio across the complete simulation.

## AODV trace evidence
Representative AODV fields include:

```text
ns3::aodv::TypeHeader (RREP)
ns3::aodv::RrepHeader (...)
```

The retained excerpt includes transmit and receive activity for RREP packets and references nodes including `NodeList/48`, showing that AODV activity was captured in a larger-node run.

### What can be verified
- AODV route-reply packets appear in the trace.
- multiple nodes receive AODV control traffic.
- a simulation containing node indices up to at least 48 generated trace output.

### What is not safe to infer
- that all 50 intended nodes were simultaneously active traffic participants;
- that AODV outperformed OLSR;
- exact route-discovery latency;
- control-message totals.

## Trace interpretation principle
This repository treats trace excerpts as **protocol-behavior evidence**, not as a substitute for complete QoS datasets. Numerical performance claims are restricted to measurements explicitly preserved in the final report.
