# C-RH-STIELTJES-WIDDER-EULER-1-N preregistration

```text
STATUS:         NON-CANONICAL INCUBATION / PROOF-FIRST / RESULT-EXPOSED
AUTHORITY:      none
TARGET LINE:    PUBLIC context only
OWNER SESSION:  rh-stieltjes-widder-euler-2026-08-20
PUBLIC PARENT:  issue #471
MATHEMATICAL PARENT: issue #374
ADJACENT:       issue #469, public LAMBDA-COCYCLE rows
CANON WRITE:    forbidden
FORMAL PROBE:   none
```

This file is frozen before any exact script execution in this lane. The result
is exposed: the expected honest outcome is a source-side reduction, not a proof
of RH. The accepted breaker is written and pinned only after this file is read
back remotely. The positive proof and verifier are written only after the
breaker is frozen and run.

## Authority and basis

Public Canon v57 is ACTIVE on `mathorn1973/twist-j main`.

```text
main/tag:       4ef54f0c34f80897af0121a2d93b710e70a8377c
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
REGISTRY:       292 claims; T 174, D 43, C 32, H 3, O 24, F 16
```

The tag and content commit are ancestors of main. The five v57 rows concern
`2 log phi` arithmetic and metrology witnesses. They move no RH, Ray-Pick,
Stieltjes, Hausdorff, Suzuki, or lambda-cocycle row.

Collision search found no issue, branch, probe path, notes path, registry row,
or indexed file with this identifier or `STIELTJES-WIDDER-EULER`. This lane
does not duplicate the conditional finite-window theorem of issue #469.

## Field one: equation

Use the standard completed zeta function

```text
xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s),
xi(s) = xi(1-s).
```

For real `s>1`, define the functional-equation coordinate and its derivative:

```text
u = s(s-1) > 0,
q = 2s-1 = sqrt(1+4u) > 1,
D_u = q^(-1) D_s,
calX(u) = xi(s),
f(u) = D_u log calX(u) = q^(-1) xi'(s)/xi(s).
```

Because `X(a)=xi(1/2+a)` is even entire and `a^2=u+1/4`, `calX` is expected
to be entire in `u`. Its paired zeros are

```text
z_rho = rho(rho-1),
```

one location per functional pair `{rho,1-rho}`, with multiplicity retained.
Conjugation sends `z_rho` to `conj(z_rho)`.

The exact Euler display to be proved in the absolute-convergence domain is

```text
f(u) = 1/u + (1/q) [ (1/2) psi(s/2) - (1/2) log pi
                     - sum_(n>=2) Lambda(n)n^(-s) ].
```

The first target equivalence is

```text
RH  iff  f is a Stieltjes function on (0,infinity).
```

The Stieltjes convention is

```text
f(u) = C + integral_[0,infinity) dmu(t)/(u+t),
C>=0, mu>=0, integral dmu(t)/(1+t)<infinity.
```

Under RH the target measure is

```text
mu = sum_(gamma>0) m_gamma delta_(gamma^2+1/4).
```

The second target equivalence imports the exact Widder-Sokal theorem:

```text
RH iff f(u)>=0 and
       W_k(u):=(-1)^(k-1) D_u^(2k-1)[u^k f(u)] >= 0
       for every k>=1 and every u>0.
```

In the Euler variable this is

```text
W_k(s)=(-1)^(k-1)(q^-1 D_s)^(2k-1)
       [(s(s-1))^k(q^-1 xi'(s)/xi(s))] >= 0,
s>1.
```

Primary imported source: Alan D. Sokal, *Real-variables characterization of
generalized Stieltjes functions*, arXiv:0902.0065, Theorem 1. It gives the
minimal Widder subfamily `F_(k-1,k)>=0`. No novelty is claimed for that theorem.

## Field two: code

Planned exact programs, Python standard library only, deterministic output, no
float, no external data, no zeta ordinate:

```text
break.py   independent attack written and pinned before verify.py
verify.py  exact rational and polynomial audit written only after breaker run
```

The programs may use `Fraction`, integer polynomial arithmetic, factorials,
and rational complex pairs represented as two Fractions. They may not import
mpmath, numpy, scipy, sympy, a zero table, or a network source.

Frozen command:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 notes/C-RH-STIELTJES-WIDDER-EULER-1-N/<program>
```

The written proof carries every universal statement. Finite exact scripts are
only breakers and audits.

## Field three: carrier or data

No external dataset. No actual zeta zero. No measured or rounded ordinate.

The exact finite carrier consists of:

```text
Q-pairs for synthetic rho=beta+i gamma,
z=rho(rho-1) as a Q-pair,
rational u>0,
integer rung k>=1,
exact real part of (-z)^k/(u-z)^(2k).
```

Frozen synthetic controls:

```text
ON-LINE:
  rho = 1/2 + i, so z = -5/4.

OFF-LINE-LOW:
  rho = 9/10 + i/2,
  z = -17/50 + (2/5)i,
  audit u = 1/100.
  It must preserve f-pair > 0 and W_1-pair > 0.
  The breaker must test whether W_2-pair is negative exactly.

OFF-LINE-HIGH:
  rho = 3/4 + 10i,
  z = -1603/16 + 5i.
  It is a delay control. No actual-zero interpretation is allowed.
