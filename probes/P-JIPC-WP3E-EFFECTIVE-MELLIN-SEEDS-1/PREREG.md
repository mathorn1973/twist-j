# P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1 preregistration

Date: 2026-08-25

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No
scientific result is earned by this file. The accepted `verify.py` may be
read, parsed, compiled, and inspected statically before the pin, but it has
not been imported or executed. This file and `verify.py` must be committed
together, pushed, and read back byte for byte from the public remote before
the first formal scientific execution.

Public claim lock: issue 566, opened and locked before this file was
committed.

```text
public_claim_lock: issue 566
```

```text
branch:  probe/P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1
path:    probes/P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1/
owner:   A. M. Thorn
mode:    RESULT-EXPOSED, proof-first; the verifier is an exact finite audit
```

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v64
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v64
TAG_OBJECT:     09e3fa3c55230c87333f235e9bdd1e10ff670f7b
TAG_TARGET:     505f4096453a52bacb8c8de26583b38874ea408b
CONTENT_COMMIT: 78b8172a9814469415b818e9b431288b709e44ab
CANON_SHA256:   1d81a2a2736fb2f8ce8ae3f3153a519633fd70736bf147c4930c731556805d81
CANON_BYTES:    336716
BASE_COMMIT:    505f4096453a52bacb8c8de26583b38874ea408b
ACTION_LAYER:   L1 exact computable complex analysis only
```

The public claim issue is the sole claim lock for this identifier. This probe
changes exactly its own directory. It changes no Canon, registry, frontier,
dependency, evidence, gate, release, or workflow file. Public Canon v64 is the
only authority. An attachment, internal draft, archive, historical validator,
or private parent is discovery context at most and is not evidence, code, a
premise, or an instruction for this probe.

## Result exposure

`RESULT-EXPOSED`, not blind. The intended formulas, a bounded implementation,
and the distinction between a finite audit and a universal theorem were known
before this preregistration. No blindness claim is made. The public theorem
below is newly stated from explicit definitions and rests on its written
proof. The accepted public verifier is a fresh, bounded audit for this public
identifier. It has not been imported or executed at pin time.

The maximum later claim is a ceiling, not a status already earned:

```text
JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS [T], L1
```

## Field 1: equation, exact meanings, theorem, and written proof

### 1.1 The fixed effective real constant

For `q in {5,239}` and `N>=1`, put

```text
a_(q,n) = 1 / ((2n+1) q^(2n+1)),
S_(q,N) = sum_(n=0)^(N-1) (-1)^n a_(q,n).
```

The positive terms `a_(q,n)` strictly decrease to zero. Define `A_q` as the
unique real in every consecutive-partial-sum interval

```text
I_(q,N) = hull(S_(q,N), S_(q,N+1)).
```

Thus `width(I_(q,N))=a_(q,N)`. The public claim names the same
series-defined constant `p=pi_atan`. Freeze the following exact aliases, and
no generic parameter:

```text
p_M := p := pi_atan := 16 A_5 - 4 A_239.
```

This equation is the definition of all three aliases. Here `pi_atan` is only
the public identifier for this Machin-series Cauchy name; it is not an
identification with a circle, Gaussian, Gamma, SI, physical, or library
constant.

### 1.2 Domain and the three independent definitions

Let

```text
D = {s in C : Re(s)>0}.
```

Freeze `kappa_j := q_j` as two exact aliases for the public claim's final
tuple coordinate, and freeze the three tuples

```text
j   w_j  m_j  nu_j  q_j=kappa_j
E    2    1     0       1
O    2    1     1       1
C    4    2     0       2
```

and define, as complex improper Cauchy limits,

```text
F_j(s) = w_j integral_(-infinity)^infinity
         exp_C((m_j s+nu_j)u-kappa_j p_M exp_R(2u)) du.
