# First pinned Linux run

NON-CANONICAL / L1. Completed exact audits and bounded construction.

pin_commit: 38450ba5a54f0aa80c681092f3fbb5fc36161733
verifier_sha256: c8a37c2db5c5731d1df5a985e695576b39293397c45d91e70d60c48b8a5c8317
command: python3 probes/P-POLE-HEIGHT-STABILIZER-CHAIN-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: efc4392c5d719fdb15edb5d4553b26bcbb578a2189e4c336487784b5f536093e
stdout_bytes: 10576
stdout_lines: 15
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All eight source contents and Git blobs were read back publicly before
execution (issue1903, comment6638056879). The first run used a clean detached
checkout of this pin, verified every source hash, and remained clean.
Exit zero, empty stderr. No scientific failure, retry or source change.

Assertions were enabled. LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1 were set; inherited PYTHONOPTIMIZE,
PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR were removed.
The external600-second timeout was not reached. Actual wall duration was
approximately6.483seconds, operational metadata, not physical time.

The completed search outcome was INCONCLUSIVE_MINUS_TRANSPORT, with
2316921 logical search contacts. Both32768-step walk sides completed;
no work cap fired. No minus transporter was found, so the plus stage and
full five-input final witness audit were not run. Mandatory fixture and
seven-stock audits completed. No omitted gate is represented as passed.

## Frozen sources

| File | Bytes | SHA-256 |
|---|---:|---|
| BANK.json | 7943 | d4270e03f851f0d2327e2eac7f23cc796b9bbffb1e54b2943f52a0c89fb83f07 |
| PREREG.md | 10453 | da265e90359e91a8511199b3b7ddfa47568e9876e38ae409e40aaa963114a067 |
| PROOF.md | 11227 | 929b93e080267487c9860824df745f92365682b78254a5b8d832c8c9d8212bc4 |
| PROVENANCE.md | 5845 | 81be2e45a9d2117c0aa2deedbc715cfce811a30bf4a77d4309399d12f2902249 |
| README.md | 1688 | 7002fe3946b8a3b0a88eaa2e72796e7c4cf77be22a64b9d162d2e967f67e4453 |
| smallstock.py | 8873 | 852e93cdd98d8c52ed2c8f0215bf95bf39aefc91d22091612ef702d35799c8ba |
| SOURCES.tsv | 1814 | f265805d10289f5c583cb39b9353ced7f2451fe5fac4fc57ef91dd30b9488b62 |
| verify.py | 27826 | c8a37c2db5c5731d1df5a985e695576b39293397c45d91e70d60c48b8a5c8317 |

Only EXPECTED.txt, RUN.md and RESULT.md are appended after the source pin.
Required repository checks and architecture CI are reported after actual
completion. Same-session reviews are authoring checks, not independent
acceptance or Canon promotion.
