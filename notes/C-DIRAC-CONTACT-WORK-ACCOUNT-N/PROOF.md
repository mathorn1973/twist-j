# Full contact energy law and the sharp-source coherence boundary

PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T.
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

All statements concern the exact comparison model in CONTRACT.md.
No scientific executable or numerical experiment is used.
The algebraic identities are self-contained below.

## 1. One walk and the full pair

Let X,Y,Z be the Pauli matrices, r=sqrt(1+mu^2), mu>0, and

    U_mu(k) = exp(i k Z)(I+i mu X)/r.

The complete normalized walk is unitary. Its nominated sine-energy
operator is the bounded self-adjoint operator

    H(k) = r(U_mu(k)^*-U_mu(k))/(2i)
         = -mu cos(k) X + sin(k) A,
    A    = mu Y-Z,
    A^2  = (1+mu^2)I.

In position space H has only shifts by plus/minus one and no zero-shift
term. On the two-distinguishable-walk carrier set

    H0 = H tensor I + I tensor H,
    P  = sum_x |x,x><x,x| tensor I_4.

The full coin is retained. Either summand of H0 shifts exactly one
member of a coincident pair. On a ring L>=2 this leaves the coincidence
subspace, so

    P H0 P = 0.                                                   (1)

Our declared 4-divides-L scope satisfies that condition.

For real g write

    K_g = exp(-igP) = I+bP,
    b   = exp(-ig)-1,
    s   = sin^2(g/2).

Then |b|^2=4s, b+conj(b)=-4s and K_g is unitary. The full period is

    V_g = K_g (U_mu tensor U_mu).

Let a be the normalized product of momentum 0 with X eigenvalue -1
and momentum pi with X eigenvalue +1. Direct substitution gives

    H0 a = 2mu a,
    (U_mu tensor U_mu)a = -a,
    <a,P a> = 1/L.                                                (2)

Thus V_g a and K_g a differ only by a global minus sign. Energy
probabilities and reduced-state claims below apply to the actual full
period on this preparation.

## 2. Complete moments

For any real-valued function F on the finite spectrum of H0,

    <F(H0)>_out
      = F(2mu)+4s[<Pa,F(H0)Pa>-F(2mu)/L].                        (3)

Indeed, expand K_g a=a+bPa. The two cross terms use
F(H0)a=F(2mu)a, and (2) supplies their value. This formula retains
every final mode.

With F(E)=E, (1) gives

    <H0>_out = 2mu(1-4s/L),
    Delta <H0> = -8mu s/L.                                      (4)

A useful full-operator version is

    K_g^* H0 K_g-H0
      = (cos(g)-1){P,H0}+i sin(g)[P,H0].                         (5)

The quadratic b term vanishes by (1). Formula (4) is the expectation
of (5) in a. It is not the cost of one postselected upward transition.

For completeness, fix Fourier momentum k in the L-point ring set.
The coincidence vector has the exact expansion

    Pa = (1/L) sum_k |k,pi-k> tensor v,
    v  = |-x,+x>.

On that fixed coin vector,

    H0(k,pi-k)
      = mu cos(k)(-X_1+X_2)+sin(k)(A_1+A_2).

Here (-X_1+X_2)v=2v, each one-spin A expectation is zero,
and <v,(A_1+A_2)^2 v>=2(1+mu^2). Consequently

    ||H0(k,pi-k)v||^2
      = 4mu^2 cos^2(k)+2(1+mu^2)sin^2(k).

For 4 dividing L, the exact discrete averages of cos^2 and sin^2
are both 1/2. It follows that

    <Pa,H0^2 Pa> = (1+3mu^2)/L,
    <H0^2>_out   = 4mu^2+4(1-mu^2)s/L,                          (6)
    Var_out(H0)  = 4(1+7mu^2)s/L-64mu^2 s^2/L^2.                (7)

This uses finite Fourier orthogonality analytically, not a sampled check.

