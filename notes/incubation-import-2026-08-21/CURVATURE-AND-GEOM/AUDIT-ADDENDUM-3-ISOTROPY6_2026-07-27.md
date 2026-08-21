# Audit addendum 3: the sixth order, and the point group nobody has read yet

```
SESSION:   audit-external-photon-fermat-note-2026-07-27, third addendum
STATUS:    AUDIT ARITHMETIC AND SELF CORRECTION. No candidate, no prereg, no
           freeze, no promotion. No authority. Incubation lane.
SUBJECT:   the owner's bundle TWISTJ_Photon_Isotropy6_Audit_Bundle_2026-07-27.zip,
           sha256 e76c5920cb76b2bcb774398ee464b16c697bce2cdceacfe911777e3e8706de8c,
           verified 2026-07-27; correction C6 to my addendum 2; independent
           verification and strengthening of the owner's sixth-order no-go; and
           two new results.
VERDICT:   C6 accepted, and it forces two further corrections of mine that the
           owner did not ask for. The sixth-order no-go is correct and is stronger
           than stated: it holds for signed weights. But it is a statement about
           WHICH shells, not HOW MANY. Two cubic shells never suffice, three do,
           just not the first three. And the whole cubic analysis, mine and the
           owner's alike, is conditional on a point group that nobody in this
           exchange has read off the canonical object. On an icosahedral carrier
           the fourth order is free and the sixth costs one exact ratio in
           Q(sqrt5). Reading the point group is now the first gate, not a detail.
```

## 1. The bundle verifies

```
bundle    e76c5920...   as claimed
verifier  8faa6061...   as claimed
stdout    59e0a084...   as claimed
stderr    e3b0c442...   the empty-file hash
SHA256SUMS 4 of 4 OK
```

Third run of the owner's isotropy-6 verifier in this session, x86_64,
Python 3.11.15, `LC_ALL=C LANG=C PYTHONHASHSEED=0 TZ=UTC`, exit 0, empty stderr,
**byte identical** to the delivered stdout. Two Python minor versions, one
architecture. Still not a two-architecture pin.

## 2. C6 accepted, and it forces two more corrections of mine

### C6, as the owner states it. Accepted

The free Schrödinger kernel `K_t(x,y) = C(t) exp(i m |x-y|^2 / (2 hbar t))` has
constant modulus at fixed `t` and is nevertheless a real propagator whose
stationary path emerges from phase interference over intermediate points. My
addendum-2 sentence, "the whole propagator is constant in modulus on every
endpoint, which leaves no channel", is therefore wrong as a general principle.
The A3 computation is correct; my reading of it was not.

The owner's replacement reading is the right one and is adopted verbatim: what
A3 actually establishes is that this `L1` object has **instantaneous full
support**, no time symbol and no characteristic cone, so it cannot be a local
photon transfer. That is a **locality** kill, not a modulus kill.

### C7, mine, unprompted. The identification the owner's counterexample implies

The free-Schrödinger comparison is not merely an analogy. The `F_5` quadratic
path sum **is** the finite-field free Gauss kernel, term for term:

```
continuum   K_t(0,b) = C(t) exp( i m |b|^2 / (2 hbar t) )
F_5         K_N(0,b) = Z_N  j^{ Q(b) / (2 R) },        R = sum_k mu_k^{-1}
```

with `R` in the role of `t/m` and `j = zeta_5` in the role of `exp(i . )`. So the
note's section 5 did not fail because it was a bad model of light. It succeeded
completely at being the free massive kernel, which is a different object. That
sharpens the `[F]` rather than softening it.

### C8, mine, unprompted. My own kill 2 rested on a false premise

My original audit leaned on "the phase is constant on the null cone, which is
where light lives". Over `F_q` with `q` odd, **every** nondegenerate quadratic
form in three or more variables is isotropic (Chevalley-Warning). Verified by
exhaustive enumeration: all 64 nondegenerate diagonal ternary forms over `F_5`
have exactly 25 zeros, without exception.

```
The 25-point "null cone" is forced by the field. It exists for every choice of
form, it has no continuum counterpart (a positive definite real form has only the
origin), and no physical content may be read from it. It is not a light cone.
```

