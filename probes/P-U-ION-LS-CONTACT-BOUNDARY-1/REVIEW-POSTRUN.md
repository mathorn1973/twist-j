# Post-execution scientific scope and consistency review

2026-10-04. PUBLIC; NON-CANONICAL; L1.

**Disposition: ACCEPT the recorded finite audit and the restricted negative
conclusion supported by the analytical proof. Physical realization remains
NOT_PROVIDED; model error remains NOT_CALIBRATED.** No scientific or
scope blocker was found in the reviewed frozen candidate and actual output.
This disposition does not close the #1359 HOLD, promote the Canon, certify
the complete history, or report a second execution.

## Review role and method

The reviewer authored PROOF.md during preparation. This is therefore a
disclosed post-execution consistency and scope review, not a new independent
review of the reviewer's own proof. The separate implementation authorship
and independent pre-execution scientific review are documented in
REVIEW-PREREG.md. The expected mathematics and old history data were already
known; no blind discovery is claimed.

The reviewer read the accepted model, proof, preregistration, source
manifest, README, pre-execution review, both scientific programs, input
manifest and actual EXPECTED.txt. The earlier logical source interface had
also been read during preparation. No scientific program was imported or
executed in this review, and no predecessor dynamics were rerun. The only
new file written by this reviewer is this review.

Raw-byte hashing and local Git-object comparisons confirmed that all nine
accepted files agree with the immutable local pin
`88464d909304a02082c3bae8ec1156c7aec824b1` and with the coordinator's
PIN-READBACK record. All ten supporting/source entries agree with the
lengths and SHA-256 values in INPUTS.json. The manifest digest agrees with
the literal anchor in verify.py. There is no observed post-pin drift of
accepted scientific content.

The coordinator's PIN-READBACK and FORMAL-RUN records were inspected as
administrative evidence. They report public byte readback before execution
and an Ubuntu 22.04.5 LTS, x86_64, CPython 3.10.12 execution with exit code
zero and empty stderr. This reviewer did not independently revisit the
remote ref, observe the process launch, or establish current CI status.
Those are not additional claims of this review.

The reviewer independently checked the on-disk stdout identity:

```text
file: EXPECTED.txt
bytes: 936
lines: 69
sha256: 166826f72f5e61bc70dee1b447d55fa46b0c4a34a290d43bfb9c3f38cddd2754
```

It agrees with the execution record. Exit status, empty stderr and execution
timing are read from the coordinator's record, not inferred from the stdout
file alone. The later RUN.md/RESULT.md packaging and architecture checks
remain separate coordinator responsibilities.

## What the executed finite audit establishes

The actual output reports PASS and independent_audit=AGREE only after the
primary code's source checks, finite assertions and comparison with the
separately authored audit have completed. Static inspection confirms that
the status is emitted after those checks, with no swallowed assertion or
fallback success path.

The accepted programs inspect all 250 stored history rows and 50 contact
rows, including all 25 second contacts and the five |00> witness entries.
They verify the frozen target permutation, involution and its failure to
commute with swap; exact symbolic closed-phase/common-rotation identities;
the disjoint swapped readout effects; the source-history partitions; the
symbolic energy coefficients; and the different-dictionary boundary control.
The primary additionally certifies the operator inequality using an exact
real symmetric projector. All calculations are integer or rational; no
pulse angles are numerically sampled.

The corrected primary identity is
`Q4=2B-2B E41 B`, with `B=I+P`. Symmetry, `Q4^2=4Q4` and rank 14 certify
positivity of `Pplus-2 Pplus E41 Pplus`. Its symmetric vector attains 1/2
in the enlarged symmetry sector, without establishing reachability by the
specified LS pulses. The independent effect/orbit argument yields the same
bound by a different representation.

The recorded history counts are
`25,20,20,15,15,15,15,12,12,9`, with maximum fibre sizes
`1,2,2,2,2,2,2,4,4,4`. The particular four-history set {0,1} times {0,1}
is checked at n=9. The proof does not infer that this same set realizes the
earlier n=7 and n=8 maxima. Both pre-pin executable corrections described
in REVIEW-PREREG.md are present in the frozen code; no post-output repair
is needed or authorized by this review.

The energy coefficient vectors agree with the isolated endpoint expression
under common spectra and E0=0. They do not establish a measured spectrum,
laser consumption or available work after the first contact. Likewise, the
fourfold collision supports the dimension-four consequence only with the
fixed pure-code/data-remainder premises stated in PROOF.md; coarse reading
alone supplies only a fibre-capacity condition.

## What remains analytical, rather than numerically established

The finite audit is not a proof by sampling of all control sequences. The
unrestricted sequence conclusion follows from the analytical argument:
the normal diagonal force has a central two-time commutator; its first
Magnus term vanishes at a completed loop; its second term is
`-i K A A^dagger`; and the resulting data phase is invariant under port
interchange. Common rotations, common drift and remainder-only operations
preserve that endpoint commutation under finite composition. The proof's
positive-integer multiple periods contain the model's one-period primitive
as a special case.

The instantaneous Hamiltonian may lack the swap symmetry. Nothing in the
output licenses interleaving additional data operations inside an unfinished
loop or applying the closed-loop proof to the full experimentally available
control set.

For every actual history with a2=4, exact rank-one port entry gives
`|00><00| tensor sigma_h`, with arbitrary inherited sigma_h and arbitrary
correlations inside it. This factorization follows from purity; it is not a
fresh-auxiliary premise. Endpoint symmetry gives equal probabilities for
|41> and |14>, so the ordered target probability is at most one half.
The worst error over all histories is therefore at least one half.
Full-output or archive success cannot exceed this necessary port success.
Failed, leaked and discarded outcomes remain failures.

The conditional robust bound follows analytically from full-output trace
distance and the same success effect. It supplies no numerical delta_out,
no unqualified oscillator operator-norm estimate, and no experimentally
validated error domain. An approximate entry needs the separately stated
full-state term.

## Bounded final interpretation

The supported decision is exactly
`SYMMETRIC-ISOLATED-CONTACT-EXCLUDED-BELOW-1/2` for the declared class,
identical fixed port dictionaries, exact entry and real isolated post-C
endpoint. Different fixed dictionaries can represent the target as SWAP;
the checked example demonstrates a scope boundary, not its implementation.
Differential drift, asymmetric data/environment couplings, nonclosed
interleaved controls, or a combined U6*C endpoint are outside the exclusion.

No feasible full-history point is supplied. Neither the analytical proof
nor the finite output constructs preparation, the first contact, native
continuation, a fourteen-ion interaction model, all-mode closure, a finite
inherited work budget or archive protection. The imported quantum model and
its probability rule are not derived from J. These limits are accurately
reflected in the output's NOT_PROVIDED and NOT_CALIBRATED fields and must
remain attached to the result in subsequent reporting.
