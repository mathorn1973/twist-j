# P-R2-SCALING-SHIFT-1 result

Status: FORMAL PROBE RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: ALL PASS (13 gates)
exit:    0
stderr:  empty
```

No preregistered falsifier fired. The proof-first conclusion at the declared
scope is that multiplication by lambda on `L^2(K_lambda)` is a bilateral shift
of homogeneous Lebesgue type: S2 and cocycle forms both fail, and the
boundary-ladder increments increase strictly toward phi^2 without attaining
it, missing the second Li rung.

## Two-architecture gate

```text
preregistration pin:  3c5d2e6e778aab8e2c3d29f09df4e2c7532de12a
formal evidence head: 788582577ed888b93974c30ee49fa91a35c42de4
pull request:          62

aarch64 platform:     Ubuntu 24.04.4 LTS
aarch64 Python:       CPython 3.12.3
aarch64 executions:   3, byte-identical
aarch64 exit/stderr:  0 / 0 bytes

x86_64 workflow run:  29642463172
x86_64 workflow job:  88075125797
x86_64 runner:        GitHub-hosted Ubuntu 24.04 x86_64;
                      image ubuntu24/20260714.240, runner 2.335.1
x86_64 Python:        CPython 3.12.13
x86_64 result:        VERIFY PASS

verifier SHA-256:     e8519402773cc0d94425eb9d4afa6d7f260c3c770c5d142bfbb5c13e44ff3894
stdout SHA-256:       4f50c87d24d0705d843dfe431d43fa472ba46ecf7f28ad7471711f62a113180f
stdout bytes:         1832
stdout lines:         22
byte identity:        PASS; GitHub x86_64 reproduced EXPECTED.txt byte for byte
gate:                 PASS
```

The GitHub policy workflow succeeded on the exact formal-evidence head and
enforced verifier integrity, exit zero, empty stderr, and byte-identical
`EXPECTED.txt`. `RUN.md` remains the neutral aarch64 record. This close-gate
update changes only `RESULT.md`.

`verify.py` audits finite witnesses; the theorem rests on the proof frozen in
`PREREG.md`. This probe changes no normative Canon file. Registration is a
separate sealed fold, and RH remains O.
