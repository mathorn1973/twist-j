# Contact bound branch: full analytical proof

Status: NON-CANONICAL mathematical candidate, conditional on the complete carrier and step frozen in PREREG.md. No numerical experiment or verifier was executed by this proof author to obtain the derivation below. This is a declared product-walk/contact model, not an established factor of the complete native TWIST-J update.

Preregistration reviewed before scientific execution: SHA-256 4394fa54dab7cfa6b67ad57310d6b11b3bb760038a3e673448ddac4075626761. The proof author read F1 through F6 and found no scope conflict or mathematical counterexample. This is an analytical review, not a claim that program execution or an architecture gate has occurred. No verifier source was read or edited in preparing this proof.

The notation below uses A,S,T,B for the preregistered Bell vectors chi,eta,zeta,xi respectively. The scalar z denotes the preregistered contact phase gamma, never the Bell vector zeta. The full contact evolution is written U(P) below and V_mu,g(P) in the preregistration. These are explicit aliases for exactly the same objects, not changes of convention.

## Source provenance and new scope

The frozen mathematical premises have this public lineage:

- Public Canon v103 at main 5f20429944b409d912202d141e158fdfec145c41: DIRAC-STEP-THEOREMS [T] and DIRAC-STEP [D]. Its finite-step algebra does not admit a physical contact or derive a particle species. Source: https://github.com/mathorn1973/twist-j/blob/5f20429944b409d912202d141e158fdfec145c41/canon/CANON.md
- The immediate declared Hilbert comparison is the unmerged NON-CANONICAL notes program at da39ea38df90bbf594e90a00f0532964e4e1f041. The original coined walk, sine-energy reader, exact one-step displacement, and onsite product contact are already supplied there. Source: https://github.com/mathorn1973/twist-j/blob/da39ea38df90bbf594e90a00f0532964e4e1f041/notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/CONTACT-KINEMATICS.md
- The earlier one-particle clock/rest/curvature mismatch and nonunique conserved energy readers are already supplied in that same source, and are not new claims here. Source: https://github.com/mathorn1973/twist-j/blob/da39ea38df90bbf594e90a00f0532964e4e1f041/notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/ENERGY.md

The new analytical scope here is the explicit infinite-relative-coordinate contact eigenbranch, its gap and simplicity, its exact curvature and full open-contact-phase comparison, together with the particular impulse-response qualification of that branch. General finite-rank spectral methods and differentiation of a simple eigenvalue are mathematical tools, not claimed new methods. No source-admission or physical status flows from their use.

| Frozen claim | Proof location | Pre-execution review |
| --- | --- | --- |
| F1 | Massless control | Supported on each complete chirality sector. |
| F2 | Compact state and free sign sectors | Supported, including exchange symmetry and zero same-sign component. |
| F3 | Free spectrum, contact simplicity, analytic localization | Supported strictly inside the stated open gap; endpoints excluded. |
| F4 | Exact curvature; actual band displacement | Supported as isolated-band response; bare kick is separately qualified. |
| F5 | Entire contact-phase family | Supported by strict monotonicity and both endpoint limits. |
| F6 | Arithmetic specialization | Supported by exact radical identities and explicit gap inequality. |

## Frozen model

Let mu>0, theta=atan(mu), C=(I+i mu X)/sqrt(1+mu^2), 0<g<2 theta and z=exp(-i g). On the even-relative sector use r=(x1-x2)/2 in Z and R=(x1+x2)/2 in Z. Their Fourier momenta are P and q. In the ordered coin basis (++,+-,-+,--), set

    W(P,q)=diag(exp(iP),exp(iq),exp(-iq),exp(-iP)) (C tensor C),
    V=|r=0><r=0| tensor I_4,
    U(P)=[I+(z-1)V] W(P).

Use the coin vectors A=(++ - --)/sqrt(2), S=(++ + --)/sqrt(2), T=(+- + -+)/sqrt(2), B=(+- - -+)/sqrt(2). At P=0 the A channel is the identity before contact, so chi=delta_0 A obeys U(0)chi=z chi. This vector is exchange-symmetric. A two-fermion antisymmetry restriction would exclude it.

