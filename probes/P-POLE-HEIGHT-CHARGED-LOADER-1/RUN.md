# First pinned Linux run

NON-CANONICAL / L1 / completed bounded exact search; no loader found.

pin_commit: d01c2ff5e9c2a4b339979fd14edde310e81debfd
verifier_sha256: 5855dec65533917ae67c268b3f7f033b11ed8c5eb8e106fd9b3341e4deb46de4
command: python3 probes/P-POLE-HEIGHT-CHARGED-LOADER-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: d72e632ced1e8b06f1c2821b83b7217578235b99949f9f9e358a60a202b15926
stdout_bytes: 6640
stdout_lines: 47
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All six immutable sources were publicly read back byte for byte and by
Git blob before the first execution. A clean Linux clone fetched this
exact pin, verified all six source hashes and remained clean afterwards.
This was the first scientific execution of the probe. No failed attempt,
retry or source/threshold change occurred.

Assertions were enabled. The environment set LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC; inherited
PYTHONOPTIMIZE, PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR
were removed. The execution limit remained 600 seconds. Measured wall
duration was approximately 12.894 seconds, operational metadata only.

## Pinned source custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 10232 | `fafa7a0ff444446e294ba088830adfa31121218e212cc3c73a8cba8c4d57534d` |
| PROOF.md | 8951 | `22fad7854b981e3e119781601d1d3fc5f66d593ba079edc828ed3b487f0376a3` |
| PROVENANCE.md | 2281 | `398f11a8a19690bc3d65297c57a5a0b6f384277bb4f99c1f4fa109515e5ab906` |
| README.md | 1989 | `4552c64a31fe4734e031ff13832bfb0818c82892019c12dbddfe3df2f37da4f7` |
| SOURCES.tsv | 2565 | `d9e7b8832f80fa46323f26c1d3b5771a9e59c01a94970bb3a4d22a6d604a04a4` |
| verify.py | 22620 | `5855dec65533917ae67c268b3f7f033b11ed8c5eb8e106fd9b3341e4deb46de4` |

This is the actual author Linux x86_64 run. Required GitHub x86_64 and
aarch64 results are reported only after their jobs complete. Same-session
static review is not independent scientific acceptance.