```

The public names are `E=F_E`, `O=F_O`, and `C=F_C`. Each branch reads only
its own tuple and the common elementary arithmetic, exponential, integration,
and fixed `p_M` name. “Independent” means precisely this construction
provenance. It is not probabilistic independence and it does not assert that
the three resulting values are algebraically unrelated.

For `x>0`, define

```text
x^s = exp_C(s log_R(x)).
```

The exact substitution-compatibility targets are

```text
E(s) = 2 integral_0^infinity exp_R(-p_M x^2) x^(s-1) dx,
O(s) = 2 integral_0^infinity exp_R(-p_M x^2) x^s dx,
C(s) = 4 integral_0^infinity exp_R(-2p_M r^2) r^(2s-1) dr.
```

These are three value representations of the already independent definitions,
not a cross-definition of one branch through another.

### 1.3 Exact meaning of an effective uniform holomorphic name

A rational compact rectangle is

```text
K=[a,b]+i[c,d],  a,b,c,d in Q, 0<a<=b, c<=d.
```

A rational rectangular complex ball is

```text
B=[x-r_R,x+r_R]+i[y-r_I,y+r_I]
```

with rational `x,y,r_R,r_I` and nonnegative radii. Throughout this protocol
its radius means exactly `max(r_R,r_I)`, the radius in the coordinate
supremum norm. It never means the Euclidean radius of the rectangle. A
complex-modulus error bound `delta` therefore yields such a ball by taking
both coordinate radii at most `delta`; no hidden `sqrt(2)` conversion is used.

For every branch `j`, rectangle `K`, and precision `n in Nat`, an effective
uniform holomorphic name must terminate and return

```text
Name_j(K,n)=(A,B,M,P_j,K,n,epsilon_j,K,n,Eval_j,K,n),
```

where:

1. `A,B,M` are positive-cut/panel integers, with `B>=1` and `M>=8`;
2. `P_j,K,n` is a finite sum of entire exponentials in `s`; its coefficients
   contain the fixed computable constant `p_M` by its Cauchy-name interface,
   so it is not falsely described as finite rational data;
3. `epsilon_j,K,n` is rational and
   `sup_(s in K)|F_j(s)-P_j,K,n(s)|<=epsilon_j,K,n<=2^(-(n+1))`;
4. `Eval_j,K,n(z)` terminates for every rational complex `z in K` and
   returns a rational rectangular complex ball of radius at most `2^-n`
   containing `F_j(z)` after combining approximation and evaluation error.

No oracle for an arbitrary externally supplied computable point is in scope.
Uniformity is the supremum statement on every rational `K`, not a finite set
of samples.

### 1.4 Candidate theorem

The written theorem is:

> The fixed series constant `p_M` has an exact rational Cauchy name and obeys
> `3<p_M<16/5`. For each `j in {E,O,C}`, the displayed improper integral
> exists absolutely on `D`, the construction above gives an effective uniform
> holomorphic name on every rational compact rectangle in `D`, and `F_j` is
> holomorphic on `D`. The three branches have the frozen independent
> construction provenance. The three displayed positive-real integral
> representations agree exactly with their logarithmic-coordinate definitions.

The proof below is universal. The finite verifier in Field 2 is only its
audit.

### 1.5 Machin-name proof

The alternating partial sums with an even number of terms increase, those
with an odd number decrease, and their gap is `a_(q,N)`. Completeness gives
one common point `A_q`; conversely the shrinking gap makes it unique. Since

```text
a_(q,N) <= 5^(-(2N+1)),
```

the exact finite search for an `N` with

```text
16 a_(5,N)+4 a_(239,N) <= 2^-n
```

terminates for every `n`. Outward rational interval arithmetic on
`16 I_(5,N)-4 I_(239,N)` is therefore a total Cauchy name for `p_M`.

The first two alternating terms at `q=5` and the first upper term at `q=239`
give

```text
p_M > 16(1/5-1/(3*5^3))-4/239
    = 281476/89625
    > 3.
```

Also `0<A_239` and `A_5<1/5`, so

```text
p_M < 16/5.
```

Both inequalities are strict and use only integer comparison. They supply the
fixed lower and upper bounds used below.

### 1.6 Uniform left and right tails

Fix `K` and a branch `j`, and abbreviate

```text
lambda_j = m_j a+nu_j > 0,
h_j      = m_j b+nu_j.
```

For `u<=-A`, the negative Gaussian term can only decrease the modulus, while
the worst real part on `K` is `lambda_j u`. Hence

```text
sup_(s in K) w_j integral_(-infinity)^(-A) |...| du
 <= (w_j/lambda_j) exp_R(-lambda_j A)
 <= (w_j/lambda_j) 2^(-floor(lambda_j A))
 =: L_j(A).
