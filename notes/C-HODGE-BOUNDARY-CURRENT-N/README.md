# Boundary current, retained labels, and a complete arithmetic Hodge map

**C-HODGE-BOUNDARY-CURRENT-N. NON-CANONICAL. L1.**

Author of record: A. M. Thorn. Reservation:
[#1714](https://github.com/mathorn1973/twist-j/issues/1714).
This is the analytical successor to draft
[#1713](https://github.com/mathorn1973/twist-j/pull/1713), at the exact inputs
listed in [SOURCES.md](SOURCES.md).

**Current execution state: both exact programs are prepared and statically
reviewed, but unexecuted.** No accepted public execution pin or mathematical
program pass is claimed. See [RUN.md](RUN.md) for the resolved publication
attribution and the unchanged prospective execution rule. The analytical
arguments below are proof-derived candidate-T statements; they have not
acquired public Canon status. No candidate-C run result has been earned.
The author has now authorized the connector attribution recorded in RUN.md
for this draft; the complete accepted package must still be published and
read back before the first scientific execution.

## 1. The physical question becomes more restrictive

The predecessor found the golden boost factor in the positive part of one
marked pulse transfer. Its next question required the entire Hodge action and
its specified form to be transported by an explicit map. The present analysis
shows why adding more scalar phases or pulse words cannot complete that
particular route.

The source-side conserved quantity is the flux through a spatial cut. A
lossless two-amplitude transfer A, in fixed current-normalized coordinates,
satisfies

$$
A^\dagger\Sigma A=\Sigma,\qquad \Sigma=\operatorname{diag}(1,-1).
$$

Its complete Hermitian congruence therefore has a nonzero fixed vector:

$$
R_A(X)=AXA^\dagger,\qquad R_A(\Sigma^{-1})=\Sigma^{-1}.
$$

The marked Hodge target has polynomial

$$
\chi_{L_J}(z)=(z^2-3z+1)(z^2-\varphi z+1),
$$

and has no eigenvalue 1. Consequently no invertible intertwiner with the
complete four-coordinate boundary congruence exists. A metric equation cannot
repair a failure of the action equation.

This is a theorem for the entire fixed-current class U(1,1), including all
complex phases and finite products. The more precise classification is

$$
\chi_{R_A}(z)=(z-1)^2
\left[z^2-(|\operatorname{tr}A|^2-2)z+1\right].
$$

It permits a boost pair or a rotation pair, while retaining the two unit
eigenvalues. It cannot supply the simultaneous nontrivial boost and rotation
of the Hodge target. See [PROOF_CURRENT.md](PROOF_CURRENT.md), sections 2, 6--8.

## 2. This includes the complete pulse and the actual receiver

The proof derives the stationary spatial transfer from the full pulse period,
including its energy phase. With c=1/sqrt(5), s=2/sqrt(5),
lambda=exp[-i(E-beta)] and boundary data (a_x,u_x), it is

$$
A(\lambda)=\frac1{s^2}
\begin{pmatrix}
c^2-\lambda&c(1-\lambda^{-1})\\
c(1-\lambda)&c^2-\lambda^{-1}
\end{pmatrix}.
$$

For every unit-modulus lambda it has determinant one, preserves the same
current and reproduces the source dispersion. Thus the obstruction is not
merely a statement about an isolated coin or its positive polar factor.

The actual encoded receiver gives A(lambda) tensor J, where J exchanges all
26-by-26 pulse/memory label pairs. All old memory information remains in the
full carrier. The fixed receiver contributes only signs to joint coherences.

[PROOF_LABELS.md](PROOF_LABELS.md) strengthens the conclusion: for every
A tensor J^n with one fixed unitary involution J, **no four-dimensional
invariant linear subquotient of the whole joint Hermitian carrier** can carry
L_J. The entire spectrum is either real or of modulus one; the target needs
both nonunit real roots and nonreal unit roots. Changing the joint linear
reading, or using an occupied or entangled encoded memory, cannot create the
missing spectrum.

This does not classify the complete capture contact. Its object, token and
pulse arrangements supply additional coherent channels. Nor does it cover
arbitrary distinct receiver products, interferometric label histories or
changing context identifications.

## 3. The target itself now has an explicit full map

The separate arithmetic analysis supplies a positive result stronger than a
spectral match. It also makes its changed assumptions explicit.

Let F=Q(sqrt(5)) and K=Q(zeta_5)=F(zeta_10). Put

$$
A_H=\operatorname{diag}(\varphi\zeta_{10},\varphi^{-1}),
\qquad q_E=\frac{\sqrt5}{2}\,\beta_{E_J}.
$$

[PROOF_METRIC.md](PROOF_METRIC.md), sections 4--5, constructs an explicit
F-linear map I from Herm2(K/F) onto E_J satisfying both

$$
I(A_HXA_H^*)=L_JI(X),\qquad I^*q_E=-\det.
$$

The map is given on all four coordinates. If p1,p2,p3 are the first three
marked positive Hodge-projector columns, define

$$
v=p_1-p_3,\quad w=Lv,\quad
r=(L^2-\varphi L+1)p_1,
$$
$$
u_+=(L-\varphi^{-2})r,\quad u_-=(L-\varphi^2)r,
\quad k=\beta(u_+,u_-)=-5\varphi/4.
$$

For X with diagonal entries a,d and upper-right entry x+y zeta_10,

$$
I(X)=a u_+-\frac{d}{\sqrt5\,k}u_-+xv+yw.
$$

This is an arithmetic representation of the full target, not a derivation of
A_H from the pulse. It uses the CM field K instead of F(i) and the displayed
scale instead of the predecessor's fixed beta. The unchanged beta pulls back
to (2/sqrt(5)) times -det. Neither change can be hidden as a coordinate choice.

Two negative results explain why these distinctions matter. Over F(i), the
determinant square class excludes every scalar similarity with beta. Over K,
the seemingly natural normalization beta/sqrt(5) still fails: its compact
plane is (2/5) times the relative norm, and 2/5 is not a relative norm because
of its odd valuation at the inert prime over 2.

## 4. The residual comparison now respects the involution

The pulse lattice over R[i], R=Z[phi,1/2], reduces at sqrt(5) to the split
algebra F5 x F5, with conjugation exchanging its factors. Its complete
Hermitian reduction is all M2(F5), not an undeclared three-dimensional slice.
The honest reduced congruence is

$$
C(Y)=\overline B Y\overline B^T=-\operatorname{Ad}(\overline B)(Y).
$$

On the predecessor's unchanged traceless identification Psi it induces
-Phi. A different explicitly specified symmetric slice,
Psi_sym(v)=Psi(v) Omega^-1, induces Phi. Both are retained in the proof;
the minus sign is not an obstruction to every possible residual reading.

The trace pairing remains 3g5, while the determinant on either stated
three-coordinate slice is g5(v,v). Their normalizations are explicit.
Moreover the corrected CM field has a dual-number residue algebra and a
different degenerate standard Hermitian reduction. The field isometry does
not identify integral lattices or the reported saturated Hodge lattice.

## 5. The next source test

Further scalar phase or word searches inside the same fixed two-port class
cannot answer the original question positively. A useful successor must
derive an actual additional coherent channel or a physically fixed context
transport from the source law.

For a higher-channel fixed-current transfer, a surjective linear reading r
onto E_J must annihilate the fixed current vector: r(Sigma_m^-1)=0. This is
only a necessary condition. The reading must also carry the complete action,
the specified form and lattice, and preserve occupied-record semantics.
The extra relative phase must come from the source channels, not be inserted
from A_H.

A covariant alternative must specify the current at each context and its
source-derived transitions. If the same marked context returns after N
target steps, the transported current vector forces 10 to divide N, and must
lie in the compact plane. Recursively defining the identifications from the
desired L_J would not be a source explanation.

## 6. Evidence and present limits

The exact acceptance fixtures and failure rule are in [PREREG.md](PREREG.md).
`verify.py` and `break.py` use only standard-library exact arithmetic. They
were written separately; the breaker did not read the first implementation.
Both passed static inspection, but neither has been executed. Their hashes
and the concrete pending pin are recorded in [RUN.md](RUN.md).

Repository policy, Canon, ledger and gate checks passed, together with all
210 unit tests. The notes-only changed-path checks correctly report not
applicable: those repository checks do not execute the two scientific
programs and do not satisfy a two-architecture scientific gate.

These are candidate L1 mathematical statements. No physical spacetime,
contact-angle selection, original-U realization, public status promotion or
Canon edit follows. The complete analytical result and unresolved execution
state are summarized in [RESULT.md](RESULT.md).
