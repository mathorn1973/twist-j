# Exact execution

The [public readback](https://github.com/mathorn1973/twist-j/issues/2029#issuecomment-6984656155) covers all thirteen frozen files. The public H3 source was verified by SHA-256 before importing it. The reference data for the two old receiver cuts were extracted from the pinned #2028 output.

```text
pin_commit: 6b60135506f4c25d63bec249740e0774d2019eb2
command: python3 probes/P-H3-PHASE-CURRENT-REST-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: b793d84b1db2bfb5b7635f8b89efa336837a4511e9f95a9dd9a724f292a12c8a
started_utc: 2026-11-18T16:27:30.231846+00:00
ended_utc: 2026-11-18T16:27:35.170380+00:00
exit_code: 0
stdout_bytes: 4516
stdout_lines: 7
stdout_sha256: 96a0e7fc5cb53a7284fae26929aac08237b02197453fe89524d73e457087e4e3
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

[EXPECTED.txt](EXPECTED.txt) contains seven deterministic JSON records. The local calculation used the Python standard library and exact integer or rational arithmetic. Same-session algebraic and code checks are part of this work.
