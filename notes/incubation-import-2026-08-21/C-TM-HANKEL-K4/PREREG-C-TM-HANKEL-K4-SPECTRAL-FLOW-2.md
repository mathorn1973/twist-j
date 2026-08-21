# PREREG C-TM-HANKEL-K4-SPECTRAL-FLOW-2

```text
CANDIDATE:    C-TM-HANKEL-K4-SPECTRAL-FLOW-2
STATUS:       incubation candidate, NO AUTHORITY, promotes nothing
PUBLIC BASIS: Public Canon v43, main 981aa1b9c8bc7ecd084346e099f014f3fc78847c
              tag canon-v43, re-read at freeze time
PARENT:       C-TM-HANKEL-K4-SUBSTRATE-1 (candidate, this project); its
              frozen substrate, cell order, and canonical 109-entry
              S_4-invariant map are consumed unchanged
LAYER:        L1 only. One session per candidate; this document claims the id.
```

## The frozen question

Which minimal S_4-invariant information distinguishes the two nonbalanced
endpoint inertias NEG 7 ZERO 0 POS 9 and NEG 9 ZERO 0 POS 7 on the frozen
k = 4 substrate?

The owner directive shaping this freeze: the missing bit after the k = 4
determinant collapse is not whether a crossing happened but which way the
eigenvalue passed through zero. The second cut therefore targets oriented
spectral flow, not another determinant.

## Convention, frozen

For the pencil K(s) = Kxor + sR on 0 <= s <= 1, an eigenvalue crossing
zero upward as s grows counts +1. With sigma = POS - NEG, the net flow is
SF = (sigma(K(1)) - sigma(K(0)))/2. On the extremal locus sigma(K(0)) = 0,
so profile NEG 7 ZERO 0 POS 9 forces SF = +1 and NEG 9 ZERO 0 POS 7 forces
SF = -1. The pencil gates verify that the crossing-resolved walk realizes
these endpoint values.

## Frozen input: the seventeen real failures

Consumed as exact input from the parent candidate's recon (extremal
quadruples, n <= 4.10^9, every inertia by two independent exact paths).
Completeness of this list at its bound is a recon statement, not a gate
here; each row is re-verified from scratch by the verifier.

```text
 377931745 = 5.23.839.3917      7 0 9
 548309857 = 17.23.53.26459     7 0 9
 689952085 = 5.71.317.6131      9 0 7
1001207365 = 5.23.53.164267     7 0 9
1436418609 = 3.23.503.41387     7 0 9
1477310605 = 5.29.53.192233     7 0 9
1486919065 = 5.23.797.16223     9 0 7
1732991217 = 3.71.347.23447     7 0 9
1992609343 = 29.113.461.1319    9 0 7
2102641715 = 5.23.2791.6551     7 0 9
2388719185 = 5.101.509.9293     7 0 9
2392518595 = 5.71.1013.6653     7 0 9
2515579015 = 5.53.1559.6089     9 0 7
2843975361 = 3.71.467.28591     7 0 9
3158792005 = 5.83.89.85523      7 0 9
3174899015 = 5.53.1013.11827    7 0 9
3512837065 = 5.101.293.23741    9 0 7
```

Correction recorded against the parent record's prose: the smallest found
failing extension of {5,101,293} has n = 3512837065; the parent record
stated 3513053065 by an arithmetic slip in reporting, with the correct
prime set. The parent doc is amended, not silently.

## Field 1. EQUATION (gates, in the owner's order)