For position statements use the original source convention f_hat(P,q)=sum_(R,r) exp[-i(PR+qr)]f(R,r). Then the center position is R_op=i partial_P and relative position is r_op=i partial_q. A Fourier multiplier exp(iq) translates a profile toward decreasing r. Statements using only the speed magnitude do not depend on this sign convention.

## Massless control: F1

At mu=0, C=I and all four chirality sectors are invariant under the full contact step. In an opposite-chirality sector the relative operator is a bilateral shift multiplied by a scalar unit-modulus phase at r=0. An eigenvalue of this unitary, if it existed, would have modulus one. Its eigenvector recurrence therefore forces |psi(r+1)|=|psi(r)| at every r, including the phase-modified contact equation. An ell2 sequence of constant magnitude is identically zero. Thus no nonzero relative eigenvector exists in either opposite-chirality sector.

The full time evolution in these sectors translates the relative probability profile by one relative cell each tick; contact changes its phase only. In physical separation x1-x2 that is two units per tick. It does not bind the opposite streams.

In an equal-chirality sector the relative coordinate is unchanged by the free step even at zero coupling. At r=0 the two eigenvalues are z exp(iP) and z exp(-iP). In the frozen convention their lifted phases are g-P and g+P. Both have speed magnitude one and second derivative zero, so neither has a differentiable massive rest minimum. At other r the same nonbinding equality of relative velocities was already present without contact.

## Compact rest state and free sign sectors: F2

The identity (C tensor C)A=A follows directly from

    (X tensor I+I tensor X)A=0,
    (X tensor X)A=-A.

The two occupied coin components of A have relative streaming multiplier one at P=0. Hence W(0)(delta0 A)=delta0 A for every mu>=0, and multiplication by contact gives U(0)(delta0 A)=z delta0 A for every real g. This statement does not require an open gap; only the later simplicity and continuation do.

The single-copy sine operator in the exact source convention is

    H_mu(k)=sqrt(1+mu^2)(U_mu(k)^*-U_mu(k))/(2i)
           =[[-sin(k), -mu exp(ik)],
             [-mu exp(-ik), sin(k)]].

It obeys H_mu(k)^2=[mu^2+sin^2(k)]I. At total momentum P=0, set k1=q/2=k and k2=-k. Direct action gives

    [H_mu(k) tensor I+I tensor H_mu(-k)] A=0

for every k: the diagonal sin(k) terms cancel on each of ++ and --, and the two off-diagonal outputs of ++ and -- coincide and cancel in their difference. For mu>0 the single-copy eigenvalues are +epsilon(k) and -epsilon(k), where epsilon(k)=sqrt(mu^2+sin^2(k))>0. Therefore the tensor-sum eigenvalues are +2epsilon, 0, 0, -2epsilon. Its kernel is exactly the direct sum of the two opposite-sign sectors. This proves that the entire compact mode, whose relative Fourier vector is the constant A, has zero same-sign free-band component.

This is simultaneously a statement about free frequency signs: U_mu(k) has eigenvalues exp(-i s omega(k)) on the sign-s eigenspace of H_mu(k), where cos omega(k)=cos(k)/sqrt(1+mu^2) and 0<omega(k)<pi. At P=0, omega(k)=omega(-k), and the two opposite signed frequencies sum to zero. This calculation does not impose a positive-energy particle interpretation.

Under particle exchange, relative coordinate changes r->-r and the two coin factors swap. delta0 is unchanged and A is symmetric. The state is therefore exchange symmetric, and its antisymmetrization is zero.

## Free spectrum and contact simplicity

Put d=(1-mu^2)/(1+mu^2), h=2mu/(1+mu^2), b=1-d and ell=1+d. In the (S,T,B) complement to A, the free Fourier matrix is

    W_b(q) = [[d, i h, 0],
              [i h cos(q), d cos(q), i sin(q)],
              [-h sin(q), i d sin(q), cos(q)]].

