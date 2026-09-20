# RUN: P-J-HODGE-SEMILINEAR-MEMORY-2

pin_commit: 2f34766829481d92018588409308eb1368deb20d
verifier_sha256: 091c89279317986d4e5d9610569415d2d3f2729e4068bbf222a3796456efff8a
command: python3 probes/P-J-HODGE-SEMILINEAR-MEMORY-2/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: a8f2f972e0d30fb809a6d8526ae9ef84d236e984e42737f2e8103f1cc7daf8af
stdout_bytes: 534
stdout_lines: 12
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

prereg_sha256: 1edf5a258d8655218521ed1ffa0927441fb44f5aa873e1e5dc40a1b1c2cea292
proof_sha256: 97078ad1a9e6d04aa8ae2dd8a04c00b2889440700aa0a2fd0e5dbc7203b16665

The first valid scientific execution followed public readback of the atomic
three-file pin. The exact pinned verifier was materialized byte-for-byte and
its SHA-256 matched the public file before execution.

The repository-relative command ran with LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.
EXPECTED.txt contains the actual stdout.

This is one local x86_64 lane. Required clean GitHub x86_64/aarch64 replay and
the aggregate check remain the public computation gate. No independent-agent
or result-blind review is claimed.
