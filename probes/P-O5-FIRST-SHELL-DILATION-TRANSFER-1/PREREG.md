# P-O5-FIRST-SHELL-DILATION-TRANSFER-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED**

Date: 2026-08-27.

## Public identity

```text
probe:             P-O5-FIRST-SHELL-DILATION-TRANSFER-1
public claim lock: issue #606
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-O5-FIRST-SHELL-DILATION-TRANSFER-1
path:              probes/P-O5-FIRST-SHELL-DILATION-TRANSFER-1/
basis main:        0612f5edec662eedb428e8a0d6bd77437f9579ac
canon:             Public Canon v67, tag canon-v67
CONTENT_COMMIT:    f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:      b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:       351502
action layer:      NOT_APPLICABLE, exact multiplicative combinatorics / summatory dilation algebra
layer lift:        none
authority:         none until a later sealed Canon fold
```

The tag targets activation commit
`7dd25c7c21202c560d8a31774971c7c6200fca76`. The activation and content
commits are ancestors of the declared basis.

The formulas below were exposed in non-formal exact reconnaissance before the
claim lock and disclosed in issue #606. That reconnaissance carries no
scientific evidence credit. This written proof and the post-pin exact audit are
the candidate evidence.

## Collision and ownership boundary

The collision scan covered current and historical issues, pull requests,
remote branches, the v67 tree, Registry, Frontier, evidence, gates, current O5
probes and current Notes.

