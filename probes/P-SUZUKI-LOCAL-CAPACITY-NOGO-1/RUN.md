# RUN P-SUZUKI-LOCAL-CAPACITY-NOGO-1

## Immutable pin

```text
pin_commit: dec24ca9b50a9863180c444a1f0aa87cef753175
prereg_sha256: c503fc2a62cdb50ddbc536751bd618d84d00926652846dc9059005cbf84fe859
prereg_bytes: 18774
prereg_blob: 42ff82893ff9670d69e80d30946238263f573c86
verifier_sha256: c68381aff92bd6b01d2170e40d1d82da909f7ec11c3f597516da8c1c1e128ddb
verifier_bytes: 13554
verifier_blob: 702979b0025f5ec96deddf591b34e538b5d9d5b2
expected_sha256: ad99e73f827fbc075342d93fbc8e840c05cba8764c99b5c26bedf37b46050a84
expected_bytes: 1054
expected_blob: 5720d24bf69cb8786ceb1f3d99f662be96828bb0
```

The public branch readback resolved to the full pin commit before execution.
The pin contains exactly `PREREG.md`, `verify.py`, and `EXPECTED.txt`; all
three Git blob identities above are from that commit. The verifier is byte
identical to the frozen candidate verifier at
`notes/c-suzuki-local-capacity-nogo-1` commit `f0f2a8c0`, and
`EXPECTED.txt` equals the frozen candidate stdout recorded there, per the
disclosures in `PREREG.md`.

## Claim issue

The claim issue could not be opened before the pin because the executing
session holds repository push access and no API credential; the exception
and the collision scan are disclosed in `PREREG.md`. The claim issue is
https://github.com/mathorn1973/twist-j/issues/399, opened post-pin under
that exception on 2026-08-17.

## Command

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1/verify.py
```

Machine-readable command field:

```text
command: python3 probes/P-SUZUKI-LOCAL-CAPACITY-NOGO-1/verify.py
```

## Local leg record

```text
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: Python 3.12.3
start_utc: 2026-08-17T10:29:04.256993479Z
finish_utc: 2026-08-17T10:29:04.660419118Z
wall_seconds: 0.40
deterministic_executions: 1
pre_status_bytes: 0
post_status_bytes: 0
exit_code: 0
stdout_sha256: ad99e73f827fbc075342d93fbc8e840c05cba8764c99b5c26bedf37b46050a84
stdout_bytes: 1054
stdout_lines: 14
stdout_cr: 0
stdout_final_byte: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
checks: 12 of 12 PASS
verdict: SURVIVED
```

The checkout was clean immediately before and after the single execution.
`EXPECTED.txt` is the exact raw stdout, with LF line endings and a final LF;
stderr is empty. The verifier uses exact integer and Fraction arithmetic
with outward-rounded scaled-integer intervals only; the written universal
statements of `PREREG.md` are carried by their proofs, not by this finite
audit. The local stdout equals the frozen candidate stdout recorded on
2026-08-17 in the pin, so the frozen x86_64 record of 2026-08-13 and this
aarch64 leg already exhibit cross-architecture byte identity of the same
verifier bytes.

## Pending GitHub leg

The required GitHub architecture check (x86_64, complementary to the local
leg) runs at pull-request time. Its machine fields are to be recorded in
this section after the check completes; until then the verifier
reproduction check reports the missing GitHub leg, which is the expected
pre-finalization state.
