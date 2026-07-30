# P-R2-K-JUNCTION-PIN-1 result

Status: FORMAL PROBE RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: ALL PASS (12 gates)
exit:    0
stderr:  empty
```

No preregistered falsifier fired. The exact rational enclosure is

```text
lambda_1^K in
[0.304595618542798635262524662701,
 0.304595618542798635262524662702].
```

The complete nonprincipal logarithmic-derivative sum is enclosed by

```text
[1.143408547611871901089216,
 1.143408547611871901089217].
```

The inherited Q guard reproduced as

```text
lambda_1^Q in
[0.023095708966121033814310,
 0.023095708966121033814311],
```

strictly inside its public bracket. The literal modulus-five
principal-character convention fired its intended negative control: it
shifts the result by `+log(5)/4` to the disjoint interval

```text
[0.706955096651323728912714,
 0.706955096651323728912715].
```

## Two-architecture gate

```text
preregistration pin:  4617d988650356e8e3ea9384985d48f2bbc791e2
formal evidence head: b468fe029f0c2d22956587e90fd5f0b6680ed30e
pull request:          97

aarch64 platform:     Ubuntu 24.04, Linux 6.17.0-1014-nvidia
aarch64 Python:       CPython 3.12.3
aarch64 executions:   3, byte-identical
aarch64 exit/stderr:  0 / 0 bytes

x86_64 workflow run:  29733171782
x86_64 workflow job:  88322208737
x86_64 tested merge:  07fb01633f12b9a0b937b790a3cf26f927c53080
x86_64 runner:        GitHub-hosted Ubuntu 24.04.4 x86_64;
                      image ubuntu24/20260714.240, runner 2.335.1
x86_64 Python:        CPython 3.12.13
x86_64 result:        VERIFY PASS

verifier SHA-256:     e87e019f07f067f463a9e196279e67f4226966172a0ab5fcad6bfe0643bd750d
stdout SHA-256:       dcf9f60a5f965fedb28a15bd9ae0bfd1cb1ec27ab76c8097f4d686dff30d3813
stdout bytes:         1775
stdout lines:         18
byte identity:        PASS; GitHub x86_64 reproduced EXPECTED.txt byte for byte
gate:                 PASS
```

The policy workflow also passed repository policy, 44 tool tests, Public
Canon v11 validation, and the ledger check. `RUN.md` remains the neutral
aarch64 record. This close-gate update changes only `RESULT.md`.

## Scientific status and scope

At the declared finite-enclosure scope, the result is
`R2-K-JUNCTION-PIN [C]`. It is a rigorous computed enclosure of the first
completed-zeta rung for `Q(zeta_5)`, with an independent generalized
Stieltjes enclosure, explicit complex character assembly, the Q guard, and
the principal-character convention control.

It constructs no R2 carrier, proves no higher Li rung, and makes no RH
claim. `R2 [O]` and `RH [O]` remain unchanged. No normative Canon file was
changed. Canon registration, review, and merge are separate actions.
