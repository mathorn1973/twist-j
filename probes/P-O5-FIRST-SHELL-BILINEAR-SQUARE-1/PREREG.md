# P-O5-FIRST-SHELL-BILINEAR-SQUARE-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED**

Date: 2026-08-27.

## Public identity

```text
probe:             P-O5-FIRST-SHELL-BILINEAR-SQUARE-1
public claim lock: issue #608
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-FIRST-SHELL-BILINEAR-SQUARE-1
path:              probes/P-O5-FIRST-SHELL-BILINEAR-SQUARE-1/
basis main:        ed15b8e526cece98a407c7587d61f2e084267f86
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, exact multiplicative combinatorics / bilinear summatory algebra
layer lift:        none
authority:         none until a later sealed Canon fold
```

The tag `canon-v67` targets activation commit
`7dd25c7c21202c560d8a31774971c7c6200fca76`; the activation and content commits
are ancestors of the declared basis.

The structural formulas were visible in non-formal exact reasoning before the
claim lock and were disclosed in issue #608. They carry no scientific evidence
credit. This written proof and the post-pin exact audit are the candidate
evidence.

## Collision and ownership boundary

The collision scan covered current and historical issues, pull requests,
remote branches, the v67 tree, Registry, Frontier, evidence, gates, current O5
probes and current Notes.

- merged `P-O5-FIRST-SHELL-DILATION-TRANSFER-1` owns the exact reduction of the
  squarefree carrier to the annular first shell `W_11` for all power exponents
  above `log_11(2)`, in particular throughout `theta>1/3`.
- merged `P-O5-FIRST-MISSING-SHELL-1` owns the first-missing-prime terminal
  shell identity.
- merged `P-O5-SQUAREFREE-CORE-1` owns the prime-power dressing removal to the
  squarefree split carrier.
- merged `P-O5-WALSH-LINK-HOMOLOGY-1` and
  `P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1` remain separate topology lanes.
- merged `P-O5-DEDEKIND-GRH-DIVISOR-READ-1` is not an evidence input.
- draft Notes PR #595 is a separate NON-CANONICAL growing-mode lane.
- `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` remains untouched.

No existing object owns `P-O5-FIRST-SHELL-BILINEAR-SQUARE-1` or
`O5-FIRST-SHELL-BILINEAR-SQUARE`.

## Proposed candidate row

At most one row may be offered to a later sealed fold.

```text
O5-FIRST-SHELL-BILINEAR-SQUARE [candidate-T]
```

Let `P_>` be the rational primes `p>11` with `chi_5(p)=1`. Define

```text
nu(n)=mu(n)
```

when `n` is squarefree and every prime divisor belongs to `P_>`, and put
`nu(n)=0` otherwise. Thus on `Re(s)>1`,

```text
M_>(s)=sum_(n>=1)nu(n)n^-s
      =product_(p in P_>)(1-p^-s).
```

Define

```text
b(n)=(-2)^omega(n)
```

on the same squarefree support and zero otherwise. Its summatory function is
`B_11(N)`. The merged first-shell carrier is

```text
W_11(N)=B_11(N)-B_11(floor(N/11)).
```

Define the ordinary Dirichlet convolution square

```text
c=nu*nu,
C(N)=sum_(n<=N)c(n)=sum_(ab<=N)nu(a)nu(b),
Q_11(N)=C(N)-C(floor(N/11))
       =sum_(N/11<ab<=N)nu(a)nu(b).
```

No orientation is selected.

## Frozen theorem package

### A. Exact coprime bilinearization

For every integer `n>=1`,

```text
b(n)=sum_(ab=n,(a,b)=1)nu(a)nu(b).
```

Therefore

```text
B_11(N)=sum_(ab<=N,(a,b)=1)nu(a)nu(b),

W_11(N)=sum_(N/11<ab<=N,(a,b)=1)nu(a)nu(b).
```

### B. Ordinary convolution square and overlap dressing

On `Re(s)>1`,

```text
C_>(s)=M_>(s)^2
      =product_(p in P_>)(1-2p^-s+p^-2s).
```

