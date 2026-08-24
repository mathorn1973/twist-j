# R2 SPEC. The equivalence relation for CURVATURE-OPERATOR-CANONICAL [O]

```
SESSION:   r2-curvature-equivalence-2026-07-26
STATUS:    R2 SPECIFICATION. Incubation lane. NO AUTHORITY. Not a prereg
           freeze of the row. R1 (narrow versus generative choice space) is
           deliberately left OPEN by owner ruling of 2026-07-26.
TARGET:    public, mathorn1973/twist-j, row CURVATURE-OPERATOR-CANONICAL [O],
           program DECODER_CORE.
CURRENCY:  public main 91854391, Public Canon v22, CONTENT_COMMIT dd455edf,
           CANON_SHA256 67b12868, 113066 bytes, canon/SHA256SUMS 5 of 5 OK.
LINEAGE:   claude/C-CURVATURE-OPERATOR-CANONICAL_RECON_2026-07-18.md (R1-R3),
           claude/NADHLED-DEKODER-A-METROLOGIE_2026-07-25.md (the anchor
           diagnosis), claude/AUDIT-EXTERNAL-D-GEOM-DRAFT_2026-07-26.md.
WHY R2 FIRST: without a frozen relation, any classification under any R1
           reading is attackable after the fact by re-reading the relation.
           R2 is the only ruling that is logically prior to both R1 readings.
```

## 0. What this document does

It freezes a proposal for R2 and it establishes, by exact computation, four
facts about the candidate relations that were not previously recorded. Two of
them change which relation can be primary. It computes nothing about the row's
outcome and constructs no operator.

## 1. The four candidate relations

On Q-linear endomorphisms of a finite dimensional Q-vector space:

```
EQ    A = B entrywise on the frozen basis
SIM   exists P in GL_n(Q) with P A = B P
SCL   exists lambda in Q*, P in GL_n(Q) with P A = lambda (B P)
ISO   charpoly(A) = charpoly(B)
```

Similarity over Q for matrices over Q coincides with similarity over any
extension field, so SIM carries no field ambiguity and needs no separate
ruling on the coefficient field.

## 2. FINDING 1. The relations form a diamond, not a chain

```
            EQ  <  SIM  <  SCL
                      <  ISO
            SCL and ISO INCOMPARABLE
```

Certified exactly (checker gates L1 to L4):

```
L1  EQ < SIM strict.  N = [[0,1],[0,0]] and N^T, conjugated by P = [[0,1],[1,0]],
    det P = -1.
L2  SIM < SCL strict. I and 2I have different characteristic polynomials, so
    they are not similar; P = I with lambda = 1/2 certifies SCL.
L3  SIM < ISO strict. N and 0 share charpoly x^2 but rank 1 != rank 0.
L4  SCL vs ISO incomparable. (I, 2I) is SCL and not ISO. (N, 0) is ISO and not
    SCL, because rank is an SCL invariant and 1 != 0.
```

Consequence for the recon's R2 proposal. The robustness table was proposed as a
ladder "strict equality, similarity, similarity up to scale, isospectrality".
That ordering is false as a ladder. The table is a poset with two incomparable
coarsenings above SIM, and a join (isospectral up to scale) that nobody has
proposed. A verdict reported as "robust across the table" must be stated as
robust across the poset; a monotone reading of the table would be an error.

## 3. FINDING 2. ISO cannot certify the registered rank data

`charpoly` does not determine rank: N and 0 have the same characteristic
polynomial and different rank (checker gate L5). The public line registers, for
K_hist, rank 292 and nullity 526, and registers K_ext with rank 0 and nullity
818, inside CURVATURE-HISTORICAL-GAUSS-SPLIT [T].

Therefore an ISO-primary classification is not allowed to cite the registered
rank and nullity facts as class invariants. ISO is eliminated as primary for
any classification that wants to use the Gauss-split data, which is the only
second structural fact the public line currently carries about this operator.

## 4. FINDING 3. SCL destroys the registered trace value, and it destroys
exactly the freedom the row is missing

Exactly: `Tr((lambda A)^2) = lambda^2 Tr(A^2)`. Hence under SCL the registered
value is not an invariant. What survives is the sign and the class in
`Q*/(Q*)^2`:

