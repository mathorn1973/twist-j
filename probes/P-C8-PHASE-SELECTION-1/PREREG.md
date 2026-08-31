# P-C8-PHASE-SELECTION-1 — preregistration

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**

Issue lock: #721

## Authority pin

- authority: Public Canon v72, `mathorn1973/twist-j main`
- public base: `d6e8e466c1d5b1c447acf12fc653059ae8aa65e7`
- predecessor: merged probe `P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1` / PR #717
- predecessor public claim status: unregistered
- action layer: L1 algebra / representation theory only

The public inputs used at their registered scopes are `PENTIT-ROOT-FACTS [T]`,
`RAMIFIED-TM-LIFT [T]`, and `SQRT-PHI-DIGIT-LIFT [T]`. The exact four-phase
representation found by #717 is rederived here where needed rather than treated
as a registered Canon dependency.

## Question

Classify the selector debt in the four exact phase representations

```text
rho_k : C8 -> mu_8,
rho_k(tau) = zeta_8^k,
k in {1,3,5,7},
```

without inserting a source-root choice or a target phase orientation as a
premise.

The probe separates two different binary choices:

1. source sign branch `tau <-> -tau`, which sends `k -> k+4`;
2. target C4 orientation `S <-> S^-1`, which exchanges the pairs
   `{1,5}` and `{3,7}`.

These choices must not be conflated.

## Frozen carrier

Work in

```text
F25 = F5[tau]/(tau^2 - 2),
J_lambda = 2 in F5^*,
R = {r in F25 : r^2 = J_lambda},
E = {rho_k : k in {1,3,5,7}}.
```

For the target comparison use a formal primitive eighth root `zeta_8`. Write

```text
T = diag(1,zeta_8),
S = T^2,
Z = T^4.
```

No physical qubit or gate is introduced by these names.

## G1 — intrinsic root pair and Frobenius

Exhaust `F25` and verify

```text
R = {tau,-tau},
ord(tau)=ord(-tau)=8.
```

For Frobenius

```text
sigma(x)=x^5,
```

verify that it fixes every element of `F5`, fixes `J_lambda=2`, and swaps the
root pair:

```text
sigma(tau) = -tau = tau^5,
sigma(-tau) = tau.
```

Thus `D=(F25/F5,J_lambda,R)` is Frobenius-fixed as an intrinsic datum while
neither point of `R` is fixed.

## G2 — four-representation torsor

Verify that the isomorphisms `C8 ~= mu_8` are exactly the four odd-exponent
maps `rho_k`, `k in {1,3,5,7}`.

Precomposition by source Frobenius acts by

```text
B(k) = 5k mod 8 = k+4 mod 8.
```

Postcomposition by target complex conjugation acts by

```text
O(k) = -k mod 8.
```

Verify that `B` and `O` are commuting involutions and that

```text
{id,B,O,BO}
```

acts freely and transitively on the four-element set `E`. The result is a
Klein-four torsor: a classification of selector freedom, not a selector.

## G3 — Frobenius sign-branch no-go

Freeze the selector class before execution:

A **Frobenius-natural root selector** is a rule that assigns one element
`s(D) in R` to the intrinsic datum `D=(F25/F5,J_lambda,R)` and is equivariant
under every automorphism of `D`, in particular Frobenius.

Because Frobenius fixes `D` but has no fixed point in `R`, equivariance would
force

```text
s(D) = sigma(s(D)),
```

which is impossible. Therefore no Frobenius-natural selector exists in this
frozen class.

Equivalently, once a target C4 orientation is held fixed, no selector using
only Frobenius-invariant source data can distinguish `rho_k` from
`rho_(k+4)`.

This is a relative no-go. It does not exclude a selector using additional
non-Frobenius-invariant structure.

## G4 — C4 orientation firewall

The sign-branch no-go MUST NOT be extended to the other binary choice.

Verify that the source power automorphisms which exchange the two C4
orientations do not preserve the marked source element `J_lambda=2`:

```text
(tau^3)^2 = (tau^7)^2 = 3 = J_lambda^-1 != J_lambda.
```

Equivalently, on exponent labels the Frobenius branch action `B` preserves the
partition

```text
{1,5}  -> J_lambda maps to S,
{3,7}  -> J_lambda maps to S^-1,
```

whereas target conjugation `O` exchanges the two parts.

Therefore this probe earns **no source-side impossibility theorem** for
`J_lambda -> S` versus `J_lambda -> S^-1`. `RAMIFIED-TM-LIFT [T]` already
carries the stronger source fact that the fixed `M_J/Tr_4` channel selects the
multiplier `2`, while the sign quotient alone is inversion-blind. What is not
supplied here is a forced comparison map from that source orientation to the
target phase orientation.

## G5 — full-k boundary

If both the source root branch and target phase orientation are left unchosen
and natural under `B` and `O`, the free transitive Klein-four action has no
fixed element of `E`. Hence there is no unique symmetry-natural `k` in that
frozen class.

A future unique `k` requires either:

- additional independently justified datum that breaks the relevant symmetry;
- a narrower admissible selector class with that narrowing justified before
  target comparison; or
- a proof that every final claimed readout is invariant under the surviving
  choice.

## Method

`verify.py` uses only exact integer arithmetic modulo five and modulo eight.
It exhausts all 25 field elements, both square roots, all four phase
representations, and all four elements of the generated Klein action. It uses
no floating point, files, network, subprocesses, external packages, or random
choice.

The mathematical no-go in G3 is carried by the fixed-point proof above; finite
execution audits the hypotheses and the finite group actions.

## Firewalls

This probe MUST NOT claim:

- that TWIST/J derives quantum mechanics or a physical `T` gate;
- that no conceivable extension can select `k`;
- a Frobenius-based source-side no-go for `S` versus `S^-1`;
- that the presentation symbol `tau` is itself a canonical root selector;
- that the principal complex embedding of `J` automatically supplies a map to
  the target qubit phase orientation;
- that target complex conjugation is a physical gauge identification;
- registration of the #717 result or closure of issue #716;
- Born, measurement, apparatus, Hamiltonian, speedup, universality, clock,
  gravity, SI, decoder, or L2-L6 conclusions.

## Falsifiers

Fire if any exact field, root, order, Frobenius, representation-census, `B`,
`O`, commutation, freeness, transitivity, or C4-orientation-boundary statement
fails; if a Frobenius-fixed root exists in `R`; if the declared natural-selector
no-go has a logical gap; or if the result silently imports a chosen source root
or target orientation.
