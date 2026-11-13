# PREREG P-METRO-ENC4-CLOSURE-1

- Public lock [#1984](https://github.com/mathorn1973/twist-j/issues/1984)
- Owner item METRO-ADMISSIBILITY-DIM [O], common ENC4 portion
- Action layer L5 raw stream to candidate L6 tagged aggregate
- Source Public Canon v111, public main f390a3ada72892afa5b73e6f07990dc4ab129dfb
- Canon content 0f4a0fb4100eced68fe17d802062b74b9b9caa4e
- Canon SHA-256 9a9f80571f4fbfe50dbfda1bf0e8d7e46e3fa1827bc989621eb8fd875aff75e6

## Equation and decision

For each allowed start s and translated integer box R, set
M_R(s) = sum_(n in R) W5(state(s,n))/|R| and
A_R(s) = Normalize(M_R(s)). Normalize gives ZERO at zero mass,
or PROBABILITY with rational coordinates divided by their sum.
Convergence is uniform in all translations and allowed starts
as the minimum side grows. Unlike tags have distance 1.
RAW is the separate question of arithmetic convergence of M_R.

The candidate criterion uses the exact finite set G of aligned
raw limits. RAW accepts iff G is a singleton. LIT accepts
with ZERO iff the complete stream vanishes. For a nonzero
stream it accepts iff zero is absent from G and all members of
G have one normalized direction. Accepted decisions have a
uniform effective rational modulus. The all-input proof and
the proposed adoption are in the companion
[Canon proposal](../../notes/canon/METRO-ENC4-CLOSURE-2026-11-13.md).

## Carrier and finite audit

The proposed theorem's carrier is the full common ENC4 class
of finite deterministic commuting tuples with q >= 2, rank
a >= 2, a nonempty allowed start set, and rational nonnegative
vector outputs of dimension r >= 1. This audit runs the
following exact finite tests. Their outcomes do not exhaust
that theorem's domain.

1. Under each ENC4 convention, check a zero-at-infinity stream
   whose E0 origin is positive but whose Z0 origin vanishes,
   a period-two direction split, and a period-two positive
   common ray with unequal raw masses. Require the stated
   RAW and LIT decisions, exact probability (1/2,1/2) in the
   common-ray control, and the verifier's explicit side bound
   25200 at tolerance 1/100.
2. Check the four-state LSD transient positive-tail example
   and its different exact zero aligned box family. Changing
   the certificate to the original positive-tail family must
   fail. Check a commuting Cartesian two-axis product with
   two active period-two residues and differing directions.
   Check a size-two interior Jordan chain and reject a
   tampered observable quotient. Require exact factorization
   of (x^2+1)^2 over Q.
3. Exhaust 192 two-state binary systems with two named axes,
   every second-axis digit map being the identity. Each first-axis digit
   map independently ranges over identity and swap, the
   allowed start set over the three nonempty subsets, each
   of the two scalar output weights over {0,1}, and the
   convention over ENC4. The independent pointwise oracle
   sums exact aligned intervals at prefixes 1 and 2 and
   exponents 2 and 3. If both maps are identical, residues
   depend only on parity, exhausted by these lengths. If
   the maps differ, every variable segment of positive
   length averages over both states exactly. The pointwise
   zero test also enumerates inputs 0 through 7 to include
   zero and positive words of both length parities. The
   second axis is trivial. Compare every exact decision and
   accepted limit, and compare positive mass bounds on this
   surface.

## Code and systematics

Run `python3 probes/P-METRO-ENC4-CLOSURE-1/verify.py` from the
repository root. The entire six-module implementation is
frozen with this preregistration. The verifier checks SHA-256
of auxiliary.py, check.py, common.py, generate.py, polynomial.py,
and the companion Canon proposal before importing the modules.
It uses only the Python
standard library, integer and rational arithmetic, and fixed
finite enumeration. It has no external inputs, randomness,
timing thresholds, or numerical tolerances. Its general
checker independently validates contraction and witness data
and reconstructs auxiliary module and spectral data using
shared exact algebra. The finite oracle enumerates stream
values directly without calling the certificate construction.

The theoretical checker may require large finite resources.
The exact finite audit is subject to the repository's ordinary
execution limit. Development work explored earlier fixtures
and checker implementations before this preregistration.
Such runs are design context, not formal evidence or the
execution of this pinned audit.

## Failure thresholds and interpretation

A discrepancy in any frozen exact comparison is the failure
threshold. A directly verified admitted counterexample to a
stated mathematical clause falsifies that clause. A verifier
defect, provenance failure, timeout, or unclassified exception
is integrity STOP and supplies no scientific counterexample.
A passing run establishes only the frozen bounded comparisons.
The proposed theorem and tagged aggregate adoption require
independent proof and scope review and a separately authorized
Canon fold. This probe changes no active claim, registry, or
gate, and covers no outside-ENC4 padding convention.
