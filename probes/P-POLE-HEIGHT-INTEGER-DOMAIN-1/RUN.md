# Formal run record

NON-CANONICAL / L1. First execution from the clean public source pin.

pin_commit: 5d02197f2ab28f336f74314cd0cf87cddc65cbf5
verifier_sha256: 3c91fb43d8813e1a9d44e03f499c14bc901db36cf9244a95c3f2132361ab3afb
command: python3 probes/P-POLE-HEIGHT-INTEGER-DOMAIN-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 092b93a5ae235c631dd72b8adb51b02d7b1e91cf78a86f53ce307672a5eac84d
stdout_bytes: 8944
stdout_lines: 29
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The source commit was pushed and all six public files read back before the
first execution, with exact bytes, SHA-256 and Git blobs matched. Issue
#1911 records the prospective pin. The checkout was clean at the pin before
and after execution. Assertions were enabled; LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. No scientific execution or
import preceded the pin. Static inspection and AST parsing did precede it.

The first run completed in approximately 0.374 seconds (an engineering
measurement, not a scientific threshold), without hitting any cap. Its
stdout is copied verbatim to EXPECTED.txt. There was no failed scientific
run, retry, source adjustment or resource expansion. Only EXPECTED.txt,
RUN.md and RESULT.md are appended to the frozen six source files.

| Source | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 6824 | 711358d26521266ba067b312400db30058436be1c3e5faa7982db4032a4a6c48 |
| PROOF.md | 6302 | 3bdc7a78fbca37597953e9c68dffabf3dc6974a178f247fc5feaa613783e4898 |
| PROVENANCE.md | 2274 | 3f350fb01c67eb3fa60c50f91a1b275b2b71bffc0dd6f7e6e9c3e87ca51fe59e |
| WORD.txt | 966 | 6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7 |
| checker.py | 6712 | 553404d4cd8facd1dee7f842bae8d454504e20a64f6143f8b6c2c60351174d72 |
| verify.py | 19475 | 3c91fb43d8813e1a9d44e03f499c14bc901db36cf9244a95c3f2132361ab3afb |

The existing pull-request workflow independently executes the unchanged
verifier on x86_64 and aarch64, requiring identical stdout against this
EXPECTED.txt. Its actual job results are the cross-architecture evidence;
this local record alone does not claim that gate has passed.
