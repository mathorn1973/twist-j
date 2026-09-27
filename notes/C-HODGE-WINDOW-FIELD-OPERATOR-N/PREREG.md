# C-HODGE-WINDOW-FIELD-OPERATOR-N: preregistration

Status: PUBLIC NON-CANONICAL incubation. No Canon authority.
Owner: A. M. Thorn / hodge-window-field-operator-20260927; issue #1237.
Date: 2026-09-27.
Basis: Public Canon v92, main fa5bc67cfff8a7133ea0085548881f1f1114a944.
Action scope: MULTI L1/L2/L5 mathematics. No L6 or physical realization.

A conversation-local symbolic design preflight informed the class below but is
not evidence. This candidate is not blind/prospectively independent. All
universal results require the written proof; the pinned verifier is
corroboration/reproduction only. No class, threshold, equality, coframe or
rounding rule below may change after this pin.

## 1. Frozen inherited data

Use exactly the marked basis of Lambda=Lambda^2 A4=Z^6, wedge form beta,
fixed-J predictive chart E=E_+, inclusion i, metric g=i^T beta i, projector

    Pi=i g^-1 i^T beta,       N=I-Pi,

and compact-window event set from C-HODGE-SPACETIME-WINDOW-N:

    c0=(4+2sqrt5)/5,
    M={Pi w: w in Lambda, -beta(Nw,Nw)<=c0},
    M_H=M/H.

Literal event equality is equality in E_R. Pi is injective on integer labels,
so event equality is also equality of the corresponding admitted labels.

Frozen source hashes:
- probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py
  02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9
- notes/C-HODGE-SPACETIME-WINDOW-N/PREREG.md
  1d987e7f6dae7d1f0b31990ae144a6ad5e719625503abd42d0567db56de75dfa
- notes/C-HODGE-SPACETIME-WINDOW-N/PROOF.md
  aefac8315a9858e9bfdf26a51f95b6790830a31e9c185a4c883ad66129f70442
- probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1/verify.py
  3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e

Let e_i be the six marked source basis vectors and p_i=Pi e_i. In E
coordinates put C=[p_0 ... p_5]=g^-1 i^T beta. The predecessor auxiliary
norm and covering constant are retained exactly:

    R=10-9sqrt5/5.

The componentwise rounding rnd:R^6->Z^6 uses nearest integers with ties
toward +infinity. For every H>=1 and z in E_R define the total event map

    rho_H(z)=Pi rnd(H z)/H in M_H.

This is the already proved rounding mechanism, not a new event selector.

## 2. G1: diagonal six-direction no-go

Freeze the complete F=Q(sqrt5) class

    sum_(j=0)^5 a_j p_j p_j^T = c g^-1,

with unknown a_0,...,a_5,c in F. Decide its exact solution space.
ZERO means no nonzero operator made only from six independent second
differences can have the inherited Hodge principal quadratic form.
No larger mixed-difference class is excluded.

## 3. G2: inherited mixed-form operator

Prove

    C beta^-1 C^T = g^-1.

In the marked wedge basis beta^-1=beta and its only nonzero unordered pairs are

    beta^(05)=+1, beta^(14)=-1, beta^(23)=+1.

Therefore the continuum scalar operator induced by the source form is

    Box_g = 2(d_0 d_5-d_1 d_4+d_2 d_3),

where d_j is directional differentiation along p_j.
The coefficients are inherited integers. No fit to the photon cone is allowed.

## 4. G3: fixed unit-stencil totality boundary

Test the complete claim that every admitted w in M keeps all labels required by
the forward complementary-pair stencil

    {0,e0,e5,e0+e5,e1,e4,e1+e4,e2,e3,e2+e3}

inside the same window after translation by w.
One exact admitted witness with one missing translated label gives
UNIT-STENCIL-TOTALITY-FAIL. This does not affect G2.

## 5. G4: total event-only two-scale field operator

For positive integer n set

    H=n^4,        delta=1/n,        q=n^3.

For x in M_H and a in Z^6 define the actual-event neighbor

    R_n(x,a)=rho_H(x+delta Pi a).

For i!=j define

    Delta_ij^(n) psi(x)
      =(n^2/4)[
          psi(R_n(x, e_i+e_j))
         -psi(R_n(x, e_i-e_j))
         -psi(R_n(x,-e_i+e_j))
         +psi(R_n(x,-e_i-e_j))
       ],

and

    Box_n=2(Delta_05^(n)-Delta_14^(n)+Delta_23^(n)).

Fields are arbitrary complex-valued functions on M_H. Every stencil value must
be at an actual event of M_H. The operator introduces no off-event hidden
field value.

Prove totality for every x and n. Every rounded neighbor differs from its
ideal target x+delta Pi a by at most R/n^4 in the predecessor norm, so the
physical stencil radius is O(1/n).

