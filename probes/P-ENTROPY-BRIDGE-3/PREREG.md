# P-ENTROPY-BRIDGE-3 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete decision surface for the third probe of
the ENTROPY-BRIDGE program: the living-set structure theorem of the driven
kernel, the unique-past law along the driver word, the tower carrier, and
the lambda-order table that together put the bridge cut into selection
form. It contains no gate output and earns no scientific status. Formal
execution is forbidden until this document and the accepted verifier are
committed and pushed as one immutable preregistration pin and that remote
pin is read back.

## Public identity and action layer

```text
program:          ENTROPY-BRIDGE
probe:            P-ENTROPY-BRIDGE-3
public lock:      issue 29
owner:            entropy-bridge session
branch:           probe/P-ENTROPY-BRIDGE-3
path:             probes/P-ENTROPY-BRIDGE-3/
initial base:     c53a5c42a30c9773817f8c2d4d41f07069cf713f
action layer:     L5 stream (kernel and driver combinatorics; exhaustive
                  finite checks on the full core; the lambda-tower
                  arithmetic is exact algebra); no L2 lift and no L6
                  measure claim is made by this probe
scientific state: structural facts inside ENTROPY-LAYER-BRIDGE [O]; the
                  set-level facts are exhaustive finite verifications on
                  the declared carrier; the word-anchored facts are C at
                  the frozen anchors and depths; no promotion by this
                  probe
```

This probe is based on Public Canon 2, tag `canon-v2`, activation commit
`5abb22319007fd3172f7123f4b3a71b547fb94af`, content commit
`7cfe2a62a456d0f84b1f60b4945dcdfe896e99db`, Canon SHA-256
`abd0e026ccc2be00cdb0d9d13d634e0a71602b1565e6d53ac23a99b506281021`, and
follows the sealed P-ENTROPY-BRIDGE-1 (pull request 26) and
P-ENTROPY-BRIDGE-2 (pull request 28, merge c53a5c42). Inputs by reference:
the branch indegree partition {0: 3125, 2: 3125} with total exactly 2 per
core state (probe 1, gate G10) and the cylinder no-go with the
one-bit-per-scale law (probe 2).

## The frozen claims

Setting as in the sealed probes: the public F_5^6 kernel, five involutive
generators, selector i = (z + 2 theta) mod 5, Thue-Morse drive theta_n,
branch maps F_eps, recurrent core R (6250 states, 313 attractors),
multiplication-by-J matrix M_J, lambda = 1 - zeta_5.

1. THE TWO HALVES. Im F_0 and Im F_1 partition the core into 3125 + 3125.
   (One-line proof from the sealed probe-1 indegree gate: each state has
   total indegree exactly 2, per branch 0 or 2, so the two image sets are
   disjoint and cover.) Gate G02 re-verifies set-theoretically.
2. THE LIVING BIJECTIONS. Every branch map restricted to either half is a
   BIJECTION onto its own image half: F_t : Im F_s -> Im F_t bijective for
   all four (s, t). All irreversibility of the driven kernel is spent in
   the first tick; from the halves onward the flow is invertible. Gate
   G03, exhaustive on the full core.
3. THE COMPONENT SPLIT AND THE LIVING COUNT. Every size-20 attractor
   splits (10, 10) across the halves; the singlet splits (5, 5); the
   bi-infinite (living) trajectories over a fixed driver word number
   exactly 312 x 10 + 5 = 3125 = 5^5. Gate G04.
4. THE UNIQUE-PAST LAW. Along the driver word, the composition of the
   last d branch maps on the core has image exactly 3125 with EVERY fiber
   exactly 2, for d = 1..12 at the frozen anchors (4096, 4873, 6144).
   (Derivation note, frozen: images are nested, image_{d+1} subset of
   image_d, and equal sizes force equality, so the image depends only on
   the last letter; with claim 2 the backward tree is a caterpillar.)
   Gate G05.
5. THE CATERPILLAR SHAPE. The backward tree of a trajectory state has
   width exactly 2 at every depth 1..12, and from depth 2 on exactly one
   of the two nodes carries both preimages while the sibling dies (frozen
   anchors 5000, 8192, 12345). The infinite past of a living state over
   the word is unique. Gate G06.
6. THE TOWER CARRIER. On the seed-0 attractor the boundary states at
   times m 2^k occupy exactly 10 states, 5 in each half, for k in
   {1, 2, 4, 8} (frozen sampling: m from max(8, (4096 >> k) + 1) to
   2^15 >> k). Gate G07.
7. THE LAMBDA-ORDER TABLE. ord(J mod lambda^i) = (4, 20, 20, 20, 20, 20,
   100, 100) for i = 1..8; consequently the orbit spectrum of
   multiplication by J on O/lambda^5 is {1: 1, 4: 1, 20: 156} (valuation
   formula: points of exact valuation j lie on orbits of length
   ord(J mod lambda^(5-j))). Gates G08, G09. Membership tests use
   lambda^i O superset of 5 O for i <= 4 (reduction mod 5) and
   lambda^(4+j) O = 5 lambda^j O mod 25 for j = 1..3; lambda^8 O = 25 O.