```

For the prime-local cut formula, `ell` and `y` remain positive symbolic
variables in the written proof. The verifier may audit the algebraic branch
orientation using a formal pair representation, but it may not approximate pi
or cosine.

## Field four: systematics

### S1. Entire descent and product

Prove that the even order-one function `X(a)=xi(1/2+a)` descends to an entire
function of `a^2`, hence to `calX(u)`. Rewrite the absolutely convergent paired
Hadamard product as a genus-zero product in `u`. A nonconstant exponential
factor is forbidden unless proved unavoidable. The logarithmic derivative must
have residue exactly the positive zero multiplicity.

### S2. Pair convention

One `z_rho` belongs to the functional pair `{rho,1-rho}`. Off the critical
line, the conjugate functional pair gives `conj(z_rho)`. On the critical line
the two coincide on the negative real axis. No zero is counted twice.

### S3. Stieltjes converse

Agreement on the positive ray must be extended by the identity theorem. An
off-cut pole of the xi-side logarithmic derivative cannot be hidden by a
Stieltjes continuation. Cancellation is possible only at identical squared
pole locations; `z_rho=z_beta` must be reduced to the same functional pair or
an explicitly declared multiplicity sum.

### S4. Euler domain

The map `s>1 -> u=s(s-1)>0` is a bijection. Every differentiated von Mangoldt
series must be justified by local uniform absolute convergence on `s>1`. No
claim is made at `s=1` or `u=0`.

### S5. Widder sign and order

For the Stieltjes kernel the target identity is

```text
(-1)^(k-1) D_u^(2k-1)[u^k/(u-z)]
  = (2k-1)!(-z)^k/(u-z)^(2k).
```

The breaker must attack the factorial, derivative order, and sign at k=1,2,3.

### S6. First rung

For one conjugate pole pair `z=-A+iB`, `A>0`, the target formulas are

```text
f_pair(u)=2(u+A)/((u+A)^2+B^2),

W_1_pair(u)=
2[A(u+A)^2+B^2(2u+A)]/((u+A)^2+B^2)^2.
```

Both are strictly positive. Absolute convergence of their grouped sums must be
proved. If correct, `f>=0` and `W_1>=0` are unconditional and the first
possible Widder obstruction is k=2.

### S7. Prime-local no-go

For `ell>0`, put

```text
p_ell(u)=exp(-ell s(u))/q,
s(u)=(1+sqrt(1+4u))/2.
```

On the upper lip of the cut

```text
u = -1/4-y^2/4+i0, y>0,
q=iy, s=(1+iy)/2,
```

the target boundary density is

```text
-(1/pi) Im p_ell(u)
  = exp(-ell/2) cos(ell y/2)/(pi y).
```

Its sign changes infinitely often. The conclusion is bounded: the literal
term-by-term Euler decomposition does not provide a nonnegative per-prime
Stieltjes measure. No global prime-defined quadratic construction is excluded.

### S8. Separation from adjacent lanes

Issue #469 owns a conditional finite zero-window certificate. This lane owns
only the Euler-domain real-variable hierarchy and local source no-go. The
lambda grid is separate and strictly stronger than RH. Nothing here changes
`LAMBDA-COCYCLE-ANGLES [H]`.

## Field five: failure threshold

Local falsifiers:

```text
WF1  calX is not single-valued entire in u, or a nonconstant Hadamard
     exponential survives in f.
WF2  RH does not imply the stated Stieltjes representation, or a Stieltjes f
     is compatible with an off-critical zero.
WF3  the Widder minimal subfamily is copied with the wrong derivative order,
     sign, or required base inequality.
WF4  the Euler display or termwise differentiated display fails on s>1.
WF5  one admissible conjugate pole pair gives f_pair<=0 or W_1_pair<=0.
WF6  the single-pole factorial identity fails at any k.
WF7  the upper-lip cut orientation gives the opposite density or no sign
     change for p_ell.
WF8  the low synthetic control fails to preserve the first rung or fails to
     exhibit any higher-rung sign defect at the frozen rational point.
WF9  the result duplicates #469, claims finite sufficiency, uses a zero table,
     or silently strengthens the lambda grid.
WF10 any remote byte, pin, execution-order, stdout, stderr, or hash mismatch.
```

A mathematical WF is recorded as bounded F. An integrity WF is STOP. No
threshold moves after this preregistration is pinned.

Decision vocabulary:

```text
REDUCTION   W1-W6 survive. Candidate theorem: RH is exactly the infinite
            Euler-Widder hierarchy; f and W_1 are unconditional; literal
            per-prime Stieltjes positivity is false.
SOURCE      every Widder inequality is proved from the Euler side without a
            criterion equivalent to RH as an input.
F           one frozen mathematical statement is exactly false.
STOP        authority, convergence, pair counting, source, or integrity is
            incomplete.
```

Expected outcome is `REDUCTION`. It is not evidence for RH.

## Field six: action layer

Analytic and operator-theoretic only. No TWIST-J L1 to L6 physical lift. No
Canon, Registry, Frontier, evidence, formal probe, release, physical, decoder,
Born, SI, or J-native carrier claim.

## Fixed order

```text
1. This PREREG.md is committed and read back remotely.
2. break.py is written, committed, read back, and executed once.
3. Only then are PROOF.md and verify.py written and pinned.
4. verify.py is executed once.
5. Exact stdout, stderr, environment, bytes, hashes, and conclusions are
   recorded without changing pinned files.
6. Every fired falsifier is preserved.
7. PROMO.md is written only for a surviving theorem-grade bounded result.
```
