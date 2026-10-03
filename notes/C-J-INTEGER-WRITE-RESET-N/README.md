# Integer write, hold and reset with finite-phase readout

**PUBLIC / NON-CANONICAL / candidate-T / L1 only / no authority.**
Author: A. M. Thorn <thorn@twistj.com>.
Owner: [#1292](https://github.com/mathorn1973/twist-j/issues/1292).
Basis: Public Canon v94, main/tag target
`af8dc5956e26917b265fd0070f500c841c326512`.

This note constructs a complete classical arithmetic transaction: transfer a
source message into a ready integer memory, hold it for any number of exact
J steps, read it with a finite phase, and restore source and work ports to
ready while moving the complete held state into one unbounded integer archive.
Every operation is a bijection on its declared complete carrier, not only an
injection on prepared states. The source is vacated by transfer, not copied
and then silently discarded. Zero is a valid occupied message.

The construction is an **explicitly added nonlinear architecture**. J supplies
the holding operation and its residue arithmetic; it does not supply the
write coupling, occupancy flags, phase clock, archive packing or schedule.
The unchanged native U is neither modified nor claimed to implement them.

| Question | Exact result in this note |
| --- | --- |
| Read all 625 coefficient-residue messages after arbitrary J holding | Residue modulo five plus phase modulo twenty suffices. Twenty is least in the full-residue-alphabet, residue-only observation class. |
| Transfer into a ready memory | A phased exchange of the low residue digits and occupancy flags is a global involution and vacates the source port. |
| Reset after the source is absent | A global involution moves the entire integer memory and its phase into a tagged integer stack and returns work memory to ready. |
| Erase only the visible residue and phase | Impossible on the displayed held-state pair 1 and J^20 unless their remaining distinction survives elsewhere. |
| Append independent messages by E -> J E + c_p | Impossible for two or more messages when every old E in O is admitted. J is unimodular; the message images coincide. |
| General affine append on Z^d | Injectivity is equivalent to a nonsingular old-archive matrix and distinct message cosets. Capacity is at most the matrix index. |
| A nonunit radix comparison | Multiplication by five has index 625; a two-register digit transfer is globally reversible when the quotient is retained. |

One integer register is not finite memory capacity. Its bit length grows and
the packing operations have no established constant bit cost, locality,
energy cost or physical implementation. A fixed finite clock is enough for
the current message read, while the exact archive preserves unbounded hidden
information, including information about elapsed holding that may reside in M.

The negative result for unit append is scoped to the displayed affine class
on the unrestricted old-archive lattice. It is not a theorem against all
J-based codes on restricted reachable sets, all nonlinear archives, or all
physical memory. The positive result is an existence witness, not a selection
theorem for the added interaction.

The finite-closed-permutation recurrence argument is distinct from the native
finite-window dyadic-period candidate discussed after PR #1291. The latter is
not a premise here and is not promoted or silently incorporated by this note.

Read [PREREG.md](PREREG.md) for the exact comparison class,
[PROOF.md](PROOF.md) for the constructions and obstructions,
[REVIEW.md](REVIEW.md) for the exposed proof review, and
[PROMO-C-J-INTEGER-WRITE-RESET-N.md](PROMO-C-J-INTEGER-WRITE-RESET-N.md)
for the promotion boundary. No new scientific program was executed. All
25 public H/O obligations stay open; no Canon or physical gate changes.
