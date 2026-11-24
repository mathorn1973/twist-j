# Round 19. A sharper original slope bound and a separate spectral route

**NON-CANONICAL. No authority. No Canon status change.**

Candidate: **C-RH-SEMISTABLE-FRAME-N**, alias C-RH-BK-CONCENTRATION-N.
Session: **ChatGPT-Astra-Sol-20261124-R19**. Owner: A. M. Thorn.
Handoff: [issue 2070](https://github.com/mathorn1973/twist-j/issues/2070),
existing [draft PR 2071](https://github.com/mathorn1973/twist-j/pull/2071).

All new mathematical statements are **candidate-D** paper deductions
with their stated hypotheses. The uniform spectral estimate for the
actual multiplicity maps remains **O**. No new scientific computation,
Lean verification, external independent review or promotion was performed.

## 1. What this round actually closes

The finite-dimensional step used by the original proof can be sharpened
on its existing inputs. Centering both traces gives a smaller corank
bound for the span of images after a prescribed total source loss.
Matching it to the source's actual threshold spaces improves the
coefficient of the integrated logarithmic loss from four to two, and
improves the diagonal error coefficient. This deduction does not need
exact semistability or a new higher-moment estimate.

A separate sufficient certificate addresses the stronger all-subspace
problem. It compares the spectral gap of a double-commutator operator
with the spectral diameter of the summed image projections. When the
gap covers the diameter, every subspace has at most its proportional
image incidence inside that block. This can hold with a nontight frame.
The certificate is a finite positive-semidefinite test. It is strictly
stronger than semistability, even after arbitrary changes of target
metric, so it is not another equivalent form of the same criterion.

The opposition also gives arrangements with exactly the same summed
frame operator and hence all the same aggregate moments, but different
concentration defects. The missing information can instead be expressed
by a two-copy operator on the matrix space. Its actual period expansion
pairs the closed chains of round 18 and retains their relative additive
character. No estimate for the needed gap follows from merely writing
this expansion.

- [Finite certificate, proof and Gram-only construction](PROOF.md)
- [Original slope improvement and actual two-copy bridge](BRIDGE.md)
- [Current source audit and exact threshold normalization](SOURCE.md)
- [Counterexamples and internal opposition](OPPOSITION.md)

## 2. The target needed by the original proof

For maps $A_u:E_u\to F$, write $R=\sum_u\dim E_u$ and $D=\dim F$.
The earlier concentration question concerns

$$
 \epsilon(A)=\max_{W\le F}
   \left(\frac{\sum_u\dim A_u^{-1}W}{R}-\frac{\dim W}{D}\right).
$$

The source's actual frame argument has a more specific task. It retains
source spaces $E'_u$ with a small **total** discarded rank, and bounds
the codimension of $\sum_u A_uE'_u$. In the arithmetic application these
spaces come from the filtration by slopes. Their images lie in a target
threshold space. A bound for the missed target fraction then bounds the
fraction of low target slopes; integration bounds the mean slope.

Thus an exponentially small all-subspace defect was an optional stronger
simplification goal in our previous rounds. It is not a missing premise
of the original formally checked proof. The square-root sharp example
for arbitrary test spaces does not prevent a variance-order bound for
the codimension of the full surviving span.

This distinction is confirmed by the current `FrameLA1`, `thmF_place`,
`theoremFSharp_of` and `Frame_at` source interfaces. Robin Zhang's
preliminary note, Lemma 4.2 and Proposition 4.3, describes the same
rank-to-slope passage. The Rubinstein and Brox readings also keep an
explicit removed-rank budget. See SOURCE.md for their separate scopes.

## 3. The sharper span inequality

Assume $D,R>0$, $0\le e\le1/4$ and

$$
 \sum_u\|A_u^*A_u-I\|_{\rm HS}^2\le eR,
 \qquad
 \operatorname{tr}(S^2)\le(1+\eta)\frac{t^2}{D},
 \quad S=\sum_u A_uA_u^*,\quad t=\operatorname{tr}S,
 \quad \eta\ge0.
$$

These are the source's weighted-map hypotheses after multiplication by
the square roots of their positive coefficients. That normalization
does not change any image. Put

$$
 \delta=\frac{\sum_u\operatorname{codim}E'_u}{R},\qquad
 w=\frac{\operatorname{codim}(\sum_u A_uE'_u)}D,
 \qquad
 a=\min\left(1,\delta+\frac Rt\sqrt{e\delta(1-\delta)}\right).
$$

**Candidate-D.** Centering the trace on the discarded source directions
and on the missed target directions gives

$$
 w-\sqrt{\eta w(1-w)}\le a,
 \qquad
 w\le\frac{2a+\eta+\sqrt{\eta^2+4\eta a(1-a)}}{2(1+\eta)}.
 \tag{19.R1}
$$

At zero source loss, $w\le\eta/(1+\eta)$, a sharp variance-order
endpoint. A convenient affine consequence, for $\delta\le\varepsilon$,
is

$$
 \boxed{
 w\le\min\left(1,\frac{2\varepsilon+\eta+c(e)}{1+\eta}\right),
 \qquad c(e)=\frac{\sqrt e}{1-\sqrt e}\le2\sqrt e .}
 \tag{19.R2}
$$

The current `FrameLA1` conclusion is
$w\le\eta+4\varepsilon+4\sqrt e$.
The replacement (19.R2) is a deduction on the same matrix hypotheses.
It is the centered compression argument, with explicit constants and
quantifiers, not a new construction of the automorphic maps.

## 4. Its passage through the actual slope thresholds

The current source proves that its retained threshold spaces have
lost source share at most $u/(u+\tau)$. The rank denominator is already
the source rank after the initial ramified restriction. Its factor
$[K:\mathbb Q]$ cancels when converting arithmetic ranks to complex
dimensions. The raw slope threshold contains a factor two, but the
source counts the normalized slopes $2\lambda+c_K$ and integrates
with respect to $d\tau$. There is no further factor two in the integral.

Let $\delta_p<1$ bound the later good-row loss, let $s,u$ be the source
frame parameters with $u\ge0$, and retain its conditions $H>0$ and
$s-\mu_{\min,\mathrm{dual}}\le H$.
**Candidate-D.** Replacing only that corank envelope and keeping the
same layer-cake argument gives

$$
 \boxed{
 \mu_{\mathrm{dual}}\ge s-\log|\mathrm{Word}|
 -\frac{2u\log(1+H/u)+(\eta+c(e))H}
        {(1-\delta_p)(1+\eta)} .}
 \tag{19.R3}
$$

At $u=0$ the logarithmic term is interpreted as zero. The original
recorded interface has numerator
$4u\log(1+H/u)+(\eta+4\sqrt e)H$ and denominator $1-\delta_p$.
The new bound improves those constants and retains the original
$\log|\mathrm{Word}|$ loss. The existing sharp source branch also
permits the counterpart without that loss.

The error order has not changed: the polynomial $\eta H$ contribution
remains. The analytic and arithmetic suppliers of $e,\eta$, the heights
and the row loss remain inputs. This is a checked paper replacement
of one local inequality, not a changed Lean theorem, an updated final
parameter choice, or a separate proof of RH.

## 5. The algebraic certificate for the stronger problem

Let $H_u$ project onto the image of a map in one reduced target block.
For a test projection $X$, the exact principal-angle decomposition gives

$$
 \operatorname{tr}(XH_u)-\dim(\operatorname{ran}X\cap\operatorname{im}H_u)
 \ge\tfrac12\|[X,H_u]\|_{\rm HS}^2. \tag{19.R4}
$$

The left side is what a trace estimate overcounts. It is lost unless the
test subspace nearly preserves the individual images. Define

$$
 S=\sum_uH_u,\qquad
 \mathcal L(Y)=\tfrac12\sum_u[H_u,[H_u,Y]],\qquad
 \Delta=\lambda_{\max}(S)-\lambda_{\min}(S).
$$

**Candidate-D.** If the quadratic form of $\mathcal L$ on traceless
Hermitian matrices is at least $\gamma\|Y\|_{\rm HS}^2$ and
$\gamma\ge\Delta$, then no subspace exceeds its proportional share
of the total image rank. For $Y=X-xI$, its trace norm is twice its
squared Hilbert--Schmidt norm. The diameter therefore bounds the
centered trace by exactly the quantity paid by (19.R4).

This gives a finite certificate consisting of
$aI\preceq S\preceq bI$ and
$\mathcal L|_{\operatorname{tr}=0}\succeq(b-a)I$.
Four rational lines in a plane provide a strict nontight example in
PROOF.md. OPPOSITION.md supplies a different semistable four-line family
which fails the exact test in every target metric. Passing the test is
sufficient; failing it does not imply concentration.

For a reducible family, use the simple matrix blocks of the algebra
generated by the image projectors. If all tests pass, the defect is
exactly the kernel fraction plus positive central mass imbalance.
The refined central masses need a fresh bound. They are not the masses
already controlled for the coarser common Hecke and determinant algebra.
In the commuting obstruction the entire old defect reappears in those
central masses.

For the actual maps one can avoid inversion of small singular values.
The averaged diagonal bound controls the total Hilbert--Schmidt and
trace-norm errors between $A_uA_u^*$ and its image projection. BRIDGE.md
proves a direct certificate using those actual positive matrices. A
normalized gap at least twice their frame diameter, or the corresponding
condition after clipping with a small weighted trace tail, leaves only
the existing kernel and block errors plus $\sqrt e+e/2$ and the tail.
The uniform actual gap and tail estimates remain **O**.

## 6. What information would settle that stronger test?

The sum $S$ forgets part of the arrangement. Two planar families in
OPPOSITION.md have the same $S$ and all its moments, with defects
$t-1/2>0$ and zero. Thus higher aggregate moments alone do not
characterize the concentration defect.

The relevant operator acts on matrices:
$\Psi_B(Y)=\sum_uB_uYB_u$, with $B_u=A_uA_u^*$.
Its exact moment identity is

$$
 \operatorname{tr}_{\operatorname{End}F}(\Psi_B^\ell)
 =\sum_{u_1,\ldots,u_\ell}
   |\operatorname{tr}(B_{u_1}\cdots B_{u_\ell})|^2.
$$

The actual ordered traces are the closed Gram chains of round 18.
Pairing two chains leaves
$\chi_2(k_\circ)\overline{\chi_2(k'_\circ)}$.
The source's present single-edge pair estimates do not bound the
resulting restricted commutator gap. Moment bounds would also have to
separate the known zero modes. The owner's peripheral note on return
periods and shifted norms supplies no such estimate and was not audited
or used as an RH premise in this round.

This direction belongs to established spectral work on operator scaling
and expansion; [Kwok, Lau and Ramachandran's 2021 paper](https://cs.uwaterloo.ca/~lapchi/papers/spectral-scaling.pdf)
is a relevant primary reference. Its hypotheses are not automatically
those of the automorphic family. No historical novelty is claimed.

## 7. Current verification and custody

The [Lean FRO and Mathlib Initiative statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)
certifies the released RH statement and proof. [Andrew Sutherland's
verification record](https://math.mit.edu/~drew/grh/), updated 23 November
2026 at 23:45 UTC, records multiple kernel checks and comparisons of the
five headline statements. Our open simplification task does not alter
those results. This round did not rerun any of those checks.

The period realization and cycle expansion retain their mathematical
pin `40e56bab026552e089d7afcfeff08d2defb9c005`. A bounded current-source
comparison was made at `4d25b0edc80cbf28a7b82a9d491d95875b36e826`.
It located a corresponding absolute projector-diagonal estimate and
the exact frame and slope interfaces, including the threshold proof
used above. It does not establish complete equivalence between the
two source revisions. Brox was read at
`fd38313e5c7018c3c988ba20510e6b0b3bca0519`.

The PUBLIC authority basis remained
`ed3b1878d95825ab9473c16416c8db76cc152079`, Public Canon v116, and the
existing draft head was `e7a1bc2910330bf41222dbf689db789860e7e095`.
STATUS-first reading, policy and authority files, tag/content ancestry,
all five normative hashes, successful exact-main checks, all 394 remote
heads and current collisions were checked. The same issue was claimed
for R19 before authoring. No new candidate or competing lane was opened.

Two Astra workers developed and opposed the paper argument, a Sol worker
read the sources, and root checked the decisive source interfaces and
integrated the transfer. Both Astra workers independently checked the
constants; the developer also read the actual slope-threshold proof.
This is internal cross-review within one session. All earlier scientific
files and frozen computations remain unchanged. Delivery is confined to
this round and the parent index/handoff on the existing draft.
