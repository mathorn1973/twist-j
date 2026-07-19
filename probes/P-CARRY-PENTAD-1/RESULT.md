# P-CARRY-PENTAD-1 result

Status: FORMAL AARCH64 LEG PASS; TWO-ARCHITECTURE GATE PENDING; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: RESULT 18/18 ALL PASS
exit:    0
stderr:  empty
```

No preregistered falsifier fired on the formal `aarch64` leg. The exact
finite audit agrees with the frozen proof of C1-C7 at the scopes stated in
`PREREG.md`. This records a surviving theorem candidate, not a Canon theorem:
the required independent GitHub `x86_64` reproduction is still pending, and
registration or promotion would require a separate sealed fold.

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
`verify.py` remain byte-identical to the public pin. The pull-request policy
check must rerun that verifier on GitHub `x86_64` and reproduce
`EXPECTED.txt` byte for byte before the two-architecture computation gate is
complete.

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
