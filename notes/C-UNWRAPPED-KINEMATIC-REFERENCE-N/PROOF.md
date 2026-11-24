# Unwrapped kinematics, clock contracts and an integer block comparison

Author: A. M. Thorn
Date: 2026-10-30
Candidate: C-UNWRAPPED-KINEMATIC-REFERENCE-N
Status: NON-CANONICAL / analytical candidate-T, subject to independent review.
Scope: L1 state/operator mathematics of an explicitly declared reference model.
There is no native-U realization, physical-admission claim or L1-L6 lift.

## 0. Purpose and attribution

The purpose is one consistent reference against which a proposed discrete
model can be tested. It is not a new derivation of special relativity.
Positive-energy relativistic position belongs to the established
Newton-Wigner literature: T. D. Newton and E. P. Wigner, Localized States for
Elementary Systems, Reviews of Modern Physics 21, 400 (1949),
DOI 10.1103/RevModPhys.21.400.

The reference distinguishes canonical position, rapidity translation,
finite momentum impulse, mass identification, clock preparation and
locality. Its integer appendix strengthens an exposed characteristic-
polynomial comparison to an explicit unimodular conjugacy.
No global novelty claim is made for any part.

Public basis: mathorn1973/twist-j main
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`, Public Canon v106.
The existing BOOST-READING-SPLIT and BOOST-COUNT-LADDER have their own
registered scopes. The existing phase-energy analysis in issue #1603 /
PR #1605 already separates phase energy, sine energy, momentum and position.
This note does not take ownership of that lane or any physical clock owner.

The public CORE explicitly permits constructive models with declared
sources and readings; derivation from original U and global reading
uniqueness are not requirements for proving a declared construction.
They must not be imposed as invented prerequisites here. Conversely,
existence of this comparison model does not establish a native bridge.

## 1. Carrier, domains and position

Assume m>0 and hbar=c=1. On H_m=L2(R,deta), let

    E_m=H_m=m cosh(eta),  P_m=m sinh(eta),  K=i d/deta,
    v=tanh(eta), q=sech(eta),
    X_m={E_m^-1,K}/2
       =i/E_m d/deta-i P_m/(2 E_m^2).

The same symbol H_m for a Hilbert space and an energy operator is avoided
below: the space is denoted script-H_m and the operator by E_m.
Multiplication operators use their maximal domains. K has domain H1(R).
Commutator identities are initially on C_c^infinity(R).

Define the unitary identification with canonical momentum by

    (A_m psi)(p)=psi(asinh(p/m))/sqrt(E_m(p)),
    E_m(p)=sqrt(m^2+p^2),  dp=E_m deta.

Then

    A_m P_m A_m^-1=p,
    A_m X_m A_m^-1=i d/dp.

These equations also define the self-adjoint closure and domain of X_m.
In particular its domain is A_m^-1 H1(R,dp). They are not just formal
integration-by-parts assertions.

### Proposition 1 [analytical candidate-T]

On the stated common core,

    [K,E_m]=iP_m, [K,P_m]=iE_m, [E_m,P_m]=0,
    [X_m,P_m]=i, i[E_m,X_m]=P_m/E_m.

Moreover, on the position domain,

    exp(it E_m) X_m exp(-it E_m)=X_m+t P_m/E_m.

Proof. The first three identities are differentiation. In momentum
coordinates X=i d/dp, so the other identities follow from
E'(p)=p/E(p). This derivative is bounded, which also preserves the
position domain under the phase multiplication. K and X are different
operators. The former translates rapidity; the latter translates momentum.

## 2. Finite momentum impulse

### Proposition 2 [analytical candidate-T]

Let J_delta=exp(i delta X_m). With

    f_delta(eta)=asinh(sinh(eta)-delta/m),

its action is

    (J_delta psi)(eta)
      =sqrt(cosh(eta)/cosh(f_delta(eta))) psi(f_delta(eta)).

It is unitary, J_delta^* P_m J_delta=P_m+delta, and

    d/d(delta) [J_delta^* v J_delta] at delta=0
      =m^2/E_m^3=q^3/m.

Proof. In the p representation J_delta is the translation f(p)->f(p-delta).
Pulling it back by A_m gives the displayed square root of the Jacobian.
Conjugating multiplication by p gives p+delta. Differentiating
(p+delta)/sqrt(m^2+(p+delta)^2) gives the response.

A finite-difference numerical approximation is not an exact test of this
identity. At p=0 its centered difference equals 1/sqrt(m^2+delta^2),
not 1/m. For m=2 and delta=1/10000 the truncation error alone exceeds
1/10^10. That rejects the submitted numerical tolerance, not the identity.

## 3. Mass transport at fixed canonical (X,P)

Put

    D={v,K}/2=i(v d/deta+q^2/2).

The expression in eta is independent of m. In canonical momentum
coordinates A_m D A_m^-1=i(p d/dp+1/2), the self-adjoint dilation generator.
Its complete unitary flow gives the self-adjoint realization of D.

### Proposition 3 [analytical candidate-T]

For tau=log(m2/m1), set W(m2,m1)=exp(-i tau D). Then

    f_tau(eta)=asinh(exp(tau) sinh(eta)),
    (W psi)(eta)
      =sqrt(exp(tau) cosh(eta)/cosh(f_tau(eta))) psi(f_tau(eta)).

It equals A_m2^-1 A_m1. Thus

    W^* P_m2 W=P_m1,   W^* X_m2 W=X_m1,
    W(m3,m2)W(m2,m1)=W(m3,m1).

The associated covariant parameter derivative is

    nabla_m O_m=partial_m O_m+(i/m)[D,O_m],

and

    nabla_m E_m=m/E_m=q,
    nabla_m P_m=0, nabla_m X_m=0.

Proof. At a final rapidity eta, the same physical p=m2 sinh(eta)
had initial rapidity asinh((m2/m1)sinh(eta)). The ratio of the
momentum-density normalization factors is exactly the stated Jacobian.
Differentiation gives [D,E_m]=iP_m^2/E_m, [D,P_m]=iP_m and
[D,X_m]=-iX_m. Together with the fixed-eta derivatives these prove
all three covariant identities.

The submitted minus-flow f=asinh(exp(-tau)sinh(eta)) with the prefactor
sqrt(cosh(eta)/(cosh(tau)cosh(f))) is not this W. Change of variables gives

    ||W_wrong psi||^2=exp(tau)/cosh(tau) ||psi||^2.

At exp(tau)=2 the factor is exactly 8/5. This is an exact counterexample
to that formula, not a quadrature artifact.

## 4. Spinor frame [analytical candidate-T]

Pauli matrices are denoted sigma_x and sigma_z, never by the position X.
For r=exp(eta)>0 put

    S_r=((r,-1),(1,r)), G_r=I/(1+r^2),
    H_D=P_m sigma_z+m sigma_x.

Direct multiplication proves

    S_r^* G_r S_r=I,
    H_D S_r=S_r diag(E_m,-E_m),
    T(r',r)^* G_r' T(r',r)=G_r,
    T(r',r)=S_r' S_r^-1.

For u_+=S_r (1,0)^T,

    u_+^* G_r sigma_z u_+=(r^2-1)/(r^2+1)=v,
    u_+^* G_r sigma_x u_+=2r/(r^2+1)=q.

These identities hold over the reals for arbitrary r,r'>0. Only at
eta=n log(phi), eta'=n' log(phi) do we claim r,r' in Z[phi] and
T,G in Q(sqrt(5)). No such arithmetic-field claim is made for arbitrary
continuous eta. The frame identity is not a physical spin identification.

## 5. Two different clock contracts

### 5.1 Common rapidity and comoving read [analytical candidate-T]

Let m1,m2>0, delta_m=m2-m1. Identify the two mass spaces by the SAME
rapidity coordinate, prepare normalized f(eta)(|1>+|2>)/sqrt(2),
and use the explicitly declared common comoving generator

    G0=diag(E_m1-v0 P_m1, E_m2-v0 P_m2),
    v0=tanh(eta0), q0=sech(eta0).

Read I_eta tensor sigma_x. This is a named mathematical reading; it is
not asserted to be a spatially local detector in canonical x.

The exact difference of the two diagonal generators is

    delta_m [cosh(eta)-v0 sinh(eta)]
      =delta_m q0 cosh(eta-eta0).

Consequently

    C_t(eta0)=integral |f(eta)|^2
                    cos(delta_m q0 t cosh(eta-eta0)) deta.

If the displayed cosh moment is finite, the nonperturbative bound is

    |C_t(eta0)-cos(delta_m q0 t)|
      <= |delta_m| q0 |t| <cosh(eta-eta0)-1>
       = 2 |delta_m| q0 |t| <sinh^2((eta-eta0)/2)>.

Proof. The hyperbolic addition identity proves the generator difference.
The internal cross term gives C_t. Apply |cos(a)-cos(b)|<=|a-b| under
the integral. No small delta_m approximation is used.

Thus the previously supplied clock phase is not an arbitrary invented
profile. It has this exact named realization. What it does NOT supply
without further work is a local finite-packet preparation and detector
contract, nor a native realization. A delta-localized rapidity is a formal
central-rate reference, not a normalized state in L2.

At the central rapidity the related plane-wave phase identity is

    p_j=m_j sinh(eta0), E_j=m_j cosh(eta0),
    delta E-v0 delta p=delta_m q0.

It explains why dropping the spatial phase while following a moving
clock gives the wrong comparison. Finite spatial packets require their
own complete readout and packet-error theorem.

### 5.2 Common canonical momentum [analytical candidate-T]

If instead the two masses are identified at the SAME p, the exact energy
difference is

    delta E(p)=sqrt(m2^2+p^2)-sqrt(m1^2+p^2).

Generally it is not delta_m times one preselected q. For m2>m1,

    0 <= delta E(p)-delta_m m1/sqrt(m1^2+p^2)
       <= delta_m^2 p^2 / [2(m1^2+p^2)^(3/2)].

Proof. Integrate dE/dm=m/sqrt(m^2+p^2), whose derivative is
p^2/(m^2+p^2)^(3/2), nonnegative and decreasing for m>0.

Both clock contracts are valid reference constructions. They are not the
same preparation or the same mass-space identification. A result about
one is not a falsification of the other.

## 6. Cell charts and locality [analytical candidate-T]

Let h=log(phi)>0, alpha=h/(2pi), eta=nh+alpha k,
n in Z and -pi<=k<pi. The Hilbert space becomes the direct sum of cell
L2 spaces with measure alpha dk. The domain of K must satisfy

    psi_n(pi)=psi_(n+1)(-pi)

in the trace sense, together with square-integrable weak derivatives.
This is the image of H1(R), not independently periodic cell domains.
The global operator X_tilde=i d/dk=alpha K has continuous real spectrum.
Shifted integer spectra arise only after a further fiber decomposition;
they are not a discrete spectrum of the full unwrapped operator.

On a fixed cell,

    E_n(k)=m cosh(nh+alpha k).

For each fixed n this is bounded on the cell. Its ordinary cell Fourier
coefficients, with convention Ehat_n(l)=(1/(2pi)) integral E_n(k)e^(-ilk)dk,
are

    Ehat_n(l)=m (-1)^l sinh(h/2)/pi
               * [alpha cosh(nh)+i l sinh(nh)]/(alpha^2+l^2).

Proof. Integrate exp((alpha-il)k) and exp((-alpha-il)k) on [-pi,pi].
The integer Fourier endpoints give exp(+-i pi l)=(-1)^l.

For n=0 the nonzero coefficients decay as |l|^-2; for n!=0 they decay
as |l|^-1. Every fixed cell therefore has infinite Fourier range.
Gluing rapidity across adjacent cells does not make this matrix a finite
Fourier polynomial. Small alpha does not remove an endpoint mismatch.
This statement is specific to the declared cell Fourier basis. It is
not a theorem excluding every enlarged-carrier finite-range step.

A smooth periodic scalar map cannot have positive derivative everywhere:
the integral of its derivative over a period is zero. A positive slope
somewhere requires a negative slope elsewhere. This does not force the
negative slope to lie at +-pi, nor a third- or fourth-order defect at zero.
Smooth periodic maps can agree exactly with a linear map near zero.

## 7. Exact integer block comparison [analytical candidate-T]

Use j^4+j^3+j^2+j+1=0, J=1+j^2 and phi=-j^2-j^3.
Let M be multiplication by J in the ordered basis (1,j,j^2,j^3):

    M=((1,0,-1,1),
       (0,1,-1,0),
       (1,0, 0,0),
       (0,1,-1,1)).

Fix the Fibonacci convention

    F=((0,1),(1,1)), F^-1=((-1,1),(1,0)),
    B=diag(F,F^-1).

Put

    Q=((1,1,0,1),
       (0,0,1,1),
       (0,1,0,1),
       (0,1,0,0)),

    Q^-1=((1,0,-1, 0),
          (0,0, 0, 1),
          (0,1,-1, 1),
          (0,0, 1,-1)).

Then det(Q)=1 and

    Q^-1 M^5 Q=diag(-F^5,F^-5),
    Q^-1 M^10 Q=B^10.

More generally for every integer r,

    Q^-1 M^(5r) Q=diag((-1)^r F^(5r),F^(-5r)).

### Proof without matrix enumeration

The columns of Q represent the ordered basis

    (1, phi', j, j phi),  phi'=1-phi=-phi^-1.

It is an integral basis because the displayed Q has an integer inverse.
Both phi and phi' satisfy x^2-x-1=0, whose multiplication matrix in
(1,x) is F. The registered identity J phi=j implies J^5=phi^-5.
On the first two basis elements multiplication by phi^-5 is
multiplication by -(phi')^5, hence -F^5. On the second pair it is F^-5.
This proves the fifth-power formula and all its integer powers.

### Exact obstruction at other block lengths

For positive N, M^N and B^N are similar over C if and only if 10 divides N.

Indeed, the eigenvalues of M have arguments +-2pi/5 and +-pi/5,
with moduli phi^-1 and phi respectively. Unless 5 divides N, M^N has
nonreal eigenvalues, whereas every eigenvalue of B^N is real. If N is
an odd multiple of five, M^N has the two eigenvalues phi^-N and -phi^N,
each twice; B^N has the four distinct values +-phi^N and +-phi^-N.
For multiples of ten the integral conjugacy above proves similarity.

In particular the common characteristic polynomial at ten is

    (x^2-123x+1)^2=x^4-246x^3+15131x^2-246x+1.

The alternative Fibonacci convention ((1,1),(1,0)) is obtained by
swapping the two coordinates of each block; replacing Q by
Q diag(R,R), R=((0,1),(1,0)), gives the corresponding statement.

This is stronger than equal characteristic polynomials: it identifies
entire Z^4 lattice maps after blocks of ten. It does not identify the
one-step maps or the nine intermediate states. It gives no unitary
identification for an arbitrarily chosen positive metric, no comparison
with original nonlinear U, no contact, and no proper-time realization.
Q is not identified with an unspecified earlier lattice gate L.

## 8. Disposition

The reference is suitable for a notes-only proposal after independent
review. Standard relativistic reference facts must remain identified as
such. The useful content is the consistent contract, explicit corrections,
locality boundary and the exact integer comparison, not a claim to have
derived all physics from J.

The accompanying program audits finitely many exact arithmetic fixtures.
It does not prove analytic self-adjointness, cosine inequalities or all-N
minimality by finite enumeration. No cross-architecture or independent
confirmation is supplied by this local package, and no Canon promotion
or alteration of an existing public falsifier is proposed.
