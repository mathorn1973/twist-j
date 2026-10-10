# Contact control and the complete-source boundary

**PUBLIC / NON-CANONICAL / conditional L1 analysis.**
Author: A. M. Thorn <thorn@twistj.com>. Date: 2026-10-10.
Reservation: [#1442](https://github.com/mathorn1973/twist-j/issues/1442).
Basis: Public Canon v101, main `a18e65d3e43acc6cb1896296b8bd0fdecdad35a7`.

The occupied SUM construction in [#1439][sum-pr] preserves its added
classical source coordinate. This note makes the next admission question
concrete: what controls implement the contact, and what does preserving a
complete source mean if coherent states are admitted?

There are two results. First, the already described conditional five-level
control family can implement the complete contact exactly after explicitly
extending its access to the seventh source system. The construction uses
local operations and pair additions, with a cubic phase compiled by
compute-phase-uncompute and no initially blank work register. It does not
require postulating a new three-body coupling. Its physical carrier,
external controls, energy supply and timing remain declared resources.

Second, preserving the scalar source value does not imply preserving an
arbitrary quantum source state. For a fixed checkpoint on the prepared
occupied-SUM orbit (where h is nonzero), the five source values produce
five orthogonal records. Under the stated
quantum comparison, the source's reduced density matrix therefore loses
all off-diagonal entries in that basis. A uniform coherent source becomes
I/5 locally, while its complete joint output remains pure and reversible.
This is an application of standard information/disturbance mathematics.

| Requested source contract at the contact endpoint | Result |
|---|---|
| Preserve each orthogonal classical source value and write it | Compatible with the exact contact. |
| Preserve every diagonal source mixture | Its source marginal is preserved; source/receiver correlations change. |
| Preserve every unknown quantum state and its reference correlations while retaining an informative new record | Impossible in the stated deterministic quantum-channel model with independent initial apparatus. |
| Preserve full joint information and allow source backaction | The adopted unitary contact does this; restoration must account for every retained record. |

For a receiver preparation that suppresses information transfer, all source
states can instead be preserved. Thus this is not a general ban on source
preservation, a contradiction of the classical probe, or a proof that the
native ontology must be quantum. An erased or copied record must be counted
where it actually remains.

The admission audit also distinguishes finite-field point tables from
chosen polynomial Hamiltonian lifts. Two explicit lifts implement the same
receiver point contact with different extra-source kicks, so no universal
conjugate kick or physical energy follows from the point table alone. A
separate clean additive-energy condition constrains the receiving port
spectra; it does not assign them a physical Hamiltonian.

Read [CONTRACT.md](CONTRACT.md) for the physical resource ledger, preservation
definitions, outside-SUM calibration and lift ambiguity;
[CONTROL-PROOF.md](CONTROL-PROOF.md) for the exact circuit and conditional
energy boundary; [SOURCE-PROOF.md](SOURCE-PROOF.md) for the complete source
channel and restoration theorem; and [REVIEW.md](REVIEW.md) for the disclosed
separate derivation and cross-review. [VALIDATION.md](VALIDATION.md) records
text custody and repository integration separately from scientific evidence.

No experiment, new scientific program or verifier was run for this note.
No Canon fold or physical-owner closure is claimed. The remaining physical
choice is explicit: admit an orthogonal classical source family, accept
coherent backaction and joint records, or change the informative-transfer
specification. Actual physical carrier/control admission remains necessary
for each realizable option; a successful circuit identity does not supply it.

[sum-pr]: https://github.com/mathorn1973/twist-j/pull/1439
