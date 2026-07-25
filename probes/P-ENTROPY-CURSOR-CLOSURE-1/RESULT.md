# P-ENTROPY-CURSOR-CLOSURE-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
PUBLIC CANON UNCHANGED

The immutable preregistration pin
`916eed58a37f0a4ce56ff093fc0dcb7e1d42d5ff` was executed once on native
aarch64 after remote readback. The verifier exited zero, wrote no stderr, and
produced the exact 1,474-byte output recorded in `EXPECTED.txt` with SHA-256
`21ca2301ffa17634eb868c154e7b683c0d2ca0bc54661962029b12a7a0e65ca7`.

The first clean GitHub Linux x86_64 replay used the identical pinned verifier
at tested merge commit
`28b5166efc121073da461ce843a2a0cc7866f6be`. Workflow run `30165843010`,
job `89698596833`, exited zero with empty stderr and reproduced
`EXPECTED.txt` byte for byte. The two-architecture computation gate is PASS.

## Recorded decision

```text
window/cursor pairs: 522
depth-grid triples:  27
candidate triples:   549
nonzero:             0
zero-residue lift:   PASS
result:              PASS / cursor axis closed through window 32
```

## Exact certificate

At the preregistered finite surface, all 522 distinct window/cursor pairs for
driver windows `L = 4..32` and all 27 distinct depth-grid triples were zero.
The E05 structural certificate proves that the labelled zero-residue
restriction projects to the same pure-word obstruction, transporting this
finite-cylindrical no-go to every lambda-depth. Independent literal-affine,
Thue-Morse construction, and tree-residual routes agree on their common
surfaces; all preregistered controls and source checks pass.

## Immutable pin and formal evidence

```text
public lock:           issue 151
base commit:           a11ea993f2c120b6f5c8c896c1ce11a9d0740d44
pin commit:            916eed58a37f0a4ce56ff093fc0dcb7e1d42d5ff
PREREG.md SHA-256:     d57fc9e12527aa98db4c270952add818a1f2e3b083c13155b5861d5c24b35f14
verify.py SHA-256:     6a41a8846a19b3e0e75cbf25a87c8825a13f369238732549a004a17687092e76

aarch64 platform:     Ubuntu 24.04.4 LTS
aarch64 Python:       Python 3.12.3
aarch64 checkout:     clean, detached at the exact public pin
aarch64 executions:   1
aarch64 exit/stderr:  0 / 0 bytes
x86_64 workflow run:  30165843010
x86_64 workflow job:  89698596833
x86_64 tested merge:  28b5166efc121073da461ce843a2a0cc7866f6be
x86_64 platform:      Ubuntu 24.04.4 LTS
x86_64 runner image:  ubuntu-24.04 20260720.247.2
x86_64 runner:        2.336.0
x86_64 Python:        CPython 3.12.13
x86_64 exit/stderr:   0 / 0 bytes
x86_64 byte identity: PASS
stdout SHA-256:       21ca2301ffa17634eb868c154e7b683c0d2ca0bc54661962029b12a7a0e65ca7
stdout bytes/lines:   1474 / 19
stdout CR/final byte: 0 / 0a

architecture gate:    PASS
```

## Scope firewall

This result earns candidate-T evidence only for the typed `F_5^6`
finite-cylindrical L5 ansatz. It makes no measurable-selection, entropy,
probability, or measure-lift claim and does not close
`ENTROPY-LAYER-BRIDGE [O]`. It changes no Canon, registry, frontier,
dependency, status, release, or authority file.

Public lock: https://github.com/mathorn1973/twist-j/issues/151

## Architecture gate

The sole formal aarch64 leg passed. The first clean GitHub Linux x86_64
replay of the identical pinned verifier also passed: exit zero, empty stderr,
and byte-for-byte reproduction of `EXPECTED.txt`. The two-architecture
computation gate is therefore PASS. The final-head policy workflow remains
the merge-eligibility check for this evidence update.
