# P-QPAIR-RELATIONAL-AREA-1 preregistration (DRAFT, revision 2)

Status: `DRAFT / NOT PINNED / RESULT-EXPOSED / NO FORMAL RUN / NO CLAIM LOCK`

Revision 2 rebases the draft on Public Canon v52 and, following the owner
verdict of 2026-08-18, restricts this probe to the integral QPAIR carrier.
The rational piston carrier and every statement about it now live in the
sibling draft `P-PISTON-RELATIONAL-WEDGE-1`. No bridge between the two
carriers is stated, used, or implied here; a bridge, if ever, is a third
probe.

This document freezes one exact L1 probe carrying the incubation results of
`C-ENTANGLEMENT-RELATIONAL-WEDGE-1-N` (issue #419, verdict
RELATIONAL-AREA-PURE) and its post-result observation (the Pythagorean
identity `|b|^2 + 4||r||^2 = 1`, not absorbed there) into the public form of
the program. It contains no verifier output, earns no scientific or Canon
status, and is not a pin. Formal execution is forbidden until a public claim
lock and an immutable initial pin of `PREREG.md` and `verify.py` read back
from the public remote.

## Public identity, authority, and action layer

```text
program owner:       C-ENTANGLEMENT-RELATIONAL-WEDGE-1-N (incubation, NON-CANONICAL)
target rows:         QPAIR-DET-AREA-SLOT-COMPARISON     (new, ceiling T)
                     QPAIR-DET-AREA-PLACE-PAIR          (new, ceiling T)
probe:               P-QPAIR-RELATIONAL-AREA-1
sibling probe:       P-PISTON-RELATIONAL-WEDGE-1 (separate carrier, separate pin)
public lock:         none yet
probe owner:         A. M. Thorn / delegated drafting session
branch:              probe/P-QPAIR-RELATIONAL-AREA-1 (not created)
path:                probes/P-QPAIR-RELATIONAL-AREA-1/
initial base:        91e11e4f4db01d1badeabfea0a361972a6d4f2ea (public main = canon-v52)
Public Canon tag:    canon-v52
content commit:      6fc6923f727edacf55d511ec30eee2c7461ac497
Canon SHA-256:       b496e4e73a2b06167a981b75a5ea651591db383a9c7f222e0075eb8bb6f1ee03
Canon bytes:         261476
action layer:        L1 only (exact carrier algebra, finite exact audit family)
mode:                result-exposed, proof-first; verify.py is an exact finite audit
formal runs:         none; verify.py neither imported nor executed
static check:        py_compile PASS, pyflakes clean (drafting); to be
                     re-recorded at pin
```

Collision readback at drafting (main `91e11e4`): no registry, normative,
probe-directory or branch entry named `*DET-AREA*`, `*RELATIONAL-AREA*`;
the branches `notes/c-entanglement-relational-wedge-1-n` and its
`-duplicate` hold the incubation notes only. Open-issue readback is to be
completed by the owner at claim-lock time.

Lineage and novelty boundary, none of which is a logical premise beyond the
exact statements quoted in the equation field: `QPAIR-SYM2-TENSOR-DEFECT
[T]` supplies the determinant line `P_-- R(x tensor x) = ((ad-bc)/2) kappa`
and its conventions; `QPAIR-PRODUCT-COMPOSITION [T]` supplies the typed
matched product; `DEF-QPAIR-SPIN-CARRIER`, `DEF-QPAIR-HERM-SLOT`,
`DEF-QPAIR-SYM-SLOT` supply the integral carrier `O_K^2` and the two slots;
`QPAIR-TRANSPOSE-FIBER-REDUNDANCY [T]` (the symmetric slot determines the
Hermitian slot set-theoretically) bounds the wording of R1; `J-PROJECTIONS
[T]` names the principal archimedean embedding; `QUBIT-FROM-F5 [T]` names
`V_+ = F_5^x/{+-1}` and is cited only as a coincidence of index sets. The
rows `QUADRATIC-DECODER-DATA [O]`, `QDD-INSTRUMENT-APPARATUS [O]`,
`BELL-CAUSAL-ACCOUNTING [O]`, `BELL-MAGIC-BOUNDARY [T]`, `TWO-PLACE-PHYSICS
[D]`, `MEASURE-BORN-VERB [D]`, every `DEF-QDD-*` item and every `QDD-*` row
are excluded from the premises and are not moved, strengthened, interpreted,
or bridged by this probe.

