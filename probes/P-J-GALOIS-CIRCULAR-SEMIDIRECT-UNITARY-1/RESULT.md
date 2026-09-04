# P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1 result

Status: **candidate-T / L1 / TWO CLAIMS CONFIRMED LOCALLY / ARCHITECTURE GATE PENDING / PUBLIC CLAIMS UNREGISTERED / CANON UNCHANGED**

## Recorded decision

```text
J-GALOIS-CIRCULAR-QUOTIENT-SEMIDIRECT-UNITARY: CONFIRMED
J-GALOIS-CIRCULAR-ODD-CHARACTER:               CONFIRMED
gates:                                         18/18 PASS
exit/stderr:                                   0 / empty
stdout:                                        byte-identical to EXPECTED.txt
SCIENTIFIC-FIRED-A/B:                          NOT SELECTED
STOP:                                          NOT SELECTED
ABANDONED-PIN:                                 NOT SELECTED
ARCHITECTURE GATE:                             PENDING
MANUAL SECURITY REVIEW:                        PASS
```

The immutable verifier was executed exactly once after its public pin and
byte-for-byte remote readback. Its 26-line stdout has SHA-256
`f9f873397fc41389084e2d6aa9873858909303b60c5b8a304235a46013de32f6`.
No preregistered falsifier fired.

Manual security review of all five named probe files passed without
re-executing or importing the verifier. The pinned files and exact transcript
remain byte-identical to the recorded hashes. The verifier is deterministic,
bounded, standard-library-only, and free of file input, network, subprocess,
shell, dynamic execution, secrets, personal data, or private-machine
identifiers. The L1 scope and every physical and cross-layer firewall remain
intact.

The required GitHub-hosted x86_64 and aarch64 replay and aggregate policy
check remain pending. This file records the local result without pre-claiming
those gates.

## Claim A: quotient semidirect action and common positive form

For the actual integral circular quotient

```text
L=Alt^2(V_Z^*)/H_Z,  V_Z=O_K,
```

the ambient `J` pullback and the covariant pullback of the public Galois
automorphism both descend. The public circular lattice `C_Z` embeds in `L`
with index five and gives

```text
0 -> C_Z -> L -> Z/5 -> 0,
bar P on L/C_Z = -1,
bar S on L/C_Z =  2.
```

The rational extension of the public circular identification realizes

```text
L ~= I=(1+delta_10)^(-1) O_K,
bar P = m_(delta_10),
bar S = m_(delta_10^4) o gamma_3^Gal,
gamma_3^Gal=(gamma_2^Gal)^(-1).
```

Thus `bar S` is Galois-semilinear, not scalar `O_K`-linear, and

```text
bar S bar P bar S^(-1)=bar P^3.
```

The forty normal forms `bar P^a bar S^b` are distinct and give

```text
<bar P,bar S> ~= C_10 semidirect_3 C_4
               ~= C_2 x AGL_1(F_5),
linear image order      = 40,
projective image order  = 20,
projective kernel       = {I,-I}.
```

Both generators preserve the explicit positive Gram matrix

```text
G_L = [[2, 0,1, 0],
       [0, 2,0,-1],
       [1, 0,2, 1],
       [0,-1,1, 2]],
```

whose leading principal minors are `(2,4,6,5)`. This proves a common
Hermitian unitarization after restriction of scalars and complexification.
It does not select a Born normalization.

## Claim B: faithful odd induced character

Over `C`, `bar P` has simple spectrum

```text
delta_10^k,  k in {1,3,7,9}.
```

The exponent-three normalizer relation acts transitively on the four
character indices; dually, `bar S` transports the eigenline `k` to `7k`.
The resulting four-dimensional complex representation is irreducible and
monomial in the `bar P` eigenbasis.

Its exact character on all forty normal forms is

```text
chi(bar P^a bar S^b)=0,  b=1,2,3,
(chi(bar P^a))_(a=0..9)=(4,1,-1,1,-1,-4,-1,1,-1,1).
```

The norm is one, `chi(bar P^5)=-4`, and the linear kernel is trivial. Hence
this is the faithful odd constituent

```text
Ind_(C_10)^(G_C)(lambda_1),
lambda_1(bar P)=delta_10.
```

The complete complex irreducible census is eight one-dimensional and two
four-dimensional representations. The even four-dimensional constituent has
kernel `<bar P^5>` and is not the representation obtained here.

## Earned scope and firewalls

This is an L1 exact-algebra result. The new content is descent to the actual
circular quotient, preservation of its index-five sublattice and seam, the
central sign lift of the public affine group, one explicit common positive
form, and the faithful odd induced character.

The Galois operator is the missing noncommuting eigenline transporter, but it
is monomial in the spectral basis. It is not a Hadamard-like superposition
mixer. The linear group has forty elements but only twenty projective classes;
neither finiteness nor unitarizability licenses a physical qudit, Clifford
class, density, or universality claim.

No Born rule, probability law, state/effect interpretation, preparation,
measurement, apparatus, amplitude recombination, physical interference,
space, time, action quantum, numerical value of `h`, anyon identification,
topological protection, quantum advantage, or L2--L6 bridge is established.

Public Canon, Registry, Frontier, gates, dependencies, dictionaries, and
`STATUS.md` are unchanged. Any later registration requires a separate fold.
