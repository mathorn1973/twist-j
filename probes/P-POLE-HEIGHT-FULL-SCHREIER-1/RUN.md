# First pinned Linux run

NON-CANONICAL / L1. Complete zero-orbit audit and bounded construction.

pin_commit: 82bb5e56f1559a9db12260745c0eb4c9ea445d89
verifier_sha256: 30767524ea1e0b942d2351c320deef7ddc2a649ec66081ed2bc80207456daf68
command: python3 probes/P-POLE-HEIGHT-FULL-SCHREIER-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 4a855bef5a2954edae41f1b41e509cdeea1cd94bce23105b674079dc3c873fec
stdout_bytes: 3108
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All seven source contents and Git blobs were read back publicly before
execution (issue1905, comment6638584066). The first run used a clean detached
checkout of this pin, verified every source hash, and remained clean.
Exit zero, empty stderr. No scientific failure, retry or source change.

Assertions were enabled. LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1 were set; inherited PYTHONOPTIMIZE,
PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR were removed.
The external 600-second timeout was not reached. Actual wall duration was
approximately 3.222 seconds, operational metadata, not physical time.

The completed search outcome was INCONCLUSIVE_COMPLETED_DECLARED_SEARCH,
with 27761026 logical search contacts. The full direct descriptor pass
and both 32768-step minus walk sides completed; no work cap fired.
No minus transporter was found, so the plus stage and full five-input
final witness audit were not run. Mandatory fixture and three-input
zero-prefix audits completed. No omitted gate is represented as passed.

## Frozen sources

| File | Bytes | SHA-256 |
|---|---:|---|
| BANK.json | 7943 | d4270e03f851f0d2327e2eac7f23cc796b9bbffb1e54b2943f52a0c89fb83f07 |
| PREREG.md | 9330 | 54d6d8d9c7e97902f66d0ba3e816e362b5db6835a635db1a35149a1457fe931e |
| PROOF.md | 11315 | f5c54a115ffafc418d7fb6bb477a733f7663fac53033c37bc32cc19cfb698bda |
| PROVENANCE.md | 5455 | 134f68385ed4eac6205d3b1c2b5023039118af2ac2c46a1dd8ee3152678bb19d |
| README.md | 1457 | 9b1ced83f89a4bcdd30eb636f3b96ffc9fcc916fee71cb62b58db358b2293aee |
| SOURCES.tsv | 2320 | 79b04ce59affa230aae977fde9b68334d5e6857294b926dddf27955a019e8d9f |
| verify.py | 30512 | 30767524ea1e0b942d2351c320deef7ddc2a649ec66081ed2bc80207456daf68 |

Only EXPECTED.txt, RUN.md and RESULT.md are appended after the source pin.
Required repository checks and architecture CI are reported after actual
completion. Same-session reviews are authoring checks, not independent
acceptance or Canon promotion.
