# P-PISTON-RELATIONAL-WEDGE-1 preregistration

Status: `PREREGISTERED CANDIDATE / RESULT-EXPOSED / NO FORMAL RUN`

This revision is based on Public Canon v52 and, following the owner verdict
of 2026-08-18, carries only the rational piston half of the earlier
combined draft. Everything on the integral QPAIR carrier lives in the
sibling draft `P-QPAIR-RELATIONAL-AREA-1`. No bridge between the two
carriers is stated, used, or implied here; a bridge, if ever, is a third
probe.

This document freezes one exact L1 probe on the frozen public piston
carrier `V_eff` of Route A: a 2 x 2 reshape of the balanced piston that the
two linear kernel generators select, the integer wedge of that reshape, the
statement that the frozen `Tr_4` occurrence-weight map does not separate
that wedge although the public quadratic record carries it through its total
weight and density fields, and an exact census of the wedge over the 625
pistons. It contains no verifier output and earns no scientific or Canon
status. Together with `verify.py`, it is the complete zero-run initial pin.
Formal execution is forbidden until that immutable commit and both file
hashes read back from the public remote.

## Public identity, authority, and action layer

```text
program owner:       relational-wedge lane, piston half (NON-CANONICAL)
target rows:         PISTON-2X2-RESHAPE-WEDGE                 (new, ceiling T)
                     QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND    (new boundary row,
                                                               ceiling T, with the
                                                               three REQUIRES edges below)
                     PISTON-WEDGE-LIFT-CENSUS                 (new, ceiling T for
                                                               R5.i-R5.iv; R5.v is
                                                               REPORT-only, no row)
proposed items:      DEF-PISTON-2X2-RESHAPE, DEF-PISTON-WEDGE
probe:               P-PISTON-RELATIONAL-WEDGE-1
sibling probe:       P-QPAIR-RELATIONAL-AREA-1 (separate carrier, separate pin)
public lock:         issue #425
probe owner:         A. M. Thorn / delegated session piston_relational_wedge
branch:              probe/P-PISTON-RELATIONAL-WEDGE-1
path:                probes/P-PISTON-RELATIONAL-WEDGE-1/
initial base:        91e11e4f4db01d1badeabfea0a361972a6d4f2ea (public main = canon-v52)
Public Canon tag:    canon-v52
content commit:      6fc6923f727edacf55d511ec30eee2c7461ac497
Canon SHA-256:       b496e4e73a2b06167a981b75a5ea651591db383a9c7f222e0075eb8bb6f1ee03
Canon bytes:         261476
action layer:        L1 only (exact carrier algebra, finite exact census)
mode:                result-exposed, proof-first; verify.py is an exact finite audit
formal runs:         none; verify.py neither imported nor executed
static check:        Python 3.13 ast.parse PASS at pin; no import, bytecode
                     compilation, or execution
```

Explicit dependency edges proposed for the fold (relation `REQUIRES`):

```text
PISTON-2X2-RESHAPE-WEDGE               REQUIRES  KERNEL-WEDGE-AFFINITY
                                                 (linear/affine split of a,b,c,d,e)
PISTON-2X2-RESHAPE-WEDGE               REQUIRES  DEF-QDD-BALANCED-PISTON, DEF-QDD-QPAIR,
                                                 DEF-QDD-TRANSPOSE (the carrier and slot)
PISTON-2X2-RESHAPE-WEDGE               REQUIRES  QPAIR-SYM2-TENSOR-DEFECT restricted to
                                                 K = Q (consistency clause R3.iv only)
QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND  REQUIRES  QDD-PROJECTOR-PAIR-TR4
                                                 (the closed forms m, w_low, w_high)
QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND  REQUIRES  QDD-ALGEBRAIC-FACTORIZATION
                                                 (normalized pair; injectivity of the
                                                 record on QCarrier_QDD)
QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND  REQUIRES  PISTON-2X2-RESHAPE-WEDGE
PISTON-WEDGE-LIFT-CENSUS               REQUIRES  PISTON-2X2-RESHAPE-WEDGE
```

No edge to `QUADRATIC-DECODER-DATA [O]` or `QDD-INSTRUMENT-APPARATUS [O]`;
both stay exactly as open as they are.

