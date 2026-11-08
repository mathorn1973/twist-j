# First formal run

pin_commit: 04e21ecf4a866cd861d875706050006e0d0fbd59
verifier_sha256: 95541c29f9c92cd281576a7d95bdaecb6be692def8a1f6c8df2866569f7cb28c
command: python3 probes/P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3/verify.py
platform: Windows-11-10.0.26300-SP0
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: 3215cd17cfd2db24744de14bfbfd5b4065ab293e9a2a7a8df03750a90664ffbc
stdout_bytes: 499
stdout_lines: 17
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The first execution followed the public six-file readback receipt on issue
#1669 (comment 6286325093), itself read back before execution. The checkout
was clean at the exact pin `04e21ecf4a866cd861d875706050006e0d0fbd59`. All
public bytes and Git blob IDs matched the local frozen files. Before that
receipt, neither `verify.py` nor `breaker.py` of this pin had been executed.

The primary invoked its independently implemented frozen breaker using the
same interpreter with `-I` and a 540-second timeout. It required exit zero,
empty stderr, and byte-equality of the 15-line raw certificate output.
`LC_ALL=C`, `LANG=C`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0`, and
`TZ=UTC` were set. `EXPECTED.txt` is an exact byte copy of captured stdout.
None of the six frozen files changed.