8. THE COUNTING IDENTITY OF THE SELECTION FORM. 3125 = 5^5 =
   |O/lambda^5|: the living-trajectory count equals the lambda-tower
   capacity at depth five; per component 10 = 2 x 5; the boundary carrier
   splits 5 + 5. Gate G10. Reading, carried at R with no registry weight:
   the bridge cut reduces to an equivariant SELECTION of one living
   trajectory per (kappa, y), with y mod lambda^5 offering exactly the
   right cardinality and the component census already matching the
   antipodal structure of y mod lambda^4 (sealed probe-2 anchor); the
   regularity and canonicity of the selection family is the successor
   obligation, not claimed here.

## The six frozen fields

```text
equation:     claims 1 to 8 above with the exact gate targets G01 to G10;
              all values frozen from disclosed recon: halves 3125 + 3125;
              four bijections; splits (10, 10) and (5, 5); living count
              3125 = 5^5; fibers exactly 2 and images exactly 3125 for
              d = 1..12 at anchors (4096, 4873, 6144); caterpillar widths
              2 with one death per level at anchors (5000, 8192, 12345);
              tower carrier 10 = 5 + 5 at k in {1, 2, 4, 8}; the order
              table (4, 20, 20, 20, 20, 20, 100, 100); the spectrum
              {1: 1, 4: 1, 20: 156}.
code:         verify.py in this directory, Python 3 standard library
              only, exact integer arithmetic, no float anywhere, single
              process, no filesystem writes, runtime well under 120
              seconds (recon component timings: seconds).
carrier:      the public F_5^6 kernel constants; the Thue-Morse drive by
              popcount (prefix 2^15); M_J and lambda over Z/25 and Z/5.
              No external data.
systematics:  anchors and sampling ranges frozen as stated; the census
              protocol of the public reproduction (warmup 400, window
              300); recon-lane exploration disclosed below.
failure
threshold:    any gate FAIL. All gates are exact equalities of integers,
              sets, or finite dictionaries. No tolerances.
action layer: L5. The set-level claims are exhaustive on the declared
              finite carrier; the word-anchored claims are finite-range
              C at the frozen anchors; no lift is claimed.
```

## Gates (all exact; the frozen decision surface)

```text
G01 CORE           recurrent core 6250 on 313 attractors.
G02 HALVES         Im F_0 and Im F_1 partition the core, 3125 + 3125.
G03 LIVING-BIJECT  all four restrictions F_t : Im F_s -> Im F_t are
                   bijections onto the image halves (exhaustive).
G04 COMPONENT-SPLIT every 20-attractor (10, 10); singlet (5, 5); living
                   count 312 x 10 + 5 = 3125 = 5^5.
G05 UNIQUE-PAST    image 3125 and every fiber exactly 2 for the last-d
                   compositions, d = 1..12, anchors 4096, 4873, 6144.
G06 CATERPILLAR    backward width exactly 2 at depths 1..12 with exactly
                   one carrying node from depth 2 on, anchors 5000,
                   8192, 12345.
G07 TOWER-CARRIER  boundary states at multiples of 2^k on the seed-0
                   attractor: 10 states, 5 per half, k in {1, 2, 4, 8}.
G08 LAMBDA-ORDERS  ord(J mod lambda^i), i = 1..8, equals
                   (4, 20, 20, 20, 20, 20, 100, 100).
G09 SPECTRUM-L5    orbit spectrum of J on O/lambda^5 equals
                   {1: 1, 4: 1, 20: 156} by the valuation formula;
                   156 x 20 + 4 + 1 = 3125.
G10 COUNT-MATCH    3125 = 5^5 = |O/lambda^5|; 10 = 2 x 5.
```

Falsifier map: a non-bijective restriction in G03 kills the living-set
theorem and with it the selection form; a fiber different from 2 in G05
or a width or death-pattern violation in G06 kills the unique-past law
and revives backward accumulation; a split other than (10, 10) or (5, 5)
in G04, a carrier other than 10 = 5 + 5 in G07, or a mismatch in G08 or
G09 breaks the counting identity of the selection form. A fired gate is
merged, not hidden.

## Environment and execution

```text
cd <repo root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-ENTROPY-BRIDGE-3/verify.py
```

Exit 0; exact stdout as EXPECTED.txt on the first formal run (aarch64);
RUN.md with neutral descriptors; a preliminary RESULT.md is added BEFORE
the pull request; the pull request check reruns on GitHub x86_64; byte
identity closes the two-architecture computation gate.

## Disclosure

Recon-lane exploration (incubation lane, session records of 2026-07-14,
project docs P-ENTROPY-BRIDGE-3_RECON and predecessors) computed every
value frozen above before this pin, on x86_64, outside this repository,
with unpinned recon scripts. That exploration carries no public status.
The formal status of every gate derives only from the post-pin
two-architecture runs of the pinned verifier.

## Out of scope, explicitly

The regularity, canonicity, and measure clauses of the selection family
(the successor obligation); window or depth ranges beyond the frozen
ones; the L2 -> L5 entropy transport; any physical reading; any claim
that the public architecture is derived from J or M_J. Nothing in this
probe modifies canon/, the registry, or the frontier; folding any outcome
is a separate sealed step.
