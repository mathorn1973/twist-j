# RUN: P-ENTROPY-MEASURABLE-OBSTRUCTION-1

pin_commit: 8b434780ac9cc5c730a2ff4ef3c8ac57273d7bf3
verifier_sha256: f218660199821a73e3a6117abe8e2ba60f86335eb7c1a4ebbbee8b1470ffb5a8
command: python3 probes/P-ENTROPY-MEASURABLE-OBSTRUCTION-1/verify.py
exit_code: 0
stdout_sha256: e63aee0b6e4141b53bb54635fc874b7e1352c8ad807ac071dea36d8de84aa0a7
stdout_bytes: 667
stdout_lines: 12
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
prereg_sha256: 4cb11d85040d1144d161a22888f679312fa159906ea0715467fd65f0c7f4b8ce
proof_sha256: 4c97f04b282e99d7a804a904968fde0861b2d06634a60ab5fc9306fde3cf3cf3
break_review_sha256: 05e92872411b5de5986b868a61847033b7380f75bf865b7d215e141c535ba44c

First execution followed byte-identical public readback of all five pinned
files. Environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. This records the local execution only. Public
architecture acceptance is recorded separately in ACCEPTANCE.md.
