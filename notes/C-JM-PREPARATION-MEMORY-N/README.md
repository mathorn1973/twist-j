# Preparation memory and the resultant-41 seam

**NON-CANONICAL, L1.** `C-JM-PREPARATION-MEMORY-N`. Candidate-T analytical
implications, candidate-C finite checks. Ownership: issue #1677.

## Answer

The same one-system density can arise from sources with different repeated
preparation laws. Redrawing each label independently retains the known exact
opposite-seam indistinguishability at all block lengths. Holding the same
label while supplying a block of fresh pure systems restores distinguishable
correlations: the known collision separates already at two outputs.

For every full bounded preparation class `B_Q`, there is an explicit positive
one-sided test on a finite held block, dark on every on-seam input and bright
on every off-seam input. It also works on arbitrary held-label mixtures.
The minimum block length in this exact-zero class has order `sqrt(Q)`;
at `Q=14112` the proved interval is `3 <= k_min <= 181`. Success probability
may be extremely small. No fixed finite block works for the unbounded exact
one-sided problem. This is NOT a sampling-complexity improvement over the
previous approximate pure-state readout result.

The source's retained choice is an essential resource. A redrawn mixture
using only on-seam labels can trigger the held-block test. A state-only
operation cannot recover the missing source correlations from the common
marginal. No universal cloning is supplied; repeated preparation from a
retained program and repeated measurement of one specimen are different.

## Contract

Explicit premises: the source lattice and index-41 seam, chosen trace metric,
reference coordinate, finite norm bound, preparation law, tensor composition
of distinct output systems, positive effects and Born comparison law.
None is silently upgraded to a native apparatus, physical occurrence or energy.
The mathematical preparation program is supplied, not derived from J or U.
The oriented-quadratic/readout-cost conversation candidates are not treated
as published or promoted. All needed source definitions are restated here.

## Files

- `PROOF.md`: self-contained contracts, derivations, sharp-order lower bound,
  boundary controls and retained-program lemma.
- `PREREG.md`, `verify.py`: first public pre-execution pin.
- `SECOND-AUDIT-PREREG.md`, `second_audit.py`: result-exposed second code/pin.
- `ACTUAL.txt`, `SECOND-ACTUAL.txt`, `RUN.md`: actual one-architecture evidence.
- `RESULT.md`, `PROMO-C-JM-PREPARATION-MEMORY-N.md`, `SHA256SUMS`: disposition.

Both audits use only Python's standard library. See RUN.md for replay.
Ordinary notes-only CI does not run them. No Canon, registry, frontier, gate,
workflow, or sealed probe has changed. No merge is authorized by this packet.
