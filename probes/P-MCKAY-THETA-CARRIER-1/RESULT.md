# P-MCKAY-THETA-CARRIER-1 result

Status: FORMAL PROBE RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: ALL PASS (9 gates)
exit:    0
stderr:  empty
```

No preregistered falsifier fired. The proof-first conclusion at the declared
scope is that no function of the McKay E8 torus Laplacian realizes the xi
determinant: the forced spectrum needs at least four small-multiplicity
eigenvalues, while every nonzero E8 shell has multiplicity at least 240.

## Two-architecture gate

```text
preregistration pin:  a94cc295116b97da63b61be5c800093681d6727a
formal evidence head: 04f6caff912a60d490533314c8282ecc3e7a2b64
pull request:          60

aarch64 platform:     Ubuntu 24.04.4 LTS
aarch64 Python:       CPython 3.12.3
aarch64 executions:   3, byte-identical
aarch64 exit/stderr:  0 / 0 bytes

x86_64 workflow run:  29642446266
x86_64 workflow job:  88075078144
x86_64 runner:        GitHub-hosted Ubuntu 24.04 x86_64;
                      image ubuntu24/20260714.240, runner 2.335.1
x86_64 Python:        CPython 3.12.13
x86_64 result:        VERIFY PASS

verifier SHA-256:     f79ae9d0ee0f884148cfdc9001b73916d2518c98359993054bdb48c2795aebd2
stdout SHA-256:       6cc651b83ac8132862e90a4a1063614ccc2dfe0a3cd21c9b874912a159ce345d
stdout bytes:         667
stdout lines:         13
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
