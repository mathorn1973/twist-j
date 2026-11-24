# Sources and review

NON-CANONICAL. No authority. L1 paper work. New deductions are candidate-D.

Owner A. M. Thorn, session `ChatGPT-Astra-Sol-20261124-Signed-Gaps`.
Public Canon v117 basis `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`.
The scoped [owner claim #2082](https://github.com/mathorn1973/twist-j/issues/2082)
was opened before repository edits.

## TWIST-J source ownership

The user supplied the gap-content argument and reported computations under
the conversation alias `C-J-SIGNED-RETURN-GAPS-1`. The original calculation
package was unavailable for this review. The reported counts `9816`, `102`
and `200` are unreproduced and supply no evidence for the paper deductions.

The individual-defect reading is prior non-canonical work under
[#2080](https://github.com/mathorn1973/twist-j/issues/2080) and
[#2081](https://github.com/mathorn1973/twist-j/pull/2081). The pinned reference
is the [individual-defect proof](https://github.com/mathorn1973/twist-j/blob/bddd14b4eb684f613db3ec51df56527eea2dd480/notes/C-J-TWO-PLACE-FROBENIUS-N/PROOF.md)
at `bddd14b4eb684f613db3ec51df56527eea2dd480`. Registered inputs retain their
existing scope, including `J-GOLDEN-BRIDGE [T]` for the cyclotomic and golden
unit identities and `J-RESIDUE-PERIOD [T]` for powers of `J` in quotients by
rational integer moduli. The present claim is about common return contents
and the resulting correlations. It claims no novelty for classical
Fibonacci and Lucas divisibility.

## External source pins and attribution

- Sahibzada Allahyar, *A finite-exceptional Fourier bound for four-cycles
  of rank-three Kloosterman correlations*, 27-page preprint, 22 November 2026.
  [Pinned PDF](https://github.com/sahibzada-allahyar/math/blob/98dd9c9b95b22913916f6be0934da25e0c1773df/preprint/kloosterman-fourier/finite_exceptional_fourier_bound.pdf).
  Git commit `98dd9c9b95b22913916f6be0934da25e0c1773df`, blob
  `ed4fa53d68927357b7f2541b484ee46b06c155b2`, PDF SHA-256
  `293d28a3c6be4c42ace6060d0d43ca1b43d7f3be24525b00a99787ddcae03fa1`.
- Allahyar's §1.1 credits the result and proof strategy to Proposition 3.1
  of *Kloosterman correlations with finitely many exceptional Fourier
  frequencies*, by GPT-6 Astra, prompted by Romyar Sharifi, dated 18 September
  2026. The companion is the third manuscript in Sharifi's
  [UCLA bundle](https://www.math.ucla.edu/~sharifi/AI/prime_gaps_182_expository_bundle.pdf),
  PDF SHA-256 `5362e977880af92a73a79b411a9c66daf0b93af4ec0ed6bec320090386f4b881`.
  Allahyar gives a corrected exposition, including a different route to
  characteristic-uniform base change and inclusion of isolated exceptional
  points in the repeated-index case. The
  [companion Lean repository](https://github.com/romyar1/prime-gaps-lean)
  states its Type III derivation in terms of common adic theory interfaces
  whose joint interpretation remains external.

## Source review of the Fourier argument

Allahyar's Theorem 1.1 concerns a particular four-cycle of normalized
rank-three Kloosterman correlations over prime fields. For sufficiently
large $p$ and nonzero unit parameters, the unnormalized two-variable
Fourier transform has an $O(p^3)$ bound except at a uniformly bounded
set in the distinct-row, distinct-column case. The exceptional bound is
$O(p^{7/2})$. With a repeated index the exceptional locus can be a
bounded-degree curve, with an additional $O(p^4)$ term at the origin.
The constants are uniform and are left unspecified in the preprint.
The proof uses characteristic $p>3$ and takes coefficient prime $\ell=2$.

The elementary argument in Proposition 5.7 (§5.6, pp. 18–19) was checked
conditional on the local phases of Corollary 5.4. Over
$k(z)$, with $k=\overline{\mathbb F}_p$ and $z$ transcendental, write

$$
\beta=z^{-1}\sum_{\gamma\in\Gamma}c_\gamma(\gamma-z)s_\gamma,
\qquad s_\gamma^2=\gamma-z.
$$

A shared root label can occur only at opposite entries, since a shared
label within a row or column would give repeated indices. Opposite
amplitudes have distinct squares, so the grouped coefficients remain
nonzero. The simple valuation at each $z=\gamma$ proves independence
of the corresponding square classes. In the multiquadratic basis, the
single-root coordinates force $\beta\ne0$ and a nonzero cross term
forces $\beta^2\notin k(z)$ when there is more than one root. A single
root gives $\beta^2=c_\gamma^2(\gamma-z)^3/z^2$.

Lemmas 6.2 and 6.4 (pp. 19–22) use this structure with other hypotheses.
Generic radial tameness at infinity and curve degree less than $p$
reduce curve supports to lines through the origin. The proof uses a tame
branch at a nonzero critical value of a generic projection and a
break-one direct summand from stationary phase. An origin line would
require $\beta^2=c^2/(v_1+v_2z)$ with nonzero constant $c$. The checked
phase algebra rules this out. For one root, evaluation at $z=\gamma\ne0$
after clearing denominators gives a contradiction. Remark 6.5 records
examples showing the role of the degree restriction and exact phase
shape. The local Fourier and vanishing-cycle inputs are attributed to
[Fu, Theorem 0.1(iii)](https://arxiv.org/abs/math/0702436v5) and
[Laumon, §§2.3–2.4](https://www.numdam.org/item/PMIHES_1987__65__131_0/).

Proposition 4.6, Lemma 4.8 and Proposition 4.10 (pp. 12–16) are the
uniformity route. The proof uses Illusie's tame base-change lemma for
the smooth family and its relative normal crossings divisor, together
with compactly supported base change. The rank-six sheaf is bounded on
a common open through the image of a map between cohomology sheaves of
two bounded-complexity derived complexes. See the precedent in the
[proof of Illusie, Proposition 3.4(3)](https://arxiv.org/abs/1604.07004).
[Sawin–Forey–Fresán–Kowalski, Theorem 6.23](https://javier.fresan.perso.math.cnrs.fr/conductors.pdf)
bounds the degree of the non-lisse locus. Its use on the plane and on
the curve components, with Bézout, bounds the number of exceptional
points in Lemma 7.1 once the separate support argument has shown that
the relevant support is zero-dimensional.

The review checked the elementary phase algebra, the stated source
hypotheses and the role of each named step. A full verification of the
advanced local and global sheaf arguments remains outside this review.
External material is cited by links. No scientific executable, numerical
search, or formal proof checker was run. This is same-session source
review. External independent or blind confirmation remains absent.

## Scope of the gcd comparison

In the Sharifi companion, §§9.1–9.2 use squarefree $s$ and
$G=\gcd(s,(m-m')(n-n'))$ to mark the primes where row or column residues
coincide. The prime Fourier theorem already supplies the local envelopes.
The squarefree expansion selects finite, curve and origin conditions,
with the latter two restricted to primes in $G$. Equation (9.4) follows
from those envelopes and Fourier completion. Section 10 then averages
the gcd factors by an elementary divisor estimate off the integer
diagonals.

The reusable comparison is the separation of local exceptional cases
from the later divisor count. An identity for common support does not
supply a local oscillation estimate. For example, take every matrix
entry to be $\sqrt p$ on the torus and zero outside it. Distinct indices
and the same pointwise size bound then allow a four-cycle transform of
$p^2(p-1)^2$ at the origin. The prime-field trace-function family and
its local hypotheses would need to be established for a transfer.
The characteristic-two comparison field and the nonreduced ramified
quotient in TWIST-J do not furnish that family.

## Internal paper review of this package

The development agent read the proposed identities and wrote the result
summary. A separate opposition agent read the complete README and all
seven sections of PROOF.md after they were written. The opponent checked
the signed-gcd formula, the residual factor two for incompatible signs,
primitivity at five, both gap-two domains, the direct L18 reduction, all
five gap-182 cases and their residue counts, and the two correlation
counterexamples. The only correction requested in the proof was to
distinguish periodicity on indices n >= 2 from eventual periodicity when
the unavailable marker also covers n = 1. The text also now states that
the selected Fibonacci-pair period is a period of Lucas numbers, without
equating their least periods.

Those wording corrections were applied. This is internal paper review
with shared context. It is not blind independent confirmation, formal
verification, or execution of the supplied unprovided checking package.
The resulting scope remains candidate-D, L1. The inherited repository
checks do not promote any of these mathematical statements.
