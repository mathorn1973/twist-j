# First completed formal execution

PUBLIC / NON-CANONICAL / L1. SPDX-License-Identifier: Apache-2.0.

pin_commit: 624098e9f0b18ba5dda3f0bc57b0a669409a5d2b
verifier_sha256: 6e4490cc3cbf0e207121cadbd44bbac0ed1ad6de50c6611f9709b0b41561d160
command: python3 probes/P-NATIVE-P-RECURRENCE-BOUNDARY-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 340abf65ec084ca16869c1777f7ce6d1591e97060d4097c6b9b940e69c74b007
stdout_bytes: 1366
stdout_lines: 19
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-10-18T20:22:51.942165+00:00
finished_utc: 2026-10-18T20:22:57.127769+00:00
wall_seconds: 5.186
prereg_commit: edd18cceda98cf3b28fa104699717c204543a48b
prereg_sha256: f6d16a47d191866e2299a3802b6fc6590f5fb23042e37895f5d03fd165b6c9f7
breaker_sha256: 6a346308530a19354dc9997d93bbf015d0d3c8ca15643748100a4ce947d7c909
public_readback_utc: 2026-10-18T20:22:19Z

The complete public pin was fetched before execution. All eleven probe files
were independently read back through the GitHub connector and compared with
the local content; the ten payload hashes in CODE_SHA256SUMS also matched
the fetched commit bytes. The working tree was clean at the public pin.

This was the first scientific execution of either implementation. Static
AST and custody checks preceded publication; no scientific import, dry run
or trial was performed before the pin. PUBLICATION.md distinguishes the
local preparation commits from the actual public preregistration and pin.

The command ran from the repository root under LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC, with the repository
600-second limit. The author executable launched the unchanged independent
breaker as a separate process. EXPECTED.txt was captured directly from
the first completed process stdout and was not edited.

This flat record attests the actual local x86_64 leg only. Public workflow
evidence belongs to the exact result-commit checks and is not predeclared
as a completed second architecture here. Two same-machine implementations
do not themselves satisfy the two-architecture gate.
