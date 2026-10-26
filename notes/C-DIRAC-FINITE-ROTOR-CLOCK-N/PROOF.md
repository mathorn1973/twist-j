# A finite positive autonomous rotor clock for the nominated four-channel walk

**NON-CANONICAL, L1, conditional analytical candidate-T. Independent
mathematical acceptance pending.**

Author: A. M. Thorn. License: Apache-2.0.

This note gives a self-contained analytical construction. For each prescribed
finite horizon and error tolerance, it supplies one finite clock, one positive
bounded time-independent Hamiltonian, and one ready clock state. At every
specified tick within that horizon, their joint evolution approximates the
complete nominated walk on every system input, including inputs entangled with
an arbitrary passive reference. The clock approximately returns to the same
ready state in the joint-state comparison.

Spatial locality means range one in the single-particle position coordinate
defined below. No spatial cutoff is imposed. The clock dimension is finite;
the position Hilbert space remains the full infinite lattice.

This is a finite-horizon approximation theorem. Exact clock reset, exact
implementation at finite resources, and a bound uniform over arbitrarily many
ticks at fixed resources are not conclusions.

## 0. Provenance and dependency boundary

The authority context is
[Public Canon v105 at main 892a0b11089d34e241e1eb76d2c03247022d18e6](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
Related non-canonical predecessors are
[#1768, FINITE_MODEL.md at 811daddc3b2f085ee5bc6f50261ac95a4c11fe44](https://github.com/mathorn1973/twist-j/blob/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/FINITE_MODEL.md)
and
[#1779, COMPACT_MODEL.md at c2b06d3ee52778f804da1f84ba9f963bae1ad46e](https://github.com/mathorn1973/twist-j/blob/c2b06d3ee52778f804da1f84ba9f963bae1ad46e/notes/C-COMPACT-ENERGY-RECORD-N/COMPACT_MODEL.md).
These links identify prior finite-clock and autonomous-record work. They are
provenance references, not proof dependencies. The nominated walk, the input
contract, and every estimate used here are defined and proved in this note.

The construction does not assume a previous obstruction theorem or an
identification of its Hamiltonian with another nominated energy observable.
It makes no change to the public Canon.

Throughout, set the action unit to one. Thus a Hamiltonian has units of inverse
time. All error bounds below are analytic; no numerical or executable
scientific calculation is used.

## 1. Complete nominated system and target step

Let the system Hilbert space be

$$
\mathcal H_S
=\ell^2(\mathbb Z)\otimes\mathbb C^2_{\rm dir}
 \otimes\mathbb C^2_{\rm port}.
\tag{FRC-01}
$$

On the position factor, let \(T|x\rangle=|x+1\rangle\). On the direction
factor use a fixed ordered basis and the Pauli matrix \(X_{\rm dir}\).
Define the conditional shift, extended by the port identity, by

$$
S=
\begin{pmatrix}T&0\\0&T^\dagger\end{pmatrix}_{\rm dir}
\otimes I_{\rm port}.
\tag{FRC-02}
$$

On the port factor set

$$
R=X_{\rm port},\qquad
P_\pm=\frac{I_{\rm port}\pm R}{2},\qquad
Z_{\rm port}=
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\theta=\arctan 2 .
\tag{FRC-03}
$$

Identity factors will be suppressed when their placement is unambiguous.
In particular, \(P_\pm\) also denote their extensions to \(\mathcal H_S\).
Define the onsite coin and the free four-channel step by

$$
C=\exp\!\left(i\theta X_{\rm dir}P_-\right),
\qquad
\mathcal U=SC.
\tag{FRC-04}
$$

Equivalently, if

$$
U_\mu=
\begin{pmatrix}T&0\\0&T^\dagger\end{pmatrix}_{\rm dir}
\frac{I_{\rm dir}+i\mu X_{\rm dir}}{\sqrt{1+\mu^2}},
\tag{FRC-05}
$$

then

$$
\mathcal U=U_0\otimes P_++U_2\otimes P_-.
\tag{FRC-06}
$$

This follows from \(\cos\theta=1/\sqrt5\) and
\(\sin\theta=2/\sqrt5\). Formula (FRC-06) nominates one fixed unitary on the
complete four-channel carrier.

Let the spatial contact be at the origin. For any fixed real \(g\), put

$$
Q_{\rm site}=|0\rangle\langle0|\otimes I_{\rm dir}\otimes I_{\rm port},
\qquad
Z=I_{\rm pos}\otimes I_{\rm dir}\otimes Z_{\rm port},
\qquad
C_g=\exp(-igQ_{\rm site}Z),
\qquad
V=C_g\mathcal U .
\tag{FRC-07}
$$

The target of the theorem is \(V^n\) on all of \(\mathcal H_S\). In
particular, the input need not have finite spatial support, a nominated
momentum, a selected port parity, or a selected direction state.

An operator has spatial range at most \(r\) if its position matrix element
between \(x\) and \(y\) vanishes whenever \(|x-y|>r\), with all its internal
factors retained in that matrix element. The onsite operators above have
range zero; \(S\), \(\mathcal U\), and \(V\) have range at most one.

## 2. Three bounded local pulse generators

Let

$$
J=I_{\rm pos}\otimes X_{\rm dir}\otimes I_{\rm port},
\qquad
B=SJ.
\tag{FRC-08}
$$

Because \(JSJ=S^\dagger\), the operators \(J\) and \(B\) are self-adjoint
involutions, and \(BJ=S\). For either involution \(F\),

$$
\exp\!\left[-i\frac{\pi}{2}(I-F)\right]=F.
\tag{FRC-09}
$$

Define three complete bounded self-adjoint generators on \(\mathcal H_S\):

$$
\begin{aligned}
K_{\rm on}&=\frac{\pi}{2}(I-J)-\theta JP_-,\\
K_{\rm link}&=\frac{\pi}{2}(I-B),\\
K_{\rm contact}&=gQ_{\rm site}Z.
\end{aligned}
\tag{FRC-10}
$$

The two terms of \(K_{\rm on}\) commute. Consequently,

$$
e^{-iK_{\rm on}}=JC,\qquad
e^{-iK_{\rm link}}=B,\qquad
e^{-iK_{\rm contact}}=C_g,
\qquad
e^{-iK_{\rm contact}}e^{-iK_{\rm link}}e^{-iK_{\rm on}}=V.
\tag{FRC-11}
$$

Thus the chronological pulse order is onsite, link, contact. The first
and third generators are onsite; the link generator has spatial range one.
All three are defined on the entire system space, not only on an input code.

The onsite eigenvalues are \(0,\pi,-\theta,\pi+\theta\).
Also, \(\|K_{\rm link}\|=\pi\) and
\(\|K_{\rm contact}\|=|g|\). Hence

$$
\kappa=\max(\pi+\theta,|g|)
=\max\bigl(\|K_{\rm on}\|,\|K_{\rm link}\|,
                 \|K_{\rm contact}\|\bigr).
\tag{FRC-12}
$$

## 3. A periodic local program with an idle interval

Fix the desired tick period \(\tau>0\), and set \(d=\tau/5\).
For \(j=1,2,3\), define a real periodic pulse envelope on the clock circle:

$$
a_j(\phi)=
\begin{cases}
\displaystyle\frac2d\sin^2\!\left(\frac{\pi(\phi-jd)}d\right),
   & jd\le\phi\le(j+1)d,\\[4pt]
0,&\text{otherwise in }[0,\tau).
\end{cases}
\tag{FRC-13}
$$

Define the bounded Hermitian program

$$
A(\phi)
=a_1(\phi)K_{\rm on}
 +a_2(\phi)K_{\rm link}
 +a_3(\phi)K_{\rm contact}.
\tag{FRC-14}
$$

Each envelope and its first derivative vanish at its endpoints. Therefore
\(A\) is a periodic \(C^1\) operator-valued function. Its supports are
disjoint apart from endpoints where the envelopes vanish. Moreover,

$$
\int_0^\tau a_j(\phi)\,d\phi=1,\qquad
\|a_j\|_\infty=\frac2d,\qquad
\|a_j'\|_\infty=\frac{2\pi}{d^2}.
\tag{FRC-15}
$$

It follows that

$$
h:=\sup_\phi\|A(\phi)\|=\frac{10\kappa}{\tau},
\qquad
h_1:=\sup_\phi\|A'(\phi)\|=\frac{50\pi\kappa}{\tau^2}.
\tag{FRC-16}
$$

The program vanishes on the first and last open fifths of the circle.
Let \(I=(0,d)\) be the ready interval. If \(F(b,a)\) denotes the
chronologically ordered unitary propagator of \(A\) from \(a\) to \(b\),
then (FRC-11) and (FRC-15) give

$$
F(\tau,0)=V.
\tag{FRC-17}
$$

The pulse envelopes are used to define one static clock-coordinate
dependent interaction. They are not externally timed controls during the
autonomous evolution constructed below.

## 4. Auxiliary exact circle suspension and its domains

Let

$$
\mathcal H_C=L^2(\mathbb R/\tau\mathbb Z,d\phi),
\qquad
P=-i\partial_\phi,
\qquad
D=P+A(\phi)
\tag{FRC-18}
$$

on \(\mathcal H_C\otimes\mathcal H_S\), with periodic boundary conditions.
The Sobolev domains below are for \(\mathcal H_S\)-valued functions.
The operator \(P\) is self-adjoint on \(H^1\). Since \(A\) is bounded
and Hermitian, \(D\) is self-adjoint on the same domain.

The bounded \(C^1\) multiplication operator \(A\) maps \(H^1\) to \(H^1\).
Consequently,

$$
\operatorname{Dom}(D)=H^1,\qquad
\operatorname{Dom}(D^2)=H^2.
\tag{FRC-19}
$$

Indeed, if a vector is in \(H^2\), then \(D\) maps it into \(H^1\).
Conversely, if \(\Psi\in H^1\) and \(D\Psi\in H^1\), then
\(P\Psi=D\Psi-A\Psi\in H^1\), so \(\Psi\in H^2\).

The evolution equation for \(D\) is

$$
(\partial_t+\partial_\phi)\Psi(t,\phi)
=-iA(\phi)\Psi(t,\phi).
\tag{FRC-20}
$$

Its characteristic solution is

$$
\Psi(t,\phi_0+t)=F(\phi_0+t,\phi_0)\Psi(0,\phi_0),
\tag{FRC-21}
$$

where \(A\) is extended periodically to the real line. This establishes
the formula first on the Sobolev domain and then by unitarity on all
square-integrable inputs.

For clarity about the order of the factors, put \(F_\phi=F(\phi,0)\).
Periodicity and composition give

$$
F(\phi+\tau,0)=F_\phi V,\qquad
F(\phi+\tau,\phi)=F_\phi V F_\phi^\dagger.
\tag{FRC-22}
$$

On \(I\), \(F_\phi=I\). After \(n\) full periods, the clock coordinate
returns to its starting point and the corresponding monodromy is the
\(n\)-th power of (FRC-22). Therefore, for every normalized packet \(f\)
supported in \(I\),

$$
e^{-in\tau D}(f\otimes\psi)=f\otimes V^n\psi
\qquad(n=0,1,2,\ldots).
\tag{FRC-23}
$$

The indefinite operator \(D\) is only an auxiliary device in the proof.
It is not the positive finite Hamiltonian asserted by the theorem.

## 5. An explicit normalizable ready packet

Choose \(w>0\) and \(\phi_*\) such that

$$
0<\phi_*<\phi_*+w<d.
\tag{FRC-24}
$$

Define the real normalized packet

$$
f(\phi)=
\begin{cases}
\displaystyle
\sqrt{\frac{8}{3w}}\,
\sin^2\!\left(\frac{\pi(\phi-\phi_*)}{w}\right),
   & \phi_*\le\phi\le\phi_*+w,\\[4pt]
0,&\text{otherwise}.
\end{cases}
\tag{FRC-25}
$$

Both the value and the first derivative vanish at the two endpoints.
Thus \(f\in H^2\); no smoothness beyond \(H^2\) is needed for this packet.
Direct integration yields

$$
\alpha:=\|f'\|^2=\frac{4\pi^2}{3w^2},\qquad
\beta:=\|f''\|^2=\frac{16\pi^4}{3w^4},
\qquad
\|f'\|=\frac{2\pi}{\sqrt3\,w},\quad
\|f''\|=\frac{4\pi^2}{\sqrt3\,w^2}.
\tag{FRC-26}
$$

Because \(A\) vanishes on a neighborhood of the support of \(f\),
for every system vector \(\psi\),

$$
D(f\otimes\psi)=-if'\otimes\psi,\qquad
D^2(f\otimes\psi)=-f''\otimes\psi.
\tag{FRC-27}
$$

## 6. A positive rotor and a uniform finite-horizon error

Set \(\Omega=2\pi/\tau\). For a positive integer \(\ell\), let
\(\Lambda=\ell\Omega\) and define the periodic multiplication unitary

$$
(G_\ell f)(\phi)=e^{i\Lambda\phi}f(\phi),
\qquad
f_\ell=G_\ell f.
\tag{FRC-28}
$$

The integrality of \(\ell\) makes this a unitary on the periodic clock
space. Introduce the positive rotor Hamiltonian

$$
H_\Lambda
=\frac{P^2}{2\Lambda}+A(\phi)+hI
\ge\frac{P^2}{2\Lambda}\ge0.
\tag{FRC-29}
$$

It is self-adjoint on \(H^2\), as a bounded perturbation of \(P^2/(2\Lambda)\).
Its spatial hopping is exactly that of \(A\), so it has spatial range one
and bounded hopping coefficients. The unbounded part acts only on the
clock coordinate.

Since \(G_\ell^\dagger P G_\ell=P+\Lambda I\),

$$
G_\ell^\dagger H_\Lambda G_\ell
=c_\Lambda I+L_\Lambda,\qquad
c_\Lambda=\frac{\Lambda}{2}+h,\qquad
L_\Lambda=D+\frac{P^2}{2\Lambda}.
\tag{FRC-30}
$$

The operator \(L_\Lambda\) is self-adjoint on \(H^2\) by this unitary
equivalence.

The commutator \([P,A]=-iA'\) gives the identity

$$
P^2=D^2-2AD+iA'+A^2
\qquad\text{on }H^2.
\tag{FRC-31}
$$

Let \(\Phi_0=f\otimes\psi\), with \(\|\psi\|=1\).
The group generated by \(D\) preserves \(\operatorname{Dom}(D^2)=H^2\)
and the norms of \(D\Phi_0\) and \(D^2\Phi_0\). Equations
(FRC-27) and (FRC-31) therefore imply, for every real \(t\),

$$
\|P^2e^{-itD}\Phi_0\|
\le C_f,
\qquad
C_f=\|f''\|+2h\|f'\|+h_1+h^2.
\tag{FRC-32}
$$

In particular, the right-hand side does not grow with the number of
periods. Duhamel's identity on \(H^2\) now gives, for \(t\ge0\),

$$
\begin{aligned}
(e^{-itL_\Lambda}-e^{-itD})\Phi_0
&=-\frac{i}{2\Lambda}
\int_0^t e^{-i(t-s)L_\Lambda}
       P^2e^{-isD}\Phi_0\,ds,\\
\|(e^{-itL_\Lambda}-e^{-itD})\Phi_0\|
&\le\frac{tC_f}{2\Lambda}.
\end{aligned}
\tag{FRC-33}
$$

The integrand is well-defined and norm-continuous: the exact \(D\) orbit
stays in \(H^2\), and (FRC-31) controls \(P^2\) on that orbit.
Thus no boundedness assumption on the perturbation \(P^2/(2\Lambda)\)
on the whole Hilbert space is being made.

Combining the gauge relation, (FRC-23), and (FRC-33) yields

$$
\left\|
e^{-in\tau H_\Lambda}(f_\ell\otimes\psi)
-e^{-in\tau c_\Lambda}f_\ell\otimes V^n\psi
\right\|
\le\delta_n,\qquad
\delta_n=\frac{n\tau C_f}{2\Lambda}.
\tag{FRC-34}
$$

For the explicit packet and pulses above, the constant is

$$
C_f=
\frac{4\pi^2}{\sqrt3\,w^2}
+\frac{4\pi h}{\sqrt3\,w}
+h_1+h^2,
\qquad
h=\frac{10\kappa}{\tau},\quad
h_1=\frac{50\pi\kappa}{\tau^2}.
\tag{FRC-35}
$$

All estimates in this section are uniform in the normalized system
vector. They also hold with every system operator tensored by the identity
on an arbitrary passive reference.

## 7. Rotor energy and a tail bound that is uniform in time

Let \(\Phi=f_\ell\otimes\psi\). Since \(A\Phi=0\), the initial rotor
energy is independent of the normalized system input:

$$
E:=\langle\Phi,H_\Lambda\Phi\rangle
=\frac{\Lambda}{2}+h+\frac{\alpha}{2\Lambda},
\qquad
C_E:=\sqrt{2\Lambda E}
=\sqrt{\Lambda^2+2h\Lambda+\alpha}.
\tag{FRC-36}
$$

For completeness, its energy variance is finite and equals

$$
\operatorname{Var}_\Phi(H_\Lambda)
=\alpha+\frac{\beta-\alpha^2}{4\Lambda^2}
=\frac{4\pi^2}{3w^2}
 +\frac{8\pi^4}{9\Lambda^2w^4}.
\tag{FRC-37}
$$

To obtain these formulas, apply the gauge relation to \(f\) and use
\(\langle f,Pf\rangle=0\) and
\(\operatorname{Re}\langle Pf,P^2f\rangle=0\), which hold for this real
packet. The variance here is
\(\|(H_\Lambda-E)\Phi\|^2\). Membership in
\(\operatorname{Dom}(H_\Lambda)=H^2\) suffices; no fourth Sobolev derivative
or operator application \(H_\Lambda^2\Phi\) is assumed.

Let

$$
e_m(\phi)=\tau^{-1/2}e^{im\Omega\phi},\qquad
Q_M=\sum_{m=-M}^{M}|e_m\rangle\langle e_m|,
\qquad
p_{\rm cut}=\Omega(M+1).
\tag{FRC-38}
$$

The same symbol \(Q_M\) denotes its extension by the system identity.
For \(u(t)=e^{-itH_\Lambda}\Phi\), positivity in (FRC-29) and energy
conservation imply

$$
\|Pu(t)\|^2\le2\Lambda E=C_E^2.
\tag{FRC-39}
$$

On the discarded modes, \(|P|\ge p_{\rm cut}\). Hence

$$
\|(I-Q_M)u(t)\|
\le\frac{C_E}{p_{\rm cut}}
\qquad\text{for every real }t.
\tag{FRC-40}
$$

This bound controls the actual interacting rotor orbit, not just the
initial free packet.

## 8. The finite clock and its complete Hamiltonian matrix

Restrict the clock to
\(\mathcal H_{C,M}=\operatorname{span}\{e_m:|m|\le M\}\), of dimension
\(2M+1\). Define

$$
H_{\Lambda,M}
  =Q_MH_\Lambda Q_M
\quad\text{on }\mathcal H_{C,M}\otimes\mathcal H_S.
\tag{FRC-41}
$$

This compression is an everywhere-defined bounded self-adjoint operator:
the retained kinetic term is finite and the retained potential is bounded.
It obeys

$$
0\le H_{\Lambda,M}\le B_M I,\qquad
B_M=\frac{(\Omega M)^2}{2\Lambda}+2h.
\tag{FRC-42}
$$

There is no approximation in the definition (FRC-41).
For an explicit finite matrix description, define

$$
\bigl(A_j^{(M)}\bigr)_{mn}
=\frac1\tau\int_0^\tau
 a_j(\phi)e^{i(n-m)\Omega\phi}\,d\phi,
\qquad -M\le m,n\le M.
\tag{FRC-43}
$$

Writing \(K_1=K_{\rm on}\), \(K_2=K_{\rm link}\),
and \(K_3=K_{\rm contact}\), the actual finite-clock Hamiltonian is

$$
H_{\Lambda,M}
=\operatorname{diag}_{|m|\le M}
 \left(\frac{(\Omega m)^2}{2\Lambda}\right)\otimes I_S
 +\sum_{j=1}^3 A_j^{(M)}\otimes K_j
 +hI.
\tag{FRC-44}
$$

Thus all clock matrices are finite and fixed. Reordering tensor factors
identifies the complete space with
\(\ell^2(\mathbb Z)\otimes\mathbb C^{4(2M+1)}\).
Only the term containing \(K_{\rm link}\) hops spatially. The Hamiltonian
has spatial range one, and its hopping contribution has bounded norm
at most \(h\).

Let

$$
p_0=\|Q_Mf_\ell\|,\qquad
f_M=\frac{Q_Mf_\ell}{p_0}
\quad\text{when }p_0>0.
\tag{FRC-45}
$$

Its coefficients are the finite normalized list

$$
c_m=\langle e_m,f_\ell\rangle
=\frac1{\sqrt\tau}\int_0^\tau
e^{-i(m-\ell)\Omega\phi}f(\phi)\,d\phi,\qquad
f_M=\frac1{p_0}\sum_{m=-M}^M c_m e_m,\qquad
p_0^2=\sum_{m=-M}^M|c_m|^2.
\tag{FRC-46}
$$

The initial case of (FRC-40) supplies

$$
p_0\ge
\sqrt{1-\frac{C_E^2}{p_{\rm cut}^2}}
\quad\text{if }p_{\rm cut}\ge C_E.
\tag{FRC-47}
$$

The parameter choices below make this lower bound strictly positive.

## 9. Compression error without an additional final-tail term

For fixed normalized \(\psi\), retain the uncompressed orbit \(u(t)\)
from Section 7 and set

$$
q(t)=Q_Mu(t),\qquad
v(t)=e^{-itH_{\Lambda,M}}Q_M\Phi.
\tag{FRC-48}
$$

Since \(Q_M\) commutes with the kinetic operator and the scalar shift,

$$
i\dot q(t)
=H_{\Lambda,M}q(t)
 +Q_MA(I-Q_M)u(t).
\tag{FRC-49}
$$

Only the bounded program \(A\) couples the retained and discarded
Fourier modes. Duhamel's formula and (FRC-40) therefore give

$$
\|v(t)-q(t)\|
\le\int_0^t h\|(I-Q_M)u(s)\|\,ds
\le\frac{thC_E}{p_{\rm cut}}
\qquad(t\ge0).
\tag{FRC-50}
$$

At a tick time, projecting the ideal target gives exactly

$$
Q_M(f_\ell\otimes V^n\psi)
=p_0f_M\otimes V^n\psi.
\tag{FRC-51}
$$

Apply \(Q_M\) to the rotor comparison (FRC-34), combine it with
(FRC-50), and divide by \(p_0\). The result is

$$
\begin{aligned}
&\left\|
e^{-in\tau H_{\Lambda,M}}(f_M\otimes\psi)
-e^{-in\tau c_\Lambda}f_M\otimes V^n\psi
\right\|
\le\eta_n,\\
&\eta_n
=\frac1{p_0}\left(
\frac{n\tau C_f}{2\Lambda}
+\frac{n\tau hC_E}{p_{\rm cut}}
\right).
\end{aligned}
\tag{FRC-52}
$$

There is no separate final-tail error to add to (FRC-52). Both states
being compared there lie in the retained space. The projected ideal
packet is exactly the normalized packet \(f_M\) times the common
normalization factor already divided out in (FRC-51).

## 10. Finite-resource theorem and explicit error budget

**Conditional analytical theorem.** Fix \(g\in\mathbb R\), \(\tau>0\),
an integer \(N\ge1\), and \(\varepsilon>0\). Fix \(w,\phi_*\)
satisfying (FRC-24), and use the nominated system, pulses, and packet
above. There exist finite integers \(\ell\ge1\) and \(M\ge0\) such that
the positive bounded Hamiltonian (FRC-44), with the single prepared
clock state \(f_M\), satisfies

$$
\sup_{\|\psi\|=1}
\left\|
e^{-in\tau H_{\Lambda,M}}(f_M\otimes\psi)
-e^{-in\tau c_\Lambda}f_M\otimes V^n\psi
\right\|
\le\varepsilon
\qquad(0\le n\le N).
\tag{FRC-53}
$$

The supremum remains bounded by the same number when every system
operator is tensored with the identity on any passive reference.
One fixed Hamiltonian and one initial preparation serve the whole
specified horizon.

**Proof and resource prescription.** Put \(T_{\rm hor}=N\tau\).
Choose

$$
\ell=
\max\left(
1,\left\lceil\frac{2T_{\rm hor}C_f}{\Omega\varepsilon}\right\rceil
\right),
\qquad
\Lambda=\ell\Omega .
\tag{FRC-54}
$$

Compute the finite \(E,C_E\) of (FRC-36) with this \(\Lambda\), and choose

$$
M=
\left\lceil
\frac1\Omega
\max\left(
2C_E,\frac{4T_{\rm hor}hC_E}{\varepsilon}
\right)
\right\rceil .
\tag{FRC-55}
$$

This slightly conservative integer choice implies

$$
\Lambda\ge\frac{2T_{\rm hor}C_f}{\varepsilon},
\qquad
p_{\rm cut}\ge2C_E,
\qquad
p_{\rm cut}\ge\frac{4T_{\rm hor}hC_E}{\varepsilon},
\qquad
p_0\ge\frac{\sqrt3}{2}.
\tag{FRC-56}
$$

For every \(n\le N\), the first numerator term in (FRC-52) is at most
\(\varepsilon/4\), and the second is at most \(\varepsilon/4\).
Consequently,

$$
\eta_n
\le\frac{\varepsilon/2}{\sqrt3/2}
=\frac{\varepsilon}{\sqrt3}
<\varepsilon.
\tag{FRC-57}
$$

This proves (FRC-53). All constants are independent of \(\psi\).
To include a reference, repeat the construction with \(K_j\otimes I\).
Every operator norm, initial clock calculation, and energy bound is
unchanged. Equivalently, (FRC-52) is an operator-norm bound between
input isometries, and tensoring those isometries with a reference
identity preserves that norm. This completes the proof.

The scalar \(e^{-in\tau c_\Lambda}\) is retained explicitly. It is
independent of the input and cancels from all channel comparisons.
No reset or re-preparation is performed between the tick times in
(FRC-53).

## 11. Energy bounds for the actual finite ready state

The finite packet \(f_M\) is a trigonometric polynomial. It generally
has tails in the active program intervals, so the exact idle-support
property of \(f_\ell\) must not be transferred to it. In particular,
the actual finite-ready energy can depend on the system input.
Nevertheless it has a uniform explicit bound.

For a normalized system input, let

$$
E_M(\psi)=
\langle f_M\otimes\psi,
H_{\Lambda,M}(f_M\otimes\psi)\rangle.
\tag{FRC-58}
$$

Use the uncompressed initial vector \(\Phi=f_\ell\otimes\psi\), and
write \(q=Q_M\Phi\), \(r=(I-Q_M)\Phi\). Since \(A\Phi=0\) and \(A\)
is self-adjoint,

$$
\langle q,Aq\rangle
=\langle r,Ar\rangle
\le h\|r\|^2.
\tag{FRC-59}
$$

Let \(K=P^2/(2\Lambda)\). The projection commutes with \(K\), so
\(\langle q,Kq\rangle\le\langle\Phi,K\Phi\rangle\).
Using \(\|q\|^2+\|r\|^2=1\) gives

$$
\begin{aligned}
\langle q,H_\Lambda q\rangle
&=\langle q,Kq\rangle+\langle r,Ar\rangle+h\|q\|^2\\
&\le\langle\Phi,K\Phi\rangle+h=E.
\end{aligned}
\tag{FRC-60}
$$

After normalization,

$$
0\le E_M(\psi)\le
\min\left(B_M,\frac{E}{p_0^2}\right).
\tag{FRC-61}
$$

Since \(0\le H_{\Lambda,M}\le B_MI\), functional calculus gives
\(H_{\Lambda,M}^2\le B_MH_{\Lambda,M}\). Hence

$$
\begin{aligned}
\operatorname{Var}_{f_M\otimes\psi}(H_{\Lambda,M})
&\le B_ME_M(\psi)-E_M(\psi)^2\\
&\le\frac{B_ME}{p_0^2}.
\end{aligned}
\tag{FRC-62}
$$

The same estimates hold uniformly for input-reference states.
The actual mean and variance are conserved by the autonomous
\(H_{\Lambda,M}\) evolution. These are bounds for the constructed
finite machine, rather than an unproved transfer of the exact rotor
moments (FRC-36)--(FRC-37).

## 12. Channel and coherent clock-return interpretation

Define the two channels from the system into the joint clock-system
space by

$$
\begin{aligned}
\mathcal E_n(\rho)
&=e^{-in\tau H_{\Lambda,M}}
 \bigl(|f_M\rangle\langle f_M|\otimes\rho\bigr)
 e^{in\tau H_{\Lambda,M}},\\
\mathcal F_n(\rho)
&=|f_M\rangle\langle f_M|
 \otimes V^n\rho(V^\dagger)^n .
\end{aligned}
\tag{FRC-63}
$$

The reference-uniform isometry bound (FRC-52) implies

$$
\|\mathcal E_n-\mathcal F_n\|_\diamond\le2\eta_n.
\tag{FRC-64}
$$

Thus, for every input-reference density operator, the trace distance
with the convention \(\tfrac12\|\cdot\|_1\) is at most \(\eta_n\).
Partial trace cannot increase that distance. Both the system output
and the returned clock marginal therefore satisfy the corresponding
bound, while (FRC-64) retains the stronger joint comparison.

The comparison includes coherence and correlations with unknown
references. It does not replace the system input by an eigenstate,
a probability table, or a finite spatial sample.

## 13. Exact scope of the construction

The construction supplies a finite clock of dimension \(2M+1\), the
explicit ready vector (FRC-46), and the complete bounded positive
Hamiltonian (FRC-44). Its spatial range is one on the full nominated
lattice. Its parameters are chosen once for the requested horizon
and tolerance; the actual evolution is autonomous.

The target unitary \(V\), the tick period, the contact parameter, the
local program, and the initial clock readiness are declared inputs.
The theorem is conditional on these definitions. It does not derive
their preparation or their selection from a more primitive law.

At finite \(M,\Lambda\), the stated conclusion is approximate. The
proof does not assert exact reset, exact equality with \(V\), or
unlimited repetition at the same resources. It also does not assert
equality between \(H_{\Lambda,M}\) and a logarithm or sine-energy
observable previously assigned to the nominated walk. The machine
conserves its own displayed total Hamiltonian.

The infinite circle suspension and rotor are intermediate analytical
tools. The final model contains only the finite clock matrices in
(FRC-44), together with the untruncated system position coordinate.
No infinite clock is retained in that final carrier.