## The question this probe attacks, at this carrier

Public Canon says that the symmetric slot of the composite pair on
`V tensor W` has a one-dimensional summand carrying the coefficient
`(ad-bc)/2`, and that the symmetric slot determines the Hermitian slot as a
set map. Two exact questions remain open at L1 on the integral carrier:

```text
1  which determinant form does each typed slot carry, and how do the two
   forms compare;
2  what kind of object the normalized squared determinant is for an
   integral cyclotomic state: one number, or an element of the real
   subfield with two archimedean values.
```

R1 answers 1: the Hermitian slot carries `N(D) = D c(D)` as the determinant
of its typed partial trace, the symmetric slot carries `D/2` on the kappa
line; the two agree through `4 N(kappa_coef) = det rho_V`; the Hermitian
form is invariant under the phase `u^2` that the symmetric form retains. No
necessity or minimality of the pair is claimed. R2 answers 2: the area is
one element of `K+ = Q(phi)`, hence a pair of real embeddings indexed by
`Gal(K+/Q) = F_5^x/{+-1}`, equal iff the area is rational; the local
eigenvalues need a square root the area does not.

## Result exposure

Every finite value quoted below was derived by hand in the drafting session
and reproduced by a scratch exact computation outside the repository, using
a third-party symbolic library for independence from the verifier. The
scratch scripts share no code with `verify.py`:

```text
scratch A   scratch_area.py     sha256 7f1756b2e2c711dc439fcfd855748f4ba7124616f6f0efeaf79d4e1b39e893b2
            stdout              sha256 ae9dbfcc69c6597818f4701d1864954dd555c428f042314fff1bad5ed6f75ccf
scratch B   scratch_pentit.py   sha256 00dff57823bfe823459a8452f26b6dc6c890b7305cda6ccc633d1fb7da89632f
            stdout              sha256 b19d4d1c0f8ee980aa17f8630e4962d5db175ef75c9af7514628de832ae21ece
```

(`scratch_area.py` also contains piston material that belongs to the sibling
probe; only its Q(zeta_5) block is exposure for this document.)

This probe is therefore a pinned confirmation and adversarial audit, not
blind discovery. No equation, carrier, systematic, threshold, output route,
or scope may move in response to the exposed values. `verify.py` has never
been executed and never imported; at drafting it passed `py_compile` and a
`pyflakes` static pass, and its helper functions (field arithmetic,
polynomial ring, rank) were unit-checked on a copied source slice in the
scratch environment without evaluating any gate. No dynamic evaluation of
`U`, no orbit, window, seed, or event tally of any kind was run for this
draft, and none is part of the probe.

## Falsifier first

A single exact counterexample to R1 or R2 falsifies the corresponding row:
a partial trace, trace, determinant, norm, or discriminant identity failing
on a generic polynomial audit; the kappa coefficient differing from
`(ad-bc)/2` or the comparison `4 N(kappa_coef) = det rho_V` failing; the
phase witness having unequal Hermitian slots or equal determinants; a local
character differing from `det(g) det(h)`; an integral witness whose area
lies outside `K+`, differs from its stated exact value, has the wrong order
of its two real embeddings, or is negative or exceeds `1/4` at either
embedding; any state of the pentit audit family violating those bounds; the
discriminant witness having a square norm.

An environment or argument defect, an exception, a nonzero exit on a valid
route, nonempty stderr, or a cross-architecture byte mismatch is `STOP`, not
`FALSIFIED`. Exit code map: 0 pass, 1 STOP, 2 FALSIFIED.

## The six frozen fields

### 1. Equation

#### 1.1 Field, involution, real embeddings

