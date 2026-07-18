# P-KERNEL-CONNECT-ALL-K-1 result record

Status: INTERIM. This probe is pinned and has passed one formal
architecture leg. The two-architecture gate is not yet complete and the
row fold has not been performed. This record is finalized before merge.

## Pin

```
preregistration + verifier pin commit  17c5f5b5042f053db83d687a67612629cd1bae05
verify.py sha256                        b6fd3cb513987aae9b9c6d5a5c31e26c2c9a34b4610582e8c8072ffaa33cccbc
PREREG.md sha256                        618f9ceee71254698152cc5dbd5598bcfd58de9eb6b0e62a901e9039b669317b
```

## Formal legs

```
leg          architecture   result           stdout sha256
-----------  -------------  ---------------  ----------------------------------------
local        x86_64         8/8 ALL PASS     15685afb...9709 (2040 bytes, 14 lines)
CI x86_64    x86_64         pending          (policy workflow re-runs the pinned verifier)
aarch64      aarch64        pending          (formal leg via MCP machine; output is platform neutral)
```

The verifier stdout is platform neutral (exact integer arithmetic, standard
library only), so every conforming leg must reproduce
`15685afbb9a96ca4ba2cb3787b4ddd74b57cd9d89436350ca7b4ee9542ac9709` byte for
byte. The x86_64 local leg already does.

## Gate

Two-architecture gate: NOT YET PASSED (aarch64 leg pending). No falsifier
fired: gate 02 reported `dim U = 6`, the positive branch of the frozen
dichotomy; RESULT 8/8 ALL PASS.

## Fold

The row fold (`KERNEL-CONNECT-ALL-K` H -> T) is a separate, later change and
is NOT part of this probe PR. It requires the owner decisions D1, D2, D3 and
proceeds under the release procedure in `POLICY.md`.