Collision readback at claim lock #425 (main `91e11e4`): no other registry,
normative, probe-directory, issue or branch entry collides with this probe or
its target rows. The branches `notes/c-entanglement-relational-wedge-1-n` and
`-duplicate` and issues #419 and #422 are non-canonical linguistic lineage
only; the `KERNEL-WEDGE-*` rows name a different object, the cell-pair wedge.

Lineage and novelty boundary, none of which is a logical premise beyond the
exact statements quoted in the equation field: `DEF-QDD-BALANCED-PISTON`,
`DEF-QDD-QPAIR`, `DEF-QDD-DAGGER`, `DEF-QDD-TRANSPOSE`, `DEF-QDD-GRAM`,
`DEF-QDD-PROJECTOR-LOW/HIGH` supply the frozen carrier, slots, Gram matrix
and effect pair; `QDD-PROJECTOR-PAIR-TR4 [T]` supplies the closed forms;
`QDD-ALGEBRAIC-FACTORIZATION [T]` supplies the record and its injectivity on
`QCarrier_QDD`; `QDD-QCARRIER-DIAGONAL-BOUNDARY [T]` supplies
`A_dagger = A_T = v v^T`; `KERNEL-WEDGE-AFFINITY [T]` supplies the
linear/affine split of the five generators; the Canon transcription of the
generators supplies the piston actions. `QUADRATIC-DECODER-DATA [O]`,
`QDD-INSTRUMENT-APPARATUS [O]`, `QDD-INSTRUMENT-NONSELECTION [T]`, `KERNEL-WEDGE-COUPLING [T]`,
`KERNEL-WEDGE-LINEAR-STRATA [T]`, `DEF-QPAIR-SPIN-CARRIER` and every
statement on the integral cyclotomic carrier are excluded from the premises
and are not moved, strengthened, interpreted, or bridged by this probe.

## The question this probe attacks, at this carrier

```text
1  does the public piston carry a canonical 2 x 2 arrangement, and is its
   determinant a well-defined integer sign semi-invariant of the public
   linear generators, with invariant absolute value;
2  does the frozen public occurrence law of Route A separate that
   determinant, given that the public quadratic record is injective;
3  where exactly do the F_5 wedge and its balanced Z lift disagree.
```

R3 answers 1: exactly one product labeling class makes both linear
generators factor-local; its determinant `D_Z` is odd under each of them,
so `|D_Z|` and `c_Z = 2|D_Z|/|v|^2` are invariants; `D_Z` is a linear
functional on the transpose slot. R4 answers 2 in the narrow form the
owner fixed: the frozen `Tr_4` occurrence-weight map and its normalized pair
are not separating for `D_Z`, while the record's total-weight and density
fields together determine `D_Z`; it is the displayed linear functional on
the reconstructed transpose slot. R5 answers 3: on exactly 16 pistons,
all rank one modulo 5 and all sent by the lift to `c_Z = 1`.

## Result exposure

Every finite value quoted below was derived by hand in the drafting session
and reproduced by a scratch exact computation outside the repository, using
a third-party symbolic library for independence from the verifier. The
scratch script shares no code with `verify.py`:

```text
scratch A   scratch_area.py     sha256 7f1756b2e2c711dc439fcfd855748f4ba7124616f6f0efeaf79d4e1b39e893b2
            stdout              sha256 ae9dbfcc69c6597818f4701d1864954dd555c428f042314fff1bad5ed6f75ccf
```

(`scratch_area.py` also contains cyclotomic material that belongs to the
sibling probe; only its piston block is exposure for this document.) The
owner has separately reproduced the counts 145 = 129 + 16, 48, 8 and the
twelve values of `c_Z` in a one-platform review computation outside the
formal protocol; that reproduction is a review witness, not public evidence.

This probe is therefore a pinned confirmation and adversarial audit, not
blind discovery. No equation, carrier, systematic, threshold, output route,
or scope may move in response to the exposed values. `verify.py` has never
been executed or imported. Before the preparation commit and again at this
pin it passed only a Python 3.13 `ast.parse` syntax check. No helper or gate
was evaluated from the verifier. No dynamic
evaluation of `U`, no orbit, window, seed, or event tally of any kind was
run before this pin, and none is part of the probe.

