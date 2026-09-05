# Local observed interval adapter: formal run

```text
pin_commit: 0ddc026fa5f2eefcfbc122d38585f475bd6418cc
pin_tree: 9fc14c020b77f88379799a20326a3ec749973e53
base_commit: 11556f685f0c51c06fec6da32118a1d1e63d7fa4
public_lock: https://github.com/mathorn1973/twist-j/issues/838
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/838#issuecomment-5551298548
command: python3 probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
start_utc: 2026-09-05T10:56:24.737755+00:00
finish_utc: 2026-09-05T10:58:31.139703+00:00
exit_code: 0
stdout_sha256: c10825ec57fd5672e7a05d9caba1d1946cbea420d9cbf10968b596c7cb847836
stdout_bytes: 58096
stdout_lines: 1419
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
formal_execution_count: 1
child_invocations: 1
capture_complete: true
stdout_encoding: ASCII / UTF-8 subset
stdout_line_endings: LF-only; final LF present
verifier_sha256: e7bab46a821edd7c1e4accb89bfee106d3f8076086667b3dfaec5991a1491cc5
verifier_bytes: 29924
prereg_sha256: 7841ead15690dddc67967de6a0176d124c228074d10bdb613d6cdaf5c2e47498
prereg_bytes: 9870
public_readback: PASS before new execution and new delay extraction
all_pinned_sources_pre_post_match: yes
worktree_clean_before_and_after: yes
claim_A: CONFIRMED
claim_B: CONFIRMED
architecture_gate: PASS aarch64 and x86_64; workflow 33962156745
```

## Complete immutable source inventory

| File | SHA-256 | Bytes | Git blob |
|---|---|---:|---|
| `notes/NIST-RAW-CUSTODY-1.md` | `b6d19a283ede826cb41910e80db567f71f95e2cc3258fce2f03e0d1525471ec2` | 5906 | `c13ce4a811c39f5d641f0a229787f785f36e5e37` |
| `probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/DEPENDENCIES.json` | `99875763b8b918ed951534ad0128e09813084aa685482e7579d32b13cfd06dd0` | 905 | `fe181ed16d1c28515d01f679445d79ab63b87b08` |
| `probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/PREREG.md` | `7841ead15690dddc67967de6a0176d124c228074d10bdb613d6cdaf5c2e47498` | 9870 | `63ba50674634e4c2d23c3ab585cb19043647eebb` |
| `probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/PROOF.md` | `06634045e87a8720216a41e96b4034fc793a03cbb7623dc8ee2f7d00c78639e6` | 3514 | `2525166f5d397b58e99e0fabb98b8fbbb20d92d9` |
| `probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/README.md` | `226b30a0dcfd51840c4f713302709d2b8407adf977e78ba7cdef9aad917747e6` | 1489 | `36bcac0a2802a890a8755f8b8fea57e993a43788` |
| `probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/adapter.py` | `13cd74be2c5e48f30de15e6eb3c949736eeb0634bfe7463e20c6da8300ca7bf4` | 8278 | `03be0d80250159049538a277c04b1df74988de46` |
| `probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/verify.py` | `e7bab46a821edd7c1e4accb89bfee106d3f8076086667b3dfaec5991a1491cc5` | 29924 | `b4ea776f863bbf32261de7adf731e9e57e724b29` |
| `probes/P-NIST-RAW-RECORD-QUALIFICATION-1/SOURCE.json` | `653e5dd17b041ecf38244bcd8312fa724863eb681f940795e38974182f7bbe8a` | 4058 | `bcc91d20b63ecf362819a7c78cb380abc3a0167a` |
| `probes/P-NIST-RAW-RECORD-QUALIFICATION-1/verify.py` | `0e63ea7ee01bff85558af311c8d819440f7155e34a8582b003929701ee1d4bf7` | 24560 | `c9fad32da886b7ce19ece76dfb036dc2e19b9d3d` |

## Execution, exposure and limits

The exact public pin was checked out in a fresh clean Linux clone. One initial
formal child ran from the repository root, with PATH=/usr/bin:/bin, LC_ALL=C,
LANG=C, TZ=UTC, PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1 and
PYTHONNOUSERSITE=1. An external 600-second timeout was retained. Lossless capture
saved stdout/stderr and exit status, with every source hash checked before and
after the child. EXPECTED.txt is the exact captured stdout.

TWISTJ_NIST_CACHE_DIR supplied the separate opaque custody copy. The complete
compressed size and SHA-256 of each of the same four objects were checked before
ZIP access. The inherited NIST notice accompanied the data. Each selected member
portion was traversed twice for continuous/chunked comparison; no run3 tail was
decoded. Each reconstructed indexed row was also compared directly with an
independent original-row buffer. Hashes compact the output, not replace that
direct equality audit. No full packet payload stream is retained in Git.

The predecessor qualification census was known before this new pin and is
explicitly disclosed. This is not a blind experiment. New packet hashes and
delay summaries were first obtained in this pinned execution. The inherited
probe and its source manifest remain unchanged. Counterfactual algorithmic
fixtures are visibly separate from experimental records.

Independent public cold replay and post-result review will supplement this
initial record. Their scope is exact archived-record reconstruction; no physical
clock pairing, trial, post-state, no-click, apparatus or Born claim is made.

## Independent architecture and post-result review evidence

[Workflow 33962156745](https://github.com/mathorn1973/twist-j/actions/runs/33962156745) passed on result commit
`f37cb6b803ccab9c8adb4c7f310f7392cfe6494c`. This commit adds only EXPECTED.txt, RUN.md and
RESULT.md to the immutable analytical pin.

| Architecture | Public job | Exact cold replay |
|---|---|---|
| aarch64 | [101295794608](https://github.com/mathorn1973/twist-j/actions/runs/33962156745/job/101295794608) | PASS |
| x86_64 | [101295794350](https://github.com/mathorn1973/twist-j/actions/runs/33962156745/job/101295794350) | PASS |

Both public jobs retrieved the same four original NIST archives without the
local cache hint. Each verified their complete compressed hashes before the
same bounded audit and independently reported the actual runner architecture,
verifier SHA-256 and the exact stdout SHA-256 recorded above. The unchanged
600-second timeout was met. These runs reproduced archived evidence, not an
independent experiment. The aggregate required check and all 155 tool tests
passed on both jobs.

Clean Linux policy, Canon, ledger, gate-contract, status-label, tool-test and
exact changed-probe replay checks passed. No changed minimal reproduction was
applicable. Independent post-result scope, source-integrity, evidence-count,
privacy and license review passed. The nine new files are printable text;
raw archives remain outside Git under the unchanged NIST notice. Neither
review nor architecture agreement changes any public registry status.