The whole free characteristic has two eigenvalues 1 and the pair exp(+-i alpha), where alpha ranges over [2 atan(mu), pi]. Equivalently the complement characteristic is

    det(lambda-W_b(q))
      =(lambda-1)[lambda^2+(1-d)lambda+1-lambda(1+d)cos(q)].

Thus z lies in a genuine free gap. Contact is finite rank, so any spectrum there is isolated point spectrum of finite multiplicity. The computation below proves that the multiplicity of z is exactly one.

Let G be the contact block of the free complement resolvent (z-W_b)^(-1). Set

    D(q)=z^2+(1-d)z+1-z ell cos(q),
    I=integral_[0,2pi] dq/[2pi D(q)],
    rho=cos(g),
    R=sqrt[(rho-d)/(rho+1)].

The gap gives rho>d, and finite mu gives 0<R<1. Elementary contour integration, or the standard cosine integral obtained by a geometric-series expansion, gives

    I = 1/[2z sqrt((rho-d)(rho+1))],
    (z+1)^2 I = 1/R.

For an explicit real-variable proof, write c0=2cos(g)+b, so D(q)=z[c0-ell cos(q)] and c0>ell>0. The tan(q/2)=u substitution over the full circle gives

    integral dq/[2pi(c0-ell cos(q))]
      =(1/pi)integral_(-infinity)^infinity
         du/[(c0-ell)+(c0+ell)u^2]
      =1/sqrt(c0^2-ell^2).

The last equality follows by the substitution u=sqrt[(c0-ell)/(c0+ell)]v and the antiderivative atan(v). Since c0^2-ell^2=4[cos(g)-d][cos(g)+1], this proves the chosen positive-radical formula for I without a numerical branch choice.

Define

    X=[1+(z+1)(d z-1)I]/(z ell),
    Y=[(z+1)(z-d)I-1]/ell.

Oddness in q makes G block diagonal between (S,T) and B. Direct inversion of z-W_b(q) gives

    (z-1) G_ST = [[1-b(z+1)I, i h X],
                  [i h Y, (z-d)X]].

For K=I_3-(z-1)G, direct cancellation gives

    det K_ST = b(1-R)/(z ell R),
    K_BB     = (z+1)(1-R)/(z ell).

Both are nonzero. In the A sector the contact block is 1/(z-1), giving exactly one zero of I_4-(z-1)G_full. Therefore the eigenspace at z is spanned by chi alone. Since U(0) is unitary, the isolated eigenvalue is also algebraically simple.

For reference, the complete finite-rank secular equation at arbitrary P and spectral lambda outside the free spectrum is

    det[I_4-lambda(z-1)/z G_full(P,lambda)] = 0,
    G_full(P,lambda)=V(lambda-W(P))^(-1)V on ran V.

This follows by writing (lambda-W)psi=lambda(z-1)/z V psi. It supplies the starting equation for a separately frozen verifier.

## Analytic branch and relative localization

The family U(P) is norm-analytic in P. An isolated simple eigenvalue therefore continues to a unique analytic lambda(P)=exp(-i Omega(P)) near P=0, with Omega(0)=g. The free gap persists on a sufficiently small P interval. The free inverse Fourier matrix is rational in exp(iq), has no pole on the unit circle in this gap, and consequently is analytic in an annulus around it. Its Fourier coefficients decay exponentially. Every bound eigenvector is the free resolvent applied to a contact-supported vector, so this continued eigenstate is exponentially localized in relative coordinate.

This is internal binding at fixed center-of-mass momentum. It does not assert that a center-of-mass wave packet fails to spread, or that a real particle species, charge, spin or native source has been derived.

## Exact curvature

Let Q=diag(1,0,0,-1) in the original coin basis, acting at every relative site. Since contact commutes with Q,

    U(P)=exp(iP Q)U(0),
    Q chi=delta_0 S,
    <chi,Q chi>=0.

Hence Omega'(0)=0. Let U_b be U(0) restricted to the complement of the entire A channel and set

    H=<delta_0 S,(z-U_b)^(-1)delta_0 S>.