```

The last inequality follows from `exp_R(1)>2`. Starting at `A=1`, choose the
first integer with `L_j(A)<=2^(-(n+3))`. Because `floor(lambda_j A)` tends to
infinity, this exact positive-integer search terminates.

For `u>=1`, the exponential series gives `exp_R(2u)>=2u^2`. Since `p_M>3`,
if

```text
B >= B0_j := max(1,ceil((h_j+1)/(6 kappa_j))),
```

then for `u>=B`

```text
h_j u-kappa_j p_M exp_R(2u)
 < h_j u-6 kappa_j u^2
 <= -u.
```

Consequently

```text
sup_(s in K) w_j integral_B^infinity |...| du
 <= w_j exp_R(-B)
 <= w_j 2^-B
 =: R_j(B).
```

Starting at `B0_j`, choose the first integer with
`R_j(B)<=2^(-(n+3))`; the exact search terminates. The two tails total at
most `2^(-(n+2))`.

### 1.7 Compact midpoint bound and termination

On `I=[-A,B]`, write

```text
f_j(s,u)=w_j exp_C((m_j s+nu_j)u-kappa_j p_M exp_R(2u)).
```

Its exact `u` derivative is

```text
partial_u f_j
 = f_j(s,u)(m_j s+nu_j-2 kappa_j p_M exp_R(2u)).
```

Define the rational bound

```text
Z_K = max(|m_j a+nu_j|,|m_j b+nu_j|)
      +m_j max(|c|,|d|).
```

Obtain by the rational exponential enclosure primitive rational numbers

```text
X_B >= exp_R(2B),
U_K >= exp_R((m_j b+nu_j)B).
```

For negative `u`, `(m_j Re(s)+nu_j)u<=0`; for positive `u` it is at most
`(m_j b+nu_j)B`. Dropping the negative Gaussian term and using
`p_M<16/5` therefore gives the global rational derivative bound

```text
D_j,K = w_j U_K (Z_K+2 kappa_j (16/5) X_B)
      >= sup_(s in K,u in I)|partial_u f_j(s,u)|.
```

For `M` equal cells `I_k=[l_k,r_k]` of length `ell=(A+B)/M`, with midpoint
`u_k`, define a specific rational cell certificate as follows. Use the
rational exponential enclosure primitive to obtain

```text
X_tilde_k >= exp_R(2r_k),
H_k = max((m_j a+nu_j)l_k,(m_j a+nu_j)r_k,
          (m_j b+nu_j)l_k,(m_j b+nu_j)r_k),
U_tilde_k >= exp_R(H_k),
D_local,k = w_j U_tilde_k
            (Z_K+2 kappa_j (16/5) X_tilde_k),
D_cell,k = min(D_j,K,D_local,k).
```

The endpoint formula for `H_k` is the exact maximum of the bilinear
linear-exponent term on `[a,b] x I_k`; dropping the negative Gaussian term is
again an upper bound. Hence `D_local,k` and `D_j,K` are both sound derivative
bounds on the cell. Their displayed minimum is therefore a total, explicit
rational bound for `|partial_u f_j|` on `K x I_k`, and
`D_cell,k<=D_j,K` literally.

The fundamental theorem and the triangle inequality now give on each cell

```text
integral_cell |f_j(s,u)-f_j(s,u_k)| du
 <= D_cell integral_cell |u-u_k| du
 = D_cell ell^2/4.
```

The cellwise midpoint certificate is therefore

```text
Q_M=sum_k D_cell,k ell^2/4,
```

obeys

```text
Q_M <= D_j,K (A+B)^2/(4M).
```

Starting at `M=8` and doubling therefore eventually gives

```text
L_j(A)+R_j(B)+Q_M <= 2^(-(n+1)).
```

This proves termination; the cellwise calculation supplies the sharper
executed certificate.

The returned finite approximant is

```text
P_j,K,n(s)=(A+B)/M sum_(k=0)^(M-1)
            w_j exp_C((m_j s+nu_j)u_k
              -kappa_j p_M exp_R(2u_k)).