```
registered      Tr_V(K_hist^2) = -881/8            [T]
EQ  invariant   the value itself
SIM invariant   the value itself
ISO invariant   the value itself (Newton from charpoly)
SCL invariant   sign = -1, and the square class -1762 only
                (881 is prime; -881/8 ~ -2 . 881 mod squares)
```

Witness that this is not academic: `B` and `3B` have `Tr = -2` and `Tr = -18`,
same square class, different values.

This meets the diagnosis of 2026-07-25 head on. That note argued the row
resists because `Tr_V(K^2) < 0` places the operator on the hyperbolic modulus
side, which admits no torsion condition, so a canonical class does not exist
without a declared normalization, and the row declares none.

```
SCL-primary quotients the classification by exactly the scale degree of
freedom that the missing normalization is about. It does not solve the anchor
problem, it hides it: the row would close UNIQUE while remaining silent on the
one thing it needed to say.
```

Dependency consequence, and this is the load-bearing sentence of this
document. `METRO-EDGE-SCALE [O]` closes by "deriving the canonical selector on
the commutator phi ladder". That ladder is a scale ladder. A classification
quotiented by scale can never contribute a selector on it. So SCL-primary makes
`CURVATURE-OPERATOR-CANONICAL` structurally unable to feed `METRO-EDGE-SCALE`,
and the two rows become permanently disjoint. Anyone choosing SCL must accept
that edge being cut, in writing, in the same fold.

## 5. FINDING 4. R2a, an orientation sub-ruling nobody has made

```
SCL with lambda in Q*        identifies K with -K (P = I, lambda = -1, certified)
SCL with lambda in Q*_{>0}   does not
```

For an operator read off a commutator, that is the orientation of the
curvature. The project already runs an oriented census candidate
(C-CENSUS-ORIENTED-ERGODIC-625), so orientation is live content here, not a
formality. If SCL is chosen at all, the sign restriction on lambda must be
frozen in R2. It cannot be decided after the classes are counted.

## 6. FINDING 5. R2b, the certificate scheme is a feasibility gate, measured

A verifier must print a certificate, not an assertion. Costs are not comparable:

```
EQ    entrywise comparison                                O(n^2)
ISO   characteristic polynomial over Q
SIM   invariant factors of xI - A over Q[x], strictly harder than ISO
SCL   the same, modulo the scaling orbit, strictly harder again
```

Measured on this host, exact rational Faddeev-LeVerrier, standard library only:

```
n = 12   0.061 s        n = 20   0.480 s
n = 28   2.000 s        n = 36   5.778 s
fitted local exponent 4.22; extrapolated to n = 818: 3.07e6 s
against the 120 s public budget, a factor 2.6e4 over
[engineering readouts, single host, x86_64; extrapolation is a LOWER bound,
 rational coefficient growth is not captured by the fitted exponent]
```

The naive route is out of budget by four orders of magnitude before SIM is even
attempted. This does not prove infeasibility; it proves that R2 must NAME the
certificate scheme and that the scheme must itself be pinned. Two candidates
worth pricing before the freeze: multi-modular computation with a pinned prime
set and rational reconstruction, with an exact final verification step; or a
fraction-free Hessenberg route with controlled denominators. If neither lands
under budget, the primary relation is being chosen by feasibility rather than by
principle, and the row must say so out loud rather than quietly pick ISO.

## 7. The R2 proposal, frozen text

```
PRIMARY RELATION.  SIM, similarity over Q, with no scaling.
    Two candidate spatial-curvature operators on a common frozen carrier are
    the same class iff they are conjugate by an element of GL(carrier) over Q.
    The certificate is the sequence of invariant factors of xI - A over Q[x],
    printed in full for every enumerated operator.

WHY SIM.  It is the only one of the four relations that preserves every
    quantity the public line currently registers about this operator (the
    exact value -881/8, rank 292, nullity 526), and the only one that leaves
    the normalization question open instead of pre-deciding it. EQ is too fine
    to be a classification at all (it is basis bookkeeping). ISO cannot carry
    the rank data (Finding 2). SCL pre-decides the anchor and cuts the edge to
    METRO-EDGE-SCALE (Finding 4).

ROBUSTNESS POSET, published with the verdict, never used to select it:
    EQ, SIM, SCL(lambda in Q*_{>0}), SCL(lambda in Q*), ISO, and the join
    ISO-up-to-scale. For each, the class count and the verdict it would have
    produced. The row closes on SIM. The poset shows whether the verdict is
    relation-robust or relation-dependent, and a relation-dependent verdict is
    reported as such, not repaired.

SUB-RULINGS STILL OWED BEFORE ANY FREEZE OF THE ROW:
    R2a  if SCL ever becomes primary, the sign restriction on lambda
    R2b  the named, priced, pinned certificate scheme for the invariant factors
         at the carrier dimension actually used
```

