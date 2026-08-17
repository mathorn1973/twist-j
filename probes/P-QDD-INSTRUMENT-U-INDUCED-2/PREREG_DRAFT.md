# P-QDD-INSTRUMENT-U-INDUCED-2 preregistration (DRAFT for owner review)

Date: 2026-08-17

Author of record: A. M. Thorn

Status: DRAFT of a preregistered protocol. Not pinned. No scientific result is
earned by this file. Every block marked `ANO` below requires a fresh explicit
owner decision before any pin; no decision taken on
`P-QDD-INSTRUMENT-U-INDUCED-1` carries over. No formal gate may run before the
accepted file and the accepted verifier are both present at an immutable pin,
that pin is pushed, and both files are read back from the public remote.

Public claim lock: issue to be opened by the owner (none yet). The next free
shared GitHub number observed on the public remote on 2026-08-17 is `#398`;
`#395`, `#396` and `#397` are taken. `#398` is not reserved by this file.

Branch (to be created): `probe/P-QDD-INSTRUMENT-U-INDUCED-2`.

Relation to `P-QDD-INSTRUMENT-U-INDUCED-1`: fresh identity, not an erratum and
not an amendment. The sealed predecessor is left untouched.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v49
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v49
CONTENT_COMMIT: dc80228522a4ccb9495550dfbef8ba73b33b2157
CANON_SHA256:   d456c42575375774200b08dafc3b4225643f526f5f1826292f1255f39d332f9e
CANON_BYTES:    237233
BASE_COMMIT:    8e38bb773c0c9a375440eef23f764efcaa07ab5c
```

Target live row: `QDD-INSTRUMENT-APPARATUS [O]`, blockers O2 (independent
physical instrument selection from a law or coupling class frozen before
comparison with the target effects) and O1 (realized event generation and
sampling).

Question. Take the registered autonomous update `U` on `Omega` as the only
coupling law, the piston block `(p1,p4,p1p,p4p)` as the system and the fiber
`(q,r)` as the pointer. For each frozen delay `d`, does the `d`-step channel
`x_k -> x_(k+d)`, with its outcome and post-state both read at the end of that
channel through a frozen finite class of two-cell record maps, realize the
frozen ordered effect pair `(E_low,E_high)` and its occurrence law exactly on
frozen finite public windows, and what post-state object does it induce?

The apparatus dynamics is not chosen for this probe. It is the registered `U`
of Canon v49 sections 2 and 3, which predates the effect pair in the public
record. The record class, delays, windows and seed strata below mention neither
`E_low`, `E_high`, the Born pairing, nor any occurrence value.

## Mandatory result-exposure disclosure

This probe is fully result-exposed. It is not a blind protocol and must not be
read as one.

```text
PRIOR PROBE:     P-QDD-INSTRUMENT-U-INDUCED-1 (public, executed)
PRIOR PIN:       45cad3384c69d7f2e187d88e63c10ecbad965f0d
PRIOR BRANCH:    probe/P-QDD-INSTRUMENT-U-INDUCED-1
PRIOR EXPECTED:  652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c
PRIOR ROOT HASH: 0baacabc9d94a824c6a9480695c7a37f2762a3a2e773d1161c26816a2dbdee15
PRIOR BREAKER:   bae54c4df9b48bc28cb693ab70514fd91ec074181b7a1cc26e75203ecda000a6
```

The predecessor ran the same registered `U`, the same 180 record maps, the same
five delays, the same two windows and the same census control, and its complete
tally output is public. Its decisive printed results, all of which the author of
this file has read before writing it, are:

```text
CHANNEL-PASS                        (with both feedback witnesses exhibited)
RECORD-INFORMATION count=150
NO-REALIZATION-W count=0
LONG-NO-REALIZATION-W2 count=0
CENSUS-NO-REALIZATION-W count=0
INSTRUMENT-FUNCTIONAL-0
ORIENT-POST-COHERENT-0
POST-UNDEFINED-OR-ZERO-900
ZERO-INPUT-MULTIVALUED-900
FAMILY-MEMBER-0 / OUTSIDE-FAMILY-0  (empty eligible set)
SEED-DEPENDENT-271350
ORIENTATION-DEPENDENT-22500
```

Separately, a target-only algebra audit reproduced the already public
expectations 25 ZERO checkpoints, 313 classes and 22 `occ` values. That audit
touched only the frozen target algebra of 1.3 and evaluated no dynamics.

Formal dynamic execution count of the verifier accepted for **this** probe is
zero. Formal dynamic execution count of the construction itself is **not** zero.

Consequence, fixed here and not movable after the pin: because the outcome of
the shared part of the construction is already public, no tag of this probe may
be read as a blind confirmation, and the routing of Field 5 is capped
accordingly.

## Field 1: equation

### 1.1 Frozen autonomous architecture (Canon v49, sections 2 and 3)

```text
Omega = N_0 x F_5^6,               omega = (n, x),
x = (p1, p4, p1p, p4p, q, r),      all arithmetic mod 5,
theta_n = s_2(n) mod 2,            s_2 = binary digit sum,
z_6(x) = p1 + p4 + p1p + p4p + q + r mod 5,
sigma(n, x) = z_6(x) + 2 theta_n mod 5,
U(n, x) = (n + 1, g_(sigma(n,x))(x)),
(g_0, g_1, g_2, g_3, g_4) = (a, b, c, d, e).
```

Generators, verbatim from Canon v49 section 3:

```text
a  swap             (p1,p4,p1p,p4p,q,r) -> (p4,p1,p4p,p1p,q,r)
b  time inversion   x -> (-p1p, -p4p, -p1, -p4, -q, -r)
c  transport        piston -> b4(piston) + s_c + r u_c;  q -> 1 - q;  r -> -r
d  mirror           x -> c_d - x
e  shifted mirror   x -> (c_d + v_e) - x

