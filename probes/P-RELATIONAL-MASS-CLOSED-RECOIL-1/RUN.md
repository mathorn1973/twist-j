# First formal run

pin_commit: 616dff679d5f66f057b4c9a45a10ef7bc621b403
verifier_sha256: 2e976f269745e22aadfd1d0ff26ad4dddd542ac06eea5f0d761fd7098389d2c6
command: python3 probes/P-RELATIONAL-MASS-CLOSED-RECOIL-1/verify.py
platform: Linux, ('glibc', '2.36')
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_bytes: 221
stdout_lines: 10
stdout_sha256: 7b6fece8823903c4f54acac7288226328d40302adeb6a165fd70daf2213f5c7e
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
started_utc: 2026-10-20T20:01:38.071769+00:00
finished_utc: 2026-10-20T20:01:44.846014+00:00
elapsed_seconds: 6.774
timeout_seconds: 60

The displayed command is the actual first execution and the repository
replay command. The exact-pin worktree was clean before and after execution.
All six prospective files were read back at the public commit; complete text
and independently calculated Git blob identities matched before execution.
The manifest was checked again immediately before the scientific process.

| File | Public blob |
| --- | --- |
| PROOF.md | 0d8e80d0e505d89d18c700c1fc8c8233cf7b6d7c |
| FIXTURES.md | 4a31b3f91044080f618ec0e50a34214f22622edf |
| FROZEN.sha256 | c52bb1bd421bb6b85cd4c3fdd403c125c0dc3863 |
| SOURCE.md | 9d26d5ef3bf265592839ee027059c966bdcb52db |
| verify.py | 277241eea57cf0b545223d49b8cba6e9bf40f9ae |
| PREREG.md | 1ec659413d60f244331c196ca19ab9d840e65b39 |

Only analytical derivation, source reading, static review, AST parsing and
hashing preceded this run. No scientific import or trial execution occurred.
The child used LC_ALL=C, LANG=C, TZ=UTC, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0 and the existing executable PATH. Exact stdout/stderr and
metadata were captured outside the tracked tree. EXPECTED.txt is copied
byte for byte from this actual stdout. No edited retry occurred. Required
public PR architecture replays are a separate gate recorded on the PR.
