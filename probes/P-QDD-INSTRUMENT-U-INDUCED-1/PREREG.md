# P-QDD-INSTRUMENT-U-INDUCED-1 preregistration

Date: 2026-08-16

Author of record: A. M. Thorn

Status: ACCEPTED protocol, awaiting its immutable public pin. No scientific
result is earned by this file. The owner approved blocks B1 through B4 on
2026-08-16 in issue #395. No formal gate may run before this accepted file and
the accepted verifier are both present at an immutable pin, that pin is pushed,
and both files are read back from the public remote.

Public claim lock: issue #395.

Branch: `probe/P-QDD-INSTRUMENT-U-INDUCED-1`.

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
`(q,r)` as the pointer. Does the fiber, read through a frozen finite class of
two-cell record maps at frozen delays, realize the frozen ordered effect pair
`(E_low,E_high)` and its occurrence law exactly on frozen finite public
windows, and what post-state object does `U` induce on that split?

The apparatus dynamics is not chosen for this probe. It is the registered `U`
of Canon v49 sections 2 and 3, which predates the effect pair in the public
record. The record class, delays, windows and seed sets below mention neither
`E_low`, `E_high`, the Born pairing, nor any occurrence value.

## Mandatory result-exposure disclosure

No prior run, transcript, count, hash or witness search exists for this probe.
Discovery context only: an analysis conversation of 2026-08-16 identified from
the displayed Canon formulas that the six checkpoint coordinates split as
piston plus fiber and that the fiber update reads the piston only through the
selector. No computation was executed. Formal execution count of the accepted
verifier is zero at this pin candidate.

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
one orientation `0`. Thus there are `1 + 2*312 = 625` oriented pre-cells.
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

Consequence (delay one). `f(x_(k+1))` is a function of
`(f(x_k), theta_k, sum pi(x_k) mod 5)`. Every piston-to-fiber influence at
delay one passes through the selector; at longer delays the piston history
enters through later selector values. No claim about delays `d >= 2` is made
here; those are measured.

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

### 1.5 Frozen record class R and delays D  (owner ANO B1, issue #395)

```text
Lambda_0 = ((1,0), (0,1), (1,1), (1,2), (1,3), (1,4))        ordered six F_5-functionals
lambda_(alpha,gamma)(q, r) = alpha q + gamma r mod 5           modulo scalars
S ranges over the 30 nonempty proper subsets of F_5
rho_(lambda,S)(q, r) = LOW  if lambda(q, r) in S,  HIGH otherwise
R = { rho_(lambda,S) },   |R| = 6 x 30 = 180 two-cell record maps
D = {1, 2, 3, 4, 5}       read delays
```

Subsets are numbered by masks `1..30`; bit `i` means `i in S`. Enumeration is
`Lambda_0` order, mask ascending, delay ascending. Maps compose rightmost
first. The commutator convention is
`[g,h]=g o h o g^(-1) o h^(-1)`, and `T_delta(x)=x+delta mod 5`.

Event semantics. The event at time `k` is the step `x_k -> x_(k+1)`. Its
pre-vector is `v = beta(x_k)`. The register is read at time `k + d`, giving
the outcome `b = rho(f(x_(k+d)))`; the accompanying post-vector is
`v' = beta(x_(k+d))`. No ready state and no reset are assumed: the fiber is a
refreshable register, and every checkpoint reads LOW or HIGH.

Complete enumeration rule: every `(rho, d)` in `R x D` is evaluated and
reported. No member is selected by looking at counts. Complements
`S <-> F_5 \ S` are both in `R`, so the ordered pair (LOW, HIGH) is covered
without a separate swap rule.

### 1.6 Frozen sampling semantics  (owner ANO B2, issue #395)

```text
S-single  every seed x_0 in F_5^6, orbit from omega_0 = (0, x_0),
          window W = [512, 2048)   (the Law_W precedent, 1536 steps)
S-long    seeds S2 = { x_0 : f(x_0) = (0,0) } (625 seeds, ready fiber),
          window W2 = [2048, 16384)
S-census  control only: the S-single counts summed over all 15625 seeds
```

Counts, for a seed `x_0`, window `W*`, class `c`, orientation `eps`, record
`rho`, delay `d`:

```text
N_c        = #{ k in W* : cls(x_k) = c }
L_(c,rho,d) = #{ k in W* : cls(x_k) = c, rho(f(x_(k+d))) = LOW }
N_(c,eps)   = #{ k in W* : (cls(x_k),ori(x_k)) = (c,eps) }
L_(c,eps,rho,d)
             = #{ k in W* : (cls(x_k),ori(x_k)) = (c,eps),
                               rho(f(x_(k+d))) = LOW }
```

Premise statement. The single-orbit read is the long-window premise P2 of
DRIFT-IS-THE-READ; here it is used only as a frozen finite-window predicate.
No limit `N -> infinity` is asserted or established by any window in this
probe. `SAMPLING NOT PROVIDED` remains the only sampling statement beyond
exact finite-window counts.

### 1.7 Realization predicate and induced-object maps  (owner ANO B3, issue #395)

Class-averaged and orientation-resolved realization on a window for one seed:

```text
REAL-CLASS(rho,d;x_0,W*) iff for every nonzero c with N_c > 0:
                             L_(c,rho,d)/N_c = w_low(c)/m(c)
REAL-ORIENT(rho,d;x_0,W*) iff for every nonzero oriented pre-cell (c,eps)
                              with N_(c,eps)>0:
                              L_(c,eps,rho,d)/N_(c,eps)=w_low(c)/m(c)
REAL(rho,d;x_0,W*)       iff REAL-CLASS and REAL-ORIENT both hold exactly in Q
```

`REAL-ORIENT` prevents a false success obtained by averaging unequal `+` and
`-` rates. The target-free raw tables are formed and hashed completely before
`m`, `w_low`, `w_high`, `E_low`, `E_high` or `occ` is consulted. Only the
second evaluation phase may compare the frozen raw signatures with the target.
For each visited oriented pre-cell, the 180 LOW counters are accumulated during
the event loop in one packed integer, with one 31-bit lane per record map. The
class-collapsed counter is an exact packed sum of its oriented counters. For
each `(d,lambda,pre-cell)` Phase A retains only the first packed 30-subset count
block together with its event total, and a lane mask marking which subset rates
ever differ from the first by exact cross multiplication. In Phase B a subset
passes the universal seed quantifier exactly when its lane is unmarked and its
first rate equals the target. This bounded summary is logically equivalent to
retaining all seed signatures. Once all 30 lanes are marked, later signatures
cannot change any predicate and are skipped. ZERO-class differences are
retained for C8 but can never activate this shortcut, because ZERO is outside
both REAL quantifiers.

Per pair `(rho, d)`:

```text
REAL-SINGLE(rho,d)  iff  REAL(rho,d; x_0, W)  for all 15625 seeds
REAL-LONG(rho,d)    iff  REAL(rho,d; x_0, W2) for all 625 seeds in S2
REAL-CENSUS(rho,d)  iff  the summed counts satisfy the same equality
                         for every nonzero class with summed N_c > 0
```

Record-information predicate (falsifier F1 shape):

```text
INFO(rho,d)  iff  the census conditional table  c -> L_(c,rho,d)/N_c
                  is not constant over the nonzero classes with N_c > 0;
                  with fewer than two applicable classes INFO is false
```

Induced post-object, per `(rho, d)`, from the census joint tallies of
`(cls(x_k), ori(x_k), f(x_(k+d)), cls(x_(k+d)))` over W. Target
classification uses only visited nonzero pre-classes; ZERO-input behavior is
reported separately and never used to satisfy a target condition:

```text
Supp(c, b)   = set of post-classes c' occurring with visited nonzero pre-class c
               and outcome b
FUNCTIONAL   iff |Supp(c,b)| = 1 for every such (c,b) with at least one event;
               ZERO pre-input is excluded and reported separately
Dbar(c, b)   = average of dens(v') over the events with pre-class c, outcome b,
               and m(v') != 0; the number of ZERO posts is counted separately
POST-UNDEFINED-OR-ZERO iff some visited nonzero input/positive-target branch
               has no event or has any ZERO post; any event on a zero-target
               branch is also in this category
POST-PURE-STRICT iff no undefined/zero condition occurs, at least one nonzero
               post-object is defined, and rank Dbar(c,b)=1 for every defined
               applicable branch
POST-MIXED   iff no undefined/zero condition occurs and some defined applicable
               Dbar(c,b) has rank different from one
```

