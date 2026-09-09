# Run record: P-FRW-INHOM-K1-BACKREACTION-3

```text
pin_commit: 1f3a3d5b074547991919ad52824d6c7f6f591550
verifier_sha256: 12da283759b30ed9a1a388f4e022a0230e2362bd3ed2e420dacb31cc1d1c6596
command: python3 probes/P-FRW-INHOM-K1-BACKREACTION-3/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: 6bff6b9ef4a4164203c90cdbe311a760be8550199f672cc1d4576391d634f6db
stdout_bytes: 1118
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
started_utc: 2026-09-09T10:53:20.392880+00:00
finished_utc: 2026-09-09T10:53:21.516379+00:00
```

The accepted public pin and its preregistration/verifier identities were
recorded in issue #923 before scientific execution. The open pin was
completed under repository owner A. M. Thorn; no accepted scientific byte,
input, threshold or gate was changed. The remote branch still equalled the
accepted pin immediately before the run, and the native worktree was clean.

The Linux interpreter executed the displayed command from the pinned
repository root. A capture wrapper checked the preregistration (7243 bytes,
SHA-256 `958373cde52385702694fc5afe477cd08ae8fbdc6d85fe27cee79daf7e720b67`),
verifier and Canon v82 identities before and after execution. It captured
stdout and stderr separately, with a 600-second ceiling. Only the actual
completed stdout was copied byte for byte into `EXPECTED.txt`. No accepted
file changed during execution.

G1 through G11 passed. The verifier's G12 line checks its own deterministic
path only; the required public x86_64/aarch64 Python 3.12 jobs must replay
the same accepted bytes against this one `EXPECTED.txt` to complete G12.
This local x86_64 execution alone is not the two-architecture gate.

The independent pre-result audit already public in issue #923 is
corroboration, not an additional blind run. Subsequent homogeneous time
bridge constructions are outside this frozen execution and are not
attributed to it.

## Public replay evidence

[Workflow 34342847790](https://github.com/mathorn1973/twist-j/actions/runs/34342847790)
completed successfully for the first result commit of PR #925. Both required
Linux architecture jobs, x86_64 and aarch64 with Python 3.12, ran the ordinary
probe verifier gate and matched this exact `EXPECTED.txt`. The aggregate
`check` passed. No scientific input, accepted verifier or expected output
changed to obtain the public match. The final documentation head retains
the same scientific bytes and must independently pass the required checks.
