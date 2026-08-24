# Audit of an external note: the TWIST-J Photon / Fermat candidate, 2026-07-27

```
CORRECTION NOTICE, added 2026-07-27 after the owner's disposition. This document
is kept intact as the original record. Five of its statements are corrected in
claude/AUDIT-ADDENDUM-PHOTON-FERMAT_2026-07-27.md and must be read with it:
  C1  section 3, "the only canonical option is the zero form", TOO STRONG. The
      divided form (1/5) G|ker is canonical, integral and nondegenerate. The
      conclusion survives because that form is F_5 isometric to x^2+y^2+z^2.
  C2  section 4, "direction blind" is not by itself a falsifier. The falsifier
      survives in restated form: the propagator has constant modulus on ALL 125
      endpoints, so no channel of any kind can carry a selection.
  C3  section 6 and 9, "the dictionary must be non-metric", TOO BROAD.
  C4  section 5, the delta_m "definitional repair", WITHDRAWN. The delivered note
      already defines delta_m as the angular covering radius. My error.
  C5  section 4, scope. The pinned G2 is one dimensional; the null-cone objection
      touches only the d >= 3 lift. The prereg declares L1 only and was correctly
      scoped; the overreach was in the summary, not in the pin.
  Section 8 ("not verifiable as delivered") is DISCHARGED: the bundle arrived and
  every pin reproduces byte identically.
```

```
SESSION:   audit-external-photon-fermat-note-2026-07-27
STATUS:    AUDIT AND BREAK ATTEMPT. No candidate opened, no id claimed, no prereg,
           no freeze, no promotion. No authority. Incubation lane.
SUBJECT:   an externally delivered note, "TRI MATEMATICKE MOSTY UZAVRENY,
           FYZIKALNI IDENTIFIKACE ZUZENA NA TRI OTEVRENE GATE", brought into the
           project 2026-07-27, together with its claimed prereg / verifier /
           stdout pins.
CURRENCY:  public main 190e28d9 (merge PR #176, 2026-07-27 09:07 +0200), read by
           clone, not by web fetch. STATUS.md STATE ACTIVE, CANON Public Canon v24,
           CONTENT_COMMIT bee0f1bf, CANON_SHA256 2511e68c, CANON_BYTES 134556.
           canon/SHA256SUMS 5 of 5 OK. canon/CANON.md line 1 reads
           "# TWIST-J Public Canon v24". Internal v184 not reachable this session.
VERDICT:   The classical half is correct and is not new. The quantum half is dead
           in the one sector it was built for. Sections 1 to 4 stand as
           mathematics. Section 5 is either VACUOUS on the canonical carrier or
           DIRECTION BLIND on the null branch, and those are the only two options.
           Section 6's stated route to isotropy cannot succeed for any finite
           additive step alphabet, at any scale. The note's open list is wrong:
           its O2 and O3 are not open, they are closed negative. Its O1 survives
           and is now sharply constrained: the missing dictionary must be
           non-metric.
```

## 0. What was checked, and how

Independent second reading of all six claimed theorems, followed by an exact
break attempt written from scratch, not a re-run of the note's code path. The
break verifier is `claude/break_photon_fermat.py` in this project: Python
standard library only, integers and `Fraction` only, no float anywhere, 43 gates,
under nine seconds.

```
verifier SHA-256   2d49e5a778d0f5c42a3c6bf110143f9cc1012943e63e3fd8357843d1dcb2e6b3  (14366 B)
stdout   SHA-256   e6d546f1faae58b40e75b8a08dcebb16f6a233da5fdaf57a00334b63bc40ef8e  (6252 B)
stderr             empty            exit 0            43 PASS, 0 FAIL
platform           x86_64, Python 3.11.15, LC_ALL=C LANG=C PYTHONHASHSEED=0 TZ=UTC
```

This is audit arithmetic. It is one single-architecture run, it carries no status
label of its own, and it would need its own preregistration and two-platform pin
to become a probe.

## 1. Kill 0. The note's currency reading is wrong, and the mechanism matters

