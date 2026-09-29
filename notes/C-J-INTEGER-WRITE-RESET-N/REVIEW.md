# Exposed mathematical review

**NON-CANONICAL / L1 only.** Author: A. M. Thorn <thorn@twistj.com>.
Owner #1292. This is reasoning review, not independent discovery or a
scientific execution. No numerical sweep was run.

Three separate reviewers examined the exposed constructions and all five
final files. All returned mathematical PASS. The root author derived and
checked the final combined transaction. These are separate reasoning reviews
with shared exposure, not independent experimental replications.

| Review | Verified scope | Result |
| --- | --- | --- |
| A | Global write/hold/reset maps, source transfer, phase wrapping, zero records and exact stack | PASS |
| B | Sharp phase twenty, full dirty-state inverses, hidden-digit witness and absence of a supplied full counter | PASS |
| C | Affine index criterion, radix inverse, recurrence, 625^k capacity and physical-scope boundary | PASS |

The reviewers requested two wording corrections: use lowercase source flag
a, and call the compiled transaction a traversal of the program-phase cycle,
not a cycle of the full data state. Both were applied. The sharpness statement
now explicitly quantifies over positive integers h. Archive growth is also
explicitly distinguished from a derived physical time arrow.

## Issues found and resolved during derivation

- A copy gate retains the source. The final W instead exchanges phased
  residue digits and source/memory occupancy, vacating the source exactly.
- Zero payload needs an occupancy distinction. Source and memory flags are
  both explicit, and the integer stack uses a nonzero tag even for M=0.
- A reset branch that only pushes is not a full permutation. The matching
  ready-to-occupied pop branch is explicit; R is an involution, not idempotent.
- Phase-only readback cannot discard exact high digits. M=1 and M=J^20 at
  phase zero exhibit the loss; the archive preserves the full integer M.
- The affine append theorem needs unrestricted old archives. Restricting
  them to a sparse reachable subset can evade the unit-index argument.
- Surjectivity alone is not equivalent to exactly one message per coset;
  the theorem states bijectivity using distinct complete coset representatives.
- The radix comparison must retain its input quotient and distinguish a
  zero message from the end of a finite input word. It is not free reset.
- The autonomous program is an added controller and does not produce fresh
  occupied inputs or a physical occurrence law.

## Validation ceiling

Only exact written proofs and exposed review support the new candidate-T
statements. Repository policy, Canon/hash, ledger and gate checks are
administrative checks, not a finite scientific audit of the maps.

Local administrative validation passed: POLICY; CANON v94 with 474 claims;
LEDGER with 533 items, 981 dependencies, 474 evidence rows and 25 gates;
GATE CONTRACT with all 25 gates. The eventual PR workflow readback is recorded
in the owner issue rather than predicted in these source files.

No Canon/registry/frontier/gate, old probe, workflow or release is edited.
The native-window dyadic candidate is not a dependency. Neither the existing
native U nor the physical apparatus frontier is declared completed.
