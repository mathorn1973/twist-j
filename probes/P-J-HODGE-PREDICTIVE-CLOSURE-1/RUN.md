# First formal local run

pin_commit: 8766a31ccbcb59db8b5161fcd186852c1e773fd9
prereg_sha256: b47430d93a809bd181fb75ecf3bdca569096ba45feef80d2569a4ddbfea5e009
verifier_sha256: 3938e0d23cf5003fb022263dd5c360ddf3fed3ad41d974ba4c37936adb803cbc
command: python3 probes/P-J-HODGE-PREDICTIVE-CLOSURE-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 8b02840a92462b82e41ebc2526e069587f4435f73a6f221b928422209776c596
stdout_bytes: 258
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
