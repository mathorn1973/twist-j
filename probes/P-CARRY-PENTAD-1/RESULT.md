# P-CARRY-PENTAD-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: RESULT 18/18 ALL PASS
exit:    0
stderr:  empty
```

No preregistered falsifier fired on either architecture. The exact finite
audit agrees with the frozen proof of C1-C7 at the scopes stated in
`PREREG.md`. This records a reproduced scientific result, not a registered
Canon theorem. Registration or promotion would require a separate sealed
fold.

## Immutable pin and formal leg

```text
public lock:          issue 77
base commit:          633b6f220fddd5882b73b156ca12161fc6d97938
preregistration pin: c2621396f745b44060e37d77ab6efde869b075dd
pin tree:             dd79e4520fc824f933999c30b5634235b3d7ee97
PREREG.md SHA-256:    b3ad51848c09b4fa012599faef18b951a285707971496afe22202e012b4c2b2f
verify.py SHA-256:    55484d3063885966463e755fd92c3b5d735443f776824972f35371bdedcbed0f

platform:             Linux
architecture:         aarch64
Python:               CPython 3.12.3
checkout:             clean, detached at the exact public pin
exit/stderr:          0 / 0 bytes
stdout SHA-256:       a44a9bc26fcbfc91f61d77d2b2c5dc49133af889036d5a0b5c62302172492a56
stdout bytes/lines:   1621 / 19
result:               18/18 ALL PASS
```

`EXPECTED.txt` is the exact stdout of this formal leg. `PREREG.md` and
`verify.py` remain byte-identical to the public pin.

## Independent x86_64 reproduction

```text
pull request:          78
formal evidence head: 95f29296fc381f6b8a9112ce2a7192e33b2a5132
workflow run:          29700061628
workflow job:          88227505751
conclusion:            success
platform:              GitHub-hosted Ubuntu 24.04.4 LTS x86_64
runner image:          ubuntu24/20260714.240, runner 2.335.1
Python:                CPython 3.12.13
verifier SHA-256:      55484d3063885966463e755fd92c3b5d735443f776824972f35371bdedcbed0f
stdout SHA-256:        a44a9bc26fcbfc91f61d77d2b2c5dc49133af889036d5a0b5c62302172492a56
byte identity:         PASS, 1621 bytes and 19 lines
gate:                  PASS
```

The required policy workflow reran the pinned verifier on the exact formal
evidence head. It enforced verifier integrity, exit zero, empty stderr, and
byte-identical `EXPECTED.txt`, and logged `VERIFY PASS P-CARRY-PENTAD-1` with
the two frozen hashes. Together with the formal `aarch64` record, this
completes the two-architecture computation gate. `RUN.md` remains the neutral
`aarch64` record; this close-gate update changes only `RESULT.md`.

## Earned scope and fences

At the recorded leg, the audit found the declared four-bit carry geometry,
the `S5` stabilizer inside `Sp(4,2) ~= S6`, absence of order five in the raw
`d` stabilizer, the fixed-five minimum-width result, the integral cyclotomic
conjugacies and `J` bridge, the power-blind ramified quotient, and the typed
mod-two `A4` bridge with sign kernel exactly `{+-I}`.

The result does not select `p=5` or width four unconditionally, select a
cycle orientation or exponent, derive the step form, identify an integral
conjugacy with a physical gauge, or add any L2-L6, decoder, aperiodicity,
entropy, measure, spacetime, force, or phase claim. It changes no Canon,
registry, frontier, dependency, or status row.
