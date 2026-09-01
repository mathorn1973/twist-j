# P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-1 run record

Status: `WARD_ENGINE_QUALIFICATION_PASS / ZERO_ENGINEERING_ONLY / COMPLETE LOCAL RECORD`.

## Immutable public source pin

```text
pin_commit: 1f4de925d50af37f204fd69ce97b780271a6439c
parent_commit: d0bc920b27117ea4a409282e3481340f50433763
pin_tree: 68541bee237f07972a269d1f7209c40dfa0e84c9
public_issue: 756
pin_receipt: https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5499374828
pin_receipt_body_bytes: 554
pin_receipt_body_sha256: 062b467dfc221bf4a5677a273355f13d97f346ac6b47179ef3fc66ff3a04d3c9
source_manifest_bytes: 499
source_manifest_sha256: 85de92625d2716cb38e1ca5e4678ecd6e260e8e27aa7aa29e0c0d8ed8e6c259b
manifest_entries: 6
package_files: 7
```

The public branch, commit, parent, tree, bytes of all seven package files and
six source hashes were read back before execution.  The issue receipt was then
read back as 554 UTF-8 bytes with the displayed SHA-256, no CR and no final
LF.  No attempt ref was created because this deterministic qualification
reserved none.  No formal CROSSCHECK-2 seed, abandoned replay or Ward
statistic was opened.

## Sole initial pinned local leg

```text
command: python3 probes/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-1/verify.py
environment: LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
compiler: g++ 11.4.0
boost: 1_74 / 107400
git: git version 2.34.1
completed_at_utc: 2026-09-01T19:38:56Z
formal_runs: 1
exit_code: 0
verifier_sha256: cdf7edd9ecf0632b5125f4d2619cd541069ab015e7c1bbbfefffb35a9e9730f4
stdout_bytes: 891
stdout_lines: 11
stdout_sha256: 909604fb4bb6334617f8082a2715322d4af3137c93f118e50d4300c2f049db02
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
result: WARD_ENGINE_QUALIFICATION_PASS
evidential_status: ZERO_ENGINEERING_ONLY
```

The canonical command was issued exactly once in a fresh full public clone at
the immutable source pin.  It exited zero, wrote empty stderr and produced the
exact 891-byte `EXPECTED.txt`.  The build slot was removed and the formal
clone remained clean.

The verifier reproduced both old engine guards with zero consumed bits,
accepted the exact arbitrary-width replacement, audited all 28,981 frozen
small tables and 6,791,443 integer draw intervals, and established old-path
choice/draw/bit/successor parity.  Its integrated synthetic supervisor retained
both failure legs, cancelled queued work, killed and reaped the running
sibling, passed both injected cleanup faults and reported zero survivors.
