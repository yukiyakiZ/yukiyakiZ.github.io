---
layout: post
title: "A Cherry-pick of the Vast Collection of Packet Scheduling Algorithms"
excerpt: ""
categories: [network]
comments: true
---

<p class="lead text-justify">
Packet scheduling is essentially a decision making process.
Below is a subset of typical packet scheduling algorithms, highlighted by the common denominators: metadata leveraged to support the decision,
the logic of the decision, and the feature(s).
</p>
<p class="lead text-justify">
The summary focuses on the Dequeue interface, neglecting the Enqueue interface and possible Active Queue Management (AQM).
Hopefully, it could help to obtain a fast overview of the characteristics of the canonical packet scheduling algorithms.
For further details, there are papers illuminating insights on the abstractions of scheduling policies/queueing disciplines, e.g.,
<a href="https://cs.nyu.edu/~anirudh/pifo-sigcomm.pdf">Programmable Packet Scheduling at Line Rate</a>.
</p>

<h5>First In First Out (FIFO)/First Come First Serve (FCFS)</h5>
<ul class="lead text-justify">
<li>
    Metadata: the packet's time of arrival
</li>
<li>
    Logic: advance the packet with the earliest arrival
</li>
<li>
    Feature: work-conserving; also known as Drop Tail if combined with a simple if-full-then-drop buffer management policy
</li>
</ul>

<h5>Strict Priority (SP)</h5>
<ul class="lead text-justify">
<li>
    Metadata: the packet type of service field or features to support a more complex service differentiation method
</li>
<li>
    Logic: advance the packet belonging to the service of top priority (after classification); FIFO is applied to packets with the same priority
</li>
<li>
    Feature: work-conserving
</li>
</ul>

<h5>Stochastic Fair Queueing (SFQ)</h5>
<ul class="lead text-justify">
<li>
    Metadata: the session information (e.g., source/destination IP, source/destination port, protocol)
</li>
<li>
    Logic: leverage a perturbed hash function to map the packets into limited number of FCFS queues and apply a bit-by-bit round robin
</li>
<li>
    Feature: limited number of queues to maintain which is of low cost; suitable for high-speed routers
</li>
<li>
    Literature: <a href="http://www2.rdrop.com/~paulmck/scalability/paper/sfq.2002.06.04.pdf">􏰆Stochastic Fair Queueing􏰍􏰘􏰝􏰟􏰗􏰒􏰝􏰞􏰛􏰜􏰊􏰚􏰊􏰙􏰗􏰘􏰕􏰖􏰔􏰏􏰍􏰓􏰈􏰒􏰐􏰑􏰅􏰏􏰍􏰎􏰁􏰌􏰊􏰋􏰈􏰉􏰇􏰄􏰅􏰆􏰃</a>
</li>
</ul>

<h5>Shortest Job First (SJF)</h5>
<ul class="lead text-justify">
<li>
    Metadata: flow size
</li>
<li>
    Logic: similar to the equivalence in OS, SJF advances the flow with minimum flow size
</li>
<li>
    Feature: work-conserving; assume the flow size is known
</li>
</ul>

<h5>Earliest Deadline First (EDF)</h5>
<ul class="lead text-justify">
<li>
    Metadata: the deadline for the flow
</li>
<li>
    Logic: advance the packet with the minimum deadline
</li>
<li>
    Feature: work-conserving; assume the deadline of the flow is encoded in the packet field
</li>
</ul>

<h5>Shortest Remaining Process Time</h5>
<ul class="lead text-justify">
<li>
    Metadata: the remaining flow size
</li>
<li>
    Logic: advance the packet belong to the flow with minimum remaining flow size
</li>
<li>
    Feature: work-conserving; optimal in terms of minimizing flow completion time (in a single link)
</li>
<li>
    Literature: <a href="https://web.stanford.edu/~skatti/pubs/sigcomm13-pfabric.pdf">pFabric</a>
</li>
</ul>

