# PREREG - C-PHOTON-R3-FINITE-DIAGNOSTIC-N

**Status:** PUBLIC, NON-CANONICAL DIAGNOSTIC ONLY. ZERO evidential weight.
**Owner:** A. M. Thorn / photon-r3-finite-diagnostic-20260927
**Date:** 2026-09-27
**Issue:** #1202
**Authority:** Public Canon v92. No normative file changes.

## Purpose

This is not a scientific finite-size probe. It is a route-selection diagnostic
for the sufficient quantity

\[
R_3(L)=\frac1{4L^4}
E_{\rm aug}\sum_K M_K^4.
\]

The only question is whether the already-derived \(R_3\) route looks grossly
stable or grossly growing between the two small volumes for which the exact
dual mobility wrapper has already passed its own engineering qualification.

No theorem may be inferred from either terminal.

## Frozen sampler dependency

Import exactly

\`probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/mobility_kernel.py\`

from current public main, without editing it.

That module loads the immutable legacy dual kernel under its own SHA-256
custody and defines the exact \(\pi_L(n)\propto2^{-|{\rm supp}\,n|}\)
mobility chain on the hard ternary closed-surface target.

This diagnostic consumes its transition law only. It does not inherit the
scientific status of another probe.

## Frozen chain table

For each \(L\in\{3,4\}\), run exactly four chains:

\[
\begin{array}{c|c|c}
{\rm label}&{\rm start}&{\rm seed}\\
\hline
L3\_cold\_r1&cold&0xd120203000000000000000000000101\\
L3\_cold\_r2&cold&0xd120203000000000000000000000102\\
L3\_witness\_r1&witness&0xd120203000000000000000000000201\\
L3\_minus\_r1&minus\_witness&0xd120203000000000000000000000301\\
L4\_cold\_r1&cold&0xd120204000000000000000000000101\\
L4\_cold\_r2&cold&0xd120204000000000000000000000102\\
L4\_witness\_r1&witness&0xd120204000000000000000000000201\\
L4\_minus\_r1&minus\_witness&0xd120204000000000000000000000301
\end{array}
\]

Per chain:

- warmup: 4096 exact mobility transitions;
- samples: 256;
- transitions between samples: 64;
- validate the exact hard state after warmup and after every 32nd saved sample.

No adaptive extension is allowed after seeing output.

## Frozen augmentation

For every saved surface state \(n\), create one exact auxiliary matching draw.

Use a separate \`BitStream\` with domain

\`b"r3diag1202-aug"\`

and seed equal to the chain seed XOR

\[
{\tt 0x5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a5a}.
\]

At each occupied lattice edge compute all incident faces with principal signed
incidences.

Allowed cases must be exactly:

- neutral: signed sum zero and equal positive/negative counts;
- charged: degree five, signed sum \(+5\) or \(-5\), all five incidences aligned.

At every neutral edge with \(r\) positive and \(r\) negative faces, sort both
face-index lists and draw a uniform random permutation of the negative list by
exact Fisher-Yates using \`BitStream.bounded\`. Pair corresponding entries.

At a charged edge union all five incident faces.

The transitive closure of these links is the exact sampled augmentation.

For each augmented component K count

\[
M_K=\#\{\text{charged lattice edges owned by }K\}.
\]

Neutral components with \(M_K=0\) are retained in connectivity but contribute
zero to the current observables.

## Saved integer observables

For every saved state/matching draw record internally:

- \(C=\sum_KM_K\), total number of charged edges;
- \(M_{\max}=\max_KM_K\), with zero if no charge;
- \(S_4=\sum_KM_K^4\).

The exact per-sample diagnostic is

\[
R_{3,\rm sample}=\frac{S_4}{4L^4}.
\]

No floating point is needed for the decision. Chain and pooled means are
\`Fraction\` values.

## Frozen mobility guard

For each chain record:

- the number of distinct exact current hashes seen among the 256 saved states;
- the number of sample-to-sample changes in total charged-edge count C.

The chain passes the diagnostic mobility guard iff

\[
{\rm distinct\ current\ hashes}\ge16
\]

and

\[
{\rm C\ changes}\ge16.
\]

These are diagnostic guards only, not mixing-time theorems.

## Frozen start-overlap guard

At fixed L define:

- cold range = min/max of all 512 sample R3 values from the two cold chains;
- charged-start range = min/max of all 512 sample R3 values from the witness
  and minus-witness chains.

The start-overlap guard passes iff these two closed rational intervals
intersect.

## Frozen pooled means and terminal

Pool all 1024 samples at each L. Let

\[
\bar R_3(3),\qquad \bar R_3(4)
\]

be the exact pooled means.

Allowed terminals:

### STABLE-DIAGNOSTIC

All eight chains pass the mobility guard, both L values pass the start-overlap
guard, and

\[
\bar R_3(4)\le2\bar R_3(3).
\]

### GROWTH-DIAGNOSTIC

All eight chains pass the mobility guard and

\[
\bar R_3(4)\ge4\bar R_3(3)>0.
\]

### INCONCLUSIVE

Every other outcome.

If \(\bar R_3(3)=0\), only INCONCLUSIVE is allowed unless both pooled means are
zero, which also remains INCONCLUSIVE.

The factors 2 and 4 are frozen route-selection thresholds, not scientific
falsifiers.

## Reporting firewall

The result may report exact finite-volume sample statistics and one of the
three terminal strings.

It may not claim:

- bounded or divergent \(R_3\) as \(L\to\infty\);
- a scaling exponent;
- a thermodynamic limit;
- bounded \(\Xi_L\);
- \(P1\);
- a massless phase or physical photon.

## Repository boundary

After this preregistration is committed and publicly read back, one new script
\`diagnostic.py\` may be added under this package and executed once.

Result files may then record the frozen output. No existing sampler, Canon,
Registry, Frontier, probe, gate, tool, workflow or release file may be edited.