```text
K = Q(zeta), zeta = zeta_5, coordinates c0 + c1 zeta + c2 zeta^2 + c3 zeta^3,
    zeta^4 = -(1 + zeta + zeta^2 + zeta^3);
sigma_a(zeta) = zeta^a for a in F_5^x = {1,2,3,4};   c = sigma_4;
K+ = Fix(c) = Q(phi),  phi = -zeta^2 - zeta^3,  psi = sigma_2(phi) = 1 - phi,
    phi^2 = phi + 1,  phi psi = -1;
Gal(K+/Q) = Gal(K/Q)/<c> = F_5^x/{+-1}, classes {1,4} and {2,3};
iota_{1,4} : phi -> (1+sqrt5)/2   (the class of a = 1; the principal
             archimedean embedding of J-PROJECTIONS restricted to K+),
iota_{2,3} : phi -> (1-sqrt5)/2.
```

Every element of `K+` is written uniquely as `alpha + beta phi` with
`alpha, beta in Q`; its two real embeddings are `iota_{1,4}` and
`iota_{2,3}` of that expression. Exact sign tests at an embedding are
rational: with `p = alpha + beta/2` and `q = +-beta/2`, `p + q sqrt5 > 0` is
decided by the signs of `p, q` and the comparison of `p^2` with `5 q^2`.
The index set `F_5^x/{+-1}` coincides with the `V_+` of QUBIT-FROM-F5; the
coincidence of index sets is recorded and nothing is derived from it.

#### 1.2 Composite carrier, pair, kappa line

`V = W = K^2` with bases `e_0, e_1` and `f_0, f_1`; the coordinate Hermitian
forms `h_V(e_i, e_k) = delta_ik`, `h_W(f_j, f_l) = delta_jl`. A state is

```text
x = a e0f0 + b e0f1 + c e1f0 + d e1f1,     X = ((a, b), (c, d)),
```

nonzero unless stated. The integral states are `x in O_K^4`, that is
`V_spin tensor V_spin` for two copies of `DEF-QPAIR-SPIN-CARRIER`. The pair is

```text
H(x) = x tensor bar(x),  coordinates X_ij c(X_kl);      S(x) = x tensor x.
```

From `QPAIR-SYM2-TENSOR-DEFECT [T]`, with `R`, `alpha`, `beta`,
`P_-- = (1-alpha)(1-beta)/4`, `u wedge v = u tensor v - v tensor u`,
`kappa = (e0 wedge e1) tensor (f0 wedge f1)`:

```text
P_-- R(x tensor x) = (D(x)/2) kappa,      D(x) = ad - bc = det X.        (1)
```

The verifier re-audits (1) with the same conventions on the sixteen-
dimensional reordered space with generic polynomial coefficients.

#### 1.3 Typed partial traces and the area

```text
DEF-QPAIR-TYPED-PARTIAL-TRACE (proposed)
    tr_W : H(V tensor W) -> H(V) contracts the W and bar(W) factors with
    h_W; tr_V contracts V and bar(V) with h_V. In coordinates
    rho_V(x) = tr_W H(x) = X c(X)^T,    rho_W(x) = tr_V H(x) = X^T c(X).
DEF-QPAIR-DET-AREA (proposed)
    n(x) = sum_ij X_ij c(X_ij),   N(D) = D c(D),
    A(x) = N(D(x)) / n(x)^2   for x != 0;   the ZERO tag for x = 0;
    disc(x) = n^2 - 4 N(D);   beta_B(x) = disc / n^2.
```

#### Target R1. QPAIR-DET-AREA-SLOT-COMPARISON

Over every field `K` with involution `c` and two-dimensional `V, W`, for
every state `x`, the two typed slots carry two determinant forms:

```text
R1.i    tr_W H(x) = X c(X)^T,  tr_V H(x) = X^T c(X),  both of trace n(x).
R1.ii   det rho_V = det rho_W = N(D) = D c(D), an element of Fix(c)
        (the Hermitian determinant form).
R1.iii  P_-- R(x tensor x) = (D/2) kappa (the symmetric determinant form,
        equation (1) re-audited);  comparison: 4 N(kappa_coef) = det rho_V.
R1.iv   with rho_V = ((p, z), (c(z), q)):
        disc = (p - q)^2 + 4 z c(z),  hence  beta_B + 4 A = 1
        (Pythagorean identity in Fix(c), before any embedding is chosen).
R1.v    phase: for u with u c(u) = 1, H(ux) = H(x), D(ux) = u^2 D(x),
        S(ux) = u^2 S(x); witness x = (1,0,0,1), u = zeta: equal Hermitian
        slots, D = 1 against D = zeta^2, distinct symmetric slots.  For
        trivial c the phase group is {+-1} and u^2 = 1.
R1.vi   local maps g in GL(V), h in GL(W): D -> det(g) det(h) D,
        N(D) -> N(det g det h) N(D); A is invariant under h_V-unitary and
        h_W-unitary local maps and under nonzero scalars.
```