## Falsifier first

A single exact counterexample to R3, R4 or R5 falsifies the corresponding
row: `a` or `b` failing to be factor-local under the frozen reshape, a
labeling count other than 8 of 24, the 8 labelings not sharing `|D_Z|`, a
sign character other than `-1` for `a` or for `b`, `D_Z` differing from the
transpose-slot functional or from `det X_p` on some piston, the singular-matrix
count modulo 5 differing from 145; the frozen closed forms failing on some
piston, the witness pair failing to have equal occurrence weights and equal
normalized pair with unequal `D_Z`, the total_weight and density fields
failing to recover `D_Z` on some record, or the density-only scale witness
failing; any of the counts 145, 129, 16, 48, 8 differing, a
`|D_Z| = 5` piston with `|v|^2 != 10`, or `c_Z` outside `[0, 1]`.

An environment or argument defect, an exception, an unexpected nonzero exit
other than the declared scientific exit 2, nonempty stderr, or a
cross-architecture byte mismatch is `STOP`, not `FALSIFIED`. Exit code map:
0 pass, 1 STOP, 2 FALSIFIED.

## The six frozen fields

### 1. Equation

#### 1.1 Carrier and public generators on the piston

Checkpoints are `x = (p1, p4, p1p, p4p, q, r) in F_5^6`; the piston is
`pi(x) = (p1, p4, p1p, p4p)`; the balanced lift is `ell(0,1,2,3,4) =
(0, 1, 2, -2, -1)` and `v = ell(pi(x)) in V_eff = ell(F_5)^4 subset Q^4`
(`DEF-QDD-BALANCED-PISTON`). The two linear generators restricted to the
piston are

```text
a  (p1, p4, p1p, p4p) -> (p4, p1, p4p, p1p),
b  (p1, p4, p1p, p4p) -> (-p1p, -p4p, -p1, -p4),
```

and `c, d, e` are strictly affine (`KERNEL-WEDGE-AFFINITY [T]`; from the
Canon transcription `d` has linear part `-I` and translation `(2,1,3,4)`,
`e` the same piston action, `c` has linear part `b_4` and a translation
`(2,1,2,1) + r(0,1,0,-1)` depending on `r`; the verifier audits only that
each of them moves the zero piston, for every `r`). The transpose slot of
`DEF-QDD-QPAIR` on `V_eff` is `A_T = v v^T` and equals the dagger slot
numerically (`QDD-QCARRIER-DIAGONAL-BOUNDARY`).

#### 1.2 Frozen definitions

```text
DEF-PISTON-2X2-RESHAPE (proposed)
    X_p = ((ell p1, ell p4), (ell p1p, ell p4p)),
    the product labeling p1 -> (0,0), p4 -> (0,1), p1p -> (1,0), p4p -> (1,1)
    of Q^4 = Q^2 tensor Q^2 (first bit: unprimed 0 / primed 1; second bit:
    piston 1 -> 0 / piston 4 -> 1).
    Admissibility: a bijection of the four piston coordinates onto {0,1}^2 is
    admissible when a flips exactly one bit on every coordinate and b flips
    exactly one bit on every coordinate, the two bits different; signs are
    ignored for admissibility.  A reshape is any admissible labeling read
    as X[first bit][second bit].
DEF-PISTON-WEDGE (proposed)
    D_Z(v) = det X_p = ell(p1) ell(p4p) - ell(p4) ell(p1p) in Z,
    D_5(x) = p1 p4p - p4 p1p in F_5,     D_Z = D_5 mod 5,
    W = the symmetric matrix with v^T W v = D_Z(v):
        W_14 = W_41 = 1/2,  W_23 = W_32 = -1/2,  all other entries 0,
    c_Z(v) = 2 |D_Z(v)| / |v|^2  for v != 0  (|v|^2 = sum ell(p_i)^2),
    A_Z(v) = c_Z^2 / 4 = D_Z^2 / |v|^4,   ZERO tag for the zero piston.
```

The frozen public occurrence-weight map on the piston is quoted from
`QDD-PROJECTOR-PAIR-TR4 [T]` with `s = sum v_i`:

```text
m = |v|^2 - s^2/5,   w_low = s^2/20,   w_high = |v|^2 - s^2/4,          (2)
normalized pair (w_low/m, w_high/m) for m != 0,
G = I_4 - (1/5) 1 1^T,   G^-1 = I_4 + 1 1^T   (DEF-QDD-GRAM),
density field  v v^T G / m   (QDD-ALGEBRAIC-FACTORIZATION record).
```

Under the reshape, a `4 x 4` matrix `M` is realigned to `Re(M)` with
`Re(M)[(i1,i2),(j1,j2)] = M[(i1,j1),(i2,j2)]`, indices in the product order
of DEF-PISTON-2X2-RESHAPE; a nonzero `M` is a simple product `M_1 tensor M_2` iff `Re(M)` has
rank one; the zero matrix has realignment rank zero.

#### Target R3. PISTON-2X2-RESHAPE-WEDGE

```text
R3.i    under DEF-PISTON-2X2-RESHAPE, a = 1 tensor sigma and
        b|piston = -(sigma tensor 1) as signed permutation matrices on
        ell(F_5)^4, both commuting with the lift; a and b commute and are
        involutions; c, d, e move the zero piston.
R3.ii   exactly 8 of the 24 bijections are admissible; they form one class
        under bit relabeling of each factor and factor exchange; |D_Z| is
        the same function on all 625 pistons for all 8; the frozen labeling
        is one of them.
R3.iii  D_Z(a v) = -D_Z(v) and D_Z(b v) = -D_Z(v) on all 625 pistons; ell is
        odd, so |D_Z| and c_Z are <a,b>-invariant; d changes |D_Z| on a
        nonzero reported number of pistons.
R3.iv   D_Z is the linear functional A_T -> (A_T)_14 - (A_T)_23 on the
        transpose slot; det(X_p X_p^T) = D_Z^2; consistency clause: over
        K = Q with V = W = Q^2 in the reshape, D_Z/2 is the kappa coefficient
        of QPAIR-SYM2-TENSOR-DEFECT (named dependency, no carrier bridge).
R3.v    D_5 = 0 on exactly 145 = 625 - |GL_2(F_5)| pistons, the
        singular-matrix count including the zero piston; D_Z = D_5 mod 5.
```

#### Target R4. QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND (boundary row)

```text
R4.i    the closed forms (2) hold on all 625 pistons and are functions of
        (s, |v|^2) alone.
R4.ii   witness pair v = (1,0,0,1), v' = (1,1,0,0): (s,|v|^2) = (2,2) for
        both, occurrence weights (m, w_low, w_high) = (6/5, 1/5, 1) for both,
        normalized pair (1/6, 5/6) for both, while D_Z = 1 against 0 and
        c_Z = 1 against 0.  Hence the frozen Tr_4 occurrence-weight map and
        its normalized pair are not separating for D_Z, |D_Z| or c_Z.
R4.iii  on the SUPPORTED branch the pair of record fields total_weight
        m and density rho = v v^T G / m determines
        v v^T = m rho G^-1; D_Z is the displayed linear functional on this
        reconstructed transpose slot. On ZERO_SUPPORT, D_Z = 0.  Thus the full public quadratic record carries the wedge;
        only the frozen occurrence weights fail to separate it.
R4.iv   density alone is scale-blind: v = (1,0,0,1) and
        2v = (2,0,0,2) have the same rho but D_Z = 1 and 4, while their
        total weights are 6/5 and 24/5.  No density-only recovery is claimed.
G1, G2  guard gates, not claims: Re(G) has rank 2 (G is not a product
        metric for the reshape, so no G-adapted normalized wedge is defined
        here) and W is outside span{I_4, 1 1^T}.  If the owner prefers a
        registered theorem for the rank statement it becomes a separate
        atomic row QDD-TR4-GRAM-NONPRODUCT; it is not folded into R4.
R4.v    REPORT-only audit output: the number of (s,|v|^2) classes on the
        625 pistons and the number of classes containing more than one value
        of |D_Z|; neither count is a field of the target row.
```