## 3. Full finite spectral law at L=4 and mu=2

Set r=sqrt5. Simultaneous translation preserves total momentum, and
both the free walk and P preserve its pi sector S. This sector has
four momentum pairs and four coin states per pair, hence dimension16.
There is no further projection inside S.

Its unshifted H0 energies are

| E | Multiplicity in S |
|---|---:|
| 4 | 2 |
| -4 | 2 |
| 2sqrt5 | 2 |
| -2sqrt5 | 2 |
| 0 | 8 |

To verify this, the pairs (0,pi) and (pi,0) have one-spin energies
plus/minus2; each pair contributes energies 4,0,0,-4.
The pairs (pi/2,pi/2) and (3pi/2,3pi/2) have one-spin energies
plus/minussqrt5; each contributes 2sqrt5,0,0,-2sqrt5.

For the actual preparation,

    Pa = (1/4)(
         |0,pi> + |pi,0> + |pi/2,pi/2> + |3pi/2,3pi/2>
         ) tensor v.                                           (8)

The original momentum pair and coin have energy4. The reversed pair
with the same coin has energy-4. At either remaining pair, the
single-spin A/sqrt5 projectors have equal probabilities 1/2 in either
X eigenstate because <+/-x,A(+/-x)>=0. The two-spin probabilities
are therefore 1/4,1/2,1/4 at energies 2sqrt5,0,-2sqrt5.

The coefficient of the original component in K_g a is 1+b/4.
Every other momentum-pair component has coefficient b/4.
Thus the complete H0 output law is

| E | w_E(g) |
|---|---:|
| 4 | 1-3s/4 |
| -4 | s/4 |
| 2sqrt5 | s/8 |
| -2sqrt5 | s/8 |
| 0 | s/4 |

The probabilities sum to one for every 0<=s<=1. They give

    <H0>_out = 4(1-s),
    <H0^2>_out = 16-3s,
    Var_out(H0) = 29s-16s^2,                                   (9)

agreeing exactly with (4),(6),(7). No restriction to outgoing positive
bands, no outcome rejection and no postselection has been used.
The event E=2sqrt5 includes both pi/2 and 3pi/2 equal-momentum pairs.

At the nominated g=2pi/5,

    s = (5-sqrt5)/8,

and the law is

| E | w_E |
|---|---:|
| 4 | (17+3sqrt5)/32 |
| -4 | (5-sqrt5)/32 |
| 2sqrt5 | (5-sqrt5)/64 |
| -2sqrt5 | (5-sqrt5)/64 |
| 0 | (5-sqrt5)/32 |

Therefore

    <H0>_out = (3+sqrt5)/2,
    Delta <H0> = (sqrt5-5)/2 < 0,                               (10)
    <H0^2>_out = (113+3sqrt5)/8,
    Var_out(H0) = (85-9sqrt5)/8.                                (11)

The inherited upward channel still increases energy by 2sqrt5-4.
Its sign does not determine (10), which includes the complete output.

## 4. Exact positive five-level account

This construction is a declared additive-conserving unitary dilation
on the complete S sector. It is not a spatially local implementation
of the original coherent contact channel.

Make the system account nonnegative by the fixed common shift

    H_S = H0+2sqrt5 I_S >= 0.                                   (12)

This shift changes no energy difference or stationarity statement.
Introduce five orthogonal battery states |b_E>, one for each distinct
unshifted system energy E, with

    H_B |b_E> = (2sqrt5-E)|b_E>.                                (13)

The levels, in increasing order, are

    0, 2sqrt5-4, 2sqrt5, 2sqrt5+4, 4sqrt5.                       (14)

Let Pi_E be the complete spectral projector of H0 on S and define the
isometry T:S -> S tensor C^5 by

    T psi = sum_E Pi_E psi tensor |b_E>.

Then T^*T=I_S. Every image component has total account
(E+2sqrt5)+(2sqrt5-E)=4sqrt5, so

    (H_S tensor I+I tensor H_B)T = 4sqrt5 T.                    (15)