```
note:   "Verejny STATUS.md nyni oznacuje za autoritu Public Canon v24, zatimco
         hlavicka aktualniho CANON.md stale rika v23."
fact:   canon/CANON.md line 1 = "# TWIST-J Public Canon v24"
        STATUS.md CANON = Public Canon v24
        STATUS.md CANON_SHA256 = 2511e68c = sha256(canon/CANON.md), 134556 B
        canon/SHA256SUMS 5 of 5 OK
```

The tree is atomic and internally consistent. There is no v24/v23 discrepancy.

The mechanism is worth recording because it will recur. This session's own first
attempt at the currency gate used a caching web fetch of
`raw.githubusercontent.com/.../STATUS.md` and was served **Public Canon v5**, a
nineteen-version-old copy. A caching fetcher can serve two files of different
ages from the same path, which manufactures exactly the phantom the note
reported.

```
RULE: the currency gate is a clone, not a fetch. Read STATUS.md, CANON.md and
      canon/SHA256SUMS from a fresh clone of main, in one tree, and verify the
      five sums. Never gate currency on a cached HTTP read of a raw file.
```

## 2. What survives, and what it is worth

All four are correct. Reproduced independently.

**Section 1, earliest arrival on a positively weighted graph.** Correct. It is
the standard fact that a positive-weight shortest path is simple, exists on a
finite graph, has the optimal-substructure property, and satisfies the Bellman
recursion. Textbook mathematics, correctly stated. It carries no TWIST-J content
and cannot acquire any until the graph and the weights are the program's.

**Section 2, static ADM null condition to the Fermat functional.** Correct, and
the input is real: the decoder metric with `beta^i = 0`, `A = N`, one scalar, is
`PART_XXII_Shadow_Functor.md` SS94.1, and `gamma_ij = a^2 h_ij`, `N = a^{-1}`,
`a = e^chi` is the v184 XLVI.2 embedding `iota_chi`. The algebra
`ds^2 = 0  =>  T[gamma] = int e^{2chi} sqrt(h(xdot,xdot))`, optical metric
`e^{4chi} h`, `kappa = 2 grad_perp chi` is exact.

Two scope facts the note does not state, and both matter.

```
(a) It has no discriminating power. Writing Phi_N = -chi, the decoder metric IS
    the isotropic weak-field metric, and n_opt = e^{2chi} = e^{-2 Phi_N} is
    exactly the textbook GR optical index. Section 2 therefore reproduces
    standard first-order light deflection. That is a consistency check on the
    dictionary, not evidence for the axiom. Any metric theory with this
    weak-field form passes it identically.
(b) It has no target row on the public line. Public Canon v24 contains ZERO
    occurrences of "optical", "Fermat", "eikonal", "null geodesic", "shift
    vector" and "arrival time" across CANON.md, REGISTRY.tsv and FRONTIER.md.
    The only public lapse object is FRW-CANONICAL-FORM [T], the rank 1
    homogeneous lapse action. There is currently nothing on the public line for
    this result to attach to.
```

**Section 3, general stationary ADM to the Randers functional.** Correct. Checked
term by term: `-A tdot^2 + 2B tdot + C = 0`, future branch
`F = (B + sqrt(B^2 + AC))/A`, and `F = b_i xdot^i + sqrt(a_ij xdot^i xdot^j)` with
`b_i = beta_i / A`, `a_ij = h_ij / A + beta_i beta_j / A^2`. The Randers reading
is the standard Zermelo form and it is right.

It has no carrier. The decoder metric's shift vector vanishes identically, and
that is not an accident of a chart: it is the Shadow Rank theorem
(`PART_XXII` SS94.1, one scalar determines ten components, `beta^i = 0`,
`A = N`, "No shift vector"). Section 3 is a correct theorem in search of a
carrier. It becomes TWIST-J content only if and when a rotating sector with a
derived nonzero shift is put on the table, and no such object is registered.

**Section 4, the exact five-phase cancellation.** Correct and trivial:
`sum_{r in F_5} (j^delta)^r = (1 - j^{5 delta})/(1 - j^delta) = 0` for
`delta != 0`. The note is right that this is stronger than an asymptotic
stationary-phase heuristic. All of its content sits in the unproven hypothesis
that real deformations come in complete, equally weighted `F_5` orbits with
`S_r = S_0 + r delta` exactly linear in `r`. The note names this correctly as its
O2.