The row is a boundary statement next to `QDD-QCARRIER-DIAGONAL-BOUNDARY`.
It moves no QDD status, names no effect identifier, selects no instrument,
and says nothing about what a decoder should read.

#### Target R5. PISTON-WEDGE-LIFT-CENSUS

```text
R5.i    |D_Z| <= 8 on all pistons; exactly 8 pistons have |D_Z| = 8.
R5.ii   exactly 16 pistons have |D_Z| = 5; each has |v|^2 = 10 and c_Z = 1;
        these are exactly the pistons that are rank one modulo 5 with
        nonzero balanced wedge, so exactly 129 pistons have D_Z = 0 (128
        nonzero and the zero piston) and 145 = 129 + 16.  The disagreement
        exists because ell : F_5 -> {-2,-1,0,1,2} is not a ring
        homomorphism.
R5.iii  exactly 48 pistons have c_Z = 1, namely those with X_p X_p^T =
        lambda I, lambda > 0; the 16 of R5.ii are among them.
R5.iv   0 <= c_Z <= 1 on all 624 nonzero pistons and A_Z = c_Z^2/4.
R5.v    REPORT-only audit output: the number of distinct values of c_Z and
        the full multiset over the 624 nonzero pistons; neither is a field of
        PISTON-WEDGE-LIFT-CENSUS and no separate status is earned.
```

#### Wording firewall

"Piston wedge" names `D_Z` and `D_5`; it is a wedge inside one checkpoint
and is not the cell-pair wedge `w_ij` of the `KERNEL-WEDGE-*` rows. "Not
separating" means: the map takes equal values on the exhibited pair with
unequal `D_Z`. The sentence "the decoder does not read the wedge" is
forbidden: the public record is injective on `QCarrier_QDD` and the
transpose slot carries `D_Z`. `c_Z` is a normalized wedge ratio; the words
"concurrence", "entanglement", "joint state", "two-qubit" and "measurable"
do not occur in the theorem layer of this probe. DEF-PISTON-2X2-RESHAPE is
an arrangement selected by `a` and `b`; R3.ii is its uniqueness within the
declared admissibility class only; no sentence says which physical systems
the two factors are. The consistency clause R3.iv applies a
characteristic-not-two theorem to `K = Q`; it imports nothing from the
integral cyclotomic carrier.

#### What is not claimed

No BELL-CAUSAL-ACCOUNTING row is created. No physical reading of `X_p`, no
L2 to L6 statement, no instrument, no
event stream, no measure, no effect identifier, no change to any QDD row,
no statement that a decoder must or will read `D_Z`, no derivation of the
reshape from `J`, no dynamic evaluation of `U`, no G-normalized wedge, no
bridge to `O_K^2`, no Bell or CHSH statement, and no SI statement.

### 2. Code

`verify.py`, Python standard library only, exact integer and
`fractions.Fraction` arithmetic for every scalar, no float anywhere, no
random choice, no file input, no arguments, no network, canonical ASCII
stdout with final newline, empty stderr, runtime under 120 seconds from the
repository root under

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-PISTON-RELATIONAL-WEDGE-1/verify.py
```

Gate list, in order:

```text
I01  environment (interpreter, no arguments, 625 pistons)
R3a  a = 1 tensor sigma, b = -(sigma tensor 1), lift compatibility on 625,
     c/d/e move the zero piston, a and b commute and are involutions
R3b  admissible labelings 8 of 24, one class, common |D_Z|, frozen reshape
     admissible and D_Z = det X_p
R3c  sign characters of a and b on 625, ell odd, <a,b>-invariance of |D_Z|
     and c_Z, d changes |D_Z|
R3d  D_Z equals the transpose-slot functional (14)-(23), equals 2 kappa_coef
     over Q, det(X_p X_p^T) = D_Z^2, on all 625
R3e  singular-matrix count 145 modulo 5, |GL_2(F_5)| = 480,
     D_Z mod 5 = D_5
R4a  closed forms (2) on 625 and their dependence on (s,|v|^2) alone
R4b  witness pair: equal (s,|v|^2), equal occurrence weights, equal
     normalized pair, unequal D_Z and c_Z; G^-1 = I + 1 1^T; total_weight
     together with density determines D_Z on all records through the
     reconstructed transpose slot; a scale pair proves that density alone
     does not
