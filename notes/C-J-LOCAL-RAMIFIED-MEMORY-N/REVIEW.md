# Exposed proof review

**NON-CANONICAL / L1 only.** Author: A. M. Thorn <thorn@twistj.com>.
Owner #1294. Review is of written mathematics, not a scientific execution.

The construction was developed with three separate reasoning reviewers.
The digit obstruction, balanced-digit carry circuit, Smith charts, finite
endpoint transport, phase interfaces and locality lower bound were shared
openly. These reviews are not blind discovery or independent experimental
replications. All three reviewed the actual files and returned PASS subject
to the entry-section clarification recorded below, which has been applied.
The inverse-pass directions and inverse receiving-register reserve were
also made explicit before publication.

| Review | Scope | Disposition |
| --- | --- | --- |
| A | General digit obstruction, six-cycle, clean adder, J factorization, latency and controller | PASS with entry-section clarification applied |
| B | Smith charts, full inverses, phase-four/twenty readers and inverse pass order | PASS with entry-section and traversal clarification applied |
| C | Finite alphabet, endpoint transport, reserve, local scheduler and full-carrier scope | PASS with entry-section clarification applied |

## Issues resolved during derivation

- Unique one-step beta division does not imply finite expansions. The
  nonzero fixed point d/j proves the general obstruction, and the explicit
  six-cycle proves failure of closure even at J times 1 for digits 0,...,4.
- The positive construction changes to balanced base-five coefficient
  tracks. It does not silently claim the failed literal digit class works.
- Division by beta is not introduced as a global primitive: P M_beta=D Q
  reduces the complete two-register operation to an actual digit transport.
- An endpoint digit is not erased. The finite rotation is a permutation,
  and its integer reading requires a proved zero receiving top digit.
- Every local carry gate is a permutation, including on dirty workspace.
  Cleanup uses the updated digit and proceeds from high to low. Exact
  integer arithmetic is restricted to the reserved, prepared domain.
- The circuit family has finite cell alphabets but length-dependent depth.
  It is not presented as a single autonomous native transition.
- A subsequent explicit one-head scheduler internalizes the fixed program.
  It retains endpoint/side marks, acts on exactly one head and arbitrary
  data/workspace, and distinguishes the program phase from the read phase.
  Its control cycle is not a cycle of the full data state. It supplies no
  automatic growth or native source coupling.
- A single beta write admits a modulo-four phase reader, whereas the full
  modulo-five source needs phase twenty. These are different interfaces.
- Relative write phase, occupancy and full mixed-operation history are
  retained obligations; no irreversible clock reset is smuggled into readout.
- Reversible operations and a finite residue reader do not defeat finite
  closed-system recurrence, select a physical graph, or realize native U.
- The macro operation is read at the explicit head entry/return section
  (0,+,0). A full controller turn from an arbitrary other head phase gives
  a cyclically shifted gate word; it is not silently identified with the
  same prepared macro operation.

## Validation ceiling

The candidate statements rely on exact written proofs. No new scientific
verifier was compiled or run, and no table above comes from an executed
search. Repository policy, Canon/hash, ledger and gate checks are
administrative. Final check results and public custody belong in the owner
issue, rather than being predicted here.

No Canon, registry, frontier, gate, old probe, workflow or release is edited.
