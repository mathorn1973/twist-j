# The actual capture law and its two receiver-parity transfers

**NON-CANONICAL. L1. Analytical candidate-T; C-HODGE-CAPTURE-PARITY-N.**

This is a new, explicitly marked arrangement reading of the complete active
contact channels of the homogeneous source. It is not the isolated pulse
transfer of #1716. The original source law, preparation, energy interval,
receiver and labels are retained. The sources and immutable input hashes are
listed in SOURCES.md. No source program is needed for the derivation.

## 1. Fixed source and boundary domain

Use the source of handoff #33 at
`0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`. Its two free arrangements are

~~~
U01 = exp(-i*beta) integral W(P) dP/(2*pi),
U02(K) = integral [W(P) tensor Vtilde(K-P)] dP/(2*pi),
g=2*pi/5, beta=4*pi/5, Vtilde=exp(-i*beta)*E*Q.
~~~

The first operator is independent of the total momentum K. The contact
vectors, with one label suppressed, are a=delta(u=0,r=0)*i*B_object and
b=delta(u=0,r=0)*A_object tensor eta, where

~~~
A_object=(e1-e4)/sqrt(2), B_object=(e2-e3)/sqrt(2), eta=e1.
~~~

The contact matrix on (a,b) is C=[[3/5,-4/5],[4/5,3/5]]. The full law is
U=U0*C. Define the COMPLETE normalized Caratheodory functions

~~~
F1(z)=<a,(z+U01)*(z-U01)^-1*a>,
F2(K,z)=<b,(z+U02(K))*(z-U02(K))^-1*b>,    |z|>1.
~~~

Their real parts are positive in the exterior disk and their values at
infinity are one. Every bound and continuum contribution, both pulse
branches, and both velocity signs belong in these functions. Selected
incoming or bound/right-going partial densities cannot replace them.

At an energy E use the exterior radial boundary z=R*exp(-i*E), R decreasing
to one. The regular domain consists of finite F1,F2 with r1=Re(F1)>0 and
r2=Re(F2)>0. All later equations concern this explicitly stated domain.
Since the source spectral measures are positive, rj=2*pi*rho_j for their
full absolutely continuous contact densities in the source convention.

For each arrangement and each retained label the spectral image of its
contact vector defines one normalized bright direction. The orthogonal
spectral directions are dark for the finite-rank contact. Reducing the
stationary scattering problem to these two directions is exact: all other
channels enter their full scalar spectral measures. It is not the assertion
that the entire scattering Hilbert space has dimension two.

## 2. Complete scattering matrix

Put m=diag((F1-1)/2,(F2-1)/2) and Kc=C-I. The source's stationary equation is

~~~
T=Kc*(I-m*Kc)^-1
 =(1/D)*[[-2*F2,-4],[4,-2*F1]],
D=4+F1*F2.
~~~

The exterior convention gives the bright scattering matrix
S=I+sqrt(Rho)*T*sqrt(Rho), where Rho=diag(r1,r2). This sign can also be checked
without choosing a phase from one entry: unitarity of I+Kc implies

~~~
Kc^-1+Kc^(-dagger)=-I,
T^-1+T^(-dagger)=-Rho,
T+T^dagger+T^dagger*Rho*T=0.
~~~

Thus S is unitary. Define

~~~
r=r1*r2, B=4*sqrt(r), A=4-conjugate(F1)*F2.
~~~

Direct expansion gives |D|^2-|A|^2=B^2>0, so D is nonzero on the regular
domain. All four scattering entries are

~~~
S=(1/D)*[[A,-B],[B,conjugate(A)]].
~~~

Its full bright transition probability is B^2/|D|^2. It is distinct from
the selected capture probability, whose numerator uses the partial incoming
continuum and outgoing bound/right-going densities. The latter is an
operational capture probability; the former normalizes this closed bright
unitary block.

The two scattering eigenphases may be written -arg(D) plus or minus theta,
where cos(theta)=Re(A)/|D|. The phase of T21 by itself is not this relative
phase. No later step inserts an independent rotation.

## 3. The actual receiver produces two different blocks