```

Every summand is the exponential of an affine function of `s`, with fixed
computable coefficients, and hence is entire. The two tail bounds and the
midpoint certificate prove

```text
sup_(s in K)|F_j(s)-P_j,K,n(s)| <= 2^(-(n+1)).
```

### 1.8 Exact evaluator budget

Only finitely many values occur in `P_j,K,n`. Fix a rational `z in K`, let
`eta=2^(-(n+1))` be the remaining point-evaluation budget, put

```text
theta = eta/(4 w_j (A+B)),
```

and retain the rational global bounds `X_B>=exp_R(2B)` and
`U_K>=exp_R((m_j b+nu_j)B)` from the derivative proof.

First refine the `p_M` Cauchy name to a positive rational interval
`P=[p_-,p_+] subset (3,16/5)` with

```text
delta_p=width(P) <= theta/(2 kappa_j U_K X_B).
```

The strict rational margins proved in Section 1.5 and the shrinking Machin
interval widths make the simultaneous search for containment in `(3,16/5)`
and this `delta_p` bound terminate.

For every rational midpoint `u_k`, independently evaluate the inner
coefficient to a positive rational interval

```text
X^(k)=[x^-_k,x^+_k] contains exp_R(2u_k),
delta_x,k=width(X^(k)) <= 5 theta/(32 kappa_j U_K).
```

The inner Taylor enclosure terminates by the explicit power-series remainder.
Moreover `0<x^+_k<=X_B` after intersecting with the already sound global
enclosure. Exact positive interval multiplication gives

```text
width(kappa_j P X^(k))
 <= kappa_j ((16/5) delta_x,k+X_B delta_p)
 <= theta/U_K.
```

Thus the full exponent rectangle

```text
(m_j z+nu_j)u_k-kappa_j P X^(k)
```

contains the exact exponent and has uncertain real width at most
`theta/U_K`; its imaginary coordinate is exact rational data. Every exponent
in that rectangle has real part at most `(m_j b+nu_j)B`, so the complex
exponential mean-value bound turns the input uncertainty into output error at
most `theta`. Refine the outer complex Taylor enclosure until its own outward
rounding error is also at most `theta`. This search terminates by the same
explicit remainder theorem.

Each exponential term is now enclosed with error at most `2 theta`. After
multiplication by `w_j(A+B)/M` and summation over `M` terms, the complete
evaluation error is at most

```text
w_j(A+B) 2 theta = eta/2 < eta.
```

All other operations are exact rational interval operations. Enlarging the
resulting ball by the already certified uniform approximation error, which is
at most `eta`, produces radius less than `2^-n` around `F_j(z)`. This proves
both rational complex-ball enclosure and termination without treating either
`p_M` or `exp_R(2u_k)` as exact rational data.

### 1.9 Improper limit, absolute convergence, and gluing

For each `K`, the tail bounds show that the compact-cut integrals form a
uniformly Cauchy net as `A,B` increase. Completeness of `C` gives a uniform
limit `F_j,K`. The same bounds applied to the absolute value prove absolute
convergence. If `K` and `K'` overlap, both limits at an overlap point are the
limit of the same compact-cut net, so uniqueness of a Cauchy limit makes them
equal. Rational rectangles with positive real margin cover `D`; the local
limits therefore glue to one well-defined `F_j:D->C`.

The midpoint estimate proves that the displayed `P_j,K,n` converge uniformly
to that same limit. There is no second value selected by the evaluator or by
the choice of rectangle.

### 1.10 Locally uniform holomorphy

Each `P_j,K,n` is entire. For every point of `D`, choose a rational rectangle
whose interior contains the point and whose left edge remains positive. On
that rectangle, `P_j,K,n` converges uniformly to `F_j`. The locally uniform
limit theorem in the frozen TCB therefore makes `F_j` holomorphic near the
point, and hence on all of `D`. This conclusion is carried by the written
universal proof, not by the verifier's one compact rectangle.

### 1.11 Exact `x=exp_R(u)` compatibility

On every finite cut, `x=exp_R(u)` is a positive orientation-preserving `C1`
bijection and `du=dx/x`. With `x^s=exp_C(s log_R(x))`, componentwise complex
substitution gives exactly

```text
2 integral_(-A)^B exp_C(su-p_M exp_R(2u)) du
 =2 integral_(exp_R(-A))^(exp_R(B))
    exp_R(-p_M x^2)x^(s-1) dx,

2 integral_(-A)^B exp_C((s+1)u-p_M exp_R(2u)) du
 =2 integral_(exp_R(-A))^(exp_R(B))
    exp_R(-p_M x^2)x^s dx,

4 integral_(-A)^B exp_C(2su-2p_M exp_R(2u)) du
 =4 integral_(exp_R(-A))^(exp_R(B))
    exp_R(-2p_M r^2)r^(2s-1) dr.
```