Candidate bridge C-GATE-L2-L5-HODGE-EVENT-FIELD is exactly:
source = the selected windowed event geometry, marked beta pair structure and
the displayed rounding rule; target = the total scalar Box_n family and its
local characteristic. It is an incubation contract only and is NOT added to
canon/GATES.tsv.

## 6. G5: continuum consistency and explicit plane-wave residual

Let f be C^4 on E_R. Sample it only on M_(n^4). Prove on every compact set,
with bounded derivatives on a fixed compact enlargement,

    Box_n(f|M_(n^4))(x) = Box_g f(x)+O(n^-2)

uniformly over event points x in that compact set.

For a real covector xi define

    a_j=xi(p_j),
    A_xi=max_j |a_j|,
    X_xi=dual norm of xi for the predecessor auxiliary norm.

For the event plane wave psi_xi(x)=exp(i xi(x)), prove the explicit bound

    | Box_n psi_xi(x)/psi_xi(x) + g^-1(xi,xi) |
       <= (2 A_xi^4 + 6 R X_xi)/n^2.

The first term is the ideal centered mixed-difference error using
|sin u-u|<=|u|^3/6. The second is the total four-corner rounding error using
|exp(iu)-1|<=|u|. No unstated Fourier completeness of M_H is claimed.

## 7. G6: local D3 scalar-mode transfer

Freeze one explicit coframe, independently of target data. In the ordered E
coordinates define

    s1=(1,-1,0,0), s2=(1,1,-2,0), s3=(1,1,1,0), t=(0,0,0,1),

and normalize each by the positive square root of the absolute inherited
g-norm, keeping t future-directed. For a covector xi set

    F0(xi)=(Omega,k1,k2,k3)
          =(xi(T),xi(S1),xi(S2),xi(S3)),

so exactly

    -g^-1(xi,xi)=Omega^2-|k|^2.

This fixed positive-root recipe is a coframe choice, not a physical selection.

For epsilon=1/n and epsilon|k|<=1, use the actual registered principal D3 roots

    Omega_epsilon(k)=+/- (2/epsilon) asin(sqrt(s(epsilon k))/2).

Set xi_epsilon=F0^-1(Omega_epsilon,k) and define the actual event field

    psi_(n,k)(x)=exp(i xi_epsilon(x)),     x in M_(n^4).

Using G5 and the inherited root theorem, prove uniformly for |k|<=K and
n>=max(1,K):

    sup_x |Box_n psi_(n,k)(x)| = O_K(n^-2).

An explicit bound may retain A_xi and X_xi; neither may be chosen after the
result. This is a scalar local mode map. It is not a global reciprocal-torus
map, field-Hilbert-space isomorphism, probability law, polarization or
physical photon.

## 8. G7: finite-scale covariance boundary

Let S be the marked integral source step L or Q=Lambda^2 C, with induced
real map S_E on E. For the rounded neighbor rule test literal equality

    S_E R_n(x,a) = R_n(S_E x, S a)

on its complete mathematical definition. Exact equality is required.
A single exact witness routes FINITE-ROUNDING-COVARIANCE-FAIL for that S.
Do not repair a failure by changing rnd, H=n^4, q=n^3, the window or equality.

A finite-scale failure does not affect exact covariance of the continuum
principal tensor C beta^-1 C^T=g^-1 and does not prove physical Lorentz
violation. Exact finite-n self-adjointness, energy conservation, stable Cauchy
evolution and a Green function are explicitly NOT claimed.

## 9. Prospective exact audit and status ceiling

Before scientific execution, commit/push/read back this PREREG and verify.py.
The standard-library verifier will:
- validate all frozen hashes;
- reconstruct Pi,C,beta,g and the exact tensor identities;
- solve the complete G1 linear system;
- search the frozen G3 unit-stencil claim for its first lexicographic exact
  witness in [-1,1]^6 if one exists;
- check total rounded stencils over declared finite exact fixtures for
  n in {1,2,3,5};
- audit quadratic-polynomial consistency and the exact plane-wave-bound
  algebraic coefficients without floating point;
- prospectively search G7 for the first exact covariance witness on declared
  finite fixtures.

Universal all-n/C^4/G6 statements rest on PROOF.md, not finite scans.
A second execution is reproduction, not independent-agent confirmation.
Ordinary notes-only CI is not scientific execution of this verifier.

Accepted statuses are candidate-T for exact theorems/no-gos, candidate-D for
the selected bridge/operator dictionary and candidate-C for finite audits.
Integrity/runtime failure is STOP. No Canon/Registry/Frontier/public gate,
formal probe, tool, workflow or existing note changes. PHOTON-CONE-CONVERGENCE
and PHOTON-MASSLESS-PHASE remain unchanged. No native Omega/U realization,
SI scale, apparatus, Born measure, vector gauge field or finite-n physical
propagation conclusion.