Put

```text
R_>(s)=B_11(s)/C_>(s)
      =product_(p in P_>)R_p(p^-s),

R_p(T)=(1-2T)/(1-T)^2.
```

Then

```text
R_p(T)-1     = -T^2/(1-T)^2,
R_p(T)^-1-1  =  T^2/(1-2T).
```

Both deviations begin exactly at degree two.

Let `theta>1/2` be real and write `rho=p^-theta`. Since `p>=19`,

```text
rho < 1/sqrt(19) < 1/4,
2rho < 1/2.
```

The absolute local coefficient masses are

```text
sum_abs(R_p-1)=rho^2/(1-rho)^2,
sum_abs(R_p^-1-1)=rho^2/(1-2rho).
```

They are bounded by constant multiples of `p^(-2theta)`. Because
`2theta>1`, their sum over `P_>` is bounded by the convergent integer p-series.
Hence `R_>` and `R_>^-1` have absolutely convergent Dirichlet coefficient
series at every real `theta>1/2`. Their Euler products converge locally
normally and are holomorphic and nowhere zero on `Re(s)>1/2`.

### C. Direct annular transfer

Write

```text
R_>(s)=sum_(d>=1)r(d)d^-s,
R_>(s)^-1=sum_(d>=1)q(d)d^-s.
```

Then coefficient convolution gives

```text
b=r*c,
c=q*b.
```

The annular summatory operator commutes with these convolutions because for all
positive integers `N,d`,

```text
floor(floor(N/d)/11)
 = floor(N/(11d))
 = floor(floor(N/11)/d).
```

Therefore for every `N>=0`,

```text
W_11(N)=sum_(d<=N)r(d)Q_11(floor(N/d)),
Q_11(N)=sum_(d<=N)q(d)W_11(floor(N/d)).
```

If one annular carrier is `O(N^theta)`, convolution with the absolutely
summable coefficient sequence of the appropriate dressing transfers the same
power to the other. Hence, for every fixed real `theta>1/2`,

```text
W_11(N)=O(N^theta)
iff
Q_11(N)=O(N^theta).
```

In particular,

```text
for every epsilon>0,
W_11(N)=O_epsilon(N^(1/2+epsilon))
iff
Q_11(N)=O_epsilon(N^(1/2+epsilon)).
```

This is a transfer theorem, not a bound.

### D. Exact hyperbola form

Let

```text
U(X)=sum_(n<=X)nu(n),
H(X)=sum_(ab<=X)nu(a)nu(b).
```

For `R=floor(sqrt(X))`, the region `ab<=X` is the union of its `a<=R`
and `b<=R` halves, while the square `a,b<=R` is counted twice. Therefore

```text
H(X)=2 sum_(a<=R)nu(a)U(floor(X/a))-U(R)^2.
```

The ordinary bilinear annulus is

```text
Q_11(N)=H(N)-H(floor(N/11)).
```

Equivalently,

```text
Q_11(N)=sum_(a>=1)nu(a)
  [U(floor(N/a))-U(floor(N/(11a)))],
```

with only finitely many nonzero terms.

### E. Support-preserving color no-go

Fix one squarefree `P_>`-support `S`. Every ordered partition

```text
S=A disjoint-union B
```

has

```text
nu(product A)nu(product B)
 = (-1)^|A|(-1)^|B|
 = (-1)^|S|.
```

Thus all `2^|S|` colorings have the same bilinear sign. Every permutation or
involution which only redistributes primes between the two colors while
preserving their union support is sign-preserving. The bilinearization itself
therefore cannot generate cancellation inside one fixed `n`.

Any successful bilinear cancellation mechanism must couple different products
or supports, or introduce a genuinely nontrivial signed kernel whose
reconstruction is separately controlled.

## Falsifier first

One exact defect falsifies the corresponding frozen statement:

1. the coprime bilinear coefficient differs from `b(n)` for one integer;
2. one local ordinary-square or dressing identity fails;
3. either dressing has a nonzero degree-one deviation;
4. an absolute coefficient product fails at one frozen `theta>1/2`, a local
   denominator can vanish in the claimed half-plane, or the majorant is wrong;
