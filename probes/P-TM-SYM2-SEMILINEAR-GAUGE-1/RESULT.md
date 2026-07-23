# P-TM-SYM2-SEMILINEAR-GAUGE-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
PUBLIC CLAIM UNCHANGED

## Recorded decision

```text
route:                 SEMILINEAR-DOUBLE
exit:                  0
stderr:                empty
Gamma_sl order:        24
exponent-one count:    12
coset character:       (1,1)
residual invariant:    chi_Q chi_F
selector orbit count:  2
selector orbit sizes:  24, 24
result:                PASS
```

This is a valid positive classification of the preregistered candidate
semilinear equivalence. It is not a technical fallback and it is not a
normative gauge adoption.

## Exact classification certificate

The verifier reconstructed the full 48-element centralizer `W`, the two
characters `chi_Q` and `chi_F`, and their 12-element common kernel `G`.
The exponent-zero realization image agrees exactly with `G`.

The complete scan of both exponents and all 48 centralizer permutations
decided all 96 exact incidence systems. It found exactly 12 exponent-one
realizations. They form one left and right coset of `G`, so

```text
Gamma_sl = G disjoint-union hG
|G| = 12
|hG| = 12
|Gamma_sl| = 24
```

Every exponent-one element has additive character

```text
c = (q(h),f(h)) = (1,1).
```

Thus the semilinear coset toggles both old orientation characters. The
product `chi_Q chi_F` is unchanged and is the exact residual invariant.
Postcomposition on the 48-element selector torsor is free and gives exactly
two orbits, each of size 24.

The full accepted witnesses are recorded in `EXPECTED.txt`. The complete
96-case certificate table has SHA-256
`ce9252a773ac3f05425d62afa81d2ea6016b29461adf8e29f2eede52f53d6289`.

## Scientific meaning

The attack succeeds in enlarging the candidate effective equivalence from
the old 12-element projective-linear image to a 24-element semilinear image.
It therefore proves that Galois conjugation pairs the four old
`(chi_Q,chi_F)` fibers:

```text
(0,0) <-> (1,1)
(1,0) <-> (0,1)
```

It does not make the selector canonical. The 48 selectors still split into
two inequivalent blocks, now distinguished exactly by `chi_Q chi_F`.
Consequently the successor attack removes one binary ambiguity but leaves a
genuine final twofold ambiguity.

## Immutable pin and formal evidence

```text
public lock:           issue 134
definition issue:      issue 132
definition PR:         PR 133
parent commit:         87c1a0a42a23ad68612cabcddd1c91fd784c9150
pin commit:            3d3521fe1ed557cc0b2c271baea9a67787aa7951
PREREG.md SHA-256:     034a2da5c56036700cea2e166f7b4c7306da2f12ddee863ab2cdce1c4de38d5a
verify.py SHA-256:     f526af796e0fd2951d5b136b17f786045a932214744040dfd0b86e47c50b3590

aarch64 platform:     Ubuntu 24.04
aarch64 Python:       Python 3.12.3
aarch64 checkout:     clean, detached at the exact public pin
aarch64 executions:   1
aarch64 exit/stderr:  0 / 0 bytes
x86_64 workflow run:  30015742345
x86_64 workflow job:  89235142494
x86_64 tested merge:  4c1b0d4278b0b6357a6b3d39b23a311c92429952
x86_64 platform:      Ubuntu 24.04.4 LTS
x86_64 runner image:  ubuntu-24.04 20260714.240.1
x86_64 runner:        2.336.0
x86_64 Python:        CPython 3.12.13
x86_64 exit/stderr:   0 / 0 bytes
x86_64 byte identity: PASS

stdout SHA-256:       47e04141e0ee0b290a4ca91b1b0b977ad2674d555ab296aaa371177f662bfd19
stdout bytes/lines:   29205 / 146
stdout CR/final byte: 0 / 0a
result:               PASS / SEMILINEAR-DOUBLE

architecture gate:    PASS
```

The complete neutral metadata and exact raw stdout are public in issue #134
comment `5059483579`. `EXPECTED.txt` is byte-identical to that raw stdout.
The pinned five files remain unchanged.

## Scope firewall

This result classifies a candidate enlarged L5 equivalence only. It does not
retroactively replace the frozen `S_TM` projective-linear gauge, change the
old N2 result, or normatively adopt `Gamma_sl`. Such adoption would require a
separate owner decision and Canon fold.

The result supplies no L5-to-L6 bridge, no physical probability theorem, and
no unique microscopic selector. `TM-SYM2-MEASURE` remains `[H]`. Issues
#107--#109 and active C20 issue #126 are unchanged.

No Canon, registry, frontier, dependency, gate, status, release, or authority
file is changed by this evidence-only record.

## Architecture gate

The sole formal aarch64 leg passed. The first clean GitHub Linux x86_64
replay of the identical pinned verifier also passed at tested merge commit
`4c1b0d4278b0b6357a6b3d39b23a311c92429952`: exit zero, empty stderr, and
byte-for-byte reproduction of `EXPECTED.txt`. The two-architecture
computation gate is therefore PASS. The final-head policy workflow remains
the merge-eligibility check for this evidence update.
