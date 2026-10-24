# RUN

**PUBLIC, NON-CANONICAL. candidate-C finite audit only.**
Owner: #1179
Author: A. M. Thorn
Date: 26 September 2026

## Frozen input

Candidate pin:

`af41b8321c83e0ce815005cb96f30a4ff18a5001`

GitHub readback before execution:

- `PREREG.md`
  - Git blob: `1267336f06787af36e98bc969d48c441474886aa`
  - SHA-256: `abdc04dd45f99d6544e50591f4b1c1eba723a1699d0e290db1b903f0a1f9bf23`
- `verify.py`
  - Git blob: `3c337654f3bdabc371fde57df77da745d07041cc`
  - SHA-256: `f72a7d86cd189a2f57bedd4ebb243b36800442c373ced5c8126e9b964ede38ea`

## Environment

```text
platform: Linux
architecture: x86_64
python: 3.13.5
```

One architecture only. No two-architecture scientific gate is claimed.

## Result

```text
exit_code: 0
stdout_bytes: 657
stderr_bytes: 0
stdout_sha256: 21f0271bf19e2c3a6ab6d9a21bca64ff22d3524352b9a48434d1fc6c1369182b
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Exact stdout:

```text
CONSTANTS PASS a=15625/177147 r=41/25 s=9/25 tau=73/70 q0=169375/177147 A=374125/1240029 q=2472875/2480058
IMPLICATION_AUDIT PASS finite_cases=18707
WITNESS PASS m=10 Oplus=2 Ominus=1 O=3 signed_factor=15129/15625 tau_power=4297625829703557649/2824752490000000000
CONTACT_1 (((0, 0, 0), 0), 1, ((0, 0, 1), 0), -1, ((0, 0, 0), 0, 2), '+')
CONTACT_2 (((0, 0, 0), 0), 1, ((0, 1, 0), 0), 1, ((0, 0, 0), 0, 1), '-')
CONTACT_3 (((0, 1, 0), 0), 1, ((0, 1, -1), 0), -1, ((0, 1, -1), 0, 2), '+')
BOUND PASS C_SC=19289287085600601415245438839426542724609375/48127709445264405068802290089074432
AUDIT PASS; signed_contact_class=STRICT_EXTENSION; full_Xi=OPEN; P1=OPEN
```

Stderr is empty.
