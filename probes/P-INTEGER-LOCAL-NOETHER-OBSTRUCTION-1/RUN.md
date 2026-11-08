# First formal run

pin_commit: 6c257b169054625aa608974c1c6a264fb56e5d02
verifier_sha256: 912ddf907dc2f88d7322cca3581beba3e90686165061e8c360546c7959add03a
command: python3 probes/P-INTEGER-LOCAL-NOETHER-OBSTRUCTION-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: d37addee43da071da1e4aa702b2408b9b5dd4b8fed38a5666a84bb3b8d3d825a
stdout_bytes: 508
stdout_lines: 19
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The first execution followed the public six-file readback receipt on issue
#1661 (comment 6279453073). The primary executed the separate breaker with
the same interpreter and -I, required an empty stderr and exit zero, and
compared unmodified raw certificate bytes. No scientific execution preceded
the pin. The result packaging changes no frozen scientific file.
