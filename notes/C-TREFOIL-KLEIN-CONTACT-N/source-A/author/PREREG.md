# Frozen local checks: marked Klein coordinate bridge

Status: NON-CANONICAL, candidate-T analytic note with auxiliary local exact checks.
This is not a public P-probe, not an activation gate, and not a physics result.
The native-U realization, stability, and proton interpretation remain OPEN.

Date: 2026-10-17.
This file is frozen before any new machine evaluation of the proposed identities.
The author implementation and an independently written checker must use the targets below without modifying them after a result is observed.

## 1. Public basis and ownership boundary

Repository: mathorn1973/twist-j.
Public Canon: v103 ACTIVE.
Pinned main: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.
CANON.md SHA-256: d87657aeccc568dd668718fb9cbea6136643e5db32dd4e328e64f824b.

Owned inputs: COLOR-CORE-2I, COLOR-SPECTRAL-INVARIANTS, COLOR-KLEIN-REDUCTION, and COLOR-INTEGRAL-LIFT, including reproduce/color-ladder/verify.py rungs 10 and 11.

Rung 11 already constructs marked invariants by Reynolds averaging and their Hessian/Jacobian, proves an adjusted Klein relation, and checks a ramified residue orbit. This note does not claim that existence again. The new content is an explicit marked change of coordinates, exact chosen normalizations and reductions, the obstruction to an integral diagonalizing change of coordinates at the ramified prime, and a fixed J-bearing branch point.

## 2. Arithmetic, action, and named constants

K = Q[j]/(1+j+j^2+j^3+j^4), O = Z[j], j = exp(2*pi*i/5) in the principal embedding.
Complex conjugation c sends j to j^4. All computational assertions use exact coefficients; pi and numerical complex approximations are not inputs.

lambda = 1-j, a = j+j^4 = phi^-1, phi = a+1, J = 1+j^2 = a*j.
r = j-j^4, s = j^2-j^3 = j^2*lambda.

Frozen scalar identities:

    a^2+a=1, s^2=a-2, s^4=5*a^2, r=s/a,
    a^2+s^2=-1, c(a)=a, c(s)=-s.

The lambda valuation v_lambda has v_lambda(lambda)=1; v_lambda(s)=1 and v_lambda(5)=4.
For a nonzero polynomial, its valuation is the minimum valuation of its coefficients.
Coefficient reduction modulo lambda sends j to 1 and integers to F_5.

Column vectors are the carrier. Invariance under g means p(g*(u,v)^T)=p(u,v).
Do not replace this convention with the transposed substitution used internally by the old rung 11 without a stated conversion.

## 3. Frozen matrices and conjugacy targets

    S = [[0,-1],[1,0]]
    T = [[j,1],[0,j^4]]
    P = [[1,-a],[0,s]]
    B = [[s,a],[0,1]] = s*P^-1
    D = [[j,0],[0,j^4]]
    E = [[1/r,1/s],[1/s,-1/r]]

Targets:

    det(P)=s, det(B)=s,
    P^-1*T*P=D, P^-1*S*P=E,
    B*T=D*B, B*S=E*B,
    det(D)=det(E)=1, E^2=-I,
    c(D)^T*D=I, c(E)^T*E=I.

P is invertible over K and O[1/lambda], and is not invertible over the localization O_(lambda). This is an exact valuation statement, not a numerical conditioning claim.

The analytic obstruction must also be stated: no integral invertible diagonalizing matrix over O_(lambda) can conjugate T to D, because their reductions are respectively a nonidentity unipotent and the identity.

## 4. Frozen standard Klein forms

    f0(x,y) = x^11*y + 11*x^6*y^6 - x*y^11

    H0(x,y) = -x^20 - y^20 + 228*x^15*y^5
               - 228*x^5*y^15 - 494*x^10*y^10

    W0(x,y) = x^30 + y^30 + 522*x^25*y^5
               - 522*x^5*y^25 - 10005*x^20*y^10
               - 10005*x^10*y^20

Standard identities:

    W0^2 + H0^3 = 1728*f0^5,
    H0 = det(Hessian(f0))/121,
    W0 = Jac(f0,H0)/20,
    Jac(p,q) = p_x*q_y - p_y*q_x.