Differentiating the eigenvalue equation, with the eigenvector derivative orthogonal to chi, gives

    lambda''(0)=z-2z^2 H,
    Omega''(0)=i[1-2z H].

The contact resolvent identity at lambda=z gives

    z H = [G(I_3-(z-1)G)^(-1)]_SS
        = [(K^-1)_SS-1]/(z-1).

The above 2-by-2 inverse reduces to

    (K^-1)_SS = -d(z+1)/b + ell^2 z/[b(1-R)(z+1)],
    1-2zH = -(ell/b)R(z+1)/(z-1).

Using ell/b=1/mu^2 and (z+1)/(z-1)=i cot(g/2) proves

    Omega''(0) = R cot(g/2)/mu^2
      = sqrt(mu^2-tan^2(g/2)) /
        [mu^2 sqrt(1+mu^2) tan(g/2)] > 0.

Spatial reflection together with both coin flips conjugates U(P) to U(-P), so the simple branch is even. Its expansion is therefore

    Omega(P)=g + Omega''(0)P^2/2 + O(P^4).

## Arithmetic specialization supplied before computation

For mu=2 and g=2pi/5, put phi=(1+sqrt(5))/2. The gap condition follows from cos(g)=(phi-1)/2 > -3/5=cos(2atan2), with both angles in (0,pi). The two elementary identities

    R^2=(4phi-3)/5,
    cot^2(pi/5)=(4phi+3)/5

give

    Omega''(0)=sqrt(16phi+7)/20,
    M_curv=1/Omega''(0)=20/sqrt(16phi+7),
    E_rest=g=2pi/5,
    M_curv/E_rest=50/[pi sqrt(16phi+7)].

The equivalent preregistered value t^2=7-4phi follows from

    tan^2(pi/5)=(1-cos(2pi/5))/(1+cos(2pi/5))
               =(3-phi)/(1+phi)
               =(3-phi)(2-phi)=7-4phi.

Every displayed root is taken positive, justified by the open-gap condition. This curvature mass differs exactly from the earlier unit-photon chord: its square is 400/(16phi+7)>400/39>4, while the earlier squared chord 2+phi is less than 4. These are different states and different declared readings, so equality was not a premise.

The last comparison assumes the ordinary linear frequency-energy and translation-momentum dictionary with the same massless reference speed c=1. More generally, E=A Omega and p=B P with common massless c=A/B give the same dimensionless ratio M_curv c^2/E_rest. These physical readings and contact coupling are declared premises. They are not consequences of the arithmetic specialization or of the existence of the bound branch.

## Actual displacement, band preparation and a sudden impulse

This section makes the response in F4 an actual displacement statement for the same declared step. It does not supply the unresolved physical apparatus or native-U admission. Let R_op=i partial_P on its natural differentiable domain in the full center-momentum direct integral. Direct differentiation gives the bounded one-step displacement

    D(P)=U(P)^* R_op U(P)-R_op=i U(P)^* partial_P U(P)
        =-U(0)^* Q U(0)
        =-(C tensor C)^* Q(C tensor C).

The contact phase commutes with Q, as does the entire diagonal streaming matrix. Thus D is independent of P, q and g. It acts only on the coin, has norm one, and has spectrum {-1,0,1}. With d,h as above, it is also

    D=-(d/2)(Z tensor I+I tensor Z)
       +(h/2)(Y tensor I+I tensor Y).

This is the two-copy specialization of the earlier source's one-copy displacement identity; the operator identity itself is not claimed as a new method.

### Band expectation and curvature

Write chi_P for the normalized isolated eigenvector, chosen analytically near zero, and Pi(P)=|chi_P><chi_P|. Differentiating U(P)chi_P=exp(-i Omega(P))chi_P and taking the scalar product gives

    <chi_P,D chi_P>=Omega'(P),
    Pi(P) D Pi(P)=Omega'(P) Pi(P).

For a normalized wave packet f(P)chi_P with finite center-position expectation and support inside the gap interval, one exact update changes its mean center position by

    integral |f(P)|^2 Omega'(P) dP.