s_c = (2, 1, 2, 1),  u_c = (0, 1, 0, -1),  c_d = (2, 1, 3, 4, 1, 1),
v_e = (0, 0, 0, 0, 1, 0),  b4(p1,p4,p1p,p4p) = (-p1p, -p4p, -p1, -p4).
Relations audited: a^2 = b^2 = c^2 = d^2 = e^2 = id, (bc)^5 = id.
```

`N_0` is the forward orbit of `0` under the 2-adic odometer. The largest
requested register time is `16383 + 5 = 16388`, so exactly the update bits
`theta_n` for `0 <= n < 16388` are used, computed from the binary digit sum.
The largest requested state index is `x_16388`. No `theta_n` with `n >= 16388`
and no state with index above `16388` may be touched.

### 1.2 Frozen split

```text
pi(x) = (p1, p4, p1p, p4p) in F_5^4        system block (piston)
f(x)  = (q, r) in F_5^2                     pointer block (fiber)
ell(0,1,2,3,4) = (0, 1, 2, -2, -1)
beta(x) = (ell(p1), ell(p4), ell(p1p), ell(p4p))^T in V_eff = ell(F_5)^4 subset Q^4
```

`beta` is DEF-QDD-BALANCED-PISTON restricted to the head checkpoint. As there,
`q`, `r`, the counter, later checkpoints and dynamic evaluation are forbidden
inputs of `beta`. The fiber is read only by the record maps of 1.5.

Piston class: `cls(x) = {beta(x), -beta(x)}`. There are 313 classes: the
ZERO class (`beta = 0`, 25 checkpoints, all `f`) and 312 nonzero classes.
Class `0` is ZERO. The nonzero classes are numbered `1..312` by sorting
`rep(c) = min_lex(v,-v)` lexicographically over the balanced integer vectors.
For a nonzero checkpoint define `ori(x)=+` when `beta(x)=rep(cls(x))` and
`ori(x)=-` otherwise. The oriented pre-cell is `(cls(x),ori(x))`; ZERO has
one orientation `0`. Thus there are `1 + 2*312 = 625` oriented pre-cells, of
which `624` are nonzero.

Target weights and densities are sign-invariant, but the dynamic fiber record
is not assumed to descend through `v ~ -v`; that descent is tested rather than
averaged in.

### 1.3 Frozen effect pair and occurrence law (DEF-QDD-*, Canon v49)

```text
1 = (1,1,1,1)^T,   G = I_4 - (1/5) 1 1^T,
E_low = (1/4) 1 1^T,   E_high = I_4 - E_low,
m(v)      = v^T G v        = sum v_i^2 - (1/5)(sum v_i)^2,
w_low(v)  = v^T G E_low v  = (1/20)(sum v_i)^2,
w_high(v) = v^T G E_high v = sum v_i^2 - (1/4)(sum v_i)^2,
dens(v)   = v v^T G / m(v)                     for m(v) != 0,
occ(v)    = (w_low(v)/m(v), w_high(v)/m(v))    for m(v) != 0,   ZERO_DENOMINATOR otherwise.
```

All quantities are class functions (`v` and `-v` agree). `occ` is the
`normalized_weight_state` of DEF-QDD-MATTER-RECORD and is used only as the
comparison target after all counts are formed. Public audit expectations from
Canon v49: `m = 0` exactly on the 25 ZERO checkpoints; `occ` takes exactly 22
distinct values on the 312 nonzero classes.

Frozen integer form of the target, used by every realization test of 1.7:

```text
S(v)     = sum v_i,        Q(v) = sum v_i^2,
Delta(v) = 5 Q(v) - S(v)^2 = 5 m(v).
```

`S^2`, `Q` and `Delta` are class functions. Because `G` is positive definite
with eigenvalues `1,1,1,1/5`, `m(v) = 0` holds only at `v = 0`, so
`Delta(c) > 0` on every one of the 312 nonzero classes and no degenerate case
arises inside any realization quantifier.

### 1.4 Structural channel statements (written proof; audited exhaustively)

S1. For every generator `g` in `{a,b,c,d,e}` the fiber after the step is a
function of the fiber before the step and of `g` alone:

```text
f(a(x)) = (q, r)
f(b(x)) = (-q, -r)
f(c(x)) = (1 - q, -r)
f(d(x)) = (1 - q, 1 - r)
f(e(x)) = (2 - q, 1 - r)
```

Proof: read off the displayed formulas; no piston coordinate appears.

S2. The selector depends on the piston only through
`sum pi(x) mod 5 = ell-sum of beta(x) mod 5`, since
`sigma = (p1+p4+p1p+p4p) + (q+r) + 2 theta_n mod 5`.

Consequence (one-step channel only). `f(x_(k+1))` is a function of
`(f(x_k), theta_k, sum pi(x_k) mod 5)`. Every piston-to-fiber influence in the
one-step channel passes through the selector. Nothing here is asserted about
the `d`-step channels with `d >= 2`; those are different channels and are
measured, not derived.

S3. Fiber-to-piston influence exists through two separately audited channels.
The verifier performs no frozen witness lookup before the pin. On its first
formal run it carries out two deterministic lexicographic searches and prints
the first witness:

```text
S3_SELECTOR  equal piston and equal r, unequal q, unequal selectors,
             and unequal output pistons;
