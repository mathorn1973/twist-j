# First local verifier run: P-QDD-UNINTERRUPTED-RECORD-1

pin_commit: a6c66f3b5ae9c75f35980816a2b00007f366bdc2
verifier_sha256: 2f4ee7d4fdb86c69082ecdd31eeb1c20c8c59940dddb215a031e01b391c34136
command: python3 probes/P-QDD-UNINTERRUPTED-RECORD-1/verify.py
exit_code: 0
stdout_sha256: 876bb254aa77fe5be6ec4a79ec4905bc71ec3ac17176b0fda5750e89cd471347
stdout_bytes: 689
stdout_lines: 12
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
prereg_sha256: dc68075257665e2ff826b2afe21413dc3ecee2b2348b6bca1d92e803412b6251
proof_sha256: e633e4031cc246dc2c41763209d38592b37b8b2babd9da8dc19f57f3708e4efe
break_review_sha256: 3dd0dd76eae7ed124add84bab20f0c6d29f9f977d95dd5188ecc3c476f619f9d

The first execution followed byte-identical public readback of all seven
frozen files and a clean checkout of the exact pin. Environment: LC_ALL=C,
LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC. The seven
files remained byte identical after both executions. This is the local
run record; public architecture acceptance is separately recorded in
ACCEPTANCE.md. The breaker is not counted as a second architecture.
