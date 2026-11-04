# Run record

NON-CANONICAL / L1. First completed author-session execution.

- Source pin: `d321ff7aca4106bf0dc516f08d105da2cfa1b6bf`.
- Public source readback: all six immutable contents and Git blobs matched
  before execution; receipt in reservation issue1899.
- Command: `python3 probes/P-POLE-HEIGHT-NEUTRAL-STOCK-1/verify.py`.
- Platform: Ubuntu22.04.5 LTS, Linux-compatible WSL2.
- Architecture: x86_64. Python3.10.12, assertions enabled.
- Environment: LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
  PYTHONDONTWRITEBYTECODE=1; no optimization or evidence-directory override.
- Checkout: clean detached source pin before and after the command.
- External timeout:600seconds, not reached.
- Exit code:0. Standard error:0bytes.
- Standard output:6829bytes,29LF-terminated lines.
- Standard output SHA-256:
  `ee3221166f7bda7bceadeae50761562fa76159f4400afb22c9bd5a3166f9902c`.
- Elapsed wall time: approximately0.160seconds, operational metadata only.
- Scientific attempts: one completed run, no failed attempt or retry.

| Frozen source | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 8403 | 619c233f93eee073d9160816da74d2cabbe75d106e2452229fb37446237bdb97 |
| README.md | 1735 | d5f60a4a20b740dc023c95d058dde31bbe2fccfe5dafaca70058abbe5b35733b |
| PROVENANCE.md | 2593 | 2577032410610994fc49b6bef4d54e7d6b1c3bf20ebfe39cbaad6f5df59f803e |
| PROOF.md | 10961 | 30a943cf444932c3de031a98c798860d9e43f2ec3ae989181ac4182f6b7c0158 |
| SOURCES.tsv | 2560 | d24622c225de4ad5abda61f5617f36db95e62e12e0c35019ac45fc5401234cc5 |
| verify.py | 20139 | 9a1ccdec2797e4b3c3f58f30bc1c92a433ca4a7d18dfc55d9f3d6c815c7bef06 |

EXPECTED.txt is the exact captured scientific stdout. RUN.md and RESULT.md
are post-execution records, not amendments to the frozen source. Only these
three declared result files are appended. Independent arithmetic here is
inside one authoring session; it is not independent scientific acceptance.
The PR's required x86_64/aarch64 checker replays the same source and stdout.
Its actual CI conclusion is reported separately after readback.
