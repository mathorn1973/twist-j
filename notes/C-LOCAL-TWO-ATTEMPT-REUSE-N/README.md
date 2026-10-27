# Local thermal control for two retained attempts

**NON-CANONICAL, L1. Analytical candidate; independent acceptance pending.**
Author: A. M. Thorn. License: Apache-2.0. Public reservation: #1769.

This is a separate successor to the frozen twenty-two-file package in
[PR #1768 at 811daddc3b2f085ee5bc6f50261ac95a4c11fe44](https://github.com/mathorn1973/twist-j/tree/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N).
The old branch and source files are not changed. The prior independent
mathematical PASS covers only its older seven-file revision d138517;
the later local, thermal and reuse layers remain conditional inputs
awaiting independent review.

The construction supplies a single local positive static Hamiltonian
for two source attempts, two retained outputs and a final reset of the
working hardware at its original physical sites. One counted thermal
controller runs the sequence. A fixed first record remains available
during reset one and attempt two. One joint output channel retains
both records, the restored hardware, the supplied next input and an
arbitrary passive reference, including their permitted correlations.

[CONTRACT.md](CONTRACT.md) fixes support, geometry, coupling cap, errors,
resources and failure conditions at the preceding analytical contract
pin 49753622604d8c64f12b9ac5d8889831e1a5f168. That file is unchanged.
This is an exposed analytical construction, not blind discovery or a
scientific execution. No new scientific program or matrix expansion ran.

The proof is divided into the following auditable statements.

- [LOCAL_COMPILATION.md](LOCAL_COMPILATION.md) approximates each complete
  raw core endpoint by local gates with operator error below 2^-120,
  including the onsite phases. The complete two-run error is below
  2^-119, uniformly with a reference; exports and resets are exact.
- [LOCAL_CONTROLLER.md](LOCAL_CONTROLLER.md) gives coordinates, all
  transport/return edges and the thermal static law. Each term uses at
  most nine qubits, radius 256, incidence 64 and fixed norm cap J_*.
  It counts every auxiliary, interaction energy, entropy and time scale.
- [TWO_USE_CHANNEL.md](TWO_USE_CHANNEL.md) proves the exact replacement
  identity and the completed joint actual-thermal error below 2^-96.
  Both accepted records have probability above 1/12000000000 and joint
  ideal-ready error below 2^-67, within the fixed 2^-60 target. The
  common outer launch is counted once, even for correlated inputs.
- [RESOURCE_ACCOUNT.md](RESOURCE_ACCOUNT.md) connects these results to
  prepared stock, two temperatures, first-record availability, a finite
  read window and the distinction between a reset core and a renewed
  whole apparatus.
- [VALIDATION.md](VALIDATION.md) records immutable inputs, proof hashes,
  integrity checks and the independent review obligations.

The fixed-strength time scale is T_hold=pi hbar(K_out+1)/(3g_out).
The first export is available from T_hold/2; the final completed window
is [T_hold,2T_hold]. Conditional active-history failure weights are
below 2^-128; these are not unconditional detector success rates.
The clean closed law returns at 3T_hold and undoes the exports too.
Permanent closed storage, perturbation robustness and regeneration of
spent stock are not supplied. Canon and the frozen source remain
unchanged; neither this successor nor the three inherited layers gain
independent acceptance from the authoring checks or repository CI.
