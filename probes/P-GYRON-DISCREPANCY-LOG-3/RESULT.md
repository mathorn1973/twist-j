# P-GYRON-DISCREPANCY-LOG-3 result

Status: EXTERNAL GATE C PASS; PUBLIC CLAIM UNCHANGED

## Recorded decision

```text
exit:                   0
stderr:                 empty
counterexample:         NONE
diagnostic:             NONE
gate A proof:           PROOF-SURVIVES
gate B proof:           PROOF-SURVIVES
gate C local audit:     AUDIT-PASS
theorem A decision:     PROOF-SURVIVES
theorem B decision:     PROOF-SURVIVES
run integrity:          PASS
scientific decision:    PROOF-SURVIVES
route:                  PROOF-SURVIVES
native aarch64 leg:     PASS
x86_64 replay:          PASS
cross-architecture:     PASS
external Gate C:        PASS
```

This is the exact outcome of the sole authorized native Linux/aarch64
execution and the first public GitHub Linux/x86_64 replay. It is not a Canon
promotion, registry edit, or public theorem-status change.

## Reported proof and audit nodes

```text
I01 RUNTIME:                     PASS
I02 EXACTNESS:                   PASS
A01 SEAMS:                       PASS
A02 BALANCE:                     PASS
A03 DISCREPANCY:                 PASS
A04 TRANSDUCER:                  PASS
A05 FOUR-BIT:                    PASS
A06 BASE-TABLE:                  PASS
A07 INDUCTION:                   PASS
A08 EXTREMA:                     PASS
A09 COROLLARIES:                 PASS
B01 PHASE-MAPS:                  PASS
B02 ANCHOR-SPECTRA:              PASS
B03 STATIONARY:                  PASS
B04 FIXED-POINT:                 PASS
B05 CONVERGENCE+PHASE-LAWS:      PASS
C01 DIRECT-PREFIX:               PASS
C02 ROUTE-AGREEMENT:             PASS
C03 NEGATIVE-CONTROLS:           PASS
```

The direct prefix audit used the frozen horizon `H=256` and exact records
through prefix 1024. Route agreement covered 1921 discrepancy comparisons,
15 phase comparisons, and all 96 four-bit affine paths. All six negative
controls passed.

## Theorem A certificate

The symbolic route established the four substitution seam identities, the
balance laws, the `c_10` census identity, and the exact discrepancy laws

```text
d(2L)=-d(L)+3S(L)-6
d(4L)=d(L)-3S(L)
```

for the frozen domain. It retained `L=1`, `d(1)=-1`, `d(4)=-4` as the least
positive counterexample to the unqualified four-step invariant and proved
that `d(4L)=d(L)` holds exactly for even `L`.

The route established exact closure and reachability of the six-state
signed-affine transducer, all 96 four-bit paths, all 24 frozen base
intervals, and the translation-equivariant four-step induction. The
resulting all-`k` extremum certificate is

```text
E_1=2
E_2=4
E_k=2(floor((k+1)/4)+2), k>=3.
```

It also established the separately handled endpoint two-cycle and the
in-scope corollaries

```text
d(L)=O(log L)
d(L)/L^epsilon -> 0 for every fixed epsilon>0
c_00(L)/L -> 1/6
c_00(L)/(L-1) -> 1/6.
```

The finite prefix census is an independent audit only; it is not used as the
proof of any universal clause.

## Theorem B certificate

The exact rational route derived `I_L`, `I_R`, `B`, `R_L`, and `R_R`, and
retained the required full-space anchoring systematic:

```text
chi_(R_L)(x)=x(x-1)(x-1/2)(x+1/2)
chi_(R_R)(x)=x(x-1)(x+1/2)^2.
```

The full maps and their spectra are unequal. Their restrictions to the
stationary space `b=c` agree and have spectrum `{1,-1/2,0}`. The route
established

```text
v_*=(1,2,2,1)/6
R v_*=v_*
```

and proved, through a complete exact eigenbasis, that `v_*` is the unique
fixed point in the normalized stationary affine space and that
`R^n v -> v_*` componentwise for every input in that space.

The frozen phase laws also passed:

```text
I(v_*)=(0,1/2,1/2,0)
B(v_*)=(1/3,1/6,1/6,1/3)
v_*=(I(v_*)+B(v_*))/2.
```

Thus the `00` coordinate is `0` in the internal phase, `1/3` in the boundary
phase, and `1/6` only under the frozen equal phase average.

