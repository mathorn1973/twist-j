# P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2 run record

Status: `WARD_ENGINE_QUALIFICATION_PASS / ZERO_ENGINEERING_ONLY / COMPLETE LOCAL RECORD / PUBLIC REPLAY PENDING`.

## Immutable public source pin

```text
pin_commit: 9b43eb9a780890d0816f7f528f2b0938edb06af9
parent_commit: d0bc920b27117ea4a409282e3481340f50433763
pin_tree: 239ab88dc1320c8ad1297464fccf989a93dd0340
public_issue: 756
reservation_receipt: https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5499620053
reservation_receipt_body_bytes: 4497
reservation_receipt_body_sha256: 6a40d3e4444aa60223c02518b7f02c9758d7a17cd8cfcbd12dfb82fceb3a3db9
reservation_addendum_receipt: https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5499627693
reservation_addendum_receipt_body_bytes: 2239
reservation_addendum_receipt_body_sha256: 15e897a86452d46bf543dae3f3056919755437e32daf4ab6bb9eb9677fcfa2a0
input_custody_receipt: https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5499632482
input_custody_receipt_body_bytes: 530
input_custody_receipt_body_sha256: 3dfcb7bd2e9f74e0dce18296be863b8a09a80ad3abeaf9be63c20f3549e5a144
pin_receipt: https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5500053159
pin_receipt_author: mathorn1973
pin_receipt_body_bytes: 510
pin_receipt_body_sha256: c5369a71aadffb1084d0075e5e0d021f3015b0c71401f884035fc8fb75c22fa2
pin_receipt_has_cr: NO
pin_receipt_final_lf: YES
source_manifest_bytes: 499
source_manifest_sha256: ee7c5051514da7b033a61fb1d30ceaef3f66d83aa059d52c12e6cb1f3e71b974
manifest_entries: 6
package_files: 7
attempt_ref: NONE
```

The public branch, commit, unique parent, tree, seven-path diff, package
inventory, source manifest and all six listed source hashes were read back from
a fresh full public clone before execution. The issue receipt was then read
back as 510 UTF-8 bytes with the displayed SHA-256, no CR and a final LF. No
attempt ref was created, and no CROSSCHECK-3 seed or Ward statistic was opened.

## Sole initial pinned local leg

```text
command: python3 probes/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2/verify.py
environment: LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
compiler: g++ 11.4.0
exact_integer_backend: repository-owned standard-C++17 ExactUInt; no Boost or third-party dependency
git: git version 2.34.1
completed_at_utc: 2026-09-01T20:36:06Z
formal_runs: 1
exit_code: 0
verifier_sha256: d01b594d1e546fbc3480b48e8f59ca361913b1fc39b7e9de8977509b3f5601b4
stdout_bytes: 891
stdout_lines: 11
stdout_sha256: bd919866d3ffc40f7022530dcb099a267a904cbd4c9a111f3ff7f082235cbb35
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
result: WARD_ENGINE_QUALIFICATION_PASS
evidential_status: ZERO_ENGINEERING_ONLY
```

The canonical command was issued exactly once through the preregistered empty
Linux environment in a second fresh full public clone detached at the immutable
source pin. It exited zero, wrote empty stderr and produced the exact 891-byte
`EXPECTED.txt`. The verifier removed its bounded build slot and the formal
clone remained clean.

The verifier reproduced the legacy engine guards without consuming random
bits, qualified the repository-owned arbitrary-width `ExactUInt` replacement,
audited all 28,981 frozen small tables and 6,791,443 integer draw intervals,
and established old-path choice/draw/bit/successor parity. Its integrated
synthetic supervisor retained both failure legs, bounded both streams,
cancelled queued work, killed and reaped the running sibling, passed the
injected cleanup faults and reported zero survivors.

## Selected public aarch64 leg

```text
github_workflow_run: 33556718173
github_job: 100019224672
github_head_commit: 5fb82f00fc328408b660cba01a01452d9236057f
github_tested_merge_commit: 705ab1ec65f29bb2ac2f2593c77f91dab36080f5
github_base_commit: d0bc920b27117ea4a409282e3481340f50433763
github_platform: Ubuntu 24.04.4 LTS
github_architecture: aarch64
github_python: CPython 3.12.14
github_verifier_sha256: d01b594d1e546fbc3480b48e8f59ca361913b1fc39b7e9de8977509b3f5601b4
github_stdout_sha256: bd919866d3ffc40f7022530dcb099a267a904cbd4c9a111f3ff7f082235cbb35
github_exit_code: 0
github_stderr_bytes: 0
github_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
github_status: PASS
github_verdict: VERIFY PASS
github_byte_identity: PASS
github_replay: PASS
```

The selected native aarch64 job replayed the unchanged verifier from the first
PR workflow against the displayed synthetic merge commit. The parallel
x86_64 job and aggregate `check` also passed before this receipt was appended.
