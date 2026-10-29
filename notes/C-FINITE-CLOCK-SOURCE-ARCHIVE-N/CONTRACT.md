# The common apparatus contract

2026-10-29. NON-CANONICAL, conditional analytical L1 proposal.
This document fixes one mathematical interface. It is not an execution
preregistration, experimental result or physical acceptance.

## Declared objects

| Object | Fixed meaning |
| --- | --- |
| System | Complete16D total-momentum-pi sector of two distinguishable mu=2 walks on the four-site ring |
| Target | G_j=W_j...W_1, with W_j=C_j(V_g tensor I), not the unrecorded V_g^j |
| New record | N five-level cells; complete modular-add gates from one fixed projective partition of S |
| Old record | Arbitrary occupied register O retained as an identity factor, including its correlations |
| Source | One finite box B_M with one initially independent sine packet beta_M |
| Clock | One finite Fourier clock C_L with one supplied coherent ready packet f_L |
| Account | E_M=H_S+H_B; the new archive and clock have declared zero terms in this account |
| Generator | The full positive bounded static H in PROOF.md Section6; generally H differs from E_M |
| Read times | Every prefix tick j tau,0<=j<=N, and every time in [N tau,(N+1)tau] for the final channel |
| Output | Whole joint state including source, clock, active archive and arbitrary passive reference |
| Error | Joint vector/isometry error at most epsilon; half-diamond and trace distance at most min(1,epsilon) |

The quantifiers are: for every finite N, supplied g and tau, and positive
epsilon, construct one finite apparatus; for every admitted input and
reference, all declared times obey its bound. This does not interchange
the horizon and apparatus quantifiers.

## Preparation and use

The system, older record and reference may initially be arbitrarily
correlated. New zero cells, beta_M and f_L are independent supplied ready
factors. There is no preparation from one equilibrium bath in this
contract. The source may become correlated during evolution and is never
replaced. Full-shell homomorphism handles those correlations for each
prefix. Active archive cells belong to the source-lift system, not merely
to a passive-reference qualification.

The original complete archive state is retained. No occupied value is
erased. Later ideal stages leave earlier written cells alone. Actual
finite-clock states obey the complete joint comparison at the stated
times; no stronger continuous-time nondisturbance is inferred.

The evolution is uninterrupted. A measurement at an earlier tick and
subsequent conditioning is a different intervention protocol. The result
is unconditional and has no successful-read denominator. Its finite
window does not mean a stopped clock or indefinite storage.

## Proof obligations and failure conditions

The construction would fail if an active archive degree were omitted
from a complete shell, a boundary state lacked a unitary extension, the
source estimate required an unjustified product state between stages,
or the spectral convention for a stage omitted eigenvalue -1. It would
also fail if the clock packet overlapped a pulse at a nominated boundary,
wrapped into the next program during the final window, lost its common
projection norm, or dropped the boost-induced phase.

Its analytical acceptance requires the explicit H^2/Duhamel argument,
the interacting rotor tail bound, the finite compression comparison,
finite noncircular resource choices, exact conservation on the entire
carrier, and one joint reference-sensitive output statement. Separate
component successes alone do not meet these obligations.

Spatial locality, preparation work, original26-state capture behavior,
native-U implementation and identification of H with physical energy are
not included. Adding one of these requirements changes this contract and
requires another proof. No earlier proof or run is modified here.

Copyright 2026 A. M. Thorn. Apache-2.0, under the repository license.
