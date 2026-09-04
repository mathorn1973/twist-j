# Pointed batch decoder formal run

```text
pin_commit: 69c9dc34f57d5f9943681761eb6386a17d4bfc47
source_commit: 69c9dc34f57d5f9943681761eb6386a17d4bfc47
pin_tree: 5206ec0e59bfaf141aa2c9afde39513d9e434763
base_commit: 1a58703ec17a4c031bb8c450f56162f5aa3e5e5a
public_lock: https://github.com/mathorn1973/twist-j/issues/820
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/820#issuecomment-5547516232
command: python3 probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
start_utc: 2026-09-04T23:13:51.619185+00:00
finish_utc: 2026-09-04T23:13:56.493749+00:00
formal_execution_count: 1
exit_code: 0
stdout_sha256: daa88d06662b436550ff461b73fff2a8d357f1f35b9adf7c2a192e6b260e6213
stdout_bytes: 521
stdout_lines: 17
stdout_encoding: ASCII / UTF-8 subset
stdout_line_endings: LF-only, final LF present
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
verifier_sha256: 3552a6e7617cdcd4a6b1fa21fa2e49c71a0771fa42edc9e9643650f688cb35ad
verifier_bytes: 14746
verifier_blob: 4b0b594579b9a53f7f2c61f6c53e9d021bbb3759
prereg_sha256: 29eb58b082856440d98180d7f26297782e79c569efca2d3dbfa595ee1eef46ac
prereg_bytes: 21608
prereg_blob: 7d04a4adf5e4f07081cd4332e79be96fe5b563af
public_readback: PASS before formal execution
all_pinned_sources_pre_post_match: yes
worktree_clean_before_and_after: yes
result: LOCAL CONFIRMED; 10/10 gates; one conditional mathematical claim
architecture_gate: PASS x86_64 and aarch64 exact public replay
post_result_security_review: PASS independent read-only review of all fourteen files
```

## Complete immutable source inventory

All eleven files were matched against the public commit before execution.
Their SHA-256 values were identical before and after the clean Linux run.
The verifier additionally enforces its own seven-entry dependency hash table.

