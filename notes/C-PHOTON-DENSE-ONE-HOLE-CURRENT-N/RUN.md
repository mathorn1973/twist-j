# RUN - C-PHOTON-DENSE-ONE-HOLE-CURRENT-N

**Status:** candidate-C audit only. Not a formal public probe.
**Owner:** #1204.

## Frozen custody

- preregistration commit:
  \`5ad0eac6708e1df2d100769943bf3805f203b3a4\`
- PREREG blob:
  \`4a29e4ad44f7866e098b2cbc2dbe2fc80b07afe3\`
- verifier commit before first execution:
  \`a34e2ace6f323b7a255d71985205abf404fc42a9\`
- verifier blob:
  \`984f0df97cde157c1dfdfca5d8375a75a67b7b22\`
- PREREG SHA-256:
  \`26ac6677855c483e09d8209e23b4c627695edb5cf2a819a73054a64def50ef85\`
- verifier SHA-256:
  \`e95d7cce6afd866fe488f04e4e38b8d6bd78d9b6bda70c65baa294d35930194c\`

PREREG.md and verify.py were publicly read back before execution.

## Clean-clone run A

\`\`\`text
architecture: aarch64
python: Python 3.11.2
head: a34e2ace6f323b7a255d71985205abf404fc42a9
verify_sha256: e95d7cce6afd866fe488f04e4e38b8d6bd78d9b6bda70c65baa294d35930194c
exit_code:0
stdout_bytes:511
stderr_bytes:0
\`\`\`

## Clean-clone run B

\`\`\`text
architecture: aarch64
python: Python 3.12.3
head: a34e2ace6f323b7a255d71985205abf404fc42a9
verify_sha256: e95d7cce6afd866fe488f04e4e38b8d6bd78d9b6bda70c65baa294d35930194c
exit_code:0
stdout_bytes:511
stderr_bytes:0
\`\`\`

The two connected ARM systems produced byte-identical stdout. This is
same-architecture reproduction, not the repository two-architecture scientific
gate.

Exact stdout:

\`\`\`text
PASS L=4 A=640 M=256 A_over_M=5/2 edge_degrees=0:128,2:640,5:256 B_zero=YES ell=0 R3_component=16777216/4
PASS L=6 A=3240 M=1296 A_over_M=5/2 edge_degrees=0:648,2:3240,5:1296 B_zero=YES ell=0 R3_component=2176782336/4
PASS L=8 A=10240 M=4096 A_over_M=5/2 edge_degrees=0:2048,2:10240,5:4096 B_zero=YES ell=0 R3_component=68719476736/4
PASS L=10 A=25000 M=10000 A_over_M=5/2 edge_degrees=0:5000,2:25000,5:10000 B_zero=YES ell=0 R3_component=1000000000000/4
ALL PASS: dense one-hole current family audit complete.
\`\`\`

The universal even-L statement rests on the written proof. The runs are finite
exact audits only.