S3_DIRECT_C  equal piston and equal q+r, both selectors equal c, unequal r,
             and output-piston difference exactly (r-r') u_c after the
             common b4(piston)+s_c term is removed.
```

Absence of either witness is C3 failure. The searches range first over
`theta in (0,1)`, then piston, then `(q,r)`, then `(q',r')`, all
lexicographically.

S1, S2 and S3 as stated are finite audited statements over the 15625
checkpoints and both drive bits. They are not a general proof; see the
`CHANNEL-PASS` cap in Field 5.

### 1.5 Frozen record class R, delays D, and channel semantics  (ANO block B1)

```text
Lambda_0 = ((1,0), (0,1), (1,1), (1,2), (1,3), (1,4))        ordered six F_5-functionals
lambda_(alpha,gamma)(q, r) = alpha q + gamma r mod 5           modulo scalars
S ranges over the 30 nonempty proper subsets of F_5
rho_(lambda,S)(q, r) = LOW  if lambda(q, r) in S,  HIGH otherwise
R = { rho_(lambda,S) },   |R| = 6 x 30 = 180 two-cell record maps
D = {1, 2, 3, 4, 5}       read delays,   |R x D| = 900
```

Exact completeness statement for `R`. `R` is a complete class **only among the
two-cell record maps on the fiber that factor through a single nonzero
`F_5`-linear functional of `(q,r)`**. Under that restriction the enumeration is
exhaustive: there are exactly 6 nonzero functionals modulo scalars, exactly 30
nonempty proper subsets of `F_5`, and `6 x 30 = 180` distinct maps. Two-cell
maps that do **not** factor this way, in particular arbitrary bipartitions of
the 25 fiber values and maps built from two independent functionals, lie
outside `R` and are not tested by this probe. No tag of this probe may be
phrased as a statement about all two-cell records of the fiber.

Subsets are numbered by masks `1..30`; bit `i` means `i in S`. Enumeration is
`Lambda_0` order, mask ascending, delay ascending. Maps compose rightmost
first. The commutator convention is
`[g,h]=g o h o g^(-1) o h^(-1)`, and `T_delta(x)=x+delta mod 5`.

Channel semantics, frozen. For each delay `d` in `D` the trial is the
**`d`-step channel**

```text
x_k  -->  x_(k+d)

pre-vector   v  = beta(x_k)                  read at the start of the channel
outcome      b  = rho(f(x_(k+d)))            read at the end of the channel
post-vector  v' = beta(x_(k+d))              read at the end of the channel
```

The outcome and the post-state are read at the same time index, namely the end
of the channel. For distinct `d` these are distinct channels, not distinct
readings of one channel. No count, tag, table or conclusion obtained at one `d`
is transferred to another `d`, and no tag of this probe aggregates over `D`
except by explicitly reporting a per-`d` breakdown alongside it.

Admissibility. A trial at time `k` in window `W*` and delay `d` is admissible
only when `k + d` lies within the frozen horizon of 1.1. With
`W = [512, 2048)` the largest touched index is `2047 + 5 = 2052`; with
`W2 = [2048, 16384)` it is `16383 + 5 = 16388`.

No ready state and no reset are assumed: the fiber is a refreshable register,
and every checkpoint reads LOW or HIGH.

Complete enumeration rule: every `(rho, d)` in `R x D` is evaluated and
reported. No member is selected by looking at counts. Complements
`S <-> F_5 \ S` are both in `R`, so the ordered pair (LOW, HIGH) is covered
without a separate swap rule.

### 1.6 Frozen sampling semantics  (ANO block B2)

```text
S-single  every seed x_0 in F_5^6 (15625 seeds), orbit from omega_0 = (0, x_0),
          window W = [512, 2048)   (the Law_W precedent, 1536 trial times)
S-long    seeds Z0 = { x_0 : f(x_0) = (0,0) }, the zero-fiber-at-n=0 stratum
          (625 seeds), window W2 = [2048, 16384)   (14336 trial times)
S-census  control only: the S-single counts summed over all 15625 seeds;
          it shares the window W and is therefore not an independent window
```

Naming discipline for `Z0`. `Z0` is defined by the seed value at `n = 0` and by
nothing else. It is **not** a ready-fiber stratum. No readiness, reset,
relaxation or preparation of the fiber at time 2048, or at any other time, is
asserted, assumed or tested anywhere in this probe. Any prose that reintroduces
the word "ready" for `Z0` is a completeness failure of the run record.

Counts, for a seed `x_0`, window `W*`, class `c`, orientation `eps`, record
`rho`, delay `d`, over admissible trials only:

```text
N_c              = #{ k in W* : cls(x_k) = c }
L_(c,rho,d)      = #{ k in W* : cls(x_k) = c, rho(f(x_(k+d))) = LOW }
N_(c,eps)        = #{ k in W* : (cls(x_k),ori(x_k)) = (c,eps) }
L_(c,eps,rho,d)  = #{ k in W* : (cls(x_k),ori(x_k)) = (c,eps),
                                rho(f(x_(k+d))) = LOW }
```

Premise statement. The single-orbit read is the long-window premise P2 of
DRIFT-IS-THE-READ; here it is used only as a frozen finite-window predicate.
No limit `N -> infinity` is asserted or established by any window in this
probe. `SAMPLING NOT PROVIDED` remains the only sampling statement beyond
exact finite-window counts.

### 1.7 Realization predicates and induced-object maps  (ANO block B3)

#### 1.7.1 Realization, in integers, on visited cells only

Frozen integer test. For a class `c` with representative `rep(c)`, write
`S = S(rep(c))`, `Q = Q(rep(c))`, `Delta = 5Q - S^2`. A count pair `(L, N)`
with `N > 0` realizes the target at `c` exactly when

```text
4 * L * Delta = N * S^2
```

This is an identity between integers. It is exactly equivalent to
`L/N = w_low(c)/m(c)` in `Q`, and no rational arithmetic is required to decide
it. No float, no `Decimal` and no `Fraction` may be used in the decision.

```text
REAL-CLASS-ON-VISITED(rho,d;x_0,W*)
    iff for every nonzero class c with N_c > 0:
        4 * L_(c,rho,d) * Delta(c) = N_c * S(c)^2

