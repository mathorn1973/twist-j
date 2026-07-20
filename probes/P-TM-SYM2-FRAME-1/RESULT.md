# P-TM-SYM2-FRAME-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: RESULT POSITIVE 8/8 ALL PASS
exit:    0
stderr:  empty
```

No preregistered falsifier of the frozen golden-frame candidate fired. The
direct exact construction gives

```text
M = (1/3) P1 + (2/15) P5.
```

The scalar to per-channel traceless coefficient ratio is `5:2`. After block
multiplicity is included, the scalar to total traceless trace-mass ratio is
`1:2`. The two ratios are distinct. The six equal-channel ansatz
`M = (1/6) I6` is false at this exact frame scope.

This is an L1 algebraic result for the candidate
`GOLDEN-SIX-LINE-SYM2-FRAME`. It is not a registered Canon theorem. In
particular, `TM-SYM2-MEASURE [H]` remains unchanged.

## Immutable pin and formal evidence

```text
public lock:          issue 92
draft pull request:   93
base commit:          3d8c6307f20d01ad50fc90ae1c5777926b884881
preregistration pin: d36c3304b796596456dbc070b3fa5cd73fe97044
formal evidence head:1754059fa364a27842b45ba267b0f0955b1397cd
tested merge commit: 8eae53b5efd98441372a77c8749a9c45f0b8e310
PREREG.md SHA-256:    9ac19d18e8d1836f16024c27be15e450646b624b693f90920187cc00a44ebe63
verify.py SHA-256:    4b84f8ddf35be025224ba5d3a44159ffecd5e93face5a0536971357928083135

aarch64 platform:    Ubuntu 24.04.4 LTS
aarch64 Python:      CPython 3.12.3
aarch64 checkout:    clean, detached at the exact public pin
aarch64 exit/stderr: 0 / 0 bytes

x86_64 workflow run: 29729754592
x86_64 workflow job: 88311179186
x86_64 platform:     Ubuntu 24.04.4 LTS
x86_64 runner image: ubuntu-24.04 20260714.240.1
x86_64 runner:       2.335.1
x86_64 Python:       CPython 3.12.13
x86_64 exit/stderr:  0 / 0 bytes

stdout SHA-256:      d144486d47039ea3b2a4402647df315fba55d265788e7d1b8d56124e7ea98f43
stdout bytes/lines:  742 / 10
byte identity:       PASS
result:              POSITIVE 8/8 ALL PASS
```

`EXPECTED.txt` is the exact LF-only stdout of the formal aarch64 leg.
`PREREG.md` and `verify.py` remain byte-identical to the public pin. The
GitHub pull-request workflow reran the pinned verifier on x86_64 and reported
the identical verifier and stdout hashes.

## Exact frame result

The six projective lines over `Q(phi)` produce symmetric, idempotent,
trace-one rank-one projectors. Their Frobenius Gram has diagonal `1` and
off-diagonal `1/5`, and their sum is `2 I3`. After subtracting `I3/3`, the
six projectors form a rank-five regular simplex with diagonal Gram value
`2/3` and off-diagonal value `-2/15`.

The complete 36-variable commutant system for the exact rational `so(3)`
action on `Sym2(Q^3)` has rank 34 and nullity two. The canonical trace and
traceless projectors span it. The frame operator is built directly from the
six rank-one projectors, not from the target spectrum. It descends from
`Q(phi)` to `Q`, agrees under `phi -> 1-phi`, and is `so(3)`-central.

The cube-line negative control has second moment `I3/3` but fails the Sym2
centrality test. This proves that second-order isotropy alone is insufficient
and prevents the old hidden inference from entering the result.

## Scope firewall

The six golden lines and their equal cardinal weights are frozen inputs.
Their selection is not derived from `J`, `U`, a checkpoint, the decoder, or
a Thue-Morse orbit. The `1/6` in the direct average counts six frame lines;
it is not `GYRON-DENSITY`, a clock density, or a Born multiplier.

No faithful rational three-dimensional `A5` representation is asserted. No
`A5` commutant dimension, Thue-Morse average, clock-direction independence,
Born phase halving, physical probability, L5 stream, or L6 measure lift is
earned. The identity `1/6 = (1/2)(1/3)` remains arithmetic only.

The public rows `TM-SYM2-MEASURE [H]`,
`QUADRATIC-ENVELOPE-DECODER [H]`, and `QUADRATIC-DECODER-DATA [O]` retain
their present status and scope. Any Canon, registry, dependency, frontier,
or ledger fold is a separate reviewed change.

## Architecture gate

The clean formal aarch64 run and the GitHub x86_64 pull-request workflow
executed the identical pinned verifier, exited zero with empty stderr, and
reproduced the 742-byte, 10-line transcript byte for byte. The exact finite
result therefore passes the two-architecture computation gate.

Policy, unit, Canon, ledger, verifier, and minimal-reproduction workflow
stages passed. This gate does not register the candidate, change a Canon
status, or supply the missing Thue-Morse or physical-measure bridge.
