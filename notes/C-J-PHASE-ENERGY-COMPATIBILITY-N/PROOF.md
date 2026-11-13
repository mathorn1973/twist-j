# Two exact compatibility tests

PUBLIC / NON-CANONICAL / L1. Authored conditional candidate-T only.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
The sources, domain and exposed hypotheses are frozen in PREREG.md.
These are two different constructions, not one jointly admitted machine.

## A. Can the existing area scalar be an energy clock?

### A1. Necessary and sufficient cycle condition

Let T be a permutation of a finite set X, E:X->F5 invariant under T,
and a:X->F5. Fix kappa,beta in F5. There exists chi:X->F5 such that

    a(x)=kappa E(x)+beta+chi(Tx)-chi(x)                       (1)

if and only if every complete orbit C satisfies

    sum_(x in C) a(x)=|C|(kappa E(C)+beta).                  (2)

Necessity follows by summing (1): each chi value cancels once. Conversely,
choose one root x0 on each disjoint orbit, set chi(x0)=0, and define
chi(Tx)=chi(x)+a(x)-kappa E(x)-beta successively. The only consistency
condition is the return to x0, exactly (2). This also proves the criterion
on a disjoint union of finite orbits, with independent root constants.
This elementary criterion is not claimed as a new general theorem.

### A2. Application to the complete funded-area state

For every accepted Q, Delta p=Delta u=Delta v=0. For every accepted P_h,
Delta p=h and Delta u=Delta v=hq. A rejection changes none of these
coordinates. Thus, over the integers on EVERY actual step,

    a=q Delta p=Delta u=Delta v.                            (3)

Consequently every complete return has sum a=0, and chi=u modulo five
solves (1) with kappa=beta=0. Finite energy shells are finite because
each integer square and the nonnegative bank are bounded by E. T is a
permutation: for each elementary map, an accepted candidate is undone by
the opposite requested sign; a rejected step flips sigma, and the inverse
request then attempts the same unaffordable candidate and flips back.
The controller inverse first decrements c. Hence all complete orbits are
finite. This uses the stated funded-map definitions, not a native-U claim.

There can be no other universal pair. Consider

    x0=(0,0,0,0,0,1,1,0), E=0;
    x1=(0,0,1,0,0,1,1,0), E=1.

At both states and every subsequent step, q=p=b=0. Every Q or P trial
would increase H by one, so every step rejects. Sigma flips and c advances.
Each complete orbit has exact length four, because c cannot return sooner;
its area sum is zero. Equation (2) therefore gives 4 beta=0 and
4(kappa+beta)=0 in F5. Since 4 is invertible, beta=kappa=0.

Thus the existing area scalar on this WHOLE complete carrier cannot be
gauge-equivalent to a nontrivial affine clock of its full energy modulo five.
This remains true for any faithful fifth-root character j^(r a), r!=0:
the scalar is then the difference of r u, and the same zero-sum witnesses
force kappa=beta=0.

The usual cold B=0 preparation has E=2 and the same four rejected steps.
It alone excludes nonzero kappa if beta is fixed to zero. If beta is free,
it imposes only beta=-2 kappa. The two cold-orbit audit in PREREG.md is a
separate finite check, not required for the whole-carrier proof above.

### A3. What this does and does not close

Formally on basis vectors, define V|s>=j^a(s)|Ts> and G|s>=j^u(s)|s>.
Equation (3) yields V=G P G^-1, where P|s>=|Ts> is the bare permutation.
This is a statement about the defined scalar-weighted permutation.
It does NOT identify V with the source's full open-path Weyl word.

A base loop returning q,p can still have nonzero area because its final
record coordinates u,v differ. Its nontrivial spatial Weyl holonomy is
fully compatible with (3). The obstruction concerns full-state cycles and
the particular total energy account. Over U(1), the same four-step witnesses
would permit sampling aliases; the F5 conclusion is not a no-go for every
continuous phase or Hamiltonian. A different phase generator, energy reader,
prepared invariant class or clock must be independently justified.

## B. Does the Dirac eigenphase give the same rest and curvature mass?

### B1. Declared comparison and dispersion

The canonical algebraic step is D_m(k)=S(k)(I+i m X), where
S=diag(exp(ik),exp(-ik)) and X exchanges the two components. Introduce
W_m=D_m/r, r=sqrt(1+m^2), for m>0. This complete normalized Fourier family
is a comparison construction; it is not asserted to be the native U.

