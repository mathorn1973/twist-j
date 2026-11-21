# Exact Hodge matching cannot persist on the source window

**NON-CANONICAL. L1. Analytical candidate-T; C-HODGE-CAPTURE-PARITY-N.**

This proof uses the pinned source law and the fixed bright arrangement-transfer
marking derived in PROOF_TRANSFER.md. The proof was prepared before its first
computational audit. All fiberwise readings use the same regular (E,K) context
at input and output, in the source-calibrated arrangement chart. It does not
replace the dark boundary relation by an invertible transfer or classify a
separately derived physical spatial multichannel cut or an arbitrary nonlocal
mixing of K fibers.

Source:

<https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md>.

The inputs are its equations (1)--(6), (15), (20)--(24), and (43)--(50).
The source preparation and its existing windows are equations (26), (51)--(54).

## 1. The actual bright parity transfers

At a boundary point where the source Caratheodory functions are finite, write

~~~
F1 = a + i b1,          F2 = c + i d,
a > 0,                 c > 0,
r = a*c,               B = 4*sqrt(r),
D = 4 + F1*F2,         A = 4 - conjugate(F1)*F2.
~~~

Here B is a positive scalar, not a new transfer matrix. The exact identity

~~~
|D|^2 - |A|^2 = B^2
~~~

follows directly by expanding the two squared moduli. The complete two-active-
channel scattering matrix, including repeated contacts, is

~~~
S_active = (1/D)*[[A,-B],[B,conjugate(A)]].
~~~

With the fixed receiver calibration and the declared arrangement regrouping,
the two swap parities give

~~~
M_plus = (1/B)*[[conjugate(D),-conjugate(A)],[A,-D]],
M_minus = diag(-1,1)*M_plus.
~~~

Both preserve Sigma=diag(1,-1). Their determinants are -1 and +1, respectively,
and their traces are

~~~
tr(M_plus)  = -2i*Im(D)/B,
tr(M_minus) = -2*Re(D)/B.
~~~

This is not a factor A0 tensor J. The two parities have different directional
transfer matrices. In particular the earlier fixed-factor involution lemma
cannot be applied to this full capture-and-receiver bright transfer.

Put

~~~
kappa_plus  = |tr(M_plus)|^2 - 2,
kappa_minus = |tr(M_minus)|^2 - 2.
~~~

Each parity congruence has polynomial

~~~
(z-1)^2*(z^2-kappa_parity*z+1).
~~~

The target is the marked four-dimensional Hodge action with polynomial

~~~
(z^2-3*z+1)*(z^2-phi*z+1),       phi=(1+sqrt(5))/2.
~~~

## 2. Cross-parity coherences do not evade the two trace conditions

The full label swap acts on C^26 tensor C^26. Its plus and minus spaces have
dimensions 351 and 325. The complete transmitting bright amplitude carrier is

~~~
(C^2 tensor L_plus) direct-sum (C^2 tensor L_minus),
T_bright = (M_plus tensor I_351) direct-sum (M_minus tensor I_325).
~~~

Its entire Hermitian carrier includes both diagonal parity blocks and all
off-diagonal parity coherences. No label state is projected out in the
following spectral argument.

Remove the determinant phase from M_plus by setting A_plus=-i*M_plus, and put
A_minus=M_minus. Both are in SU(1,1), so their traces are real. Write their
eigenvalue multisets as

~~~
spec(A_plus)={rho,rho^-1},       spec(A_minus)={sigma,sigma^-1}.
~~~

Each reciprocal pair is either real and nonzero, or lies on the unit circle.
This includes the repeated roots +1 and -1. The diagonal Hermitian blocks
have eigenvalues drawn from

~~~
{1,rho^2,rho^-2,sigma^2,sigma^-2}.
~~~

An off-diagonal block Z evolves by M_plus*Z*M_minus^dagger. Complexification
and tensor triangularization give its eigenvalues i*rho^epsilon*sigma^delta,
where epsilon,delta are independently +1 or -1. Realifying this block adds
their conjugates. Since each reciprocal multiset is closed under complex
conjugation, the complete cross-parity eigenvalue set is contained in

~~~
{ plus-or-minus i*rho^epsilon*sigma^delta : epsilon,delta in {+1,-1} }.
~~~

Label multiplicities only repeat these eigenvalues. Triangularization proves
the statement even when a transfer is not diagonalizable.

The target requires both the nonunit positive-real pair phi^2,phi^-2 and the
nonreal unit pair zeta_10,zeta_10^-1. Consider the possibilities:

1. If both reciprocal pairs are on the unit circle, every joint congruence
   eigenvalue has modulus one. The required boost is absent.
2. If both pairs are nonunit real pairs, the diagonal-block eigenvalues are
   positive real and the cross-block eigenvalues are purely imaginary.
   Neither zeta_10 nor its inverse is available.
3. If exactly one pair is nonunit real, a nonreal unit target eigenvalue must
   come from the square of the other, unit-modulus pair: cross-block moduli
   are nonunit. Once that square is zeta_10 or its inverse, the unit pair is
   not {i,-i}; cross-block eigenvalues therefore cannot be positive real.
   The target boost must come from the internal square of the real pair.