**The note's opening falsification is accurate.** `F-A17-ACTION-SELECTOR` did
fire at v168 / DFA1, agreement 4446 of 31250, with the d,e sector failing
identically 12500 of 12500 by `D-DFA1-DE-BLINDNESS`. Dynamics is not pointwise
action minimization. Correctly cited.

## 3. Kill 1. Section 5 is vacuous on the canonical spatial carrier

Section 5 builds `S[x] = (1/2) sum mu_k |x_{k+1} - x_k|^2` over `F_5^d` and never
declares which quadratic form `|.|^2` is. The only form the program supplies on
the spatial carrier is the Galois-trace Gram, and its reduction mod 5 on that
carrier is identically zero.

```
G = p I_4 - 1 1^T at p = 5:  diagonal 4, off diagonal -1.
On ker(Tr_4):  G v = 5 v - 1 (1^T v) = 5 v,  so v^T G v = 5 |v|^2_euclid.
Explicit Z-basis B = {(1,-1,0,0), (0,1,-1,0), (0,0,1,-1)}:
    G|ker  =  [[10,-5,0],[-5,10,-5],[0,-5,10]]  =  5 x (euclidean Gram)   exact
Every entry divisible by 5, so G|ker is the ZERO form over F_5.
Exhaustive: no vector in ker(Tr_4) cap [-2,2]^4 has nonzero Gram square mod 5.
```

The canon's phrase "isotropic under the Galois Gram" (KERNEL-CELL-DICTIONARY [D])
is exactly right over Q, where the restricted Gram is `5 I_3` up to the basis
change. But 5 is precisely the prime at which that isotropy degenerates: mod 5 the
form vanishes on the whole spatial kernel.

Consequence, computed and not argued: with the canonical form, every path carries
phase `j^0 = 1`, and

```
K_N(0,b) = 125^2 = 15625  for EVERY one of the 125 endpoints, at N = 3.
```

The path sum is a bare path count. The stationary path, the localization, the
factorization `K_N = Z_N j^{S*}` and the caustic classification are all exactly
true and exactly empty. Section 5 on the canonical carrier proves nothing about
anything.

## 4. Kill 2. Grant an arbitrary nondegenerate form, and Section 5 is direction
blind exactly where light lives

Suppose the note declares a nondegenerate `F_5` form instead. Then its theorem is
correct, and this audit reproduced it independently by convolution over `F_5^3`
rather than by re-deriving its algebra:

```
localization exact: K_N(0,b) = Z_N j^{Q(b)/(2R)} at all 125 endpoints, verified
for (mu) = (1,1,1) and (1,1,1,1), for Q = x^2+y^2+z^2 and Q = x^2+y^2+2z^2.
Caustics R = 0 mod 5 recorded and computed, not skipped: support collapses to the
single point b = 0.
```

Now put light in it. The photon is the null branch. Both readings of "null" give
the same verdict.

```
spatial null,  Q(b - a) = 0:   S* = 0, so K_N(0,b) = Z_N for every one of the 25
                               points of the null cone. The propagator is
                               CONSTANT on the entire cone.
counter light cone, Q(b-a) = N^2 with constant weights:
                               S* = mu N / 2, independent of the direction of
                               b - a. Verified constant on all 30 such points at
                               N = 3 and all 20 at N = 4.
```

The endpoint phase carries no directional information on the light cone. There is
no Fermat content, no fastest-path selection, and no lever by which a dictionary
could later install one, because the dependence that would carry it has been shown
to be absent by construction, not by lack of a dictionary.

There is also a category error underneath. The action `(1/2) sum mu |Delta x|^2`
is the discrete free NON-relativistic particle. Its stationary path has nonzero
action for `b != a`. A photon path is null, and the canon already says so
explicitly: the photon "belongs to the null light branch, E+ E- = 0 identically,
not the last rung of massive acceleration" (v159). Section 5 models the massive
sector and was then read as the photon mechanism.

