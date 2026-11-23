# Round 13 source record and internal paper opposition

**NON-CANONICAL. No authority. No Canon status change.**

Candidate C-RH-SEMISTABLE-FRAME-N, alias C-RH-BK-CONCENTRATION-N.
Session ChatGPT-Astra-Sol-20261123-R13. Date: 2026-11-23.

## 1. Outcome and inherited hypotheses

**Candidate-D:** every genuine row constituent covered by round 11 is
cuspidal and occurs with multiplicity one. Chen-Zou's unconditional
near-equivalence decomposition assigns its elliptic Arthur parameter.
The exclusion of Satake adjacency at a suitable unramified split place
forces every Arthur SL2 length to be one. Their generic multiplicity
formula and cuspidality proposition then apply to the actual occurring
representation.

**Candidate-D:** the auxiliary smooth infinity vector in round 12 need
not belong to the finite row cut. Its evaluation through each original
row intertwiner already computes the original period pairing. The
remaining unknown is the rank of the global scalar forms with fixed
finite tests. An exact integer-column example has full visibility and
injective aggregate analysis but defect 1/12 on a mixed target line.

The new theorem retains the entire genuine-realization and parameter
hypotheses of [round 11](../round11/PROOF.md). It uses its proved strict
Satake annulus, not an independent assumption of Ramanujan or everywhere
temperedness. The general multiplicity-space formula of round 12 remains
valid; its specialization here has one-dimensional multiplicity spaces.

**O:** the full coefficient on the prescribed rational orbit for
positive r_S, and the total restricted rank of the selected finite
period tests on every target subspace. Neither is established by the
new multiplicity-one statement.

## 2. Primary sources actually checked