- merged `P-O5-FIRST-MISSING-SHELL-1` (#605) owns the full
  first-missing-prime terminal-shell identity and explicit link homology. This
  probe isolates only its `r(n)=11` shell and proves a two-sided dilation
  transfer.
- merged `P-O5-SQUAREFREE-CORE-1` owns the squarefree split carrier and the
  transfer from the public `O_5` coefficients for every exponent above `1/3`.
- merged `P-O5-WALSH-LINK-HOMOLOGY-1` and
  `P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1` remain separate topology lanes.
- merged `P-O5-DEDEKIND-GRH-DIVISOR-READ-1` is not an evidence input.
- draft Notes PR #595 is a separate NON-CANONICAL growing-mode lane.
- `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` remains untouched.

No existing object owns `P-O5-FIRST-SHELL-DILATION-TRANSFER-1` or
`O5-FIRST-SHELL-DILATION-TRANSFER`.

## Proposed candidate row

At most one row may be offered to a later sealed fold.

```text
O5-FIRST-SHELL-DILATION-TRANSFER [candidate-T]
```

Let

```text
b_11(n)=(-2)^omega(n)
```

when `n` is squarefree and every prime divisor is split and strictly greater
than `11`, and let `b_11(n)=0` otherwise. Put

```text
B_11(N)=sum_(n<=N)b_11(n),
B_11(0)=0,
D f(N)=f(floor(N/11)),
W_11=(I-D)B_11.
```

Let `S_5^sum(N)` be the squarefree split summatory carrier of merged probe
`P-O5-SQUAREFREE-CORE-1`.

The theorem package is:

```text
A. Exact dilation identities

   S_5^sum = (I-2D)B_11,
   W_11    = (I-D)B_11.

   Moreover W_11 is exactly the first terminal shell of merged probe #605:

   W_11(N)
     = sum_(N/11<n<=N, n squarefree,
            every p|n split and p>11) (-2)^omega(n).

B. Exact pointwise finite inversions

   B_11(N) = sum_(j>=0) W_11(floor(N/11^j)),

   S_5^sum(N)
     = W_11(N)
       - sum_(j>=1) W_11(floor(N/11^j)),

   W_11(N)
     = S_5^sum(N)
       + sum_(j>=1) 2^(j-1) S_5^sum(floor(N/11^j)).

   Every displayed sum is finite for each N.

C. Dirichlet-series identity on Re(s)>1

   B_11(s)=product_(split p>11)(1-2p^-s),
   S_5(s)=(1-2*11^-s)B_11(s),
   W_11(s)=(1-11^-s)B_11(s),

   W_11(s)
     = ((1-11^-s)/(1-2*11^-s)) S_5(s).

D. Let X_theta be the weighted sup space

     ||f||_theta=sup_(N>=1)|f(N)|/N^theta,
     f(0)=0.

   For every real theta with 2*11^-theta<1,

     ||S_5^sum||_theta
       <= 1/(1-11^-theta) ||W_11||_theta,

     ||W_11||_theta
       <= (1-11^-theta)/(1-2*11^-theta)
          ||S_5^sum||_theta.

   Hence, for every fixed theta>log_11(2),

     S_5^sum(N)=O(N^theta)
       iff
     W_11(N)=O(N^theta).

E. Since 2^3<11, log_11(2)<1/3. Every power-bound question at exponent
   theta>1/3, including every theta=1/2+epsilon, is therefore equivalent on
   the complete squarefree carrier and on this one annular first shell.
```

The result is a transfer theorem, not a bound. It does not claim that `W_11`
is small.

## Falsifier first

One exact defect falsifies the corresponding frozen statement:

1. the optional-`11` decomposition fails to give
   `S_5^sum=(I-2D)B_11`;
2. `W_11` differs from the first terminal shell of #605;
3. one of the three pointwise finite inversions fails;
4. the local Dirichlet factors or their quotient are wrong;
5. the weighted operator constants or threshold are wrong;
6. the `theta>1/3` consequence does not follow from `2^3<11`;
7. the construction admits inert or ramified support, selects an orientation,
   imports RH/GRH or a target cancellation estimate, or widens beyond the
   frozen transfer.

A stale basis, changed pin, failed startup preflight, nonzero verifier exit,
nonempty stderr, stdout mismatch, architecture disagreement, moved threshold
or scope widening is STOP, not a mathematical counterexample.

## The six frozen fields

```text
EQUATION
  Statements A-E exactly as displayed.

CODE
  probes/P-O5-FIRST-SHELL-DILATION-TRANSFER-1/verify.py.
  Python standard library only; exact integers and Fraction arithmetic;
  deterministic squarefree-support recursion and exact finite dilation sums;
  no float, complex approximation, network, random, zero table, special
  function or external package.

CARRIER
  chi_5 split rational primes, the squarefree split coefficient carrier,
  the tail excluding 11, integer summatory functions and floor dilation D.

SYSTEMATICS
  The smallest split prime is 11. The tail excludes 11 exactly. Inert and
  ramified primes are absent. The two prime-ideal orientations remain an
  unordered pair; no orientation is selected.

THRESHOLD
  G01 through G08 pass exactly. B1 through B5 fire at the frozen witnesses.
  One LF EXPECTED.txt, exit zero, empty stderr and byte identity are required.

LAYER
  NOT_APPLICABLE. Exact arithmetic and summatory dilation algebra only. No
  state, manifold, boundary, support-to-stream lift, measure, decoder,
  observable, physical dictionary or SI statement.
```

## 1. Optional-11 decomposition

The squarefree split Euler carrier is

```text
S_5(s)=product_(split p)(1-2p^-s).
```

The smallest split prime is `11`, so separating its local factor gives

```text
S_5(s)=(1-2*11^-s)B_11(s),
B_11(s)=product_(split p>11)(1-2p^-s).
```

Coefficientwise, a squarefree split support either omits `11`, contributing
`b_11(n)`, or contains `11`. Removing `11` from the second case gives one
unique tail support and multiplies its coefficient by `-2`. Therefore, for
every integer `N>=0`,

```text
S_5^sum(N)=B_11(N)-2B_11(floor(N/11)).
```

This is `S_5^sum=(I-2D)B_11`.

## 2. First annular shell

By definition,

```text
W_11(N)=B_11(N)-B_11(floor(N/11)).
```

Thus

```text
W_11(N)
  = sum_(floor(N/11)<n<=N)b_11(n).
```

Since `n` is integral, `floor(N/11)<n` is equivalent to `11n>N`. Every
support counted by `b_11` omits `11`, so its first missing split prime is
exactly `11`. This is precisely the `r(n)=11` terminal shell of merged probe
#605.

## 3. Pointwise finite inversions

The equation

```text
B_11=W_11+DB_11
```

iterates to

```text
B_11(N)
  = W_11(N)+W_11(floor(N/11))+W_11(floor(N/11^2))+...
```

and terminates because the floor becomes zero.

Substituting the finite sum into `(I-2D)B_11` gives

```text
S_5^sum(N)
  = W_11(N)-sum_(j>=1)W_11(floor(N/11^j)).
```

Similarly, solving

```text
(I-2D)B_11=S_5^sum
```

pointwise gives the finite geometric expansion

```text
B_11(N)=sum_(j>=0)2^j S_5^sum(floor(N/11^j)).
```

Applying `I-D` gives

```text
W_11(N)
  = S_5^sum(N)
    +sum_(j>=1)2^(j-1)S_5^sum(floor(N/11^j)).
```

No convergence theorem is needed for these pointwise formulas: every sum is
finite.

## 4. Dirichlet quotient

On `Re(s)>1` all displayed Euler products converge absolutely. The local
relations are

```text
S_5(s)=(1-2T)B_11(s),
W_11(s)=(1-T)B_11(s),
T=11^-s.
```

Hence

```text
W_11(s)/S_5(s)=(1-T)/(1-2T).
```

The formal local expansions are

```text
(1-T)/(1-2T)
  = 1 + sum_(j>=1)2^(j-1)T^j,

(1-2T)/(1-T)
  = 1 - sum_(j>=1)T^j.
```

They are the coefficient-level versions of the pointwise dilation inversions.

## 5. Weighted power-bound transfer

Let

```text
||f||_theta=sup_(N>=1)|f(N)|/N^theta,
f(0)=0.
```

For every `j>=0`,

```text
|D^j f(N)|
  = |f(floor(N/11^j))|
  <= ||f||_theta (N/11^j)^theta,
```

so

```text
||D^j||<=11^(-j theta).
```

The formula for `S_5^sum` in terms of `W_11` has absolute coefficient sum

```text
1+sum_(j>=1)11^(-j theta)=1/(1-11^-theta).
```

The inverse formula has absolute coefficient sum

```text
1+sum_(j>=1)2^(j-1)11^(-j theta)
  = (1-11^-theta)/(1-2*11^-theta).
```

The latter is finite exactly when `2*11^-theta<1`, equivalently
`theta>log_11(2)`. This proves the norm bounds and the two-sided power-bound
transfer.

The statement is exact for this explicit absolute Neumann-series route. It
does not classify every conceivable transfer below the threshold.

Finally,

```text
2^3=8<11,
```

so `log_11(2)<1/3`. The whole exponent region inherited from the merged
squarefree-core transfer, `theta>1/3`, is safely inside the dilation-transfer
domain.

## Frozen negative controls

```text
B1  replace `(I-2D)B_11` by `(I-D)B_11`.
    First failure: N=11.

B2  replace the dilation scale 11 by 19 in W_11.
    First failure: N=11.

B3  omit the j=0 term in the B_11 inversion.
    First failure: N=1.

B4  replace inverse weights 2^(j-1) by 1.
    First failure: N=121.

B5  claim absolute inverse convergence at theta=1/4.
    It fails because 2^4=16>11; theta=1/3 passes because 2^3=8<11.
```

Each breaker changes a production constructor or the exact threshold. No
parallel toy formula is used.

## Frozen verifier gates

```text
G01  first split prime 11 and exact full/tail coefficient census through 20000.
G02  optional-11 and first-shell identities through 5000 plus 10000,20000.
G03  all three finite dilation inversions on the same surfaces.
G04  coefficient local factor and quotient series through degree 16.
G05  exact Neumann operator algebra through degree 18 and threshold integers.
G06  exact weighted geometric constants on a rational interior witness.
G07  B1-B5 at 11,11,1,121,1/4.
G08  LF-only exact-rational standard-library source firewall.
```

The finite gates audit the universal written proof and do not define its
scope.

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
  /usr/bin/python3 probes/P-O5-FIRST-SHELL-DILATION-TRANSFER-1/verify.py
```

The one accepted stdout becomes `EXPECTED.txt`. `RUN.md` and `RESULT.md` are
post-pin records only.

## Explicit nonclaims

No RH or GRH result, new summatory estimate, analytic continuation,
zero-location statement, Hecke or automorphic object, selected split
orientation, physical interpretation, probability statement, SI statement or
L1-L6 lift is claimed. The theorem proves only that one annular first shell is
power-bound equivalent to the complete squarefree split carrier above the
exact dilation threshold.
