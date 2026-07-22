# P-C20-TEICHMULLER-SPLIT-1 formal run record

pin_commit: 22b33ed99fce414f3cce53f664900610a990ef3e
base_commit: 434e02a01903ef7a237053eac1231dbe7496bbf5
prereg_sha256: 7b268c4121bf8413c005525d377262f7c92f2480ae7a7c7fc870425bc8357bf4
verifier_sha256: c0909d286b634edeaae867767549a5f8d98a8e80102462a10ea6b368e7ec43fe
command: python3 probes/P-C20-TEICHMULLER-SPLIT-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
clean_checkout: yes
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 leg pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: 5f4822f9b49d3936d98289f9374de291d2810d27daeada2a16a468670fd05e9e
stdout_bytes: 918
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
