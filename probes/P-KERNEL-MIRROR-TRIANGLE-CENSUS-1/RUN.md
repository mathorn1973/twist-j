# RUN: P-KERNEL-MIRROR-TRIANGLE-CENSUS-1

pin_commit: 0d8142c85f1522ed16827a3d794482cc21a15cc9
prereg_sha256: 96836285b2e4a16b9f323e8168e661f360cb0d595e50e98a391bba1ea9f727e5
verifier_sha256: c93b6c6c2643af149d4464244cc639163cbada04da8904985d3b26d1c52d6c5f
companion_sha256: 880f670d8cd9eda087c8b145527c70743c376bfca9ccb3290822c948f088c9b9
command: python3 probes/P-KERNEL-MIRROR-TRIANGLE-CENSUS-1/verify.py
platform: Ubuntu 22.04.5 LTS (WSL2)
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: c9f71fc2b8211ec670df610ef2d108e16861b1a3fb0b743d7e8bf122551519d0
stdout_bytes: 4342
stdout_lines: 62
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The first formal execution occurred on 2026-10-05 after the pin was pushed.
The remote branch commit was read back, and GitHub's contents API returned
PREREG.md, verify.py and crosscheck.py bytes matching the three hashes above.
The worktree was clean before the run. PREREG.md, both code files and both
proof texts are unchanged from the pin. README.md subsequently adds links
to the actual run and result.

The command ran from the repository root with LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC. EXPECTED.txt is the
actual stdout, including its original whitespace. No supplied historical
transcript was used as the new expected output. The companion's SHA-256 is
checked by the main verifier before import.

Local result: 27/27 PASS. All 21 structured census records agree between
the two implementations. This is one local x86_64 lane.

The existing public PR workflow completed both architecture jobs and its
aggregate check at head `afb5062fdbb5751dc1ad67ce321e56cec113ea8f`:
[run 37290826956](https://github.com/mathorn1973/twist-j/actions/runs/37290826956).
Both job logs report VERIFY PASS with the exact verifier and transcript
hashes below. Both also pass 183 repository-tool tests and the policy,
Canon, ledger and gate-contract checks. These are neutral replay receipts;
they change no frozen source, proof, target or scientific stdout.

## GitHub x86_64

| Recorded field | Value |
|---|---|
| Platform | Ubuntu 24.04 (GitHub-hosted) |
| Architecture | x86_64 |
| Python | 3.12.14 |
| Verifier SHA-256 | c93b6c6c2643af149d4464244cc639163cbada04da8904985d3b26d1c52d6c5f |
| Stdout SHA-256 | c9f71fc2b8211ec670df610ef2d108e16861b1a3fb0b743d7e8bf122551519d0 |
| Status | PASS |

[Job 111700543774](https://github.com/mathorn1973/twist-j/actions/runs/37290826956/job/111700543774).

## GitHub aarch64

github_platform: Ubuntu 24.04 (GitHub-hosted)
github_architecture: aarch64
github_python: 3.12.14
github_verifier_sha256: c93b6c6c2643af149d4464244cc639163cbada04da8904985d3b26d1c52d6c5f
github_stdout_sha256: c9f71fc2b8211ec670df610ef2d108e16861b1a3fb0b743d7e8bf122551519d0
github_exit_code: 0
github_stderr_bytes: 0
github_status: PASS

[Job 111700544135](https://github.com/mathorn1973/twist-j/actions/runs/37290826956/job/111700544135).

The two-architecture computation gate is satisfied for the pinned code and
the one committed EXPECTED.txt. Public acceptance and a Canon fold remain
separate from these receipts.

The later receipts-only head `e22496a3739629c6fbd9f7f78e38069b92256111`
was rejected by the run-record parser for repeating unstructured fields.
This record uses the supported named GitHub leg for aarch64 and a separate
table for the same-architecture x86_64 receipt. The correction changes no
pinned code, proof, target or scientific output; the failed metadata check
remains in public commit and workflow history.
