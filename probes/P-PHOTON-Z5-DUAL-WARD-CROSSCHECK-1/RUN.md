# P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1 formal run record

Status: `STOP_DUAL_MIXING / ZERO_ENGINEERING_ONLY / COMPLETE LOCAL RECORD`.

## Immutable public pin

```text
pin_commit: afb896b71a5721c9704ab64f172e3de7df71ca02
parent_commit: ec84f7bd153a32068b8a267ea75dfc179ad8ba47
pin_tree: 17b8a3ec6e60e8dc9761e7ad5bcb4cf48c1636b6
public_issue: 756
pin_receipt: https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5495151506
source_manifest_sha256: 40bfff46f61619e4fc40065afa8e9c0dd1b89728462d175e6040948b89f2eaf9
input_manifest_sha256: 31aab8dfcda1d22377f6aa346467222b80a7b2b6ac72cf73465ed63f4d97d780
```

The public branch ref, commit, parent and all package bytes were fetched and
compared with the local package before execution. The fetched package diff was
empty and the fetched nine-entry source manifest matched the frozen hashes.
No `L=6,8` decision chain existed before that public readback.

## Sole formal local leg

```text
command: python3 probes/P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1/verify.py
orchestration_command: python3 run_crosscheck.py
environment: LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
platform: Ubuntu 22.04.5 LTS / Linux 6.6.87.2-microsoft-standard-WSL2
architecture: x86_64
python: CPython 3.10.12
compiler: g++ 11.4.0
boost_headers: libboost-dev 1.74.0.3ubuntu7 / BOOST_VERSION=107400
completed_at_utc: 2026-09-01T14:06:19Z
formal_runs: 1
driver_exit_code: 0
child_exit_codes: all 0
captured_child_stderr_bytes: all 0
verifier_sha256: c25c2ac1305f9244375bb02008e822201f8e6768cd269a58af86b2884d7f450d
exit_code: 0
stdout_bytes: 511
stdout_lines: 7
stdout_sha256: 33279470394266ebbbce1b4cba24751e424583cca2faf1b51dfd4384f9a881dc
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
result: STOP_DUAL_MIXING
evidential_status: ZERO_ENGINEERING_ONLY
```

The driver revalidated the nine source hashes and nineteen public input hashes,
matched the small frozen fixture, compiled the inherited primal kernel, ran the
four exact primal replays and eight independent dual chains, wrote the custody
records, analyzed them and invoked the formal verifier exactly once. The
driver and verifier were not rerun after the terminal was produced.

## Raw and derived custody

```text
raw_logs: 12
raw_samples: 6144
raw_bytes: 12347567
dual_markov_steps: 33128448
PRIMAL_RUNS.tsv: bytes=682 lines=5 sha256=5fa9f54593d79be603ca85b22e406ce00df73e94b6810c9b7eb6804be8acde03
DUAL_RUNS.tsv: bytes=1384 lines=9 sha256=eb0bc949c55d37114473cd04d6884cdcede226a1ace073ebc56dcf5c8f854b35
OUTPUT_SHA256SUMS: bytes=1307 lines=15 sha256=c9ecf3189e9162329700cb649ab6c2a1aa50041869e2a94b95742e59235a4a62
ANALYSIS.txt: bytes=15640 lines=180 sha256=563e2d07e80486e3db6e2ee40e16d05cf29e02a236d39a385025c12df5f52b72
EXPECTED.txt: bytes=511 lines=7 sha256=33279470394266ebbbce1b4cba24751e424583cca2faf1b51dfd4384f9a881dc
```

Every raw file is regular printable ASCII/LF text below the policy size cap.
The two run tables record the frozen schedule, byte count, SHA-256, exit zero
and empty stderr for each raw transcript. The verifier checked those fields
semantically against all twelve transcripts, replayed `ANALYSIS.txt` byte for
byte and emitted `OUTPUT_CUSTODY PASS` and `ANALYSIS_REPLAY PASS`.

## Frozen terminal audit

The primal mixing audit passed at both volumes with zero failures. The dual
audit returned 57 failures at `L=6` and 60 at `L=8`. The smallest reported
per-chain ESS was `3.56722` against `64`; the smallest pooled bulk ESS was
`6.33387` against `200`; the largest split Rhat was `1.66461` against `1.05`;
and the largest half-drift z was `5.26172` against `4`.

At both volumes every dual chain had zero variance in `j2_mean`,
`j_nonzero_density` and all four lowest-momentum `j` powers. The odd `n_mean`
mode also had zero variance in three `L=6` chains and all four `L=8` chains.
These failures select `STOP_DUAL_MIXING` before any statistical dictionary
residual can acquire decision authority.

## Public deterministic replay

```text
status: PASS
workflow_run_id: 33518375898
workflow_url: https://github.com/mathorn1973/twist-j/actions/runs/33518375898
event: pull_request
evidence_head: f14986b53ba063cb77abc54bc4ef6710082deded
tested_merge_commit: 7d1de970b226e3563ffda54b799d370600e1db2f
base_commit: ec84f7bd153a32068b8a267ea75dfc179ad8ba47
x86_64_job_id: 99891064719
x86_64_job_url: https://github.com/mathorn1973/twist-j/actions/runs/33518375898/job/99891064719
x86_64_result: success
aarch64_job_id: 99891064984
aarch64_job_url: https://github.com/mathorn1973/twist-j/actions/runs/33518375898/job/99891064984
aarch64_result: success
aggregate_job_id: 99891196408
aggregate_job_url: https://github.com/mathorn1973/twist-j/actions/runs/33518375898/job/99891196408
aggregate_terminal: TWO-ARCHITECTURE CHECK PASS
X86_VERIFIER_SHA256 = c25c2ac1305f9244375bb02008e822201f8e6768cd269a58af86b2884d7f450d
X86_STDOUT_SHA256 = 33279470394266ebbbce1b4cba24751e424583cca2faf1b51dfd4384f9a881dc
X86_STDOUT_BYTES = 511
X86_STDOUT_LINES = 7
X86_BYTE_IDENTITY = PASS
ARM_VERIFIER_SHA256 = c25c2ac1305f9244375bb02008e822201f8e6768cd269a58af86b2884d7f450d
ARM_STDOUT_SHA256 = 33279470394266ebbbce1b4cba24751e424583cca2faf1b51dfd4384f9a881dc
ARM_STDOUT_BYTES = 511
ARM_STDOUT_LINES = 7
ARM_BYTE_IDENTITY = PASS
```

Both public jobs passed policy, all 148 tool tests, Canon, Ledger and gate
contract checks before reproducing the canonical verifier output byte for
byte. They replayed only the committed deterministic record and did not
regenerate any chain.