`Dbar(c,eps,b)` is also formed separately for both orientations. For a class
whose two oriented pre-cells are both visited, `ORIENT-POST-COHERENT` requires
the two branch-event domains to agree; on every present branch their ZERO-post
fractions and defined orientation-resolved post objects must agree. A pair with
no defined nonzero post-object is not POST-PURE. The three
pair tags `POST-PURE-STRICT`, `POST-MIXED`, and `POST-UNDEFINED-OR-ZERO` form a
partition of all 900 pairs, with undefined/zero taking precedence over purity.

For the exact implementation, write `P(v)=v v^T/m(v)`, so
`dens(v)=P(v)G`. The ten symmetric entries of the weighted sum of `P(v')` are
stored as scaled integers with one exact common denominator; multiplying the
average by `G` reconstructs the displayed `Dbar` exactly. Moreover
`G=I_4-(1/5)11^T` is positive definite, with eigenvalues `1,1,1,1/5`.
Therefore a positive average of the post densities has rank one exactly when
all nonzero post-vectors in its support are rationally collinear. The verifier
tests this through canonical direction bitsets and reconstructs full rational
matrices wherever orientation coherence or C7 requires them.

Family membership, decided only for `(rho, d)` that are FUNCTIONAL or satisfy
REAL-SINGLE, using the frozen L4 family of P-QDD-INSTRUMENT-NONSELECTION-1:

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
spanned by some `w` in `ker(sum)`; write `u = u_r r_v + u_f f_v + u_g g_v`
and `w = w_r r_v + w_f f_v + w_g g_v`; membership holds iff there is a
rational `mu != 0` with `w_g = mu u_g`, `w_r^2 + w_f^2 = mu^2 (u_r^2 + u_f^2)`
and `(w_r, w_f) = mu (c u_r - s u_f, s u_r + c u_f)` for a rational point
`(c, s)` on the unit circle with `c != -1`; then `t = s/(1+c)`. All steps are
exact rational arithmetic; the exhibited `t` is printed.

Pair-level frozen-family membership requires one common rational parameter
`t` for the HIGH branch across every applicable nonzero input class of that
pair and across both orientations. Each orientation contributes either all of
`Q`, at most two rational candidates, one rational candidate, or the empty
set; the exact sets are intersected. Per-class choices do not constitute one
instrument. The complete finite common candidate set is printed. If the
intersection is all of `Q`, the verifier prints `ALL_Q` and the canonical witness
`t=0`. Every candidate is checked again by reconstructing the full normalized
matrix. The image direction is canonicalized by clearing denominators, dividing
the integer gcd and making its first nonzero component positive.

LOW must pass on every applicable nonzero class and orientation. The branch
rules are frozen:

```text
target weight = 0:  any event -> OUTSIDE-FAMILY; no event -> no post test
target weight > 0:  no event or any ZERO post -> OUTSIDE-FAMILY;
                    otherwise Dbar must exist and equal the frozen target
```

Seed dependence (falsifier F4 shape): the number of triples `(rho, d, c)`,
including `c=ZERO`, for which two seeds visiting `c` in W have different
class-averaged `L/N` is reported. Orientation dependence is reported separately
as the number of `(rho,d,c)` whose `+` and `-` census rates differ when both
are present.

## Field 2: code

Accepted verifier, frozen together with the accepted preregistration:

```text
probes/P-QDD-INSTRUMENT-U-INDUCED-1/verify.py
```

Requirements:

```text
Python standard library only
integers and Fraction only; no float, Decimal or external dataset
deterministic order of enumeration: seeds lexicographic in (p1,p4,p1p,p4p,q,r),
  R lexicographic in (Lambda_0 index, subset bitmask), D ascending
stdout: gate lines, all counts and tags of Field 5, and SHA-256 of the
  canonical serialization of every joint tally table (tables themselves are
  not printed)
```

