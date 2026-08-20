# C-RH-WIDDER-ANGLE-SWEEP-CORRECTION-1-N preregistration

```text
STATUS:         NON-CANONICAL / PROOF-FIRST / RESULT-EXPOSED / CORRECTION
AUTHORITY:      none
TARGET LINE:    PUBLIC context only
OWNER SESSION:  rh-widder-angle-sweep-correction-2026-08-20
PUBLIC ISSUE:   #477
PARENTS:        #471, #374
AUDITED INPUT:  handoff/audit-euler-widder-depth-20260820 at c1196615
CANON WRITE:    forbidden
FORMAL PROBE:   none
```

This file is frozen and remotely read before any formal execution in this
lane. The correction is result-exposed: an exact counterexample to the
handoff audit's arbitrary-level endpoint criterion was already found before
this lock. That calculation is preparation only. `break.py` is written and
pinned after this readback; the positive proof and verifier are written only
after the breaker is frozen and run.

## Authority and basis

Public Canon v57 is ACTIVE.

```text
main at lock:   e6845b96fc19a47c473761ad49d4f8a7812c2f58
TAG:            canon-v57 at 4ef54f0c34f80897af0121a2d93b710e70a8377c
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
```

The tag and content commit are ancestors of the lock-time main. The seven
post-tag commits add only the two QDD probe directories merged by PRs #473 and
#475. No normative file changed after the v57 activation tree.

Collision searches found no issue, branch, probe, note path, Registry row, or
indexed file with this identifier or `WIDDER-ANGLE-SWEEP-CORRECTION`.

## Field one: equation

Retain the paired-pole conventions of #471. For one conjugate pair

```text
z=-A+iB,       A>0, B>=0,
```

and integer `k>=1`, define its contribution to the Widder level by

```text
P_k(A,B;u)
 =2(2k-1)! Re[(A-iB)^k/(u+A-iB)^(2k)],       u>0.
```

For `B>0`, put

```text
theta=arctan(B/A) in (0,pi/2),
phi(u)=arctan(B/(u+A)) in (0,theta).
```

The frozen positive magnitude and phase form is

```text
P_k(A,B;u)
 =2(2k-1)!
  [(A^2+B^2)^(1/2)/((u+A)^2+B^2)]^k
  cos(k(2phi(u)-theta)).
```

The target sweep theorem is

```text
u in (0,infinity)  maps  2phi(u)-theta  monotonically onto (-theta,theta).
```

Therefore

```text
P_k(A,B;u)<0 for some u>0   iff k theta>pi/2,
P_k(A,B;u)>0 for every u>0 iff k theta<=pi/2.
```

At equality the endpoint cosine is zero only in the limit `u->0+` or
`u->infinity`; the contribution is strictly positive at every finite `u>0`.
For `B=0`, every level is strictly positive.

The corrected first-failure depth is

```text
k_min(A,B)
 =min{k>=1: P_k(A,B;u)<0 for some u>0}
 =floor(pi/(2theta))+1
 =min{k>=1: Re[(A-iB)^k]<0}.
```

The last equality is only a first-failure statement. For a fixed arbitrary
later level, the exact integer-only condition is

```text
P_k is negative somewhere
iff there exists j<=k with Re[(A-iB)^j]<0.
```

## Field two: code

Two exact programs, Python standard library only:

```text
break.py   independent attack, frozen and run before the positive proof;
verify.py  exact rational audit, written only after the breaker run.
```

Allowed objects:

- `int` and `Fraction`;
- rational complex pairs in `Q(i)`;
- integer polynomials and factorials;
- exact alternating-series brackets for pi only where the depth formula is
  audited.

Forbidden:

- float, `math.pi`, mpmath, numpy, scipy, sympy;
- actual zeta ordinates or any zero table;
- network or external data;
- importing or executing the handoff audit's programs as evidence.

Frozen command:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 notes/C-RH-WIDDER-ANGLE-SWEEP-CORRECTION-1-N/<program>
```

The written proof carries all universal statements. Scripts are exact breakers
and finite audits only.

## Field three: carrier or data

No external dataset and no actual zeta zero.

Frozen exact controls:

```text
HANDOFF OWNER LOW:
  rho=9/10+i/2,
  A=17/50, B=2/5,
  first failing level 2.

HANDOFF OWNER HIGH:
  rho=3/4+10i,
  A=1603/16, B=5,
  first failing level 32.

ARBITRARY-k ENDPOINT COUNTEREXAMPLE:
  A=B=1, k=8, u=1/2,
  Re[(1-i)^8]=16>0,
  P_8(1,1;1/2)
   =-172056926056081143103488000/51185893014090757<0.

RESONANCE COUNTEREXAMPLE:
  A=B=1, theta=pi/4,
  P_2(1,1;u)>0 for all u>0,
  infimum 0 at the excluded endpoint,
  first failing level 3, not ceil(pi/(2theta))=2.