R1 asserts no necessity, minimality, or informational independence of the
two slots; `QPAIR-TRANSPOSE-FIBER-REDUNDANCY [T]` already states that the
symmetric slot determines the Hermitian slot set-theoretically. R1 says only
which determinant form each typed slot carries and how the two compare.

#### Target R2. QPAIR-DET-AREA-PLACE-PAIR

For `K = Q(zeta_5)` and every nonzero `x in K^4`:

```text
R2.i    A(x) in K+;  sigma_a(A) depends only on the class of a in
        F_5^x/{+-1};  writing A = alpha + beta phi, the two real embeddings
        agree iff beta = 0 iff A in Q (embedding-blind); otherwise
        embedding-split.
R2.ii   0 <= iota(A) <= 1/4 at both real embeddings;
        iota(A) = 1/4 iff at that embedding X X-bar^T is a scalar matrix.
R2.iii  integral witnesses (exact):
        (1, 0, 0, 1)         A = 1/4            blind
        (1, 0, 0, phi)       A = 1/5            blind, irrational entry
        (1, zeta, 0, 1)      A = 1/9            blind
        (1, 1, 0, phi)       A = (10 + 3 phi)/121,
                             iota_{1,4} = (23 + 3 sqrt5)/242 > iota_{2,3} = (23 - 3 sqrt5)/242
        (1, 1, 1, 1 + zeta)  A = (26 - 9 phi)/361,  iota_{1,4} < iota_{2,3}
R2.iv   Schmidt-root obstruction: the eigenvalues (n +- sqrt(disc))/2 of
        rho_V lie in K+ iff disc is a square in K+, which forces
        N_{K+/Q}(disc) to be a rational square; witness (1, 1, 0, phi):
        disc = 6 + 3 phi, N_{K+/Q} = 45, not a square, so the local weights
        are not in K+ while N(D) = 1 + phi lies in O_{K+};
        witness (2, 0, 0, 1): disc = 9, weights 4 and 1.
R2.v    finite audit family: over the pentit class (mu_10 union {0})^4
        minus zero (14640 states) every area lies in K+ and satisfies R2.ii
        at both embeddings; the counts of blind and split states, the
        number of distinct area values, and the multiset are reported.
```

#### Wording firewall

The kappa line is a direction in the quadratic target, not a Bell state and
not the two-qubit singlet (as in `QPAIR-SYM2-TENSOR-DEFECT`). The word
"area" names `A(x)`, an element of `Fix(c)`; "embedding" means a real
embedding of `K+`; the principal one is named through J-PROJECTIONS as a
dictionary reference only and no gate depends on which embedding is called
principal. `F_5^x/{+-1}` is used as an index set; no sentence says "hence a
qubit" or creates an edge to QUBIT-FROM-F5. No sentence names a physical
system, a measurement, or a reading of `A` as a measured quantity. The
integral carrier is `O_K^2 tensor O_K^2`; the rational carrier `V_eff` and
every `QDD` object are absent from this probe.

#### What is not claimed

No mixed states, no Schmidt rank above two, no `2 x n` bivector, no
BELL-CAUSAL-ACCOUNTING row or dependency, no link to `BELL-MAGIC-BOUNDARY`,
no L2 to L6 statement, no instrument, no measure, no decoder statement, no
uniqueness of the area among entanglement monotones, no derivation of the
principal embedding from `J`, no bridge to `V_eff`, and no SI statement.
The `phi`, `zeta` and `1 + zeta` witnesses are exact algebraic witnesses
with no fifth-prime physical content.

### 2. Code

