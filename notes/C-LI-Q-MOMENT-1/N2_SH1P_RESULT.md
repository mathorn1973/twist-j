# C-LI-Q-MOMENT-1 / N2 result. Sigma_4 and shifted SH-1'

```text
STATUS:       N2 CLOSED at notes-grade candidate scope.
AUTHORITY:    none. NON-CANONICAL, NON-FORMAL.
PUBLIC STATE: unchanged; no issue, probe, registry row, Canon edit, tag,
              release, or RH claim.
```

## 1. Frozen basis

The first execution occurred only after the following immutable sequence:

```text
base                   d94d4a94976a9b5d27db3a1c586e4886697daabb
verifier commit        132538257e2671e50393d0f3fae42a101b47b3aa
verifier SHA-256       fc86ec75f31cd2884c6dffa36ba0068e778faebc06cf0c70aaae0ae3f6e80300
verifier bytes         17534
freeze commit          58ed100 (pin record normalized before execution)
equation               SH-1' = qw_1 qw_3 - qw_2^2
precision              scale 10^24; N=200000; 32 log terms
gamma_3 width ceiling  1e-17
```

The verifier commit is a direct child of Public Canon v8.  The later freeze
commits change only the candidate explanation, pin record, and manifest; the
verifier bytes were not amended after their commit.  `N2_SH1P_PIN.md` is the
binding pre-run record.

## 2. First run and deterministic replay

Neutral environment:

```text
platform          Windows 11
architecture      x86_64
python            CPython 3.12.13
LC_ALL/LANG       C/C
PYTHONHASHSEED    0
TZ                UTC
command           python -B notes/C-LI-Q-MOMENT-1/verify_q_moment_n2.py
```

The first captured run and two immediate replays returned the same byte
stream:

```text
exit_code       0
stderr_bytes    0
stderr_sha256   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stdout_bytes    2034
stdout_lines    29
stdout_sha256   743c0886225489f16e0fa03bb74108f8d444303739520b83f3947ccc1d807a9f
assertions      9 PASS, 0 FAIL
```

The exact stream is `stdout_q_moment_n2.txt`.

## 3. Exact derivation and refreshed constants

The symbolic gate independently expands the frozen Stieltjes series and
proves

```text
sigma_4 = 1 + gamma^4 + 4 gamma^2 gamma_1 + 2 gamma_1^2
          + 2 gamma gamma_2 + (2/3) gamma_3 - pi^4/96.
```

In particular, the pre-freeze shorthand suggesting a `gamma*zeta(3)` term
was corrected: no such term survives in `sigma_4`.  The full determinant
still reads `zeta(3)` through `sigma_3`.

The common B4 calculation produced

```text
gamma_3 in
[0.002053834420303343805534,
 0.002053834420303347765456]

width = 0.000000000000000003959922 < 1e-17.
```

The resulting fourth zero-power sum is

```text
sigma_4 in
[0.000073627221261687555177,
 0.000073627221261691351731].
```

The refreshed `sigma_1,...,sigma_3` intervals all lie inside their frozen N1
comparators.

## 4. N2 decision and third ladder junction

The new moment is strictly positive:

```text
qw_3 in
[0.000000000659827686284693,
 0.000000000659828142527711].
```

Both frozen interval graphs decide the shifted determinant positively:

```text
direct qw graph:
[0.000000000000003836699546,
 0.000000000000003836716508]

antisymmetric T_3 block graph:
[0.000000000000003836691348,
 0.000000000000003836724705].
```

The intervals overlap.  Exact polynomial algebra proves before evaluation
that both graphs equal

```text
SH-1' = qw_1 qw_3 - qw_2^2
      = det(T_3 antisymmetric block).
```

This is the third exact Hankel--Toeplitz ladder junction.  It decides one
`2 by 2` block under the reversal decomposition of `T_3`; the complementary
block is not evaluated here, so full `T_3` positivity is not claimed.

## 5. Boundary and next constructive gate

```text
N1                                CLOSED at notes-grade candidate scope
N2                                CLOSED at notes-grade candidate scope
J-LI-Q-CALIBRATION-LADDER         unregistered
J-LI-Q-MOMENT-REALIZATION         O
P-J-LI-S2-RELATIVE-DETERMINANT-1  BLOCKED-ON-CONCRETE-A_J
RH                                O
```

N2 is a reference-side calibration.  It does not construct `A_J`, `B_J`, a
positive moment functional, or a relative determinant.  Further finite
prefixes alone do not cross the all-order wall.  The next constructive task
is therefore the separately frozen route RA: define a concrete J-native
parent pair and test its G0--G3 dependency, trace-class, normalization, and
positivity gates before comparing it with N1 or N2.

## 6. Independent aarch64 readback

A fresh Ubuntu 24.04/aarch64 clone at exact commit
`a002e72481b8cf74fc95e51411bf3c9ead29cda3` verified the folder manifest and
ran the pinned verifier three times under the neutral environment.  All three
runs returned exit zero, empty stderr, and the same 2034-byte stdout SHA-256
`743c0886225489f16e0fa03bb74108f8d444303739520b83f3947ccc1d807a9f`.
They were byte-identical to the Windows 11/x86_64 first-run record.  Policy,
38 tool tests, Canon v8, and the ledger also passed in that fresh clone.

The neutral record is `N2_AARCH64_READBACK.md`.  This independent
two-architecture agreement strengthens the notes result but is not a formal
public-probe promotion gate.
