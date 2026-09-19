# First formal local run

pin_commit: f259d00e471ef22fa3417dd7967601cd1b24aa52
prereg_sha256: 64132f29159199daae5f083f55ba576c3699077efe2b3f2857b4708a99cc9af8
verifier_sha256: 28424856e7143cb593872bdc7a8c1654de6bd1a874cdb231330e8eb67b1d0161
command: python3 probes/P-A4-RAMIFIED-HODGE-TRACEKERNEL-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: ef3db1b8d206623316dfc253738cb8e644e41b3f3036ebd5574b0b1639a9de5d
stdout_bytes: 308
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The two pinned source files were publicly read back from the reserved GitHub
branch before this first execution and matched the recorded byte counts and
SHA-256 values exactly. Network checkout is unavailable in the execution
container; the formal local tree was reconstructed from those exact read-back
bytes and run from its repository root. No source byte was changed after the
pin.

The local run is one x86_64 lane only. It is not the required public
two-architecture gate. The unchanged verifier must replay against the one
EXPECTED.txt on the required GitHub x86_64 and aarch64 jobs.
