# First completed pinned run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, 2026-10-18.
SPDX-License-Identifier: Apache-2.0.

The fields below record the first scientific execution, after public pinning
and exact public readback. The scientific outcome is recorded in RESULT.md.

pin_commit: 3c4855829770229b87d6c86740a215f78b213056
prereg_sha256: 9d577a850c55928de789546a774436b6c7ef7c38bcf9ddccf957d4df8b3afa11
verifier_sha256: 6e7bbc45db3ada142466662836ec2a20c40c9d5232d7f92783a2a6030738f21c
independent_sha256: e03c31b5d07294c8f1e4e35f186824ea6d1d38160d8e6d62965e3a48e2458f4d
domain_sha256: 2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0
proof_sha256: 7ab8edf5e3eb225ed984cfdf74116b7a4821d78dea1ca307587045de0c8f1184
command: python3 probes/P-EVEN-CONTACT-3ADIC-TEST-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: CPython 3.12.14
started_utc: 2026-10-18T09:43:58+00:00
finished_utc: 2026-10-18T09:44:00+00:00
elapsed_seconds: 1.422278
timeout_seconds: 600
exit_code: 0
stdout_sha256: 92b0c3fefdc0b4e24c1ea4532057adef7bf8a8654e288ec7cb07d47fe79208ce
stdout_bytes: 5210
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1

## Public custody

- Public claim: https://github.com/mathorn1973/twist-j/issues/1603#issuecomment-6248306355
- Public pin: https://github.com/mathorn1973/twist-j/commit/3c4855829770229b87d6c86740a215f78b213056
- Pin tree: 19af81673acf06e7a8b874d85077696ed3044150
- Sole parent: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
- Public author and committer: A. M. Thorn <221838986+mathorn1973@users.noreply.github.com>
- Public commit time: 2026-10-18T09:41:31Z

Before started_utc, the public branch was read back at this pin, each of the
eight accepted files was fetched by the exact commit and compared byte for
byte, and the public Git commit was fetched into the local repository.
Its tree and sole parent matched the staged accepted tree. The local
worktree was clean at the pin before execution and remained clean afterward.
Every pinned file retained its hash. No earlier scientific run, import or
benchmark was performed.

EXPECTED.txt is the first stdout copied without reserialization. It includes
the complete 705-by-2 image and the deterministic rank certificate. The
scientific exit code is zero, stderr has zero bytes, and the run completed
within the frozen 600-second limit. The public connector identity uses the
previously documented owner approval cited in PREREG.md.

## Accepted file custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| DOMAIN.tsv | 5029 | 2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 |
| PREREG.md | 10096 | 9d577a850c55928de789546a774436b6c7ef7c38bcf9ddccf957d4df8b3afa11 |
| PROOF.md | 11256 | 7ab8edf5e3eb225ed984cfdf74116b7a4821d78dea1ca307587045de0c8f1184 |
| README.md | 3811 | 73e36963fbdaf28125a8912d26cbd4bda980263b0068bdd41c680da05a4adfee |
| REVIEW.md | 5684 | ff8af7da03358402a3732a2a40530d096e1508d969dbcc3a376c1c14015437c4 |
| SOURCES.tsv | 600 | 0e796302aea3e377d30acaacac57fba8252f4a56151421896f101e023e8f4faf |
| check_independent.py | 4369 | e03c31b5d07294c8f1e4e35f186824ea6d1d38160d8e6d62965e3a48e2458f4d |
| verify.py | 10025 | 6e7bbc45db3ada142466662836ec2a20c40c9d5232d7f92783a2a6030738f21c |

## Required public replay

The existing PR workflow reruns this same verifier and its byte-pinned
companion/domain with Python 3.12 on x86_64 and aarch64, comparing against
this one EXPECTED.txt. This first-run record does not predeclare the
outcome of those later jobs. Their exact-head evidence is reported in the
PR checks; a same-architecture local repeat is not a second architecture.