The same reasoning includes a repeated unit pair. It follows that every
four-dimensional invariant linear subquotient of the full bright Hermitian
carrier carrying the target must satisfy

~~~
{kappa_plus,kappa_minus} = {3,phi}.
~~~

Conversely, at these trace values the two moving parity planes supply the
target action as an invariant direct sum. Thus this is the exact spectral
condition for this bright carrier, including its cross-parity coherences.
It is not yet an identification of the fixed canonical metric or lattice.

Spectral containment for subquotients is elementary: a basis adapted to an
invariant subspace and its invariant kernel makes the ambient matrix block
triangular. The quotient characteristic polynomial is a factor of the
ambient polynomial. No new eigenvalue can appear in the quotient.

## 3. At one energy there are at most sixteen admissible F2 values

Fix a finite F1=a+i*b1 with a>0. Set f=b1/a and t=sqrt(a*c)>0. The target
conditions require

~~~
Re(D) = sign1*u*t,       Im(D) = sign2*v*t,
~~~

where sign1,sign2 are independently +1 or -1, and (u,v) is either

~~~
(2*sqrt(5),2*sqrt(phi+2))
~~~

or the reversed ordered pair. Both assignments are allowed; the proof does
not preselect which parity supplies the boost.

From Im(D)=a*d+b1*c one obtains

~~~
c = t^2/a,
d = (sign2*v*t-f*t^2)/a.
~~~

Substitution into Re(D)=4+a*c-b1*d gives the exact quadratic equation

~~~
(1+f^2)*t^2 - (sign1*u+sign2*v*f)*t + 4 = 0.
~~~

Its leading coefficient is strictly positive and its constant term is 4.
For each of the two assignments and four sign pairs it has at most two
positive real roots. Each root determines c and d uniquely. Consequently,
for this fixed F1 there are at most sixteen possible complex values of F2
compatible with the complete target spectrum. The bound may be loose; its
finiteness is the only property needed.

No continuity of a sign choice, parity assignment, root branch, or K-dependent
boundary value is assumed.

## 4. The first exact source moment distinguishes all momenta

Let b_source denote the unit-norm output contact vector from source equation
(16), with its label suppressed. Its Caratheodory function is

~~~
F2(K,z) = <b_source,(z+U02(K))*(z-U02(K))^-1*b_source>,   |z|>1.
~~~

For every K, expansion at infinity gives

~~~
F2(K,z) = 1 + 2*mu1(K)/z + O(z^-2),
mu1(K) = <b_source,U02(K)*b_source>.
~~~

All quantities in the first coefficient can be obtained directly from one
source step. The object contact vector is A_obj=(e1-e4)/sqrt(2). The source
coin satisfies M2*A_obj=A_obj, hence

~~~
<delta0*A_obj,W(P)*delta0*A_obj> = exp(-i*g)*cos(P).
~~~

For the pulse contact port eta=e1, source equation (3) gives

~~~
<eta,Vtilde(k)*eta> = exp(-i*beta)*(1/5-(4/5)*exp(i*k)).
~~~

Using the exact fiber relation k=K-P and source equation (15),

~~~
mu1(K)
 = exp(-i*(g+beta))*integral_T cos(P)*(1/5-(4/5)*exp(i*(K-P))) dP/(2*pi)
 = -(2/5)*exp(-i*(g+beta))*exp(i*K).
~~~

