# Diameter-two obstruction certified for both original sources

**NON-CANONICAL. L1. Conditional finite certificate; external acceptance pending.**
A. M. Thorn. 2026-10-26. Apache-2.0.
Reservation: [#1790](https://github.com/mathorn1973/twist-j/issues/1790).

Status: CERTIFIED_OBSTRUCTION

The first publicly pinned execution completed all 66 declared comparisons
with exit zero, empty stderr and integrity PASS. **Both original source
settings are CERTIFIED_OBSTRUCTION.** Of the fixed cases, 31 pass the
strict sufficient threshold and 35 are INCONCLUSIVE. Every case remains
in the unchanged [EXPECTED.txt](EXPECTED.txt); none was hidden or replaced.

## Complete disposition table

| Source | Witness power m | Certified exponents a | Inconclusive exponents a |
|---|---|---|---|
| Plus | 0 | None | 0 through 10 |
| Plus | 1 | 3 through 10 | 0 through 2 |
| Plus | 2 | 3 through 10 | 0 through 2 |
| Minus | 0 | None | 0 through 10 |
| Minus | 1 | 4 through 10 | 0 through 3 |
| Minus | 2 | 3 through 10 | 0 through 2 |

There are 16 passing plus cases and 15 passing minus cases. In particular,
the same predeclared member **m=1, a=4** certifies both original settings.
It uses the same common forbidden projection, source, energy and threshold.
Its dual-vector propagation radius is at most 11+2+4=17; the full declared
family was nevertheless executed through its maximum radius 25.

The original m=0,a=0 cases remain INCONCLUSIVE and reproduce both exact
witness norms and the full R10 from PR1789. The present success does not
revise either predecessor outcome. All m=0 cases are also inconclusive in
this larger family; the positive compressed witness update is essential
to the particular passing certificates reported here.

## Earned physical conclusion

For each original sign sigma separately, the printed X,N,B and sharp_R
values give nonnegative P=B*sharp_R and strictly positive N,X,d,e, where

    t=1/1800,
    d=X²-P-t²N,
    e=d²-4t²NP.

For example these four guards hold for the common m=1,a=4 member. The
prospectively proved equivalence gives

    (X-sqrt(P))/sqrt(N) > 1/1800.

Applying PROOF.md (D25)-(D28) and pi>3 therefore establishes

    ||H_tilde Vpsi_sigma - VQpsi_sigma|| > E0/1200,
    for sigma=+1 AND sigma=-1.

This holds for **every** comparator in the declared class: a sum of
terms whose physical support has diameter at most two in the original
integer lattice, with the stated source-action and matrix-element
convergence assumptions. Each term may act arbitrarily inside an interval
of three consecutive sites. The class allows fixed data-independent
ancillary readiness, including entanglement among ancillary sites.
Positivity, charge conservation and bounded coupling strength were not
needed. The obstruction thus also covers the smaller desired positive
charge-conserving class.

The bound is uniform over all 26 old-memory labels and their arbitrary
passive reference correlations. Even choosing a different local comparator
and fixed ancillary readiness separately for each original sign cannot
meet the stated tolerance for that sign. This is a necessary energy-action
obstruction on the actual sources, not merely a global operator-norm claim
or an inference that one unspecified input must fail.

## Why the stronger test succeeds

The preceding full-vector remainder allowed too much error in directions
irrelevant to a selected forbidden output. The present proof bounds the
error pairing against w_m=(F A² F)^m F p4(A)psi. Its positive Taylor
envelopes use the same source moments through C^10, and its weighted dual
vectors retain forbidden support. All sources and physical comparators
are unchanged. These are mathematical test vectors, not a physical source
preparation or a changed apparatus.

The 66 comparisons were declared before execution. Reporting one common
passing member is a readable consequence of that completed finite family;
the complete exact values and failures remain available for reconstruction.
No numerical root, fitted precision, parameter search or extra trial was
used to decide the published guards.

## Limits and next physical boundary

The result excludes diameter two and therefore its smaller subclasses
under the fixed bare encoding and nominated logarithmic energy. It does
not exclude a local discrete step, good time evolution alone, dressed
encodings, another declared energy or larger interaction diameter. It does
not identify a minimum sufficient diameter, nor construct a local physical
Hamiltonian. The separate compact apparatus keeps its own energy and is
not contradicted by this result.

For the unchanged original energy the next open geometric boundary is
diameter three and larger. A physical construction there must still meet
the original source-energy requirement and count its actual sites, strength,
ancillas and preparation. Native-law derivation, empirical units, thermal
readiness, terminal outcome selection and replenished indefinite operation
remain outside this certificate.

## Custody and acceptance

Prospective public pin: `b5ebcd6276d538710d3ff19534b67e46a04bda18`.
Verifier SHA-256:
`c637973a805bddbf38071d3e758416454ca7bd3821bd074d72d08640993c46ad`.
All three prospective files were publicly read back before execution and
remain unchanged. The first stdout is 28742 bytes and 381 lines, SHA-256
`33a03e3b6a194dde05bb9e132e05fde5244792cd4a3a36aaa0f3b4e102301fbd`.
[RUN.md](RUN.md) records the local run. The pull request records required
two-architecture reproduction after the actual logs are available.

Two other same-session agents checked the complete proof, final program
and preregistration before pinning. These checks are disclosed authoring
checks, not independent external scientific acceptance. All 14 proof
obligations remain available for external review. Only this probe directory
changes; Public Canon v105 remains the sole authority.
