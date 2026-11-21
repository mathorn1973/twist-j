# Positive-weight cut twist and the uniform-source response

**PUBLIC, NON-CANONICAL. Written proof candidate; separate review pending.**

- Author: A. M. Thorn, drafted with an AI agent session.
- Owner: #1217, primal-cut-twist-score-20260927.
- Date: 27 September 2026.
- Basis: Public Canon v92; public main `2294a75656ea10eeef2e11e04ac31f5d57ffdd8d`.
- Scope: the same finite four-dimensional fixed-weight model as #1208 and
  #1216. No physical, thermodynamic, or Canon status is promoted.

This note proves an exact representation of the remaining cut derivative
using a strictly positive primal measure, and an exact first-order bridge
from a localized seam source to a uniformly distributed source. It does
not prove a positive thermodynamic floor. It also corrects a possible
misreading of the Fisher reduction: a uniform floor for H is not, from
those identities alone, equivalent to a uniform floor for the unweighted
sum of the two squared twist derivatives.

No scientific verifier execution, computational gate, numerical phase
estimate, or candidate-C result is part of this item. The evidence here is
the written argument and symbolic controls below.

## 1. Fixed model, orientations, and source partition function

Let L be even and L >= 4. Work on the periodic cubical lattice
K_L = (Z/LZ)^4, with positively labelled links and plaquettes. Coordinate
0 is the transfer direction; fix spatial coordinate i = 1. The argument
applies to the other spatial directions by relabelling.

Set

\[
\zeta=e^{2\pi i/5},\qquad \vartheta=2\pi/5,\qquad
w(u)=2+2\cos u.
\]

For a real or complex plaquette cochain B define the finite entire function

\[
\mathcal Z_L(B)
=\sum_{a\in C^1(K_L;\mathbb F_5)}
 \prod_p w\bigl(\vartheta(da)_p+B_p\bigr).                 \tag{1}
\]

The choice of integer representative of (da)_p is irrelevant by 2 pi
periodicity. At B = 0 this is exactly the original link measure:

\[
w(\vartheta f)=W(f)
=\bigl(4,\varphi^2,\varphi^{-2},\varphi^{-2},\varphi^2\bigr)_f.
                                                                    \tag{2}
\]

No coupling, local weight, lattice dimension, or volume prescription has
been changed. An external source is not a replacement model.

Expanding each factor in (1) and summing each link variable gives

\[
\mathcal Z_L(B)
=5^{|E(K_L)|}
 \sum_{\substack{n\in\{0,\pm1\}^{P(K_L)}\\
                  \partial n=0\pmod5}}
 2^{N_0(n)}e^{i\langle n,B\rangle}.                       \tag{3}
\]

Here N_0(n) counts zero plaquettes. Thus the normalized surface law is
exactly proportional to 2^{-supp(n)}, equivalently to 2^{N_0(n)}. All
summands in its unsourced partition function are nonnegative.

The temporal plaquette convention is
(da)_{0i}(t,x)=a_i(t+1,x)-a_i(t,x)-(d_i a_0)(t,x).
With the Fourier convention of the finite transfer construction in
PR #1104, the temporal character n_{0i}(t,x) is the slice label r_t(x,i).
Expanding the transfer kernels produces the same positive periodic path
law used in #1208, equation (17). In particular its one-cut flux is the
F below, not a differently normalized observable.

## 2. The discrete seam is a positive primal twist

For t,s in Z/LZ, let Sigma_{t,s} be the 01 plaquette cochain which equals
one when x_0=t and x_1=s, and zero elsewhere. Each sheet has L^2
plaquettes. It is a cocycle, and any two such sheets differ by the
coboundary of an integer link cochain. For example their translation in
coordinate 0 is implemented by a periodic step function on 1-links;
translation in coordinate 1 is implemented on 0-links.

Write Sigma = Sigma_{0,0} and

\[
F=\langle n,\Sigma\rangle,
\qquad \theta_k=k\vartheta.
\]

The coboundary observation and partial n = 0 mod 5 imply

\[
\langle n,\Sigma_{t,s}\rangle\equiv F\pmod5.               \tag{4}
\]

Equation (3) gives the exact characteristic-function identity

\[
\Psi_L(\theta)
:=\frac{\mathcal Z_L(\theta\Sigma)}{\mathcal Z_L(0)}
=\mathbb E_{\nu_L}e^{i\theta F}.                          \tag{5}
\]

In particular

\[
\rho_{L,k}:=\Psi_L(\theta_k)=\Phi_k(0),\qquad k=1,2.        \tag{6}
\]

At theta_k, every factor of (1) is one of the five strictly positive
values (2). Hence

\[
\boxed{0<\rho_{L,k}\le1.}                                \tag{7}
\]

