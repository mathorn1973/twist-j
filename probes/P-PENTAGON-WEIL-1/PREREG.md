# P-PENTAGON-WEIL-1 preregistration

Status: PREREGISTERED CANDIDATE; FIRST FORMAL RUN PENDING REMOTE PIN READBACK

This document freezes the complete G0 decision surface for the first public
root-filter normalization probe on the PENTAGON-WEIL route.  It contains no
formal gate output and earns no scientific status.  Formal execution is
forbidden until this exact revision and the accepted verifier are committed,
pushed, and read back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          PENTAGON-WEIL
probe:            P-PENTAGON-WEIL-1
public lock:      issue 41
owner:            pentagon-weil G0 session
branch:           probe/P-PENTAGON-WEIL-1
path:             probes/P-PENTAGON-WEIL-1/
initial base:     6bb013bafb2d1c06fcb295fdbfce0f86198fd685
action layer:     L5 analytic/root-filter stream; no L5-to-L6 lift, measure
                  construction, Weil form, or physical reading is claimed
scientific state: candidate exact normalization and equivalence facts only;
                  Weil positivity and RH remain open
```

The authority base is Public Canon v6, tag `canon-v6`, activation commit
`6bb013bafb2d1c06fcb295fdbfce0f86198fd685`, content commit
`46f6412943bbd32bd3a686456c36612a1fc8fb3c`, Canon SHA-256
`5b810f0d7d36254d6968f72cd4cefe6956b772e0046ca41f0a9867b3818bb748`,
and Canon byte count 60697.  At issue-lock time, no earlier public claim,
probe, or branch carried this PENTAGON-WEIL scope.

## Frozen definitions

Let

```text
j = zeta_5 = exp(2 pi i/5),        j^5 = 1,
J = 1 + j^2,                       j = (J-1)^3,
P_0(s) = sum_(a=1)^4 Li_s(j^a),
5^(1-s) = exp((1-s) log 5),        log 5 > 0,
f_5(s) = 5^(1-s) - 1.
```

For `Re(s) > 1`, expand the polylogarithms absolutely and define

```text
c(n) = sum_(a=1)^4 j^(a n).
```

The root filter gives

```text
c(n) = 5[5 divides n] - 1,
P_0(s) = sum_(n>=1) c(n)n^(-s) = f_5(s) zeta(s).
```

The normalized meromorphic branch and standard completion are

```text
Z_J(s)  = MerCont_(Re(s)>1) P_0(s)/f_5(s) = zeta(s),
xi_J(s) = (1/2)s(s-1)pi^(-s/2)Gamma(s/2)Z_J(s) = xi(s).
```

The raw standard completion, which is deliberately not normalized, is

```text
Xi_raw(s) = (1/2)s(s-1)pi^(-s/2)Gamma(s/2)P_0(s)
          = f_5(s) xi(s).
```

## Frozen theorem-grade consequences

### G01 ROOT-FILTER

In `Z[j]`, exhaustive reduction of the five residue classes gives exactly

```text
c(n) = 4   if 5 divides n,
c(n) = -1  otherwise.
```

Hence `P_0(s) = f_5(s) zeta(s)` on `Re(s)>1`; uniqueness of meromorphic
continuation gives `Z_J = zeta` globally.

### G02 VALUE AT ONE

Cyclotomic factorization gives

```text
prod_(a=1)^4 (1-j^a) = Phi_5(1) = 5.
```

The factors form the conjugate pairs `(a,5-a)` and are nonreal, so none lies
on the principal-log branch cut.  Moreover, under the fixed positive real
embedding of `sqrt(5)`,

```text
(1-j)(1-j^4)     = (5-sqrt(5))/2 > 0,
(1-j^2)(1-j^3)   = (5+sqrt(5))/2 > 0.
```

Thus `Log(conjugate(z))=conjugate(Log(z))` applies to each pair, their
principal arguments cancel, and the sum of their real logarithms is the
logarithm of the positive product.  Therefore

```text
P_0(1) = -sum_(a=1)^4 Log(1-j^a) = -log 5.
```

This is also the value of the naturally ordered convergent Dirichlet series,
not merely a continued value.  Exactly,

```text
sum_(n<=N) c(n)/n = H_floor(N/5) - H_N -> -log 5.
```

For `N=5M`, the positive quantity `H_(5M)-H_M` is the right Riemann sum for
the decreasing function `1/x` on `[1,5]`, and the left-right sum difference
is exactly `1/M-1/(5M)=4/(5M)`.  Hence

```text
0 <= log 5 - (H_(5M)-H_M) <= 4/(5M).
```

For `N=5M+r`, `0<=r<=4`, the remaining term is
`-sum_(q=1)^r 1/(5M+q)`, whose absolute value tends to zero.  This proves the
displayed limit for the full natural sequence without floating point.

### G03 EXACT FINITE CUTOFF

For every positive integer `N` and integer `s > 1`, the exact finite identity
is

```text
sum_(n=1)^N c(n)/n^s
  = 5^(1-s) H_floor(N/5)^(s) - H_N^(s).