The proof of standard invariance may use the existing perfect group <S,T>, conjugacy, the root permutation of f0, and the displayed covariant identities. No new finite-group enumeration is required.

## 5. Frozen marked polynomials and exact output targets

Set x=s*u+a*v and y=v. Define

    fhat = f0(x,y), Hhat = H0(x,y), What = W0(x,y),
    F = fhat/s^10, H = Hhat/s^20, W = What/s^25.

All of fhat,Hhat,What and F,H,W must belong to O[u,v].
All six polynomials must be invariant under the fixed column actions S,T.

Exact valuation targets, in this order:

    (v_lambda(fhat),v_lambda(Hhat),v_lambda(What)) = (10,20,25),
    (v_lambda(F),v_lambda(H),v_lambda(W)) = (0,0,0).

Exact marked relations:

    What^2 + Hhat^3 = 1728*fhat^5,
    W^2 + s^10*H^3 = 1728*F^5,
    W = (a^2/4)*Jac(F,H).

The last equality is over K, with W already separately certified integral.

Define the modular forms

    E6 = u^5*v - u*v^5,
    D20 = (u^5-u*v^4)^4 + v^20.

Frozen reduction targets:

    F mod lambda = 2*E6^2,
    H mod lambda = 4*D20,
    W mod lambda = 4*E6^5.

The normalized K-valued pullbacks are

    fK = F/s^2 = f0(P^-1*(u,v)^T),
    HK = H = H0(P^-1*(u,v)^T),
    WK = W/s^5 = W0(P^-1*(u,v)^T).

They must satisfy WK^2+HK^3=1728*fK^5 and have coefficient valuations (-2,0,-5).

An analytic consequence, not an extra numerical search: within the one-dimensional invariant spaces of degrees 12,20,30, no rescaling over K simultaneously retains the standard relation and makes its degree-12 and degree-30 forms lambda-primitive. Writing (f,h,t)=(cF,dH,eW) forces e^2=c^5 and d^3=e^2*s^10. Primitive f and t would force 3*v_lambda(d)=10, impossible in K.

## 6. Frozen J-bearing branch point and Hermitian form

    v0 = (-a,j^2)^T,
    M = c(P^-1)^T*P^-1 = [[1,a/s],[-a/s,1]].

Targets:

    B*v0 = j^2*(J,1)^T,
    f0(J,1)=0, F(v0)=0,
    det(M)=-1/s^2, trace(M)=2,
    c(S)^T*M*S=M, c(T)^T*M*T=M,
    c(v0)^T*M*v0=1.

The proof must explain positivity in both archimedean places from s being nonzero and purely imaginary at each place, determinant -1/s^2>0 and trace 2. Positive-definite existence is already owned in COLOR-CM-2I-SEMILINEAR-PAIR; only this explicit coordinate normalization is new.

## 7. Falsifiers, execution, and reporting

F1: any frozen scalar or matrix identity fails.
F2: a marked polynomial is nonintegral or fails either marked-generator invariance.
F3: any standard or marked polynomial identity has a nonzero exact residual.
F4: any one of the six exact valuations or three residue scalars differs from the frozen target.
F5: any fixed J-point or Hermitian-form identity fails.
F6: the analytic nonintegrality or normalization arguments require an unstated field extension, action convention, or unproved independence claim.

No coefficients, exponents, marked matrices, target reductions, or point coordinates may be changed after a check fails. A failed auxiliary check is reported as a failure of this frozen candidate; an amended candidate would require a separate preregistration and an explicit explanation.

The author checker must output a deterministic structured report and its own source hash. A second implementation must be written from this preregistration without reading the author's checker. Both use exact arithmetic only and report architecture, versions, exit status, and stderr. One local architecture is not represented as a two-architecture public gate.

A successful finite check is auxiliary evidence for the identities. The delivered result must contain the analytic derivation, declared coefficient rings and action conventions, and the ramified obstruction. It must not claim that the microscopic dynamics selects the scalar action, creates a trefoil in physical space, stabilizes B=1, or predicts a mass.