This equality holds at every tick: the packet remains in the same band and its momentum weights do not change. A central-momentum approximation requires a narrow packet. Berry-connection terms in the position expectation are the same before and after a step and cancel in this difference.

Consequently comparing band-prepared states at momenta zero and eta gives

    Delta v_band=Omega'(eta)-Omega'(0)=kappa eta+O(eta^3).

In the physical linear comparison units, Delta p=B eta and Delta v=(A/B)Delta v_band. Hence the inverse differential mobility is B^2/(A kappa), exactly the phase-curvature mass in F4. Following chi_P while changing momentum is a preparation or adiabatic statement, not an automatic property of an arbitrary sudden impulse.

### A scalar sudden kick has zero instantaneous velocity here

For an ideal initial P=0 rest fiber, a spin-neutral scalar momentum kick changes the total momentum to eta while retaining the relative/coin vector chi_0=delta0 A. The relevant first-update displacement is therefore

    <chi_0,D chi_0>=0

for every eta, because D is momentum independent and its expectation in A is zero. The first-tick velocity is exactly zero, rather than kappa eta. This is a concrete failure of an unrestricted instantaneous-impulse reading, not a failure of F4's isolated-band statement.

Let chi_0=a(P)chi_P+epsilon_P, with epsilon_P orthogonal to chi_P. Analyticity permits a local gauge with <chi_0,partial_P chi_P|_0>=0. Then

    ||epsilon_P||^2=P^2 ||partial_P chi_P|_0||^2+O(P^3),
    partial_P chi_P|_0=i z (z-U_b)^(-1)delta0 S.

The coefficient is finite and nonzero. In particular the kick has leakage amplitude O(|P|) and leakage probability O(P^2). Coherent cross-band contributions to a displacement expectation can still be O(|P|); here they cancel the isolated-band drift at the first tick. Small leakage probability alone does not justify discarding those terms. Projection onto the bound band, or an adiabatic momentum change, is a different preparation.

### Long-time mean displacement after the same bare kick

No post-kick band projection is needed for the following mean-response statement. Choose a sufficiently small closed P interval about zero on which the bound eigenvalue remains isolated and simple. By continuity there is a uniform Delta>0 such that

    dist(lambda(P),spec(U_c(P)))>=Delta,

where U_c is the restriction of U(P) to the complement of chi_P. Put e(P)=||epsilon_P||. The mean actual displacement over T positive integer ticks is

    v_T(P)=<chi_0,D_T(P)chi_0>,
    D_T(P)=(1/T)sum_(n=0)^(T-1) U(P)^(-n) D U(P)^n.

On differentiable full wave packets this also equals the expectation of [U^(-T)R_op U^T-R_op]/T. The fiber current formula is meaningful without assigning a position expectation to a nonnormalizable center plane wave.

The bound-band term in v_T is |a(P)|^2 Omega'(P). The complement term has absolute value at most e(P)^2 because ||D||=1. For the cross term, normality and the gap give

    ||(I-lambda(P)^(-1)U_c(P))^(-1)||<=1/Delta,

    ||(1/T)sum_(n=0)^(T-1) [lambda(P)^(-1)U_c(P)]^n||
        <=2/(T Delta).

The latter follows from the finite geometric-sum identity, with numerator norm at most two. The full cross contribution therefore has absolute value at most 4|a(P)|e(P)/(T Delta). Since |a|<=1 and |Omega'|<=||D||=1, this proves the explicit bound

    |v_T(P)-Omega'(P)|<=2e(P)^2+4e(P)/(T Delta).

Analyticity gives constants L,C, independent of P in a possibly smaller fixed interval, with e(P)<=L|P| and |Omega'(P)-kappa P|<=C|P|^3. Consequently

    |v_T(P)-kappa P|
      <=C|P|^3+2L^2 P^2+4L|P|/(T Delta).

This is a mean displacement of the actual unprojected kicked state under the same complete unitary. It asserts neither instantaneous mobility nor pointwise decay of all interband oscillations. Even if the complement's own time average has no limit, the displayed finite-T bound is sufficient for the differential-response limit.