So the premise of kill 2 is retired, not only its wording. What survives is the
owner's locality argument and nothing else from that section.

## 3. The sixth-order no-go, verified independently and strengthened

Recomputed from my own code path, no shared code with the owner's verifier:

```
S1 (1,0,0)   |S|=6   M2=2 I   P4=(2,0)    P6=(2,0,0)
S2 (1,1,0)   |S|=12  M2=8 I   P4=(8,24)   P6=(8,60,0)
S3 (1,1,1)   |S|=8   M2=8 I   P4=(8,48)   P6=(8,120,720)
```

Every entry matches the delivered table. The cone `w1 = 2 w2 + 8 w3` and the
residue `B6 - 3 A6 = 24(u + 2v) > 0` both reproduce.

**Strengthening.** Write each shell's three isotropy defects as a row:

```
             B4-2A4   B6-3A6   C6-6A6
S1             -4       -6       -12
S2              8       36       -48
S3             32       96       672        determinant = -69120
```

The matrix is **nonsingular**. So on `S1, S2, S3` the only weight vector giving
isotropy through `O(k^6)` is `w = 0`, for **signed** weights, not merely for
nonnegative ones. The positivity argument in the delivered note is not needed;
the obstruction is linear-algebraic and does not depend on the sign of anything.

**Structural lemma, shell-set independent.** Every shell with a zero coordinate
has `C6 = 0` and `A6 > 0`, checked on 14 such shells. So `C6 = 6 A6` with only
zero-coordinate shells forces `A6 = 0`, impossible for a nonzero nonnegative
mixture. **At least one shell with all three coordinates nonzero is necessary**,
for any shell set whatsoever.

**Detail worth recording.** On the fourth-order cone, exactly one of the two
sixth-order conditions is reachable: `C6 = 6 A6` holds precisely at `u = 8 v`,
while `B6 = 3 A6` never holds. The no-go is one condition short, not two.

**The two frozen numbers reconfirmed.** `P6(face) - P6(axis) = A6/2` and the
relative spread `|k|^4 / 720`, both independent of the point on the cone; the
per-direction normalized `R8` coefficients come out `1/20160` on the axis and
`11/80640` on the face, both under the owner's universal `29/20160`; and the
critical squared mode radius is exactly `14/29`.

## 4. New result 1. The no-go is about WHICH shells, not HOW MANY

Exhaustive exact search over the 19 `O_h` orbits with maximum coordinate at most
3, solving the three isotropy constraints in rational arithmetic and requiring
**strictly positive** weights:

```
two shells    0 sets work.  Two shells never suffice.
three shells  5 sets work.
four shells   428 sets work.
```

So the minimal number is **three**, and the first three are simply the wrong
three. All five working triples:

```
shells                              weights            max |s|^2
(1,0,0)  (1,1,1)  (2,1,0)           20 :  5 : 1            5
(1,1,1)  (2,0,0)  (2,2,0)           16 : 10 : 1            8
(1,1,0)  (2,0,0)  (2,2,2)          256 : 40 : 1           12
(1,1,0)  (3,0,0)  (3,2,1)         3780 : 224 : 27         14
(1,1,1)  (3,1,0)  (3,2,1)          140 : 14 : 5           14
```

Certified end to end for the cheapest one: with `(1,0,0), (1,1,1), (2,1,0)` at
`20 : 5 : 1`,

```
P4 = 216 |k|^4   EXACTLY        P6 = 600 |k|^6   EXACTLY        M2 = 120 I_3
```

as polynomial identities, with strictly positive integer weights and zero
fitting. Exchanging `(1,1,0)` for `(2,1,0)` is the entire cost.

The owner's reading, "vyzaduje dalsi slupky nebo jiny operator", is right in
substance; the price is one shell **substitution**, not more shells.

## 5. New result 2. The point group decides which obligation the program is under

Everything above, mine and the owner's, assumes the octahedral group `O_h` acting
on `Z^3`. Nobody in this exchange has read the point group off the canonical
decoder object. That assumption is doing more work than either of us admitted.

TWIST-J is cyclotomic at `p = 5` and carries `phi`. Suppose the emergent point
group is icosahedral. Exact computation in `Q(sqrt5)`, with the dual shells
**constructed** from the icosahedron rather than asserted:

