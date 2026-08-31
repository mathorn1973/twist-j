# P-C8-MARKING-RIGIDITY-1 formal run record

pin_commit: 3ccb245b565b77fdd05636c1b91dcd6e99629457
pin_tree: 972b64cb4c844bff8834837375eaefa48c347c6d
base_commit: 64055c8a2879668c5bf79eea8cdef067f0ac95a2
public_lock: issue 729
prereg_sha256: 73d058b3200263c2cd8291cc11de2389f2cb4e0bdd3e92e5a9f553c97016c689
prereg_bytes: 6977
verifier_sha256: 416ff70a8c32a2457f131759d4d7e7cee0386ac21a9d0cb37ae69f99d2ad85df
verifier_bytes: 6723
command: python3 probes/P-C8-MARKING-RIGIDITY-1/verify.py
environment: env -i PATH=/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin LC_ALL=C LANG=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC
platform: macOS 26.5.2, reported by platform.platform as macOS-26.5.2-arm64-arm-64bit, fleet node STUDIO
architecture: aarch64
python: CPython 3.9.6
clean_checkout: yes, dedicated git worktree at the pin commit, no untracked or modified files at execution
working_directory: repository root of that worktree
architecture_gate: local aarch64 audit complete; required x86_64 and aarch64 workflow pending
public_readback_before_execution: yes, issue 729 comment 5477760531
formal_executions: 1
exit_code: 0
stdout_sha256: 783e32ec52372c9d47519276ccf0fb2d5853d3c2692dafa37435f6fb01f2bc90
stdout_bytes: 709
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 6/6 ALL PASS
pinned_files_unchanged_after_execution: yes

The verifier is standalone and reads no repository files. EXPECTED.txt is the
exact captured stdout of the single formal execution, not a transcript composed
from the expected mathematics. The reported architecture token is the spelling
required by tools/check_verifier.py; the machine reports the same architecture
as arm64.

The first execution used the portable command field above, so no command-field
normalization was needed. Repository checkers were not run locally; they belong
to the required public workflow.