The exponential cuts decrease to zero and increase to infinity cofinally.
The already proved absolute tail bounds permit the Cauchy-limit passage.
Thus the three positive-real integral representations agree exactly with the
three logarithmic-coordinate definitions on `D`. No identity between two
different branches is used or obtained.

### 1.12 Branch isolation

The construction graph has three edges from the common primitive package and
the fixed `p_M` name, one to each frozen tuple. Each branch reaches its own
`F_j`, approximants, error certificates, and evaluator before the three names
are collected into the result. No branch has another `F_j`, approximant, or
value as a predecessor. This is a direct property of the displayed
definitions and is audited syntactically by the three distinct public
wrappers. The collection node is named exactly
`INDEPENDENT_EOC_SEED_PACKAGE`, matching the public claim lock. Collection
does not add a cross-branch mathematical identity.

## Field 2: accepted code

Accepted path:

```text
probes/P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1/verify.py
```

The accepted file is fresh Python 3.12 standard-library code. Its sole import
is exactly

```python
from fractions import Fraction
```

It takes zero arguments and reads no file, archive, standard input,
environment variable, clock, hostname, platform field, network resource, or
external process. It writes no file and performs no dynamic code loading. It
uses no helper program. Its only observable output is deterministic stdout
and, on integrity failure, stderr. It uses exact integers, `Fraction`,
rational intervals, and rectangular complex balls; it contains no float,
tolerance, randomness, or decision-bearing `assert`.

The repository verifier checker imposes the decision-bearing hard timeout of
600 seconds, and the verifier must complete within that bound. The surrounding
workflow job may have a 25-minute outer ceiling, but that larger wrapper limit
does not relax the 600-second verifier threshold. A completed PASS or
scientific FIRED decision exits zero with empty stderr and exact frozen stdout. Authority,
pin, internal arithmetic, security, resource, or incomplete-execution failure
exits nonzero and is `STOP`. The verifier audits the finite surface in Field 4;
it does not execute the universal limit proof and cannot by itself earn `T`.

At preregistration time it has not been imported or executed.

## Field 3: carrier, data, and exact TCB

### 3.1 Carrier and data

```text
integer/rational carrier: N, Z, reduced Q and exact finite searches
constant carrier:         the single p_M Cauchy name of Field 1
parameter carrier:        s in D={Re(s)>0}
compact carrier:          rational closed rectangles K subset D
branch carrier:           exactly E, O, C with the frozen three tuples
output carrier:           finite entire exponential sums, rational error
                          certificates, rational rectangular complex balls
external datasets:        none
parent archives:          none
```

No private hash, archived helper, hidden parent definition, inherited
certificate, or precomputed value is a premise. The only repository authority
is the Public Canon v64 tuple above.

### 3.2 `COMPLEX_BALL_MELLIN_TCB/v1`

This identifier means exactly the following positive list:

1. natural-number induction; exact integer and reduced rational field
   arithmetic, order, floor, ceiling, powers, factorials, and finite search;
2. the complete ordered real field, the complex field, complex conjugation,
   modulus, the triangle inequality, and Cauchy completeness;
3. closed rational real intervals and rectangular complex balls with sound
   inclusion operations and outward rational rounding;
4. `exp_R` and `exp_C` defined by their power series, with coefficientwise
   differentiation, the product law, positivity and monotonicity on `R`,
   `|exp_C(z)|=exp_R(Re(z))`, and the rational Taylor tail
   ```text
   sum_(k>N) R^k/k!
    <= (R^(N+1)/(N+1)!)/(1-R/(N+2))  when R/(N+2)<1;
   ```
5. the elementary series consequences `exp_R(1)>2`, `exp_R(1)<3`, and
   `exp_R(2u)>=2u^2` for `u>=0`;
6. the positive inverse `log_R` of `exp_R`, with derivative `1/x`, and the
   positive `C1` substitution theorem;
7. the compact real Riemann integral, complex integration componentwise,
   linearity, additivity, the norm bound, the fundamental theorem, and the
   `C1` change-of-variables theorem on a compact interval;
8. the Lipschitz midpoint lemma
   `|integral_I f-|I|f(mid(I))|<=D|I|^2/4` when `|f'|<=D`;
9. uniqueness of Cauchy limits, uniform Cauchy completeness, and gluing of
   equal limits on overlaps;
10. finite sums and products of holomorphic functions are holomorphic, the
    complex exponential is entire, and a locally uniform limit of
    holomorphic functions is holomorphic;
