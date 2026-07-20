# P-R2-K-JUNCTION-PIN-1 result

Status: FORMAL AARCH64 RESULT; GITHUB X86_64 GATE PENDING; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: ALL PASS (12 gates)
exit:    0
stderr:  empty
```

No preregistered falsifier fired on the first architecture. The exact
rational enclosure is

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
shifts the result by `+log(5)/4` to a disjoint interval.

## Aarch64 evidence

```text
preregistration pin:  4617d988650356e8e3ea9384985d48f2bbc791e2
platform:             Ubuntu 24.04, Linux 6.17.0-1014-nvidia
architecture:         aarch64
Python:               CPython 3.12.3
executions:           3, byte-identical
exit/stderr:          0 / 0 bytes
verifier SHA-256:     e87e019f07f067f463a9e196279e67f4226966172a0ab5fcad6bfe0643bd750d
stdout SHA-256:       dcf9f60a5f965fedb28a15bd9ae0bfd1cb1ec27ab76c8097f4d686dff30d3813
stdout bytes:         1775
stdout lines:         18
```

The independent GitHub-hosted `x86_64` reproduction is still required.
Until it passes, this is not a two-architecture result.

## Scope

The maximum possible registration is `R2-K-JUNCTION-PIN [C]`: a rigorous
finite enclosure of the first completed-zeta rung for `Q(zeta_5)`, with
convention and Q-case guards. It constructs no R2 carrier, proves no higher
Li rung, and makes no RH claim. `R2 [O]` and `RH [O]` remain unchanged.