`verify.py`, Python standard library only, exact integer or
`fractions.Fraction` arithmetic for every scalar, an exact four-coordinate
`Q(zeta_5)` arithmetic (Fraction coordinates for the witnesses, integer
coordinates for the pentit audit family), exact multivariate polynomials
with rational coefficients for the generic identities, no float anywhere in
an asserted identity, no random choice, no file input, no arguments, no
network, canonical ASCII stdout with final newline, empty stderr, runtime
under 120 seconds from the repository root under

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-QPAIR-RELATIONAL-AREA-1/verify.py
```

Gate list, in order:

```text
I01  environment (interpreter, no arguments)
R1a  generic partial-trace, trace, determinant, norm identities in the eight
     variables a,b,c,d and their bars (c acting as the bar swap)
R1b  generic discriminant and Pythagorean identities
R1c  kappa coefficient (ad-bc)/2 on the 16-dimensional reordered space with
     the frozen conventions; slot comparison 4 N(kappa_coef) = det rho_V
R1d  phase witness (1,0,0,1) against zeta (1,0,0,1)
R1e  local characters on generic matrices (12 variables) and on an exact
     non-unimodular witness pair; local-unitary and scalar invariance of A
R2a  every witness area lies in K+ and equals its stated exact value; the
     order of the two real embeddings of each split witness
R2b  exact bounds 0 <= iota(A) <= 1/4 on the witnesses and on all 14640
     pentit states
R2c  discriminant witnesses: 6 + 3 phi with norm 45 not a square; 9 with
     weights 4 and 1; N(D) = 1 + phi integral
R2d  Galois-class indexing sigma_2 = sigma_3 and sigma_1 = sigma_4 on the
     numerator and denominator of every witness area
REPORT lines (no gate): the two real embeddings of each split witness as
     exact surds; pentit counts and area values
RESULT PASS | FALSIFIED | STOP
```

### 3. Carrier or data

`Q(zeta_5)` in the power basis with `c = sigma_4`; `K+ = Q(phi)`; the
integral witnesses of R2.iii and R2.iv; the pentit family
`(mu_10 union {0})^4`. No external data, measurement, fit, orbit, window,
seed, or stochastic sample; no rational piston carrier.

### 4. Systematics

```text
S1  Conventions of (1) are those of QPAIR-SYM2-TENSOR-DEFECT: Sym^2 as the
    +1 eigenspace, R orders (V_1, V_2, W_1, W_2), the wedge is not halved,
    P_-- = (1-alpha)(1-beta)/4.  With them the coefficient is D/2, and the
    slot comparison reads 4 N(kappa_coef) = det rho_V.
S2  The partial traces use the coordinate Hermitian forms h_V, h_W; a
    different local form changes rho_V by congruence and A accordingly.
    R1.vi records exactly which local maps leave A fixed.
S3  Areas are elements of Fix(c); "embedding" means a real embedding of
    K+.  Ordering statements are decided by exact rational sign tests,
    never by floats.  No gate depends on which embedding is called
    principal.
S4  The pentit family in R2.v is an audit family for the universal bounds
    of R2.ii and a reported census; it is not a state space of the machine.
S5  Reported values (REPORT lines) are frozen only in EXPECTED.txt after the
    formal run; they are not thresholds.  The drafting expectations below
    are exposure, not thresholds.
S6  Two-architecture gate: the local formal run is on aarch64, the required
    public job on x86_64; the finite audit reaches C by byte-identical
    output and T only through the written proofs the verifier audits.
S7  Nothing in this probe uses, names, or restricts to the rational
    carrier V_eff; the sibling probe P-PISTON-RELATIONAL-WEDGE-1 is
    logically independent of this one.
```

### 5. Failure threshold

Exact and binary. Any scientific falsifier below records the affected row
`F`; no threshold may be moved after the pin.

```text
F1  any identity of R1.i to R1.iv fails on the generic polynomial audit, or
    the phase witness of R1.v has unequal Hermitian slots or equal
    determinants, or a character of R1.vi is wrong, or the local-unitary or
    scalar invariance of A fails on the witness.
F2  a witness area is not in K+, differs from its stated exact value, has
    the wrong order of embeddings, or violates 0 <= iota(A) <= 1/4 at either
    embedding; or any pentit state violates those bounds; or 45 is a
    rational square; or sigma_2(A) != sigma_3(A) on a witness.
