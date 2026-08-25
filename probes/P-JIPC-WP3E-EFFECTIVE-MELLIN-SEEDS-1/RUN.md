# P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1 run record

pin_commit: 46004772f3a6510791adf2ae4afd14a8a9f7f5af
verifier_sha256: 373ff274abcc27e06b12e8aee1ebd0bfc0de6bebbc66ed69e1c53e87a06369d1
command: python3 probes/P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: Python 3.10.12
exit_code: 0
stdout_sha256: f51edb6ed4d7733abca72ea45e091cfa9241c36848b9509d532828e609cc2056
stdout_bytes: 407
stdout_lines: 12
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

base_commit: 505f4096453a52bacb8c8de26583b38874ea408b
claim_issue: https://github.com/mathorn1973/twist-j/issues/566
prereg_sha256: af078f17645dc8b5ef78acefb53bf73b791045efd2147bf2d87ed5006e9bdd80
prereg_bytes: 28884
prereg_lines: 829
prereg_blob: 431b2d7163c29022165429e6d4daac83aa0beb71
verifier_bytes: 32304
verifier_lines: 976
verifier_blob: c4297a592c4daa9f99806110681ca01d0a06fec1
encoding: UTF-8
line_endings: LF
final_lf: yes
public_readback: PASS
formal_execution_count: 1
elapsed_wall_seconds: 1.671

The immutable two-file pin was pushed before execution and read back from a
second clean checkout of the public branch. Both pinned files matched their
recorded SHA-256, Git blob, byte count, line count, LF-only encoding and final
LF. The exact command recorded above then ran once from that clean checkout in
a neutral Linux environment with no inherited Python path or user site and a
600-second hard timeout. It completed before the threshold, produced the
committed stdout bytes and wrote empty stderr.

The local record is one x86_64 execution. The required public Python 3.12
x86_64 and aarch64 pull-request legs remain a later architecture gate and are
not fabricated here.
