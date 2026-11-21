# First pinned Linux run

NON-CANONICAL / L1 / exposure-disclosed exact audit.

pin_commit: 85678ffbee93f4468d3564f8f284cfcd981fdc6d
verifier_sha256: 70287075d859a455cf69bc1b01b5a23cdfdf35b3df46e7ad0b93aebe597471d1
command: python3 probes/P-NEUTRAL-RING-LATCHED-RECEIVER-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 820befea266e72b7a4284e714bbe853b4504bf60991a744ecc4e9932c5cd3291
stdout_bytes: 1012
stdout_lines: 37
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The six scientific sources were publicly read back byte for byte before
the first execution. A clean Linux clone fetched and checked out the exact
pin, verified all six hashes, and stayed clean after the run. This was the
first scientific execution, with no failed attempt or retry. No source or
threshold changed after the pin.

Assertions were enabled. The environment set LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC, and removed
PYTHONOPTIMIZE, PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR.
The unchanged execution limit was 600 seconds. Measured wall duration was
approximately 2.785 seconds, operational metadata rather than physical time.

## Pinned source custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 9034 | `99499bd236c5d3b2f4b8977a1e3322a0de4bc8fcd40749764664ddc29bbb084c` |
| PROOF.md | 14857 | `d2dab0bf6dedd7c17375516ad00af86a60402e61125d17bcab2beba108a0585e` |
| PROVENANCE.md | 2000 | `fa93fb9a5090ff19f82e060e1f5a1921e56bb13bd5cdf53cbe36dcae4d0e2103` |
| README.md | 1816 | `be9a7216bd1b1767aa2fcb85d2d67b8ae39c53c294705101ef1abb7c781ded9b` |
| SOURCES.tsv | 1364 | `80a0b1ed7aba18c89616a6bede44cacaef22327bb2072d7f9e6afc1396ce30f6` |
| verify.py | 9937 | `70287075d859a455cf69bc1b01b5a23cdfdf35b3df46e7ad0b93aebe597471d1` |

This records the actual first Linux x86_64 run. Required GitHub x86_64
and aarch64 replay results are reported only after those jobs complete.
A same-session analytical review is not independent acceptance.