```

A verifier, expected-output, or hash mismatch, any execution before the
immutable pin, a float in an asserted identity, an unapproved dependency,
any QDD or V_eff statement, or wording that crosses the firewall is an
integrity or scope `STOP`, not a rewritten scientific threshold.

### 6. Action layer

`L1` only: exact carrier algebra and a finite exact audit family on the
integral QPAIR carrier. Nothing lifts to L2 through L6.

## Proofs

These proofs carry the universal statements; the verifier audits their
coordinates and finite witnesses.

### Proof of R1

`R1.i` and `R1.ii`. `H(x)` has coordinates `X_ij c(X_kl)` on
`e_i f_j tensor bar(e_k f_l)`. Contracting `f_j` against `bar(f_l)` with
`h_W` sets `j = l` and sums, giving `(rho_V)_ik = sum_j X_ij c(X_kj)`, that
is `X c(X)^T`; contracting the `V` factors gives `X^T c(X)`. Both traces are
`sum_ij X_ij c(X_ij) = n(x)`. For a two-by-two matrix
`det(X c(X)^T) = det X det c(X)^T = D c(D)`, since `c` is a ring
automorphism and `det` is a polynomial with integer coefficients; the same
for `X^T c(X)`. `D c(D)` is fixed by `c`. QED

`R1.iii`. Only terms of `R(x tensor x)` with both basis indices in each
factor survive `P_--`; the four ordered terms `ad, da, bc, cb` project to
`+kappa/4, +kappa/4, -kappa/4, -kappa/4`, giving `(ad-bc)/2` (this is the
proof of QPAIR-SYM2-TENSOR-DEFECT, re-audited). Then
`N(2 kappa_coef) = N(D) = det rho_V` by `R1.ii`. QED

`R1.iv`. For `rho_V = ((p, z), (c(z), q))` with `p, q` fixed by `c`,
`n = p + q` and `N(D) = det rho_V = pq - z c(z)`. Then
`n^2 - 4 N(D) = (p+q)^2 - 4pq + 4 z c(z) = (p-q)^2 + 4 z c(z)`. Dividing by
`n^2` gives `beta_B + 4A = 1`. Both sides are in `Fix(c)`. QED

`R1.v`. `H(ux) = u c(u) H(x) = H(x)` when `u c(u) = 1`, while
`D(ux) = u^2 D(x)` and `S(ux) = u^2 S(x)`. For `x = (1,0,0,1)` and
`u = zeta`, `zeta c(zeta) = 1`, `D` becomes `zeta^2 != 1`, and `S` changes by
the factor `zeta^2`. If `c` is trivial then `u c(u) = u^2 = 1`. QED

`R1.vi`. `X -> g X h^T` for local `g, h`, so `D -> det g det h D` and
`N(D) -> N(det g det h) N(D)`. `rho_V -> g X h^T c(h) c(X)^T c(g)^T`; when
`h^T c(h) = 1` and `g c(g)^T = 1` this is a unitary similarity of `rho_V`,
so `n` and `det` are unchanged, and `A` is unchanged. Under a scalar
`lambda`, `N(D)` and `n^2` both scale by `N(lambda)^2`. QED

### Proof of R2

`R2.i`. `N(D)` and `n` are sums of products `y c(y)`, hence in `Fix(c) = K+`;
`A` is their quotient. `Gal(K/Q)` is abelian, `sigma_-a = sigma_a sigma_-1`
and `sigma_-1 = c` fixes `A`, so `sigma_a(A)` depends only on the class of
`a` modulo `{+-1}`. `iota_{1,4}(alpha + beta phi) = iota_{2,3}(alpha + beta
phi)` iff `beta (phi - psi) = beta sqrt5 = 0` iff `beta = 0`. QED

`R2.ii`. Fix a real embedding `iota` of `K+` and extend it to a complex
embedding `tau` of `K`; then `iota(N(D)) = |tau(D)|^2` and
`iota(n) = ||tau(x)||^2`. Let `s_1 >= s_2 >= 0` be the singular values of
`tau(X)`. Then `|tau(D)|^2 = s_1^2 s_2^2` and `||tau(x)||^2 = s_1^2 + s_2^2`,
so `iota(A) = s_1^2 s_2^2 / (s_1^2 + s_2^2)^2 in [0, 1/4]`, with equality at
`1/4` iff `s_1 = s_2` iff `tau(X) tau(X)^*` is scalar. QED

`R2.iii`. Direct computation, audited exactly. For `(1,1,0,phi)`:
`D = phi`, `N(D) = phi^2 = 1 + phi`, `n = 2 + phi^2 = 3 + phi`,
`n^2 = 10 + 7 phi`, `(10 + 7 phi)(10 + 7 psi) = 121`,
`(1 + phi)(10 + 7 psi) = 10 + 3 phi`, so `A = (10 + 3 phi)/121`; with
`phi = (1 + sqrt5)/2` this is `(23 + 3 sqrt5)/242`. For `(1,1,1,1+zeta)`:
`D = zeta`, `N(D) = 1`, `n = 3 + (1+zeta)(1+zeta^4) = 4 + phi`,
`n^2 = 17 + 9 phi`, `(17 + 9 phi)(17 + 9 psi) = 361`, so
`A = (26 - 9 phi)/361`. For `(1,0,0,phi)`: `N(D) = 1 + phi`,
`n = 1 + phi^2 = 2 + phi`, `n^2 = 5 + 5 phi = 5(1 + phi)`, `A = 1/5`. QED

`R2.iv`. The eigenvalues of `rho_V` are the roots of `t^2 - n t + N(D)`,
namely `(n +- sqrt(disc))/2`; they lie in `K+` iff `disc` is a square there.
A square `y^2` in `K+` has `N_{K+/Q}(y^2) = N(y)^2`, a rational square. For
`(1,1,0,phi)`, `disc = 10 + 7 phi - 4 - 4 phi = 6 + 3 phi` and
`(6 + 3 phi)(6 + 3 psi) = 36 + 18 - 9 = 45`, not a square. For `(2,0,0,1)`,
`n = 5`, `N(D) = 4`, `disc = 9`, eigenvalues `4` and `1`. QED

## Drafting expectations (exposure, not thresholds)

```text
pentit family (mu_10 union {0})^4 minus zero: 14640 states
    bound violations 0; blind 6640; split 8000;
    A = 1/4: 1200;  A = 0: 1440;  distinct A values 7, of which split 4:
    (1 + phi)/16, (2 - phi)/16, (2 + phi)/16, (3 - phi)/16, each 2000 times
