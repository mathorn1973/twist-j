# P-C8-PAULI-QUOTIENT-TRANSPORT-1 formal run record

pin_commit: 9a9a54abb09eb053e379b288214e16aaaa1165e9
pin_tree: 89e8948194cc6e0815233f65f5a43801adbbd5f3
base_commit: 9f88c4c93aab3139ee0a2e007f0e60891957aa21
public_lock: issue 724
prereg_sha256: e14d76de51c9c2d666c8baba008d16a73c2c12a20da320ec0bbbbe97b822bd35
prereg_bytes: 14084
verifier_sha256: 091c2c924ab4ce530e556ebd8c99a128abc8b76bfb7ac764217efb8de452de2f
verifier_bytes: 10667
command: python3 probes/P-C8-PAULI-QUOTIENT-TRANSPORT-1/verify.py
resolved_executable: /opt/pyvenv/bin/python3
initial_command: /opt/pyvenv/bin/python probes/P-C8-PAULI-QUOTIENT-TRANSPORT-1/verify.py
environment: env -i PATH=/opt/pyvenv/bin:/usr/local/bin:/usr/bin:/bin LC_ALL=C LANG=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC
initial_environment: env -i PATH=/usr/local/bin:/usr/bin:/bin LC_ALL=C LANG=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: CPython 3.13.5
clean_checkout: not claimed; exact pinned payload files only, matched to public Git blob IDs before execution
working_directory: repository-relative payload root
architecture_gate: local x86_64 audit complete; required clean-checkout x86_64 and aarch64 workflow pending
public_readback_before_execution: yes, issue comment 5476772274
formal_executions: 2
exit_code: 0
stdout_sha256: 7b947696bae49095be87d37d6551825537b67c7833df5405953d9b75dc3e79c6
stdout_bytes: 664
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 7/7 ALL PASS
pinned_files_unchanged_after_execution: yes

The verifier is standalone and reads no repository files. This local run does
not claim a full repository checkout or locally executed repository checkers.
Those checks belong to the required public workflow. EXPECTED.txt is the exact
captured stdout, not a transcript composed from the expected mathematics.

## Command-field normalization

The first public workflow (33380984891) rejected the absolute interpreter
spelling in the command field before executing this verifier. Both architecture
jobs had already passed policy, unit, Canon, ledger, and gate-contract checks.
The initial local invocation and its environment are preserved above. A second
local execution used the exact portable command required by check_verifier.py,
with python3 resolving to the same CPython 3.13.5 environment. It returned exit
zero, empty stderr, and the same 664 stdout bytes. Neither pinned file nor
EXPECTED.txt changed. This is a run-metadata correction, not a new scientific
threshold, altered verifier, or replacement result.
