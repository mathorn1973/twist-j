# K1: invariant quadratic form and the exact integer-time Cesaro state

**Status: candidate-T / NON-CANONICAL.**
**Scope:** the selected mathematical K1 construction in Public Canon v82.
**Owner unchanged:** TT-VECTOR-STATE-NORMALIZATION [O].

No statement here adopts a physical state, physical energy, source,
cosmological scalar, tensor power, native-U occurrence law, or numerical r_T.
The rational certificates were calculated on one x86_64 lane. Two algebraic
implementations agree, but both were written by the same agent.

## 1. Source and explicit additional reading convention

The source is DEF-K1-LINEAR-METRIC at the following immutable public basis:

- activation/main: `f6baa1fbfe320e5e6cef610f9da6a500e1ba8f08`;
- content: `4e65adf0b483311d2a031cf2a23a65f2caf5af8a`;
- `canon/CANON.md`, SHA-256
  `5dcbf2abac151af1e6019ea4c009c7631cb773824a850bc5f5ff61bb324f9146`,
  580724 bytes.

The original ten words, optional weights nu, unit amplitude, five marked
sites, initial pair h_0,h_1, and rational L are unchanged. Write

\[
 h_{n+1}=(2I-L)h_n-h_{n-1},\qquad
 L={188I-29(S+S^{-1})-65(S^2+S^{-2})\over324}.
\]

The Canon proves mean_r(h_n)=1/5 and -59/100<h_n(r)<99/100.
Its five Fourier eigenvalues are 0,lambda_+,lambda_-,lambda_-,lambda_+,
where

\[
 \lambda_\pm={235\pm18\sqrt5\over324},\qquad
 c_\pm=1-\lambda_\pm/2={413\mp18\sqrt5\over648},\qquad
 d_\pm=1-c_\pm^2>0.
\]

The **additional explicit mathematical reading convention** in this note
is uniform averaging over successive integer times, not over native
four-bit packets supplied again at every time. For a continuous function
F of the centered two-slice state X_n=(h_{n+1}-1/5,h_n-1/5), define

\[
 \mathcal A(F)=\sum_{w\in W}\nu(w)
       \lim_{N\to\infty}{1\over N}\sum_{n=0}^{N-1}F(X_n(w)).
\]

We prove that these limits exist and determine one comparison law. This
choice of readout is not claimed to be forced by J or by physical measuring
procedures. In particular the original finite packet ensemble is not
stationary under the K1 continuation.

## 2. Exact invariant and its complete energy-value law

Define a mathematical quadratic invariant, in the normalization of the
restricted K1 action,

\[
 E(a,b)={1\over2}\bigl(\|b-a\|^2+\langle b,La\rangle\bigr).
\]

If a=h_n,b=h_{n+1}, and c=h_{n+2}, symmetry of L gives

\[
 2[E(b,c)-E(a,b)]
 =\langle c-a,c-2b+a+Lb\rangle=0.
\]

This is an all-time identity, not an inference from finitely many ticks.
Putting p=b-a and m=(a+b)/2 gives

\[
 E(a,b)={1\over2}\left[
  \langle p,(I-L/4)p\rangle+\langle m,Lm\rangle\right].
\]

All nonzero eigenvalues of L lie in (0,4). Thus E is nonnegative, and
zero only for a common spatially constant pair. Every K1 initial packet
has nonzero spatial modes, so E>0 for every word. Constants carry no
spatial restoring energy; this does not remove their field equation.

A direct rational evaluation on the three displacement classes gives

| Absolute displacement | E | Total nu weight |
| --- | --- | --- |
| 0 | 53/432 | 1/3 |
| 1 | 713/2592 | 1/3 |
| 2 | 67/162 | 1/3 |

Consequently

\[
 \boxed{\mathbb E_\nu E={701\over2592}}.
\]

This invariant has not been identified with a lapse-variation source,
physical mass density, or a nonlinear gravitational energy. In particular
its value must not be inserted into a Friedmann equation by hand.

## 3. An all-order nonresonance proof

Let K=Q(sqrt5), omega_+,omega_- in (0,pi), and

\[
 z_\pm=c_\pm+i\sqrt{d_\pm}=e^{i\omega_\pm}.
\]

The exact arithmetic certificates are

\[
 d_\pm={247715\pm14868\sqrt5\over419904},\qquad
 d_+d_-={60257434105\over176319369216},\qquad
 \operatorname{Tr}_{K/\mathbb Q}(2c_\pm)={413\over162}.
\]

The numerator of d_+d_- has 11-adic valuation one; the denominator has
valuation zero. A positive rational number is a square in Q(sqrt5) only
if it is a rational square or five times a rational square. Indeed,
(a+b sqrt5)^2 in Q implies ab=0. The odd valuation at 11 therefore proves
that d_+d_- is not a square in K.

