# P-U-PISTON-GRAM-DESCENT-1 first author run

pin_commit: 25a9034379fccb29d1408d505fa5dfd6319b6e6d
base_commit: d4d363722f052141a4ce65e9da39f11a74b43b95
execution_commit: bd2d5658d32837a3d8113d751cae0960d97b0807
branch: probe/P-U-PISTON-GRAM-DESCENT-1
prereg_sha256: 9c6cc1cbbfcd50779f52dcdf1e77b4d6cc8b068b69996ff19807cf6ab7d47a1a
prereg_bytes: 12715
prereg_git_blob: 449b73b6f7675c277de79145f4dac08b1c6fe1f0
verifier_sha256: 7f7e78cb75a3e29d4eae9210aa715454fdcbdfbd5cf93108fd1eea1e4b01831c
verifier_bytes: 10481
verifier_git_blob: a4e5443fcea273ca0f3144cf58fb23d0684e204c
command: python3 probes/P-U-PISTON-GRAM-DESCENT-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.12.14
run_started_utc: 2026-11-07T21:22:42.169315+00:00
run_finished_utc: 2026-11-07T21:22:42.569571+00:00
detached_checkout: yes
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 1efb8cfdc2c2c6c157c77913a847476c4790f44ecfae23f0d08b9fbf325a5599
stdout_bytes: 2303
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
run_integrity: PASS

The accepted verifier was executed once after both scientific programs were
publicly frozen and read back. The execution commit adds only the independent
breaker to the original three-file preregistration pin. Neither source was
changed, imported or executed before its freeze. The first exact stdout is
EXPECTED.txt; it was published on issue #1949 before these run records.

The independently authored breaker produced exactly the same bytes on this
architecture. Its distinct method and custody are recorded in INDEPENDENT.md.
This local record alone is not a two-architecture gate. The unchanged required
pull-request workflow must replay this verifier on x86_64 and aarch64 against
this one EXPECTED.txt. No workflow success is asserted in advance here.