G1   guard: realignment rank of G is 2
G2   guard: W outside span{I, 1 1^T}; W is the quadratic form of D_Z
R5a  |D_Z| <= 8, count 8 at the maximum
R5b  count 16 at |D_Z| = 5, all with |v|^2 = 10 and c_Z = 1; singular
     modulo 5 iff D_Z in {0, +-5}; count 129 with D_Z = 0;
     145 = 129 + 16
R5c  count 48 at c_Z = 1 and characterization X_p X_p^T = lambda I; the 16
     are among the 48
R5d  bounds of c_Z on all 624 nonzero pistons; A_Z = c_Z^2/4
REPORT lines (no gate and no row/status): d-change count, (s,|v|^2) class
     counts, distinct c_Z values, c_Z multiset, value set
terminal line: RESULT PASS | RESULT FALSIFIED | STOP <exception>: <detail>
```

### 3. Carrier or data

The 625 pistons `F_5^4` with the balanced lift; the piston actions of
`a, b, c, d, e`; the frozen matrices `G, E_low, E_high` and the closed forms
transcribed from Canon v52. No external data, measurement, fit, orbit,
window, seed, or stochastic sample; no cyclotomic carrier.

### 4. Systematics

```text
S1  The reshape is frozen as DEF-PISTON-2X2-RESHAPE; admissibility ignores
    signs.  Factor exchange transposes X_p and fixes D_Z; bit relabelings
    negate D_Z at most.  Only |D_Z|, c_Z and A_Z are labeling invariants.
S2  c_Z is normalized by the coordinate form |v|^2 (a product metric for the
    reshape), not by the trace pairing m = v^T G v; guard G1 records that
    G is not a product metric.  No G-normalized wedge is defined or
    reported.
S3  D_5 lives in F_5 and has no size; the Z lift is the balanced ell of
    DEF-QDD-BALANCED-PISTON.  R5.ii is the exact locus where the two
    disagree.
S4  R3.iv's consistency clause uses QPAIR-SYM2-TENSOR-DEFECT only as a
    theorem over K = Q with the frozen conventions (Sym^2 as the +1
    eigenspace, R orders (V_1, V_2, W_1, W_2), the wedge not halved,
    P_-- = (1-alpha)(1-beta)/4); nothing about O_K^2 enters.
S5  "Not separating" is proved by one exhibited pair; the REPORT-only class
    counts quantify it and are neither thresholds nor registered fields.
S6  Reported values (REPORT lines) are frozen only in EXPECTED.txt after the
    formal run.  The drafting expectations below are exposure, not
    thresholds, claims, or status-bearing output.
S7  The first formal run is local Linux/aarch64.  The required pull-request
    workflow reruns the pinned verifier on x86_64 and aarch64 and requires
    the aggregate check.  Computation status rests on byte identity; T can
    come only from the written proofs the verifier audits.
```

### 5. Failure threshold

Exact and binary. Any scientific falsifier below records the affected row
`F`; no threshold may be moved after the pin.

```text
F3  a or b is not factor-local under the frozen reshape, or the admissible
    labeling count is not 8, or the 8 labelings do not share |D_Z|, or
    D_Z(av) != -D_Z(v) or D_Z(bv) != -D_Z(v) on some piston, or D_Z differs
    from the transpose-slot functional, from 2 kappa_coef over Q, or from
    det X_p on some piston, or det(X_p X_p^T) != D_Z^2, or the singular-
    matrix count modulo 5 is not 145.
F4  the closed forms (2) fail on some piston or depend on more than
    (s,|v|^2), or the witness pair has unequal occurrence weights or unequal
    normalized pair or equal D_Z, or the total_weight and density fields
    fail to recover D_Z on some record, or the density-only scale witness
    fails.  (G1, G2 failing is integrity STOP for the guard, not
    a scientific falsifier of R4.)
F5  |D_Z| > 8 somewhere, or the counts (8 at |D_Z| = 8; 16 at |D_Z| = 5,
    all with |v|^2 = 10 and c_Z = 1; 129 with D_Z = 0; 48 with c_Z = 1)
    differ, or singularity modulo 5 is not equivalent to D_Z in
    {0, +-5}, or
    some c_Z lies outside [0, 1], or some piston with c_Z = 1 does not
    satisfy X_p X_p^T = lambda I, or A_Z != c_Z^2/4 somewhere.
