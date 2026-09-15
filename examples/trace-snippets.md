# Representative Trace Snippets

The following excerpts are intentionally short summaries of the retained trace evidence. They are included to show the protocol headers observed in the report without republishing pages of raw output.

## OLSR HELLO

```text
t ... /NodeList/3/.../Tx DsssRate1Mbps
...
ns3::olsr::PacketHeader
ns3::olsr::MessageHeader (type: HELLO TTL: 1 ...)

r ... /NodeList/2/.../RxOk
r ... /NodeList/4/.../RxOk
r ... /NodeList/8/.../RxOk
```

Interpretation: an OLSR HELLO control packet was transmitted and received by multiple neighboring nodes.

## AODV RREP

```text
t ... /NodeList/48/.../Tx DsssRate1Mbps
...
ns3::aodv::TypeHeader (RREP)
ns3::aodv::RrepHeader (...)

r ... /NodeList/41/.../RxOk
r ... /NodeList/47/.../RxOk
```

Interpretation: the retained AODV trace contains Route Reply activity in a simulation referencing node index 48.

## Important note
These excerpts are evidence of protocol behavior only. They are not used to calculate routing overhead or a complete QoS comparison because the full raw trace files are not part of the retained portfolio source.
