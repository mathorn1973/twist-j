# C-LI-Q-MOMENT-1 / N1 result. Fresh gamma_2 width and SH-1 = Q

```text
STATUS:          NON-CANONICAL NOTES-GRADE RESULT
PUBLIC CLAIMS:   none
DATE_UTC:        2026-07-17T09:16:44Z
PIN_COMMIT:      1799c1887055d77b213bdee777b154950219f021
RH:              O
```

The N1 run passed every frozen gate.  It closes N1 only at notes-grade
candidate scope: the second Stieltjes constant is enclosed at the requested
width, the exact determinant junction `SH-1 = Q` is machine-pinned, and both
rigorous interval evaluation graphs are strictly positive and consistent
with the historical `Q` certificate.

## 1. Frozen source and environment

```text
verify_q_moment_n1.py
  sha256  9b5fc0e18eda719ca8d63ce3626e449d3d0c7859288d4ba361f550ba502df486
  bytes   12947
  lines   420

platform       Microsoft Windows NT 10.0.26200.0
architecture   AMD64
python         3.12.13
```

The neutral environment and command were the pinned values:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
python -B notes/C-LI-Q-MOMENT-1/verify_q_moment_n1.py
```

Immediately before process creation, local `HEAD` and the fetched remote tip
both equalled the pin commit, the worktree was clean, and the verifier hash
equalled the frozen source hash.  Earlier preflight/launcher failures stopped
before any Python process was created and produced no verifier output.  The
first actual verifier process is the run recorded here; the pinned verifier
was not rerun afterward.

## 2. Execution record

```text
exit_code       0
stderr_bytes    0
stderr_sha256   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stdout_bytes    1537
stdout_lines    26
stdout_sha256   11904f3ca3058ca617ea01c769a622fea226081d235d604d31b38be28fb002af
assertions      10 PASS, 0 FAIL
```

The exact captured stdout is `stdout_q_moment_n1.txt` in this directory.

## 3. Certified intervals

At scale `10^24`, with `N=200000` and `LOG_TERMS=32`, the fresh `B_2`
Euler--Maclaurin enclosure is

```text
gamma_2 in
[-0.009690363452405785691059,
 -0.009690362933338851294461]

width = 0.000000000519066934396598 < 0.000000001.
```

The first three pole power sums and q moments relevant to N1 are

```text
sigma_1 = qw_0 in
[0.023095708965079367097561,
 0.023095708971329335948397]

sigma_2 in
[-0.046154317344901637723149,
 -0.046154317237087378863919]

sigma_3 in
[-0.000111158665537209572582,
 -0.000111157790857999161284]

qw_1 in
[0.000037100585257096471973,
 0.000037100705571293032875]

qw_2 in
[0.000000143090234079843337,
 0.000000144325855879937341].
```

The direct and reduced interval graphs give

```text
SH-1 direct in
[0.000000001928308048165368,
 0.000000001956854538021970]

SH-1 = Q normal form in
[0.000000001925826928889160,
 0.000000001959335657298853].
```

Both lower bounds are strictly positive.  The intervals overlap, and the
reduced interval lies inside the historical two-architecture pin

```text
Q in
[0.000000001883563636456191,
 0.000000001989968490233267].
```

The fresh `qw_0` and `qw_1` intervals are also contained in the previously
frozen `lambda_1` and `M_1` intervals, respectively.

## 4. Exact interpretation

The symbolic gate proves before interval arithmetic that

```text
SH-1 = qw_0 qw_2 - qw_1^2
     = 2 sigma_1^2 - sigma_1 sigma_2
       + sigma_1 sigma_3 - sigma_2^2
     = Q,

det T_2 = 2(2 sigma_1 + sigma_2 - sigma_3) SH-1.
```

Thus the radial Hankel ladder and angular Toeplitz ladder meet not only at
`qw_0=lambda_1` and `qw_1=M_1`, but also at their first nontrivial determinant
invariant.  The fresh run refines the width and audits that transfer; it does
not create the positivity, which was already present in the historical `Q`
pin.

## 5. Boundary and next gate

```text
N1                               CLOSED at notes-grade candidate scope
J-LI-Q-CALIBRATION-LADDER        unregistered
J-LI-Q-MOMENT-REALIZATION        O
RH                                O
```

No J-native `A_J`, `B_J`, or positive moment functional is constructed.  No
Canon, registry, public probe, or normative status changes.  No finite
Hankel/Toeplitz prefix proves RH.  The next genuinely new finite q-moment gate
is the shifted 2x2 determinant `qw_1 qw_3-qw_2^2`, which first requires a
separately derived and frozen `sigma_4`.