The serialization is architecture-independent: deterministic table labels
followed by lexicographically ordered nonzero integer entries in fixed-width
big-endian fields. The pre-cell field is the oriented ID of 1.2. Separate hashes
cover the single-seed tables, long-seed tables, single-window joint table,
long-window joint table and both aggregate fiber tables. Zero entries are
omitted canonically. A seventh root hash commits to those six labeled hashes in
that displayed order. Dense joint counters are unsigned 32-bit cells: their
absolute per-cell bounds are the total events per delay, respectively
`15625*1536 = 24000000` and `625*14336 = 8960000`, both strictly below `2^32`;
the verifier checks the storage widths and these bounds before allocation.

Memory and traversal are frozen as follows. LONG is formed, hashed and released
before SINGLE is allocated, so at most one dense five-delay joint dataset is
resident in Phase A (`5*625*25*313*4 = 97812500` bytes). No unbounded cache or
set of seed signatures is permitted. Each fiber value has one frozen packed
180-lane increment, so an event adds one Python integer rather than rescanning
`6*25` bins for each visited group. The 31-bit lane layout uses bit 30 as a
guard, bit 29 as the equality-test bias, and the lower bits for counts and cross
products. The verifier audits `14336^2 < 2^29`, audits the target numerator and
denominator products against the same bound, and reads lane equality by guarded
broadword subtraction without inter-lane carry or borrow. In Phase B each of the
25 fiber cells is binned once into the five residues of a chosen `lambda`; the
30 record masks are then exact subset sums and support unions of those five bins.
Python dictionaries are not a representation of the joint table.

The verifier audits: the transcription of the generators and relations (1.1),
the split and the 25/313/22 expectations (1.2, 1.3), S1 and S2 exhaustively over
all 15625 checkpoints (including both drive bits where applicable), and S3 by
the two deterministic witness searches of 1.4. It then forms the counts of 1.6
and evaluates every predicate and map of 1.7. The
predicates of 1.7 are complete enumerations; no finite sample replaces a
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
C3  S1, S2 audited over all checkpoints; S3 witnessed.
C4  Every (rho, d) in R x D evaluated on S-single, S-long and S-census;
    the sets of pairs satisfying REAL-SINGLE, REAL-LONG, REAL-CENSUS printed
    in full (possibly empty); REAL includes orientation resolution. The packed
    lane transcription and all no-carry/no-borrow bounds reproduce exactly.
C5  INFO evaluated for every (rho, d); the number of pairs with INFO true printed.
C6  FUNCTIONAL, ORIENT-POST-COHERENT and the strict partition
    POST-PURE-STRICT / POST-MIXED / POST-UNDEFINED-OR-ZERO are evaluated for
    every (rho,d); counts printed. ZERO pre-input behavior is printed separately.
C7  Family membership decided exactly once for every (rho, d) that is
    FUNCTIONAL or REAL-SINGLE, and for no other pair, with exhibited t where it
    exists. The evaluated-name set, member set and outside set are audited as an
    exact disjoint partition of the eligible set.
C8  Seed-dependence including ZERO and orientation-dependence counts printed.
C9  Six labeled table hashes and their root hash printed; both architectures
    must agree byte for byte on the whole stdout.
```

Any hidden input, floating tolerance, post hoc restriction of `R x D`, use of
`E_low`, `E_high` or `occ` before the counts are formed, or an unnamed
L5-to-L6 lift is STOP.

## Field 5: failure threshold and scientific routing  (owner ANO B4, issue #395)

No tolerance exists.

```text
ARCH-STOP
  C1, C2 or C3 fails: transcription or integrity error; no scientific reading.

CHANNEL-PASS
  S1, S2, S3 audited. Structural statement about the registered coupling.

REGISTER-REALIZED-W        at least one (rho,d) satisfies REAL-SINGLE
NO-REALIZATION-W           no (rho,d) satisfies REAL-SINGLE
LONG-REALIZED-W2 / LONG-NO-REALIZATION-W2       same for REAL-LONG on S2
CENSUS-REALIZED-W / CENSUS-NO-REALIZATION-W     control only

