# P-J-BINARY-NORM-DESCENT-1 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed only
by the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.
This local x86_64 leg is not by itself a two-architecture gate.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 846f116b817284c688235bbea729cd9a9cd1f20f
verifier_sha256: 6f10ad20cada339372e3d76417ff558386948967975c2eb7ebd19747e0858ea6
command: python3 probes/P-J-BINARY-NORM-DESCENT-1/verify.py
platform: Debian 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: bdeb9a20fe8c436b4f788fb637894113317610e450abb127fc3646210ee4d500
stdout_bytes: 1604
stdout_lines: 27
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 1b288cbed5a9ccdfed5edde906df82fa1522870e
root_tree: 0450c3b3bbe01738a145b4e0e33cf194035b29d4
probe_tree: 0946bfb17c47afb86b5b28ea575961b6d4f78c18
prereg_sha256: a023d6c83813b7b8b37472e99ad4e4ddb1314a6fa0f5b7a0c0090d8b18a6d7b5
prereg_bytes: 14276
prereg_lines: 474
prereg_blob: ca9110cfa3cbb2dba2e05252ab7ae271906c4c2c
verify_bytes: 13714
verify_lines: 427
verify_blob: bfd38eb834eecb873dece5fed03193e4149bf0a6
claim_lock: issue 499
```

The execution environment could not make a network `git clone`, so the exact
pin was materialized sparsely from public GitHub Git-object readback rather
than approximated from a local copy. This is an exact-pin checkout surface, not
a substitute commit: the two remote blobs were read back; their local Git blob
IDs and SHA-256 values matched; the probe subtree was reconstructed as
`0946bfb17c47afb86b5b28ea575961b6d4f78c18`; the public root tree was
reconstructed as `0450c3b3bbe01738a145b4e0e33cf194035b29d4`; and the unsigned
commit object reconstructed from the public metadata hashed exactly to
`846f116b817284c688235bbea729cd9a9cd1f20f`. `HEAD` was set to that exact
commit. The execution surface contained only the two pinned probe files, the
index held their exact remote blob IDs, and `git diff-files --quiet` passed
after refresh.

The verifier reads no repository file, external input or environment value.
It was executed exactly once after this readback, from the repository root of
the sparse exact-pin surface, with the inherited process environment plus:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

`EXPECTED.txt` is the complete raw stdout with LF endings and a final LF. The
process wrote zero stderr bytes and exited zero. The verifier was not rerun and
no byte of either pinned file was modified by the run.

## Accepted local result

```text
checks: 20/20 PASS
decision: J-BINARY-NORM-DESCENT-CONFIRMED
field: O/(2) = F16; Frobenius^2 fixed field = F4
action: D_J mod 2 is multiplication by alpha^2 and acts as k->k+2 on mu5;
        Frobenius acts as k->2k; the two maps are unequal and generate AGL1(F5)
form: q_+ mod 2 = Trace_F4/F2 o Norm_F16/F4
singular_locus: the five nonzero q_2-singular elements are exactly mu5
bridge: P mod 2 identifies q_2 with the registered A4 carry form q_A
scope: L1 only; no Boolean selection, Thue-Morse, Born, decoder, apparatus,
       sampling, measure or L2-L6 lift
```
