# P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1 — preregistration

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**

Issue lock: #716

## Question

Does the already-carried XOR/AND carry algebra and the exact TWIST/J cyclic tower admit an exact representation-theoretic bridge to standard qubit phase gates, while remaining strictly at L1 and making no physical identification?

## Frozen scope

The probe tests three exact statements.

### G1 — C4 carry-phase identity

For bits `a,b in {0,1}` and `S = diag(1,i)`, `Z=S^2`, verify

`S^a S^b = S^(a XOR b) Z^(a AND b)`.

The intended algebraic source is the section identity for `C4=<g>`:

`g^a g^b = g^(a XOR b) (g^2)^(a AND b)`.

### G2 — quadratic carry phase

For `x in F_2^4`, define

`q(x)=sum_{i<j} x_i x_j mod 2 = binom(popcount(x),2) mod 2`.

On the 4-qubit computational basis, verify the exact diagonal identity

`U_q |x> = (-1)^q(x)|x> = (product_{i<j} CZ_ij)|x>`.

Also verify that the nonzero `q=0` locus is exactly `{1000,0100,0010,0001,1111}`, matching the already-carried CARRY-PENTAD carrier, but do **not** assign it a physical meaning.

### G3 — C8/C4/C2 phase-tower bridge

Using the already-carried exact relations in `F_25`:

`tau^2 = J_lambda`, `tau^4 = -1`, `ord(tau)=8`, `ord(J_lambda)=4`,

verify that every group isomorphism from `<tau> ~= C8` to the eighth roots of unity sends a generator to `exp(i*pi*k/4)` for odd `k`, hence its one-qubit diagonal realization is an odd power `T^k` of `T=diag(1,exp(i*pi/4))`.

Under that representation,

`tau -> T^k`, `J_lambda=tau^2 -> S^k`, `-1=tau^4 -> Z`,

with `S=diag(1,i)`, and changing the algebraic branch `tau -> -tau=tau^5` multiplies the represented gate by `Z`.

The probe records, as an external standard quantum-computation comparison only, that odd powers of T are non-Clifford while S and Z are Clifford. This comparison is **not** a TWIST/J physical promotion or a proof of quantum speedup.

## Firewalls

The probe MUST NOT claim any of the following:

- TWIST/J derives quantum mechanics;
- `tau`, `J_lambda`, the pentad, or any Canon carrier is a physical qubit or physical phase;
- a Born rule, measurement law, apparatus, state preparation, decoherence law, Hamiltonian, or L2-L6 lift;
- that the nontrivial `H^2(C2,C2)` extension class remains nontrivial after embedding its kernel into `U(1)`;
- quantum computational advantage from the C4/quadratic layer alone;
- selection of a unique C8 generator orientation from the existing algebra.

The distinction between algebraic representation and physical realization is load-bearing.

## Falsifiers

The probe fires if any exact G1, G2, or G3 identity above fails, if the branch/orientation statement is wrong, or if an attempted proof requires a physical premise excluded by the firewalls.

A failure to derive physical quantum mechanics is **outside scope**, not a falsifier.