## Integrity controls

The implementation rejected all six forbidden substitutions:

1. a global four-step invariant;
2. equality of the full left and right anchoring maps;
3. equality of their full spectra;
4. density `1/6` in either fixed phase;
5. invertibility of the stationary operator;
6. use of the finite audit as a universal proof.

Proof nodes and finite-audit nodes have disjoint provenance. The independent
prefix and matrix routes agreed with the proof route. No exact falsifier,
proof gap, structural gap, route disagreement, malformed witness, or STOP
diagnostic was emitted.

## Immutable pin and native evidence

```text
public lock:           issue 171
parent commit:         1a4ae20d05cd76f93f70b2b011979b22a15fcde7
pin commit:            ee06791f7a0a31b28ca1958c62e2abd01a55b456
PREREG.md SHA-256:     b45c42ad7f169d7c6cd01f1d6e785a5baf6ac46960dfa456d2447cc68c9b59b0
verify.py SHA-256:     10ebef3ffd10067dce0b47b95e58f6ffb8437a2d252eba0510afc39e98bee3ae
EXPECTED.txt SHA-256:  ce10ac43276890c4978b189d830b6c989ae31b4e74cb42380a09f845e4a802b4

aarch64 platform:     Ubuntu 24.04.4 LTS
aarch64 Python:       Python 3.12.3
aarch64 checkout:     clean and detached at the exact public pin
aarch64 executions:   1
aarch64 exit/stderr:  0 / 0 bytes
stdout bytes/lines:   1735 / 34
stdout CR/NUL/final:  0 / 0 / 0a

x86_64 workflow run:  30221889556
x86_64 job:           89845627151
tested merge commit:  9ac6ef90a2d12ff233513d372ede8491f7315f57
tested PR head:       fb1c86e6e5b43de8692b0ff9cb0d6fae8708b8c8
x86_64 platform:      Ubuntu 24.04.4 LTS
runner image:         ubuntu-24.04 20260720.247.2
runner version:       2.336.0
x86_64 Python:        CPython 3.12.13
x86_64 exit/stderr:   0 / 0 bytes
x86_64 stdout SHA:    ce10ac43276890c4978b189d830b6c989ae31b4e74cb42380a09f845e4a802b4
byte identity:        PASS
external Gate C:      PASS
public claim status:  UNCHANGED
```

The complete neutral metadata and exact raw stdout were returned publicly on
issue #171 in comment `5085509668` before `EXPECTED.txt`, `RUN.md`, and this
file were created. `EXPECTED.txt` is byte-identical to that raw stdout. The
first public x86_64 replay return was recorded in issue #171 comment
`5085569836`.

## Scope firewall

This is an L1 exact substitution result. The operator `R` is a normalized
forward phase-averaged substitution operator on stationary sliding-pair
frequencies. It is not coarse-graining, desubstitution, inverse RG, a
finite-prefix invariant, a decoder factor, a physical probability, a
physical measure, or an L1-to-L5/L6 bridge.

The result supplies no decoder existence, totality, uniqueness, canonicity,
completeness, terminality, source map, event map, Born rule, geometry, time,
mass, or cosmological claim. The decoder predefinition remains context and
firewall only.

No Canon, registry, frontier, evidence, dependency, gate, status, workflow,
release, or authority file is changed by this result commit. Any later row
or Canon wording change requires a separate owner-reviewed fold after the
cross-architecture gate is complete.

## Architecture gate

The sole native aarch64 leg passed. The first public GitHub Linux/x86_64
pull-request replay also passed in workflow `30221889556`, job `89845627151`,
on merge commit `9ac6ef90a2d12ff233513d372ede8491f7315f57`.
The successful policy checker used the byte-identical pinned verifier,
enforced exit code 0 and empty stderr, and reproduced `EXPECTED.txt`
byte for byte with SHA-256
`ce10ac43276890c4978b189d830b6c989ae31b4e74cb42380a09f845e4a802b4`.

`C-PIN`, `C-REMOTE`, `C-AARCH64`, `C-PUBLIC-RETURN`, `C-X86_64`, and
`C-BYTES` are all `PASS`. The cross-architecture computation gate and
external Gate C therefore pass, with no rerun of the sole native aarch64
leg and no minimal reproduction required. This record still claims no
public Canon status; that requires a separate owner-reviewed fold.