### Normalizable wave packets and the order of limits

The ideal fixed-P calculation is a fiber statement, not a normalized state of the center coordinate. To realize the same conclusion with normalized states, take a smooth normalized even momentum envelope f_0 supported in [-sigma,sigma] and the full state f_0(P)chi_0. A scalar kick K_eta=exp(i eta R_op) gives f_eta(P)chi_0=f_0(P-eta)chi_0. Choose |eta|+sigma inside the fixed gap interval, so no momentum wrapping occurs. Its mean canonical momentum changes by exactly eta. The un-kicked symmetric packet has zero mean displacement by parity at every time; the kick leaves the first-tick mean zero as well.

Write s_f^2=integral P^2 |f_0(P)|^2 dP<=sigma^2. Averaging the preceding exact fiber bound over |f_eta|^2 gives

    |v_T(packet)-kappa eta|
      <=C(|eta|+sigma)^3
         +2L^2(eta^2+s_f^2)
         +4L sqrt(eta^2+s_f^2)/(T Delta).

The first moment of the shifted distribution is eta; its second moment is eta^2+s_f^2, and Cauchy-Schwarz bounds the first absolute moment. Thus, as eta tends to zero through nonzero values, sigma=o(|eta|), and T tends to infinity,

    v_T(packet)/eta -> kappa.

These are sufficient explicit limits. An arbitrary fixed-duration or broad-packet measurement need not give kappa. The same estimate also permits other coupled limits if every displayed error divided by |eta| vanishes. The impulse/readout is a declared mathematical protocol; its physical source, timing, energy debit and complete apparatus account remain open.

The O(eta^2) population in other spectral components can affect the expected energy at the same order as a quadratic kinetic-energy increment. The above first-order velocity conclusion therefore does not independently establish an energy-transfer or work law for the sudden kick.

## Entire contact-phase family

For fixed mu>0, the same calculation gives the dimensionless ratio

    R_mass(g)=mu^2 sqrt(1+mu^2) tan(g/2) /
              [g sqrt(mu^2-tan^2(g/2))],
    0<g<2atan(mu).

It is strictly increasing. Indeed tan(g/2)/g and [mu^2-tan^2(g/2)]^(-1/2) are positive strictly increasing functions. For the first factor, with x=g/2, the derivative of tan(x)/x has the sign of x-sin(x)cos(x); that quantity vanishes at zero and has positive derivative 2sin^2(x) on the interval. The endpoint limits are

    limit_(g->0+) R_mass(g)=mu sqrt(1+mu^2)/2,
    limit_(g->2atan(mu)-) R_mass(g)=+infinity.

Consequently the equation R_mass(g)=1 has exactly one admitted positive-gap solution if

    mu^2 < (sqrt(17)-1)/2,

and no admitted solution at or above that threshold. For the preselected rung mu=2 the stronger uniform result is

    R_mass(g)>sqrt(5)>1

for every g in the complete open gap interval. Changing the contact phase anywhere inside this interval therefore cannot repair the frequency/translation mass equality at mu=2.

For mu=2, among the nontrivial fifth-root contact phases, the phases with principal |g|=2pi/5 lie in a free gap. Those with |g|=4pi/5 lie in the dispersive free spectrum because cos(4pi/5)=-phi/2<-3/5=d. The compact P=0 vector still exists there algebraically, but the gap-based continuation and stability argument above does not apply to those embedded eigenvalues.

## Scope boundaries

1. mu=2 gives massive individual product-walk bands; these constituents have not been identified with physical massless photons.
2. The unperturbed compact mode lies in the free mixed-sign zero-quasienergy sector at P=0. A positive-energy two-particle projection is a different model and may remove the witness.
3. The branch is exchange symmetric and therefore is not a two-identical-fermion state.
4. The selected phase z=exp(-2pi i/5) is an explicit contact definition. No unchanged-native-U-to-contact factor map, occurrence law or apparatus calibration is proved.
5. Nonlinear redefinitions of energy or momentum are outside the stated frequency/translation test. A mismatch under that test cannot be promoted to a no-go over all decoder families.
