# P-J-FIBONACCI-BRAID-1 result

Status: **candidate-T / L1 / TWO CLAIMS CONFIRMED / TWO-ARCHITECTURE COMPUTATION GATE PASS / PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED**

## Recorded decision

```text
J-CM-FIBONACCI-BRAID-PROJECTIVE-NONMEMBERSHIP: CONFIRMED
J-CIRCULAR-FIBONACCI-DETERMINANT-CHARACTER:     CONFIRMED
gates:                                         17/17 PASS
exit/stderr:                                   0 / empty
stdout:                                        byte-identical to EXPECTED.txt
SCIENTIFIC-FIRED-A/B:                          NOT SELECTED
STOP:                                          NOT SELECTED
ABANDONED-PIN:                                 NOT SELECTED
ARCHITECTURE GATE:                             PASS
MANUAL SECURITY REVIEW:                       PASS
```

The immutable verifier was executed exactly once after its public pin and
byte-for-byte remote readback. Its 23-line stdout has SHA-256
`09886942e87b9962b85f9823eeac8b4fb36b9f41489ecae3731dac9a30240999`.
No preregistered falsifier fired.

## Required two-architecture workflow

```text
pull_request:          796
tested_head:           c0518fc2bc02a8ca78b5c5c4006449c14496ccfd
workflow_run:          33793354343
x86_64_job:            100775018150 success
aarch64_job:           100775018233 success
aggregate_check_job:   100775105189 success
verifier_sha256:       d30193d720e57a8e35c0ee40161406f50150ff024d96d240c44c699b869b1b77
stdout_sha256:         09886942e87b9962b85f9823eeac8b4fb36b9f41489ecae3731dac9a30240999
stdout_bytes/lines:    1391 / 23
byte_identity:         PASS on x86_64 and aarch64
manual_security:       PASS on the five named probe files
```

Both architecture jobs passed repository policy, all 148 unit tests, Canon,
ledger, gate-contract, changed-probe reproduction, and exact transcript
comparison. The aggregate job reported `TWO-ARCHITECTURE CHECK PASS`. Their
common verifier receipt is

```text
VERIFY PASS P-J-FIBONACCI-BRAID-1 d30193d720e57a8e35c0ee40161406f50150ff024d96d240c44c699b869b1b77 09886942e87b9962b85f9823eeac8b4fb36b9f41489ecae3731dac9a30240999
```

Manual security review found only fixed exact inputs, bounded small-matrix
loops, deterministic ordered output, and standard-library `Fraction` and
`combinations` imports. It found no file, network, subprocess, shell, dynamic
execution, environment read, random, clock, secret, or private-machine data
surface. The recorded invocation trusts the named system Python and its normal
site startup; it does not use `-I` or `-S`. The empty environment and absence
of hook modules in the reviewed tree bound that non-blocking trust assumption.

`RUN.md` remains the immutable historical record of the sole local formal leg
and therefore retains `architecture_gate: PENDING`; this result section closes
that gate with the public workflow receipt above.

## Claim A: exact projective nonmembership

The derived hyperbolic restriction is

```text
A_CM = [[ 1,-1],
        [-1, 2]],

kappa(A_CM)=tr(A_CM)^2/det(A_CM)=9.
```

The frozen Fibonacci generators preserve the positive Hermitian form
`G_Fib=diag(a,1)` in the selected embedding. Every braid word is therefore
conjugate to a unitary matrix. For every invertible two-by-two unitary matrix,
the conjugacy- and scalar-invariant quantity `kappa=tr^2/det` lies in `[0,4]`.
The exact value `9` proves that there are no

```text
w in B_3, lambda in C^x, G in GL_2(C)
```

with

```text
A_CM = lambda G^-1 rho(w) G.
```

The same continuous invariant excludes the closure of the projective-unitary
locus. This conclusion is exact and does not depend on a bounded word search.

## Claim B: exact determinant-character channel

The unimodular `c2` orbit gives the integral intertwiner

```text
(C_Z,P_C) ~= (Z[delta], multiplication by delta),
delta=1-J=-zeta_5^2,
```

with `delta` of exact order ten and `Z[delta]=Z[zeta_5]`. In the frozen linear
ribbon normalization,

```text
det(B_1)=det(B_2)=delta.
```

Consequently, for the exponent-sum homomorphism `e:B_3->Z`,

```text
det(rho(w))=delta^e(w),
chi_C(w)=P_C^e(w),
```

and `chi_C` is integrally isomorphic to the underlying `Z`-lattice action of
the scalar determinant character. The companion intertwiner was checked for
the full integral module, including inverse generators.

## Earned scope and firewalls

These are L1 exact algebraic results only. The raw `M_J` remains a type
boundary and is not identified with a braid generator. The circular result is
an abelian rank-one determinant shadow, not the full nonabelian rank-two
Fibonacci representation, and it depends on the frozen linear ribbon lift
rather than only its projective class.

No phibit or other TWIST-J object is identified with `tau`. The Galois/
Lee--Yang branch and any enriched carrier remain outside this decision. No
action quantum, numerical value of `h`, Born rule, preparation, apparatus,
sampling law, physical realization, topological protection, universality,
quantum advantage, or L2--L6 bridge is established.

Public Canon, Registry, Frontier, gates, dependencies, dictionaries, and
status rows are unchanged. Any later registration requires a separate fold.