The source gives S_rec=Tplus*(S_full tensor I_memory)*Tminus^dagger.
On the token arrangement Tplus=Tminus=T1, a position-dependent label swap.
On the pulse arrangement their swaps act on opposite velocity signs. These
calibrations are commuting involutions, and

~~~
G=Tplus*Tminus=I_token direct-sum J_pulse,
S_rec=Tminus*[G*(S_full tensor I_memory)]*Tminus.
~~~

This is one common source-derived unitary conjugation on the complete channel
space. Tminus can mix original K labels on the token arrangement. The present
reading is defined AFTER this displayed calibration; it does not assert that
the physical receiver scattering is diagonal in that original uncalibrated
K chart. This is a material part of the declared reading.

The label swap J on C^26 tensor C^26 has dimensions 351 and 325 in its plus
and minus eigenspaces. In the calibrated chart the two active scattering
blocks are S_plus=S and S_minus=diag(1,-1)*S. The dark part remains a
separately defined scattering relation with singular cross-arrangement
transmission. No arbitrary inverse is supplied on that part.

## 4. One fixed arrangement regrouping

For every scalar block S=[[u,v],[w,z]] regroup the same ports by solving the
first outgoing equation for its second incoming amplitude. The result is

~~~
M=[[w-z*v^-1*u,z*v^-1],[-v^-1*u,v^-1]].
~~~

The inverse exists here because v=-B/D is nonzero. Applying this same
regrouping to both receiver blocks gives

~~~
M_plus =(1/B)*[[conjugate(D),-conjugate(A)],[A,-D]],
M_minus=diag(-1,1)*M_plus.
~~~

Both preserve the SAME current Sigma=diag(1,-1). Their exact invariants are

~~~
det(M_plus)=-1,         tr(M_plus)=-2i*Im(D)/B,
det(M_minus)=1,         tr(M_minus)=-2*Re(D)/B.
~~~

Consequently the complete bright amplitude transfer, with every label, is
(M_plus tensor I_351) direct-sum (M_minus tensor I_325). It is not a common
matrix tensored with J. The fixed-factor receiver obstruction in #1716
therefore does not decide this full-capture reading.

The port regrouping is an arrangement transfer derived from the stationary
scattering relation. It has not been derived as transfer through a specified
physical spatial cut of the whole capture circuit. A new spatial-cut law
would require its own external ports, eliminations, current and regularity
analysis. This distinction bounds every theorem in this note.

## 5. Exact action conditions and natural form

For either two-port matrix M, the Hermitian congruence R_M(X)=M*X*M^dagger
has characteristic polynomial

~~~
(x-1)^2*(x^2-kappa*x+1),   kappa=|tr(M)|^2-2.
~~~

The current gives a fixed direction Sigma^-1, and the determinant phase can
be removed to reduce the remaining classification to SU(1,1). Thus

~~~
kappa_plus =(Im D)^2/(4*r)-2,
kappa_minus=(Re D)^2/(4*r)-2.
~~~

PROOF_WINDOW.md treats the entire Hermitian carrier, including cross-parity
coherences, and proves that any invariant four-dimensional linear subquotient
carrying the full Hodge action requires the unordered pair {3,phi}. At such
a match one necessarily has

~~~
B^2/|D|^2 = 4/(7+phi).
~~~

This single probability equality is necessary, not sufficient: it forgets
the separate real and imaginary parts of D. Nor does it identify the source
packet's selected capture probability with this value.

PROOF_METRIC.md selects and evaluates the natural invariant quadratic form
Q_H(X,Y)=-(1/2)*tr(H*X*H*Y), H=Sigma tensor I_labels. Its moving-plane
restriction has real Lorentz signature when one parity is hyperbolic and the
other elliptic. Conservation of H does not uniquely declare this quadratic
form to be physical spacetime geometry. The fixed target beta, arithmetic
field, label weights and integral lattice must still be accounted for.

The exact analytic window obstruction comes before the form equation. It
uses the source's nonconstant first moment, not a fitted phase, a radial
approximation, a changed packet or an assumed arithmetic boundary field.
