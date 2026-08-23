# P-J-ODD-MOTOR-BRIDGE-HARDENING-1 run record

Status: **FIRST FORMAL EXECUTION COMPLETE. LOCAL x86_64 REPRODUCTION ONLY. PUBLIC TWO-ARCHITECTURE GATE PENDING.**

```text
claim lock:       issue #536
branch:           probe/P-J-ODD-MOTOR-BRIDGE-HARDENING-1
base commit:      94bca32b151e161322c4437e8317a03e653e35fa
pin commit:       11f168d72e6301e4cfd8c892f67525c5d7c66d8f
formal run count: 1
command:          python3 verify.py
exit code:        0
stderr bytes:     0
stdout bytes:     706
stdout lines:     19
stdout final LF:  yes
stdout SHA-256:   ba9cb5e6edc0efb297ee9fd5213dd6da9ff3a9b641a00ea96107bd9ea7917ac7
```

## Immutable pin readback

Both accepted files were fetched from the exact pin commit before execution.
Their Git blob IDs agree with local `git hash-object`, so the executed verifier
bytes are exactly the public pinned blob.

```text
PREREG.md
  Git blob:       0585909508f968ed915d0e0e183806ac76d34d28
  SHA-256:        840f15800a5fa4956059c14e5be5ce929b3eaec34a70958ba07905cf3d05ba86
  bytes:          6018
  LF count:       193
  final LF:       yes

verify.py
  Git blob:       92219129a08fa0a5795715ae4ab6e358100dc888
  SHA-256:        682e1ccdbdc61597d9c08d594c9ea8a9c56b9364e419bc0c0e893c908977c2c8
  bytes:          18268
  LF count:       568
  final LF:       yes
```

## Environment

```text
platform:        Debian GNU/Linux 13
architecture:    x86_64
Python:          3.13.5
arithmetic:      Fraction and exact Q(sqrt(5)) pairs only
randomness:      none
environment input: none
network input:   none
third-party code: none
```

The empty stderr SHA-256 is
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
`EXPECTED.txt` is the exact stdout of this single formal execution.

This local run does not satisfy the public two-architecture gate by itself.
That gate requires byte identity to the same `EXPECTED.txt` in the GitHub-hosted
x86_64 and aarch64 pull-request jobs.
