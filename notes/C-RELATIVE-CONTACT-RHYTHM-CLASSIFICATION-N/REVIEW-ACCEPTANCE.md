# Acceptance of the author-confirmed mathematical review

**NON-CANONICAL / L1.** General derivations remain candidate-T; the finite
census remains candidate-C. This receipt creates no Canon status or new
computational gate.

On 2026-11-02 the author supplied a review of PR #1855 at exact commit
`9b9aa5eea52e18cc662a59df117cd2072e63e478` and explicitly instructed that it
be treated as confirmed and the PR formalities completed. This document
records that accepted report, rather than presenting the publication
session's own work as an independent review.

## Accepted mathematical findings

The supplied reviewer found no error affecting a claim and confirmed all
four points requested by the promotion dossier:

1. The first-return law `F^(1+4r)(2y)=2F(y)` has the four exact time/refusal
   pairs `(1,0), (5,4), (5,4), (9,8)`.
2. The even return states occur in precisely the lower cycle's order, so
   minimality of the lifted period holds also for fixed lower states.
3. The no-H case analysis is complete, and the stated witness first reaches
   H after exactly eight ticks.
4. The account normalization is exactly the canonical
   `Q(a)=q(a)=Tr(a*conjugate(a))/2`.

The reviewer explicitly disclosed prior knowledge of the results. This was
not a blind review. The author accepts the separate mathematical review;
same-session assistance used to process this receipt is not an additional
independent confirmation.

## One accepted correction

Equation (20) must bind its indices to the **four marked coefficients**:
`i,j,k in {0,1,2,3}`. The artificial fifth coefficient appended in equation
(1) is not an index of (20). For `a=1` and `i=0`, the left side and the
four-coefficient right side both equal 3; including the fifth coefficient
would make the right side 4.

That domain is now explicit in `PROOF.md`. The existing shell verifier
already uses `range(4)`, so its code, expected stdout, all input families,
and the conclusions are unchanged. The original proof and replay pin remain
available in Git; the hashes in `RUN.md` describe that original execution.
The current `SHA256SUMS` describes the clarified documents.

## Reported computational review and its provenance

The supplied review reports 20/20 checks passing on 1,030,861 tested states
at relative account `M<=64`, together with the X/Y witnesses. It also reports
an unchanged replay of this PR's `verify.py` with byte-identical stdout on
x86_64. That is the same scientific architecture as the original replay,
not a second architecture.

The report names a separate review script and its output, but their full
bytes and full hashes were not supplied in this acceptance message or found
in the accessible publication sources. Consequently this receipt attributes
those counts to the confirmed reviewer report; it does not claim that this
session reran or established custody of those additional files. They are not
added as a new executable evidence dependency of the present note.

The precise finite domain of that additional count is also not restated as
all of `O^3`: common translation preserves M, so `M<=64` alone admits
infinitely many absolute triples. A fixed sum or a declared choice of
translation representatives is needed to define a finite census. The
self-contained public census in this PR remains the explicitly fixed
`E=32,S=4` shell with 2,895 states.

## Scope retained when accepting the interpretation

The X/Y witness equates E, S, M, each local residue modulo `(1-j)`, and the
entire common-depth history. It does **not** equate every local observation:
the initial slot accounts are `(180,0,0)` for X and `(140,20,20)` for Y,
and the coefficient residues modulo 5 also differ. The accepted obstruction
is exactly the restricted reading stated in the proof.

The inequality `3P<=2M-5` bounds a period by an arithmetic account. It does
not identify that account with physical energy or establish a physical
frequency law. The contact-built marker, interval counter, retained record,
funded renewal and native-U bridge remain open at their declared scopes.

## Disposition

The author-confirmed mathematical review is accepted with the index-domain
clarification. The notes-only PR may complete its ordinary repository checks
and merge under the author's instruction. Merging it does not promote its
candidate claims or close the common-apparatus obligation. Any later public
fold and computation-grade promotion retain the requirements in the
promotion dossier.
