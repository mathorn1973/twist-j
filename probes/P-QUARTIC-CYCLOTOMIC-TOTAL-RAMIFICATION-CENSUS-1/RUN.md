# P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1 formal run record

pin_commit: 7291c079811a2a0191ab536590f7a5d723a9a7c7
base_commit: f8c4cc64ba4fc21723fc3e715b5a40036ef7b404
prereg_sha256: f8ac045f4f35a87a04a4f8578b1bb1a8b69c75f8434d981fc6d77e71ffea9e72
prereg_bytes: 19692
prereg_git_blob: 70c6bf019c7d86c84f53d273cd90489d7807d97b
verifier_sha256: 60fd58dc3eeab0e40bf0b2ab04e05690b4a1cc088cade4ce500007ce930c1539
verifier_bytes: 18225
verifier_git_blob: 0ea124bc0ec838566b35d82728be8c6e91860e58
command: python3 probes/P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
run_started_at: 2026-08-03T09:19:55Z
run_finished_at: 2026-08-03T09:19:55Z
pre_run_clean: yes
post_run_clean: yes
architecture_gate: formal aarch64 leg complete; required GitHub x86_64 and aarch64 replays pending
deterministic_executions: 1
exit_code: 0
stdout_sha256: 88413e040ab1c10d88dc64611a0f7e7d259c3ac6301b3f213707107c06d9822a
stdout_bytes: 1031
stdout_lines: 11
stdout_cr_bytes: 0
stdout_final_byte: 0a
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 9/9 ALL PASS
public_lock: issue 256
blind_breaker_commit: 3d550f27a326aa1a49c34ac111f6723806562c50
blind_breaker_sha256: 316f014dfe579136e20d84907ad0e9b6362ec3e101174deee9c68e3d35bf4875
blind_breaker_stdout_sha256: f6fec277be2d7984c1b541cc86cdb67eadfee307dd9879a72aef2bdf528384ef
blind_breaker_result: NO BREAK FOUND 10/10

The formal run used a fresh, isolated fetch of only the public builder branch
and a clean detached checkout of the exact pin commit. Before execution, the
public branch tip, both frozen file SHA-256 values, byte counts, Git blobs, and
Public Canon v32 identity matched the pin. The checkout contained only
`PREREG.md` and `verify.py` in this probe directory; the breaker branch and
`break.py` were not fetched or opened.

Raw stdout and stderr were captured separately outside the worktree. The
machine is recorded only by neutral platform and architecture descriptors.
`EXPECTED.txt` is the exact ASCII, LF-only stdout and has a final LF.

The independent breaker metadata above is transcribed from the public freeze
record in issue #256. No builder-side code comparison with `break.py` has been
performed. Both required GitHub architecture replays remain pending.
