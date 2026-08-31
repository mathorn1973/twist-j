# Run record

Probe: `P-FCC-WEIGHTED-SHELL-REMAINDER-1`

```text
pin_commit: 27724dadd0be26682077e0391595fbef93bd3a53
verifier_sha256: 9cf242aeecdd5ae1d1fef3bf80b3a12dd37b01648988f4eaf4fae62eb80452b6
command: python3 probes/P-FCC-WEIGHTED-SHELL-REMAINDER-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: d6ca49f59e1f634251db3095565c9f6d4a5e38ddd4d44ebf259a03b676d8279f
stdout_bytes: 1004
stdout_lines: 20
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
pin_parent: cff4c896cbbaf63ebeeec5cf4f50c6fb57b64414
prereg_sha256: a725bac783da95a6e06c0797dd6c73acbf792b4d24265c242fbc72dd7fff69e0
prereg_bytes: 18321
prereg_blob: 81d98317802dc29fdd10cf5cf34abdeac8765937
verify_bytes: 15691
verify_blob: 5c41fbbc63ac058bcf362286a6c244200c322d35
expected_sha256: d6ca49f59e1f634251db3095565c9f6d4a5e38ddd4d44ebf259a03b676d8279f
public_claim_lock: issue 710
formal_date: 2026-08-30
started_utc: 2026-08-30T21:49:06.095982+00:00
```

The complete PREREG and accepted verifier were committed and pushed before
any formal execution. A separate Linux checkout fetched that public pin,
confirmed its single parent, clean state, exact file hashes and blob byte
equality, and Public Canon v72 ancestry and content hash. The pin and file
receipts were publicly recorded under issue #710 before the run.

The accepted verifier was then executed once from that clean pinned
repository root. Raw stdout and stderr were captured separately. EXPECTED.txt
is the entire actual stdout: 1004 ASCII bytes, 20 LF-terminated lines.
Stderr was empty and the repository remained clean after execution.
Neither pinned file was changed to obtain this output.

This recorded run is one aarch64 lane. The independent written proof in
PREREG establishes the universal real-variable conclusions; the verifier
audits its finite exact certificates. Required PR acceptance additionally
reruns the exact head on x86_64 and aarch64 and compares the same committed
EXPECTED.txt byte for byte. No machine nickname, private execution path or
third-party source bytes form part of this record.
