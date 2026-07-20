# P-TM-SYM2-FRAME-1 formal run record

pin_commit: d36c3304b796596456dbc070b3fa5cd73fe97044
base_commit: 3d8c6307f20d01ad50fc90ae1c5777926b884881
prereg_sha256: 9ac19d18e8d1836f16024c27be15e450646b624b693f90920187cc00a44ebe63
verifier_sha256: 4b84f8ddf35be025224ba5d3a44159ffecd5e93face5a0536971357928083135
command: python3 probes/P-TM-SYM2-FRAME-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
clean_checkout: yes
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: d144486d47039ea3b2a4402647df315fba55d265788e7d1b8d56124e7ea98f43
stdout_bytes: 742
stdout_lines: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: POSITIVE 8/8 ALL PASS
public_lock: issue 92

The formal run used a clean detached checkout of the exact public pin commit.
The checkout and the separate raw stdout and stderr files are retained for
audit. The machine is recorded only by neutral platform and architecture
descriptors. `EXPECTED.txt` is the exact 742-byte LF-only stdout.
