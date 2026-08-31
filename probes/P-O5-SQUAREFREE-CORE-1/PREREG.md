# P-O5-SQUAREFREE-CORE-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / NO FORMAL RUN YET / CANON UNCHANGED**

Date: 2026-08-27.

This probe freezes one exact analytic-number-theory reduction at the safe Euler-factor level. It removes the split prime-power tail of the public scalar channel `O_5` by an Euler product which is already a holomorphic unit on `Re(s)>1/3`.

It does not construct a continuation of `O_5`, locate a zero or pole, prove a summatory estimate, or prove or disprove RH or GRH.

## Public identity, authority, and action layer

```text
probe:             P-O5-SQUAREFREE-CORE-1
public claim lock: issue #591
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-SQUAREFREE-CORE-1
path:              probes/P-O5-SQUAREFREE-CORE-1/
basis main:        9fbda966b134090128e6f7172e8ce167abe0de8a
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, analytic number theory / Dirichlet-series algebra
layer lift:        none
authority:         none until a later sealed Canon fold
```

The public issue was opened after a collision search across current and historical issues, pull requests, branches, the Public Canon v67 tree, Registry, Frontier, dependencies, gates, evidence, and the current rapidity/O5 lanes.

The distinct in-flight issue #590, `P-O5-DEDEKIND-GRH-DIVISOR-READ-1`, owns the divisor-coordinate theorem. It is not a dependency or evidence input here. This probe may neither consume nor modify that lane.

## Proposed candidate row

At most the following row may be offered to a later sealed fold:

```text
O5-SQUAREFREE-CORE [candidate-T]

For the public scalar split-prime factor

    O_5(s) = product_(chi_5(p)=1) (1-p^(-s))^2/(1+p^(-2s))

on its registered safe half-plane Re(s)>1, define

    S_5(s) = product_(chi_5(p)=1) (1-2p^(-s))

and

    A_5(s) = product_(chi_5(p)=1)
             (1-p^(-s))^2 /
             ((1+p^(-2s))(1-2p^(-s))).

Then O_5=A_5 S_5 on Re(s)>1. Both A_5 and A_5^-1 have
absolutely convergent Dirichlet series and are holomorphic nowhere-zero
Euler-product units on Re(s)>1/3. The coefficient s_5(n) of S_5 is

    s_5(n) = mu(n) a_F(n) 1_(5 does not divide n),

where a_F=1*chi_5 is the registered ideal-count sequence of
F=Q(sqrt5). Equivalently s_5(n)=(-2)^omega(n) exactly on squarefree
integers supported on split rational primes, and zero otherwise.

If T_5(x)=sum_(n<=x)o(n) for the public O_5 coefficients and
S_5^sum(x)=sum_(n<=x)s_5(n), then for every fixed real theta>1/3,

    T_5(x)=O(x^theta)  iff  S_5^sum(x)=O(x^theta).

No continuation, divisor, zero, RH, GRH, physical, or L1-L6 claim is included.
```

No status is earned by this preregistration. The written proof below is the proposed theorem-grade evidence. The verifier is a bounded exact audit of the frozen algebra and negative controls.

## Falsifier first

One exact counterexample to any frozen universal statement below falsifies the corresponding candidate theorem:

1. the local rational-function identity `O_p(T)=A_p(T)(1-2T)` fails;
2. either `A_p(T)-1` or `A_p(T)^-1-1` has a term below degree three;
3. a split rational prime below 11 exists, or a local factor used by `A_p` or `A_p^-1` can vanish at a point with `Re(s)>1/3`;
4. the absolute local coefficient bounds below do not imply convergence for one fixed `theta>1/3`;
5. `s_5(n)=mu(n)a_F(n)1_(5 does not divide n)` fails at one positive integer;
6. one exact Dirichlet convolution `o=a*s_5` or `s_5=b*o` fails, where `a,b` are the Dirichlet coefficients of `A_5,A_5^-1`;
7. the summatory transfer uses a coefficient series which is not absolutely convergent at the same `theta>1/3`;
8. the proof imports the continuation/divisor conclusion of issue #590, a zeta-zero statement, RH/GRH, an equivalent Mertens estimate, a Hecke/automorphic object, or a selected split orientation.

A changed pinned byte, stale basis, failed startup preflight, nonzero verifier exit, nonempty stderr, stdout mismatch, architecture disagreement, post-pin threshold change, or out-of-scope claim is STOP, not a mathematical counterexample.