```
G1  CROSSINGS. For each of the seventeen: certify extremal; endpoint
    inertias by three independent exact paths (fraction-free minors,
    characteristic polynomial, rational symmetric congruence); skeleton
    endpoint NEG 8 ZERO 0 POS 8; det(Kxor + sR) interpolated exactly at
    the seventeen integer nodes; squarefree part; every root in (0,1)
    isolated into disjoint rational intervals; the number of multiple
    roots in (0,1) determined exactly from gcd(f, f').
G2  ORIENTED FLOW. Inertia of the scaled integer pencil at rational
    sample points separating the isolated roots; ZERO = 0 at every
    sample; per-crossing orientation = drop in NEG across the isolating
    interval; SF = sum of orientations; gates: SF = sigma(K(1))/2, equal
    to +1 on profile 7 0 9 and -1 on profile 9 0 7; crossing count
    congruent to SF mod 2; multiple-root count 0 or honestly reported
    with the walk still consistent. The full crossing and orientation
    table is printed for all seventeen.
G3  MODULE. The frozen 65-cell substrate as an S_4-module: permutation
    character computed from the cell action; multiplicities by exact
    character inner products equal to 10, 12, 5, 3, 0 for [4], [31],
    [22], [211], [1111]; dimension identity 65; ranks of the five
    unnormalized isotypic operators sum_g chi_lambda(g) g equal to
    10, 36, 10, 9, 0 by exact integer elimination. The [1111] sector is
    absent: no pure sign channel exists on this substrate.
G4  SECTORS ON THE REALS. The canonical invariant layers of the parent
    freeze, sliced by sector: sums10 (trivial), gram31 (78), gram22
    (15), gram211 (6), full109. For each layer, report whether the two
    flow classes are separated on the seventeen (no equal-layer pair
    with opposite flow). Descriptive; a mixed layer fires nothing.
G5  COLLISION SEARCH. On the frozen abstract domain of Field 3, among
    tables whose endpoint profile is one of the two frozen profiles
    (for which net flow is the endpoint signature half), bucket each
    layer and report the first collision pair with opposite flow, or
    that none exists in the domain. A collision falsifies that layer as
    the carrier of orientation. Both flows must be present in the pool.
G6  SUFFICIENCY. Reserved and UNREACHABLE here: no sufficiency statement
    of any layer may be made by this candidate at any search size.
```

The invariant layers are constructed from the S_4 module alone (they are
the parent's canonical map, frozen before the seventeen existed). The
seventeen enter only as evaluation points, never as construction input.

## Field 2. CODE

`verify_tm_hankel_k4_spectral_flow_2.py`, assembled from the parent's
pinned machinery plus the new pencil and module gates, hash recorded after
this file freezes. Python standard library only; exact integer and
Fraction arithmetic; no float anywhere; deterministic stdout; environment
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC. Two
platforms, byte-identical stdout: Ubuntu 24.04 x86_64 and Debian 13
aarch64.

## Field 3. CARRIER AND DATA

No external data, no network, no randomness. Abstract search domain,
frozen: the same 64-bit LCG recurrence as the parent (multiplier
6364136223846793005, increment 1442695040888963407, x_0 = 1), tables
2000..5999 of the stream (the first 4000 steps are discarded, then 4000
tables built exactly as in the parent); plus one expansion round of
single-cell flips over the first 200 pool members in ascending table
order, seeded by the found two-profile tables and the parent's abstract
witness 0x02e639472cd318ed2; plus the seventeen real sign tables as
evaluation points. Tables outside the two frozen profiles are discarded.

## Field 4. SYSTEMATICS

```
S1  polarization: t(1) = -1 fixed, as in the whole lane.
S2  scope: gates quantify only over the seventeen reals and the declared
    finite abstract domain; the word every never ranges over the 2^65
    substrate.
S3  independence: endpoint inertias by three paths; walk inertias by two
    paths; a break attempt with independent code follows the run.
S4  the flow convention is fixed above; the opposite convention negates
    every SF and swaps the two profiles coherently.
```

## Field 5. FAILURE THRESHOLD

Zero tolerance: any FAIL line fires the candidate. G1 and G2 fire on any
path disagreement, endpoint mismatch, inconsistent walk, or a profile
outside the two frozen ones among the seventeen. G3 fires on any deviation
from 10, 12, 5, 3, 0 and 10, 36, 10, 9, 0. G4 and G5 outcomes are
findings and cannot fire except on recomputation failure. A verifier
defect is an integrity STOP; the candidate is then dead under this id and
a successor uses a new name. No threshold moves after this freeze.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 throughout. Recorded as owner hypotheses, NOT gates of this
candidate: [H] the orientation lives in a new irreducible four-prime
component, prime candidate the [22] sector; [H] a decoder reading would
prohibit an orientation of spectral flow rather than force positivity.
Neither is evaluated as a claim here. Not claimed: sufficiency of any
layer; irrelevance of any sector beyond the searched domain; any census
over the substrate; anything about zeta zeros, the Riemann hypothesis,
Weil positivity, explicit formulae, the infinite operator beyond finite
compressions, J, p = 5, decoder, measure, physical readings, or L2-L6
lifts. No registry row, no status movement.
