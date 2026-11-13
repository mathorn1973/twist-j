# Run Record: `C-HOMOGENEOUS-RECORD-RETENTION-BALANCE-N`

**PUBLIC, NON-CANONICAL. Design-exposed correction audit; not a registered probe.**

## Pin

| Field | Value |
|---|---|
| Correction pin commit | `3c32bcbb412a46938ff455a2998c785667390e59` (pushed and read back before execution) |
| `verify.py` | SHA-256 `b6730c48e9fc3bb7a4c3f08094263a80de5ff209aaef83db68749d112df36fd7`, 8596 bytes |
| Contract `notes/.../CORRECTION_PROTOCOL.md` | SHA-256 `8cb3096af2fa93cde689122eb2d17e4ce4ee64c6fa241ae88f3b00d669376140`, 4131 bytes |
| Imported original verifier | SHA-256 `a349d3fc0711a59e6174a2534b47c62df766b1f6ab82e0e215ebcd8a596f26c7`, 33053 bytes (unchanged since pin `24cc067983142017d3fd9a111acf80d6ab29db54`) |
| Checked original stdout | SHA-256 `dccec8381f051efede09b61cea2b15c6735a883a4286e2d13c131bc2ea0164d3`, 1162 bytes |

## Execution

| Field | Value |
|---|---|
| Checkout | clean detached worktree of the correction pin; still clean after the run (no bytecode written) |
| Command | `python3 reproduce/C-HOMOGENEOUS-RECORD-RETENTION-BALANCE-N/verify.py` from the repository root |
| Environment | `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC` |
| platform | Ubuntu 24.04 |
| architecture | x86_64 |
| Python | 3.13.17 |
| Time (UTC) | 2026-10-24T18:21:50Z to 2026-10-24T18:21:55Z, about 5 seconds wall time |
| Exit code | 0 |
| Standard error | 0 bytes |
| Standard output | 696 bytes, SHA-256 `e11c1c3738605723ab6d620bca10acbc117f1e5687205aaec73eaa67d5488c66`, saved unchanged as `EXPECTED.txt` |
| Checks | 112 (groups 0–3: 4, 100, 6, 2) |

This was the only execution at the frozen instance. Before the pin, the audit
functions were exercised on non-frozen toy instances only, as disclosed in
`CORRECTION_PROTOCOL.md` §4. The pull-request workflow reruns this verifier on
x86_64 and aarch64 and compares its stdout byte for byte.