## 8. What this changes for R1

Nothing is decided about R1, by ruling. But two of the findings narrow it:

```
NARROW reading   with SIM primary and one registered tuple, the outcome is
                 UNIQUE by absence of registered alternatives. Finding 2 and
                 Finding 3 do not bite, because no second operator exists to
                 compare. The certificate cost of Finding 5 still bites: even
                 one operator needs its invariant factors printed at dim 818.
GENERATIVE       Findings 2 to 5 all bite, and R2b becomes the schedule driver:
                 invariant factors per tuple, times the tuple count, under
                 120 s. The frozen list must stay in single digits, as the
                 recon already estimated for a cheaper certificate.
```

Read together: R2b is now the gate on both readings, not just the generative
one. That is new, and it is the reason doing R2 first was correct.

## 9. Pins

The current checker is rev2. Its stdout carries exact content only; the measured
cost benchmark of section 6 is written to stderr, so the pinned stdout is
byte-reproducible.

```
checker            check_r2_lattice_rev2.py
                   sha256 b7f32fe67fc80e906f16de0ea997aa65f7f9016faf1329d3f74e8b479643317c
stdout             sha256 32b21bd330a25451d365b9634ec010ae249fb8de92524b064f210da50febc190
                   reproduced twice on this host, identical
                   all relation gates PASS (L1 L2 L3 L4 L5 I1 O)
platform           Ubuntu 24.04 x86_64, CPython 3.11.15, standard library only,
                   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
second platform    aarch64 leg OWED. Not run. No two-platform claim is made.
```

## 10. Defect record, first class. Two defects, both retained

```
D1  rev0, a wrong certificate.
    The first revision used a similarity certificate for an SCL claim; its
    certificate function carried no lambda, so gate O compared B with -B
    directly and FIRED. An implementation defect of fresh code, caught by the
    gate it was written for, not a scientific outcome.
    check_r2_lattice_rev0_DEFECT.py
    sha256 67409974f6465f1d59152fde1d5b5493bb45a7f165690672296923ec0c852597
    stdout sha256 83e66c97606a40f39981c527a01316a6b16b94cdef844db5dafd3ec139164644
    VERDICT FAILURE, gate O.
    Repair in rev1: scl_cert(P, lambda, A, B), used in gates L2 and O.
    Implementation only; no gate text, threshold, or claim moved.

D2  rev1, a non-reproducible pin. Found while packaging, reported.
    rev1 printed the measured timings of section 6 to STDOUT, so its stdout
    was not byte-reproducible across runs or hosts by construction. The
    pin published for rev1 was therefore a pin on one execution, not on the
    content, and it could never have passed a two-platform byte-identity gate.
    check_r2_lattice_rev1.py
    sha256 ea430d6dab54ef8e1f3482f452f778a374a48f11a70bb153f1e0cde4946ec183
    stdout sha256 e3908db8293d2b6eedb37f17381a582934c76ca322ad286949ffcdfd18cf6177
                  (one run only; NOT reproducible, superseded)
    Repair in rev2: every measured readout goes to stderr; stdout carries
    exact content only. Verified by running twice: identical sha256.
    General rule this yields, worth carrying into any future probe here:
    a pinned stdout may contain no measured quantity, only exact ones.
```

## 11. Non-claims

No operator is constructed. No classification is run. No outcome of
CURVATURE-OPERATOR-CANONICAL is computed or predicted. R1 is untouched. The
exact statements here are about the relations, and they hold for any finite
dimensional Q-vector space; the registered numbers -881/8, 292, 526, 818 are
quoted from public rows and are not recomputed here. Nothing in this document
is canon, and the R2 proposal in section 7 becomes binding only if the owner
adopts it and a fold carries it.
