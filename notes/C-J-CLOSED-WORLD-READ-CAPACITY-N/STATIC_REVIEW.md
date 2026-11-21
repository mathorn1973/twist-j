# Source-visible static review before the scientific code pin

**NON-CANONICAL; L1; static review only.**

Reviewer: A. M. Thorn / capacity-theory review lane, 2026-10-23.
The reviewer read verify.py and the public preregistration and proof. This is not the code-independent breaker, not blind confirmation, not execution, and not a two-architecture result. The finite reconnaissance is exposed.

Reviewed verifier SHA-256:

    0d088a7bbb06f1b0b97680d71dc848f654d91ae7948777b7cb6a7cf062a9f230

Reviewed PREREG.md SHA-256:

    33da6e2fc870a6006c0e71407c64e52028e01154212d88cdc10876be244a9802

No scientific program was executed or imported during this review. Reading source and computing the two file hashes were the only relevant machine operations.

## Findings

No mathematical defect or mismatch with the frozen finite audit contract was found in the inspected implementation. This disposition authorizes no claim about runtime, successful execution, or the eventual output.

### Complete cycle assignment

`necklace_patterns` enumerates every nonnegative integer vector with sum (e/d)y_e=c, excluding only inadmissible divisibility or weights already exceeding c. Its recursive coordinate resetting preserves completeness.

`complete_assignment` groups target necklaces by least period and assigns multiplicities of all allowed patterns. A pattern exceeding the starting source capacity cannot occur even once, so its initial filter is safe. Pattern multiplicities range over all values permitted by the remaining target count and source capacities. For the final pattern, requiring its multiplicity to equal the number of remaining necklaces is exact.

The coordinatewise minimum pruning is necessary only: every remaining necklace consumes at least the smallest available pattern contribution in each source coordinate. It does not impose a simultaneous-achievability assumption and therefore cannot discard a feasible assignment. Failed-state memoization omits the accumulated certificate but retains all data affecting future feasibility: pattern index, target count and capacities. Group-level memoization likewise retains the complete remaining capacity vector.

The two positive shortcuts are the written sufficient constructions. The upper bound on c combines total cardinality with the exact requirement that each primitive target necklace consumes c distinct n-cycles. The independent `audit_certificate` checks every reported general assignment, including counts, divisibility, common preimage multiplicity and capacities. The statement that a negative result is exhaustive remains conditional on the program completing its finite search within the frozen execution budget.

### Integral lattice and quotient enumeration

Each Bezout column operation has determinant one. Column swaps and sign changes have determinant minus one. The inspected transformation therefore preserves the relation lattice, and the code additionally checks H=BQ and |det Q|=1. Processing rows from bottom to top preserves zeros already established below the diagonal. The final reductions yield positive upper-triangular H with the required residue bounds.

Bottom-up reduction by H gives the unique representative in the diagonal box. Reduction of multiplication columns followed by integer linear combination implements the same quotient map. In the one-active-coordinate shortcut, all other canonical coordinates vanish, the active generator has order equal to its diagonal modulus, and the map is multiplication by its reduced scalar. The general branch reconstructs and reduces all active coordinates.

The traversal visits each representative exactly once. Requiring each path to close at its own starting point rejects a noninjective tail or an overlap with an earlier cycle; together with complete coverage this certifies a permutation of the representative box. Each orbit length is bounded by and divides n. The enumerated cardinality and cycle census are compared against the separate determinant/Mobius path. No singular quotient enters this routine.

### Controls and tail onset

The singular zeta rows are explicitly reported INFINITE_QUOTIENT. The one-tick zeta readers and the no-reader longer finite zeta rows are checked separately. The de Bruijn four-cycle protects against an overbroad prohibition of all finite independent windows on rotations. The exposed J counts, primitive counts, binary n=2,3 existence, binary n=5 failure, and small ternary/pentit failures are asserted.

The sufficient-onset routine uses the exact frozen integer inequalities and the exact n0. Both all-n monotonicity premises are checked, as are the two consecutive-step ratio inequalities at the chosen onset. The subsequent thirteen-horizon determinant checks are correctly identified as finite audits of the analytical proof. Lucas stride comparisons use strict b<L_(2k), preserving the stated off-by-one boundary.

## Limitations

Static review cannot establish that the exhaustive search or representative enumeration finishes within 2400 seconds, that no Python/runtime defect occurs, or that the first-run output agrees with the separately frozen breaker. Those remain execution obligations. The frozen proof and preregistration were not edited by this review.
