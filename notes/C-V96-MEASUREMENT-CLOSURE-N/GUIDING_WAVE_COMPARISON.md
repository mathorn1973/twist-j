# AH-SF-1 compared with guiding-wave constructions

PUBLIC, NON-CANONICAL comparison, 2 October 2026. This is a scoped literature
comparison, not a priority claim or a new physical occurrence derivation.
AH-SF-1 denotes the previously local conditional trial specified below;
this note does not claim a public reproduction of that entire trial.

## The AH-SF-1 ingredients being compared

The trial retains a coherent guide psi, one actual configuration q, and a
finite initially uniform word reservoir with a cursor. A supplied guide gate
G produces the next guide. For each spectator block it computes

```
a_i = |psi_i|^2,       b_j = |(G psi)_j|^2,
sum_j C_ij = a_i,      sum_i C_ij = b_j,
Pr(q_next=j | q=i) = C_ij/a_i       when a_i>0.
```

Its particular C uses a maximal diagonal part followed by lexicographic
residual transport. Seed intervals implement the conditional row law;
finite midpoint words approximate those intervals. The guide retains phase,
including correlations not present in the point marginal. Both the squared
marginals and the initial reservoir law are supplied. Equivariance of that
construction transports them; it does not derive them from native U or J.
This algebra states the comparison object without calling it Bohmian dynamics.

## What the established comparators actually provide

Bohmian mechanics combines an actual particle configuration with a wave
function and a specified deterministic guiding velocity. Quantum equilibrium
and the effective wave function support its statistical account. A new
uniform random word at each measurement is not its defining dynamical law.
The equilibrium/typicality argument is a substantive part of the model, not
the claim that every arbitrary initial ensemble becomes uniform. See
[Durr, Goldstein and Zanghi, Quantum Equilibrium and the Origin of Absolute
Uncertainty](https://arxiv.org/html/quant-ph/0308039v1), published in 1992.

Bell-type theories provide a closer comparator for discrete configuration
transitions: the quantum state and Hamiltonian determine jump rates, and
equivariant processes preserve the squared-state distribution. Their minimal
jump-rate construction is not AH-SF-1's discrete-time diagonal/lexicographic
coupling. Neither equality of trajectories nor derivation of one rule from
the other has been shown. See [Durr, Goldstein, Tumulka and Zanghi, Bell-Type
Quantum Field Theories, sections 2.1-2.3 and 2.7](https://arxiv.org/html/quant-ph/0407116v1).

Goldstein and Struyve prove uniqueness of quantum equilibrium among
equivariant distributions that are local functionals of the wave function
for their Bohmian dynamics. This restricted uniqueness theorem does not
select a measure for arbitrary integer automata or for a different coupling
C. The locality condition concerns the wave-function functional, not an
automatic physical-port locality certificate. See [On the Uniqueness of
Quantum Equilibrium in Bohmian Mechanics](https://arxiv.org/html/0704.3070v1).

## What can and cannot be called new here

| Feature | Assessment for AH-SF-1 |
|---|---|
| Guide plus one actual configuration | An established type of construction; its presence alone supports no novelty claim. |
| Squared guide weights and equivariance | Established comparison concepts; AH-SF-1 inserts squared marginals into its own transition rule. |
| Uniform finite reservoir | A particular added sampling resource. It is not a universal ingredient of deterministic guiding-wave dynamics. |
| Diagonal/lexicographic coupling and finite-grid error account | A concrete conditional algorithm to assess on its own merits; no claim of literature priority or a new physical principle is established. |
| Phase retained through successive records | A necessary continuation property already expected of the comparator class; mere success here does not derive preparation. |
| Native U/J implementation and physical preparation | Still absent. Comparison with a guiding-wave model supplies neither. |

The useful novelty question is therefore whether a proposed native model
independently supplies the actual dynamics, preparation and record law with
fewer or differently justified assumptions. A larger reversible simulator
or another proof that a supplied square-weight coupling is equivariant does
not by itself answer that question. The new counting hypothesis must be
assessed separately at its frozen carrier and trial semantics.
