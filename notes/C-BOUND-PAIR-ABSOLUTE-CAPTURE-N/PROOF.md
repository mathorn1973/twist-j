# Complete boundary certificate for absolute bound-pair capture

**NON-CANONICAL / L1. Prospective analytical and computational package.**

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Reservation: [#1814](https://github.com/mathorn1973/twist-j/issues/1814).

This proof fixes the scalar reductions and certified numerical method for `P-BOUND-PAIR-ABSOLUTE-CAPTURE-1`. `SOURCES.md` identifies the adopted Canon premises and the unmerged conditional predecessor. All source, event and normalization conventions remain those of that predecessor. The computation concerns the original asymptotic joint event; it does not assert a physical particle assignment or a native preparation mechanism.

The derivations and static cross-review were completed within one continuing authoring session before the scientific run. They are not external independent theorem acceptance. The frozen executable and its finite disposition are specified in `../../probes/P-BOUND-PAIR-ABSOLUTE-CAPTURE-1/PREREG.md`.

## Part I. Complete contact resolvents

This note concerns the complete internal object walk W = Gamma_g S M_2. The separate capture rotation remains (3/5,-4/5;4/5,3/5). Nothing here replaces the capture denominator 4+F1 F2 or its complete spectral channels.

### 1. Definitions and the physical algebraic sheet

Use the Bell order (A,S,T,B), with A=(++ - --)/sqrt(2), S=(++ + --)/sqrt(2), T=(+- + -+)/sqrt(2), and B=(+- - -+)/sqrt(2).

Set

    d = -3/5, c = 4/5, ell = 1+d = 2/5, b = 1-d = 8/5,
    v = cos P, uP = sin P, gamma = exp(-i g), x = lambda/gamma,
    u = (lambda + lambda^(-1))/2,
    t = v - 5u,
    R = sqrt(t^2 - 16), with R/t -> 1 as lambda -> infinity,
    q = (t-R)/4 = 4/(t+R).

Here q is an effective boundary return coefficient, NOT the relative momentum integrated out below. It satisfies

    2 q^2 - t q + 2 = 0.

The R branch is analytic for |lambda|>1. For lambda=exp(-i omega) approached radially from outside, away from thresholds,

    R = sgn(t) sqrt(t^2-16)                    if |t|>4,
    R = i sgn(sin omega) sqrt(16-t^2)          if |t|<4.

The second case is the free spectral gap relevant to bound eigenvalues. The first case is the free continuous spectral region. The apparent factors lambda^2-1 of the unsimplified determinant discriminant are removed in these scalar formulas.

### 2. Exact q-momentum integration, without a relative-space truncation

For relative momentum kappa,

    det(lambda I - F(P,kappa)) = a - Bcos cos(kappa),
    a = lambda^4 -(2v/5)lambda^3 -(6/5)lambda^2 -(2v/5)lambda +1,
    Bcos = (2/5)lambda(lambda^2-2v lambda+1).

For v=1 this is

    (lambda-1)^2 [lambda^2 +(8/5 -(2/5)cos(kappa))lambda +1].

Let Sigma=sqrt(a^2-Bcos^2) with Sigma/lambda^4 -> 1 at infinity. The complete integrals are

    I0 = 1/Sigma,
    I1 = (a/Sigma-1)/Bcos.

They follow from the two roots (a +- Sigma)/Bcos in exp(i kappa), the first of which selected by the minus sign stays inside the circle. No root can cross the unit circle for |lambda|>1. The relation a I0-Bcos I1=1 proves the second formula.

Every 3x3 minor of lambda I-F uses its exp(i kappa) row and exp(-i kappa) row at most once. Thus every adjugate entry has harmonics only 0,+1,-1. With Nplus=adj(lambda I-F(P,0)) and Nminus=adj(lambda I-F(P,pi)),

    N0=(Nplus+Nminus)/2, Nc=(Nplus-Nminus)/2,
    Gfree(P,lambda)=N0 I0+Nc I1.

This is the full 4x4 contact compression of the infinite free resolvent. The sine harmonic integrates to zero. It is not a scalar approximation.

### 3. A smaller exact Schur calculation

The free symbol in Bell order is

    [ v,       i d uP,       -c uP,          0          ]
    [ i uP,    d v,           i c v,         0          ]
    [ 0,       i c cos kappa, d cos kappa,   i sin kappa]
    [ 0,       -c sin kappa,  i d sin kappa, cos kappa  ].

Eliminate the stationary (A,S) block. Its determinant and the induced moving T coefficient are

    D0(lambda)=lambda^2-ell v lambda+d,
    D1(lambda)=d lambda^2-ell v lambda+1,
    eta=D1(lambda)/D0(lambda).

The moving (T,B) Schur block is lambda I-S(kappa)diag(eta,1). Its integrated T diagonal is h=D0(lambda)(lambda I0-I1). Block inversion gives the exact inverse of the EVEN (A,S,T) free contact Green matrix:

    Gfree_even^(-1) =
    [ lambda-v, -i d uP,       c uP        ]
    [ -i uP,    lambda-d v,    -i c v      ]
    [ 0,        -i c q,        lambda-d q  ],

where q=(lambda-1/h)/eta, extended through removable expressions. Algebra reduces this q to the single-root expression in section 1.

For reference,

    Sigma^2=(4/25)lambda^2(lambda^2-1)^2 (t^2-16),
    Sigma=-(2/5)lambda(lambda^2-1)R

on the sheet fixed at infinity. These identities explain the simplification.

The exchange-odd B contact is exactly separate. The entire even 3x3 block is retained; it contains all spectral channels having a nonzero A-port overlap.

### 4. The complete scalar f_A

Woodbury gives

    Ginteracting_even = gamma^(-1)
        [Gfree_even^(-1)-lambda(1-gamma^(-1)) I3]^(-1).

The bracket replaces every diagonal lambda in the displayed 3x3 inverse by x=lambda/gamma, while retaining q(P,lambda). Define

    N = x^2-d(v+q)x+v q,
    C = x^2-ell v x+d,
    B = -d x^2+ell v x-1,
    D = x C+q B
      = x^3-(ell v+d q)x^2+(d+ell v q)x-q.

Then the complete scalar Caratheodory function of the interacting object at the A contact is

    f_A(P,lambda) = 2x N/D -1.

This is a rational function of cos P, lambda, gamma and the ONE algebraic root R. It includes all relative even-sector poles and continua.

Checks available without an executable:

* f_A -> 1 as lambda -> infinity; its first correction is 2 gamma v/lambda, the actual one-step A return amplitude.
* At v=1, D=(x-1)N, so f_A=(lambda+gamma)/(lambda-gamma).
* At v=-1, D=(x+1)N, so f_A=(lambda-gamma)/(lambda+gamma).

The endpoint formulas remove all A-invisible factors at exact P=0,pi. The verifier uses the full denominator on interval boxes; if a removable factor cannot be separated or certified by its complete real gap equation, it returns INCONCLUSIVE.

### 5. Complete algebraic pole candidates

If B is nonzero, D=0 gives q=-x C/B. Elimination with 2q^2-tq+2=0 yields

    Q6(x,v) = 4x^2 C^2
       +(2v x-5 gamma x^2-5 gamma^(-1)) C B
       +4 B^2 =0.

This has degree at most six in x. It is only a candidate polynomial. A candidate must satisfy the ORIGINAL D=0 on the physical sheet and must not cancel in N/D. Multiplying by five in C and B clears their rational denominators.

For -1<v<1 and |lambda|=1, write D1x=d x^2-ell v x+1=-B. Then D1x=x^2 conjugate(C), so the candidate q=x C/D1x has modulus one. On the open continuous region |t|>4, the physical q has modulus less than one. Therefore no A-visible bound pole lies there. All such poles lie on the strict gap |t|<4, apart from threshold limiting cases treated separately.

There are no A-invisible even gap eigenstates for sin P != 0. If the A contact amplitude vanished, the first stationary equation would give T=i d S/c; the second would then give x S=0. Thus S=T=0 and the complete even contact vector would vanish. The contact eigenvalue equation would reduce to a free eigenstate in a free gap, which is impossible. The same observation proves simplicity: an eigenspace of dimension at least two would contain a nonzero vector with zero A contact amplitude. Hence physical even gap eigenvalues for sin P != 0 are simple and visible. Polynomial candidates on the other sheet still have to be rejected.

### 6. Real gap denominator and real pole weights

On each strict gap interval let

    delta=omega-g,
    eta=sgn(sin omega) arccos(t/4),
    chi=(eta-delta)/2,
    H=(cos delta-v) sin chi-4 sin delta cos chi,
    G=4(cos delta+v) cos chi+sin delta sin chi.

Then q=exp(-i eta), x=exp(-i delta), and exactly

    D=(4i/5)exp[-i(eta+3delta)/2] H,
    2xN-D=(4/5)exp[-i(eta+3delta)/2] G,
    f_A=-i G/H.

This gives a real scalar equation H=0 for every physical gap pole. Also

    partial_omega eta=-5 |sin omega|/sqrt(16-t^2)

within each such interval.

For a simple pole omega_b(P), the complete A spectral weight is

    r_b(P)=-G(P,omega_b)/(2 partial_omega H(P,omega_b)) >0.

Equivalently, with lambda_b=exp(-i omega_b),

    r_b = Res_(lambda=lambda_b) f_A /(2lambda_b)
        = N/(gamma partial_lambda D) at the pole.

The selected original bound branch is only one of these poles. A full F2 evaluation must retain every visible one.

### 7. Shifted energies, all pulse branches, and a finite algebraic root problem

Let zE=exp[-i(E-beta)] and k=K-P. The two shifted object phases are

    omega_sigma(P)=E-beta-sigma epsilon(k), sigma=+1,-1.

For the current windows, omega_plus is strictly in (0,pi); omega_minus is in (0,2pi) and may cross pi. Its R sheet cannot be fixed to a positive imaginary square root throughout.

The complete F2 is

    F2(K,zeta)=integral_(all P) sum_sigma h_sigma(K-P)
       f_A(P,zeta exp[i(beta+sigma epsilon(K-P))]) dP/(2pi),
    h_sigma(k)=(1-sigma epsilon'(k))/2.

The pulse dispersion gives the exact quadratic relation

    lambda^2-2 c_k zE lambda+zE^2=0,
    c_k=(1-4cos(K-P))/5.

Together with Q6(lambda/gamma,cos P)=0 it yields a finite algebraic candidate system for ALL P-poles of both shifted branches. Half-angle charts in P turn it into a polynomial system; the physical gap sheet, the original denominator, and the chosen pulse sign then filter the candidates. No selected-branch substitution is valid.

Object thresholds satisfy

    t=+4 or -4,
    5lambda^2-2(v-4)lambda+5=0  (t=+4),
    5lambda^2-2(v+4)lambda+5=0  (t=-4).

Combining these quadratics with the pulse quadratic similarly gives every shifted threshold candidate.

### 8. Pole-threshold coincidences are outside the current K,E rectangle

At t=+4, q=+1 and

    D=(x-1)[x^2+(b-ell v)x+1].

At t=-4, q=-1 and

    D=(x+1)[x^2-(b+ell v)x+1].

For g=2pi/5 and v in [-1,1], the possible D=0 threshold locations reduce to

    (omega,v)=(g/2, 5cos(g/2)-4),
    (omega,v)=(pi+g/2, 4-5cos(g/2)).

The linear factors x=+1 or -1 would require v outside [-1,1]. The quadratic factors use cos(omega-g)=cos omega and give exactly the two displayed admissible cases.

Put phi=(1+sqrt5)/2. These threshold v values have |v|<1/8, and the frozen k0 has

    cos k0=(7-5phi)/8,  |cos k0|<1/6.

Therefore at either sign of P with the displayed v,

    |cos(k0-P)| > (5/6)(7/8)-1/48 =17/24.

At E*=8pi/5, pulse resonance at the first threshold instead requires

    cos(k0-P)=(5phi-3)/8, whose absolute value is <2/3.

At the second threshold it requires cos(k0-P)=cos k0, whose absolute value is <1/6. Thus neither is resonant. Moving K over its width changes the actual cosine by at most 1/1000. Moving E changes the required cosine by at most 5h/4=1/800. Their sum 9/4000 is less than the smaller gap 1/24. Hence no object pole-threshold coincidence occurs anywhere on the full frozen K,E rectangle.

This does NOT by itself exclude a critical point of a bound-plus-pulse dispersion. The remaining condition H_sigma=0 and partial_P H_sigma=0 must still be isolated or covered in the certified quadrature.

### 9. Complete boundary formula with pole subtraction

For a fixed regular (K,E), set H_sigma(P)=H(P,omega_sigma(P)). Let Pj be ALL simple physical gap zeros of H_sigma, with nonzero G. At each such zero write

    cj = h_sigma(K-Pj) G(Pj)/(2 H_sigma'(Pj)).

The pointwise gap boundary integrand has singular part

    h_sigma f_A = -2i cj/(P-Pj) + regular.

Add i cj cot((P-Pj)/2) to the pointwise integrand. This removes the pole, and its principal-value integral over the whole P circle is zero. The exterior radial limit contributes the additional real pole weight

    h_sigma(K-Pj) |G(Pj)|/(2 |H_sigma'(Pj)|).

Thus F2 is the integral over the complete, pole-subtracted pointwise boundary integrand, plus the sum of these real weights. The continuum pieces use the same algebraic f_A and physical R sheet. This retains both the PV imaginary part and every real spectral contribution; it is not radial extrapolation.

At pulse eigenvalue degeneracy k=pi modulo 2pi, use the combined two-branch limit or the original 2x2 pulse symbol. At object thresholds the present verifier uses a bounded algebraic range enclosure, including both sides of the physical square root. A simultaneous H_sigma=H_sigma'=0 must be excluded by the complete interval census; otherwise this probe returns INCONCLUSIVE. No critical-point excision or external subdivision is implemented in this pin.

### 10. What is still a genuine certification obligation

The formulas provide a complete, finite, implementable boundary prescription. A scientific run must still certify all relevant roots and interval partitions, control threshold quadrature and exclude unresolved velocity matching, and integrate the original K,E event with its original source normalization. The one selected positive-pulse bound root is already proved in the source; the full denominator requires the complete root census above.

The inherited full-event bounds from ABSOLUTE_BOUND.md are the complete-event fallback if this finite certificate is inconclusive. They do not license omitting any inner spectral channel.

### 11. Companion complete odd scalar simplification

The complete odd scalar identity is

    f_B(P,lambda) = [R-4i sin(omega-g)]/[t+4cos(omega-g)],
    lambda=exp(-i omega), t=v-5cos omega,

with the SAME analytic R sheet. Complex sine and cosine define the exterior analytic expression. It follows from the free scalar (R-4i sin omega)/(t+4cos omega), its contact Mobius transform, and

    R^2+16sin^2 omega=(t+4cos omega)(t-4cos omega).

On the whole target I_omega and all P, the denominator is strictly larger than 21/5: v>=-1, cos omega<-4/5, cos(omega-g)>3/10. Thus the complete F1 boundary has no poles on this rectangle, and t>3 means its only root thresholds are t=+4, at the two P signs. Closed relative channels still contribute their imaginary term. This is an exact full-port formula, not the restricted prepared density.

### 12. Explicitly positive full even continuum density

On |t|>4 the physical q is real with |q|<1. Put

    C=x^2-ell v x+d,
    A=x^2+(1-d)v x-d.

For unit-modulus x,

    2xN-D=x A+q x^2 conjugate(A),
    D=x C-q x^2 conjugate(C).

The cross terms in the product of the first expression with conjugate(D) are purely imaginary. Furthermore

    Re(A conjugate(C))=(1-d^2)(1-v^2)=16(1-v^2)/25.

Consequently the exact full continuum density is

    Re f_A = (16/25)(1-v^2)(1-q^2)/|D|^2
           = (8/25)(1-v^2) q R/|D|^2.

The second equality uses qR=2(1-q^2). Both q and R have the same sign in the continuum, so the expression is nonnegative. At a nonresonant threshold it vanishes with the square root, and at v=+-1 it vanishes exactly. The helper model.py uses the first positive expression on a proved strict continuum box; threshold-straddling boxes retain the full safe complex enclosure instead.

## Part II. Complete boundary accounting and quadrature

### 1. The quantity that must be enclosed

Keep CP-13 of `notes/C-BOUND-PAIR-CAPTURE-MOMENTUM-N/PROOF_CAPTURE_PROFILE.md` exactly:

\[
P_0=\int_{I_K}\frac{dK}{2\pi}\int_{I_E}\frac{dE}{2h}
\frac{64\pi^2\rho_{\rm in}(E)\rho_{2,b,+}(K,E)}
 {|4+F_1(E)F_2(K,E)|^2}.
\]

Here `h=delta=delta_K=1/1000`, and all source, event, pulse, branch and projector definitions remain those of the inherited proof. The complete functions are

\[
F_1(E)=\int f_B(P,E-\beta)\frac{dP}{2\pi},
\]

\[
F_2(K,E)=\int_{-\pi}^{\pi}\sum_{\sigma=\pm1}
 h_\sigma(k)f_A(K-k,E-\beta-\sigma\varepsilon(k))\frac{dk}{2\pi}.
\]

Boundary integrals in the second formula include the delta/coarea contributions of gap poles. Neither function is replaced by a selected incident or outgoing density.

The complete `f_A`, its physical sheet, real gap functions `H,G`, and degree-six pole candidate polynomial are in Part I, sections 1, 4–9. The source definition and stationary normalization of the full functions are in `PROOF_CAPTURE_SCATTERING.md`, section 2. The finite incoming-source width is covered by CP-24, not by setting that width to zero.

### 2. Two additional simplifications before any quadrature

#### 2.1 The full odd function has no poles in the required energy window

Put `u=cos omega`, `s=sin omega`, `v=cos P`, `t=v-5u`, and use the same physical `R=sqrt(t^2-16)` as the even formula. Direct cancellation in the inherited odd Schur/Mobius expression gives

\[
\boxed{f_B(P,\omega)=
 \frac{R-4i\sin(\omega-g)}{t+4\cos(\omega-g)}.}
\]

For example, the free expression is `(R-4 i s)/(v-u)`. Substituting it into `(f0+i tau)/(1+i tau f0)` and using

\[
R^2+16s^2=(v-u)(v-9u)
\]

cancels the apparent `v-u` factor and gives the boxed expression. This is an algebraic identity on the exterior analytic sheet, so it continues through the removable original Schur denominator.

Throughout the full `P` circle and `omega in I_omega`, the inherited bounds `u<-4/5` and `cos(omega-g)>3/10` give

\[
t+4\cos(\omega-g)>21/5.
\]

Thus there are no `F1` boundary poles to isolate. Only the two simple square-root transitions

\[
P=\pm p_c(\omega),\qquad p_c=\arccos(4+5\cos\omega)
\]

remain. In this window `t>3`, so there is no `t=-4` transition.

#### 2.2 The pulse can be evaluated without acos or a removable 0/0

Use `k in [-pi,pi]` and `P=K-k`. Set

\[
a_k=\sqrt{3-2\cos k}/\sqrt5,
\qquad b_k=2\cos(k/2)/\sqrt5.
\]

Then `a_k=cos(epsilon/2)`, `b_k=sin(epsilon/2)`, and

\[
\lambda_\sigma=e^{-i(E-\beta)}(a_k+i\sigma b_k)^2,
\qquad v_\varepsilon(k)=\frac{-2\sin(k/2)}{\sqrt{3-2\cos k}},
\qquad h_\sigma=(1-\sigma v_\varepsilon)/2.
\]

All square roots in these pulse formulas have argument at least one before division by five. The formulas extend one-sidedly to both endpoints; the sum over the two branches is periodic and regular there. The branch exchange at the endpoints does not discard either branch. In the frozen window those endpoints are also away from an object threshold or pole: `P=K+-pi`, `omega=E-beta`, and `t>4` with a strict margin.

Gap half-angles can likewise avoid acos:

\[
\cos(\eta/2)=\sqrt{(4+t)/8},\qquad
\sin(\eta/2)=\operatorname{sgn}(\sin\omega)\sqrt{(4-t)/8}.
\]

Combining these with the half-angle of `omega-g` gives `H,G`. There is no need to evaluate an inverse trigonometric function at every integrand call.

### 3. Exact boundary accounting for the complete F2

#### 3.1 The continuum is positive and has a simple scalar formula

In the physical continuum `|t|>4`, `q=(t-R)/4` is real and `|q|<1`. With `D` from Part I,

\[
\boxed{\operatorname{Re}f_A=
 \frac{16(1-v^2)(1-q^2)}{25|D|^2}
 =\frac{8(1-v^2)qR}{25|D|^2}.}
\]

One proof writes `C=x^2-ell v x+d`, `A=x^2+(1-d)v x-d`. On the unit circle,

\[
D=xC-qx^2\overline C,\quad
2xN-D=xA+qx^2\overline A,\quad
\operatorname{Re}(A\overline C)=(1-d^2)(1-v^2).
\]

This positive formula avoids cancellation in `Re f_A`. At an ordinary object edge it vanishes as a square root. Part I section 8 proves that pole/edge coincidences are excluded from the entire frozen `(K,E)` rectangle. Therefore the full `f_A` is bounded at every object edge relevant here. Only velocity matching of a gap pole remains a possible source of an unbounded full `F2` density.

#### 3.2 All simple gap poles contribute explicitly

For each pulse sign put

\[
H_\sigma(k;K,E)=H(K-k,E-\beta-\sigma\varepsilon(k)),\qquad
B_\sigma(k)=h_\sigma(k)G(K-k,E-\beta-\sigma\varepsilon(k)).
\]

Let `k_j` range over **every** physical, A-visible, simple zero of these functions on the full `k` interval. Define

\[
c_j=\frac{B_\sigma(k_j)}{2\partial_k H_\sigma(k_j)}.
\]

The full real boundary value is

\[
\boxed{\operatorname{Re}F_2=
 \int_{-\pi}^{\pi}\sum_\sigma h_\sigma\operatorname{Re}f_A\,
 \mathbf1_{\{|t_\sigma|>4\}}\frac{dk}{2\pi}
 +\sum_j|c_j|.}
\]

The last terms are the coarea contributions of the relative point spectrum after convolution with the moving pulse. The interval census can retain a root family whose A weight vanishes at an exceptional compact parameter P=0 or pi; its corresponding residue then vanishes and the formulas extend continuously. Strict positivity is required separately only for the selected outgoing root. No unselected family is assumed to have positive weight at every external parameter.

For the imaginary part define the regularized integrand

\[
Y_{\rm reg}(k)=\operatorname{Im}\sum_\sigma h_\sigma f_A
 +\sum_j c_j\cot\frac{k-k_j}{2}.
\]

Each added cotangent has exactly zero principal-value integral on a full circle. Hence

\[
\boxed{\operatorname{Im}F_2=\int_{-\pi}^{\pi}Y_{\rm reg}(k)\frac{dk}{2\pi}.}
\]

The selected outgoing root is the already known unique plus-pulse root with `|K-k_j|<1/100`. Its numerator is directly

\[
\rho_{2,b,+}=|c_{\rm selected}|/(2\pi).
\]

Thus the same certified root and residue used in the full denominator also provide the selected numerator. All other roots remain in `F2`.

#### 3.3 A numerical root midpoint cannot replace the actual root in PV subtraction

An interval Newton certificate must define the unique exact root `r` in its enclosure. Subtracting a cotangent centered at a decimal approximation leaves a residual pole and is not a valid quadrature remainder.

In a pole collar use the exact identities

\[
H(r+s)=s\widehat H(s),\quad
\widehat H(s)=\int_0^1H'(r+\theta s)d\theta,
\quad A(s)=B(r+s)/\widehat H(s).
\]

The singular part then becomes the regular function

\[
-\frac{A(s)-A(0)}s
 +c\left(\cot(s/2)-2/s\right),\qquad
c=A(0)/2.
\]

The second bracket is analytic with series `-s/6-s^3/360-...`; the first is an ordinary divided difference. A Taylor enclosure, or an integral derivative bound, evaluates it including `s=0`. Its center value is

\[
-\frac{B'(r)}{H'(r)}+\frac{B(r)H''(r)}{2H'(r)^2}.
\]

This construction remains valid with `r=r(K,E)` in a uniform root tube. The physical variation of that root across the external rectangle must not be confused with numerical root-enclosure error.

### 4. Geometry certification before integration

Cover the entire integration circle for both pulse signs, uniformly over the complete frozen external rectangle. A cell is accepted only if the physical denominator is separated from zero, if the open-continuum pole exclusion of Part I applies, if the strict-gap H value excludes zero, or if the cell is contained in an already certified strict-gap monotone root cover.

A root cover requires strict physical-gap membership, a separated H derivative and opposite endpoint signs uniformly over K,E. These conditions prove exactly one root for every external parameter pair. Interval Newton refinement encloses that same root family. The physical variation of its location is retained. Overlapping root tubes are merged only after a separated derivative on the union of their original covers proves they represent the same root family; their refined enclosures can then be intersected. Every part of the circle outside an accepted cover remains in the census queue until independently certified.

The scalar denominator remains authoritative near thresholds. Its algebraic interval enclosure includes the real and imaginary square-root arcs on the required physical sheet. Pole/edge coincidence is excluded analytically in Part I. If interval dependency still prevents finite classification, the fixed-budget census returns INCONCLUSIVE. No critical strip, external cell or inner pole is silently discarded.

### 5. Cheapest first certificate: uniform interval ranges on the small external window

First try one external box `I_K x I_E`. Enclose `F1` and the complete `F2` uniformly there, together with the positive incoming and selected outgoing densities. Do not perform a two-dimensional numerical integration unless this uniform enclosure is too broad.

For each regular integration panel `J`, use the rigorous range enclosure

\[
\int_J f(k)dk\ \in\ |J|\,f(J).
\]

Sum these enclosures with outward rational arithmetic. Their width includes the full quadrature uncertainty. Bisect the panel contributing the largest remaining width; use a fixed deterministic tie break. Pole collars use the divided-difference enclosure above. Bounded edge collars can be integrated by a range enclosure without differentiated square roots.

This rule needs no differentiated square-root endpoint and no radial-limit remainder. The present pin uses only one external box. Physical K,E variation is included in each interval value. Further inner subdivision may stop improving its width; the fixed resource and disposition contract below then applies without changing the source window.

### 6. Turn the enclosures into an absolute probability immediately

For each external rectangle `X=J_K x J_E` obtain

\[
\rho_{\rm in}\in[a_-,a_+],\quad \rho_{2,b,+}\in[b_-,b_+],
\quad |4+F_1F_2|^2\in[D_-,D_+],\quad D_->0.
\]

Then its contribution is bounded by its exact normalized area times

\[
\frac{64\pi^2a_-b_-}{D_+}\le\mathcal P(K,E)
\le\frac{64\pi^2a_+b_+}{D_-},\qquad
\text{area weight}=\frac{|J_K||J_E|}{4\pi h}.
\]

For one full external box the area weight is `delta_K/pi`. The incoming density may use CP-24:

\[
\rho_{\rm in}(E)=\frac\delta\pi\rho(0,E-\beta)(1+\eta),
\qquad |\eta|<\delta^2.
\]

The exact center identities provide checks, not substitutes for this enclosure:

\[
\rho(0,\omega_*)=\frac{\sqrt{45\varphi-35}}{2\pi(9\varphi-2)},\qquad
v_0=\sqrt{(4\varphi-3)/5},\qquad
\rho_{2,b,+}(k_0,E_*)=\frac{1-v_0}{4\pi v_0}.
\]

For the denominator use complex interval arithmetic and the inherited identity

\[
|4+F_1F_2|^2\ge16\operatorname{Re}F_1\operatorname{Re}F_2>0.
\]

This positivity bound prevents a spurious interval zero from blocking the upper probability bound. The verifier intersects the direct squared-modulus lower bound with this positive lower bound. It keeps the direct safe upper bound; no sampled corner search is used.


## Part III. Exact local pole cancellation used by the verifier

Let r be the unique exact root in a certified strict-gap monotone cover, and let the entire segment between k and r lie in that cover. For each fixed K,E write d=k-r. Taylor's integral identities give

\[
H(k)=d\widehat H,\qquad
\widehat H=H'(r)+dA,\qquad
A\in\tfrac12H''(\operatorname{hull}(k,r)),
\]
\[
B(k)=B(r)+dC,\qquad
C\in B'(\operatorname{hull}(k,r)),\qquad
\widehat H\in H'(\operatorname{hull}(k,r)).
\]

Consequently the ordinary continuous extension of the canceled quotient satisfies

\[
-\frac{B(k)}{H(k)}+\frac{B(r)}{H'(r)d}
=\frac{B(r)A-H'(r)C}{H'(r)\widehat H}.
\]

The right-hand side has no division by d. Its interval evaluation therefore includes k=r and the complete parametric root tube. The missing difference between `2/d` and the periodic cotangent has the elementary bound

\[
\left|\cot(d/2)-\frac2d\right|\le\frac{|d|}{5}
\qquad (|d|\le1).
\]

For x=|d|/2<=1/2, `sin x-x cos x = integral_0^x t sin t dt <= x^3/3`, while `sin x >= x-x^3/6`. Thus

\[
\frac1x-\cot x\le\frac{x}{3(1-x^2/6)}\le\frac{8x}{23}<\frac{2x}{5}.
\]

The odd extension proves the claim for either sign; d=0 follows by continuity. The verifier uses the stricter distance `|d|<=1/8`, a separated derivative throughout the segment, and containment in the certified gap cover. A distance cutoff without that containment would not justify differentiation across an object threshold.

For every other root, the exact interval-defined cotangent remains in the integrand. Away from all local collars the full boundary expression and all cotangents are evaluated directly. A denominator containing zero forces subdivision or a controlled INCONCLUSIVE outcome; no approximate pole center is substituted.

## Part IV. Fixed arithmetic, complete coverage and disposition

`interval_core.py` encloses real numbers on the dyadic grid `Z/2^96`. Its stored endpoints are integers. Addition is exact on the grid; multiplication and division use directed integer floors and ceilings. Integer square roots certify both square-root endpoints. Complex arithmetic and second derivatives are built from these outward operations. The latter store actual derivatives, not Taylor coefficients.

Pi is enclosed by `16 atan(1/5)-4 atan(1/239)`, using 40 alternating terms for each arctangent and a first-omitted-term remainder. Trigonometry uses certified reduction by pi/2, 24 Taylor terms on a reduced argument with absolute value at most one, and remainders `|r|^49/49!` for sine and `|r|^48/48!` for cosine. Endpoint enclosures are supplemented by every possible internal extremum, including uncertainty in pi. No binary floating-point operation decides a scientific assertion.

The external rectangle is fixed in its entirety. The total-momentum center k0 is isolated from its defining cosine by interval bisection and a derivative enclosure, with a maximum permitted enclosure width of `10^-20`. It is not replaced by a decimal approximation.

The finite census covers `u=k/pi in [-1,1]` for both pulse signs. It starts with 64 panels per sign and uses at most 4096 uncached model evaluations. Root covers can expand at most 9 times. Parametric interval Newton refinement takes at most 16 steps. A census cell narrower than `2^-40` in u that remains unresolved ends the audit as INCONCLUSIVE. A complete census must identify exactly one plus-pulse root wholly inside the original selected outgoing interval and with a strictly positive residue lower bound. All other certified roots remain in the full function.

Both integrals use outward range sums, not sampled quadrature. F1 uses `P=pi u`, `u in [0,1]`, exploiting its exact evenness. F2 uses `k=pi u`, `u in [-1,1]`, with the exact factor 1/2 in the normalized measure. Both start with 64 panels. At each refinement the panel with the largest sum of component interval widths is bisected; unresolved panels have priority and insertion order breaks ties. The respective final panel budgets are 1024 and 4096. Early width targets are 1/100 for F1 and 1/20 for the regularized F2. Reaching a panel budget with every panel bounded still gives a valid range sum, even if its early width target was not met. Any unresolved panel instead produces INCONCLUSIVE.

The final probability enclosure uses the complete F1 and F2, the incoming finite-width bound CP-24, the selected outgoing pole from the same full census, and the exact external normalized measure delta_K/pi. It is intersected with the inherited full-event bounds

\[
\frac{2}{10^{28}}<P_0<\frac{8}{5\pi\,10^6}.
\]

An exact rational comparison `U<=10L`, with L>0, is the predeclared target. A wider complete enclosure is reported as INCONCLUSIVE with that enclosure. If interval domain separation or the finite census/integration budgets are insufficient, the complete inherited full-event enclosure is retained and the unresolved reason is printed. A partial F2 is never reported as complete.

A technical exception, nonzero exit, nonempty stderr or process timeout is not a scientific INCONCLUSIVE result. It is an incomplete execution governed by the repository's abandoned-pin policy. The accepted code and all inputs must remain unchanged after their public pin. The first completed stdout and its exact hashes determine the recorded disposition; repeated tuning on this identifier is excluded.

The package is a conditional mathematical/computational certificate for one prepared source and one joint event. Even a successful absolute interval does not fix physical units, identify an electron or another particle, supply a native port-preparation law, or select the laboratory apparatus.