| File | SHA-256 | Bytes | Git blob |
|---|---|---:|---|
| `notes/canon/C-DECODER-POINTED-BATCH-1.md` | `8b95c1d9a5a2c1cf26bdfc601c24812a5c75340bf5ac03d975adcc448a898980` | 31162 | `3dc8417c0fb5efc27f2ad1e3b0803547e1be1ee4` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/PREREG.md` | `29eb58b082856440d98180d7f26297782e79c569efca2d3dbfa595ee1eef46ac` | 21608 | `7d04a4adf5e4f07081cd4332e79be96fe5b563af` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/PROFILE.json` | `2007c0a68d663eb4214341c75f7310d1430ca8e2cf4620f9bac03616aae6f79e` | 195811 | `0f7ea2fce4dd8d89875d570c943b94c9ab319acf` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/README.md` | `96fe0e2e8a13e4f315cde4b163da070fa4fc30387959588b2fc7a718fade8eb5` | 2787 | `420ff1708413a4e8fc2c202ce023d4b9ac53c2b3` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/apparatus.py` | `b9efc44e415c250f7a7c4639a05601ad97713ac20d5e49e14da894bc05581e79` | 16132 | `dc704b861038930e27325ec98445a2ff90023743` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/audit_apparatus.py` | `26afd62aed517289624dec8a9f6a167ccb4a6c99e573803877a20c5f646aa87b` | 11004 | `6f2f091d09fde8ccdf30ca0389f80690cc1d1c5d` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/audit_geometry.py` | `4e4a07e384600eaa3480d3c026fcaaa04ec3f2a5cf780eae4254edf6fa740d9a` | 17686 | `439d3eb5f2ad745c3b68d946241f302cf2efd6c3` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/decoder.py` | `85809a77013791ef9fa175484bc3a85e7b515eaeda20fd3ba36fdc5d6627b912` | 4603 | `73c29f3dd9d4d5f74b79851d70684283883e5f89` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/geometry.py` | `e485201def16cf7c237ee662167ddf9de787fd89f9af32c5e2622e2ce25f4e4c` | 12258 | `185ae5350420d359e3e6cfd946c52b86def3f863` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/kernel.py` | `8fe60efb5f1c8888ac455332ec8305bc531687836f5c604aedd2e483ed534ba9` | 4471 | `8dc23b379ef8417cee8fcc83c6cabc3375b480e3` |
| `probes/P-DECODER-POINTED-BATCH-CONFORMANCE-1/verify.py` | `3552a6e7617cdcd4a6b1fa21fa2e49c71a0771fa42edc9e9643650f688cb35ad` | 14746 | `4b0b594579b9a53f7f2c61f6c53e9d021bbb3759` |

## Execution and evidence boundary

The Linux checkout was a clean clone at the exact public pin. The verifier ran
from the repository root with standard Python 3.12 and deterministic LC_ALL=C,
LANG=C, TZ=UTC, PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1 and
PYTHONNOUSERSITE=1. No source was changed and no scientific run preceded
the public pin/readback. EXPECTED.txt is the captured stdout byte for byte;
raw capture hex, its digest, byte/line counts, empty stderr and final LF were
checked before writing it. This is the sole initial local formal execution.

The deferred `PIN:RUN.md:source_commit` reference in the immutable PROFILE
now resolves to the actual source_commit above. The preregistration PROFILE
retains its pre-execution evidence states; this later record and RESULT.md
supply the evidence without rewriting that frozen profile.

Independent architecture replay and manual post-result review are recorded
below as subsequent evidence. Mathematical conformance is not physical realization.
Public claims remain unregistered and Canon v76 is unchanged.

## Independent replay and security review

The public policy workflow
[33928937450](https://github.com/mathorn1973/twist-j/actions/runs/33928937450)
completed successfully on PR head `3ac929d1e1076147a340d394826e7540c1910a71`.
Both architecture jobs printed the same verifier/output hash pair and
`VERIFY PASS`. Their required runner check compared exact stdout bytes and
required exit zero and empty stderr. The aggregate check also passed.

| Architecture | Platform | Python | Successful job |
|---|---|---|---|
| x86_64 | Ubuntu 24.04.4 | CPython 3.12.14 | [101203375858](https://github.com/mathorn1973/twist-j/actions/runs/33928937450/job/101203375858) |
| aarch64 | Ubuntu 24.04.4 | CPython 3.12.14 | [101203376160](https://github.com/mathorn1973/twist-j/actions/runs/33928937450/job/101203376160) |

The required architecture pair is the original local x86_64 leg above and
the independent public aarch64 leg below. The additional public x86_64 job
is recorded in the table, without reinterpreting the original local run.

```text
github_platform: Ubuntu 24.04.4
github_architecture: aarch64
github_python: CPython 3.12.14
github_verifier_sha256: 3552a6e7617cdcd4a6b1fa21fa2e49c71a0771fa42edc9e9643650f688cb35ad
github_stdout_sha256: daa88d06662b436550ff461b73fff2a8d357f1f35b9adf7c2a192e6b260e6213
github_exit_code: 0
github_stderr_bytes: 0
github_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
github_status: PASS
github_verdict: VERIFY PASS
github_byte_identity: PASS
github_replay: PASS
```

The clean Linux validation also passed policy, all 155 tools unit tests,
Canon, ledger, gate contract, status labels and exact changed-probe replay.
No minimal reproduction changed. Both public architecture jobs passed the
required full tools suite and policy/Canon/ledger/gate checks as well.

Independent post-result review matched all eleven pinned files against the
immutable Git blobs, and matched EXPECTED.txt against captured stdout hex.
It reviewed all fourteen submitted files for imports, file/network/process
operations, secrets, binary/symlink content, scope, typed carrier separation
and physical overclaim. No blocking finding was found: the accepted code
uses only the standard library and pinned modules; no Canon, workflow, tool
or prior probe is changed. The source/current/propagator/detector physical
coupling and all other explicitly unresolved obligations remain unresolved.
