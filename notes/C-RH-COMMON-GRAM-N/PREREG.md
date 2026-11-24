# C-RH-COMMON-GRAM-N: centered frame and full-distribution comparison

NON-CANONICAL. No Canon authority. Action layer: NOT_APPLICABLE.

Owner: A. M. Thorn, session ChatGPT-Astra-Sol-20261123-RH-COMMON-GRAM.
Claim: https://github.com/mathorn1973/twist-j/issues/2065
Public basis: v116, `93c36089db57032a6cbca482ff62c95884567d0f`.
External basis: `leanprover-community/riemann-hypothesis` at
`40e56bab026552e089d7afcfeff08d2defb9c005`.

## Scope and chronology

This is proof-only incubation under `notes/`, not a formal public probe.
The algebraic derivation and source-reading discussions preceded this record.
No numerical experiment, exact finite scientific audit, or Lean compilation
has been run for this item. The record freezes the proposed mathematical
scope before any such computation; it does not claim that the theoretical
idea was blind or preregistered before it was conceived.

No verifier is registered or required for this proof-only note. Any later
computational audit must first freeze its own exact code and declared scope
in an additional prospective record. No computational outcome may be
attributed to this record alone.

## Frozen mathematical domain

Finite-dimensional complex inner-product spaces V_i and H, positive real
weights c_i, maps B_i: V_i -> H, positive total source dimension S, and
positive ambient target dimension D. The zero-dimensional target is handled
separately. Put K_i=c_i B_i* B_i, T=direct_sum K_i, Q=sum c_i B_i B_i*.
Assume

    sum ||K_i-I||_HS^2 <= e S,       0 <= e < 1,
    tr(Q^2) <= (1+eta) tr(Q)^2/D,    eta >= 0.

The application retains the original stronger assumption e <= 1/4.
Source truncations are arbitrary orthogonal subspaces inside each V_i,
not just deletion of whole labels. Let r be their aggregate discarded
dimension fraction, z the ambient missing-image dimension fraction, and p
the fraction of the trace carried by discarded source directions.

The proposed centered bounds are

    (1-e)(p-r)^2 <= e r(1-r),
    (z-b)^2 <= eta z(1-z),  0 <= b <= p,

where b is the trace fraction on the missing target subspace.

Define, for 0 <= r,p <= 1,

    g_e(r) = min(1, r + sqrt(e*r*(1-r)/(1-e))),
    f_eta(p) = (2*p+eta+sqrt(eta^2+4*eta*p*(1-p)))/(2*(1+eta)),
    Phi(r) = min(1, f_eta(g_e(r))/(1-delta)),  0 <= delta < 1.

The projected missing fraction is at most Phi(r). The projection keeps at
least a fraction 1-delta of the ambient target dimensions.

## Frozen slope claim

Keep exactly the integral maps, lattice metrics, heights, field embeddings,
and hypotheses of the pinned `TheoremFSharp`. Let a be its rank-weighted
adjusted source slopes and b its target slopes, with

    E a >= s,  a <= s+U,  b >= s-H,  U,H >= 0.

The proposed replacement comparison is

    s-mu(C) <= (H+U)*Phi(U/(H+U)) - U,   H+U > 0.

If H=U=0, the loss is at most zero. The important test case e=eta=delta=0
must give loss zero for every U,H, not a surviving spread penalty.

## Systematics and source obligations

1. T is the block-diagonal source operator. It is not the full Gram operator
   of the concatenated maps; redundant families are admitted.
2. The source trace normalizes by S, the target by D. These dimensions need
   not agree. All discarded dimensions are counted before applying B_i.
3. Apply the frame result to the original full rows kappa + kappa_1, then
   use the original row projection. No change of the integer lattice,
   its degree, saturation, denominator, or metric is allowed.
4. The full-distribution argument uses thresholds throughout [s-H,s+U].
   The original `hMle`, exact threshold counts, and projection argument
   must remain valid there, including negative tau=s-threshold.
5. Count slopes strictly below the threshold. Equality affects finitely
   many integration endpoints only. All integrals are finite sums over
   intervals on which the empirical distribution functions are constant.
6. Preserve the realification factors 2 and [K:Q] in the source-to-slope
   correspondence. Do not add or silently omit log(card I).
7. Distinguish the original theorem, external working expositions, this
   paper derivation, formal Lean verification, and computation receipts.

## Falsifiers and limits

Any exact admitted finite-dimensional example violating either centered
bound, the monotonicity/concavity needed for the transfer, or the final
comparison falsifies the respective claim. A missing all-threshold source
identity blocks application to TheoremFSharp even if the abstract lemma is
true. A normalization or source-byte mismatch is an integrity stop.

The proposed uniform positive least-eigenvalue shortcut is to be tested
against the abstract hypotheses, and a counterexample is to be preserved.
Failure of that stronger shortcut does not falsify a corank theorem.

No claim is made about new global RH/GRH exponents, construction of theta
kernels, arithmetic existence or uniform windows, TWIST-J augmentation,
Hecke-mode identification, physical predictions, or any L1-L6 lift.
The source method already contains Hilbert-Schmidt estimates; no priority
claim is made for those classical inequalities.

## Deliverable and status rule

Produce a self-contained English proof, a pinned source correspondence,
independent written reviews with exposure declared, and
`PROMO-C-RH-COMMON-GRAM-N.md`. Record at most candidate-T, candidate-D, or
candidate-C. No canonical status changes are part of this item.
Exact source and document hashes are administrative integrity checks,
not numerical scientific evidence or a second-architecture receipt.