Strict positivity uses the actual primal weight. The upper bound follows
from the absolute value of the normalized character in (5). Charge
conjugation makes rho real and pairs k with 5-k.

Define the genuine positive probability measure

\[
\mu_L^{(k)}(a)
=\frac{\prod_p w(\vartheta(da)_p+\theta_k\Sigma_p)}
       {\mathcal Z_L(\theta_k\Sigma)}.                    \tag{8}
\]

This is a sum over all link fields with a prescribed external cocycle.
It is not the sector-filtered sampling law of the earlier orientation
simulations, and it is not obtained by dropping any current configurations.

A finite but nonuniform bound follows immediately from (2):

\[
\left(\frac{\varphi^{-2}}4\right)^{L^2}
\le\rho_{L,k}\le1.                                      \tag{9}
\]

Indeed the ratio of the twisted and untwisted factors is at least
phi^{-2}/4 on each of the L^2 affected plaquettes. This bound is not a
nonzero thermodynamic floor.

## 3. Exact first derivative and its sign

Put

\[
X_{L,k,p}(a)
=\tan\!\left(\frac{\vartheta(da)_p+\theta_k\Sigma_p}{2}\right),
\qquad
D_{L,k}
=\mathbb E_{\mu_L^{(k)}}\sum_{p\in\Sigma}X_{L,k,p}.        \tag{10}
\]

These are real, finite quantities: no angle in (10) is an odd multiple
of pi. Since w'(u)/w(u)=-tan(u/2), differentiation of the finite sum gives

\[
\left.\frac{d}{d\theta}\log\mathcal Z_L(\theta\Sigma)
\right|_{\theta=\theta_k}=-D_{L,k}.                       \tag{11}
\]

Charge conjugation gives E F = 0. Consequently the normalized real-source
quantity of #1216 obeys

\[
\Phi_k(h)
=\frac{\mathcal Z_L((\theta_k-ih)\Sigma)}
       {\mathcal Z_L(-ih\Sigma)},
\qquad
C_{L,k}:=\Phi_k'(0)=\mathbb E[F e^{i\theta_k F}].          \tag{12}
\]

The derivative of (5) is i C_{L,k}. Combining this with (11) proves

\[
\boxed{C_{L,k}=i\rho_{L,k}D_{L,k}.}                        \tag{13}
\]

The factor i and the sign in (13) are fixed by (3) and (11); no helicity
modulus convention is imported. Reversing the orientation of F changes the
corresponding signs but not the squared response.

Thus both the partition ratio and the expectation needed for the original
complex character derivative have an exact positive-weight primal
representation. Positivity of the measure does NOT make D_{L,k} positive:
the local score has both signs.

## 4. Exact bridge to a uniform source

Let U_{01} be one on every positively oriented 01 plaquette and zero
elsewhere. Define, for real s near zero,

\[
\mathcal F_{L,k}(s)
=-\log\frac{\mathcal Z_L(\theta_k\Sigma+sL^{-2}U_{01})}
                 {\mathcal Z_L(0)}.                     \tag{14}
\]

This is a real smooth function near zero, since every factor at zero is
strictly positive. Its value is the discrete twist free-energy cost:

\[
\mathcal F_{L,k}(0)=-\log\rho_{L,k}\ge0.                  \tag{15}
\]

We claim the exact first-order identity

\[
\boxed{
\mathcal F'_{L,k}(0)
=L^{-2}\mathbb E_{\mu_L^{(k)}}\sum_{p\parallel01}X_{L,k,p}
=D_{L,k}.
}                                                        \tag{16}
\]

Proof. The finite link sum has the exact discrete source invariance

\[
\mathcal Z_L(B+\vartheta\,d\lambda)=\mathcal Z_L(B)         \tag{17}
\]

for any integer link cochain lambda, by a change of the F_5 link variables.
For a translated sheet Sigma_j, the background theta_k(Sigma_j-Sigma)
is such a discrete coboundary. Therefore, for all sufficiently small real
epsilon,

\[
\mathcal Z_L(\theta_k\Sigma+\epsilon\Sigma_j)
=\mathcal Z_L(\theta_k\Sigma_j+\epsilon\Sigma_j)
=\mathcal Z_L(\theta_k\Sigma+\epsilon\Sigma).              \tag{18}
\]

The first equality uses (17); the second uses lattice translation. Hence
all L^2 translated-sheet first derivatives, evaluated at the same
background theta_k Sigma, agree. Since the sheets partition the 01
plaquettes and

\[
L^{-2}U_{01}=L^{-2}\sum_{t,s}\Sigma_{t,s},
\]

linearity of the first directional derivative proves (16).