```
icosahedron        12 vertices, from (0, +-1, +-phi) and its cyclic images
its 1-skeleton     30 edges, 20 triangular faces
dodecahedron       20 vertices, computed as the face centroids
icosidodecahedron  30 vertices, computed as the edge midpoints
```

Results, every one an exact polynomial identity:

```
M_2 exactly isotropic for all three shells
P_4 = c |k|^4 EXACTLY for all three shells, with NO weight tuning
     icosahedron        c = 18 + 6 sqrt5
     dodecahedron       c = 846 + 378 sqrt5
     icosidodecahedron  c = 336 + 144 sqrt5
no single shell is isotropic at O(k^6)
```

Fourth-order isotropy is **free** on an icosahedral carrier, because the
icosahedral group has no degree 4 invariant other than `|k|^4`. On the cubic
lattice the same thing costs the tuned cone `w1 = 2 w2 + 8 w3`.

Sixth order, exact solve followed by exact verification of the full polynomial:

```
icosahedron : dodecahedron         ratio =  85 + 38 sqrt5    exact, POSITIVE
icosahedron : icosidodecahedron    ratio =  10 +  4 sqrt5    exact, POSITIVE
dodecahedron : icosidodecahedron   ratio = -18 +  8 sqrt5    exact, negative
```

Both positive mixtures are exactly isotropic at `O(k^4)` **and** `O(k^6)`. And the
cheapest ratio is not an arbitrary rational:

```
10 + 4 sqrt5 = 2 sqrt5 phi^3          exactly.
```

A ratio in the program's own field, containing `phi` and `sqrt5`, produced by a
symmetry requirement and not fitted to anything.

```
cubic carrier        O(k^4) costs a tuned cone; the first three shells cannot
                     reach O(k^6) at all; three shells minimum.
icosahedral carrier  O(k^4) free; O(k^6) costs two shells and one exact ratio
                     in Q(sqrt5).
```

**The honest caveat, and it is a large one.** An icosahedral step set does not
generate a lattice. Icosahedral symmetry is incompatible with three-dimensional
periodicity, so such a carrier is quasiperiodic, a rank 6 `Z`-module projected to
three dimensions. That is a serious structural commitment, and it is not free:
the word-metric no-go from the first audit still applies to it unchanged, because
a finitely generated abelian group still has a polytope limit shape. What changes
is only the **operator symbol** side, which is the side that matters here.

It is also not a coincidence worth ignoring that this program already carries
`phi`, `p = 5`, Thue-Morse and aperiodic-order material throughout. Whether the
decoder graph is cubic, icosahedral, quasiperiodic or none of these is a question
about a registered object and it is decidable by inspection.

## 6. My own gates that fired in this addendum, recorded

Two, both from asserting instead of constructing.

```
FIRED 1  I conjectured that the icosahedron and the dodecahedron carry
         opposite-signed degree 6 invariants and cancel with positive weights.
         The first run said NO EXACT SOLUTION for that pair and I was ready to
         record the conjecture as refuted.
FIRED 2  The refutation was itself wrong. I had asserted the dodecahedron vertex
         list from memory and got the CYCLIC ORIENTATION wrong, which placed the
         two shells in different copies of the icosahedral group. Their degree 6
         invariants then genuinely could not cancel, because they were invariants
         of different groups.
FIX      construct the dual shells from the icosahedron by computation: minimum
         edge length, 3-cliques, centroids and midpoints. The whole class of
         error disappears, and the conjecture is confirmed with ratio 85 + 38
         sqrt5.
```

Recorded because a refutation that turns out to be an artifact of a remembered
vertex list is exactly the failure mode this discipline exists to catch. It was
caught by the exact full-polynomial verification refusing to close, not by
inspection.

## 7. Agreement on the threshold, and one addition to the probe architecture

Agreed, without reservation: `BOUNDED` must not be used, and `1/30` must not be
imported as a threshold. It is a benchmark of a named test alphabet, not the
canonical graph's number, not a physical tolerance, and not a preregisterable
pass/fail line. Either the exact theorem is tested, in which case the threshold is
zero, or a physical approximation on a finite window is tested, in which case the
mode window and the observational tolerance must both be derived first.

