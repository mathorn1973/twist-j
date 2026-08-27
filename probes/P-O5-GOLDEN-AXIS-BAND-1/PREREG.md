# P-O5-GOLDEN-AXIS-BAND-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED**

Date: 2026-08-27.

## Public identity

```text
probe:             P-O5-GOLDEN-AXIS-BAND-1
public claim lock: issue #610
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-GOLDEN-AXIS-BAND-1
path:              probes/P-O5-GOLDEN-AXIS-BAND-1/
basis main:        c5d618f57099471bd9871c7918c3ba4da90f1a04
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, exact Lucas arithmetic / bilinear shell geometry
layer lift:        none
authority:         none until a later sealed Canon fold
```

The structural formulas were exposed in exact non-formal reasoning before the
claim lock. After issue #610 was opened, development-only computation found
the exact breaker witnesses and caught the omitted unit shell in the first
issue draft. The issue was corrected before this pin. That development run is
not evidence. The theorem, carrier, thresholds and witnesses below are the
frozen formal contract.

## Collision and ownership boundary

The collision scan covered current and historical issues, pull requests,
remote branches, the v67 tree, Registry, Frontier, evidence, gates, current O5
probes and current Notes.

- merged `P-O5-FIRST-SHELL-BILINEAR-SQUARE-1` (#609) owns the ordinary
  bilinear annulus `Q_11(N)` and its hyperbola form;
- merged `P-O5-FIRST-SHELL-DILATION-TRANSFER-1` owns the first-shell/full
  squarefree-carrier transfer;
- draft PR #595, `C-RAPIDITY-GOLDEN-LADDER-1`, is NON-CANONICAL and studies
  the diagonal **evaluation** ladder `tau=L_(2k)`. It does not own the
  cutoff-axis theorem here. This probe re-derives all Lucas facts it uses and
  consumes no evidence from #595;
- merged `P-O5-FIRST-MISSING-SHELL-1`,
  `P-O5-SQUAREFREE-CORE-1`, and
  `P-O5-DEDEKIND-GRH-DIVISOR-READ-1` remain separate candidate-grade lanes;
- `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` is untouched.

No existing object owns `P-O5-GOLDEN-AXIS-BAND-1` or
`O5-GOLDEN-AXIS-BAND`.

## Proposed candidate row

At most one row may be offered to a later sealed fold.

```text
O5-GOLDEN-AXIS-BAND [candidate-T]
```

Put

```text
alpha = phi^2 = (3+sqrt(5))/2,
A_k   = L_(2k),
X_k   = A_k-1.
```

For `k>=0`, the theorem proves `X_k=floor(alpha^k)`.

Define the complete integer golden-shell partition

```text
I_-1 = {1},

I_k = {n in Z_(>=1): X_k<n<=X_(k+1)}
    = {L_(2k),...,L_(2k+2)-1},           k>=0.
```

Equivalently, for every `k>=-1`,

```text
I_k = {n in Z_(>=1): alpha^k<n<=alpha^(k+1)}.
```

Let `nu(n)=mu(n)` on squarefree integers supported only on rational split
primes strictly greater than `11`, and let `nu(n)=0` otherwise. This is exactly
the restricted sequence used by merged probe
`P-O5-FIRST-SHELL-BILINEAR-SQUARE-1`.

Define

```text
u_k = sum_(n in I_k) nu(n),

P_s(Y)
  = sum_(i+j=s)
      sum_(a in I_i,b in I_j,ab<=Y) nu(a)nu(b),

D_s = sum_(i+j=s) u_i u_j.
```

Indices start at `-1`, so anti-diagonals start at `s=-2`.

The ordinary convolution-square hyperbola carrier is

```text
H(Y)=sum_(s>=-2) P_s(Y),
Q_11(N)=H(N)-H(floor(N/11)).
```

## Frozen theorem package

### A. Lucas cutoff is the exact unit-scale floor

For every `k>=0`,

```text
floor(alpha^k)=L_(2k)-1=X_k.
```

For `k>=1`,

```text
alpha^k=(L_(2k)+F_(2k)sqrt(5))/2
```

and the even-index Pell identity is

```text
L_(2k)^2-5F_(2k)^2=4.
```

The upper inequality `alpha^k<L_(2k)` is equivalent to

```text
5F_(2k)^2 < L_(2k)^2,
```

which follows from the Pell difference `4`.

The lower inequality `L_(2k)-1<alpha^k` is equivalent to

```text
F_(2k)sqrt(5) > L_(2k)-2.
```

Both sides are nonnegative for `k>=1`; after squaring, the required inequality
is

```text
5F_(2k)^2 > (L_(2k)-2)^2.
```

Using the Pell identity, this is

```text
L_(2k)^2-4 > L_(2k)^2-4L_(2k)+4,
```

equivalent to `L_(2k)>2`, true for `k>=1`. The case `k=0` is direct.

Therefore the integer boundaries of the multiplicative `phi^2` unit scale are
exactly the shifted even Lucas values.

This is an independent proof. The fact that draft #595 uses the same even
Lucas sequence as an evaluation ladder supplies no evidence here.

### B. Product shells localize multiplication

For `a in I_i`, `b in I_j`, with `i,j>=-1`,

```text
alpha^i<a<=alpha^(i+1),
alpha^j<b<=alpha^(j+1).
```

Multiplication gives

```text
alpha^(i+j)<ab<=alpha^(i+j+2).
```

Hence, if `N in I_m`,

```text
P_s(N)=D_s    for s<=m-2,
P_s(N)=0      for s>=m+1.
```

Indeed, for `s<=m-2` every product is at most `alpha^m<N`, while for
`s>=m+1` every product is greater than `alpha^(m+1)>=N`.

Only `s=m-1,m` may be partial.

### C. Eleven lies between two and three golden steps

The exact identities

```text
alpha^2=(7+3sqrt(5))/2,
alpha^3=9+4sqrt(5)
```

give

```text
alpha^2<11<alpha^3.
```

The first inequality is `3sqrt(5)<15`, whose square comparison is
`45<225`. The second is `4sqrt(5)>2`, whose square comparison is `80>4`.

If `N in I_m`, then `alpha^m<N<alpha^(m+1)`, so

```text
alpha^(m-3) < N/11 < alpha^(m-1).
```

This is the fixed arithmetic reason the ratio-11 annulus has bounded golden
width.

### D. Full-axis five-diagonal band theorem

Let `m>=3`, let `N in I_m`, and put

```text
M=floor(N/11).
```

For every `s<=m-5` and every factor pair from anti-diagonal `s`,

```text
ab<=alpha^(s+2)<=alpha^(m-3)<N/11.
```

Because `ab` is an integer, `ab<=M`. Therefore

```text
P_s(N)=P_s(M)    for s<=m-5.
```

For every `s>=m+1`,

```text
ab>alpha^s>=alpha^(m+1)>N,
```

so

```text
P_s(N)=P_s(M)=0.
```

Consequently,

```text
Q_11(N)
  = sum_(s=max(-2,m-4))^m
      [P_s(N)-P_s(M)].
```

For every `m>=4` this is exactly the width-five band

```text
s=m-4,m-3,m-2,m-1,m.
```

For `m=3` the same formula starts at `s=-1`; the unit-unit diagonal `s=-2`
has already cancelled.

Thus the linear-coordinate hyperbola annulus becomes a uniformly finite-range
bilinear operator on the golden shell index.

### E. Lucas-top four-diagonal refinement

Let

```text
N=X_K=L_(2K)-1=floor(alpha^K),   K>=4,
M=floor(N/11).
```

First, `M in I_(K-3)`.

The upper bound follows from

```text
N/11 < alpha^K/11 < alpha^(K-2)
```

because `alpha^2<11`.

For the lower bound, `M>X_(K-3)` is equivalent to

```text
N >= 11(X_(K-3)+1)=11L_(2K-6).
```

For `K=4,5` this is checked directly. For `K>=6`, the Lucas product identity

```text
L_6 L_(2K-6)=L_(2K)+L_(2K-12),
L_6=18,
```

gives

```text
L_(2K)=18L_(2K-6)-L_(2K-12)
      >=17L_(2K-6),
```

because the positive even Lucas sequence is increasing. Hence

```text
N=L_(2K)-1 >= 11L_(2K-6).
```

Now the top cutoff `N=floor(alpha^K)` fills every anti-diagonal through
`K-2`, kills every anti-diagonal from `K` upward, and leaves only `K-1`
partial:

```text
P_s(N)=D_s   for s<=K-2,
P_s(N)=0     for s>=K.
```

Since `M in I_(K-3)`, its only partial diagonals are `K-4,K-3`.

Therefore the exact normal form is

```text
Q_11(X_K)
 = [D_(K-4)-P_(K-4)(M)]
   +[D_(K-3)-P_(K-3)(M)]
   + D_(K-2)
   + P_(K-1)(X_K).
```

The Lucas-top annulus occupies only four adjacent anti-diagonals and three
boundary forms.

### F. Exact boundary

The theorem supplies localization only.

It does not show that the five full-axis forms, the four top-cutoff forms, or
any individual boundary form is small. Applying only the triangle inequality
to the surviving band gives no square-root estimate.

Any actual successor must supply a signed kernel, spectral estimate, recurrence
or another cancellation mechanism **inside the finite golden band**.

## Why this tests the alternate-axis idea

The ordinary summatory coordinate is `1,2,3,...`. This probe does not alter
integer addition and does not claim that the physical number line is
Lucas-ordered.

It asks one exact question about the current multiplicative carrier:

```text
does the hyperbola become more local when indexed by the canonical
multiplicative unit scale phi^(2k)?
```

The theorem answer is yes: the exact integer boundaries are
`L_(2k)-1`, and the ratio-11 annulus has uniformly finite interaction range in
that index.

## Falsifier first

One exact defect falsifies the corresponding frozen statement:

1. the Lucas-floor identity fails;
2. the complete shell partition including `I_-1={1}` misses or duplicates one
   positive integer;
3. one product-shell bound fails;
4. `alpha^2<11<alpha^3` fails;
5. one anti-diagonal outside the width-five band changes between `N` and
   `floor(N/11)`;
6. the Lucas-top four-diagonal normal form fails;
7. the construction claims a cancellation estimate, imports RH/GRH, selects
   an orientation, or conflates this cutoff axis with the evaluation ladder
   of draft #595.

A stale basis, changed pin, failed startup preflight, nonzero verifier exit,
nonempty stderr, stdout mismatch, architecture disagreement, moved threshold
or scope widening is STOP, not a mathematical counterexample.

## The six frozen fields

```text
EQUATION
  Statements A-F exactly as displayed.

CODE
  probes/P-O5-GOLDEN-AXIS-BAND-1/verify.py.
  Python standard library only; exact integer arithmetic; no float, complex,
  network, random, external data, special function or external package.

CARRIER
  even Lucas/Fibonacci recurrences, the exact golden shell partition,
  restricted Mobius sequence nu, ordinary convolution-square coefficients,
  shell-pair anti-diagonals P_s, hyperbola H and annulus Q_11.

SYSTEMATICS
  I_-1={1} is part of the carrier. The tail prime support is exactly the
  split rational primes strictly greater than 11. Draft #595 is adjacent but
  is not an evidence input. No orientation is selected.

THRESHOLD
  G01 through G08 pass exactly. B1 through B5 fire at their frozen witnesses.
  One LF EXPECTED.txt, exit zero, empty stderr and byte identity are required.

LAYER
  NOT_APPLICABLE. Exact arithmetic and bilinear shell geometry only. No state,
  manifold, cross-layer lift, stream, measure, decoder, observable, physical
  dictionary or SI statement.
```

## Frozen negative controls

```text
B1  use X_k=L_(2k) instead of L_(2k)-1.
    Witness k=1: floor(alpha)=2, L_2=3.

B2  assert the false upper inequality 11<alpha^2.
    Exact square comparison instead proves alpha^2<11.

B3  drop the lower outer anti-diagonal m-4.
    First witness N=322, m=6:
    P_2(322)-P_2(29)=-4.

B4  drop the upper outer anti-diagonal m.
    First witness N=361, m=6:
    P_6(361)-P_6(32)=+1.

B5  replace the two-step product-shell range by one exact target shell.
    Both 19 and 41 lie in I_3, but
    19^2=361 lies in I_6 while 41^2=1681 lies in I_7.
```

All five witnesses were obtained only in disclosed non-formal development
after issue #610 and are frozen here before the public pin.

## Frozen verifier gates

```text
G01  even Lucas/Fibonacci recurrence, Pell identity and exact floor theorem
     through k=19.

G02  complete unit-plus-Lucas shell partition through 20000 and product-shell
     bounds on every divisor factorization through 20000.

G03  exact alpha^2<11<alpha^3 integer comparisons and shell-endpoint guards.

G04  H=sum_s P_s and the full-axis five-diagonal theorem for every N through
     10000.

G05  Lucas-top four-diagonal formula for every K>=4 with X_K<=20000.

G06  coefficientwise agreement with the independently constructed ordinary
     convolution-square carrier through 20000.

G07  B1-B5 at k=1, alpha^2, N=322, N=361 and the 19/41 shell witnesses.

G08  LF-only exact-integer standard-library source firewall.
```

Finite gates audit the universal written proof and do not define its scope.

## Development disclosure

After public issue #610 but before this pin, a development copy of the
verifier was executed once to find the exact B3/B4 first witnesses and to
audit implementation. It returned `8/8`, but the ordinary host injected its
known spreadsheet-runtime warmup on startup stderr. That run is non-formal,
is not committed, and carries no evidence credit.

The accepted formal invocation occurs only after this two-file pin and public
readback, and only after the frozen clean `/usr/bin/python3` startup preflight
passes.

## Formal execution discipline

The first pushed probe commit contains only this `PREREG.md` and `verify.py`.
After exact public readback run

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

and require exit zero, exactly `PYTHON_STARTUP_CLEAN` plus LF, and empty
stderr.

Only then may the single accepted scientific command run:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-GOLDEN-AXIS-BAND-1/verify.py
```

The accepted stdout becomes `EXPECTED.txt`. `RUN.md` and `RESULT.md` are
post-pin records only.

## Explicit nonclaims

No RH or GRH result, new summatory estimate, zero-free region, analytic
continuation, Hecke or automorphic object, selected split orientation,
physical interpretation, probability statement, SI statement or L1-L6 lift
is claimed.

The probe does not claim that arithmetic addition is replaced by Lucas
addition or that Nature uses a different number line. It proves only the exact
finite-band localization of the present bilinear carrier on the canonical
`phi^2`/Lucas cutoff scale.
