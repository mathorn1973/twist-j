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
the two implementations. This is one local x86_64 lane. The existing
public PR workflow supplies the separately required x86_64/aarch64 replay;
its completion and exact head must be checked before claiming that gate.
