# P-BELL-MAGIC-BOUNDARY-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS

## Scientific decision

```text
DECISION POSITIVE
```

On the complete preregistered finite carriers, exact enumeration gives

```text
M_5 = 1/2 + sqrt(5),
M_8 = 2 sqrt(2),
2 < M_5 < M_8.
```

Both closed-form predictions therefore match. The full and global-phase
quotient enumerations agree exactly:

```text
n = 5: 625 full tuples, 125 quotient tuples,
        10 full maximizers, 2 quotient maximizers
n = 8: 4096 full tuples, 512 quotient tuples,
        32 full maximizers, 4 quotient maximizers
```

All three verifier audit checks pass. No invalidity threshold or scientific
falsifier fired.

## Scope

This result concerns only the declared finite functional
`S_n = abs(C_n)` on the phase carriers `Z/5Z` and `Z/8Z`. The threshold `2`
is used only in the preregistered exact comparison. The result is not an
unrestricted Bell cap, a local-hidden-variable theorem, a continuous quantum
optimum, or a Tsirelson claim. The legacy modulus bound involving `phi` is a
different observable and remains outside this probe.

## Formal evidence

```text
preregistration pin: 1e141603b7977902a88e80d5fe6ff2d72364f82e
verifier SHA-256:    6fcfe90a0e920b85ade1e6ff93f799137fec41c1bb6fb1d3fea119da1c0c7268
formal run commit:   f753bb0cd4acef4a7ce02094c62b9d4fe47de5a4

aarch64 platform:    Ubuntu 24.04
aarch64 Python:      3.12.3
aarch64 exit code:   0
aarch64 stderr:      0 bytes

x86_64 workflow run: 29281622849
x86_64 workflow job: 86923949971
x86_64 platform:     Ubuntu 24.04.4
x86_64 Python:       3.12.13
x86_64 exit code:    0
x86_64 stderr:       0 bytes

stdout SHA-256:      7f6d21994ae02a07a6399853f5bef6748f0b16569304e58095d1589ccc01a3da
stdout bytes:        852
stdout lines:        14
```

`EXPECTED.txt` is the exact formal stdout. `RUN.md` contains the neutral
local run record. Audit success and the positive scientific decision are
separate: exit zero certifies exact execution and integrity, while
`DECISION POSITIVE` records the preregistered scientific branch.

The public repository pull-request workflow independently reran the pinned
verifier on GitHub `x86_64` with Python 3.12.13 and reproduced
`EXPECTED.txt` byte for byte. Its verifier and reproduction stages passed;
the run's later failure was an unrelated post-cutover activation-routing
false negative. That routing defect was corrected separately by policy PR
`#14`, merged as `eabf309d8f73ff452e116d163487fa62f4191620`, without relaxing
immutable tag or release readback. The formal `aarch64` record and public
`x86_64` reproduction therefore satisfy the two-architecture computation
gate for this finite result.