Agreed: `M_2 = c I_3` is an integrity check, not a science gate, whenever cubic
symmetry and orbit-constant weights are already premises.

Agreed: the `L2 SPATIAL-SYMBOL` and `L5 PHOTON-CHARACTERISTIC` split is the right
architecture.

One addition, and on this evidence it belongs at the very front:

```
I0'  READ THE POINT GROUP FIRST.
     Determine the symmetry group of the canonical step set as a group of
     orthogonal transformations, before any symbol is expanded. Everything
     downstream is conditional on it:
       octahedral    -> the cone w1 = 2 w2 + 8 w3, the three-shell minimum, the
                        first-three no-go, the |k|^2/30 style benchmarks
       icosahedral   -> fourth order free, sixth order at two shells and one
                        Q(sqrt5) ratio, and a quasiperiodic carrier
       neither       -> M_2 = c I_3 is NOT automatic, and the integrity check
                        becomes a real gate again
     This is a finite exact computation on a registered object and it costs
     almost nothing. Doing it after the symbol expansion risks expanding in the
     wrong invariant basis, which is a silent error, not a loud one.
```

Noted and agreed on scope: Public Canon v24 carries `PHOTON-WINDOW-PROOF [O]`
only, an occupancy bound plus an electric-face roughening certificate. An operator
symbol row would be a new, separately argued registry row, not a quiet widening
of the existing one.

## 8. The merged obligation list

```
[F]  raw G mod 5 as the quadratic photon action
[F]  the quadratic F_5 path sum as a local photon transfer: instantaneous full
     support, no time symbol, no characteristic cone   (owner's grounds, not mine)
[F]  a fixed finite additive word metric as the origin of euclidean optics
[F]  j^{c T(path)} as localization on the fastest path, in the declared scope
[T]  the F_5 quadratic path sum IS the finite-field free Gauss kernel
[T]  the F_5 null cone is a Chevalley-Warning artifact, not a light cone
[T]  the cubic fourth-order cone w1 = 2 w2 + 8 w3
[T]  the first-three-shell sixth-order no-go, for SIGNED weights, det = -69120
[T]  a body-type shell is necessary for any shell set
[T]  two cubic shells never suffice; three do; five working triples, cheapest
     (1,0,0),(1,1,1),(2,1,0) at 20 : 5 : 1
[T]  icosahedral: O(k^4) free; O(k^6) at two shells, ratio 10 + 4 sqrt5 = 2 sqrt5 phi^3
[T]  the universal axis-face spread |k|^4/720 and the window 0 < |k|^2 < 14/29
[O]  READ THE POINT GROUP of the canonical step set                    <- first
[O]  derive the canonical photon transfer or wave operator W
[O]  derive c_t and c_s, not choose them, and exhibit the null characteristic branch
[O]  place the canonical shell weights against whichever cone applies
[O]  carry the O(k^6) and O(k^8) remainders explicitly, with a derived mode window
[O]  derive the gauge and holonomy phase from the registered Z_5 connection
[O]  nonzero shift only if a rotational sector is genuinely opened
```

## 9. Pins

```
verifier   230c311be0fa960535257fd96cffbd575d4ea83c19103d9108ce62cf702cb85f   20859 B
stdout     0b3b3d26f15e79271ff907f8af0b7ff64d62462a15241beb986a30dc25967709    8909 B
           61 PASS, 0 FAIL, exit 0, stderr empty, about one second
owner's isotropy-6 verifier rerun here, byte identical: 59e0a084...
platform   x86_64, Python 3.11.15, LC_ALL=C LANG=C PYTHONHASHSEED=0 TZ=UTC
```

One single-architecture run. Audit arithmetic, not a probe.

## 10. Non-claims

No candidate opened, no id claimed, no threshold set, no status moved. The
icosahedral computation is a statement about icosahedral shells, not a claim that
the TWIST-J decoder graph has icosahedral symmetry; that is precisely the open
question it is offered to motivate. No physical dispersion, mode window or
observational tolerance is claimed anywhere. The `O(k^8)` remainder is carried
only in the owner's cubic bound, not in the icosahedral computation. The v184 pin
and the Private Canon HEAD remain unverified in this session.