REAL-ORIENT-ON-VISITED(rho,d;x_0,W*)
    iff for every nonzero oriented pre-cell (c,eps) with N_(c,eps) > 0:
        4 * L_(c,eps,rho,d) * Delta(c) = N_(c,eps) * S(c)^2

REAL-ON-VISITED(rho,d;x_0,W*)
    iff both of the above hold
```

`REAL-ORIENT-ON-VISITED` prevents a false success obtained by averaging unequal
`+` and `-` rates.

Coverage, reported alongside every realization tag and never inferred:

```text
COV-CLASS(x_0,W*)   = #{ nonzero classes c with N_c > 0 }        out of 312
COV-ORIENT(x_0,W*)  = #{ nonzero oriented pre-cells with N > 0 } out of 624
FULL-COVERAGE(x_0,W*) iff COV-CLASS = 312 and COV-ORIENT = 624
```

The verifier prints, for each window, the minimum, maximum and exact
distribution summary of `COV-CLASS` and `COV-ORIENT` over the applicable seeds,
and the census coverage of the union.

```text
REAL-FULL(rho,d;x_0,W*)  iff  REAL-ON-VISITED(rho,d;x_0,W*) and FULL-COVERAGE(x_0,W*)
```

Claim rule, frozen. A statement of the form "the target is realized on all 312
nonzero classes" may be printed **only** under the corresponding `REAL-FULL`
tag. Under `REAL-ON-VISITED` alone the only admissible phrasing is "on the
visited nonzero classes, whose count is printed".

#### 1.7.2 Per-pair realization tags

```text
REAL-SINGLE(rho,d)  iff REAL-ON-VISITED(rho,d; x_0, W)  for all 15625 seeds
REAL-LONG(rho,d)    iff REAL-ON-VISITED(rho,d; x_0, W2) for all 625 seeds in Z0
REAL-CENSUS(rho,d)  iff the summed W counts satisfy the same integer identity
                        for every nonzero class with summed N_c > 0
REAL-BOTH(rho,d)    iff REAL-SINGLE(rho,d) and REAL-LONG(rho,d)
```

`REAL-BOTH` is the only admissible joint statement about the two windows. Two
distinct pairs, one satisfying `REAL-SINGLE` and another satisfying
`REAL-LONG`, do not constitute a joint witness and may not be reported as one.

The corresponding full-coverage variants `REAL-FULL-SINGLE`, `REAL-FULL-LONG`,
`REAL-FULL-BOTH` are evaluated and printed separately.

#### 1.7.3 Record information, census level and orbit level

```text
INFO-CENSUS(rho,d)
    iff the census conditional table  c -> L_(c,rho,d)/N_c  is not constant
        over the nonzero classes with N_c > 0; with fewer than two applicable
        classes it is false

INFO-ORBIT(rho,d;x_0,W*)
    iff the same table formed from the single orbit of x_0 is not constant
        over the nonzero classes with N_c > 0; with fewer than two applicable
        classes it is false