## The six frozen fields

```text
EQUATION
  The local O_p=A_p(1-2T) factorization, the exact cubic-onset
  formulas for A_p and A_p^-1, the Re(s)>1/3 unit theorem,
  the all-n squarefree coefficient identity, the two exact Dirichlet
  convolutions, and the all-theta>1/3 summatory power-bound equivalence.

CODE
  probes/P-O5-SQUAREFREE-CORE-1/verify.py.
  Python standard library only; exact integers; exact polynomial and
  formal-power-series arithmetic; deterministic stdout; no float,
  complex approximation, special functions, network, random input,
  zero table, or external package.

CARRIER
  F=Q(sqrt5), chi_5, the registered ideal-count sequence a_F,
  the public scalar split-prime local factor O_p(T), formal rational
  functions in T, multiplicative integer Dirichlet coefficients,
  and ordinary finite partial sums.

SYSTEMATICS
  Split means chi_5(p)=1. The two prime ideals above a split rational
  prime remain an unordered orientation pair. No orientation is selected.
  A_5 is only the prime-power dressing between O_5 and its squarefree
  split support. Issue #590's continued O_5 is not an admitted input.

THRESHOLD
  G01 through G09 must pass exactly. B1 through B5 must fire at their
  frozen first witnesses or local identity. Stdout must equal one
  committed LF EXPECTED.txt byte for byte; exit zero and empty stderr
  are required on x86_64 and aarch64.

LAYER
  NOT_APPLICABLE. Analytic number theory / Dirichlet-series algebra.
  No state, manifold, boundary, support, stream, measure, decoder,
  observable, probability, physical dictionary, SI bridge, or L1-L6 lift.
```

## 1. Frozen public inputs

Public Canon v67 registers `J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T]` at formal Euler-factor scope for `Re(s)>1`:

\[
O_5(s)
=
\prod_{\chi_5(p)=1}
\frac{(1-p^{-s})^2}{1+p^{-2s}}.
\]

The same row explicitly owns no continuation, zero location, cancellation, RH, physical, or L2-L6 statement.

Public Canon v67 also registers `J-IDEAL-COUNT-QUADRATIC-CHARACTER [T]`:

\[
a_F=1*\chi_5
\]

for `F=Q(sqrt5)`, where `a_F(n)` is the number of nonzero integral ideals of norm `n`.

No statement from issue #590 is used.

## 2. Local squarefree factor and exact cubic onset

At a split rational prime write `T=p^{-s}` and set

\[
O_p(T)=\frac{(1-T)^2}{1+T^2},
\qquad
S_p(T)=1-2T,
\]

\[
A_p(T)
=
\frac{(1-T)^2}{(1+T^2)(1-2T)}.
\]

Then directly

\[
\boxed{O_p(T)=A_p(T)S_p(T)}.
\]

The load-bearing point is not merely this definition but the exact order of the residual dressing. Since

\[
(1+T^2)(1-2T)
=
1-2T+T^2-2T^3,
\]

one has

\[
\boxed{
A_p(T)-1
=
\frac{2T^3}{(1+T^2)(1-2T)}.
}
\]

Also

\[
A_p(T)^{-1}
=
\frac{(1+T^2)(1-2T)}{(1-T)^2},
\]

so

\[
\boxed{
A_p(T)^{-1}-1
=
-\frac{2T^3}{(1-T)^2}.
}
\]

Both residuals begin exactly at degree three. Therefore the linear split coefficient `-2T` and the vanishing quadratic coefficient already belong entirely to the squarefree core.

## 3. The dressing is a unit on Re(s)>1/3

The rational primes below 11 are `2,3,5,7`. Their `chi_5` values are respectively `-1,-1,0,-1`; `11` is the first split prime.

Fix a compact set in `Re(s)>=sigma_0>1/3`. For every split prime `p`, put

\[
r_p=p^{-\sigma_0}.
\]

Since `p>=11`,

\[
r_p<11^{-1/3}<\frac9{20}<\frac12.
\]

The middle exact inequality is certified by

\[
11\cdot9^3=8019>8000=20^3.
\]

Hence on the compact set, with `T=p^{-s}`,

\[
|T|\le r_p<9/20.
\]

All local factors are nonzero there:

- `1-T != 0` because `|T|<1`;
- `1+T^2 != 0` because `|T^2|<1`;
- `1-2T != 0` because `|2T|<9/10`.

From the exact cubic formulas,

\[
|A_p(T)-1|
\le
\frac{2r_p^3}{(1-r_p^2)(1-2r_p)}
<
26r_p^3,
\]

because at `r=9/20` the reciprocal constant is `8000/319<26`.

Likewise,

\[
|A_p(T)^{-1}-1|
\le
\frac{2r_p^3}{(1-r_p)^2}
<
7r_p^3,
\]

because `800/121<7`.

Since `3 sigma_0>1`,

\[
\sum_{\chi_5(p)=1}p^{-3\sigma_0}
\le
\sum_{n\ge2}n^{-3\sigma_0}
<\infty.
\]

Therefore the sums of the local deviations for both `A_p` and `A_p^-1` converge uniformly on compact subsets of `Re(s)>1/3`. Their Euler products converge locally normally. The partial products are holomorphic, and the simultaneously convergent inverse products show that the limits are mutual inverses. Thus

\[
\boxed{
A_5,\ A_5^{-1}
\text{ are holomorphic and nowhere zero on }\Re(s)>1/3.
}
\]

No continuation of `O_5` is used in this proof.

### Absolute Dirichlet coefficients

For a real `theta>1/3`, put `r=p^{-theta}`. The same formulas majorize the sum of the absolute values of the nonconstant local power-series coefficients by

\[
26p^{-3\theta}
\quad\text{for }A_p,
\qquad
7p^{-3\theta}
\quad\text{for }A_p^{-1}.
\]

The products of `1` plus these summable local majorants converge. Therefore if

\[
A_5(s)=\sum_{n\ge1}a(n)n^{-s},
\qquad
A_5(s)^{-1}=\sum_{n\ge1}b(n)n^{-s},
\]

then for every `theta>1/3`,

\[
\boxed{
\sum_{n\ge1}|a(n)|n^{-\theta}<\infty,
\qquad
\sum_{n\ge1}|b(n)|n^{-\theta}<\infty.
}
\]

These are exactly the coefficient bounds used in the summatory transfer. No weaker abscissa claim is substituted.

## 4. Exact squarefree coefficients

Define

\[
S_5(s)
=
\prod_{\chi_5(p)=1}(1-2p^{-s})
=
\sum_{n\ge1}s_5(n)n^{-s}
\]

on `Re(s)>1`.

By Euler multiplication,

\[
s_5(n)=
\begin{cases}
(-2)^{\omega(n)},&
n\text{ squarefree and every }p\mid n\text{ is split},\\
0,&\text{otherwise}.
\end{cases}
\]

Now use the registered identity `a_F=1*chi_5`. Its prime-power values are

\[
a_F(p^e)
=
\begin{cases}
e+1,&p\text{ split},\\
1,&p\text{ inert and }e\text{ even},\\
0,&p\text{ inert and }e\text{ odd},\\
1,&p=5.
\end{cases}
\]

The ordinary Mobius function kills every exponent `e>=2`. On squarefree input:

- split `p`: `mu(p)a_F(p)=-2`;
- inert `p`: `mu(p)a_F(p)=0`;
- ramified `p=5`: `mu(5)a_F(5)=-1`.

Removing the ramified prime therefore gives, for every positive integer,

\[
\boxed{
s_5(n)
=
\mu(n)a_F(n)\mathbf 1_{(n,5)=1}.
}
\]

This is a coefficient theorem, not a summatory estimate.

For squarefree split `n` with `a=omega(n)`, `a_F(n)=2^a` is also the cardinality of the product of the `a` unordered two-point prime-ideal orientation pairs. The sign `mu(n)=(-1)^a` is ordinary squarefree prime-count parity. It is not claimed to be the sign of global conjugation acting as a permutation of the full `2^a` orientation fiber.

## 5. Exact convolution and summatory transfer

On `Re(s)>1`, all products are absolutely convergent and

\[
O_5=A_5S_5.
\]

Therefore their Dirichlet coefficients satisfy

\[
\boxed{o=a*s_5}.
\]

Because `A_5^-1` is also an absolutely convergent Dirichlet series there,

\[
\boxed{s_5=b*o}.
\]

Now fix any real `theta>1/3`.

Suppose