5. one annular convolution transfer identity fails;
6. one hyperbola identity fails;
7. one support-preserving redistribution changes the bilinear sign;
8. the construction admits inert or ramified support, selects an orientation,
   imports RH/GRH or a target cancellation estimate, or widens beyond the
   frozen route.

A stale basis, changed pin, failed startup preflight, nonzero verifier exit,
nonempty stderr, stdout mismatch, architecture disagreement, moved threshold
or scope widening is STOP, not a mathematical counterexample.

## The six frozen fields

```text
EQUATION
  Statements A-E exactly as displayed.

CODE
  probes/P-O5-FIRST-SHELL-BILINEAR-SQUARE-1/verify.py.
  Python standard library only; exact integers and Fraction arithmetic;
  deterministic factorization, divisor sums, finite formal power series and
  exact hyperbola sums; no float, complex approximation, network, random,
  zero table, special function or external package.

CARRIER
  chi_5 split rational primes strictly greater than 11, restricted Möbius
  sequence nu, squarefree weight b, ordinary convolution square c, annular
  sums W_11 and Q_11, and the overlap dressing R_>.

SYSTEMATICS
  The tail begins at split prime 19 and excludes 11 exactly. Inert and
  ramified primes are absent. The two prime-ideal orientations remain an
  unordered pair. No orientation is selected.

THRESHOLD
  G01 through G08 pass exactly. B1 through B5 fire at their frozen witnesses.
  One LF EXPECTED.txt, exit zero, empty stderr and byte identity are required.

LAYER
  NOT_APPLICABLE. Exact arithmetic and bilinear summatory algebra only. No
  state, manifold, boundary/support lift, stream, measure, decoder,
  observable, physical dictionary or SI statement.
```

## Frozen negative controls

```text
B1  drop the coprimality restriction in A while still claiming exact b(n).
    First coefficient failure: n=19^2=361.

B2  replace R_p(T) by 1.
    First ordinary-square/coprime defect: degree two.

B3  use the wrong inverse deviation T/(1-2T).
    The forbidden degree-one coefficient fires.

B4  treat 11 as part of P_>.
    First tail-support mismatch: n=11.

B5  claim that moving a prime between the two colors reverses the product sign.
    Witness support S={19}: both partitions have sign -1.
```

## Frozen verifier gates

```text
G01  exact nu, b, c, r and q coefficient census through n=30000.
G02  coprime bilinear coefficient identity and B1 witness 361.
G03  local ordinary-square and dressing series through degree 18.
G04  exact local-majorant algebra and half-plane denominator guards.
G05  direct annular transfer identities through N=10000.
G06  ordinary bilinear annulus and exact hyperbola identities on frozen N.
G07  support-preserving sign no-go and B2-B5.
G08  LF-only exact-integer/Fraction standard-library source firewall.
```

The finite gates audit the universal written proof and do not define its scope.

## Formal execution discipline

Before pin, `verify.py` may only be read and AST-parsed. The first pushed probe
commit contains only this `PREREG.md` and `verify.py`. After exact public
readback, run

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

and require exit zero, exactly `PYTHON_STARTUP_CLEAN` plus LF, and empty
stderr. Only then may the single scientific command run:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-FIRST-SHELL-BILINEAR-SQUARE-1/verify.py
```

The accepted stdout becomes `EXPECTED.txt`. `RUN.md` and `RESULT.md` are
post-pin records only.

## Explicit nonclaims

No RH or GRH result, new summatory estimate, zero-free region, meromorphic
continuation of the square-root carrier, Hecke or automorphic object, selected
split orientation, physical interpretation, probability statement, SI
statement or L1-L6 lift is claimed. The theorem does not claim that `Q_11` is
small. It replaces the first-shell target by an equivalent ordinary bilinear
annulus at every exponent strictly above `1/2`, and records the exact no-go for
cancellation that only recolors a fixed support.