```

Constancy is decided by exact cross multiplication of integer count pairs.

The census table is an aggregate. Aggregation can cancel opposite correlations
carried by individual orbits, so `INFO-CENSUS` false does **not** imply
`INFO-ORBIT` false for any seed. Both are therefore evaluated, and the negative
tags of Field 5 are separated accordingly.

#### 1.7.4 Induced post-object: class level and physical level

The post-object is formed from the census joint tallies of
`(cls(x_k), ori(x_k), f(x_(k+d)), cls(x_(k+d)))` over `W`, that is from the two
ends of the `d`-step channel. Target classification uses only visited nonzero
pre-classes; ZERO-input behaviour is reported separately and never used to
satisfy a target condition.

Two distinct functionality notions are defined, because they are not the same
statement:

```text
phys(v')  = ZERO            if m(v') = 0
          = dens(v')        otherwise

Supp_cls(c, b)   = set of post-classes c' occurring on the branch (c, b)
Supp_phys(c, b)  = set of values phys(v') occurring on the branch (c, b)

CLASS-FUNCTIONAL iff |Supp_cls(c,b)| = 1 for every applicable branch with at
                 least one event
PHYS-FUNCTIONAL  iff |Supp_phys(c,b)| = 1 for every applicable branch with at
                 least one event
```

`dens(v') = dens(t v')` for every nonzero rational `t`, so `v'` and `2v'` are
different QDD classes with the same normalized density. `Supp_phys` is the
image of `Supp_cls` under `phys`, hence `CLASS-FUNCTIONAL` implies
`PHYS-FUNCTIONAL` and the converse fails in general. Only `PHYS-FUNCTIONAL` is
a statement about physical functionality of the induced map. `CLASS-FUNCTIONAL`
is a statement about the class label and is reported under that name and no
other.

```text
Dbar(c, b)   = average of dens(v') over the events on the branch with m(v') != 0;
               the number of ZERO posts on the branch is counted separately
POST-UNDEFINED-OR-ZERO iff some visited nonzero input branch with positive
               target weight has no event or has any ZERO post; any event on a
               zero-target-weight branch is also in this category
POST-PURE-STRICT iff no undefined/zero condition occurs, at least one nonzero
               post-object is defined, and rank Dbar(c,b) = 1 for every defined
               applicable branch
POST-MIXED   iff no undefined/zero condition occurs and some defined applicable
               Dbar(c,b) has rank different from one
```

`Dbar(c,eps,b)` is also formed separately for both orientations. For a class
whose two oriented pre-cells are both visited, `ORIENT-POST-COHERENT` requires
the two branch-event domains to agree; on every present branch their ZERO-post
fractions and defined orientation-resolved post objects must agree. A pair with
no defined nonzero post-object is not POST-PURE. The three pair tags
`POST-PURE-STRICT`, `POST-MIXED` and `POST-UNDEFINED-OR-ZERO` form a partition
of all 900 pairs, with undefined/zero taking precedence over purity.

For the exact implementation, write `P(v) = v v^T / m(v)`, so
`dens(v) = P(v) G`. The ten symmetric entries of the weighted sum of `P(v')`
are stored as scaled integers with one exact common denominator; multiplying
the average by `G` reconstructs the displayed `Dbar` exactly. Because `G` is
positive definite, a positive average of the post densities has rank one
exactly when all nonzero post-vectors in its support are rationally collinear.
The verifier tests this through canonical direction bitsets and reconstructs
full rational matrices wherever orientation coherence or C7 requires them.

#### 1.7.5 Frozen family membership

Eligibility, frozen before the run: family membership is decided for exactly
those `(rho,d)` in the union

```text
ELIGIBLE = { (rho,d) : CLASS-FUNCTIONAL } union
           { (rho,d) : PHYS-FUNCTIONAL }  union
           { (rho,d) : REAL-SINGLE }
```

and for no other pair. The union is used so that no pair is excluded by the
narrower of the two functionality notions.

Using the frozen L4 family of `P-QDD-INSTRUMENT-NONSELECTION-1`:

```text
LOW branch:   member iff Dbar(c, LOW) = E_low
HIGH branch:  member iff there is t in Q with
              Dbar(c, HIGH) = (R_t u)(R_t u)^T G / w_high(v),  u = E_high v,
              R_t the frozen rational rotation on span(r_v, f_v) fixing g_v and 1,
              r_v = (1,1,-1,-1)/2, f_v = (1,-1,1,-1)/2, g_v = (1,-1,-1,1)/2.
```

The frozen parameterization is

```text
c_t = (1-t^2)/(1+t^2),       s_t = 2t/(1+t^2),
R_t r_v = c_t r_v + s_t f_v,
R_t f_v = -s_t r_v + c_t f_v,
R_t g_v = g_v,               R_t 1 = 1.
```

Decision procedure for the HIGH test: `Dbar` must have rank one with image
spanned by some `w` in `ker(sum)`; write `u = u_r r_v + u_f f_v + u_g g_v` and
`w = w_r r_v + w_f f_v + w_g g_v`; membership holds iff there is a rational
`mu != 0` with `w_g = mu u_g`, `w_r^2 + w_f^2 = mu^2 (u_r^2 + u_f^2)` and
`(w_r, w_f) = mu (c u_r - s u_f, s u_r + c u_f)` for a rational point `(c, s)`
on the unit circle with `c != -1`; then `t = s/(1+c)`. All steps are exact
rational arithmetic; the exhibited `t` is printed.

Single-parameter requirement, frozen. `FAMILY-MEMBER(rho,d)` requires **one
common rational parameter** `t = t_(rho,d)` for the HIGH branch, valid
simultaneously across every applicable nonzero input class of that pair and
across both orientations. Each orientation contributes either all of `Q`, at
most two rational candidates, one rational candidate, or the empty set; the
exact sets are intersected and the complete finite common candidate set is
printed. Per-class choices of `t` do not constitute one instrument and are a
`FAMILY-MEMBER` failure, not a partial success. If the intersection is all of
`Q`, the verifier prints `ALL_Q` and the canonical witness `t = 0`. Every
candidate is checked again by reconstructing the full normalized matrix. The
image direction is canonicalized by clearing denominators, dividing by the
integer gcd and making the first nonzero component positive.

Branch rules, frozen:

```text
target weight = 0:  any event on the branch          -> OUTSIDE-FAMILY
                    no event on the branch           -> no post test
target weight > 0:  no event, or any ZERO post-state -> OUTSIDE-FAMILY
                    otherwise Dbar must exist and equal the frozen target
```

Every tested positive-weight branch must therefore have exactly zero ZERO
post-states. LOW must pass on every applicable nonzero class and orientation.

#### 1.7.6 Dependence counts

```text
SEED-DEPENDENT        number of triples (rho,d,c), including c = ZERO, for which
                      two seeds visiting c in W have different class-averaged
                      L/N, decided by exact integer cross multiplication
ORIENTATION-DEPENDENT number of (rho,d,c) whose + and - census rates differ
                      when both orientations are present
```

## Field 2: code

Accepted verifier, to be written and frozen together with the accepted
preregistration:

```text
probes/P-QDD-INSTRUMENT-U-INDUCED-2/verify.py
```

Requirements:

```text
Python standard library only
integers only in every decision path; Fraction permitted only for printing
  reconstructed matrices, never for a gate decision; no float, no Decimal,
  no external dataset
deterministic order of enumeration:
  seeds lexicographic in (p1,p4,p1p,p4p,q,r),
  R lexicographic in (Lambda_0 index, subset mask 1..30), D ascending
stdout: gate lines, all counts and tags of Field 5, coverage lines, and
  SHA-256 of the canonical serialization of every joint tally table
  (tables themselves are not printed)
```

### 2.1 Canonical serialization, frozen  (ANO block B4 depends on this)

Nothing below may be changed after the pin.

```text
Table set, in this displayed order, with these exact labels:
  T1  "SINGLE_SEED_TABLES"
  T2  "LONG_SEED_TABLES"
  T3  "SINGLE_JOINT"
  T4  "LONG_JOINT"
  T5  "FIBER_AGG_SINGLE"
  T6  "FIBER_AGG_LONG"
  ROOT "ROOT" commits to the six labeled digests in the order T1..T6

Record layout: label bytes, then entries sorted lexicographically by key,
  each field big-endian fixed width:
    delay d            1 byte
    pre-cell id        2 bytes   (0 = ZERO, 1..624 oriented nonzero of 1.2)
    functional index   1 byte    (position in Lambda_0, 0..5)
    subset mask        1 byte    (1..30)
    post-class id      2 bytes   (0 = ZERO, 1..312)
    count              4 bytes   unsigned
Entries with count zero are omitted. Omission is the canonical encoding of
  zero and never an abbreviation of a nonzero value.
Class order is the rep(c) = min_lex(v,-v) lexicographic order of 1.2.
Orientation order is + before -.
Mask order is ascending 1..30. Delay order is ascending 1..5.

Reported numbers:
  every count is printed as a bare integer together with its frozen total;
  every rate is printed as an exact reduced fraction "num/den" with den > 0,
    reduced by integer gcd, never as a decimal;
  the frozen denominators are: N_c for class rates, N_(c,eps) for oriented
    rates, the summed N_c for census rates, 312 for COV-CLASS, 624 for
    COV-ORIENT, 900 for pair partitions, 15625 and 625 for seed tallies;
  each printed rate line names its denominator explicitly.

Admissible t sets:
  printed as "ALL_Q", or as "{}" for the empty set, or as an ascending list of
  exact reduced fractions with positive denominator, sorted by (num*den' ,
  num'*den) integer comparison; the canonical witness for ALL_Q is t = 0.
```

Dense joint counters are unsigned 32-bit cells. Their absolute per-cell bounds
are the total admissible trials per delay, respectively `15625*1536 = 24000000`
and `625*14336 = 8960000`, both strictly below `2^32`; the verifier checks the
storage widths and these bounds before allocation.

### 2.2 Cost and the interruption rule

Minimum number of applications of `U`, with prefix reuse across the two
windows:

```text
single window, all 15625 seeds, states up to x_2052 :  15625 * 2052 = 32062500
long window, 625 seeds in Z0, states x_2053..x_16388:    625 * 14336 =  8960000
total                                                                 41022500
```

The frozen budget of this probe is therefore at least `41022500` applications
of `U`. The figure `32062500` is the single-window part alone and may not be
quoted as the cost of the probe.

Interruption rule, frozen. Early elimination is permitted **only** to stop
further checking of the `REAL-SINGLE` flag on an already eliminated lane. It
may not stop, shorten, sample or skip:

```text
any other table or tag;
the long window W2;
the post-state tallies and the induced-object classification;
the coverage counts;
any hash or the canonical serialization.
```

Every table listed in 2.1 is formed in full and hashed in full regardless of
how early any realization flag is decided. Any implementation in which an
eliminated lane shortens a hashed table is a C-gate failure, not an
optimization.

Memory and traversal are frozen as follows. `LONG` is formed, hashed and
released before `SINGLE` is allocated, so at most one dense five-delay joint
dataset is resident in Phase A. No unbounded cache and no retained set of seed
signatures is permitted. Each fiber value has one frozen packed 180-lane
increment. The lane layout uses one guard bit and one equality-test bias bit
per lane, and lane equality is read by guarded broadword subtraction without
inter-lane carry or borrow; the verifier audits `14336^2 < 2^29` and audits the
target numerator and denominator products against the same bound. Python
dictionaries are not a representation of the joint table.

The verifier audits: the transcription of the generators and relations (1.1),
the split and the 25/313/22 expectations (1.2, 1.3), the integer identity of
1.3 against an independent rational evaluation on all 312 nonzero classes, S1
and S2 exhaustively over all 15625 checkpoints including both drive bits, S3 by
the two deterministic witness searches of 1.4, the admissibility bound of 1.5,
and then forms the counts of 1.6 and evaluates every predicate and map of 1.7.
The predicates of 1.7 are complete enumerations; no finite sample replaces a
quantifier over `R x D`, seeds, or classes.

## Field 3: carrier or data

No external data.

```text
autonomous carrier   Omega = N_0 x F_5^6, U as in 1.1
system carrier       V_eff subset (Q^4, G) via beta
pointer carrier      F_5^2 (the fiber), read only through R
target objects       E_low, E_high, m, w_low, w_high, dens, occ of 1.3
```

All displayed vectors, matrices and maps are frozen in this file.

## Field 4: systematics and completeness

There is no measurement systematic.

```text
C1  Generators, relations and (bc)^5 = id reproduce exactly; the sheet
    commutators [d,e] = T_(0,0,0,0,3,0), [b,d] = T_(0,0,0,0,3,3),
    [b,e] = T_(0,0,0,0,1,3) of FIRED-COMMUTATOR-NOGO reproduce exactly.
C2  25 ZERO checkpoints, 313 classes, 22 distinct occ values reproduce.
C3  S1, S2 audited over all checkpoints; both S3 witnesses found.
C4  The integer identity 4*L*Delta = N*S^2 agrees with an independent exact
    rational evaluation of L/N = w_low/m on all 312 nonzero classes and on a
    frozen sweep of count pairs; Delta > 0 on all 312 classes.
C5  Every (rho,d) in R x D evaluated on S-single, S-long and S-census;
    REAL-SINGLE, REAL-LONG, REAL-CENSUS, REAL-BOTH and their REAL-FULL
    variants printed in full, possibly empty. Coverage distributions printed.
C6  INFO-CENSUS and INFO-ORBIT evaluated for every (rho,d); both counts printed.
C7  CLASS-FUNCTIONAL, PHYS-FUNCTIONAL, ORIENT-POST-COHERENT and the strict
    partition POST-PURE-STRICT / POST-MIXED / POST-UNDEFINED-OR-ZERO evaluated
    for every (rho,d); counts printed. ZERO pre-input behaviour printed
    separately. The inclusion CLASS-FUNCTIONAL subset PHYS-FUNCTIONAL is
    audited, and a violation is a C-gate failure.
C8  Family membership decided exactly once for every pair in ELIGIBLE and for
    no other pair, with the exhibited common t where it exists. The evaluated
    set, member set and outside set are audited as an exact disjoint partition
    of ELIGIBLE.
C9  Seed-dependence including ZERO and orientation-dependence counts printed.
C10 Horizon audit: no theta_n with n >= 16388 and no state index above 16388
    is touched; the per-delay admissibility bound of 1.5 holds for every
    counted trial.
C11 Interruption audit: the byte length and entry count of every table of 2.1
    are independent of the order in which realization flags are decided.
C12 Six labeled table hashes and their root hash printed; both architectures
    must agree byte for byte on the whole stdout.
```

Any hidden input, floating tolerance, post hoc restriction of `R x D`, use of
`E_low`, `E_high` or `occ` before the counts are formed, or an unnamed
L5-to-L6 lift is STOP.

## Field 5: failure threshold and scientific routing  (ANO block B4)

No tolerance exists.

```text
ARCH-STOP
  C1, C2, C3, C4, C10 or C11 fails: transcription, horizon or integrity error;
  no scientific reading.

CHANNEL-PASS
  S1, S2, S3 audited over the finite checkpoint set. Finite audited statement
  about the registered coupling.

REGISTER-REALIZED-W          at least one (rho,d) satisfies REAL-SINGLE
NO-REALIZATION-W             no (rho,d) satisfies REAL-SINGLE
LONG-REALIZED-W2 / LONG-NO-REALIZATION-W2        same for REAL-LONG on Z0
CENSUS-REALIZED-W / CENSUS-NO-REALIZATION-W      control only, shares W
REGISTER-REALIZED-BOTH       at least one (rho,d) satisfies REAL-BOTH
NO-REALIZATION-BOTH          no (rho,d) satisfies REAL-BOTH
REAL-FULL-*-k                counts under full coverage, printed separately
COVERAGE-INCOMPLETE-W / -W2  full coverage fails somewhere; printed with the
                             exact minimum COV-CLASS and COV-ORIENT

NO-RECORD-CENSUS-W           INFO-CENSUS false for every (rho,d)   (F1a shape)
NO-RECORD-ORBIT-W            INFO-ORBIT false for every (rho,d) and every seed
                                                                   (F1b shape)
ORBIT-RECORD-k               number of (rho,d) with INFO-ORBIT true for at
                             least one seed

CLASS-FUNCTIONAL-k           (F2a shape)
PHYS-FUNCTIONAL-k            (F2b shape, the physical one)
ORIENT-POST-COHERENT-k
POST-PURE-STRICT-k / POST-MIXED-k / POST-UNDEFINED-OR-ZERO-k
                             exact partition of all 900 pairs
FAMILY-MEMBER-k / OUTSIDE-FAMILY-k   counts over ELIGIBLE, with common t values
SEED-DEPENDENT-k                                                   (F4 shape)
ORIENTATION-DEPENDENT-k

STOP
  authority, pin, verifier integrity, completeness, security or layer
  discipline fails.
```

Scientific routing, fixed before the pin.

**Global grade cap.** Every dynamic outcome of this probe, positive or
negative, is capped at **candidate-C**. No dynamic tag of this probe may be
proposed as candidate-T, candidate-D or higher at any fold, and the cap is not
movable after the pin. The cap follows from the result-exposure disclosure
above: the shared construction has already been executed in public.

**CHANNEL-PASS cap.** As tagged here, `CHANNEL-PASS` is a finite audited
statement over 15625 checkpoints and is candidate-C. It may be proposed as
candidate-T only if, and only when, a separate written general proof of S1, S2
and S3 is pinned in the same branch as `PROOF-S123.md`, with the proof standing
on its own without reference to any tally of this probe. Without that file the
candidate-T reading of `CHANNEL-PASS` is unavailable.

- `REGISTER-REALIZED-BOTH` together with `CHANNEL-PASS` earns at most a
  finite-window realization statement on the frozen public windows, at
  candidate-C. It does not close O1: no limit is proved. It does not close O2:
  the record map is exhibited from a class that is complete only among
  functional-factoring two-cell records, and its status as a physical selector
  is a separate owner decision. Both realization tags require the
  orientation-resolved integer test; quotient averaging cannot earn them.
- `REGISTER-REALIZED-W` and `LONG-REALIZED-W2` carried by two **different**
  pairs earn nothing jointly. They are reported as two separate single-window
  facts and may not be combined in prose.
- `NO-REALIZATION-BOTH` leaves O1 and O2 at STOP. It is not a negative closure
  of `QDD-INSTRUMENT-APPARATUS`: finite windows do not refute a limit law, and
  the class {registered `U` on the 4 + 2 split, read through `R` at `D`} is not
  the complete admissible physical class of the row, nor even the complete
  class of two-cell fiber records.
- `NO-RECORD-ORBIT-W` is the sharpest negative reading available here: on the
  frozen windows no single orbit carries piston-class information for any
  member of `R` at any delay in `D`. `NO-RECORD-CENSUS-W` alone is strictly
  weaker and is recorded as a census-level statement only, because aggregation
  can cancel opposite per-orbit correlations.
- `PHYS-FUNCTIONAL-0` is the negative functionality reading. `CLASS-FUNCTIONAL-0`
  alone does not support any statement about physical functionality of the
  induced map.
- Any statement quantified over all 312 nonzero classes requires the matching
  `REAL-FULL` or coverage tag.

The threshold and scope may not move after the pin.

Falsifier map:

```text
F1a fiber holds no census record   -> NO-RECORD-CENSUS-W
F1b fiber holds no orbit record    -> NO-RECORD-ORBIT-W
F2a induced class map not functional -> CLASS-FUNCTIONAL-0
F2b induced physical map not functional -> PHYS-FUNCTIONAL-0, with
                                        POST-MIXED or POST-UNDEFINED-OR-ZERO
F3  effects not realized           -> NO-REALIZATION-BOTH and its components
F4  seed dependence                -> SEED-DEPENDENT-k with k > 0
F5  weights not realized           -> identical to F3 in this discrete setting:
                                      realizing the ordered effects means
                                      realizing occ
```

## Field 6: action layer

```text
L1  exact autonomous dynamics and finite audited channel statements
L4  induced apparatus classification on the frozen split, class level and
    physical level separately
L5  finite-window realized-trial stream and exact integer counts
L6  none: no normalized measure, no limit, no SI statement
```

## Scope firewall

This probe does not:

- close `QDD-INSTRUMENT-APPARATUS [O]` in either direction;
- modify `QUADRATIC-DECODER-DATA [O]` or any DEF-QDD-* definition;
- modify, amend or reinterpret the sealed `P-QDD-INSTRUMENT-U-INDUCED-1`;
- choose a coupling: `U` is the registered update, unchanged;
- define the record class, delays, windows or seed strata with reference to
  `E_low`, `E_high`, the Born pairing or any occurrence value;
- treat `R` as complete among all two-cell fiber records;
- transfer any count or tag between different delays;
- assert readiness, reset or preparation of the fiber at time 2048 or anywhere;
- select one `(rho, d)` before the complete enumeration is reported;
- average `beta` and `-beta` before the orientation-resolved realization test;
- read physical functionality off the class label;
- assert existence of any long-window limit or an L6 measure;
- adopt `G`-positivity, minimal disturbance, decoherence or collapse as a premise;
- derive the effect pair, the Born pairing or the architecture from `J`;
- fill a decoder-completion-contract field;
- claim that a second-copy (composition) apparatus is excluded or required;
- earn any grade above candidate-C from a dynamic tag.

## Formal sequence after the pin

1. Owner ANO on blocks B1 to B4, recorded on a freshly opened claim-lock issue.
2. Push the accepted `PREREG.md` and `verify.py` on the claimed branch.
3. Read both files back from the public remote; record the immutable pin,
   SHA-256 and byte counts on the issue.
4. Only then execute the accepted verifier for the first formal run.
5. Commit exact `EXPECTED.txt`, neutral `RUN.md` and `RESULT.md` without
   changing the pinned preregistration or verifier.
6. Open one pull request changing only
   `probes/P-QDD-INSTRUMENT-U-INDUCED-2/`.
7. Require GitHub x86_64 and aarch64 jobs to reproduce the same committed
   `EXPECTED.txt` byte for byte.
8. A later separate reviewed Canon fold may register only the status and scope
   actually earned by this probe, subject to the candidate-C cap.

## Appendix: owner-fix map

Owner STOP verdict of 2026-08-17, twelve mandatory corrections, and where each
is discharged in this file.

```text
 1  result-exposure wording        -> "Mandatory result-exposure disclosure"
                                      DEVIATION, see note below
 2  d-step channel x_k -> x_(k+d)  -> 1.5 "Channel semantics, frozen"
 3  range 0 <= n < 16388, Z0 name  -> 1.1 horizon, 1.6 "Naming discipline"
 4  R complete only via one
    nonzero linear functional      -> 1.5 "Exact completeness statement"
 5  integer test 4 L Delta = N S^2 -> 1.3 integer form, 1.7.1, gate C4
 6  one common t, zero-weight
    branch, zero ZERO posts        -> 1.7.5 "Single-parameter requirement"
                                      and "Branch rules"
 7  CLASS-FUNCTIONAL and
    {ZERO, dens(v')}               -> 1.7.4, both notions defined, gate C7
 8  REAL-ON-VISITED plus coverage  -> 1.7.1 coverage block and claim rule
 9  direct intersection marker     -> 1.7.2 REAL-BOTH, tag
                                      REGISTER-REALIZED-BOTH
10  NO-RECORD-CENSUS-W             -> 1.7.3, plus NO-RECORD-ORBIT-W
11  candidate-C cap, CHANNEL-PASS
    candidate-T only from proof    -> Field 5 "Global grade cap" and
                                      "CHANNEL-PASS cap"
12  canonical serialization        -> 2.1
    cost 41022500                  -> 2.2
    interruption rule              -> 2.2 "Interruption rule, frozen"
```

Note on correction 1, the single deliberate deviation in this file. The
mandated sentence "No dynamic evaluation of U, R, D, either window, or any
event tally has been run" is exact for the pre-pin state of
`P-QDD-INSTRUMENT-U-INDUCED-1`. It is false for a fresh identity that reuses
the same `U`, the same 180 record maps, the same five delays, the same two
windows and the same tallies, because that construction has since been executed
and its complete output is public. Writing the mandated sentence here would be
a false result-exposure declaration. This file therefore keeps the mandated
target-only algebra-audit sentence and the mandated "formal dynamic execution
count is zero" statement, both scoped explicitly to the verifier accepted for
this probe, and adds the full prior-run disclosure that the fresh identity
requires. The grade cap of Field 5 is the consequence. This deviation needs an
explicit owner ANO or a replacement wording.
