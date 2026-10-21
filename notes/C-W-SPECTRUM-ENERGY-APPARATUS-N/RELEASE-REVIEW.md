# Result-exposed release intake review

NON-CANONICAL. Date: 2026-10-21. Review for public issue #1700.
This is a source-exposed analytical review by a separate subagent of the
release session. It is not a blind experiment or independent queue closure.

Verdict: ACCEPT WITH SCOPED EDITS for existence and correctness of the
specified model. The full proof chain was read, including the supplied
contact and finite-preparation inputs, both moving-reference versions,
the direct-integral apparatus and the symbolic programs. All 29 entries
of the original final manifest and all eight local freeze entries match.

The full free symbol factors into two one-walk symbols. The normal-resolvent
perturbation by the centered contact gives a genuine global gap, not merely
a gap at rest. Its width is acos(7/25)-2pi/5>0. The selected logarithm,
annular contour and exponential weight estimate establish an exponential
upper bound. The Cayley/arctangent estimate is an operator estimate; it
does not assume that every scalar Lipschitz function is operator Lipschitz.

For the battery, the exact direct integral over total energy handles point
and continuous system spectra. Full fibers contain the entire system space;
the unitary acts as the target V there and identity on edge fibers. The sine
preparation stays in full fibers, without postselection or normalization at
the boundary. The Fourier second moment pi^2/L^2 gives the stated upper
error bounds. Its symmetry cancels the first-order channel term. Exact
conservation and approximate implementation are distinct proved statements.

The moving-reference argument uses two actual copies of W. Its translation
conservation concerns circular total momentum; (P-Q)/2 is a local coordinate
near rest. Unbounded position is treated with a separate commutator/domain
bound, rather than inferred from trace distance. The finite preparation,
time average and kick scales make the remaining errors vanish in the
specified response limit. No bridge to the distinct relational-metric
Hamiltonian in #1695 is inferred.

Both unchanged exact scripts were replayed on Darwin arm64, Python 3.9.6.
Each exited zero with empty stderr and produced the 656-byte certificate
SHA-256 7bbf0e0e6546a79961f52fbc9de448b349c6d66fb79ef12b9a64c64f72579c48,
identical to both historical Linux x86_64 certificates. The formal Laurent
polynomial and coefficient checks are supplementary audits; the infinite
operator theorems rest on their analytical proofs. This is not a public
preregistration or a claim that ordinary notes CI reruns those scripts.

## Exclusions and corrections

- The quantitative lower bound a_D^2/[4(L+3h)^2] lacks its cited earlier proof
  in this package and is excluded from the fold.
- An exponential upper bound alone does not prove nonzero tails at every
  distance. Strict non-finite-range language is excluded without that proof.
- Only run_one.py and the primary script protect existing outputs; the
  direct independent script can overwrite one. Use fresh output paths.
- Local metadata consistency is not external confirmation of temporal
  priority or of the absence of earlier executions.
- The battery has finite capacity and infinite Hilbert dimension. A
  logarithm branch and a one-shot switching protocol are declared inputs.
  The optional autonomous generator repeats the interaction each period;
  it does not itself supply an internally stopping one-shot clock.

These exclusions leave the explicit positive construction intact. A different
possible decoder does not falsify the nominated one.

## Primary-source readback

The review opened Chiribella, Yang and Renner, arXiv:1908.10884v3,
https://arxiv.org/html/1908.10884v3, equations (12)-(15). Its finite-level
construction motivates the method; the supplied proof separately justifies
the direct-integral extension. The review also opened Kuramochi and Tajima,
arXiv:2208.13494v3, https://arxiv.org/html/2208.13494v3, Theorem 2, for the
qualitative exact-implementation boundary. Neither source is used to assert
the excluded quantitative constant or novelty of the general battery idea.