11. the Archimedean property and cofinality of the exponential cut sequence
    `[-A,B]` with the positive cut sequence
    `[exp_R(-A),exp_R(B)]`.

The TCB does not contain the existence, tail bounds, effective name,
holomorphy, independence, or substitution compatibility of the three target
integrals. Those are derived in Field 1. It contains no target value table,
product or duplication theorem, continuation principle, Fourier theorem,
physical measure, or protocol verdict.

```text
FORMAL_VERIFICATION = NOT_CLAIMED
```

The exact finite implementation is trusted code whose public two-architecture
execution audits this written proof; it is not a proof-assistant kernel.

## Field 4: systematics and complete finite audit surface

The verifier's finite surface is frozen before execution:

```text
Machin enclosure:
  exact alternating rational enclosure at BITS=16;
  width <=2^-16 and strict 3<p_M<16/5.

branches:
  E=(2,1,0,1), O=(2,1,1,1), C=(4,2,0,2);
  three distinct public wrappers and frozen provenance.

uniform compact:
  K=[1,3/2]+i[-1/2,1/2];
  uniform-name precision b=1 for each of E,O,C;
  exact left/right formulas, minimal accepted cuts;
  midpoint starts at 8 panels and doubles cellwise until
  tail+quadrature<=2^(-(b+1)).

rational point audit:
  s=3/2+i/2;
  b=2 and b=3 balls for each branch;
  each radius meets its budget and coarse/fine balls overlap.

proof-control mutations, exactly 12/12:
  Machin coefficients;
  Machin strict bounds;
  seed tuples;
  branch provenance;
  left tail;
  right tail;
  cut minimality;
  midpoint one-quarter cell error;
  panel doubling;
  finite-entire marker;
  relative-TCB scope;
  written-proof/carrier separation.
```

For this finite compact only, the accepted verifier is expressly allowed to
use a different concrete sound cell certificate. Let `ExpInt(2I_k)` denote
the verifier's frozen outward-rational interval enclosure of
`exp_R(2I_k)`. It interval-evaluates

```text
R'_k = ([m_j a+nu_j,m_j b+nu_j] I_k)
       -kappa_j [3,16/5] ExpInt(2I_k),
X'_k = upper(ExpInt(2I_k)),
U'_k >= exp_R(upper(R'_k)),
D'_local,k = w_j U'_k (Z_K+2 kappa_j (16/5) X'_k),
D_audit,k = min(D'_local,k,D_j,K).
```

All interval operations here are outward rational and contain the exact
operands, because `p_M in (3,16/5)`. Thus `D'_local,k` and `D_j,K` are both
sound derivative bounds. The verifier uses exactly

```text
D_audit,k=min(D'_local,k,D_j,K).
```

This executed certificate need not equal the explicit `D_cell,k` selected by
the universal Name algorithm in Section 1.7, and no ordering between
`D'_local,k` and the textual `D_local,k` is assumed. Both independently
dominate the same cell derivative. The verifier additionally checks

```text
sum_k D_audit,k ell^2/4
 <= D_j,K (A+B)^2/(4M),
```

so the finite interval calculation is an independent sound certificate under
the same written global termination bound, not a change to the universal
Name algorithm.

Every mutation must fail at its named semantic guard, not merely at a final
snapshot. The completed PASS stdout is frozen as

```text
JIPC_WP3E_EFFECTIVE_MELLIN_SEEDS_AUDIT 1
ARITHMETIC Q_INTERVAL_COMPLEX_BOX PASS
MACHIN_ATAN 3<P<16/5 BITS=16 PASS
SEED_TUPLES E,O,C PASS
BRANCH_PROVENANCE INDEPENDENT PASS
TAIL_BOUNDS LEFT_RIGHT CUTS PASS
MIDPOINT_REFINEMENT CELLWISE PASS
FINITE_APPROXIMANTS K=[1,3/2]x[-1/2,1/2] PASS
SAMPLE_BALLS S=3/2+i/2 BITS=2,3 PASS
PROOF_CONTROLS 12/12 PASS
THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT
RESULT PASS
```

This is the complete computational window. It contains no universal
quantifier. The universal conclusion comes only from the written proof in
Field 1.

## Field 5: immutable failure thresholds and decision

Thresholds and scope never move after the pin.

