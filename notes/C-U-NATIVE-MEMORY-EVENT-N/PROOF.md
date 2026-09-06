# Native protected record and fixed-reader boundary

Status: **NON-CANONICAL incubation; candidate-T; L1 only.** Issue #861.
This proof package works within the unchanged preregistration at
`9eef145d285325f2b3b48efcc740adf04d574632`. It creates no public claim status.

The retained public mathematical source is
`probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md` at public main
`5de2e71f4000e02599919bf3dcb18c7671b67445`. Its generator, synchronization,
five-label chart and QDD definitions are inherited explicitly. The authority
is Public Canon v78, with content commit
`767b136713ae12f5f30869642852dcb8a3f671b0`. Neither Canon nor source probe
changes in this incubation.

## Proposition and proof dependencies

1. On all 6250 synchronized checkpoints and both control bits,
   `V(next)=-V(x)`. The sign record `R={V,-V}` has 313 fibres: 312 of
   size 20 and one of size 10. These are exactly the strongly connected
   components of the native graph with either control bit allowed. Every
   invariant fixed checkpoint reader factors uniquely through R.
   [MEMORY-PROOF.md](MEMORY-PROOF.md), sections 1-2, proves this algebraically.

2. The frozen clock automaton has 100 reachable states, one strongly
   connected component and period one. Its exact fixed-origin letter
   frequencies are `1/150` for equal adjacent bits and `1/75` for unequal
   adjacent bits, for each fixed residue pair. Explicit connecting words,
   an integer primitive certificate and a contraction bound prove uniform
   dyadic-block convergence and then convergence along all prefix lengths.
   [CLOCK-PROOF.md](CLOCK-PROOF.md), sections 1-4, supplies the proof.

3. Pushing those frequencies through the inherited chart gives exactly the
   checkpoint and decorated atom multisets in CLOCK-PROOF.md, section 5,
   for all 3125 labels. In particular every point of the corresponding R
   fibre recurs with positive frequency along the actual native orbit.
   Hence a fixed checkpoint reader that is eventually constant was already
   constant throughout its synchronized orbit. This excludes a permanent
   blank-to-written transition after synchronization in that frozen class.

4. [FREQUENCY-PROOF.md](FREQUENCY-PROOF.md) classifies every fixed reader by
   whole-atom partitions, proves the complete integer allocation spectra,
   and derives the exact accepted-event rational sets. On a nonzero record
   they are all rationals in [0,1] with reduced denominator at most 60;
   on the zero record the bound is 30. Restricting to either driver bit
   gives bounds 30 and 15 respectively. Empty acceptance is UNDEFINED.
   This statement is per orbit and makes no simultaneous-reader claim.

5. A target-independent static encoding realizes all 313 invariant messages.
   It is a preparation, not a native writing mechanism. R does not recover
   the QDD head record lost in native mergers and does not even determine
   the current QDD weight on a synchronized fibre. MEMORY-PROOF.md,
   sections 5-6, proves both distinctions with exact witnesses.

6. Only after classifying the native reader sets is comparison made with the
   inherited QDD target weights. The supported weight 1/256 is outside every
   accepted-event set above. Therefore the complete restricted reader class
   cannot realize the entire supported QDD target law. This is a boundary
   theorem for the frozen class, not a negative closure of the complete
   physical apparatus, decoder or sampling question.

## Audit and falsifiers

The companion exact verifier exhausts finite native states, both bits,
clock states, all chart labels, all supported piston heads and all whole-atom
allocations. It also audits the frozen ordinary and enormous clock times.
The large-time samples audit the algebraic chart proof; they do not prove
the universal frequency result. The output must report disagreements even
if the main positive conjecture fails. Incomplete computation or an
implementation defect is STOP and is documented without changing the
scientific scope or thresholds.

The proofs were developed collaboratively in this session, with a separately
written mathematical audit. This is not blind independent confirmation.
The code is committed and pushed before recorded execution. RUN.md records
that distinct code pin, exact bytes, environment, exit status and stderr.
The original preregistration is not rewritten.

No physical event, system/apparatus coupling, selected context, reset law,
realization certificate, or L1-to-L5/L6 bridge is supplied here.
QDD-INSTRUMENT-APPARATUS and its physical children remain open.