In fact image(T) is precisely this full total-energy shell: each
available system energy has one and only one complementary battery
energy in (14). Write Q=TT^* for its projector.

For V_g restricted to S set

    W_g = T V_g T^* + (I-Q).                                   (16)

This is a unitary on the entire 80-dimensional carrier S tensor C^5:
its inverse/adjoint is T V_g^* T^*+(I-Q), the cross products vanish,
and either product is Q+(I-Q)=I. It preserves the shell and is identity
on its orthogonal complement. Hence

    [W_g,H_S tensor I+I tensor H_B]=0                           (17)

on the full carrier, including all unprepared battery levels.

The common battery readiness is

    |b_4>,  E_B,in = 2sqrt5-4.                                 (18)

Because the initial system vector a has energy4,

    a tensor |b_4> = T a,
    W_g(a tensor |b_4>)=T V_g a.                               (19)

Every energy branch balances exactly. In unshifted notation,

    E + E_B,out = 2sqrt5.

The full mean battery gain at g=2pi/5 is consequently

    Delta <H_B> = (5-sqrt5)/2.                                 (20)

Its initial energy is positive because the upward branch requires it,
even though the battery gains energy on average.

### Exact minimum in the frozen class

Assume the initial system energy is4, the battery initially has one
sharp energy b>=0, the battery spectrum is nonnegative, the complete
energy is additive and exactly conserved, and there is no additional
energy store. The initial total unshifted energy is 4+b.

For every nonzero output weight at system energy E, the final battery
must have an energy 4+b-E. For s>0 the five distinct E in the table
all occur. Therefore the battery needs at least five distinct energy
levels, independently of degeneracies. The largest E=2sqrt5 requires

    b >= 2sqrt5-4.                                             (21)

Equations (14),(18),(19) attain both lower bounds. These minima do
not apply to arbitrary non-sharp preparations or to changed target
distributions/accounts.

### Information and locality boundary

Tracing out the battery in (19) gives exactly

    rho_S,out = sum_E Pi_E |phi_g><phi_g| Pi_E,
    phi_g = V_g a.                                             (22)

Thus every energy probability is preserved, as is coherence inside
each degenerate energy block, but coherence between distinct energies
is absent from the reduced system. It survives only relationally in
the joint system/battery state. On inputs supported in the original
energy4 subspace, the same channel statement holds with arbitrary
correlated references, with Pi_E acting only on S.

The spectral projectors, invariant-sector encoding and battery
couplings are supplied. Their spatially local preparation/compilation
is not proved. This is a finite nonnegative account on a declared
extension, not a native-U bridge or laboratory apparatus.

## 5. Stationary complete sources cannot produce the pure target

The following elementary covariance fact is applied here; it is not
claimed as a new general theorem.

Let the complete source B, including controller, clocks and all
energy-bearing auxiliary systems, have Hamiltonian H_B and initial
state rho_B with

    [rho_B,H_B]=0.

For unbounded H_B the precise assumption is invariance under its
unitary time-translation group. Assume an initially uncorrelated
system eigenstate |a><a| and a unitary W with exact additive
conservation,

    W exp[-it(H_S+H_B)]
      = exp[-it(H_S+H_B)] W  for every real t.

The initial joint state is invariant under total time translation;
so is the final joint state. Taking the partial trace and using its
invariance under conjugation on B yields

    exp(-itH_S)rho_S,out exp(itH_S)=rho_S,out,
    [rho_S,out,H_S]=0.                                         (23)

No source-size bound is used.

For s>0 the pure target phi_g has five nonzero distinct-energy
components by the complete table. Hence |phi_g><phi_g| does not
commute with H_S. It cannot be the output (23).
The g in 2pi Z case has s=0 and is expressly excluded from this
obstruction.

### Sharp squared-fidelity ceiling