```

A verifier, expected-output, or hash mismatch, any execution before the
immutable pin, a float, an unapproved dependency, a QDD status or effect-
identifier statement, any cyclotomic-carrier statement, or wording that
crosses the firewall is an integrity or scope `STOP`, not a rewritten
scientific threshold.

### 6. Action layer

`L1` only: exact carrier algebra and a finite exact census on the frozen
public piston carrier. R4 is an L1 boundary statement about the frozen
public L1 closed forms; it makes no L4 apparatus, L5 event, or L6 measure
statement.

## Proofs

### Proof of R3

`R3.i`. In the product labeling, `a` maps `(t, 0) <-> (t, 1)` for both `t`,
which is `1 tensor sigma`; `b` maps `(0, i) -> -(1, i)` and
`(1, i) -> -(0, i)`, which is `-(sigma tensor 1)`. `ell(-k mod 5) =
-ell(k)` for every `k`, so both commute with the lift. `a` and `b` are
signed coordinate permutations acting on different bits, hence commute and
square to one. `c, d, e` send the zero piston to `(2,1+r,2,1-r)`,
`(2,1,3,4)`, `(2,1,3,4)`, none zero. QED

`R3.ii`. An admissible labeling assigns to `p1` one of four labels and to
`a` one of two bits; then `p4`, `p1p`, `p4p` are forced by the flip
conditions, and consistency holds because `a` and `b` commute and generate a
Klein group acting simply transitively on the four coordinates. This gives
`4 x 2 = 8` labelings; the four choices are the bit relabelings of the two
factors and the two choices of the `a`-bit are the factor exchange.
Relabeling one factor bit negates `D_Z`; exchanging factors transposes `X_p`
and fixes `D_Z`. QED

`R3.iii`. `a` swaps the columns of `X_p`, `b` swaps the rows and negates all
entries; each has determinant `-1` on its factor, and the global sign of `b`
is squared away, so `D_Z` changes sign under each. For
`p=(1,0,0,0)`, `D_Z(p)=0`, while `d(p)=(1,1,3,4)` has balanced lift
`(1,1,-2,-1)` and `D_Z(d(p))=1`; hence `d` changes `|D_Z|`. QED

`R3.iv`. `(v v^T)_14 = v_1 v_4` and `(v v^T)_23 = v_2 v_3`, so the
functional is `det X_p`. `det(X_p X_p^T) = (det X_p)^2`. For the consistency
clause, the proof of QPAIR-SYM2-TENSOR-DEFECT over `K = Q`: only the four
ordered terms `ad, da, bc, cb` of `R(x tensor x)` survive `P_--`, projecting
to `+kappa/4, +kappa/4, -kappa/4, -kappa/4`, hence coefficient
`(ad - bc)/2 = D_Z/2`. QED

`R3.v`. `D_5 = 0` iff `X_p mod 5` is singular; there are
`|GL_2(F_5)| = (25-1)(25-5) = 480` invertible matrices among `625`. `ell(k)
= k mod 5` gives `D_Z = D_5 mod 5`. QED

### Proof of R4

`R4.i` is `QDD-PROJECTOR-PAIR-TR4 [T]`, re-audited; the closed forms are
polynomials in `s` and `|v|^2` only. `R4.ii` is the displayed computation:
`s = 2`, `|v|^2 = 2`, `m = 2 - 4/5 = 6/5`, `w_low = 4/20 = 1/5`,
`w_high = 2 - 1 = 1`, normalized `(1/6, 5/6)`, for both pistons, while
`D_Z = 1` and `0`. `R4.iii`: `G` is invertible with `G^-1 = I + 1 1^T`
(since `(1 1^T)^2 = 4 (1 1^T)`). On SUPPORTED records,
`m (v v^T G/m) G^-1 = v v^T`, whose entries `(1,4)` and `(2,3)` give
`D_Z`; ZERO_SUPPORT has `v=0` and `D_Z=0`. For `R4.iv`, replacing
`v=(1,0,0,1)` by `2v=(2,0,0,2)` multiplies `m` and `v v^T G` by four, so
rho is unchanged, while `D_Z` changes from 1 to 4. Guards: `G = I tensor I -
(1/5)(1 1^T) tensor (1 1^T)` in the reshape, and `{I, 1 1^T}` are linearly
independent `2 x 2` matrices, so the operator-Schmidt rank of `G` is `2`;
`W` has zero diagonal and a non-constant off-diagonal pattern, so it is not
in `span{I, 1 1^T}`. QED

### Proof of R5

Entries of `v` lie in `{0, +-1, +-2}`, so `|D_Z| <= 4 + 4 = 8`, with
equality iff `{v_1 v_4, v_2 v_3} = {4, -4}` or `{-4, 4}`: `2 x 2 x 2 = 8`
sign patterns. `|D_Z| = 5` forces `{v_1 v_4, v_2 v_3}` to be `{4,-1}` or
`{1,-4}` up to a common sign: four ordered product pairs, each product `+-4`
realized by two ordered entry pairs and each `+-1` by two, so
`4 x 2 x 2 = 16` pistons, all with entries of squares `4,4,1,1` and
`|v|^2 = 10`, hence `c_Z = 10/10 = 1`. Since `D_5 = 0` iff `D_Z in {0, +-5}`
(as `|D_Z| <= 8`), the `145` singular pistons split as `129 + 16`.
`c_Z = 1` iff `4 D_Z^2 = |v|^4` iff the two singular values of `X_p` are
equal iff the rows of `X_p` are orthogonal of equal norm; for a nonzero
integer row `(a, b)` with `gcd g`, an orthogonal row is `t(-b, a)/g` and
equal norm forces `t = +-g`, so the second row is `+-(-b, a)`, which stays in
the entry set. With `24` nonzero first rows this gives `48` pistons. The
bound `c_Z <= 1` is `2 s_1 s_2 <= s_1^2 + s_2^2`, and `A_Z = c_Z^2/4` is the
definition. QED

## Drafting expectations (exposure, not thresholds)

```text
pistons: (s,|v|^2) classes 63, of which 32 carry more than one |D_Z|
    d changes |D_Z| on 508 pistons
    distinct c_Z values 12 on the 624 nonzero pistons:
      0:128  2/7:32  4/13:32  1/3:32  4/9:64  3/5:16  2/3:128
      4/5:48  6/7:32  8/9:32  12/13:32  1:48
    value set c_Z = {0, 2/7, 4/13, 1/3, 4/9, 3/5, 2/3, 4/5, 6/7, 8/9,
      12/13, 1}