```text
JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-CONFIRMED
  the self-contained universal proof remains valid; all exact finite gates
  and 12/12 proof controls pass; the pin and public readbacks pass; x86_64
  and aarch64 produce byte-identical expected stdout. The later status ceiling
  is candidate T because the independent proof carries the quantifiers.

JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-FIRED
  a completed exact argument or calculation fires a scientific falsifier
  below. The fired result is preserved and merged. No domain, TCB, threshold,
  branch tuple, or wording is changed to rescue the route.

JIPC-WP3E-BOUNDED-AUDIT-C
  the exact finite PASS surface completes without a scientific counterexample,
  but independent review does not accept the universal written proof as
  theorem-grade. The maximum result is then C at exactly the BITS=16,
  K, b, sample, tuple, and 12-control surface of Field 4. It clears no
  universal seed or holomorphy obligation. This fallback cannot replace a
  fired exact counterexample.

STOP
  authority, collision, pin, public readback, exactness, internal arithmetic,
  deterministic output, stderr, mutation, security, timeout, resource, or
  architecture integrity fails. A verifier defect that prevents a completed
  formal run spends this identifier and requires an ABANDONED record under
  POLICY.md.
```

Frozen scientific falsifiers:

```text
F1  the alternating intervals fail to contain one common p_M, their effective
    width search fails to terminate, or the exact strict bounds 3<p_M<16/5
    are false;
F2  one displayed logarithmic integral fails absolute convergence at a point
    of D, or the left or right uniform tail inequality is false;
F3  the derivative enclosure, one-quarter midpoint error, global O(1/M)
    bound, or panel-doubling termination is false;
F4  for some frozen branch, rational K subset D, and n, the prescribed name
    construction does not terminate or its rational supremum error exceeds
    the claimed bound;
F5  the coefficient-name or exponential evaluation budget fails to enclose
    F_j(z) at a rational z in K;
F6  compact cuts are not Cauchy, limits disagree on an overlap, or the three
    local constructions fail to glue to functions on D;
F7  one F_j is not holomorphic at a point of D despite all stated TCB
    premises;
F8  one finite-cut x=exp_R(u) formula or its cofinal improper-limit passage is
    false;
F9  a construction branch reads another seed or a target cross-branch
    identity before the independent three-branch join;
F10 a finite verifier PASS is necessary to rescue a false universal clause,
    or the completed exact audit contradicts the written proof.
```

Pin, hash, architecture, implementation, or TCB-identity mismatches without an
exact negation of F1-F10 are integrity `STOP`, not scientific falsifiers.

## Field 6: action layer and scope firewall

`L1` exact computable complex analysis only.

This probe fixes only the single series-defined `p_M`; it does not establish a
generic theorem for an externally supplied positive-real oracle. It does not
identify `p_M` with the Canon's classical or circle constant. It does not
establish `E(s)O(s)=C(s)`, a product or duplication identity, analytic or
meromorphic continuation, a functional equation, a local zeta object,
Fourier self-duality, or an archimedean place. It imports no QPOS parent and
claims no compatibility with a private or historical family. The later WP3F
program remains `UNRUN` and outside this identifier.

The rational-point evaluator is not an arbitrary computable-point oracle. The
three positive-real representations are only substitutions within each
branch. They supply no physical measure, apparatus, event stream, probability,
Born law, decoder, dynamics, entropy, spacetime, force, SI value, or L2-L6
lift.

```text
FORMAL_VERIFICATION = NOT_CLAIMED
PROTOCOL_VERDICT    = NO_VERDICT
SAMPLING NOT PROVIDED.
```

## Formal order

1. Commit exactly this `PREREG.md` and the never-executed accepted `verify.py`
   together; push the full pin commit.
2. In a separate clean checkout, read both files back from that immutable
   public commit and record the full pin, SHA-256, bytes, lines, LF, and final
   LF.
3. Only then run from the repository root exactly
   `python3 probes/P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1/verify.py` in a neutral
   Linux environment, with zero arguments and empty stderr on completion.
4. Commit exactly `EXPECTED.txt`, `RUN.md`, and `RESULT.md` afterward. Never
   alter either pinned file.
5. Open one probe-only pull request. Require byte-identical Python 3.12 output
   on GitHub x86_64 and aarch64 plus aggregate `check`.
6. Merge with a merge commit only. Never amend, rebase, squash, force-push,
   rename, resume, or reuse this identifier after the pin.
7. Any registry or Canon treatment is a separately claimed and sealed later
   fold.