Write phi_E=Pi_E phi_g and w_E=||phi_E||^2. Every stationary output
rho has blocks rho_E=Pi_E rho Pi_E. Positivity gives

    <phi_g,rho phi_g>
       = sum_E <phi_E,rho_E phi_E>
       <= sum_E w_E Tr(rho_E)
       <= max_E w_E.

The first quantity is the squared fidelity with the pure target.
For the table and 0<=s<=1,

    max_E w_E = 1-3s/4.                                        (24)

It is attained over stationary states by the unchanged initial
system vector a: the target's E=4 component is parallel to a.
The identity implementation is an admissible stationary-source
realization of that maximizer. Thus the ceiling is sharp in the
unrestricted stationary-output comparison. It is not asserted sharp
when the full target energy distribution is also imposed.

At the nominated g=2pi/5,

    <phi_g,rho phi_g> <= (17+3sqrt5)/32 < 1.                     (25)

Testing the two-outcome projector {|phi_g><phi_g|, I-|phi_g><phi_g|}
gives the half trace-distance bound

    (1/2)||rho-|phi_g><phi_g|||_1
       >= 1-<phi_g,rho phi_g>
       >= 3s/4
       = (15-3sqrt5)/32  at g=2pi/5.                           (26)

No sharpness claim is made for (26). Increasing stationary energy
capacity or adding more stationary ancillary degrees of freedom does
not remove this fixed gap.

If the exact energy distribution w_E is ALSO required, the stronger
squared-fidelity bound is sum_E w_E^2 and is attained by (22).
The proof is the same with Tr(rho_E)=w_E. This refinement is a direct
analytical consequence of the same fixed contract.

    sum_E w_E^2 = 1-3s/2+23s^2/32
                = (409+77sqrt5)/1024 at g=2pi/5.                (27)

### Necessary energy spread for an exact pure target

An arbitrary initially independent source need not be stationary.
Suppose instead that it produces the exact pure system target under
the same additive conservation and has finite second energy moment.
The initial system energy is sharp, so the initial total variance is
Var(H_B,in). A pure system marginal forces the final joint state to
factor as |phi_g><phi_g| tensor rho_B,out, even if the source is mixed.
Exact conservation of the full energy distribution therefore gives

    Var(H_B,in) = Var(H_S,target)+Var(H_B,out)
                >= 29s-16s^2,
    Var(H_B,in) >= (85-9sqrt5)/8 at g=2pi/5.                    (28)

This is a necessary condition, not a sufficient coherence certificate.
A stationary mixed source can have arbitrarily large energy variance
while remaining excluded by (23)-(25). The source must also supply
the required coherence between different energies.

## 6. Energy account versus generator and clock

Let A_total=H_S+H_B in (15). It is constant, 4sqrt5, on the active
shell image(T). Its continuous exponential therefore acts there as
a common phase:

    exp(-it A_total) T psi = exp(-it4sqrt5) T psi.

For s>0, W_g changes a tensor |b_4> by the nontrivial law (19).
Consequently this bare additive account alone does not generate that
contact on the same clock. A continuous realization can introduce
an interaction/control generator; its energy, preparation, relation
to the clock and relation to the original step then need a separate
account. This observation does not rule out such a realization.

The conclusions are therefore precise:

- The complete contact has the negative mean sine-energy change (4).
- A five-level sharp battery balances its complete distribution,
  at the sharp ready-energy minimum within the frozen class.
- That stationary-source completion cannot reproduce the original
  coherent pure output. Additional energy coherence in the complete
  source, or a changed account/law/target, is required.
- Neither the availability of energy funding nor its mean direction
  selects omega rather than sin(omega) as physical energy.
- The inherited single-walk ratio 2/atan(2) at the specified common
  linear phase reading remains unchanged.

The present two-walk contact is a discriminator involving TWO
distinguishable already two-component objects. It does not say that
the two directional components of one electron are two particles.
No physical electron identification, actual force-response mass,
native realization, SI calibration or occurrence law is concluded.
