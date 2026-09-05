# Reservoir quadratic partition formal run

```text
pin_commit: 87b085422dbe7ed7975333f14c884431ea9c2f36
source_commit: 87b085422dbe7ed7975333f14c884431ea9c2f36
pin_tree: db3362e763e230c9eee6ef20e50165b6457dee67
base_commit: 4e794a01aec719a4536f2028ecbfd2f876a19e2b
public_lock: https://github.com/mathorn1973/twist-j/issues/827
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/827#issuecomment-5550546474
command: python3 probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
start_utc: 2026-09-05T08:20:11.529423+00:00
finish_utc: 2026-09-05T08:20:54.379150+00:00
formal_execution_count: 1
exit_code: 0
stdout_sha256: 9ee2b5a125f975babb4ae1707c9c58d83d8268a50ac8c251044219c915464331
stdout_bytes: 613
stdout_lines: 16
stdout_encoding: ASCII / UTF-8 subset
stdout_line_endings: LF-only, final LF present
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
verifier_sha256: c9b140dced94518b596fef12053c38791cc8e34dea60aa5b938e5a60d89b1d17
verifier_bytes: 2603
verifier_blob: 0eb86d9820de381c3069647c2f57bd59ba7e3d7b
prereg_sha256: 0b4730312240d78bb8733144251d369fb16505f89b52b280a227cf30d3a1086c
prereg_bytes: 12184
prereg_blob: fc6dfd1110b1e44b49af3506567a06a5e5a775d7
public_readback: PASS before formal execution
all_pinned_sources_pre_post_match: yes
worktree_clean_before_and_after: yes
result: CONFIRMED both conditional claims
architecture_gate: PASS aarch64 and x86_64; workflow 33955143771
post_result_security_review: PASS independent scope, pin, exact bytes, sources, security and license review
```

## Complete immutable source inventory

All eight files (six new sources and two inherited executable dependencies)
matched the public source pin before execution and retained their exact hashes
after the clean Linux run. No scientific import or execution preceded the pin.

| File | SHA-256 | Bytes | Git blob |
|---|---|---:|---|
| `probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/PREREG.md` | `0b4730312240d78bb8733144251d369fb16505f89b52b280a227cf30d3a1086c` | 12184 | `fc6dfd1110b1e44b49af3506567a06a5e5a775d7` |
| `probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/PROOF.md` | `296cba62fe32484bdbdf04feda5a9c12f7ddd91af15e8dc0597b161dfe49eee9` | 11349 | `112509704c7d520de43a0bde2fcf0e6a9216e3b4` |
| `probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/README.md` | `1e737e2a78d3d1a42c14b69629c2755f2a29c2b079077dcd98799fa50dce379e` | 3583 | `a80a3e078d503f1135ecf70d91b2d599b8df1bc0` |
| `probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/partition.py` | `9a990cf8f7096a3078b6cc3a2f05d801444511f12865381d1476af9533503c45` | 8025 | `c17b12873cdf411b8c8c61765e9d9ae4436dd177` |
| `probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/audit_partition.py` | `82b8f293d3eb9114d4d35d67adcdac09f5c580a63e0596dd7aad29f6d2055a44` | 13972 | `1469ba319dc27a3971bc6f56d0d5c35be543f607` |
| `probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/verify.py` | `c9b140dced94518b596fef12053c38791cc8e34dea60aa5b938e5a60d89b1d17` | 2603 | `0eb86d9820de381c3069647c2f57bd59ba7e3d7b` |
| `probes/P-DECODER-RESERVOIR-COUPLING-1/coupling.py` | `54f8b03762639e2573f02210b07e0d19b28935c2bc68c7f5988b15efbe26d403` | 7966 | `6fd369a86ec8585877377b801aa01b852789ec20` |
| `probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/transport.py` | `983d22690e061128d287f23ef4672fbd72954faa28f1a3fde9ce38b0d6660a60` | 11353 | `9af43a4fb9ac812d81bd04c3a047cf9ce720c4ab` |

## Execution and evidence boundary

The exact public pin was checked out in a clean Linux clone. The sole initial
formal command ran from the repository root with LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1 and PYTHONNOUSERSITE=1.
EXPECTED.txt is the captured stdout byte for byte, with empty stderr, exit zero,
ASCII content, LF-only endings and a final LF. All eight frozen gates passed.

The finite audit uses four contexts and every horizon 0..3; its independent
reference propagates four basis sources and six pair sums and polarizes actual
residual wave energy. Exact principal minors audit positivity. PROOF.md supplies
the uniform rational-context/finite-horizon and real-postprocessing arguments.

Frozen source files keep their pre-execution labels. RUN.md and RESULT.md
record later evidence without editing those inputs. Independent architecture
evidence will be added after public replay. Physical apparatus/occurrence and
Canon v76 status remain unchanged; public claims are unregistered.

## Independent architecture and review evidence

[Workflow 33955143771](https://github.com/mathorn1973/twist-j/actions/runs/33955143771)
passed on result commit `9b589dbeef755e640fc8565929da68393a389705`, which adds
only EXPECTED.txt, RUN.md and RESULT.md to the immutable source pin.

| Architecture | Job | Exact replay |
|---|---|---|
| aarch64 | [101276999494](https://github.com/mathorn1973/twist-j/actions/runs/33955143771/job/101276999494) | PASS |
| x86_64 | [101276999652](https://github.com/mathorn1973/twist-j/actions/runs/33955143771/job/101276999652) | PASS |

Both public logs report verifier SHA-256
`c9b140dced94518b596fef12053c38791cc8e34dea60aa5b938e5a60d89b1d17`
and stdout SHA-256
`9ee2b5a125f975babb4ae1707c9c58d83d8268a50ac8c251044219c915464331`.
The two architecture jobs and aggregate check were read back as successful.
All 155 tool tests and policy, Canon, ledger and gate-contract checks passed;
clean Linux validation also passed status labels and exact changed-probe
record/replay validation. No changed minimal reproduction was applicable.

Independent post-result review confirmed the exact three-file result diff,
all eight unchanged source hashes and byte counts, the 613-byte/16-line
transcript, both claim scopes and neutral provenance. No blocking security
or license issue was found. These are mathematical evidence records; no
physical effect, apparatus, occurrence or Canon status is adopted.