This argument does not distribute a discrete twist by an assumed
continuous gauge transformation. It proves equality of FIRST derivatives.
It does not assert equality of the nonlinear localized-source and
uniform-source functions; mixed higher derivatives are additional data.
The factor L^{-2} is essential.

Combining (13), (15), and (16),

\[
\boxed{
\Phi_k'(0)
=i e^{-\mathcal F_{L,k}(0)}\mathcal F'_{L,k}(0).
}                                                        \tag{19}
\]

## 5. Consequence for the sufficient P1 route

Let

\[
\mathcal D_L=|C_{L,1}|^2+|C_{L,2}|^2.
\]

At the candidate scope of #1213 and #1216, their existing chain gives

\[
\boxed{
\Delta_L(q)\ge H_L\ge\frac45
\sum_{k=1}^2
 e^{-2\mathcal F_{L,k}(0)}[\mathcal F'_{L,k}(0)]^2
}                                                        \tag{20}
\]

for every allowed nonzero q. The present note establishes the new
representation of the right-hand side, not the independent premises of
those earlier candidate notes.

For example, for one fixed k, the following two estimates would suffice:

\[
\mathcal F_{L,k}(0)\le B,
\qquad |\mathcal F'_{L,k}(0)|\ge s_*>0                    \tag{21}
\]

uniformly for large even L. The one-mode inequality H_L >= |C_{L,k}|^2
from #1216 then gives the slightly sharper conclusion

\[
\boxed{H_L\ge e^{-2B}s_*^2.}                             \tag{22}
\]

The same statement permits a choice k=k_L if both constants are uniform.
Neither estimate in (21) is established here. In particular (9) gives
only B growing like L^2, not a fixed B.

A controlled limiting argument for (14) must control its first derivative,
not just its value. Pointwise convergence of partition ratios is not such
an argument. Neither a Maxwell effective action nor C^1 convergence to one
is assumed in this proof.

## 6. A fixed-model upper bound and a necessary free-energy test

The five possible scores in (10) satisfy

\[
|X_{L,k,p}|\le\tan(2\pi/5)=\sqrt{5+2\sqrt5}.
\]

There are L^2 seam plaquettes, so (13) gives the evaluated finite bound

\[
\boxed{
|C_{L,k}|\le L^2\sqrt{5+2\sqrt5}\,\rho_{L,k},
\qquad
\mathcal D_L\le(5+2\sqrt5)L^4(\rho_{L,1}^2+\rho_{L,2}^2).
}                                                        \tag{23}
\]

For a putative floor mathcal D_L >= d_0 > 0, at least one twist must
therefore satisfy

\[
\rho_{L,k}\ge
\sqrt{\frac{d_0}{2(5+2\sqrt5)}}L^{-2}.
\]

Equivalently, the cheaper of the two twist costs must be at most
2 log L + O(1). A bounded cost is sufficient only together with a response
estimate, while a cost above this logarithmic scale for BOTH modes would
rule out this particular route.

There is also an H bound in that latter regime. Fourier inversion and
charge conjugation give

\[
p_a=\frac15\left[1+2\rho_{L,1}\cos(2\pi a/5)
                       +2\rho_{L,2}\cos(4\pi a/5)\right]. \tag{24}
\]

Writing m_a=E[F 1_{F mod 5=a}], Parseval gives

\[
\sum_a m_a^2=\frac25\mathcal D_L,
\qquad H_L=\sum_a\frac{m_a^2}{p_a}.                       \tag{25}
\]

If 2(rho_{L,1}+rho_{L,2}) < 1, equations (23)-(25) imply

\[
\boxed{
H_L\le
\frac{2(5+2\sqrt5)L^4(\rho_{L,1}^2+\rho_{L,2}^2)}
     {1-2(\rho_{L,1}+\rho_{L,2})}.
}                                                        \tag{26}
\]

In particular, if BOTH twist costs were at least (2+epsilon) log L for
some fixed epsilon > 0 and all large even L, then H_L and mathcal D_L
would tend to zero. This is a conditional exclusion test, NOT a claimed
property of the four-dimensional fixed model. It would invalidate the
cut-Fisher sufficient route, not by itself disprove P1: the preceding
inequalities are one-sided lower bounds for Delta.

## 7. Correction: H and the two-derivative floor are not automatically equivalent

For p_min = min_a p_a > 0, (25) and #1216 give

\[
\frac45\mathcal D_L\le H_L
\le\frac{2}{5p_{\min}}\mathcal D_L.                       \tag{27}
\]

A uniform lower bound on p_min makes the two nonvanishing criteria
equivalent. Positivity of every p_a separately at every finite L does not.

Here is a fully symbolic counterexample to the unsupported logical
converse. It is NOT the fixed-model Gibbs distribution.

Choose M >= 6 with M = 1 mod 5 and set

\[
\Pr(F=M)=\Pr(F=-M)=\frac1{2M^2},
\quad
\Pr(F=2)=\Pr(F=-2)=\frac1{2M^4},
\quad
\Pr(F=0)=1-M^{-2}-M^{-4}.
\]

All five residues have positive probability and charge conjugation holds.
Their conditional means give

\[
\boxed{
H=1+\frac4{M^4},\qquad
\mathcal D=\frac5{4M^2}+\frac5{M^8}\longrightarrow0.
}                                                        \tag{28}
\]

In detail, m_1=1/(2M), m_2=1/M^4, and the paired means have the opposite
signs. Even the characteristic function is strictly positive for every
real angle: it is at least 1-2/M^2-2/M^4 > 0. Thus the positivity in (7)
alone cannot repair the converse.

The size constraint can be respected along even L by taking the largest
M <= L^2 congruent to one modulo five. Its flux values can be represented
inside the actual ternary slice carrier by M or two disjoint oriented
coordinate loops. The probabilities just assigned to those representatives
are synthetic, not the transfer weights. This distinction is essential.

The valid conclusion of #1216 survives unchanged: a positive two-derivative
floor is SUFFICIENT for a positive H floor and hence for its P1 route.
The unproved converse should not be used to discard the potentially
broader H route.

## 8. Dimension control: bounded twist cost alone is insufficient

This paragraph deliberately concerns a TWO-dimensional torus, not the
four-dimensional target. It is an exactly solvable control using the same
five local weights (2).

In two dimensions, adjacent surface plaquette labels must agree modulo
five. Since each is in {0,+1,-1}, they agree as integers. Thus the only
surface configurations have constant labels 0,+1,-1. For area A=L^2 the
source-dependent partition factor is exactly

\[
\mathfrak Z_A(\theta)=2^A+2\cos\theta.
\]

Consequently

\[
\rho_{A,k}=\frac{2^A+2\cos\theta_k}{2^A+2}\longrightarrow1,
\qquad
D_{A,k}=\frac{2\sin\theta_k}{2^A+2\cos\theta_k}
\longrightarrow0,
\]

and

\[
C_{A,k}=\frac{2i\sin\theta_k}{2^A+2}\longrightarrow0.
\]

The twist cost tends to zero while the derivative also tends to zero.
Strict positivity of the actual local weight and bounded twist cost do
not, as a general argument, supply the missing response estimate. This is
not a four-dimensional counterexample and does not determine its phase.

## 9. Remaining fixed-model theorem and review boundary

The work required for this sufficient route is now explicitly a statement
about the positive measures (8) and uniform-source free energies (14):

\[
\liminf_{L\to\infty,\ L\ {\rm even}}
\sum_{k=1}^2
 e^{-2\mathcal F_{L,k}(0)}[\mathcal F'_{L,k}(0)]^2>0.
\]

No positive constant for this statement is derived in this note. A proof
must prevent both expensive twists and vanishing signed response; local
variance, topology, finite positivity, and bounded cost alone do not do so.
The explicit positive measure and uniform-source normalization provide a
model-specific starting point for a free-energy or multiscale response
estimate, without an absolute neutral-surface polymer sum.

Separate review should check the character/transfer orientation, the factor
i in (13), the discrete coboundary argument (18), the L^-2 factor in (16),
the distinction between first-order and nonlinear source equivalence, and
the scope of the two controls. The proof has not been independently accepted.

P1, P2, S7, full Xi control, PHOTON-MASSLESS-PHASE, and the physical photon
remain open. Canon, registry, frontier, gates, release files, existing
probes, and existing scientific verifiers are unchanged.

## Source pins

- Public model and score: `notes/C-PHOTON-PHASE-ORIENTATION-N/README.md`,
  section 2, at public main `2294a75656ea10eeef2e11e04ac31f5d57ffdd8d`.
- Finite transfer conventions: PR #1104,
  `notes/C-PHOTON-POLE-S1-S7-N/TRANSFER.md`, sections 1-3, at
  `87ccd4b80575143ba1d3418171a7171c6e7d82e4`. This is a non-canonical
  source, not a merged Canon theorem.
- Sector path law and Mazur reduction: #1208,
  `notes/C-PHOTON-SLOW-MODE-SECTOR-MAZUR-N/PROOF.md`, especially equation
  (17), at the public-main pin above.
- All-frequency bridge: #1213, used only at its declared candidate scope.
- Cut-Fisher identities: #1216 and its preserved written-proof blob
  `0e7bb04f3a3d7a2ed2c69d058553d676f71a0390`, used only at candidate scope.
