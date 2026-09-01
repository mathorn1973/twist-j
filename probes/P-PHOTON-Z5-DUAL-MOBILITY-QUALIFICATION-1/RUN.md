# P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1 formal run record

Status: `DUAL_MOBILITY_QUALIFICATION_PASS / ZERO_ENGINEERING_ONLY / COMPLETE LOCAL RECORD`.

## Immutable public pin

```text
pin_commit: a4b9ca828e8c17c5125fef98c6d8cf34e4e1dfb6
parent_commit: ebf1d8a2100cb26c58721edaade67a278a0004a7
pin_tree: 62cfcc4a47f42a01690f69ea5b30d8563a0bb3f1
public_issue: 756
pin_receipt: https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5497343780
source_manifest_sha256: 6f8b8df01293abd065cd69f1dddb7d3df956bf651b046993fec0d55eaadd2001
input_manifest_sha256: 5ea7eba13b04de8276a26f1231299334b1c04048b4e061b545aead30368d0eeb
local_attempt_ref: refs/probe-attempts/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1
public_attempt_ref: refs/heads/probe-attempts/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1
```

The public branch, commit, parent, tree, ten-line issue receipt, ten source
hashes and five input hashes were read back before execution.  The local and
public attempt refs were atomically created at the pin and the public ref was
immediately read back before compilation or any formal seed.

## Sole formal local leg

```text
command: python3 probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/verify.py
orchestration_command: python3 probes/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1/qualification_run.py --formal --pin-commit a4b9ca828e8c17c5125fef98c6d8cf34e4e1dfb6 --pin-receipt https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5497343780
environment: LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
platform: Windows 11 10.0.26200
architecture: x86_64
python: CPython 3.12.10
compiler: g++ 15.2.0 MinGW-W64 x86_64-ucrt-posix-seh
completed_at_utc: 2026-09-01T16:51:06Z
formal_runs: 1
driver_exit_code: 0
exit_code: 0
verifier_sha256: 94fd10eeeb15ee0fbf7bc2566eb67d12217752b390413a01b8bf413d98b99c32
stdout_bytes: 4656
stdout_lines: 30
stdout_sha256: 27dcb0a084de3526b97d9df2531a2451b44cfb5d19aa2717ba8dc15dcefd7871
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
result: DUAL_MOBILITY_QUALIFICATION_PASS
evidential_status: ZERO_ENGINEERING_ONLY
```

The runner revalidated the twelve pinned package bytes and both manifests,
compiled the exact C++ engine, matched the frozen C++/Python fixture, executed
the eight frozen L3/L4 chains in table order, and analyzed the complete
in-memory transcripts.  The driver was invoked exactly once and was not
restarted or extended.  Captured stderr was empty.

## Frozen decision summary

```text
L3 mobility chains:       4/4 PASS
L4 mobility chains:       4/4 PASS
L3 mixing metrics:       15/15 PASS
L4 mixing metrics:       15/15 PASS
L3/L4 scale gate:             PASS
analysis failures:                 0
terminal: DUAL_MOBILITY_QUALIFICATION_PASS
```

At L3 the smallest per-chain ESS was `1414.65`, the largest Rhat was
`1.00038`, and the largest drift z was `1.96731`.  At L4 the corresponding
values were `657.985`, `1.00119`, and `3.57926`.  All remain inside the frozen
ESS >= 128, Rhat <= 1.03 and z <= 4 boundaries.  Every registered current,
H2, ladder-transport, quartile, uniqueness and cross-size count passed.

No raw JSONL is retained.  `EXPECTED.txt` is the complete immutable stdout;
the no-argument verifier deterministically regenerates all streams only after
the committed result and both public refs are read back.
