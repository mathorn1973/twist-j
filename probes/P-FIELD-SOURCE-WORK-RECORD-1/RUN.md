# First pinned execution

PUBLIC / NON-CANONICAL / L1. Author: A. M. Thorn. Apache-2.0.

pin_commit: 541aeeef12ab271b50a64ec6526f2580b3a874c1
command: python3 probes/P-FIELD-SOURCE-WORK-RECORD-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
started_utc: 2026-10-18T09:22:21.639810+00:00
finished_utc: 2026-10-18T09:22:22.906612+00:00
elapsed_seconds: 1.267912
exit_code: 0
verifier_sha256: d2ad3cbe0b4e3015c5cf3f14e44a17217f3f372412796f6043c3c92efccdb313
stdout_sha256: 0d10aa0af5f327bb6ee874679e3577e9a82715be7a72d742727057dee8b21cdf
stdout_bytes: 857
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC.
The registered subprocess timeout was600 seconds. This was the first scientific
execution of this verifier, from the clean exact published pin. No pre-pin
scientific executable was run or imported.

Public pre-run receipt: https://github.com/mathorn1973/twist-j/issues/1611#issuecomment-6248186919

The actual 857-byte stdout is EXPECTED.txt. Stderr was empty. The final line
is AUDIT PASS and no FALSIFIER line occurred. All five frozen inputs retain
their pre-run hashes. No scientific parameter, fixture, code or threshold
was changed after this execution. GitHub reproduction, when completed, is
reported separately on the PR with exact head and job evidence.
