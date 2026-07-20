# P-SQRT-PHI-DIGIT-1 result

Status: SCIENTIFIC RESULT; FORMAL AARCH64 LEG PASS;
SECOND-ARCHITECTURE COMPUTATION GATE PENDING; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: RESULT 6/6 ALL PASS
exit:    0
stderr:  empty
```

No preregistered falsifier fired in the formal aarch64 leg. The frozen proof
establishes the exact two-branch `C8 -> C4 -> C2` digit lift and the
nonconstant chronological carry law at L1. The finite verifier exhausts the
field and restricted norm sequence and audits both digit branches through
the frozen prefix. This records a proof-first scientific result, not a
registered Canon theorem. The proposed `SQRT-PHI-DIGIT-LIFT` claim is not yet
registered, and `SQRT-PHI-TIME-GRAVITY` remains `[O]`.

## Immutable pin and formal leg

```text
public lock:          issue 87
base commit:          3d8c6307f20d01ad50fc90ae1c5777926b884881
preregistration pin: 25821b83bf9763b07802526a3a3e3036a7a4cbb0
PREREG.md SHA-256:    b8f3e7769490da70b686f5de21769ccb29b79fca4304256dd477aff198eaeada
verify.py SHA-256:    ad94fdff5cf0b7c8674d36b675f058f347287702c90428c19aa6b76e8e4a1cab

platform:             Ubuntu 24.04.4 LTS
architecture:         aarch64
Python:               CPython 3.12.3
checkout:             clean, detached at the exact public pin
exit/stderr:          0 / 0 bytes
stdout SHA-256:       9a82917b6736026c3b4e0af9d401400be78be920582f6f8acdbffd87c2e4ddde
stdout bytes/lines:   606 / 7
result:               6/6 ALL PASS
```

`EXPECTED.txt` is the exact LF-only stdout of this formal leg. `PREREG.md`
and `verify.py` remain byte-identical to the public pin.

## Proof and audit verdict

In `F_25=F_5[tau]/(tau^2-2)`, the element `eta=tau^3` has square
`phi=3`, fourth power `-1`, exact order eight, and norm `J=2`. The roots of
`r^2=phi` are exactly `eta` and `-eta`. On `<eta>`, the norm has kernel
`{+-1}`, image `<J>`, and no section because both preimages of the generator
`J` have order eight. This proves the restricted exact sequence is
nonsplit.

For either root `r_epsilon`, binary-length induction gives the unique digit
solution `Y_n^epsilon=r_epsilon^s2(n)`. Norm, square, fourth power, and sign
quotient then give the exact `C8 -> C4 -> C2` tower and the relation between
the two branches. Clearing the trailing one-bits of `n` gives the successor
multiplier `r_epsilon^(1-nu2(n+1))`. It equals `r_epsilon` at `n=0` and `1`
at `n=1`, so it is not constant.

The audit exhausts all 25 field elements, every restricted `C8` product,
both digit branches for `0<=n<=2^18`, all projection identities on that
prefix, and every carry length from zero through eighteen. All six gates
pass. The frozen proof, not the finite prefix, carries the all-`n` result.

## Scope firewall

The earned statement is confined to L1 arithmetic and the inherited
`RAMIFIED-TM-LIFT`. It does not assert that the chronological successor is
multiplication by `sqrt(phi)`, that digit insertion is a physical tick, or
that either sign branch is uniquely or physically selected. It does not
identify `Y_n` with a checkpoint, decoder output, or full `U` state.

No physical time, time arrow, gravity dynamics, coupling, SI scale, force,
parity on all of `Z_2`, or lift to L2-L6 is earned. The live
`SQRT-PHI-TIME-GRAVITY [O]` obligation still requires a typed bridge into the
declared chronological clock and gravity channel. All existing Canon rows
retain their current scopes and statuses.

## Pending gate

The clean GitHub x86_64 policy run must reproduce the pinned verifier and the
606-byte transcript byte for byte. Until that succeeds, the required
two-architecture computation gate is incomplete. Any Canon, registry,
dependency, frontier, or ledger fold is a separate reviewed change.
