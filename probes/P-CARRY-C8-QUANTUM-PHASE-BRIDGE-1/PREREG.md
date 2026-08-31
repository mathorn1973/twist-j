# P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1 — preregistration

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**

Issue lock: #716

## Authority pin

At preregistration review:

- authority: Public Canon v72, `mathorn1973/twist-j main`
- public main base: `de5210f4a1bfe801d994137132a3dca4e72ff7ef`
- Canon content commit: `aac8a3a4aff027beb2b08edbde1ae8e59224914c`
- Canon SHA-256: `39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70`

The exact public inputs used here are the already-carried L1 algebra around `RAMIFIED-TM-LIFT`, `CARRY-PENTAD`, `PENTIT-ROOT-FACTS`, `MAGIC-PRIME-GATE`, and `QUBIT-FROM-F5`. The probe does not reopen or strengthen those claims.

## Question

Do the already-carried XOR/AND carry algebra, the quadratic carry form, and the exact order-eight pentit subgroup admit an exact representation-theoretic bridge to the standard one-qubit phase hierarchy, while remaining strictly L1 and making no physical identification?

## Frozen scope

The probe tests three exact statements and one mandatory cohomology firewall.

### G1 — C4 carry-phase identity

For bits `a,b in {0,1}` and

`S = diag(1,i)`, `Z=S^2`,

verify

`S^a S^b = S^(a XOR b) Z^(a AND b)`.

The algebraic source is the section identity for `C4=<g>`:

`g^a g^b = g^(a XOR b) (g^2)^(a AND b)`.

Equivalently, the kernel-valued carry is `(g^2)^(a AND b)`.

### G1b — U(1) cohomology firewall

Under the sign character `g^2 -> -1`, the carry becomes `(-1)^(a AND b)`. Verify explicitly

`(-1)^(a AND b) = i^a i^b / i^(a XOR b)`.

Thus the displayed `U(1)`-valued phase factor is a coboundary for this chosen section. The probe MUST NOT claim that the nonzero `H^2(C2,C2)` extension class remains nonzero after passage to `U(1)` coefficients.

### G2 — quadratic carry phase

For `x in F_2^4`, define

`q(x)=sum_{i<j} x_i x_j mod 2 = binom(popcount(x),2) mod 2`.

On the formal four-qubit computational basis, verify the exact diagonal operator identity

`U_q |x> = (-1)^q(x)|x> = (product_{i<j} CZ_ij)|x>`.

Also verify that the nonzero `q=0` locus is exactly

`{1000,0100,0010,0001,1111}`,

matching the already-carried `CARRY-PENTAD` set. This is an algebraic/operator comparison only.

### G3 — C8/C4/C2 phase-tower bridge

Use the already-carried exact pentit relations in `F_25`:

`tau^2 = J_lambda`, `tau^4 = -1`, `ord(tau)=8`, `ord(J_lambda)=4`.

Let `zeta_8` be a formal primitive eighth root and

`T = diag(1,zeta_8)`, `S=T^2`, `Z=T^4`.

Every group isomorphism `<tau> ~= <zeta_8> ~= C8` sends `tau` to `zeta_8^k` for exactly one odd `k in {1,3,5,7}`. Verify under the corresponding diagonal representation

`tau -> T^k`,
`J_lambda=tau^2 -> S^k in {S,S^-1}`,
`-1=tau^4 -> Z`.

Changing the algebraic sign branch `tau -> -tau=tau^5` must multiply the represented phase gate by `Z`.

For the comparison with standard quantum-computation terminology, freeze the definition: a one-qubit Clifford unitary normalizes the Pauli group. For `P_k=diag(1,zeta_8^k)`, verify directly from `P_k X P_k^dagger` that `P_k` is Clifford iff `k` is even. Therefore every generator image `T^k`, with `k` odd, is non-Clifford, whereas the carried `C4` images `S^±1` and `Z` are Clifford. This is an exact operator classification, not a speedup or universality claim.

## Firewalls

The probe MUST NOT claim any of the following:

- TWIST/J derives quantum mechanics;
- `tau`, `J_lambda`, the carry pentad, or any Canon carrier is a physical qubit, state, phase, gate, or apparatus;
- a Born rule, measurement law, state preparation, decoherence law, Hamiltonian, or L2-L6 lift;
- that the `H^2(C2,C2)` class survives as a nontrivial `U(1)` class;
- quantum computational advantage from the `C4` or quadratic layer;
- universal quantum computation from this bridge;
- selection of a unique `C8` generator orientation or sign branch from the existing algebra.

The distinction between abstract algebra/operator representation and physical realization is load-bearing.

## Method

`verify.py` uses integer exponent arithmetic modulo 8 only. It contains no floating point, numerical approximation, network, files, subprocesses, random choice, or external package.

The all-element scopes are finite and exhausted exactly: four bit pairs, sixteen `F_2^4` vectors, and all four generators of `C8`.

## Falsifiers

The probe fires if any exact G1, G1b, G2, or G3 identity fails; if the pentad locus differs; if an odd `C8` generator image normalizes the Pauli group; if the branch relation is wrong; if the cohomology firewall is false; or if a proof requires a physical premise excluded above.

Failure to derive physical quantum mechanics is outside scope, not a falsifier.
