# V2 full-state comparison receipt

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.
Scientific pin: 4947a92a5e5ca471e7acde009ef255e17a61a493.
First-run record: beeabbe9cbb493212b0868b7d25ebacfdab6785e,
public receipt #1516 comment 6190895477.

Own comparison mode ran only after the complete ordinary PASS and public
first-run record, on the same clean immutable Linux checkout. All 1200
chronological full-state arrays are computed from direct dynamics. No
counterpart scientific content has been opened. The output below is our
own digest, not a claim of cross-implementation equality.

```text
TWOUSE-COMPARE-v2 domain_sha256=2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 records=1200 sha256=670f270e88386e2f1f507e24ec0ae71daf1ff6638ea44783b793479291af3dbc
```

```text
command: python3 probes/P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-2/verify.py --compare
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
start_utc: 2026-10-15T11:24:01.839512+00:00
end_utc: 2026-10-15T11:24:04.098251+00:00
elapsed_seconds: 2.2587355180003215
exit_code: 0
stdout_sha256: 77348e12d9948ebafc15c15ea9904b53ece6a30990ea59a59633a1bef8c21c8d
stdout_bytes: 182
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Deterministic environment and 600-second limit are identical to RUN.md.
DOMAIN is silently validated before serialization. The v2 header binds the
G1 domain hash before the 1200 JSON/LF records. Large transcripts are not
committed. The old v1 comparison remains NOT_RUN.

Cross-implementation status: PENDING. At this record only I2's CLAIMED
metadata is visible; no new I2 pin/first-run receipt has been established.
Only comment marker names, URLs/times and 40-character commit metadata were
read through a filter, never scientific code, output or comparison digest.
Both independent successor pins and first records plus V2 dual-architecture
scientific replay are prerequisites for opening and comparing peer evidence.

## Architecture prerequisite completed

Both actual V2 scientific replay jobs and aggregate check passed in run
38727305980, as evidenced in REPLAY.md. The I2 pin/first-record prerequisite
remains pending at this receipt; no cross-lane equality is asserted.
