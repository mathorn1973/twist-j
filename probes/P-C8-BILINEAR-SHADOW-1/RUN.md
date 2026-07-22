# P-C8-BILINEAR-SHADOW-1 formal run record

pin_commit: c5c6db7bbba3daac1c831528acae632b1925e0bf
base_commit: 434e02a01903ef7a237053eac1231dbe7496bbf5
prereg_sha256: b990ad96c0832d470b678bdb010554e6cdf44a969472c92ce583dc3acef5e344
verifier_sha256: 542823134665618e8f1211aeabafafd22aa104654144bec8ac52ea72f56546d6
command: python3 probes/P-C8-BILINEAR-SHADOW-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
clean_checkout: yes
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: cc194c8da06d4873d6b279bbc658d2aade71be70dfa877dbdb0ab892d15c3a62
stdout_bytes: 1100
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 6/6 ALL PASS
public_lock: owner directive of 2026-07-22; issue number attached by the owner at pull-request time

The formal run used a clean detached checkout of the exact public pin commit.
The separate raw stdout and stderr files are retained for audit. The machine
is recorded only by neutral platform and architecture descriptors. An
informal pre-pin dry run of the same verifier bytes on a cloud x86_64
container produced byte-identical stdout (disclosed in PREREG systematics as
source material); the required formal x86_64 leg is the GitHub check at
pull-request time.
