# First pinned Linux replay

NON-CANONICAL / L1 / exposed-result formal publication replay.

pin_commit: aaf3ec7e925c2c0261604179ee4166d542233e14
verifier_sha256: d9968f83bf2827f0849e65b65cb00876571d4ea3f262214c65a5362dab5d8fa5
command: python3 probes/P-NATIVE-RECEIVER-CARRY-MIRROR-1/verify.py
platform: Ubuntu 24.04, Linux WSL2
architecture: x86_64
python: 3.12.3
exit_code: 0
stdout_sha256: 085d8c3dd70a9443e560440f9a4b1d70c9e66bec50b57dfdc7724ae120f8ad50
stdout_bytes: 2479
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All seven scientific source files were committed, pushed and fetched through
their immutable public GitHub URLs before the first execution. Every public
byte sequence matched the prepared SHA-256. The clean Linux checkout fetched
that exact public pin and rechecked every source length and hash before
execution. It remained clean afterward. No scientific source or threshold
changed after the pin. The first formal execution completed successfully;
there was no failed scientific attempt or retry.

The prior attachment's results were already known. This is a publication
replay of an exposed result with strengthened full-state checks, not a new
prospective discovery or independent mathematical verdict.

Assertions were enabled. The environment set LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC. Inherited
PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR were removed.
The unchanged limit was 600 seconds. Measured wall duration was approximately
2.331 seconds; this is operational metadata, not physical time.

## Frozen source custody

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 8566 | `6a2b90f07b4967d0e4eaf09c28a9628b0eae247b6acdf986c26d74f5c2b65a08` |
| PROOF.md | 16963 | `13998852f685c474e0ec775ac2e4cd41f102c2c93412ee2ef0a77beeece28fd5` |
| PROVENANCE.md | 5710 | `6882788bc1c108dfa8fe90f55fc6b93a91cc098a1d4f09153cb0d676a999c71f` |
| RUNTIME_SOURCES.json | 270 | `8238c256e9ef089ea79d9349cfa413facbf3d751cd74982dc95f53406bf40ea8` |
| arithmetic_compiler.py | 13728 | `0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027` |
| compiled_audit.py | 17474 | `1b32ea0f8b38518495e59028ad8d5867ac5a36a87da78b5924726278c56926fd` |
| verify.py | 15954 | `d9968f83bf2827f0849e65b65cb00876571d4ea3f262214c65a5362dab5d8fa5` |

This record covers the first Linux x86_64 execution only. Required PR CI must
replay these exact EXPECTED.txt bytes on x86_64 and aarch64. The actual CI head,
jobs and results are reported on the PR after completion, not inferred here.
Working-session static reviews and multiple arithmetic implementations do not
replace independent mathematical acceptance.