Both -d_+ and -d_- are negative in the principal real embedding and are
not squares in the real field K. The two quadratic extensions
K(sqrt(-d_+)) and K(sqrt(-d_-)) are distinct: otherwise their quotient
square class, equivalently d_+d_-, would be a square. Their compositum
has an automorphism fixing K and sqrt(-d_-) while negating sqrt(-d_+).
It sends z_+ to z_+^{-1} and fixes z_-.

Neither z_+ nor z_- is a root of unity. If one were, z+z^{-1}=2c would
be an algebraic integer. Its rational field trace would then be an
integer, contrary to 413/162.

Suppose z_+^a z_-^b=1 for integers a,b. Apply the automorphism just
constructed and divide the resulting relation by the original one. Then
z_+^{2a}=1, so a=0. It follows that b=0 as well. Thus

\[
 \boxed{a\omega_++b\omega_-\in2\pi\mathbb Z
       \quad\Longrightarrow\quad a=b=0.}
\]

No numerical angle tolerance or finite resonance search appears in this
argument.

## 4. One Cesaro limit for each fixed word

Let P_0=11^T/5 and

\[
 P_+={L-\lambda_-(I-P_0)\over\lambda_+-\lambda_-},\qquad
 P_-=I-P_0-P_+.
\]

These are the real orthogonal rank-two spectral projectors. For a fixed
word define

\[
 a_\pm=P_\pm h_0,\qquad
 b_\pm={P_\pm h_1-c_\pm P_\pm h_0\over\sqrt{d_\pm}}.
\]

The exact solution is

\[
 h_n={1\over5}{\bf1}+
 \sum_{\epsilon\in\{+,-\}}
 [a_\epsilon\cos(n\omega_\epsilon)
       +b_\epsilon\sin(n\omega_\epsilon)].
\]

For every nonzero (a,b) in Z^2, section 3 and the finite geometric-series
identity give

\[
 {1\over N}\sum_{n=0}^{N-1}z_+^{an}z_-^{bn}\longrightarrow0.
\]

This proves convergence to uniform product measure for trigonometric
polynomials on the two-circle phase torus. Uniform approximation by
trigonometric polynomials extends it to every continuous function. This
is the elementary character proof of the Weyl criterion. Pushing that
measure through the displayed solution and its next slice proves
existence and uniqueness of the fixed-word Cesaro limit.

Averaging those fixed-word limits with the **unchanged chosen nu** proves
existence of the comparison law in section 1. The result is uniqueness
for this initial law and this averaging convention, not uniqueness of
all invariant K1 laws or all physical states.

The averaging measure lives on the real compact closure of a rational
integer-time trajectory. It is not a new assertion that the native
substrate is continuous. Section 7 gives integer/rational computations
of every polynomial moment without drawing any continuum sample.

## 5. Full two-time covariance, with exact temporal dependence

Write

\[
 A=\mathbb E_\nu[h_0h_0^T]=\mathbb E_\nu[h_1h_1^T],\qquad
 B=\mathbb E_\nu[h_0h_1^T].
\]

The actual two-window law is symmetric under exchange, so B=B^T.
The stationary mean is 1/5 at each site. Averaging the sine and cosine
terms in section 4 gives

\[
 C_\epsilon={P_\epsilon(A-c_\epsilon B)P_\epsilon\over d_\epsilon},
 \qquad
 \boxed{C(m)=\sum_{\epsilon\in\{+,-\}}
                 C_\epsilon\cos(m\omega_\epsilon)}.
\]

Here C(m)_{rs}=A[(h_n(r)-1/5)(h_{n+m}(s)-1/5)]. Exchange symmetry
cancels the possible antisymmetric sine term. Different temporal
frequencies have zero mixed phase average. Each C_epsilon is positive
semidefinite because before averaging over words it is
(a_epsilon a_epsilon^T+b_epsilon b_epsilon^T)/2.

The two terms are Galois conjugate. Since cos(m omega)=T_m(c), with
T_m the integer Chebyshev polynomial, **C(m) is rational for every
integer lag m**. EXPECTED.json gives the complete 5 by 5 matrices C(0)
and C(1); no spatial averaging or translation-invariance assumption is
hidden in them. Their diagonals are not all equal, so this law is not
claimed to be spatially homogeneous.

The covariance does not decay to zero. Its temporal spectrum has only
the four atoms +/-omega_+ and +/-omega_-. In particular this stationary
construction is not mixing and does not produce independent time
samples. Uniform phase coordinates at one random time must not be
confused with independent draws at successive times.

## 6. Exact modal powers in the already fixed Fourier convention

Use exactly the Canon's unitary five-point transform. Put

\[
 a_\pm^{\rm pow}={3\pm\sqrt5\over40}.
\]

The initial Fourier square magnitude in a slot is a_epsilon^pow. The
law of Delta_u=u_1-u_0 gives weight 1/3 to each absolute-displacement
class 0,1,2. Therefore for every nonzero Fourier slot

\[
 \mathbb E_\nu\cos(2\pi k\Delta_u/5)
 ={1+\cos(2\pi/5)+\cos(4\pi/5)\over3}={1\over6}.
\]