<h5>Start Time Fair Queueing (STFQ)</h5>
<ul class="lead text-justify">
<li>
    Metadata: the virtual starting time maintained by the scheduler
</li>
<li>
    Logic: advance the packet with the minimum virtual starting time; update the value upon each Dequeue
</li>
<li>
    Feature: work-conserving
</li>
<li>
    Literature: <a href="http://ccr.sigcomm.org/archive/1996/papers/goyal.pdf">Start-time Fair Queuing</a>
</li>
</ul>

<h5>Hierarchical Packet Fair Queueing (HPFQ)</h5>
<ul class="lead text-justify">
<li>
    Metadata: hierarchical link-sharing model
</li>
<li>
    Logic: allocate bandwidth based on the hierarchical link-sharing model, extending fair-queueing algorithms
</li>
<li>
    Feature: guarantee bandwidth allocation for leaf classes and offer a more flexible resource management capability;
    an extension of it is the
    <a href="http://conferences.sigcomm.org/sigcomm/1997/papers/p011.pdf">Hierarchical Fair Service Curve (HFSC)</a>.
</li>
<li>
    Literature: <a href="https://www.cs.cmu.edu/~hzhang/papers/TON-97-Oct.pdf">Hierarchical Packet Fair Queueing Algorithms</a>
</li>
</ul>

<h5>Round Robin (RR)/Weighted Round Robin (WRR)</h5>
<ul class="lead text-justify">
<li>
    Metadata: a pointer of previous scheduled FIFO queue; with WRR, an array of weights is applied for scheduling decision as well
</li>
<li>
    Logic: classify the packets into a per-flow queue and schedule each queue in a circular fashion
</li>
<li>
    Feature: work-conserving; approximate the bit-by-bit round robin or Generalized Processor Sharing (GPS) with packet-level "fairness";
    memory inefficient due to the cost of maintenance
</li>
<li>
    Literature: <a href="http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-shenker.pdf">Analysis and Simulation of a Fair Queueing Algorithm</a>,
    <a href="http://www.cs.columbia.edu/~ricardo/misc/docs/gps.pdf">A Generalized Processor Sharing Approach
to Flow Control in Integrated Services
    Networks: The Single-Node Case</a>
</li>
</ul>

<h5>Deficit Round Robin (DRR)</h5>
<ul class="lead text-justify">
<li>
    Metadata: a quantum that is added to the deficit of each queue
</li>
<li>
    Logic: track the credits for each flow and send the packet that fits the flow's deficit
</li>
<li>
    Feature: work-conserving/non-work-conserving variants; approximate the bit-by-bit round robin;
    memory inefficient due to the cost of maintenance
</li>
</ul>

<h5>Token/leaky Bucket</h5>
<ul class="lead text-justify">
<li>
    Metadata: the number of tokens per step/constant leaky rate
</li>
<li>
    Logic: for the token packet (with the limited size of tokens), the packet will be forwarded only if there are enough tokens;
    for the leaky bucket, packets are always queued (and might be dropped due to constraint size) on the bucket and
    the bucket strives for a constant fixed rate service;
</li>
<li>
    Feature: conduct traffic shaping/rate-limiting; non-work-conserving; token bucket can be of variable rate while leaky bucket constant rate;
    token bucket throws away tokens but not packets while leaky packet discards packets when the bucket is full
</li>
</ul>

<h5>Least Slack-Time First (LSTF)</h5>
<ul class="lead text-justify">
<li>
    Metadata: the slack value
</li>
<li>
    Logic: slacking initialization at network edges and slack modification (deduced by queueing time) at the network core;
    the packet with the minimum slack value is prioritized for scheduling
</li>
<li>
    Feature: slack value encodes the concept of path history of the packet; slack initialization is flexible
</li>
<li>
    Literature: <a href="https://link.springer.com/article/10.1007/BF01553887">A New Algorithm for Scheduling Periodic, Real-Time Tasks</a>,
    <a href="https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-mittal.pdf">Universal Packet Scheduling</a>
</li>
</ul>