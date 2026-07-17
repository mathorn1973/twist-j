# C-LI-Q-MOMENT-1 / N1 pin. Fresh gamma_2 width and the SH-1 = Q transfer

```text
STATUS:          NON-CANONICAL NOTES-GRADE PIN
PUBLIC CLAIMS:   none
DATE:            2026-07-17
PARENT:          C-LI-Q-MOMENT-1 at
                 3d25a13a7409db2db108bc9b671b7a05899d25cb
TARGET:          N1 only
RH:              O
```

This file freezes the N1 verifier and its action rules before the first
evidentiary execution of `verify_q_moment_n1.py`.  It contains no result and
no stdout.  Compilation and source inspection are non-evidentiary static
checks.  Any source change after the pin invalidates the run and requires a
new pin.

The frozen source identity is

```text
verify_q_moment_n1.py
  sha256  9b5fc0e18eda719ca8d63ce3626e449d3d0c7859288d4ba361f550ba502df486
  bytes   12947
  lines   420
```

The execution protocol, from repository root, is exactly

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
python -B notes/C-LI-Q-MOMENT-1/verify_q_moment_n1.py
```

No `-O` or other optimization flag is permitted.  Stdout is captured byte
for byte, stderr must be empty, and the evidentiary run passes only with exit
code zero and every frozen gate printed as `PASS`.

## 1. Exact junction frozen before numerics

The q-moment candidate gives

```text
qw_0 = sigma_1,
qw_1 = 2 sigma_1 + sigma_2,
qw_2 = 6 sigma_1 + 3 sigma_2 + sigma_3.
```

Therefore

```text
SH-1 = qw_0 qw_2 - qw_1^2
     = 2 sigma_1^2 - sigma_1 sigma_2
       + sigma_1 sigma_3 - sigma_2^2
     = sigma_1(2 sigma_1 + sigma_3 - sigma_2) - sigma_2^2
     = Q.
```

The final expression is exactly the symmetric-block invariant `Q` of the
existing `T_2` cocycle certificate.  In particular,

```text
det T_2 = 2(2 sigma_1 + sigma_2 - sigma_3) SH-1.
```

The new verifier must machine-check this identity over `Q` before evaluating
any interval.  It must not demand equality of the two interval objects:
dependency inflation makes the direct and reduced enclosures different even
though the underlying expressions are identical.

## 2. Frozen analytic route and parameters

No zero list, prime table, imported decimal for a standard constant, float,
random input, network access, or external package is allowed.  All numerical
assertions use outward-rounded integer intervals at

```text
S             10^24
N             200000
LOG_TERMS     32
gamma_2 width <= 10^-9  (scaled width <= 10^15)
```

The value `N=200000` is selected from the declared Euler--Maclaurin remainder
before the N1 verifier is executed.  Put

```text
f(x) = log^2(x)/x,
A_N  = sum_(k<=N) f(k) - log^3(N)/3.
```

For `log N > 3`, `f'<0` and `f''>0`.  Euler--Maclaurin with the `B_2` term
gives

```text
gamma_2 = A_N - f(N)/2 - f'(N)/12 + R,
|R| <= -f'(N)/12,
```

and hence the outward enclosure

```text
A_N - log^2(N)/(2N)
  <= gamma_2 <=
A_N - log^2(N)/(2N)
  + (log^2(N)-2log(N))/(6N^2).
```

The standalone verifier assembles `gamma`, `gamma_1`, `zeta(3)`, `pi`, and
`log(4pi)` with the already-audited elementary methods in
`notes/j-li-schoenberg-2/verify_lambda3_t2.py`, then evaluates
`sigma_1,sigma_2,sigma_3`, `qw_0,qw_1,qw_2`, and both SH-1 forms.

## 3. Frozen comparator pins

The following intervals are comparator data, not construction inputs.

```text
lambda_1 in
[23095708964233559, 23095708972138893] * 10^-18

M_1 in
[37100438723459, 37100843555683] * 10^-18

historical gamma_2 in
[-0.009690364105552333923998,
 -0.009690362736532310677668]

historical Q in
[0.000000001883563636456191,
 0.000000001989968490233267]
```

The historical gamma_2/Q source is the two-architecture incubation pin:

```text
verify_lambda3_t2.py       sha256 49cdaa5769104fda39a18d5a3e75dd4f2da6526e4a2e93201f89345058ebad2a
LAMBDA3_T2_EXPECTED.txt    sha256 678bd1b4e88b12f074c5c46ed06c69f98984570cc3c312a64921a9ac4b0ef60a
LAMBDA3_T2_AARCH64_RUN.md  sha256 3b170c7bfac3ee1d1fbacdf16510eedb073bda443948472548fd711d8c9bcc8e
```

## 4. Frozen gates

The first failure is preserved.

```text
N1-ALG  exact SH-1 = Q coefficient identity;
N1-EM2  log/derivative shape and gamma_2 width <= 10^-9;
N1-G2   fresh gamma_2 interval lies inside the historical interval;
N1-J0   fresh qw_0 interval lies inside the lambda_1 pin;
N1-J1   fresh qw_1 interval lies inside the M_1 pin;
N1-Q2   fresh qw_2 interval is strictly positive;
N1-DIR  direct SH-1 interval is strictly positive;
N1-RED  reduced Q-normal interval is strictly positive;
N1-OVL  direct and reduced intervals overlap;
N1-XPIN fresh reduced interval lies inside the historical Q pin.
```

## 5. Frozen action rules

```text
source/hash mismatch       invalidate; do not execute or reinterpret
gamma_2 width gate fails   N1 inconclusive; do not retune this pin
junction comparator fails  stop for an arithmetic/provenance audit
SH-1 interval straddles 0  N1 inconclusive; do not widen claims
SH-1 interval < 0          stop for independent audit; no automatic RH claim
all gates pass             close N1 at notes-grade candidate scope only
```

Passing N1 creates no `A_J`, `B_J`, or J-native moment functional.  It does
not promote the sibling S2 candidate, register a public claim, change the
Canon, or prove RH.  The next genuinely new finite q-moment gate remains the
shifted 2x2 determinant requiring `sigma_4`.