```

## Discussion (NON-CLAIM)

The following sentence interprets R4 and is not a claim, gate, or row: the
relational information of the piston already lies in its public quadratic
carrier, and the frozen occurrence law is what discards it. Whether any
future occurrence law should read `D_Z` is a physical selection question
that belongs to `QDD-INSTRUMENT-APPARATUS [O]` and is not touched here.

## Owner decisions recorded

```text
B1 (2026-08-18)  NE to two carriers in one probe: this draft is the piston
                 half; the QPAIR half is P-QPAIR-RELATIONAL-AREA-1.
B2 (2026-08-18)  ANO with renaming: DEF-PISTON-2X2-RESHAPE, X_p and
                 D_Z = det X_p only; "joint state" does not occur.
B3 (2026-08-18)  ANO: hand-proved counts as F5 gates, multisets REPORT;
                 "product" replaced by "rank one modulo 5"; c_Z instead of
                 "concurrence" in the theorem layer.
B4 (2026-08-18)  reading lines dropped from the formal probe.
B5 (2026-08-18)  row renamed QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND with the
                 explicit REQUIRES edges above; the realignment rank kept as
                 guard G1, not as part of the claim.
```

Completed before this pin: public authority and collision readback, claim lock
#425, branch creation, and the Python 3.13 AST check. Next: read back the
immutable `PREREG.md` and `verify.py` pin, run once on Linux/aarch64 from
the repository root, then add `EXPECTED.txt`, `RUN.md`, and `RESULT.md`.
The later probe-only pull request must pass its x86_64 and aarch64 jobs and
the aggregate check.
