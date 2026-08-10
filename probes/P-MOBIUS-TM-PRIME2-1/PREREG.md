# P-MOBIUS-TM-PRIME2-1 preregistration

Date: 2026-08-10

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. No formal gate may run before this file and the accepted verifier are
both present at the immutable pin, that pin is pushed, and both files are read
back from the public remote.

Public claim lock: issue 326.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v40
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v40
CONTENT_COMMIT: c34c04618d6ed4035266cd8ad6c27915536bebf5
CANON_SHA256:   54842ab0327b7c3be44242dbc6cbe52682e92aa2098978fcf4cd4727480d0d38
CANON_BYTES:    189737
BASE_COMMIT:    6a376041fb3160839ffe1bfd0b66875d134e4f5b
```

The governing authority is `mathorn1973/twist-j` on `main`. This probe is L1
only. It opens no inter-layer gate.

## Mandatory result-exposure disclosure

A prior NON-CANONICAL incubation, `C-PRIME-BOOLE-2`, explored closely related
identities and ran one x86_64 verifier plus one same-session adversarial
breaker before this public preregistration existed. It produced positive
transcripts and hashes.

Every prior incubation file, run, transcript, hash, finite range, and observed
result is provenance only and is excluded from public evidence for this probe.
The accepted verifier in this directory is separately authored. Its formal
execution count is zero at this preregistration.

The earlier incubation name `C-PRIME-BOOLE-2` creates no public claim, pin,
threshold, or status.

## Field 1: equation

### Fixed notation

For positive integers, let

```text
mu(n)    = the Moebius function
1(n)     = 1
(f*g)(n) = sum_(d|n) f(d) g(n/d)       Dirichlet convolution
D_p f(n) = f(p n)                       prime dilation
```

Let

```text
tau(n) = (-1)^s_2(n),  n >= 0,
```

where `s_2(n)` is the binary digit sum, and on positive integers define

```text
c = mu * tau.
```

The theorem target is one L1 arithmetic package with six clauses.

### S1. Prime-dilation / Moebius-support equivalence

For every prime `p` and every complex-valued arithmetic function `f`, put
`g = mu*f`. Then

```text
D_p f = f on all positive integers
```

if and only if

```text
g(n) = 0 for every positive n divisible by p.
```

Written proof. Forward direction: write `n = p^a r`, `a >= 1`, `p` not dividing
`r`. Only divisors with zero or one factor `p` survive under `mu`, hence

```text
g(p^a r)
  = sum_(e|r) mu(e)
      [ f(p^a r/e) - f(p^(a-1) r/e) ]
  = 0.
```

Reverse direction: Moebius inversion gives `f = 1*g`. If `g(d)=0` whenever
`p|d`, then

```text
f(p n) = sum_(d|pn, p not dividing d) g(d)
       = sum_(d|n,  p not dividing d) g(d)
       = f(n).
```

This is an all-function theorem, not a finite classification.

### S2. Prime-2 annihilation and odd primitive reconstruction

Thue-Morse parity obeys

```text
tau(2n)   =  tau(n),
tau(2n+1) = -tau(n).
```

By S1 at `p=2`,

```text
c(2n) = 0 for every n >= 1.
```

Moebius inversion gives

```text
tau = 1*c,
tau(n) = sum_(d|n) c(d).
```

Because `c` is zero on every even positive integer,

```text
tau(n) = sum_(d|n, d odd) c(d).
```

Hence `c` is the unique arithmetic function supported on odd positive
integers whose divisor sum equals `tau`.

Scope correction frozen here: `mu(2x)=-mu(x)` is true for odd `x` and false in
general for even `x`; `x=2` is an explicit counterexample. S2 does not use the
false unrestricted wording.

### S3. Boolean mixed difference on odd squarefree support

For odd squarefree

```text
n = product_(p in P) p,
```

one has

```text
c(n) = product_(p|n) (D_p - I) tau(1)
```

and therefore

```text
c(n) = sum_(S subseteq P) (-1)^(|P|-|S|)
          tau(product_(p in S) p).
```

This is the top Boolean finite difference of binary digit parity over the
prime-divisor cube. No multiplicativity of `c` is claimed. The exact witness

```text
c(3)=2, c(5)=2, c(15)=-2
```

is frozen as a guard against such a misreading.

As immediate exact corollaries, for every odd prime `p` and `k >= 1`,

```text
c(p)   = tau(p) + 1 in {0,2},
c(p^k) = tau(p^k) - tau(p^(k-1)) in {-2,0,2}.
```

### S4. Odd divisor recursion

For every positive integer `n`, S2 and `tau(2n+1)=-tau(n)` give

```text
sum_(d|2n+1) c(d) = - sum_(d|n) c(d).
```

This is only a divisor-sum rewriting of the Thue-Morse odd-step relation.

### S5. Lambert bridge

For `|x|<1`, define

```text
F(x) = sum_(n>=0) tau(n) x^n.
```

The two Thue-Morse recurrences give directly

```text
F(x) = (1-x) F(x^2).
```

Iteration and absolute convergence yield

```text
F(x) = product_(j>=0) (1 - x^(2^j)).
```

Using S2 and absolute convergence again,

```text
F(x)-1
  = sum_(n>=1) tau(n) x^n
  = sum_(n>=1) sum_(d|n, d odd) c(d) x^n
  = sum_(d>=1, d odd) c(d) x^d/(1-x^d).
```

Therefore

```text
product_(j>=0) (1 - x^(2^j)) - 1
  = sum_(d>=1, d odd) c(d) x^d/(1-x^d),   |x|<1.
