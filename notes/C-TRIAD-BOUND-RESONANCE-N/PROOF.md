# An integer-coefficient three-channel node with bound and resonant sectors

**NON-CANONICAL / L1 / conditional analytical candidate-T.**

Author: A. M. Thorn. License: Apache-2.0.

This note constructs one explicit positive bounded Hamiltonian with two
compact bound states and a higher prepared excitation whose survival has a
controlled resonance approximation. Its coefficients in the declared local
basis are integers. The construction is a supplied model, not a derivation
from the original TWIST-J update. No physical particle identification is made.

The authority context is Public Canon v105 at public main
`892a0b11089d34e241e1eb76d2c03247022d18e6`. The owner and exposed analytical
scope were reserved in [issue #1797](https://github.com/mathorn1973/twist-j/issues/1797).
The single-contact walk of [PR #1795](https://github.com/mathorn1973/twist-j/pull/1795)
is motivation, not a premise or an operator identified with the present law.

## 1. Carrier, complete operator and spatial locality

Fix an integer K >= 2. Let u=(1,1,1)^T and J3=u u*. The carrier is

    H = C^3 direct-sum ell^2(N_0).

The first summand is a three-channel core at spatial cell zero. The lead
basis vector |n>, n >= 0, occupies cell n+1. Thus the three core coordinates
are internal channels, not three independently moving particles.

On the lead let S|n>=|n+1> be the unilateral shift. Set

    E_c = 1+3K,
    H_c = I_3+K J3,
    H_l = E_c I-K(S+S*),

and define, for x in C^3 and y in ell^2(N_0),

    H_K(x,y) = (H_c x+u y_0, H_l y+|0> u* x).                 (TBR-01)

Every matrix entry of H_K in these bases is an integer. The core entries
are 1+K on the diagonal and K off the diagonal. Lead entries are E_c on
the diagonal and -K between neighboring sites. Each core coordinate couples
to the lead endpoint with coefficient +1. The spatial range is one in the
cell coordinate just defined. This is locality on a graph with a pinned
finite core and one semi-infinite lead.

The source of integrality is the displayed operator. It does not imply that
the amplitudes of exp(-it H_K), or its state space, are an integer native
automaton. The action unit is set to one.

## 2. Exact invariant decomposition and positivity

Put

    b=u/sqrt(3),
    D={x in C^3: u* x=0},
    B=span{b} direct-sum ell^2(N_0).

The complete carrier is the orthogonal direct sum D direct-sum B. Both
summands are invariant under H_K. On D the operator is exactly I. On B,
using scalar a for the coefficient of b, it is the Jacobi operator

    H_B = [[E_c, sqrt(3)<0|],
           [sqrt(3)|0>, H_l]].                               (TBR-02)

In particular the normalized core vectors

    d_1=(1,-1,0)/sqrt(2),
    d_2=(1,1,-2)/sqrt(6)                                     (TBR-03)

are orthogonal compact eigenvectors with eigenvalue 1. The cancellation at
the endpoint is u* d_j=0. This is a supplied symmetric coupling with a
two-dimensional kernel; it is not a unique one-species ground state.

Boundedness and self-adjointness follow directly from (TBR-01), since S is
bounded and the off-diagonal coupling is finite rank. For a direct positive
bound, use ||S+S*|| <= 2 and

    2 sqrt(3)|a||y_0| <= 3|a|^2+|y_0|^2
                       <= 3|a|^2+||y||^2.

Consequently

    <(a,y),H_B(a,y)>
      >= (E_c-3)|a|^2+(E_c-2K-1)||y||^2
       = (3K-2)|a|^2+K||y||^2
      >= K(|a|^2+||y||^2),

and, in the other direction,

    <(a,y),H_B(a,y)>
      <= (E_c+3)|a|^2+(E_c+2K+1)||y||^2
      <= (2+5K)(|a|^2+||y||^2).

Together with the dark eigenvectors this proves

    I <= H_K <= (2+5K)I.                                    (TBR-04)

One initial state and this one time-independent Hamiltonian define the
evolution for all real times. No clock truncation, finite-time accuracy
horizon, postselection, reset or time-dependent switching occurs here.

## 3. Endpoint resolvent and its sheet

Write z=E_c+w. For z off the lead spectrum define

    m(z)=<0|(z-H_l)^(-1)|0>.

Removing the endpoint leaves the same half-line Jacobi tail. The Schur
complement therefore gives

    m(z)=1/(w-K^2 m(z)),
    K^2 m(z)^2-w m(z)+1=0.                                 (TBR-05)

The physical branch is fixed by m(z)~1/w as |w| tends to infinity:

    s(w)=sqrt(w^2-4K^2),  s(w)~w,
    m(z)=[w-s(w)]/(2K^2).                                  (TBR-06)

The branch is analytic on C minus [-2K,2K]. In particular s(w) is positive
for w>2K and negative for w<-2K. Its upper boundary value in the band is

    s(w+i0)=+i sqrt(4K^2-w^2),
    m(E_c+w+i0)=[w-i sqrt(4K^2-w^2)]/(2K^2).                (TBR-07)

This convention is for the resolvent (z-H)^(-1), whose scalar imaginary
part is negative in the upper half-plane. It fixes all later density and
resonance signs.

The lead spectrum is the interval [E_c-2K,E_c+2K]. For example, the sine
transform sends H_l to multiplication by E_c-2K cos(k), 0<k<pi, and the
endpoint to sqrt(2/pi)sin(k). This also derives (TBR-06) without any
finite-volume approximation.

Taking a second Schur complement in (TBR-02) gives the exact bright-core
resolvent

    G_b(z)=<b|(z-H_K)^(-1)|b>
          =1/[w-3m(z)].                                    (TBR-08)

The factor 3 is the squared norm of the unnormalized coupling vector u.

## 4. Complete bright spectral measure and absence of bound states

Substitution of (TBR-07) into (TBR-08) and Stieltjes inversion give

    rho_K(w) = 3 sqrt(4K^2-w^2)
               /{2 pi[(K^2-3)w^2+9]},   |w|<2K,
    rho_K(w) = 0,                         |w|>=2K.          (TBR-09)

Indeed the denominator of (TBR-08) on the upper band rim is

    [1-3/(2K^2)]w+i[3/(2K^2)]sqrt(4K^2-w^2).

Multiplying its squared modulus by K^2 gives
(K^2-3)w^2+9. Thus rho_K=-(1/pi)Im G_b is exactly (TBR-09), with no
unspecified normalization constant.

There is no real pole outside the band. If w-3m(z)=0 there, both w and m
are real, and (TBR-05) would imply

    (K^2-3)m(z)^2+1=0,

which is impossible for K>=2. At the endpoints the denominator is

    w-3m = +/-(2K-3/K),                                   (TBR-10)

which is nonzero. Inside the open band its imaginary part is strictly
positive. The explicit algebraic resolvent has continuous finite boundary
values at the endpoints and smooth boundary values in the band interior.
Stieltjes inversion therefore leaves no point or singular-continuous part.

The total density can also be checked exactly. Set d=K^2-3>0 and
a=3/sqrt(d). For A,a>0 the substitution w=A sin(theta) gives

    integral_(-A)^A sqrt(A^2-w^2)/(w^2+a^2) dw
      =pi[sqrt(A^2+a^2)/a-1].                              (TBR-11)

One direct derivation uses
integral_(-pi/2)^(pi/2) dtheta/(a^2+A^2 sin(theta)^2)
=pi/[a sqrt(a^2+A^2)], obtained by t=tan(theta), and then writes
A^2 cos(theta)^2=(A^2+a^2)-(a^2+A^2 sin(theta)^2).
Applying (TBR-11) with A=2K, and using

    sqrt(4K^2+9/d)=(2K^2-3)/sqrt(d),

proves

    integral rho_K(w) dw=1.                                (TBR-12)

Finally b is cyclic for H_B. The vector (H_B-E_c)b is sqrt(3)|0>.
The Jacobi recurrence then generates |1>,|2>,... from b, since K is
nonzero. Finite-support vectors are dense. Hence the scalar measure
(TBR-09) describes the entire bright sector, not only a selected component.

It follows that the full operator has precisely

    point spectrum: {1}, multiplicity two;
    absolutely continuous spectrum: [1+K,1+5K], multiplicity one;
    singular continuous spectrum: empty.                   (TBR-13)

In particular the stable core level is below the continuum by a gap K.

## 5. Continued pole and its exact width

Continue (TBR-06) from the upper band rim through an interior point of the
band into the lower half-plane. On this second sheet the square root has
the opposite sign from the physical lower-half-plane branch. A resonance
pole is a pole of this continued scalar resolvent, not a nonreal eigenvalue
of the self-adjoint H_K.

The equation w=3m, together with (TBR-05), requires

    w^2=-9/(K^2-3).

With d=K^2-3, the lower pole and the continued square root there are

    z_* = E_c-3i/sqrt(d),
    s_II(z_*-E_c)=+i(2K^2-3)/sqrt(d),
    m_II(z_*)=-i/sqrt(d).                                  (TBR-14)

These substitutions verify the sheet as well as the equation. The same
apparent zero is removable on the physical sheet. For clarity, rationalizing
(TBR-08) gives

    G_b(z)=[(2K^2-3)w-3s(w)]/[2((K^2-3)w^2+9)].            (TBR-15)

At w=-3i/sqrt(d) the physical square root is
-i(2K^2-3)/sqrt(d), so the numerator vanishes; the continued square root
in (TBR-14) produces a genuine pole instead.

Differentiate w=K^2 m+1/m at the continued pole. This gives

    m_II'(z_*)=1/(2K^2-3),
    Res_(z=z_*) G_b,II(z)
      =[1-3m_II'(z_*)]^(-1)
      =(2K^2-3)/[2(K^2-3)].                                (TBR-16)

The pole is simple. In the convention z_*=E_c-i Gamma_K/2 its width is

    Gamma_K=6/sqrt(K^2-3)>0.                               (TBR-17)

The residue may exceed one; a continued-pole contribution is not a
probability. The continuum remainder is essential, in particular at t=0.

For the fixed illustration K=4, selected without particle data, these exact
values are

    stable energy=1,  multiplicity=2;
    continuum=[5,21];
    z_*=13-3i/sqrt(13);
    Gamma_4=6/sqrt(13),  residue=29/26.                     (TBR-18)

No decimal spectral computation is used to establish them.

## 6. Survival, exact escape and a finite-K exponential bound

Prepare the normalized bright state b, with the lead empty in the direct-sum
sense y=0. Its survival amplitude is exactly

    A_K(t)=<b|exp(-it H_K)|b>
          =exp(-i E_c t) integral exp(-iwt)rho_K(w) dw.       (TBR-19)

Since rho_K is integrable, the Riemann-Lebesgue lemma gives A_K(t)->0 as
|t| tends to infinity. The evolved state remains in B. Its core component
is therefore A_K(t)b, and norm conservation gives

    probability in core=|A_K(t)|^2,
    probability in lead=1-|A_K(t)|^2 -> 1.                  (TBR-20)

The dark eigenstates are never populated by this initial bright state.
Thus this one-lead construction does not describe an excitation falling
into the dark core while also emitting products. Such a simultaneous
residual-core/output carrier is a separate construction.

There is also a controlled finite-K exponential comparison. Put

    a_K=3/sqrt(K^2-3),
    C_K=K/sqrt(K^2-3),
    h_K(w)=a_K/[pi(w^2+a_K^2)].

Both h_K and rho_K have total integral one, and

    rho_K(w)=C_K h_K(w) sqrt(1-w^2/(4K^2)) 1_(|w|<2K).

Hence both densities are bounded above by C_K h_K. Using that common
upper bound gives

    ||rho_K-h_K||_1
      <= integral[(C_K h_K-rho_K)+(C_K h_K-h_K)]
       =2(C_K-1).                                          (TBR-21)

The Fourier transform of the normalized Cauchy density h_K is
exp(-a_K|t|). Therefore for every real t,

    |exp(i E_c t)A_K(t)-exp(-Gamma_K|t|/2)|
      <=2(C_K-1),

    ||A_K(t)|^2-exp(-Gamma_K|t|)|
      <=4(C_K-1).                                          (TBR-22)

For K>=2 the elementary identity

    C_K-1 = (3/K^2)
             /[sqrt(1-3/K^2)(1+sqrt(1-3/K^2))]
           <=4/K^2

also gives the bounds 8/K^2 and 16/K^2 respectively. These are absolute,
uniform-in-time bounds, not relative accuracy in the very late tail.
For the smallest K they are coarse. As K grows they prove a precise
metastable regime with the width of the actual continued pole.

For each fixed K there is still only one fixed law. Comparing different K
compares different declared models; it does not turn K into an excitation
number of one unchanged Hamiltonian.

The rescaled survival law follows directly. For fixed real s,

    exp(i E_c K s)A_K(Ks) -> exp(-3|s|),
    |A_K(Ks)|^2 -> exp(-6|s|),              K->infinity.     (TBR-23)

Indeed K/sqrt(K^2-3)->1 and the right side of (TBR-22) tends to zero.

At finite K the survival is not exactly exponential. From

    H_K b=E_c b+sqrt(3)|0>

one gets <H_K>_b=E_c and Var_b(H_K)=3, hence

    |A_K(t)|^2=1-3t^2+O(t^4) near t=0.                     (TBR-24)

The derivative at zero is zero, whereas that of exp(-Gamma_K t) from the
right is -Gamma_K. No monotonic survival law is asserted.

## 7. Conserved norm, energy and the actual exit current

Because H_K is bounded and self-adjoint, exp(-it H_K) is unitary and
conserves the expectation and every spectral moment of H_K. This is the
displayed total Hamiltonian, not a separately assigned sinusoidal reading.

For a bright orbit write its components as a(t)b and y_n(t). The equations
at the coupling are

    i dot a=E_c a+sqrt(3)y_0,
    i dot y_0=E_c y_0-K y_1+sqrt(3)a.

The probability current from the core into the lead is

    j_(core->0)(t)=-2sqrt(3) Im(conj(a)y_0),
    d|a|^2/dt=-j_(core->0)(t).                             (TBR-25)

The lead current from n to n+1 is

    j_(n->n+1)=2K Im(conj(y_n)y_(n+1)).                     (TBR-26)

These obey the ordinary local probability continuity equation. Integration
of (TBR-25) gives the exact identity

    integral_0^t j_(core->0)(s) ds=1-|A_K(t)|^2.             (TBR-27)

The current can change sign; its limiting integrated value is one. Escape
is through an actual infinite spatial lead, not into removed clock modes.
No claim of a neutron, electric-charge current or beta-decay products is
made by these probability-current equations.

## 8. Stability scope and physical boundary

Exact compact support in (TBR-03) uses the equality of the three endpoint
couplings and the displayed core law. A perturbation that breaks that
symmetry can remove exact compactness and split the degeneracy.

Nevertheless the below-threshold eigenstates have a separate limited
robustness. If B is any bounded self-adjoint perturbation with ||B||<K/2,
the circle centered at 1 of radius K/2 stays in the resolvent of H_K+sB
for every 0<=s<=1. This follows from the distance K/2 to the unperturbed
spectrum and the resolvent Neumann series. The continuous Riesz projection
inside that circle keeps rank two. Thus a two-dimensional isolated spectral
cluster persists. This does not assert exact compactness, the same energies,
the same resonance width, or spatial locality for an arbitrary B. Positivity
after perturbation additionally follows if ||B||<1.

The exact conclusions are the supplied local positive model, its complete
spectral split, its continued resonance and the survival estimates. They
do not select the model from J or native U; select K; provide a moving
center of mass, fermionic statistics, a physical color interaction or a
unique stable species; derive a measured mass or lifetime; or furnish a
residual core and two independently propagating decay products.

Replacing the lead by a two-excitation continuum preserves the elementary
dark-kernel calculation only if the new coupling has the same kernel.
It does not preserve (TBR-06), (TBR-09) or (TBR-14) by declaration. Such an
extension needs its own resolvent, threshold and conservation proofs.

## 9. Analytical review record

The model and the pole formulas were exposed during analytical preparation
before the scope issue. An initially suggested optional residue was corrected
before that issue to (TBR-16), and the public issue records the correction.
No scientific executable, numerical search or numerical spectral run occurred.

A separate-context reviewer in this author session checked the exposed
resolvent, density, normalization, branch cancellation, pole, corrected
residue and cyclicity. That reviewer supplied the common-majorant proof
behind (TBR-21)--(TBR-22); the author rederived it. This is nonblind
same-session analytical review, not external independent acceptance and not
a two-architecture computational gate. The candidate status remains pending
independent mathematical review.
