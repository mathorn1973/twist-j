# Finite reversible control cannot hide a one-time permanent write

**PUBLIC / NON-CANONICAL / conditional L1 proof / analytical result exposed.**
Author: A. M. Thorn <thorn@twistj.com>.
Claim: [#1440](https://github.com/mathorn1973/twist-j/issues/1440).
Basis: Public Canon v101, public main
`c17fe88ddd3b95ab8ff76ac7923a37f582c97571`.

The occupied SUM construction now merged in [#1439][sum-pr] gives a first
stable sum and a later accumulated sum on the actual native trajectory.
Its one-time trigger reads the absolute counter. This note identifies a
specific resource that cannot be removed by silently substituting a fixed
finite reversible controller that sees only the recurrent local clock.

For a minimal two-sided Thue-Morse driver, let B contain every finite data,
source, program, controller, clock-phase and environment register. Freeze a
continuous driver-dependent update on B that is a permutation for each
legal driver context. Arbitrary state feedback is allowed within that
complete permutation. Then every point of the auxiliary driver-plus-B system lies in a
minimal component. Every observed fixed local event recurs with bounded
gaps; a fixed finite-valued readout that is eventually constant must already
have had that value at every earlier time in this stationary interface.

This is an application of the standard recurrence property of compact group
extensions. The proof is supplied in full. The contribution here is the
explicit controller class, its application to the actual synchronized native
trace sheets, and the resulting limitation on replacing the occupied-write
trigger. It is not a claim of a new general theorem in topological dynamics.

| Proposed capability | Conclusion in the declared class |
|---|---|
| A contact fires exactly once after the stationary interface is active | Impossible for a fixed local event predicate. |
| A readout changes from a to b != a and remains b forever | Impossible. |
| A finite reversible controller uses state-dependent feedback | Covered only when the whole feedback map is a permutation at every driver context. |
| A large finite register retains the second record for a chosen finite horizon | Not excluded; an explicit cyclic-controller construction achieves it conditionally. |
| The actual unbounded U-counter returns to its old value | Not asserted; only its finite observation/controller factor recurs. |

The theorem does not eliminate the conditional construction in #1439: its
explicit `n=N` test is outside the new counter-blind class. Nor does it
contradict the first native transient write, which uses a noninjective
synchronizing update before stable operation. Origin markers, incomplete
window warmup, an absorbing irreversible halt, unbounded storage, modified
driver dynamics or a different observation contract must be accounted for
as different resources, not smuggled into B or its stationary driver input.

The constructive finite-horizon comparison keeps the already declared
contact and adds a cyclic finite controller. It demonstrates that this
obstruction concerns indefinite retention, not a universal finite lifetime,
a hardware lower bound, or an energy/entropy cost. No bound uniform over all
controller sizes and all permitted windows is claimed.

Read [PROOF.md](PROOF.md) for the precise model, recurrence argument, native
application and finite-horizon construction; [REVIEW.md](REVIEW.md) for the
separate exposed assistant derivation; and [SOURCES.md](SOURCES.md) for
prior work and exact scope boundaries. [VALIDATION.md](VALIDATION.md)
distinguishes text/custody checks from scientific execution.

No new scientific program, finite search, verifier or simulation is supplied
or executed for this note. No existing sealed probe is resumed or changed.
This is not an accepted physical contact, QDD event law, source-selection
principle or Canon promotion. The physical apparatus owners remain open.

[sum-pr]: https://github.com/mathorn1973/twist-j/pull/1439