Here the integral of cos(P) is zero and the integral of cos(P)*exp(-i*P) is
1/2. Therefore mu1(K) is different at every two distinct momenta modulo 2*pi.
In particular F2(K,.) and F2(K',.) are different holomorphic functions when
K is not K' modulo 2*pi. No radial boundary computation enters this proof.

## 5. An elementary bounded-analytic uniqueness lemma

For |w|<1 define

~~~
C_K(w)=F2(K,1/w),       C_K(0)=1,
h_K(w)=(C_K(w)-1)/(C_K(w)+1).
~~~

Positivity of the real part of the source Caratheodory function gives
|h_K(w)|<1. Also

~~~
h_K(0)=0,       h_K'(0)=mu1(K).
~~~

For two distinct momenta, the function

~~~
g_jl(w)=(h_Kj(w)-h_Kl(w))/(2*w)
~~~

extends holomorphically to w=0, has modulus at most one by Schwarz's lemma,
and has nonzero value (mu1(Kj)-mu1(Kl))/2 at zero.

We use the following elementary fact. A holomorphic H on the disk with
|H|<=1 and H(0) nonzero cannot have radial limit zero on a boundary set of
positive Lebesgue measure. Jensen's inequality gives, for each radius,

~~~
integral -log|H(r*exp(i*theta))| dtheta/(2*pi) <= -log|H(0)|.
~~~

The integrand is nonnegative. If the radial limit vanished on a set of
positive measure, Fatou's lemma would force these integrals to become
unbounded, a contradiction. Zeros on individual circles are handled by the
usual integrable logarithm, or by taking radii avoiding such zeros.

Thus the uniqueness step needs no assumption of a continuous boundary value
and no external numerical estimate.

## 6. Seventeen fixed momenta rule out a uniform source window

Use the source momentum

~~~
k0 = -arccos((9-5*sqrt(5))/16)
~~~

and the following seventeen fixed test momenta:

~~~
K_j = k0 + j/16000,       j=-8,-7,...,7,8.
~~~

They all lie inside the source window [k0-1/1000,k0+1/1000], and are pairwise
different modulo 2*pi. The energy interval can be the source's already
declared interval [8*pi/5-1/1000,8*pi/5+1/1000], or any interval of positive
length on which the proposed uniform bright target identification is claimed.

Suppose the target identification held for almost every energy in this
interval at all seventeen momenta, with finite F1,F2 and positive bright
densities. At each such energy, section 3 allows at most sixteen values of
F2 for the common value of F1. Hence two of the seventeen F2 values coincide.
The coinciding pair may change with energy; no pair is chosen in advance.

Form the bounded holomorphic product

~~~
H(w)=product_{j<l} g_jl(w).
~~~

There are 136 factors. Their values at zero are all nonzero, so H(0) is
nonzero. On the hypothesized energy set the radial boundary value of H is
zero: equality of two finite F2 values gives equality of their Cayley
transforms and therefore a zero factor. Section 5 gives a contradiction.

Consequently the source cannot supply the exact same marked Hodge action
through an invariant linear reading of this full bright carrier throughout
the declared energy-momentum window. If a putative transfer fails to be a
defined positive-density bright graph on a positive-measure part of that
window, the asserted uniform graph contract already fails there; this does
not provide an escape from the conclusion.

## 7. Stronger conclusion: the exact matching set has measure zero

We first specify the measurability needed below. For each |w|<1 the operator
U02(K) is norm-continuous in K: the pulse V(K-P) is uniformly norm-continuous
in K, and the object factor is unitary. Its resolvent and contact scalar are
therefore continuous in (K,w) in the open disk, with the removable value at
w=0 supplied by the moment expansion. Radial limits along one fixed sequence
of radii increasing to one are jointly measurable. For each fixed K the
normalized Caratheodory function has finite radial limits for almost every E;
equivalently one can use the bounded Cayley transform and its almost-everywhere
radial limits. The Cayley transform can equal one at the boundary only on a
null set, by the
uniqueness lemma in section 5 applied to (1-h_K)/2. Fubini makes the joint
exceptional set product-null. We use this measurable representative throughout;
F1 is independent of K. No assertion of positivity outside the stated regular
domain is required.

Let S be the measurable set of (K,E) in a finite rectangle where these boundary
values are finite, both bright densities are positive, and the target trace
conditions hold in the calibrated arrangement chart. Then S has two-dimensional
Lebesgue measure zero. Momentum is represented on the circle once; equivalently
the rectangle uses a single momentum chart, so pairwise equality modulo 2*pi
defines a null set of tuples.

Indeed, suppose its measure were positive. For each E, let S_E be its momentum
section. Fubini's theorem implies

~~~
integral |S_E|^17 dE > 0.
~~~

Applying Fubini again to seventeen momentum variables produces a tuple of
seventeen momenta having a common positive-measure set of energies on which
all seventeen belong to S. The momentum diagonals have measure zero, so the
tuple can be chosen pairwise distinct modulo 2*pi. At those momenta, the
product argument in section 6 gives the same contradiction.

This proof does not require S to contain an open rectangle or require
boundary continuity in K. It also allows the parity assignment and the
quadratic-root branches to vary arbitrarily across S.

A nonzero packet whose spectral norm measure is absolutely continuous in
(K,E) cannot be supported entirely on this exact matching set. This applies
to the declared source packet with its ordinary dK/(2*pi) dE spectral measure.
It does not exclude an isolated exact equality, a lower-dimensional singular
spectral preparation, or an approximate matching on a finite-width packet.

## 8. Scope and the fixed-form question

The obstruction is already spectral. A fixed metric isometry cannot repair
it on the source window, nor can a context-dependent similarity using the
same regular (E,K) source context at input and output in the calibrated
arrangement chart. All encoded labels and all cross-parity coherences were
included in section 2; no empty-memory assumption was used.

This proof supplies no numerical distance from the target, no pointwise
certificate at the central energy and momentum, and no exclusion of
individual isolated matches. It does not establish that the entire source
law lacks every possible Hodge reading: a different physical spatial cut,
the non-total dark relation, nonlinear readings, or a genuinely covariant
identification between different contexts are separately specified problems.
In particular the source receiver calibration was accounted for before
selecting this chart; no claim is made about an arbitrary further nonlocal
operation mixing distinct K fibers.

The natural current-induced form and its label-multiplicity weights still
matter at any isolated conditional match. They must be compared with the
unchanged beta_EJ, rather than replacing that target by a newly scaled form.
No arithmetic or integral-lattice equivalence is inferred from a real
Lorentz signature or from the mere presence of cyclotomic phases in the
source coefficients.