FINITE-PREFIX FAMILY:
  for N>=1, rho_N=3/4+iN,
  A_N=N^2+3/16,
  B_N=N/2.
```

Finite verifier range for the universal family: `N=1..128`, every
`k=1..N`, and a declared rational `u` grid. The proof, not the grid, establishes
positivity for all `u>0` and all integers `N>=1`.

Additional counterexample grid for the false arbitrary-level endpoint test:

```text
A,B in {1,2,3,5}, k=1..32, rational u in
{1/100,1/10,1/2,1,2,10,100}.
```

At least one exact witness with endpoint real part nonnegative and interior
pair contribution negative must be found and the frozen `A=B=1,k=8,u=1/2`
witness must be reproduced exactly.

## Field four: systematics

### S1. Phase orientation

The numerator `A-iB` has argument `-theta`; the denominator root
`u+A-iB` has argument `-phi(u)`. The ratio phase is
`2phi(u)-theta`, not its negative. Cosine is even, but monotonic sweep and
endpoint statements must use one convention consistently.

### S2. Open endpoints

For `u>0`, `phi(u)` lies strictly between `0` and `theta`. Thus the swept
interval is open. Equality `k theta=pi/2` gives strict positivity at every
finite `u`, with zero only as an unattained limit. This is the source of the
`floor+1` formula and the resonance counterexample.

### S3. Later-level return

When `k theta>pi`, the endpoint cosine may return positive although the swept
interval contains a negative arc. Any arbitrary-level criterion using only
`Re[(A-iB)^k]` is therefore false. The first-failure integer test survives
because at the least failing `k`,

```text
pi/2<k theta<pi/2+theta<pi.
```

### S4. Pair and multiplicity convention

One `z` represents one functional pair `{rho,1-rho}`. If `B!=0`, its conjugate
functional pair supplies `conj(z)` and the real contribution has the factor 2.
If `B=0`, do not duplicate the real pole. Finite controls may use a conjugate
pair directly and must state which convention is in force.

### S5. Finite-prefix theorem

For `rho_N=3/4+iN`,

```text
B_N/A_N=(N/2)/(N^2+3/16)=8N/(16N^2+3)<1/(2N).
```

Since `arctan x<x` for `x>0`, for every `k<=N`,

```text
k theta_N<k/(2N)<=1/2<pi/2.
```

The angle-sweep theorem then gives strict positivity for every `u>0`.
Adding any on-line positive background preserves the finite-prefix result.
No masking estimate is needed.

### S6. Actual-zeta safe depth

For `rho=beta+i gamma`, `0<beta<1`, let

```text
A=gamma^2+beta(1-beta),
B=|gamma(2beta-1)|.
```

If `|gamma|>=H>=1`, then

```text
B/A<1/|gamma|<=1/H,
theta<arctan(1/H).
```

If all lower zeros are on line, all levels

```text
k<=floor(pi/(2 arctan(1/H)))
```

are positive. The weaker `floor(pi H/2)` bound is allowed as a corollary.
No numerical `H` is asserted without a separately frozen source certificate.

### S7. Status and overlap

The correction does not falsify #471. It falsifies only two auxiliary claims
of the later handoff audit:

- arbitrary-level endpoint equivalence;
- `ceil` at exact resonance.

The audit's owner depths, unconditional `W_2` conclusion, finite-height safe
range, and strategic redirection survive after corrected wording. Issue #469
continues to own the finite-window interpolation certificate. Lambda-cocycle
work is out of scope.

## Field five: failure threshold

```text
CF1 phase sweep is not monotone onto the stated open interval.
CF2 negativity somewhere is not equivalent to k theta>pi/2.
CF3 the exact A=B=1,k=8,u=1/2 counterexample fails.
CF4 first failure is not floor(pi/(2theta))+1 or does not equal the first
    negative integer power.
CF5 the resonance A=B=1 has first failure other than 3.
CF6 one N>=1 in the written family admits a nonpositive contribution at a
    level k<=N and some u>0.
CF7 the zeta safe-depth inequality is false at its stated conditional scope.
CF8 a termwise adjacent-level positivity implication survives the frozen low
    off-line counterexample.
CF9 the result is stated as RH evidence, actual-zero information, a public
    theorem, or a replacement for #469.
CF10 any remote byte, pin, execution-order, stdout, stderr, or hash mismatch.
```

A mathematical CF is recorded as bounded F. An integrity CF is STOP. No
threshold or statement moves after this preregistration is pinned.

Decision vocabulary:

```text
CORRECTION  C1-C6 survive: candidate-T written angle-sweep correction and
            finite-prefix horizon; candidate-C exact controls.
F           one corrected mathematical target fails exactly.
STOP        authority, ordering, pair convention, source, or integrity fails.
```

## Field six: action layer

Analytic and L6 spectral only. No physical TWIST-J L1 to L6 lift. No Canon,
Registry, Frontier, evidence, formal probe, release, physical, decoder, Born,
SI, or J-native carrier claim.

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
