# P-J-BINARY-NORM-INDEX-1 formal run record

Date: 2026-08-22

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 815d99ea85697bc9b4742b6036126ae8058d47e2
verifier_sha256: 93b1364ddcf76e605be37b9fc4f2163655738ef420e9585d5ce0af73507008f0
command: python3 probes/P-J-BINARY-NORM-INDEX-1/verify.py
platform: macOS 26.5
architecture: aarch64
python: CPython 3.13.13
exit_code: 0
stdout_sha256: 0cbdc63635ba19f9d7ea03e4dcbd4448d1791b5ad38c8238e6c36ccd90d4403f
stdout_bytes: 2747
stdout_lines: 28
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The recorded architecture is the Armv8-A 64-bit instruction set. The host
kernel names it `arm64`; the repository and the GitHub aarch64 runner name the
same architecture `aarch64`, and the required field uses the repository name.
The local declaration is audit metadata; the gate rests on byte identity
against the one committed `EXPECTED.txt`, which any reader can recheck.

## Pin audit

```text
parent_commit: 41754210a3a0e70b52f98988e566a73bba9b9666
prereg_sha256: e5c58dea7e3e8538c396aa9cc7a6333e06a55cce3b514055e1ef001b2d152a17
prereg_bytes: 13870
prereg_lines: 308
prereg_blob: 3bb6f993012f48f2d00802a4db7546bf61035f3b
verify_bytes: 9823
verify_lines: 281
verify_blob: b8c7548ec0609d4bb806c6c8bb5412d75f6df840
public_pin_comment: issue 522 comment 5381178264
```

Both accepted files were committed together and pushed before any formal
execution, then fetched from the public remote into a separate clean checkout
and read back there before execution. Their Git object identifiers, SHA-256
values, byte counts, LF endings, final LF and ASCII decoding matched the
accepted bytes. The read-back worktree was clean at `815d99ea` with no
untracked file. Static parsing and syntax compilation passed before the pin;
the accepted file was not imported or executed before it.

The accepted verifier was executed exactly once, from the repository root of
that clean public checkout. It began at `2026-08-22T15:31:25Z` and finished
within the same second, far inside the preregistered 120 second limit. The
interpreter was started from an emptied environment carrying only:

```text
PATH=/opt/homebrew/bin:/usr/bin:/bin
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

`EXPECTED.txt` is the complete raw stdout with LF endings and a final LF. The
process wrote zero stderr bytes and exited zero. The verifier was not rerun,
and no byte of the pinned tree was modified by the run.

## Accepted run

```text
checks: 20/20 PASS
decision: J-BINARY-NORM-INDEX-CONFIRMED
index: the norm-one subgroup of F_(p^4)^x has order (p+1)(p^2+1) and index p-1
uniqueness: p = 2 is the only inert prime where that subgroup is the whole
          group, and the only one in range where ord(Jbar) = p^4 - 1
attainment: ord(Jbar) = 15 = |F_16^x| at p = 2, by exhaustion over 1 to 15
routes: the Frobenius product and the exponent path both return one and agree
          at every inert prime below 300
genericity: the index is p - 1 in degrees 2, 3, 4, 6 and 8 alike
galois: 1 + x, 1 + x^2, 1 + x^3, 1 + x^4 are J, J^2, J^4, J^8, all of order
          fifteen, so the attainment selects no exponent
census: full norm-one generation exactly at p = 2 and p = 3 among the 156
          inert primes below 2000
controls: zeta_5 has norm one and order five at p = 2; w = 2 + zeta_5 has
          residue norm 11 mod p, which is 2 at p = 3
global_scope: L1 only; no selector, no apparatus, no instrument, no event, no
          measure; SAMPLING NOT PROVIDED
```
