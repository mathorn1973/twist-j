# P-R2-LAMBDA-HAAR-1 result

Status: FORMAL PROBE RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: ALL PASS (14 gates)
exit:    0
stderr:  empty
```

No preregistered falsifier fired. The proof-first conclusion at the declared
scope is that no unit Koopman operator on `L^2(O_lambda, Haar)` is an S2 Li
witness: for the non-torsion unit J the Hilbert-Schmidt ladder is infinite at
every rung, and the spectrum is pure point on roots of unity.

## Two-architecture gate

```text
preregistration pin:  0b4163f234e839e8898c09b98056927179a86435
formal evidence head: b712e22a1415dd1a217af5b79b7c2aa8527b4596
pull request:          61

aarch64 platform:     Ubuntu 24.04.4 LTS
aarch64 Python:       CPython 3.12.3
aarch64 executions:   3, byte-identical
aarch64 exit/stderr:  0 / 0 bytes

x86_64 workflow run:  29642453132
x86_64 workflow job:  88075097097
x86_64 runner:        GitHub-hosted Ubuntu 24.04 x86_64;
                      image ubuntu24/20260714.240, runner 2.335.1
x86_64 Python:        CPython 3.12.13
x86_64 result:        VERIFY PASS

verifier SHA-256:     ed04f70b07f39b84a1611b123e8588cc3074110966b079c7806a7e19b0e09154
stdout SHA-256:       4f1f5b82c4b812afb9d2346b25f5aa54ec7e106f43579c041221269e728f1e68
stdout bytes:         1615
stdout lines:         23
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
