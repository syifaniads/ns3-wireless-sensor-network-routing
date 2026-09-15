# Routing Protocols

## OLSR — proactive routing
OLSR keeps routing information available before an application needs to send data. In the project report, its behavior is described through four mechanisms:

1. **HELLO messages** discover neighbors and link state.
2. **Multipoint Relays (MPRs)** reduce redundant flooding by selecting relays that forward topology information.
3. **Topology Control (TC) messages** distribute topology information through the network.
4. Nodes build routing tables in advance so forwarding does not need a new route-discovery phase for every new flow.

### Why it was selected
The report motivates OLSR for a relatively dense static WSN and periodic CBR traffic because routes are maintained continuously and are ready when data must be sent.

### Retained trace evidence
The report includes NS-3 trace lines containing:

```text
ns3::olsr::PacketHeader
ns3::olsr::MessageHeader (type: HELLO ...)
```

This confirms that OLSR control traffic appeared in the retained simulation trace.

---

## AODV — reactive routing
AODV discovers a route only when one is needed. The report describes:

1. **RREQ (Route Request)** broadcast during route discovery.
2. **RREP (Route Reply)** returned when a destination or node with a route is reached.
3. Data forwarding after route creation.
4. **RERR (Route Error)** to signal a broken active route.

### Why it was selected
The report uses AODV as the reactive counterpart to OLSR: it avoids continuous routing updates when no data needs to be sent, but may incur route-discovery cost when communication starts.

### Retained trace evidence
The report includes trace lines containing:

```text
ns3::aodv::TypeHeader (RREP)
ns3::aodv::RrepHeader (...)
```

This is trace-level evidence that AODV route-reply processing occurred in the simulation.

---

## What this portfolio does not claim
The report does not retain a complete numerical AODV QoS table matching the four OLSR measurements. Therefore:

- no claim is made that OLSR is globally better than AODV;
- no claim is made that AODV is globally more efficient;
- no statistical ranking is presented;
- trace presence is not treated as a complete performance comparison.

A fair protocol comparison would require the same topology, seed policy, traffic workload, PHY/MAC configuration, simulation duration, and repeated measurements for both protocols.