```
Two horns, both fatal, no third option:
  canonical form      -> Kill 1, the theorem is vacuous.
  any nondegenerate   -> Kill 2, the theorem is direction blind on the null cone
                         and is a massive-sector object besides.
```

## 5. Kill 3. Section 6's route to isotropy cannot work, at any scale

Section 6 proves `|v| <= F_m(v) <= |v| / cos(delta_m)` and then reduces the
continuum limit to two obligations: directions must densify, and the word cost
must converge to the support norm. The note treats the first as substantive. It is
satisfiable, and it is inert.

**The bound needs a definitional repair.** The inequality holds when `delta_m` is
the COVERING RADIUS, `max_u min_{d in D} angle(u, d)`, because then
`h_K(w) >= cos delta_m` for every unit `w` and `K = conv(D)` contains
`cos(delta_m) B` by the support-function characterization. Under the note's
literal wording, "maximal angular gap" between admissible directions, the constant
is wrong in `d >= 3`. The sharp constant is `1 / inradius(conv D_m)`, and that is
the object to carry, not a secant.

**Densification holds and buys nothing.** On the nearest-neighbour alphabet in
`Z^3` the realized primitive-direction set at cost at most 12 already has 2114
members, and grows without bound. Condition one is discharged for free.

**Condition two is false for every finite additive alphabet.** Exact Dijkstra,
exact rational rates, five alphabets, rate `sigma(u) = cost(n u)/n` verified
identical at `n = 8` and `n = 10`, subadditivity checked along every test ray:

```
alphabet                 ray rates^2 on (100)(110)(111)(210)(211)(221)   anisotropy^2
nearest-neighbour(6)     1  2  3  9/5  8/3  25/9                              3
chebyshev(26)            1  1/2  1/3  4/5  2/3  4/9                           3
mixed(6 cost1 + 12 cost2) 1  2  3  9/5  8/3  25/9                             3
nn + body diagonal       1  1/2  1/3  4/5  2/3  4/9                           3
nn + face diagonal       1  1/2  3/4  4/5  2/3  25/36                         2
```

The asymptotic anisotropy is a fixed rational strictly greater than 1, it does not
decay with scale, and it is alphabet dependent (3 against 2). For the
nearest-neighbour alphabet the word cost IS `|v|_1` exactly at every radius, so
the limit gauge is the cross-polytope gauge at every radius. This is the expected
fact: the limit shape of an additive word cost on a lattice is the gauge of
`conv{g / c_g}`, a POLYTOPE, and a polytope gauge is never Euclidean. Longer words
do not help, because the limit shape is already fixed by the alphabet.

The obvious escape, "space is a commutator, so the group is not abelian", does not
save it either. For a finitely generated nilpotent group, Pansu's theorem gives a
Carnot-Caratheodory limit whose horizontal indicatrix is again the convex hull of
the projected generators, hence again polyhedral. Stated as external mathematics,
not computed here.

```
O3 as the note states it is not open. It is closed NEGATIVE. No finite additive
step alphabet on a lattice or a nilpotent carrier produces an isotropic limit
norm, at any scale, no matter how the directions densify.
```

**And here is where isotropy actually lives.** The same six-step alphabet is
exactly isotropic at the operator level and exactly anisotropic at the metric
level:

```
sum over steps of s s^T = 2 I_3           exactly  -> the O(k^2) Laplacian symbol
                                                     IS isotropic
fourth moment: 2 on (i,i,i,i), 0 on (i,i,j,j)     -> anisotropy first appears at
                                                     O(k^4)
word metric anisotropy^2 = 3              exactly  -> at every scale
```

One alphabet, two answers, because they are two different questions. The program's
own isotropy claim is already the operator one, not the metric one:
`PART_XXII` SS93.1 derives the Euclidean Laplacian on `T^3` from
`L^T L |ker(Tr) = I_3`, and KERNEL-CELL-DICTIONARY [D] says space is "isotropic
under the Galois Gram". Neither is a shortest-path statement.