NO-RECORD-W                INFO false for every (rho,d)        (F1 shape)
INSTRUMENT-FUNCTIONAL-k    number k of (rho,d) that are FUNCTIONAL   (F2 shape)
ORIENT-POST-COHERENT-k
POST-PURE-STRICT-k / POST-MIXED-k / POST-UNDEFINED-OR-ZERO-k
                           exact partition of all 900 pairs
FAMILY-MEMBER-k / OUTSIDE-FAMILY-k   counts, with exhibited t values
SEED-DEPENDENT-k           the count of 1.7                     (F4 shape)
ORIENTATION-DEPENDENT-k    unequal +/- census rates where both occur

STOP
  authority, pin, verifier integrity, completeness, security or layer
  discipline fails.
```

Scientific routing, fixed before the pin:

- REGISTER-REALIZED-W together with LONG-REALIZED-W2 and CHANNEL-PASS earns
  at most a finite-window realization statement on frozen public windows,
  candidate grade D or C at a later reviewed fold. It does not close O1: no
  limit is proved. It does not close O2 by itself: the record map is exhibited
  from a frozen complete class, and its status as a physical selector is a
  separate owner decision. Both realization tags already require the
  orientation-resolved test; quotient averaging cannot earn them.
- NO-REALIZATION-W leaves O1 and O2 at STOP. It is not a negative closure of
  `QDD-INSTRUMENT-APPARATUS`: finite windows do not refute a limit law, and
  the class {registered `U` on the 4 + 2 split, read through R at D} is not the
  complete admissible physical class of the row.
- NO-RECORD-W is the sharpest negative reading available here: on the frozen
  windows the fiber cell distribution carries no piston-class information for
  any member of R at any delay in D. It is recorded as a structural finding
  about this split and this record class only.
- CHANNEL-PASS is claimable independently of every other tag.

The threshold and scope may not move after the pin.

Falsifier map from the owner analysis of 2026-08-16:

```text
F1  fiber holds no record          -> NO-RECORD-W
F2  induced map not instrument-form -> INSTRUMENT-FUNCTIONAL-0 with
                                       POST-MIXED or POST-UNDEFINED-OR-ZERO
F3  effects not realized            -> NO-REALIZATION-W (and LONG, CENSUS variants)
F4  seed dependence                 -> SEED-DEPENDENT-k with k > 0
F5  weights not realized            -> identical to F3 in this discrete setting:
                                       realizing the ordered effects means realizing occ
```

## Field 6: action layer

```text
L1  exact autonomous dynamics and channel statements
L4  induced apparatus classification on the frozen split
L5  finite-window realized-event stream and exact counts
L6  none: no normalized measure, no limit, no SI statement
```

## Scope firewall

This probe does not:

- close `QDD-INSTRUMENT-APPARATUS [O]` in either direction;
- modify `QUADRATIC-DECODER-DATA [O]` or any DEF-QDD-* definition;
- choose a coupling: `U` is the registered update, unchanged;
- define the record class, delays, windows or seeds with reference to
  `E_low`, `E_high`, the Born pairing or any occurrence value;
- select one `(rho, d)` before the complete enumeration is reported;
- average `beta` and `-beta` before the orientation-resolved realization test;
- assert existence of any long-window limit or an L6 measure;
- adopt `G`-positivity, minimal disturbance, decoherence or collapse as a premise;
- derive the effect pair, the Born pairing or the architecture from `J`;
- fill a decoder-completion-contract field;
- claim that a second-copy (composition) apparatus is excluded or required.

## Formal sequence after the pin

1. Owner ANO on blocks B1 to B4, recorded on claim-lock issue #395. COMPLETE.
2. Push the accepted `PREREG.md` and `verify.py` on the claimed branch.
3. Read both files back from the public remote; record the immutable pin,
   SHA-256 and byte counts on the issue.
4. Only then execute the accepted verifier for the first formal run.
5. Commit exact `EXPECTED.txt`, neutral `RUN.md` and `RESULT.md` without
   changing the pinned preregistration or verifier.
6. Open one pull request changing only
   `probes/P-QDD-INSTRUMENT-U-INDUCED-1/`.
7. Require GitHub x86_64 and aarch64 jobs to reproduce the same committed
   `EXPECTED.txt` byte for byte.
8. A later separate reviewed Canon fold may register only the status and
   scope actually earned by this probe.
