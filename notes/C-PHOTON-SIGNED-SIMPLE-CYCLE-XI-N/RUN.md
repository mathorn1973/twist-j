# RUN

**PUBLIC, NON-CANONICAL. candidate-C finite audit only.**
Owner: #1176
Author: A. M. Thorn
Date: 26 September 2026

## Frozen input

Candidate pin:

`c74c6e56801bd508153b75522b294b9a22340bc7`

GitHub readback before execution:

- `PREREG.md`
  - Git blob: `ca127419ed0c15da9741808e4c9b6addece61fdb`
  - SHA-256: `618535cf6d86e967731a20623c2602657f8e09fbfe437925197278f3829063ae`
- `verify.py`
  - Git blob: `0a3a37d9c8217c3803940e0a0beff81991a5adb2`
  - SHA-256: `b3f864df08b8b74baa104978bcd7f235d22f9c148ca9de2ad60a32062986852f`

## Environment

```text
platform: Linux
architecture: x86_64
python: 3.13.5
```

One architecture only. No two-architecture scientific gate is claimed.

## Command

```text
python3 verify.py
```

## Result

```text
exit_code: 0
stdout_bytes: 623
stderr_bytes: 0
stdout_sha256: 309924aad1069eaf72e824a9067ae6aa4c7a1ddb31a9b32e673aa0f0fb34344a
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Exact stdout:

```text
CONSTANTS PASS A=374125/1240029 q=2472875/2480058 A0=51250/177147 q0=169375/177147
SERIES_IDENTITY PASS coefficients_m1_to_20=cubes
SERIES_IDENTITY PASS coefficients_m1_to_20=cubes
CYCLE_AUDIT PASS total=162 equality_cases=15 m4=1 m6=2 m8=7 m10=28 m12=124
RECTANGLES PASS count=36 exact_ell_equals_area
BOUND_CONTACT12 PASS C12=19289287085600601415245438839426542724609375/48127709445264405068802290089074432
BOUND_CONTACT0 PASS C0=84154245507509267755507354736328125/12019566150064311590964767330304
BOUND_DIGITS C12_num=44 C12_den=35 C0_num=35 C0_den=32
AUDIT PASS; signed_single_cycle_uniform=YES; full_Xi=OPEN; P1=OPEN
```

Stderr is empty.