Since (I-i m X)(I+i m X)=(1+m^2)I, W_m is unitary. Its determinant is
one and its trace is 2 cos(k)/r. Its eigenvalues are exp(+/-i omega),
where the smooth principal positive band is

    cos(omega(k))=cos(k)/r,  0<omega(k)<pi.                 (4)

At k=0, omega0=atan(m). Differentiating (4) once and twice gives

    sin(omega) omega'=sin(k)/r,
    cos(omega)(omega')^2+sin(omega) omega''=cos(k)/r.

Thus omega'(0)=0 and omega''(0)=1/m, since sin(omega0)=m/r.

### B2. Literal temporal and spatial phase readings

Fix common A,B>0 and set E_phase=A omega and p_phase=B k. The massless
branch near zero has omega=|k|, so the limiting speed read in these units
is c=A/B. Define, without claiming a force experiment,

    M_curv = 1/(d^2 E_phase/d p_phase^2 at p_phase=0).

Then

    M_curv=B^2 m/A=A m/c^2,
    E_phase(0)/c^2=A atan(m)/c^2,
    M_curv c^2 / E_phase(0)=m/atan(m)>1.                   (5)

The strict inequality follows from
atan(m)=integral_0^m dt/(1+t^2)<m for m>0. Common changes of A,B cannot
change the dimensionless ratio. For the declared algebraic rung m=2 the
two readings are proportional to 2 and atan(2), respectively. This is
not a prediction of a measured electron-mass discrepancy, because the
normalization, clock and physical readings are not yet admitted.

The principal-band scope is sufficient for (5). Even adding 2 pi n to
omega0 does not repair the m=2 equality: atan(2) is between zero and pi/2
and below 2, while for n>=1 the shifted value exceeds 2, and for n<=-1 it
is negative. A separately fitted energy zero for each m is outside the
common literal reading. The declared convention E_phase=A omega sets
E_massless(0)=0 and excludes a universal additive offset; the massless
speed by itself fixes only A/B, not the energy zero.

### B3. A positive exact shell and drift relation

The algebraic readings associated with the existing shell are

    Ehat=r sin(omega)=sqrt(m^2+sin(k)^2),  phat=sin(k).

Therefore

    Ehat^2-phat^2=m^2,
    omega'(k)=phat/Ehat=d sqrt(m^2+phat^2)/d phat.          (6)

The first equality is the inherited algebraic shell in this parametrization;
the second follows from the first derivative of (4). Locally where cos(k)
is nonzero, phat is a valid coordinate and the last derivative is the
energy derivative in that coordinate. At turning points the shell formula
still defines that derivative, but k->phat is not a local coordinate chart.

Thus the shell and the actual phase group drift agree exactly as dimensionless
functions. But Ehat is not proportional to omega, and phat is not proportional
to k. Equality of these two velocities does not prove the de Broglie reading
or a canonical position-momentum bracket for phat.

There is also a global loss of phase: k and pi-k give identical (Ehat,phat),
but omega(pi-k)=pi-omega(k). At k=0 and k=pi both readings are (m,0),
while the phases are atan(m) and pi-atan(m), which differ for finite m>0.
A declared local band restriction avoids this particular degeneracy but
does not remove the principal-band discrepancy (5).

### B4. A controlled positive weak-step limit

For the separately declared family m=epsilon M with epsilon,M>0,

    M-atan(epsilon M)/epsilon
      = (1/epsilon) integral_0^(epsilon M) t^2/(1+t^2) dt.

On that interval, 1/(1+epsilon^2 M^2)<=1/(1+t^2)<=1. Hence

    epsilon^2 M^3/[3(1+epsilon^2 M^2)]
      <= M-atan(epsilon M)/epsilon <= epsilon^2 M^3/3.     (7)

So the normalized rest frequency tends to M as epsilon tends to zero.
With k=epsilon K and time step proportional to epsilon, a continuum route
is suggested, but (7) proves only the stated rest limit and error bound.
It neither constructs that scale family from the native machine nor turns
the fixed rung m=2 into a small parameter by changing units.

## Research consequence

The positive pieces are exact: a constructive cycle criterion and a Dirac
shell matching phase group drift. The missing junction is equally exact:
the area record is not the proposed energy clock on its whole carrier,
and the literal Dirac frequency gives a different rest mass from dispersion
curvature at finite m. Closing the proposed interpretation requires one
admitted dynamics and clock for which phase frequency, energy reading and
inertial response agree. These conditional results select that obligation;
they do not refute the broader TWIST-J program or derive hbar.
