# P-CURVATURE-TRACE-VALUE-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS

## Scientific decision

```text
kappa = Tr_V(K^2) = -881/8
registered proposal = -21/8
DECISION NEGATIVE
RESULT VALID
```

The registered proposal is false for the exact owner-selected historical
operator frozen by the public ruling and preregistration. Both independent
algorithms in the pinned verifier give `-881/8` exactly:

```text
Route A: complete H-orbit incidence trace
Route B: complete 20 x 20 x 4 Reynolds group-word fixed-point trace
```

The routes agree before comparison with `-21/8`. All thirteen integrity
gates pass, including the full carrier and generator checks, exact orbit
census, rank, restriction-failure witness, projector and compression typing,
skewness, completeness of both routes, historical checksum separation, exact
arithmetic, and deterministic audit-before-decision routing.

The preregistered falsifier therefore fired. This is a valid first-class
negative outcome, not an invalid run and not a reason to alter the operator,
normalization, carrier, or threshold.

## Scope

This result concerns exactly

```text
X = F_5^6,
H = <b,d>,
V = F^H intersect 1_X^perp,
C0 = T_a T_c - T_c T_a,
K = (P0 R_H C0 R_H P0)|_V,
kappa = the ordinary unnormalized Tr_V(K^2).
```

It refutes `-21/8` only at this frozen historical-reconstruction surface. It
does not select a canonical curvature operator, prove a spectrum for `K`,
identify a distinguished boundary or golden block, define a physical decoder,
or infer continuum curvature. The separately named
`P-CURVATURE-OPERATOR-CANONICAL-1` obligation remains open.

The historical ten-mode package has the exact trace-square checksum `-22`,
derived separately from its printed polynomial. That checksum equals neither
the registered proposal nor the computed trace and is not asserted as the
spectrum of `K`. Its role here is a historical-only integrity audit, exactly
as frozen in the ruling.

## Formal evidence

```text
ruling merge:          f9aac76ac9b1355fe45b9d675de7a8ec40cc9588
ruling file SHA-256:   cf15037f5cc2690a9633ca68ef13107920ce9ce81116963dc9d8490c088eeccb
preregistration pin:   617b0ebe87b8581203abff7943c89dce28e824ae
PREREG.md SHA-256:     94ec5263d2b2931bcd3863cb5f78e2326944479aa28aef987495c8601c65f8c9
verify.py SHA-256:     c9b4d253a609cc489efc4386e5e61d3e92baa16b736b899048f2a3afa5e78c99
formal run commit:     a983560509a3ea233b26da9c32a61c3c3f841332

platform:              Ubuntu 24.04
architecture:          aarch64
Python:                3.12.3
exit code:             0
stderr:                0 bytes
stdout SHA-256:        253c23d019de9e0c648a8adfa4547e009f4b198eaa017c0347e906e7afd02ac2
stdout bytes:          738
stdout lines:          18
RUN.md SHA-256:        e40d45665c0c5391a083899e5f327485b00d7cf5553bc0a626a8e03f12471353

GitHub workflow run:   29291022771
GitHub workflow job:   86954400056
x86_64 platform:       Ubuntu 24.04.4
x86_64 Python:         3.12.13
x86_64 exit code:      0
x86_64 stderr:         0 bytes
x86_64 verifier:       c9b4d253a609cc489efc4386e5e61d3e92baa16b736b899048f2a3afa5e78c99
x86_64 stdout:         253c23d019de9e0c648a8adfa4547e009f4b198eaa017c0347e906e7afd02ac2
```

`EXPECTED.txt` is the exact formal stdout. `RUN.md` contains only neutral
public environment fields. The repository self-check reran the pinned
verifier and reproduced `EXPECTED.txt` byte for byte with empty stderr.

The required pull-request check reran the same pinned verifier on GitHub
`x86_64` and reproduced `EXPECTED.txt` byte for byte with exit zero and empty
stderr. Together with the formal local `aarch64` record, this completes the
two-architecture computation gate for the exact finite result.

## Status routing

The exact finite trace fact has passed the two-architecture computation gate
at the frozen scope. The registered `-21/8` proposal is falsified at that
surface, while canonical operator selection remains open. The normative
registry and frontier transition is deliberately excluded from this probe
pull request and belongs to the separate sealed fold prescribed by the ruling.
