# Formal run record

NON-CANONICAL / L1. First execution from the clean public source pin.

pin_commit: 43fe4fef2cff6952cf753df888bb7b1928dd744d
verifier_sha256: 33b9ba6232277c579cef1db99ce5115d397c056e10d6d9844b94a76fc0943a3a
command: python3 probes/P-OVERLAPPING-CONTACT-WORK-CLOCK-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 97c61a91ec2d6d3c06045d2da9c78ade30455ccbef9bac0036644bb93181ffbc
stdout_bytes: 3304
stdout_lines: 15
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All five source files were committed, pushed and fetched through their
immutable public contents before the first scientific execution or import.
Each public byte sequence, Git blob and SHA-256 matched the local source.
Issue #1914 records the prospective pin. Before pinning there was static
proof/code inspection and AST parsing only. The source-pin checkout was
clean before and after the first execution.

Assertions were enabled. LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1. The first run took approximately 20.190 seconds,
an engineering measurement rather than a scientific threshold. It exited
zero with empty stderr. EXPECTED.txt is its exact stdout. There was no
failed scientific run, retry, source adjustment or threshold change.

| Source | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 8532 | 689e235c75a23029c22ccb8b764a7974daf4fef420472823fcad120383ef2a4d |
| PROOF.md | 19090 | 83c42659cf08e35124403f650ba789a81ae12bbcfee256da6c290c7c84a5f4d3 |
| PROVENANCE.md | 2342 | 02068d4d763dd3d43d9019ab20cf231952e5775d2572629090d522d9a426791d |
| checker.py | 5751 | 3db7f8389fef4189631cbca38d8fa99c81ba64acb26c1a11f6ab3cc30173fe78 |
| verify.py | 23408 | 33b9ba6232277c579cef1db99ce5115d397c056e10d6d9844b94a76fc0943a3a |

Only EXPECTED.txt, RUN.md and RESULT.md are appended after the source pin.
The required x86_64/aarch64 workflow must reproduce the unchanged verifier
against these same bytes. Its actual job logs, rather than this local
record, provide the second-architecture evidence.
