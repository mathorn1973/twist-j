# P-KERNEL-CONNECT-ALL-K-1 result record

Status: two-architecture reproduction complete. The pinned verifier
reproduces its frozen stdout byte for byte on two independent
architectures. The GitHub CI x86_64 re-run confirms on the pull request.

## Pin

```
preregistration + verifier pin commit  17c5f5b5042f053db83d687a67612629cd1bae05
verify.py sha256                        b6fd3cb513987aae9b9c6d5a5c31e26c2c9a34b4610582e8c8072ffaa33cccbc
PREREG.md sha256                        618f9ceee71254698152cc5dbd5598bcfd58de9eb6b0e62a901e9039b669317b
```

## Formal legs

```
leg          architecture   python   result         stdout sha256
-----------  ------------   ------   ------------   ----------------------------------------
local        aarch64        3.12.3   8/8 ALL PASS   15685afb...9709 (2040 bytes, 14 lines, empty stderr, exit 0)
local        x86_64         3.11.15  8/8 ALL PASS   15685afb...9709 (2040 bytes, 14 lines, empty stderr, exit 0)
CI           x86_64         3.12     8/8 ALL PASS   policy workflow run 140 (job 88093122202) on commit ae7a170, VERIFY PASS
```

The verifier stdout is platform neutral (exact integer arithmetic, standard
library only). Both architectures reproduce
`15685afbb9a96ca4ba2cb3787b4ddd74b57cd9d89436350ca7b4ee9542ac9709` byte for
byte from the byte-identical pinned verifier. The recorded formal leg in
`RUN.md` is the aarch64 leg; the x86_64 leg is the second architecture and
is the one the CI re-runs.

## Gate

Two-architecture gate: PASS. No falsifier fired: gate 02 reported
`dim U = 6`, the positive branch of the frozen dichotomy; RESULT 8/8 ALL
PASS on both architectures. The pin was published before any execution and
the decision surface was not weakened after the pin.

The required GitHub `check` job is green on the pull request: policy suite,
canon, ledger, unit tests, and the pinned-verifier reproduction all pass on
x86_64.

## Fold

The row fold (`KERNEL-CONNECT-ALL-K` H -> T) is a separate, later change and
is NOT part of this probe PR. It proceeds under the release procedure in
`POLICY.md` and requires the owner decisions D1, D2, D3.