```

The verifier checks every cutoff `N = 1..625` for `s = 2,3,4` using
`fractions.Fraction`.  It does not replace `H_floor(N/5)` by `H_N`.

### G04 RAW STANDARD SYMMETRY FALSIFIER

The imported standard functional equation gives `xi(s)=xi(1-s)`.  Since

```text
f_5(2)  = -4/5,
f_5(-1) = 24,
f_5(2)/f_5(-1) = -1/30,
```

the raw standard completion does not satisfy

```text
Xi_raw(s) = epsilon Xi_raw(1-s)
```

with a constant root number `|epsilon|=1`.  In particular it is not
self-dual with root number one.  No stronger no-functional-equation claim is
made: meromorphically it obeys the variable-factor identity

```text
Xi_raw(s) = [f_5(s)/f_5(1-s)] Xi_raw(1-s).
```

### G05 SIGNED LOGARITHMIC-DERIVATIVE CORRECTION

For `Re(s)>1`,

```text
-zeta'(s)/zeta(s)
  = -P_0'(s)/P_0(s) + f_5'(s)/f_5(s),

f_5'(s)/f_5(s)
  = log 5 * sum_(m>=1) 5^m (5^m)^(-s).
```

Consequently

```text
-P_0'(s)/P_0(s)
  = sum_(n>=1) Lambda(n)n^(-s)
    - log 5 * sum_(m>=1) 5^m (5^m)^(-s).
```

At `n=5^m` the raw coefficient is `(1-5^m)log 5`; the correction adds
`+5^m log 5` and restores the true `Lambda(5^m)=log 5`.  The artificial tower
is a signed root-filter artifact, not a local Euler factor.

### G06 RH EQUIVALENCE, NOT RH

The zeros of `f_5` are

```text
s_k = 1 - 2 pi i k/log 5,    k in Z,
```

all on `Re(s)=1`.  Therefore `f_5` is nonzero in the open critical strip and

```text
RH
  iff every zero of P_0(s) in 0 < Re(s) < 1
      lies on Re(s)=1/2.
```

This equivalence is an exact reformulation.  It supplies no proof that either
side is true.

## Imported classical theorems

The following are declared imports, not TWIST-J results: the analytic
continuation and functional equation of zeta; the standard Gamma completion;
the Euler product and von Mangoldt logarithmic derivative on `Re(s)>1`;
Dirichlet/Abel convergence at roots of unity; uniqueness of meromorphic
continuation; and the standard integral definition
`integral_1^5 dx/x = log 5`.  The harmonic limit itself is proved above.
Weil's criterion is not used by this G0 probe.

## Six frozen preregistration fields

```text
equation:     G01 through G06 exactly as stated above, including the narrow
              raw standard-symmetry falsifier and the signed correction.
code:         verify.py in this directory; Python 3 standard library only;
              integer, Z[j], and Fraction arithmetic; no float, tolerance,
              random choice, external package, external data, or file write.
carrier:      the five residue classes modulo 5, Z[j] in basis
              1,j,j^2,j^3, and exact finite harmonic sums through N=625;
              no list of zeta zeros or primes is an input.
systematics:  principal Log for G02; positive real log 5; natural series
              ordering; cutoffs N=1..625; s=2,3,4; tower exponents m=1..12;
              all infinite analytic steps are the named imports above.
failure
threshold:    any verifier gate FAIL, any mismatch in an inline derivation,
              any branch ambiguity, sign reversal, hidden root-filter zero,
              or conclusion stronger than G01-G06.
action layer: L5 analytic/root-filter stream only.  No L5-to-L6 lift,
              positive form, Hilbert space, spectrum, or physical measure is
              inferred.
```

## Evidence posture

The exact derivations in this document are the proposed theorem-grade
evidence for the G0 identities.  The verifier audits finite algebra and sign
accounting; it is not a numerical proof of analytic continuation, RH, or a
Weil criterion.  An aarch64 local run and GitHub x86_64 rerun may establish
byte-identical reproducibility of the audit, but do not strengthen the scope.

## Environment and formal execution

```text
cd <repo root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-PENTAGON-WEIL-1/verify.py
```

The first formal run occurs only after the remote preregistration pin is read
back.  Its exact stdout becomes `EXPECTED.txt`; `RUN.md` records neutral
platform and architecture fields plus the pin and file hashes.  A preliminary
`RESULT.md` is added before the pull request.  GitHub x86_64 must rerun the
pinned verifier and produce byte-identical stdout.

## Pre-pin development disclosure

A local non-canonical candidate note and one non-formal Linux x86_64 run were
used before this pin to discover the correct finite cutoff, narrow the raw
functional-equation claim, and freeze the sign of the `5^m log 5` tower.
Those materials were never public claims or formal probe evidence.  The
formal verifier in this directory has not been executed before the remote pin.

## Out of scope, explicitly

- no positivity of a Weil form and no proof or numerical test of RH;
- no definition yet of a Weil test space, involution, or operator;
- no `J-WEIL-EQUIVALENCE [T]` claim before those conventions are frozen;
- no self-adjoint or positive `J` realization;
- no finite-kernel lift, no L5-to-L6 lift, and no physical interpretation;
- no relation to the distinct finite `ENTROPY-PENTAGON-QUOTIENT` claim;
- no registry, frontier, Canon, fold, release, or tag edit in this probe.

Any one of those requires a separate ruling, public probe, or later sealed
Canon fold.
