# Review, corrections, and evidence disposition

**NON-CANONICAL L1 note.** This review summarizes the critique explicitly supplied by the author in this conversation; the separately mentioned `claude/` review files and nine-check script were not accessible here and are not silently represented as inspected sources.

## What the critique establishes or corrects

- The original statement “the same spatial triple, metrically” was too strong. For the fixed ramified real-field generator `sqrt(5)` the exact coefficient is **3**, a nonsquare in F5, so the comparison is a **similarity, not isometry**. `det(g5)=4`, `det(3g5)=3`.
- The original critique called the odd-unit case “indefinite.” Corrected: every single real-embedded form is **definite**, while the **two embedding signs differ** for odd unit exponent. Changing uniformizer to `phi*sqrt(5)=phi+2` makes the F5 coefficient 1 and swaps relative real signs.
- In the fully marked setup the scalar depends on the uniformizer `epsilon phi^n sqrt(5)` through `epsilon 3^(1-n)`; its nonsquare class under totally same-sign normalization is controlled by the norm of the real-field unit. This tradeoff is the item worth preserving.
- The raw unimodular wedge pairing `beta` is part of the statement. Rescaling to `beta/2` alters the square class. An A5-equivariant isomorphism has only scalar freedom because `End_A5(W5)=F5`.
- Reversing orientation does not repair the nonsquare class at `sqrt(5)`.
- Public `J-HODGE-HERM2-LOXODROME [T]` and `A4-RAMIFIED-HODGE-TRACEKERNEL [T]` are already sources. They are dependencies, not independent new theorems. `TRACEKERNEL-CURVATURE-FORCING [O]` stays open.

## Audit of supplied ZIP, not a public preregistration

The seven ZIP entries, their sizes and digests are recorded in `SOURCE-MANIFEST.md`. They were inspected as untrusted text before any execution; the file list contains no path traversal. The six hashes listed in the author's `SHA256SUMS` match the corresponding contents. The original script was executed in one local x86_64 environment and its stored stdout reproduced, but it is a **non-blind reproduction**.

The submitted `PREREG.md` was written after the four exemplar values and corrected sign language were already known. The original `verify.py` was changed after a preliminary wrong-indexing failure. It must not be used to imply a pre-registered scientific gate, and the older evidence is no stronger than the retrospectively described local candidate-C.

The reviewer identified weaknesses in the original seven-check script: checks 01-03 materially construct the marked carrier, but checks 04-07 mostly validate inserted formulas, sign parity assertions or print success, not the full actual first-order lattice forms. In particular the six-dimensional first-order identity was a comment rather than an executed matrix identity. That critique is accepted.

## What was independently reimplemented here

`verify.py` is a new exact standard-library reconstruction from the public A4 definitions (still result-exposed and therefore **not a blind breaker**). The ten labelled checks include: complete 6x6 Hodge identity, actual plus/minus first-order matrices and quotient comparison, real-place Sylvester definiteness for 30 uniformizers, A5 simultaneous centralizer, wedge-orientation and beta/2 controls, correct exterior-square induced J step (factor 2), the fixed symmetric-form linear constraints, and arithmetic modulo p².

During construction of this new verifier, an initially used quotient action `M_J` was found to be **the wrong type** for the exterior-square-induced `D`; the correct action is `Lambda^2 M_J` and includes the scalar factor 2 from `M_J ell=2ell mod5`. This is a local implementation correction made before the recorded accepted run. It was not a frozen scientific falsifier. No theorem or threshold was changed after a public preregistration because there was none.

The full group census `SL_3(F5) x {+/-I}` (reported order 744000), the rank-two degeneration and the general modulo-25 census are review context, not all re-proved as a complete census by this new program. The only newly audited fixed-form absence is the six-parameter linear-constraint no-go; the modulo-p² statement also has a written all-odd-prime argument.

## Editorial and status corrections

- One incubation ID: `C-J-HODGE-FIRSTORDER-BRIDGE-1`.
- Potential **future** registry stem: `J-HODGE-FIRSTORDER-BRIDGE`. No registry row is created now.
- Written statement: `candidate-T` (unpromoted argument); finite/exact local audit: at most `candidate-C` and one architecture.
- Source bundle's `PREREG.md` is explicitly retrospective, not a preregistration pin.
- Public `notes/` PR is not a formal probe. Running repository workflow tests does not automatically turn this note's local verification into a two-architecture scientific T gate.
- The parent model's physical L2/L6 claims, any native-U bridge, or completeness assertions are excluded.