| Source | Checked location and use |
|---|---|
| Rui Chen and Jialiang Zou, *Arthur's multiplicity formula for even orthogonal and unitary groups*, JEMS 27 (2025), 4769-4843, DOI 10.4171/JEMS/1564 | [Publisher page](https://ems.press/journals/jems/articles/14298407) and [published full text](https://ems.press/content/serial-article-files/51452). Section 2, pp. 4772-4777, includes odd-dimensional Hermitian unitary groups, their pure inner forms and elliptic parameters. Theorem 2.1 and equation (2.4), p. 4777, give the actual almost-everywhere matching and the SL2 twist string. Theorem 2.6, p. 4780, explicitly makes the generic elliptic part multiplicity-free. Proposition 5.1, p. 4790, identifies cuspidal, discrete and full automorphic multiplicities under that same generic parameter hypothesis. |
| Kaletha-Minguez-Shin-White, *Endoscopic Classification of Representations: Inner Forms of Unitary Groups* | [arXiv:1409.3731](https://arxiv.org/pdf/1409.3731), Theorem 1.7.1 and its scope paragraph, p. 89, and Corollary 3.3.2, p. 151, were inspected. The full theorem in that version is starred and its unconditional generic case is specifically qualified. The new proof uses Chen-Zou's published theorems directly, so it does not assume the starred full statement. |
| J. S. Milne, *Class Field Theory*, version 4.03 | [Author's text](https://www.jmilne.org/math/CourseNotes/CFTc.pdf), Chapter VIII, Section 3, Theorem 3.1, printed p. 234, gives the Hasse norm theorem for cyclic extensions. The quadratic special case in TEST_SPACE is also derived from the conic and Hasse-Minkowski. All places are required. |
| Inherited source correspondence | The mathematical RH pin remains `40e56bab026552e089d7afcfeff08d2defb9c005`. The actual HH and all-gap/transfer hypotheses are documented in [round 11 source map](../round11/SOURCE_MAP.md). The fixed finite tests, RowsBij and the common infinity evaluations are documented in [round 12 source map](../round12/SOURCE_MAP.md). No live-source revision is substituted. |

The coordinator opened the primary sources used in the new deduction.
Sol and the Astra opponent independently checked the three Chen-Zou
statements and the split localization. These are applications of
published results and an explicit connecting argument, not a claim to
have re-proved the classification theorem.

## 3. Challenges and dispositions

| Challenge | Disposition |
|---|---|
| Does a generic GL transfer by itself establish the correct unitary Arthur parameter? | The proof avoids that inference. Chen-Zou Theorem 2.1 supplies the actual elliptic parameter with its conjugate-self-duality, parity and almost-everywhere matching. |
| Can a predetermined word prime fall in the exceptional set? | It could. The proof chooses an unramified split place outside the finite exceptional and ramification sets. Round 11 covers all spherical split places, so it covers this choice. |
| Is the twist ratio affected by normalization? | A block of length at least two contributes two nonzero Satake values with ratio q_v or q_v^(-1). A common character twist does not change that ratio. |
| Could other blocks cancel the offending pair? | Satake data are multisets with nonnegative multiplicities. An additional summand cannot remove the pair. |
| Are parity and distinctness being assumed? | They belong to the elliptic parameter supplied by Theorem 2.1. When all lengths are one, ellipticity implies pairwise distinct cuspidal factors. |
| Does generic parameter mean a globally Whittaker-generic row or everywhere tempered local factors? | Neither is inferred. Here it means trivial Arthur SL2. The source's real row may have its specified nongeneric orbit, and Ramanujan is not assumed. |
| Does the generic formula apply to the actual inner form? | The paper treats Hermitian unitary groups of both dimension parities and their pure inner forms. The source uses precisely a Hermitian unitary group. The argument does not import an even-orthogonal multiplicity-two phenomenon. |
| Does multiplicity at most one prove the occurring multiplicity equals one? | Yes: the representation under consideration already occurs in the discrete spectrum. Proposition 5.1 then makes its cuspidal multiplicity equal to that positive discrete multiplicity. |
| Is the resulting cuspidality only abstract? | Equality of cuspidal and discrete multiplicities puts the actual discrete isotypic copy in the cuspidal subspace. The row cut is inside it. |
| Must the auxiliary v* lie in HH? | It belongs to a different space, Sigma-infinity. The actual I_f realizes it automorphically for every original f. The period identity is still indexed by f in HH and retains x_u. No such membership is required. |
| Is the rank counterexample an actual arithmetic counterexample? | No. It refutes the proposed algebraic implication from visibility, aggregate injectivity and multiplicity-one labels. It is not asserted to satisfy every source frame/Hecke constraint or to occur among the actual P_u. |
| Does the norm-class example violate a local-global norm principle? | No. For the quadratic extension the all-place principle holds. The classes of round 12 are separated at an inert finite place, although all their real signs agree. Global period nonvanishing is another question. |
| Has equality ell_0=r_S been obtained? | No. Cuspidality now permits the first-occurrence theorem for every irreducible constituent contributing to HH, but it gives the established upper bound. A nonzero target coefficient implies equality; equality alone still does not specify the rational orbit. An arbitrary vector in HH may mix distinct constituents and has no constituent first-occurrence index. |

This was internal paper development and opposition in the same session.
It is not an external referee report, blind code confirmation or Lean
verification. The integer example is proved by its four possible target
dimensions, without a finite enumeration program.

## 4. Public basis and delivery boundary

PUBLIC main was freshly checked at
`ed3b1878d95825ab9473c16416c8db76cc152079`, the same authority verified
in round 12. STATUS was read first and still declares Public Canon v116.
POLICY and AGENTS were fetched at that exact commit; the prior CORE,
FRONTIER, tag/content ancestry, five normative hashes and successful
exact-main check receipts are unchanged because the authority commit
itself is unchanged. Their identifiers are recorded in
[round 12 SOURCE_MAP](../round12/SOURCE_MAP.md).

The full remote-head inventory, 100 recent open issues, registry and PR
conversation were checked. The source/type/multiplicity continuation was
claimed in issue #2070 before editing. The candidate keeps the existing
branch and draft PR #2071; the centered-frame item #2065/#2067 stays
separately owned.

Round 13 starts from public commit
`5436b03c09abdd867b7e6edb543fff95360b2a12`, tree
`415055eeb472db910e68b69e4054de40fda1365f`.
Only round13/ and the parent index/handoff change. Earlier scientific
files, contracts, code and first-run records are unchanged. All new
prose is original; third-party material is linked and not imported.
No computation was planned or run, so there is no new scientific
preregistration, verifier, candidate-C record or architecture claim.
Repository policy/canon checks are delivery integrity checks only.
