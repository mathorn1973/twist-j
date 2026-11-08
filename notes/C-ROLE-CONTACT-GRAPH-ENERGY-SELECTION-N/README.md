# Coupled translation, role-contact graph and energy selection

**PUBLIC / NON-CANONICAL / L1.** A. M. Thorn.
Claim [#1624](https://github.com/mathorn1973/twist-j/issues/1624).
Analytical successor to [#1621](https://github.com/mathorn1973/twist-j/pull/1621)
and [#1623](https://github.com/mathorn1973/twist-j/pull/1623).

## Main result

The existing canonical affine/CSUM coupling alphabet already reaches
the nominated contact endpoints. An explicit word of **39 original
diagonal-letter and ring-addition leaves** takes

\[
X_\rho=(\rho,\rho+(2,0),\rho)
\quad\longmapsto\quad
Y_\rho=(\rho,\rho+(1,1),\rho+(1,1))
\]

for every reference content rho on a fixed k=Az sector. It exactly
restores the complete reference and all endpoint controllers. This is
a constructive use of the canonical coupled alphabet, not an appeal
to connectivity alone.

The word is an order-five translation on the entire raw carrier. Its
first two endpoints have equal price in both source accounts, while
the full cycles have different prices:

| Macro boundary | 0 | 1 | 2 | 3 | 4 | Return |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Square star (kappa,eta)=(4,0) | 8 | 8 | 24 | 26 | 14 | 8 |
| Equal triangle (2,1) | 8 | 8 | 16 | 16 | 12 | 8 |

Thus this exact endpoint realization is not the supplied sparse
involution T0 and is not a complete conservative apparatus. The
mathematical full word, its inverse, the sign sector and its entire
account are explicit in [PROOF.md](PROOF.md), sections 1--4.

## The graph also determines the price constraints

For each rho, let A_j have only cell j shifted by u=(2,0), and let B_i
have both cells other than i shifted by w=(1,1). The six role contacts
T_ij, i!=j, exchange A_j and B_i. Their complete branch graph is the
six-cycle A1--B0--A2--B1--A0--B2--A1.

There are exactly 25 disjoint copies at fixed native counter and
controllers. The other 15475 content triples are fixed. The generated
group is diagonal S6: the same word acts on each reference fibre.
The two contacts T01,T10 in #1623 have disjoint supports, so their
energy equations do not themselves create a longer transport path.
Other exact contact words do circulate prepared source or receiver
patterns; they do not load arbitrary independent messages.

Now permit six independent positive coordinate prices: alpha_e for
magnitude one and beta_e for magnitude two on each of the three
cell-pair edges. The two content coordinates use the same prices.
If a_i is the sum of the alpha prices incident to i and y_i is half
the incident beta sum, each role conserves the account exactly when

\[
a_i=y_j.
\]

These equations are the same six-cycle. Any five of the six contacts
connect all its vertices and, after the source's common calibration,
force **alpha_e=1 and beta_e=2 on every pair**. Fewer than five leave
a positive calibrated family. A concrete four-contact family has
ratios 4,4/3,4/3 and the same calibration as the selected account.

| Declared price family | Sharp role requirement |
| --- | --- |
| The two parameters kappa,eta of #1623 | Its nominated two contacts |
| One common ratio, three free positive edge weights | Any three distinct roles |
| Six independent positive coordinate prices | Any five distinct roles |

The complete classification, positivity proof and counterfamily are in
PROOF.md, sections 5--8. The source's conditional (2,1) result remains
correct in its original family.

## What remains outside the selection theorem

Even all six contacts and the listed symmetries preserve a different
positive interaction account:

\[
E_{\rm disc}=2\,\#\{\{i,j\}:h_i\ne h_j\}.
\]

It has the same calibration 4 as the equal-triangle coordinate account,
but gives 4 instead of 8 on every active A/B state. It is a sum of
common whole-content pair prices, without additivity over the two
coordinates. Accordingly, this note selects within an explicit
reading family; it does not derive the physically complete family.

The implementation boundary is also precise. Common original letters
and whole-cell permutations preserve both all-pair magnitude counts
and cannot make the nominated transition. Adding CSUM gives the
positive endpoint word, but every fixed affine word remains unable
to implement the full 623-fixed-point contact on its 625-point
signal layer. At a fixed reference, no affine map conserving the
whole star (4,0) or triangle (2,1) account can perform the endpoint
transition either. The Canon's separate supplied nonlinear residual
architecture is named and preserved; its factor compiler has not
been transported to this three-cell law.

The macro-boundary bank changes are exact necessary balances. They
do not price CSUM's intermediate excursions outside the common
reference carrier, supply a bank transition, or derive a controller
schedule. Literal autonomous U, the declared coupled alphabet and
the supplied role-contact law remain distinct.

## Evidence and status

The immutable [CONTRACT.md](CONTRACT.md) and [SOURCES.md](SOURCES.md)
were published at `ecfb13823a43243dbdb09c5d3879d323dc2deea6` and
read back in full before final proof drafting. The derivations were
already exposed at that pin. No new scientific executable, import,
enumeration or numerical run is evidence for this work.

[REVIEW.md](REVIEW.md) records exact-file same-session analytical
review and its limits. [CHECKS.md](CHECKS.md) records administrative
and repository checks; delivery receipts bind the final public bytes
and required x86_64/aarch64 infrastructure CI.

No Canon release, registry change, native autonomous actuation,
independently selected physical energy, new-message supply, microscopic
bank or particle/Floquet conversion is claimed. The finite
m/arctan(m)>1 result retains its separate existing scope. This PR
remains a draft for review, with no merge or Canon promotion.
