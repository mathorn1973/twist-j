# P-O5-GOLDEN-PROFILE-TRANSFER-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED**

Date: 2026-08-28.

## Public identity

```text
probe:             P-O5-GOLDEN-PROFILE-TRANSFER-1
public claim lock: issue #612
proposed row:      O5-GOLDEN-PROFILE-TRANSFER
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-GOLDEN-PROFILE-TRANSFER-1
path:              probes/P-O5-GOLDEN-PROFILE-TRANSFER-1/
basis main:        66a3e68fed5988a72cd56fe411b1ed633253194f
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, exact Lucas arithmetic / finite signed profile algebra
layer lift:        none
authority:         none until a later sealed Canon fold
```

The structural formulas and the candidate witnesses were exposed in exact
non-formal reasoning before this pin, as disclosed in issue #612. They carry no
evidence credit. The theorem, carrier, endpoint conventions, mutation witnesses
and failure thresholds below are the frozen formal contract.

## Collision and ownership boundary

The collision scan recorded in issue #612 covered current and historical
issues, pull requests, remote branches, the Public Canon v67 tree, Registry,
Frontier, evidence, gates, current O5 probes and current Notes.

- merged `P-O5-GOLDEN-AXIS-BAND-1` (#611) owns the exact width-five golden
  band and Lucas-top four-diagonal formula for `Q_11`;
- merged `P-O5-FIRST-SHELL-BILINEAR-SQUARE-1` (#609) owns the ordinary
  bilinear annulus and the restricted Mobius carrier used below;
- draft PR #595 owns only a NON-CANONICAL evaluation ladder
  `tau=L_(2k)`, not the cutoff/profile state here;
- earlier first-shell, first-missing, squarefree-core and divisor-read probes
  remain separate;
- `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` is untouched.

No existing object owns `P-O5-GOLDEN-PROFILE-TRANSFER-1` or
`O5-GOLDEN-PROFILE-TRANSFER`.

## Proposed candidate row

At most one row may be offered to a later sealed fold:

```text
O5-GOLDEN-PROFILE-TRANSFER [candidate-T]
```

Its exact scope is the cutoff 5-cycle and induced recurrence, the golden
skew-product multiplication law, the exact profile-kernel representation and
Lucas-top thresholds, the universal scalar shell-mass no-go on the frozen
finite-support class, and the failure of the naive Lucas recurrence on the
actual restricted Mobius carrier. It includes no cancellation estimate.

## Frozen carrier and endpoint conventions

Put

```text
alpha = phi^2 = (3+sqrt(5))/2,
A_k   = L_(2k),
X_k   = A_k-1 = floor(alpha^k),                 k>=0,
M_k   = floor(X_k/11),
r_k   = X_k-11M_k,                              0<=r_k<=10.
```

Use the complete golden-shell partition from merged probe #611:

```text
I_-1 = {1},
I_k  = {n in Z_(>=1): X_k<n<=X_(k+1)},          k>=0.
```

For every positive integer `n`, let

```text
kappa(n) = the unique k>=-1 such that n is in I_k,
z(n)     = n alpha^(-kappa(n)).
```

The shell convention is open on the left and closed on the right, so

```text
1<z(n)<=alpha,
z(1)=alpha.
```

Let `F_all` be the class of finitely supported integer-valued sequences on the
positive integers. For `f` in `F_all`, define the canonical exact sparse
profile

```text
Profile_k(f) = {z(n) -> f(n): n in I_k and f(n)!=0}.
```

Zero entries are deleted. Keys are exact elements of `Q(alpha)`, not floating
point values.

For shell indices `i,j`, a nonnegative integer cutoff `Y`, and

```text
T=Y alpha^(-(i+j)),
K_T(x,y)=1_(xy<=T),
```

define the ordered pairing

```text
Pair_(i,j)(f;Y)
 = sum_(a in I_i,b in I_j,ab<=Y) f(a)f(b)
 = sum_(x in Profile_i(f),y in Profile_j(f))
     f_i(x)f_j(y) K_T(x,y).
```

Also define

```text
u_k(f) = sum_(n in I_k) f(n),

P_s(f;Y) = sum_(i+j=s) Pair_(i,j)(f;Y),

D_s(f) = sum_(i+j=s) u_i(f)u_j(f),

H_f(Y) = sum_(a,b>=1,ab<=Y) f(a)f(b),

Q_f(N) = H_f(N)-H_f(floor(N/11))
       = sum_(N/11<ab<=N) f(a)f(b).
```

All pair sums are ordered. They are never divided by two on the diagonal.

Let `nu` be the actual restricted Mobius sequence of merged probe #609:

```text
nu(n)=mu(n)
```

when `n` is squarefree and every prime divisor is a rational split prime
strictly greater than `11`, and `nu(n)=0` otherwise. In particular `nu(1)=1`.
Let

```text
F_nu={f in F_all: f(n) is in {0,nu(n)} for every n}.
```

Thus `F_nu` is the natural class of finite selectors of the actual signed
carrier, not a class with arbitrary replacement weights. The scalar no-go
below is universal already on this smaller class. Although the actual `nu` is
not finitely supported, every cutoff statement for it is obtained from the
finite truncation

```text
nu_[Y](n)=nu(n) 1_(n<=Y).
```

This avoids silently applying a finite-support theorem to an infinite
sequence.

## Frozen theorem package and proof

The proofs in this section are the evidence-bearing universal argument. The
finite verifier gates below audit the implementation and frozen witnesses;
their finite ranges do not define or limit the written theorem.

### A. Cutoff geometry has an exact 5-cycle and finite transfer

The even Lucas subsequence obeys

```text
A_(k+1)=3A_k-A_(k-1),                            k>=1.
```

Since `X_k=A_k-1`, subtraction gives the inhomogeneous recurrence

```text
X_(k+1)=3X_k-X_(k-1)+1,                          k>=1.
```

The initial exact values are

```text
(X_0,X_1,X_2,X_3,X_4,X_5,X_6)
  =(1,2,6,17,46,122,321).
```

Therefore

```text
(r_0,r_1,r_2,r_3,r_4,r_5,r_6)
  =(1,2,6,6,2,1,2) mod 11.
```

The same affine recurrence determines every later residue from the preceding
ordered pair. Since `(r_5,r_6)=(r_0,r_1)`, induction proves

```text
r_(k+5)=r_k                                      for every k>=0.
```

The period is exactly five, because the displayed nonconstant first cycle
cannot have any period `1,2,3` or `4`.

Insert `X_k=11M_k+r_k` into the cutoff recurrence. For every `k>=1`,

```text
M_(k+1)-3M_k+M_(k-1)=c_k,

c_k=(1-r_(k+1)+3r_k-r_(k-1))/11.
```

The residue cycle gives

```text
(c_1,c_2,c_3,c_4,c_5)=(0,1,1,0,0),
c_(k+5)=c_k.
```

Subtracting the same recurrence five indices later removes the periodic
forcing. Equivalently, for every `k>=0`,

```text
M_(k+7)-3M_(k+6)+M_(k+5)
 -M_(k+2)+3M_(k+1)-M_k=0.
```

Thus the cutoff geometry itself has an exact finite recurrence. This says
nothing about the signed amplitude.

### B. Multiplication is an exact golden skew product

Let `a,b` be positive integers and put

```text
i=kappa(a),  j=kappa(b),  x=z(a),  y=z(b).
```

Then `1<x,y<=alpha`, so `1<xy<=alpha^2`. Define

```text
epsilon(a,b)=0 if xy<=alpha,
             1 if xy>alpha.
```

Since `a=alpha^i x` and `b=alpha^j y`, exactly

```text
ab=alpha^(i+j)xy.
```

If `xy<=alpha`, then

```text
alpha^(i+j)<ab<=alpha^(i+j+1),
```

so `kappa(ab)=i+j`. If `xy>alpha`, then

```text
alpha^(i+j+1)<ab<=alpha^(i+j+2),
```

so `kappa(ab)=i+j+1`. Hence for all positive integers `a,b`, including the
unit cases,

```text
kappa(ab)=i+j+epsilon(a,b),
z(ab)=xy alpha^(-epsilon(a,b)).
```

The endpoint `xy=alpha` belongs to the zero-carry branch because the shells
are closed on the right.

The unit cases are included rather than inferred by omission. If `a=1` and
`b` is nonunit, then `i=-1`, `x=alpha`, `y>1`, so `epsilon=1`; the formula
returns shell index `j` and mantissa `y`. The case `b=1` is symmetric. If
`a=b=1`, then `i=j=-1`, `x=y=alpha`, `epsilon=1`, and the formula returns
`kappa(1)=-1` and `z(1)=alpha`.

### C. The finite band has an exact profile-kernel representation

For `a in I_i`, `b in I_j`, put `x=z(a)`, `y=z(b)`. The exact identity

```text
ab=alpha^(i+j)xy
```

gives, for every nonnegative integer `Y`,

```text
ab<=Y  iff  xy<=Y alpha^(-(i+j)).
```

Multiplying by the integer weights and summing proves the displayed profile
formula for `Pair_(i,j)(f;Y)` for every `f` in `F_all`, without a finite-range
assumption on `i,j` beyond the finite support of `f`.

The profile is sufficient for exact reconstruction at each fixed cutoff, not
merely a quotient: for fixed `k`, each exact key `x=z(n)` decodes uniquely as

```text
n=x alpha^k.
```

This is a positive integer with zero `alpha` coefficient in the exact
`Q(alpha)` representation. Therefore the keys are collision-free within a
shell and `Profile_k(f)` reconstructs `f` on `I_k` exactly.

For the actual infinite sequence `nu` and any fixed cutoff `Y`, replace it by
`nu_[Y]`. Every factor in a product `ab<=Y` is at most `Y`, so

```text
H_nu(Y)=H_(nu_[Y])(Y).
```

Consequently all profile decompositions needed for `Q_11(N)` follow from the
finite-support theorem with `Y=N` and `Y=floor(N/11)`.

At a Lucas-top cutoff `N=X_K`, `K>=4`, put `M=M_K`. The four-diagonal formula
from merged probe #611 contains three nontrivial boundary forms. Their exact
thresholds are

```text
T_K^+ = X_K alpha^(-(K-1))
      = alpha-alpha^(1-K)+alpha^(1-2K),

T_(K,3)^- = M_K alpha^(-(K-3))
          = [alpha^3+alpha^(3-2K)
             -(1+r_K)alpha^(3-K)]/11,

T_(K,4)^- = M_K alpha^(-(K-4))
          = alpha T_(K,3)^-.
```

Indeed, the conjugate of `alpha` is `alpha^(-1)`, hence

```text
L_(2K)=alpha^K+alpha^(-K),
X_K=alpha^K+alpha^(-K)-1.
```

The first formula follows after multiplication by `alpha^(-(K-1))`. Since
`M_K=(X_K-r_K)/11`, multiplication by `alpha^(-(K-3))` gives the second, and
the third differs by one shell power.

Writing `K_T` for the step kernel, the three boundary terms use the kernels

```text
D_(K-4)(f)-P_(K-4)(f;M_K):  1-K_(T_(K,4)^-),
D_(K-3)(f)-P_(K-3)(f;M_K):  1-K_(T_(K,3)^-),
P_(K-1)(f;X_K):              K_(T_K^+).
```

The fourth term `D_(K-2)(f)` is complete. Thus the exact four-diagonal normal
form is a finite sum of profile pairings, but the profiles themselves grow
with the shells.

Because `alpha>1` and `r_K` is bounded,

```text
T_K^+     -> alpha,
T_(K,3)^- -> alpha^3/11,
T_(K,4)^- -> alpha^4/11.
```

These are exact threshold limits only. They are not a norm, contraction or
spectral statement.

### D. Complete scalar shell masses do not determine the annulus

Take the two sequences in `F_nu`

```text
f=-delta_19,
g=-delta_41.
```

Both `19` and `41` lie in `I_3`, and both are allowed support points of `nu`.
Therefore

```text
u_k(f)=u_k(g) for every k,
D_s(f)=D_s(g) for every s.
```

At `N=X_7=842`, however,

```text
floor(842/11)=76,
76<19^2=361<=842,
41^2=1681>842.
```

Each sequence has only one ordered nonzero pair, so

```text
Q_f(842)=1,
Q_g(842)=0.
```

Suppose a deterministic readout of the complete shell-mass sequence at the
fixed cutoff `842` reconstructed the annulus universally on `F_nu`. Equal
inputs `u(f)=u(g)` would force equal outputs, contradicting the displayed
values. Hence there is no function

```text
R: (u_k(f))_(k>=-1) -> Q_f(842)
```

valid for every `f` in `F_nu`. In particular, no exact transfer whose entire
state is derived only from the scalar shell masses, or from the complete
diagonal scalars `D_s`, can be universally valid on that class.

This proves no no-go for a special recurrence of the one actual sequence
`nu`, and no no-go for a different finite summary retaining within-shell
information.

### E. The naive Lucas recurrence fails on the actual carrier

The first three relevant Lucas cutoffs and lower integer cutoffs are

```text
(X_4,X_5,X_6)=(46,122,321),
(floor(X_4/11),floor(X_5/11),floor(X_6/11))=(4,11,29).
```

Below `321`, a nonunit composite in the support of `nu` would require two
distinct allowed primes. The smallest possible product is

```text
19*29=551>321,
```

while a repeated prime is excluded by squarefreeness. Thus only the unit and
allowed primes contribute. The unit cancels from every displayed annulus, and
each allowed prime contributes the two ordered pairs `(1,p)` and `(p,1)`,
each of weight `-1`.

The exact prime lists in the three annuli are

```text
X_4: 19,29,31,41

X_5: 19,29,31,41,59,61,71,79,89,101,109

X_6: 31,41,59,61,71,79,89,101,109,131,139,149,151,
     179,181,191,199,211,229,239,241,251,269,271,281,311.
```

Their counts are `4,11,26`, so exact ordered-pair enumeration gives

```text
Q_11(X_4)=-8,
Q_11(X_5)=-22,
Q_11(X_6)=-52.
```

At the corresponding forcing step `c_5=0`. The direct inherited Lucas rule
would predict

```text
3Q_11(X_5)-Q_11(X_4)+c_5
  =3(-22)-(-8)+0
  =-58,
```

not `-52`. The cutoff recurrence therefore does not transfer directly to the
signed amplitude.

### F. Exact route boundary

The frozen result separates the attack as follows:

```text
cutoff geometry:             finite exact recurrence / candidate-T,
shell-index multiplication:  exact one-carry skew product / candidate-T,
profile-kernel form:          exact reconstruction at each fixed cutoff / candidate-T,
scalar shell-mass closure:    universal no-go on F_nu / candidate-T,
naive actual-nu recurrence:   exact failure / candidate-T,
cancellation estimate:        OPEN and not supplied.
```

The next positive mechanism, if any, must act on within-shell profiles or an
independently justified transform of them. The exact profile is not a
fixed-dimensional state: its cardinality may grow with the shell.

## Falsifier first

One exact defect falsifies the corresponding frozen statement:

1. the cutoff recurrence, residue 5-cycle, induced `M_k` recurrence or
   order-seven recurrence fails;
2. one positive integer product violates the skew-product carry law, including
   the endpoint convention;
3. one decoded profile differs from the original shell restriction, one key
   collides, or one profile-kernel pairing differs from the direct integer
   product cutoff;
4. one Lucas-top threshold identity or complementary-kernel assignment is
   wrong;
5. the two equal-shell-mass witnesses have equal annular values at `842`;
6. the actual `Q_11` values or the stated recurrence failure is wrong;
7. the construction claims a cancellation estimate, imports RH or GRH,
   selects an orientation, treats the growing exact profile as a uniformly
   finite-dimensional state, or upgrades the scalar no-go beyond `F_nu`.

A stale basis, changed pin, failed startup preflight, nonzero verifier exit,
nonempty stderr, stdout mismatch, architecture disagreement, moved threshold
or widened scope is STOP, not a mathematical counterexample.

## The six frozen fields

```text
EQUATION
  Statements A-F and their endpoint conventions exactly as displayed.

CODE
  probes/P-O5-GOLDEN-PROFILE-TRANSFER-1/verify.py.
  Python standard library only. Exact integer, Fraction and Q(alpha)
  arithmetic only. No float, complex, random, network, external data,
  special function or external package.

CARRIER
  The Public Canon v67 basis; the merged #611 alpha/X/I golden shell axis;
  X_k,M_k,r_k; kappa and exact reduced mantissa z; F_all and F_nu;
  canonical sparse profiles; ordered Pair, P_s, D_s, H_f and Q_f; and the
  actual restricted Mobius sequence nu from merged #609, its finite-selector
  class F_nu, and its use via finite cutoffs.

SYSTEMATICS
  I_-1={1}; shells are open-left and closed-right; xy=alpha has zero carry;
  r_k is the least residue in 0..10; zero profile entries are deleted;
  profile keys are exact and collision-free; all factor pairs are ordered;
  annuli use floor(N/11); the universal profile theorem is applied to actual
  nu only through finite truncation; F_all and the finite-selector class F_nu
  are not conflated; the
  #595 evaluation ladder supplies no evidence; no orientation is selected.

THRESHOLD
  G01 through G08 pass exactly. Production-path mutations B1 through B5 fire
  at their frozen witnesses. The complete stdout is the nine frozen LF lines
  below. Exit zero, empty stderr and byte identity are required.

LAYER
  NOT_APPLICABLE. Exact Lucas arithmetic and finite signed profile algebra
  only. No state, manifold, boundary, support-to-stream lift, stream, measure,
  decoder, observable, physical dictionary or SI statement.
```

## Frozen negative controls

Each breaker is implemented as a separate mutation of the corresponding
production path. Merely reasserting the correct witness does not satisfy G07.

```text
B1  Delete the +1 in X_(k+1)=3X_k-X_(k-1)+1.
    First witness k=1: the mutation gives X_2=3*2-1=5; correct X_2=6.

B2  Force epsilon=0 in the skew product.
    Witness a=b=41, i=j=3: the mutation predicts shell 6, while
    41^2=1681 has kappa(1681)=7.

B3  Replace the profile step kernel by the complete shell-mass pairing.
    Witness g=-delta_41, (i,j)=(3,3), Y=842: the mass-only complete pair is
    1, while the step-kernel and direct pair are 0. The equal-mass witness
    f=-delta_19 has direct value 1.

B4  Replace the residue 5-cycle by period four.
    First witness k=4: the mutation repeats r_0=1, while actual r_4=2.

B5  Impose the naive Lucas recurrence on the actual Q values.
    Witness step k=5 to 6: c_5=0 and the mutation gives -58, while the exact
    value is -52.
```

All five witnesses were exposed only in non-formal reasoning and are frozen
here before the public pin.

## Frozen verifier gates

```text
G01  Audit A_k=L_(2k) and X_k for k=0..50, the X recurrence for k=1..49,
     the residue pattern for k=0..50, the repeated state
     (r_5,r_6)=(r_0,r_1), and failure of candidate periods 1 through 4.

G02  Audit M_k and r_k for k=0..50, the exact c_k formula and cycle for
     k=1..49, and the homogeneous order-seven recurrence for k=0..43.

G03  Using exact Q(alpha) arithmetic, audit 1<z(n)<=alpha and the complete
     skew-product law for every ordered pair 1<=a,b<=512, explicitly
     including the unit and 41*41 carry cases.

G04  Use exactly these canonical sparse fixtures:

       F_EMPTY = {}

       F_BOUNDARY = {
         1:2, 2:-3, 3:5, 6:-7, 7:11, 17:-13, 18:17, 46:-19,
         47:23, 122:-29, 123:31, 321:-37, 322:41, 842:-43
       }

       F_MIXED = {
         3:0, 19:-1, 29:2, 31:-3, 41:4, 59:-5, 61:6, 360:0,
         361:-7, 500:8, 841:-9, 842:10, 843:-11, 1681:12
       }

     Canonicalization must remove the zero entries at 3 and 360.

     For every fixture and shell, audit collision-free exact profile keys and
     decode(Profile_k(f))=f restricted to I_k. Decoding z alpha^k must have
     zero alpha coefficient and a positive integral rational coefficient.

     Use exactly

       Y_VALUES=(0,1,2,5,6,10,11,17,18,45,46,47,121,122,123,
                 320,321,322,360,361,841,842,843,1680,1681).

     For every fixture, every Y in Y_VALUES, and every ordered shell pair
     -1<=i,j<=max_shell(f), compare direct integer Pair_(i,j) with the exact
     Q(alpha) profile kernel. For each fixture and Y, also compare direct H_f
     and Q_f with the complete profile sums. For every fixture and K=4..12,
     compare direct Q_f(X_K) with the four-diagonal form. Audit all three
     threshold identities exactly for every K=4..30.

G05  Audit f=-delta_19 and g=-delta_41: membership in F_nu; equal complete
     shell-mass sequences and D_s values; different exact profiles; and
     Q_f(842)=1, Q_g(842)=0.

G06  Independently construct nu through X_6=321 by exact trial division or
     sieve and factor the separate square witness 361 exactly. Pin nu(1)=1;
     nu(19)=nu(29)=nu(31)=nu(41)=-1; and nu(11)=nu(361)=0. Compute the
     ordered-pair values (-8,-22,-52) at
     (X_4,X_5,X_6), verify -52!=-58, and verify c_5=0.

G07  Execute the five separate production-path mutations B1-B5 and require
     each to differ at its frozen witness.

G08  Enforce LF-only source and an exact import allowlist. Reject float or
     complex literals, names and calls; math, cmath, decimal, numpy, sympy,
     random, network and subprocess imports; and dynamic calls including
     __import__, eval, exec, compile, getattr, globals, locals and vars.
```

The exact accepted stdout is

```text
G01 PASS Lucas cutoff recurrence and residue 5-cycle
G02 PASS lower cutoff forcing and order-seven transfer
G03 PASS exact golden skew-product multiplication
G04 PASS arbitrary-profile kernels and Lucas thresholds
G05 PASS scalar shell-mass closure no-go
G06 PASS actual nu Q values and recurrence failure
G07 PASS breakers B1-B5 frozen witnesses
G08 PASS exact-quadratic stdlib AST firewall
VERIFY RESULT 8/8 ALL PASS
```

## Development disclosure

The result-exposed formulas and witnesses in issue #612 predate this pin and
carry no evidence credit. Separate non-formal reconnaissance also enumerated
additional actual-`nu` cutoff values while auditing the proposed mechanism; it
is not committed as evidence and sets no threshold.

After issue #612 and before this pin, a development copy of the verifier was
executed five times while implementing exact `Q(alpha)` arithmetic, sparse
complete scalar states, the frozen gates and production-path breakers. The
first run passed G01 through G07 and correctly stopped at G08 because the
firewall detected its then-own loaded name `float`. The second and third runs
returned `8/8`; the third followed the stronger complete sparse-state audit in
G05. The fourth, after the first preregistration-alignment edits, also returned
`8/8`. The fifth, after making the implemented audit ranges byte-for-byte
consistent with the frozen G01/G02 contract, returned `8/8`. All five runs were
non-formal, uncommitted and carry no evidence credit.
No accepted formal invocation occurred before the fresh two-file pin and exact
public readback.

## Formal execution discipline

The first pushed probe commit contains only this `PREREG.md` and `verify.py`.
Record the pin commit and both file hashes. After exact public readback, run

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

and require exit zero, exactly `PYTHON_STARTUP_CLEAN` plus LF, and empty
stderr.

Only then may the single accepted scientific command run:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-GOLDEN-PROFILE-TRANSFER-1/verify.py
```

The accepted stdout becomes `EXPECTED.txt`. `RUN.md` and `RESULT.md` are
post-pin records only. A changed theorem, carrier, witness, threshold,
`PREREG.md` byte or verifier byte requires a fresh identifier or the exact
repository disposition; it is never repaired after the pin.

## Status boundary and explicit nonclaims

Before execution this document is `UNRUN` and has no scientific evidence
credit. A passing exact formal run audits the proof-first package and may
support at most `candidate-T` for a later sealed fold. This probe itself
changes no Canon, Registry, Frontier, dependency, gate, evidence, workflow,
Note, reproduction or existing probe file.

No RH or GRH result, cancellation estimate, new summatory bound,
spectral-radius bound, contraction, zero-free region, analytic continuation,
Hecke or automorphic statement, or fixed-dimensional closure theorem for the
actual restricted Mobius sequence is claimed.

No recurrence for the actual `nu` is excluded except the one displayed naive
Lucas recurrence. In particular, no different recurrence with periodic or
profile-dependent forcing is excluded. No finite summary other than state derived solely from the
complete scalar shell masses or `D_s` is excluded. No uniqueness or optimality
of the golden coordinate among geometric coordinates is claimed.

No selected split orientation, physical interpretation, probability
statement, SI statement or L1-L6 lift is claimed. The sparse profile is exact
finite algebraic bookkeeping on each shell, not an L6 measure. The probe does
not claim that integer addition is replaced by Lucas addition or that Nature
uses a different number line.