```
PROPOSED REPLACEMENT for the note's O3, and it is computable:
  bound the anisotropic part of the exact graph Laplacian symbol against its
  isotropic O(k^2) part on the decoder graph, and give the scale at which the
  ratio falls below a declared threshold. That is a finite exact computation on a
  registered object, and it is the honest form of "the continuum is isotropic".
```

## 6. Kill 4. The most natural repair of O1 is dead

The note leaves the path-action dictionary open. The first candidate anyone
reaches for is "the action is the arrival time", `A(gamma) = j^{c T(gamma)}`.
Tested exactly on twenty deterministic (graph, `c`) cases, seven-vertex weighted
DAGs, all paths summed exactly in `Z[zeta_5]`:

```
in 20 of 20 cases there is NO endpoint-independent Z with
    sum over paths of j^{c T(gamma)}  =  Z j^{c T_min(a,b)}
```

Arrival time does not localize the path sum on the fastest path. Any surviving
dictionary must be non-metric.

## 7. Gate firings in this audit, recorded not hidden

The anisotropy gate was posed wrongly twice before it tested the claim that was
actually being made. Both firings are first-class and are reported here rather
than quietly repaired.

```
form 1  "the ray ratio is constant from n = 1"      FIRED on 3 of 3 alphabets.
        Cause: small-n integrality is not an asymptotic claim. The gate was
        measuring lattice shells, not rays.
form 2  "n -> cost(n u) is exactly affine"          FIRED on nn+body-diagonal.
        Cause: a genuine period-2 parity structure, cost(n(1,1,0)) = 2,2,4,4,6,6.
        This is a real property of that alphabet, not noise.
form 3  Fekete rate, window independence, strict anisotropy.  PASSES.
```

No threshold was moved for the claim in section 5 above. Forms 1 and 2 tested
stronger statements than the polyhedral-limit claim requires, and they are false
as stated.

## 8. The note's own pins are not verifiable as delivered

```
claimed:  prereg 3e0f9585..., code 80c182de..., stdout 2b99a12a...
delivered as: sandbox:/mnt/data/... links from a different execution environment.
present in this project: no.  present in either repository: no.
```

None of the three artifacts is reachable from this project or from public main, so
none of the three pins can be checked. As delivered, the note is not reproducible.
Its stated gate results G1, G2, G3 are plausible and consistent with the algebra
reproduced here, but they are unverified. Attach the three files to the project or
push them to a probe branch before any further reading.

## 9. The corrected obligation list

```
was O1  path-action dictionary                     STILL OPEN, and narrowed:
                                                   the dictionary is not the
                                                   arrival time and not a
                                                   quadratic displacement action.
                                                   It must be non-metric.
was O2  orbit-completion theorem                   MOOT on the null branch. The
                                                   object it was to complete is
                                                   direction blind there, so
                                                   completing it changes nothing.
                                                   Live only if an entirely
                                                   different action is proposed.
was O3  direction densification + cost convergence CLOSED NEGATIVE. No finite
                                                   additive alphabet gives an
                                                   isotropic limit norm.
new     symbol-anisotropy bound                    the replacement for O3, exact,
                                                   finite, on a registered object.
new     nonzero-shift carrier                      Section 3 needs one, or it
                                                   stays a theorem without a home.
```

## 10. The one-line reading

The note says the classical part is essentially complete and the remaining gate is
whether real TWIST-J photon paths carry the proposed orbital structure and action.
That reading is too optimistic in one direction and too pessimistic in the other.
The classical part is complete because it is textbook and it is standard GR at
first order, so it discriminates nothing. The remaining gate is not whether real
paths carry that action. It is that no shortest-path or word-metric mechanism can
produce the target at all, and that the program's own isotropy already lives in the
operator symbol, where the note never looked.

## 11. Non-claims

Nothing here opens a candidate, claims an id, sets a threshold, or predicts the
outcome of any registered row. No public or internal status is proposed, moved or
implied. The exact arithmetic in sections 3 to 6 is audit arithmetic against
published rows and against the note as delivered; it is one single-architecture
run and it is not a probe. The v184 pin could not be checked this session; every
v184 reference above is to the project snapshot, which may lag the sealed private
head.