Solving the scalar recurrence and averaging its squared magnitude yields

\[
 \boxed{\overline P_\epsilon
  =a_\epsilon^{\rm pow}
        {10+\lambda_\epsilon\over
            3\lambda_\epsilon(4-\lambda_\epsilon)}}.
\]

More explicitly,

\[
 \overline P_+={12648837771+3876385761\sqrt5\over120514868210},
 \qquad
 \overline P_-={12648837771-3876385761\sqrt5\over120514868210}.
\]

Slots 1,4 have P_+; slots 2,3 have P_-. The centered zero slot vanishes.
These are diagonal Fourier powers. They are not a declaration that the
full spatial Fourier covariance is diagonal. The complete C above
retains the marked-coordinate correlations.

Parseval gives the exact spatial mean of the stationary site variance:

\[
 \boxed{{1\over5}\operatorname{Tr}C(0)
    ={2\over5}(\overline P_++\overline P_-)
    ={25297675542\over301287170525}}.
\]

Also E=2 sum_epsilon d_epsilon P_epsilon=701/2592. This independently
connects the modal and real-space invariant calculations.

None of these finite slot labels is a cosmological wave number. None of
these quantities is a physical tensor-to-scalar ratio.

## 7. Every finite polynomial moment has a rational algorithm

The centered two-slice state belongs to an eight-dimensional rational
space: each five-site slice has zero sum. Let T be the rational update
matrix on that space. It is diagonalizable over C, with unit-modulus
eigenvalues z_+,z_+^{-1},z_-,z_-^{-1}, each twice.

For any fixed polynomial degree D, the induced map on the finite-dimensional
space of monomials of degree at most D is rational and diagonalizable;
its eigenvalues are products of these unit-modulus eigenvalues. Hence
all eigenvalues have modulus one, and eigenvalue 1 has no Jordan block.
Its Cesaro projector is rational. Constructively, if the minimal polynomial
has the simple factorization p(x)=(x-1)q(x), q(1)!=0, that projector is
q(T_D)/q(1); if 1 is absent it is zero.

Thus every finite rational polynomial moment, including all equal-time
and multi-time fourth moments of h, is exactly rational and computable
by finite linear algebra. Fixed time lags introduce only rational powers
of the invertible matrix T. Combining with the original rational nu
preserves rationality. Bounded support and nonzero variance also exclude
a Gaussian law for h; no Gaussian or Wick hypothesis is required.

This is a moment result for the evolved metric variable h. The Canon's
local doublet square is prescribed only on its first two slices. This
note neither invents a later native doublet nor proves that an arbitrary
square-root lift is the physically selected one.

## 8. A separate rational audit

`verify.py` works in Q(sqrt5) using an explicitly implemented exact field
and the spectral formulas. It checks the universal identity T^T Q T=Q,
all projectors, the covariance formula, all 31 principal minors of C(0),
and the stationarity identity for the two-slice covariance. Its 320 finite
recurrence checks are supplementary, not its all-time proof.

`break.py` imports no spectral code. On the rational eight-dimensional
carrier it repeatedly forms K -> T K T^T from the initial moment K0,
finds the first exact Krylov dependence, and derives its own annihilator
of degree 9. Factoring the simple factor x-1 gives

\[
 q(1)={301287170525\over892616806656}\ne0.
\]

The rational Cesaro projector q(A)K0/q(1), A(K)=TKT^T, reproduces every
entry of C(0), every entry of C(1), the invariant mean, and the mean site
variance exactly. This is a same-agent cross-check by a different algebraic
route, not a blind second author, an independent scientific confirmation,
or a two-architecture public gate.

## 9. Named layer boundary, not an adopted lift

This incubation proves statements about a selected mathematical construction.
A future public proposal must place the following maps explicitly rather
than rename the comparison law as a native physical state:

- `K1-L1-L5-ORBIT`: a frozen rational two-slice packet to its derived K1
  trajectory, with exact marked-coordinate/counter equality;
- `K1-L5-L6-CESARO`: that trajectory and its chosen integer-time averaging
  convention to the mathematical Borel measure on its real orbit closure;
- a separate physical-readout bridge, if physical state or occurrence is
  claimed, preserving the source, support, averaging semantics and outputs.

These names describe proposed contracts only. No public GATES.tsv row is
created or satisfied here. In particular the mathematical proof is not a
physical L6 admission, and no current owner row is partly discharged by
calling it one.

## 10. External method reference

The character averaging argument in section 4 is self-contained. For the
standard Weyl criterion on tori, see Terence Tao, *254B, Notes 1:
Equidistribution of polynomial sequences in tori*, 28 March 2010,
Proposition 1. The reference supports the general method only, not any
K1-specific conclusion or physical interpretation.

Source paths: `canon/CANON.md` at the immutable v82 basis;
`notes/V81-TT-K1-SOURCE-MAP-1.md` and
`notes/V81-TT-NORMALIZATION-CLOSURE-INPUT-1.md` at that same basis.
