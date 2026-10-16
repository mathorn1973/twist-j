# General quadratic two-message readout

PUBLIC / NON-CANONICAL / L1. Author A. M. Thorn, Apache-2.0.
Owner Codex-20261016-quadratic-two-message; issue #1538.

The unrestricted quadratic question left open in PR #1536 has an explicit
affirmative answer, conditional on its established 550-point domain:

    P=A+2z, Q=(1+2B)D+3BC,
    decode(p,t)=BLANK if p=0, otherwise PRESENT(-p^2*t).

Here A=a+c, B=b+d, C=a-c-2, D=b-d-1, z=a+b+c+d+q+r over F5.
P is linear and Q quadratic. The inherited affine impossibility makes the
minimum maximum degree exactly two. PROOF.md gives the complete iff criterion,
the all-time proof, and the precise semantic (not common-raw-ready) scope.
REVIEW.md is an independently reasoned, formula-exposed mathematical review
inside the authoring session; it is not a new external audit of #1533/#1534.

The exact certificate is the displayed polynomial pair and the complete
25-entry decoder, compressed by its five first-coordinate cases. verify.py
checks all 550 points and all cross-label pairs. check_independent.py is a
separately authored original-coordinate scan using expanded polynomials;
the two sorted 550-row certificates must agree exactly. Neither imports nor
reruns the closed native-U audit. No search solver or exhaustive classification
of all quadratic pairs is needed for an affirmative existence result.

Run from repository root:

    python3 probes/P-U-QUADRATIC-TWO-MESSAGE-READOUT-1/verify.py

The initial/reset raw pair is (0,mu), not one common raw pair across all
preparations. Both messages are jointly prepared. No physical detector,
disjoint-sector transfer, fresh information, global coordinate bijection,
source clearing or Canon promotion is asserted.

Sources: [primary #1533](https://github.com/mathorn1973/twist-j/pull/1533),
[closed audit #1534](https://github.com/mathorn1973/twist-j/issues/1534),
[boundary #1536](https://github.com/mathorn1973/twist-j/pull/1536), and immutable
file pins in SOURCES.tsv. These sources remain unchanged.
