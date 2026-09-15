# QoS Metrics

## Delay
Average delay represents the time required for packets to travel from source to destination under the simulation's routing and wireless conditions.

In this portfolio, delay is reported exactly as preserved in the final report and expressed in milliseconds.

## Jitter
Jitter represents variation in packet delay. Lower jitter indicates more consistent packet arrival timing, while higher jitter can indicate variable queueing or contention.

## Packet loss
Packet loss is the fraction of transmitted packets that do not reach the destination. The four retained OLSR QoS runs report `0%` loss.

## Interpretation cautions
These metrics are sensitive to:
- node placement;
- number of sources;
- packet size;
- PHY/MAC settings;
- offered traffic rate;
- propagation model;
- routing protocol;
- simulation duration;
- random seed.

The retained report does not preserve every one of those parameters in enough detail for full independent reproduction. Therefore, the values are treated as verified historical experiment results rather than universal routing benchmarks.

## Useful additional metrics for future work
A stronger comparison could add:
- throughput;
- packet delivery ratio (PDR);
- routing overhead;
- route-discovery latency;
- convergence time;
- energy consumption;
- hop count;
- retransmissions;
- confidence intervals across repeated runs.
