# Parallel execution of the exact stream

The scheduler retains the pinned Philox namespaces, ordinals and absolute
macrocycle numbers. Within each sweep it preserves the order of every pair
of updates sharing an affected plaquette. Disjoint updates commute because
each reads its own link and its affected fluxes and writes only those bytes.

For a local link at site \(x\) and orientation \(\mu\), use the rank
\(4(4x_0+3x_1+2x_2+x_3)+\mu\). At a plaquette with \(\mu<\nu\), let the
four links be \(A=(x,\mu)\), \(B=(x,\nu)\), \(C=(x+e_\mu,\nu)\) and
\(D=(x+e_\nu,\mu)\). Increasing rank and the serial link order give
\(A,B,D,C\) when neither shift wraps and \(C,A,B,D\) when only \(\mu\)
wraps. When only \(\nu\) wraps the order is \(D,A,B,C\). When both wrap
it is \(C,D,A,B\), with rank of \(D\) minus rank of \(C\) equal to
\((4(L-1)-1)(\nu-\mu)>0\). Reverse sweeps reverse these dependencies.

The line sweep retains the serial orientation order. Within an orientation
only transverse nearest neighbours can touch the same plaquette. Their
transverse coordinate sums preserve their original order including across
the periodic seam. Simultaneous updates share no affected plaquette.
Thread-local counters merge by integer sum and maximum. A failed worker
aborts the sweep and its enclosing stream.

The reader can assign orientation-local calculations to independent
processes. Each uses the same parser, arithmetic and outward interval
rounding. The controller reconstructs the reader output in the original
orientation order and checks state identity. At most one unacknowledged
frame per chain is outstanding. The independent replay verifies the same
control prefix and state digests.

The bound stream fixture compares the canonical native logs and full
reader ledgers across reference and parallel execution at \(L=16\) and
\(L=24\). Both paths replay their saved-state digests. The test uses
technical seeds and a scripted diagnostic decision.