```

## Discussion (NON-CLAIM)

The following sentences interpret R1 and R2 and are not claims, gates, or
rows. For an integral state the area `A` lies in `K+` and `N(D)` in `O_{K+}`
before the local eigenvalues do; the local weights need `sqrt(disc)`, which
generically leaves `K+`. In that precise sense the relation has an integral
size before its members have integral weights. In external quantum
mechanics, after a complex norm is supplied at an embedding, `2 sqrt(iota(A))`
is the pure-state concurrence and `4 + 16 iota(A)` the Horodecki CHSH square,
as recorded in the incubation `C-ENTANGLEMENT-RELATIONAL-WEDGE-1-N`; none of
that is derived here or from `J`.

## Owner decisions recorded

```text
B1 (2026-08-18)  NE to two carriers in one probe: this draft is the QPAIR
                 half; the piston half is P-PISTON-RELATIONAL-WEDGE-1.
B4 (2026-08-18)  reading lines D1 to D4 dropped from the formal probe; the
                 provable algebra is inside R1 and R2; the remaining prose is
                 the Discussion (NON-CLAIM) above.
R1 wording       "the reading is a pair" removed; the row states two typed
                 slots carrying two determinant forms and their comparison,
                 consistent with QPAIR-TRANSPOSE-FIBER-REDUNDANCY.
```

Open before pin: owner readback of open issues for collisions; then claim
lock issue, branch `probe/P-QPAIR-RELATIONAL-AREA-1`, static check, initial
pin of `PREREG.md` and `verify.py`, readback, formal run on aarch64 from the
repository root, `EXPECTED.txt`, `RUN.md`, pull request with the x86_64
job, `RESULT.md`.