```

No analytic continuation is included.

### S6. Dirichlet bridge and prime-2 factor cancellation

For `Re(s)>1`, define

```text
T(s)     = sum_(n>=1) tau(n) n^(-s),
C(s)     = sum_(n>=1) c(n) n^(-s),
T_odd(s) = sum_(n odd) tau(n) n^(-s),
zeta_odd(s) = (1 - 2^(-s)) zeta(s).
```

Since `|c(n)| <= sum_(d|n)|mu(d)| <= d(n)`, all relevant Dirichlet series are
absolutely convergent for `Re(s)>1`. From `tau=1*c`,

```text
T(s) = zeta(s) C(s).
```

From `tau(2^a m)=tau(m)` for odd `m`,

```text
T(s) = T_odd(s)/(1 - 2^(-s)).
```

Together with `zeta(s)=zeta_odd(s)/(1-2^(-s))`,

```text
C(s) = T_odd(s)/zeta_odd(s).
```

This is cancellation of the common prime-2 dilation factor inside the proved
half-plane. It is not an Euler product for `T` or `C`; neither `tau` nor `c` is
multiplicative.

## Field 2: code

Accepted verifier:

```text
probes/P-MOBIUS-TM-PRIME2-1/verify.py
```

The verifier is Python standard library only and uses exact integer arithmetic.
It contains no `float`, complex approximation, tolerance, external data, web
input, or incubation transcript. It audits finite instances and coefficient
identities only. The public `T` target rests on the written proofs S1 through
S6, not on a finite search.

The verifier is separately authored from the exposed incubation verifier.

## Field 3: carrier or data

Carrier only. No external data.

```text
positive integers under divisibility and Dirichlet convolution;
binary digit parity tau(n)=(-1)^s_2(n);
Moebius function mu;
finite exact coefficient arrays used only by the verifier audit.
```

No zeta-zero table, measured data, external sequence file, or prior transcript
is admissible.

## Field 4: systematics and completeness

There is no measurement systematic.

Completeness obligations are frozen as follows:

```text
C1  S1 is proved for arbitrary arithmetic f and every prime p; finite synthetic
    lanes in verify.py are audits only.
C2  S2 uses the exact binary recurrences and S1. The unrestricted false formula
    mu(2x)=-mu(x) is explicitly excluded and checked false at x=2.
C3  S3 is a complete expansion over the full divisor Boolean cube of a
    squarefree n; no sampled-cube argument is used in the written proof.
C4  S5 proves the infinite product from F(x)=(1-x)F(x^2) and absolute
    convergence for |x|<1; finite coefficient checks are audits only.
C5  S6 proves absolute convergence for Re(s)>1 before rearrangement and uses
    only Dirichlet convolution plus the exact prime-2 recurrence.
C6  No clause uses RH, analytic continuation, J, p=5 selection, a decoder,
    measure, physical interpretation, or an L2-L6 object.
```

Any hidden input, external data, floating tolerance, imported incubation output,
post-pin scope change, or unnamed layer lift is a STOP condition.

## Field 5: failure threshold and scientific routing

No tolerance exists.

```text
BRIDGE-PASS
  Every frozen exact verifier gate passes and no written proof defect is found.

MISMATCH
  One exact counterexample to a frozen S1 through S6 statement, or one exact
  coefficient mismatch in the accepted audit, falsifies the affected clause.
  The exact witness is printed and preserved.

STOP
  Authority, branch, pin, verifier integrity, completeness, security,
  transcript, or layer discipline fails.
```

`BRIDGE-PASS` and `MISMATCH` are scientific outcomes and exit zero. `STOP` is
an integrity outcome and exits nonzero. The threshold and scope may not move
after the pin.

## Field 6: action layer

```text
L1 only: arithmetic functions on positive integers, divisibility, binary digit
parity, Moebius inversion, and absolutely convergent generating/Dirichlet
series in the explicitly declared domains.
```

No L1-to-L2/L3/L4/L5/L6 lift is attempted or owned.

## Scope firewall

This probe does not:

- assert RH or locate any zeta zero;
- assert Nyman-Beurling or Baez-Duarte completeness;
- analytically continue `T`, `C`, or the Lambert identity beyond the declared
  domains;
- couple the theorem to `J` or select `p=5`;
- derive a decoder, Born rule, observer, force, spacetime, SI bridge, or
  physical vacuum;
- assert pointwise Moebius orthogonality or import asymptotic correlation
  theorems as evidence;
- assert that `c` is multiplicative;
- move any current Canon v40 claim, frontier row, or status;
- reuse the prior incubation run as evidence.

A later RH, Hilbert, or J interpretation requires a separately named claim and
layer gate.

## Formal sequence after the pin

1. Read back this file and `verify.py` from the public remote at the immutable
   pin; record commit, SHA-256, and byte counts on issue 326.
2. Only then execute the accepted verifier for the first formal run.
3. Commit exact `EXPECTED.txt`, neutral `RUN.md`, and `RESULT.md` without
   changing the pinned preregistration or verifier.
4. Open one pull request changing only `probes/P-MOBIUS-TM-PRIME2-1/`.
5. Require GitHub x86_64 and aarch64 jobs to reproduce the same committed
   `EXPECTED.txt` byte for byte.
6. Because `T` is sought by written proof, the two-architecture run is an audit
   of the accepted verifier, not the source of the all-n quantifiers.
7. Any Canon/registry/frontier fold is a later separate reviewed action, with
   Public Canon v41 only if the item is eligible under the then-current fold
   policy.