\[
S_5^{\rm sum}(x)
:=
\sum_{n\le x}s_5(n)
=
O(x^\theta).
\]

Then using `o=a*s_5`,

\[
T_5(x)
=
\sum_{d\le x}a(d)
S_5^{\rm sum}(x/d).
\]

Hence

\[
|T_5(x)|
\le
C x^\theta
\sum_{d\le x}|a(d)|d^{-\theta}
\le
C' x^\theta
\]

by the absolute coefficient convergence proved in section 3.

Conversely, if `T_5(x)=O(x^theta)`, use `s_5=b*o` and the same argument with `b`.

Thus for every fixed real `theta>1/3`,

\[
\boxed{
T_5(x)=O(x^\theta)
\iff
S_5^{\rm sum}(x)=O(x^\theta).
}
\]

This is stronger than a single critical-exponent restatement: every power bound to the right of `1/3` transfers in both directions.

## 6. Negative controls

The same local and coefficient constructors used by the positive gates must carry five mutations.

### B1. Wrong linear core

Replace `1-2T` by `1-T`. The attempted dressing is

\[
\frac{O_p(T)}{1-T}
=
\frac{1-T}{1+T^2}
=
1-T+O(T^2).
\]

The dressing now has a degree-one defect. At the first split prime this is the witness `p=11`, hence global witness `n=11`.

### B2. Wrong squared core

Replace `1-2T` by `(1-T)^2`. The attempted dressing is

\[
\frac1{1+T^2}=1-T^2+O(T^4).
\]

The first defect is degree two, with global witness `11^2=121`.

### B3. Omit ramified cutoff

Replace `mu(n)a_F(n)1_(5 does not divide n)` by `mu(n)a_F(n)`. The first disagreement with `s_5` is `n=5`.

### B4. Treat inert two as split

Mutate the support predicate by admitting `p=2`. The first disagreement is `n=2`.

### B5. Delete the `(1+T^2)` denominator

Use

\[
A_p^{\rm mut}(T)=\frac{(1-T)^2}{1-2T}.
\]

Then `A_p^{mut}(1-2T)=(1-T)^2`, which is not the public local factor `(1-T)^2/(1+T^2)`. The exact rational-function identity must fail.

No mutation changes a threshold after the pin.

## 7. Frozen verifier gates

```text
G01  exact local rational-function factorization
G02  exact cubic onset for A_p and A_p^-1
G03  first split prime and exact 9/20 half-plane guard
G04  all-n coefficient formula audited through N=50000
G05  local formal-series identities through degree 16
G06  exact rational majorant constants 26 and 7
G07  both global Dirichlet convolutions audited through N=20000
G08  source firewall: stdlib only, no float/complex/eval/exec/network/random
G09  B1-B5 all fire at witnesses 11,121,5,2 and the local identity
```

The finite ranges audit the written universal proof. They are not the theorem scope and cannot replace it.

## 8. Clean interpreter-startup control

The abandoned predecessor `P-O5-DEDEKIND-GRH-READ-1` produced no accepted run because its local interpreter injected stderr before verifier startup. This probe freezes the technical preflight before its own pin:

```text
PATH:             /usr/bin:/bin
resolved python:  /usr/bin/python3
preflight:
  env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
    /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
required:
  exit 0
  stdout exactly: PYTHON_STARTUP_CLEAN plus LF
  stderr: empty
```

The preflight is an integrity/environment check, not a scientific gate. After the public pin it must pass immediately before the single accepted local verifier execution. If it fails, this probe is STOP and no scientific output is accepted.

The scientific command is:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-SQUAREFREE-CORE-1/verify.py
```

## 9. Explicit nonclaims

This probe does not:

- construct or consume a meromorphic continuation of `O_5`;
- consume issue #590's divisor theorem;
- locate a zero or pole;
- state or prove RH or GRH;
- derive any `O(x^(1/2+eps))` estimate;
- identify `S_5` with a Hecke or automorphic character;
- select one split prime ideal;
- identify Mobius parity with the permutation sign on the full orientation fiber;
- create a probability, Haar, physical, SI, decoder, or L1-L6 statement;
- change Canon, Registry, Frontier, dependency, evidence, gate, workflow, Note, reproduction, or an existing probe.

A later analytic use may combine independently earned results only through a separately reviewed fold. This probe itself stops at the squarefree-core reduction.
