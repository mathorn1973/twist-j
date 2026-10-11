# Norm-ball error closure for the frozen sine comparison

PRIVATE PRE-PIN DRAFT. Conditional L1 mathematics for reservation #1460,
`P-U-CA40-BALL-CLOSURE-1`, on authority base
`c2459261aa15552e6560753dd8e1753f5164972d`.
This proof was prepared without scientific
execution or imports. It preserves the earlier model and changes the
planned hot residual arithmetic. No scientific execution is asserted
by this draft. Earlier finite calculations are exposed inputs, not
new evidence of the bounds below. The pulses are unchanged. Numerical
configuration values and resource limits are fixed separately in PREREG.md.

## 1. Exact model and the reference frame

Keep the preceding seven harmonic axial modes, five repeated 100-us loops,
sixteen amplitude segments per loop, ideal instantaneous X5 carriers, and
the six cases: active labels `(4,3),(4,4),(1,1)` for each angle envelope.
Physical ion order is `(s,x,u,y,w,q,r)`. Only ions 4 and 5 respond; all five
protected electronic registers remain exactly dark by assumption.

Every decimal input token denotes its exact rational value. Pi, square
roots, trigonometric functions and exponentials have their mathematical
values and are enclosed numerically; their ordinary binary64 evaluations
do not redefine the model. In particular,

```text
k = 2 pi / wavelength,
kappa_mi = k b_mi sqrt(hbar/(2 mass omega_m)),
eta_mi = kappa_mi exp(i k x_i),
X_i(t) = sum_m kappa_mi [a_m exp(-i omega_m t)
                        + a_m^dagger exp(i omega_m t)],
chi_i(t) = k x_i - mu t,
s_i(z,l) = 1[z_i+l=0 mod 5], i=4,5,
H_S/hbar = 2u sum_i s_i [sin(chi_i+X_i)-sin chi_i],
H_L/hbar = 2u sum_i s_i cos(chi_i) X_i.                 (1)
```

Recorded mode frequencies and mode vectors are selected model constants,
not certified eigenvalues or uncertain apparatus measurements. The stored
legacy eta table is rounded independently of kappa. It is therefore not
substituted for the coherent eta in (1). Report a certified uniform maximum
of the entrywise discrepancies; if a legacy-reference result is compared,
account for the resulting change of linear frame separately. Agreement to a decimal
tolerance is not an exact algebraic identity.

For `g_m=sum_i eta_mi s_i`, the full two-frequency linear force is

```text
f_m=u[g_m exp(i(omega_m-mu)t)
      +conj(g_m) exp(i(omega_m+mu)t)],
dot(alpha_m)=-i f_m,
dot(Phi)=Im sum_m dot(alpha_m) conj(alpha_m),
U_L=exp(i Phi)D(alpha).                                (2)
```

In `W=U_L^dagger U_S`, the exact moving-frame equation is

```text
i dot(W)=R(t)W,
m_i=2 sum_m kappa_mi Re[alpha_m exp(-i omega_m t)],
R=2u sum_i s_i [sin(chi_i+m_i+X_i)-sin chi_i
                -cos(chi_i)(m_i+X_i)].                (3)
```

Absolute time, alpha and Phi are continuous across loops and dark intervals.
When both responses vanish, R=0 and W is constant; the clock still advances.
The shared unary compensation and the previously proved endpoint common
phase do not permit an intermediate clock or bus reset.

## 2. Enclosing the full-linear prefix

For a constant segment starting at real t0, let
`nu_-=omega-mu`, `nu_+=omega+mu`,
`c_-=u g exp(i nu_- t0)`, `c_+=u conj(g) exp(i nu_+ t0)`.
For a duration d, define entire functions with continuous zero limits:

```text
J(nu,d)=integral_0^d exp(i nu v) dv
       =d sinc(nu d/2) exp(i nu d/2),
K(a,b,d)=integral_0^d exp(i a v) integral_0^v exp(-i b w)dw dv,
K(a,b,d)=[J(a,d)-J(a-b,d)]/(i b), b nonzero,
K(a,a,d)=|J(a,d)|^2/2+i[d/a-sin(a d)/a^2], a real nonzero,
K(a,0,d)=d exp(i a d)/(i a)+(exp(i a d)-1)/a^2,
K(0,0,d)=d^2/2.                                      (4)
```

The diagonal expression in (4) is used for real d. The defining integral
or an equivalent entire continuation defines complex arguments. Advance

```text
Delta alpha_m=-i sum_(r=+,-) c_mr J(nu_mr,d),
Phi_new=Phi_old+Im sum_m [Delta alpha_m conj(alpha_old,m)
                         +sum_(r,s) c_mr conj(c_ms)K(nu_mr,nu_ms,d)],
alpha_new=alpha_old+Delta alpha.                       (5)
```

Compute these prefixes with outward enclosures. Small or zero denominators
require their continuous limits or a proved series enclosure, not an
uncontrolled cancellation. Do not invoke the old rotating-wave closure to
erase a full-linear displacement. The same formulas can enclose a second
legacy-eta reference and its endpoint Gaussian coherence difference, without
repropagating nonlinear dynamics or retuning either pulse.

## 3. A polynomial is an approximation, not an asserted exact solution

Let P_L project onto total occupation `sum_m n_m<=L`; its dimension is
`binomial(L+7,7)`. All seven modes remain present. A numerical integrator
produces a piecewise polynomial p(t) in P_L. Its stored finite coefficients
are interpreted as exact dyadic numbers. Their rounding, the accuracy of
stage states and derivative estimates, and the integrator's local error
are all charged through the subsequent defect; none is assumed negligible.

The intended reconstruction is quintic Hermite on theta=(t-t0)/h. With
approximate endpoint values y0,y1, slopes F0,F1, and approximate second
derivatives A0,A1, form

```text
c0=y0; c1=h F0; c2=h^2 A0/2;
A=y1-c0-c1-c2; B=h F1-c1-2c2; C=h^2 A1-2c2;
c3=10A-4B+C/2; c4=-15A+7B-C; c5=6A-3B+C/2;
p(t)=sum_(j=0)^5 c_j theta^j.                        (6)
```

The coefficients actually stored, not a fictitious exact floating update,
define p. Approximate A may be formed by a central directional difference
of F with delta=h/128, extending the same constant segment on both sides.
This is a construction device and introduces no unproved derivative
accuracy premise. It may affect whether the final defect bound is useful.

Roundoff can make `p(t0+h)` differ from saved y1. Charge its rigorously
enclosed norm as a jump, including the last endpoint if y1 is the reported
state. Also charge any mismatch at a force switch or frame change. An
alternative exact endpoint correction would have to be included in p and
its derivative. Silent normalization or silent replacement of an endpoint
does not satisfy this contract.

For the full-space residual `F(t)=i p'(t)-R(t)p(t)`, unitarity gives

```text
||psi_true(T)-y_saved(T)||
 <= initial_mismatch + sum_cells integral_cell ||F(t)||dt
                      + sum_jumps ||jump||.           (7)
```

This follows by differentiating the exact unitary variation-of-constants
expression on each smooth piece and applying the triangle inequality.
There is no exponential stability factor. Finite Fock vectors belong to
the domain needed here; (3) is a bounded sine term plus a linear oscillator
operator, and its propagator is defined by the full sine and known linear
unitaries. Equation (7) accounts for time, dynamic cutoff and evolution
roundoff together, provided its residual, integrals and jumps are enclosed.

## 4. Guard-space residual with a controlled infinite tail

At real time set `beta_im=i kappa_mi exp(i omega_m t)`, so

```text
exp(i X_i)=D(beta_i),
sin(A_i+X_i)=[exp(i A_i)D(beta_i)
              -exp(-i A_i)D(-beta_i)]/(2i), A_i=chi_i+m_i.
```

Normal ordering gives the true projection, not an exponential of a
truncated X matrix:

```text
P_G D(beta) P_L
 = exp(-||beta||^2/2) P_G exp(beta.a^dagger)
                         exp(-conj(beta).a) P_L.      (8)
```

The annihilation polynomial terminates after L. Creation only raises
occupation, so the projected creation polynomial terminates after G;
discarded paths cannot return. This proves (8) exactly.

Operators belonging to distinct modes commute, so either exponential in
(8) may equivalently be applied as the product of its seven one-mode
exponentials. Intermediate P_L projections during annihilation and P_G
projections during creation are exact for the same monotonicity reason.
The annihilation result and its grade norms in (9) are unchanged. This is
an algebraic implementation equivalence, not a measured speed claim.

Take G>=L+1 and compute the interval-enclosed guard residual
`d_G=i p'-P_G R p`. It preserves cancellation between the sine and linear
terms before taking its norm. Only sine displacement terms reach Q_G.
For either sign of beta, write

```text
y=exp(-conj(beta).a)p=sum_(j=0)^L y_j,
b=||beta||, K_j=G-j+1,
t_(j,k)=b^k sqrt((j+k)!/j!)/k!,
q_j=b sqrt(j+K_j+1)/(K_j+1).
```

Whenever an outward bound proves q_j<1,

```text
||Q_G D(beta)p||
 <= exp(-b^2/2) sum_(j=0)^L ||y_j|| t_(j,K_j)/(1-q_j)
 =: T(beta,p).                                        (9)
```

To prove (9), rotate modes so beta.a^dagger=b c^dagger. On total grade j,
`||(beta.a^dagger)^k y_j||<=b^k sqrt((j+k)!/j!)||y_j||`.
Successive series terms have ratio `b sqrt(j+k+1)/(k+1)`, decreasing in k.
The first omitted term and its geometric majorant give (9). No occupation
rotation is applied to the physical input; it only proves the norm bound.
Failure to establish q_j<1 invalidates that shortcut; it must not be hidden
by division through an interval containing zero.

For real time the scalar sine phases have modulus one. Hence

```text
T_R=|u| sum_i |s_i| [T(beta_i,p)+T(-beta_i,p)],
||F(t)|| <= sqrt(||d_G||^2+T_R^2).                    (10)
```

The two terms are orthogonal projections of the full residual. Formula
(10) avoids subtracting two nearly equal full norms. A finite guard alone
is not a full-space bound: the tail in (9) is mandatory. G=L+2 or a larger
guard is a computational choice to freeze in PREREG.md, not a new model.

## 5. A concrete full-Hilbert analytic tube bound

This section supplies a bound between quadrature nodes. On one cell let
t* be its midpoint, a=h/2, and choose a Bernstein ellipse parameter rho>1.
For the scaled ellipse set

```text
r_ell=a(rho+rho^-1)/2,
y_ell=a(rho-rho^-1)/2.
```

Every point z in the ellipse obeys `|z-t*|<=r_ell` and
`|Im z|<=y_ell`. Continue the current constant-amplitude/response formula
analytically. The real integration cell never straddles a switch. The
analytic continuation may extend beyond that segment's real boundary;
it is the same fixed segment formula, not the discontinuous physical
piecewise function evaluated across its next switch.

All conjugated time functions use reflection: for example
`alpha_tilde(z)=conj(alpha(conj(z)))`. It is holomorphic and equals
conj(alpha) on real time. Taking the complex conjugate of z inside the
formula without this reflection would destroy the argument. In particular,

```text
m_i(z)=sum_m kappa_mi [alpha_m(z)exp(-i omega_m z)
                       +alpha_tilde_m(z)exp(i omega_m z)].
```

The following quantities are conservative outward bounds, with real
omega_m>0, mu>0, and alpha and m at the real midpoint rigorously enclosed:

```text
F_m=|u g_m| [exp(|omega_m-mu| y_ell)
             +exp((omega_m+mu)y_ell)],
A_m=|alpha_m(t*)|+r_ell F_m,
J_i=2 sum_m |kappa_mi| exp(omega_m y_ell) (F_m+omega_m A_m),
b_i^2=sum_m kappa_mi^2,
B_i^2=sum_m kappa_mi^2 exp(2 omega_m y_ell),
D_i=exp(-b_i^2/2+B_i^2/2+2 B_i sqrt(L)),
C_i=B_i [sqrt(L)+sqrt(L+1)].                          (11)
```

Here F_m bounds both analytic force reflections, A_m bounds both alpha
reflections, and J_i bounds |m_i'|. Integrating on a vertical segment in
the ellipse yields `|Im m_i(z)|<=y_ell J_i`; integrating from the midpoint
also gives `|m_i(z)|<=|m_i(t*)|+r_ell J_i`.

For completeness the displacement estimate in (11) is not an appeal to
complex-time unitarity. At complex time its normal-ordered form has
creation coefficients c_m=+/-i kappa_mi exp(i omega_m z) and annihilation
coefficients d_m=+/-i kappa_mi exp(-i omega_m z). Their scalar product is
`c.d=-b_i^2`, but c and d are not negative conjugates. On P_L,

```text
||exp(d.a)P_L|| <= exp(||d||sqrt(L)),
||exp(c.a^dagger)P_L||
 <= exp(||c||^2/2+||c||sqrt(L)).
```

The second inequality follows by inserting a real-time unitary D(c) in
normal ordering; the preceding annihilation still maps into P_L. Since
both coefficient norms are <=B_i, the full displacement bound is D_i.
Similarly `||X_i(z)P_L||<=C_i`.

Combining the scalar sine/cosine bounds gives

```text
||R(z)P_L|| <= H_rho,
H_rho=2|u| sum_i |s_i| {
 D_i exp[y_ell(mu+J_i)]
 +exp(mu y_ell)[1+|m_i(t*)|+r_ell J_i+C_i] }.          (12)
```

Write the exact polynomial in centered powers x=(z-t*)/a as
`p(z)=sum_(k=0)^d v_k x^k`. Rigorous interval conversion from the stored
theta coefficients is permitted. With r=(rho+rho^-1)/2, let

```text
P_rho=sum_k ||v_k|| r^k,
Pprime_rho=(1/a) sum_(k>=1) k ||v_k|| r^(k-1),
M=Pprime_rho+H_rho P_rho.                             (13)
```

Then `||F(z)||<=M` on the full complex ellipse, in the full infinite
oscillator Hilbert space. It is deliberately conservative and can be
vacuous. A larger rho improves the geometric factor below but increases
the exponentials and polynomial bounds in (11)-(13); neither effect may
be silently discarded.

Equivalently, the implementation can use the stored theta powers directly:
`r_theta=1/2+(rho+rho^-1)/4`,
`P_rho=sum_k ||c_k|| r_theta^k`, and
`Pprime_rho=(1/h)sum_(k>=1) k||c_k|| r_theta^(k-1)`.
These follow from theta=(x+1)/2 and avoid a coefficient conversion. The
same M formula applies, with every operation rounded outward.

## 6. Positive Gaussian quadrature without sampling assumptions

Take n=N+1 Gauss-Legendre nodes in the cell and positive normalized weights
w_j summing to one. Enclose each exact node and weight by directed scalar
arithmetic with verified root isolation. Let b_j be a proved upper bound
for the full residual norm at that exact node, using (8)-(10), node
uncertainty and vector-arithmetic enclosures.

The bound used here is

```text
integral_cell ||F(t)||dt
 <= h [sqrt(sum_j w_j b_j^2)
       +4 M rho^(-N)/(rho-1)].                        (14)
```

Proof: the degree-N Chebyshev series truncation A_N of an analytic
Hilbert-valued F has uniform error
`E<=2 M rho^(-N)/(rho-1)`. The standard scalar coefficient proof uses
contour integrals and the triangle inequality and therefore applies in
Hilbert norm without a dimension factor. Let Q_N interpolate exact F at
the Gauss nodes. Since ||Q_N||^2 is a real polynomial of degree at most
2N, Gauss quadrature integrates it exactly. Further,

```text
||F-Q_N||_L2(average)
 <=||F-A_N||_L2(average)+||I_N(F-A_N)||_L2(average)
 <= E+sqrt(sum_j w_j E^2)=2E.
```

Cauchy-Schwarz and the exact norm-square quadrature give (14).
This does not apply Gaussian quadrature directly to the nonanalytic
function ||F|| and assume it exact. It also avoids storing a large vector
interpolation polynomial merely to integrate its norm. Sixteen nodes
mean N=15; the analytic remainder and all node errors are still required.
Outward upper weights may sum to more than one numerically; use them in
the final upper sum, while the mathematical exact weights sum to one.
The kernel may retain separate nonnegative guard and tail accounts,
replacing `sqrt(sum_j w_j b_j^2)` by
`sqrt(sum_j w_j guard_j^2)+sqrt(sum_j w_j tail_j^2)`.
This follows from the triangle inequality in the weighted Euclidean norm;
it is a potentially looser upper bound, not an equality assertion.

For the analytic Chebyshev coefficient bound, see Trefethen's primary
[ATAP Chapter 8](https://github.com/chebfun/ATAP/blob/development/chap8.m).
The Gaussian norm-interpolation application and full-Hilbert bounds above
are derived explicitly here rather than attributed to that reference.

## 7. Floating centers with rigorous Euclidean error balls

The hot guard residual uses ordinary binary64 center vectors and rigorous
scalar Euclidean radii. MPFR still encloses the exact model, nodes, phases,
prefactors, tail coefficients and analytic tube constants. The directed
interval endpoint/jump/Gram path is retained unless an equally complete
norm-ball enclosure is explicitly substituted. No ordinary transcendental
evaluation is assumed exact. All scalar bound arithmetic is outward.

The operational vector representation is a stored dyadic center x_hat,
N>=||x_hat|| and r>=||x_true-x_hat||. N bounds the stored center rather
than the exact vector. No intermediate state is normalized.

### 7.1. Exact one-mode operators and dimension-free norm bounds

Let P_d project onto total phonon number at most d in seven modes. For one
mode, all other occupations are fixed spectators. The operator therefore
splits into chains of lengths at most d+1. Its full-chain coefficient
matrices, with occupations n,j=0,...,d, are

```text
C_d(beta)[n,j] = beta^(n-j)/((n-j)!) sqrt(n!/j!), n>=j,
A_d(beta)[n,j] = (-conj(beta))^(j-n)/((j-n)!) sqrt(j!/n!), j>=n.
```

Creation uses d=G, annihilation d=L. Shorter chains are principal blocks
of these matrices. Thus no high-dimensional matrix is needed for their
norm bounds. For any nonnegative matrix B, define the Schur majorant

```text
S(B) = sqrt(max_row sum B * max_column sum B).
```

If |T_nj|<=B_nj, then ||T||_2<=S(B), including the direct sum of all
shorter chains. This follows from weighted Cauchy-Schwarz, or the usual
||T||_2^2<=||T||_1||T||_infinity inequality applied to the absolute matrix.
It has no sqrt(binomial(d+7,7)) dimension penalty.

With b=|beta|, phases are removed by diagonal unitary matrices; the
annihilation and creation positive matrices are transposes. Define S_d(b)
as the Schur majorant of C_d(b). It bounds both operator norms. It can be
cached for fixed b,d. Useful looser checks are

```text
||C_d(beta)|| <= sum_(k=0)^d b^k/k! sqrt(d!/(d-k)!) <= exp(b sqrt(d)).
```

This is an alternative operator-norm bound, not an ordering assertion
about the numerical Schur value. Either upper bound is valid, and their
minimum may be used: ||C_d(beta)|| <= min(S_d(b), polynomial_bound).

The same bounds hold for exp(sum beta_m a_m) or its projected creation
counterpart with b=sqrt(sum |beta_m|^2). A unitary rotation of modes maps
that linear combination to b times one ladder and preserves every total
occupation projector. This is only a norm proof, not a change of physical
modes. For the frozen Xi, |beta_m|=|kappa_mi| is time independent.

### 7.2. Coefficient uncertainty stays in small matrices

At an exact Gauss node enclosed in a scalar interval, compute small
complex coefficient intervals enclosing the mathematical entries above.
Let c_hat[n,j] be the exact binary64 values actually used by the fast
triangular action. They may be obtained by its ordinary powers/products;
their accuracy is not assumed. Bound each complex discrepancy by

```text
Delta[n,j] >= sup |c_exact[n,j]-c_hat[n,j]|,
delta_A = S(Delta).
```

Then ||(A_exact-A_hat)x||<=delta_A ||x||. Enclose the two component
differences and their Euclidean norm outward. This accounts for power,
factorial-root and coefficient-multiplication rounding as well as node
and model uncertainty. It does not depend on the correctness of ordinary
libm. The exact structural diagonal is one; its discrepancy is zero.

The target table uses the same exact beta as the Hamiltonian and the
Gaussian prefactor. Independently rounded coefficient dictionaries cannot
silently redefine that model. Intervals may lose coefficient correlations
without invalidating this upper bound, although they can become wider.

### 7.3. A rigorous non-FMA complex row-dot bound

Assume round-to-nearest binary64, gradual underflow, no overflow, finite
operands and the explicitly frozen operation order used by the current
non-FMA triangular action. Let epsilon=2^-53 and
gamma_k=k epsilon/(1-k epsilon), with k epsilon<1.

Each real or imaginary row accumulator starts with its exact dyadic
diagonal input. Each of q off-diagonal complex terms uses two products,
one signed sum, and one accumulator addition. A product contribution
passes through at most q+2 rounding operations; the initial diagonal
passes through q. The usual product-of-(1+delta) argument therefore gives

```text
|roundoff_vector| <= gamma_(q+2) H |x_realified| + underflow_vector,
```

where H is the entrywise absolute realification of A_hat. For a complex
entry c_hat its nonnegative 2x2 block has entries |Re c_hat| and
|Im c_hat|. Its real row/column sums are obtained from the small scalar
matrix B_hat[n,j]=|Re c_hat[n,j]|+|Im c_hat[n,j]|. Consequently, with
N>=||x|| and q<=d,

```text
roundoff_norm <= gamma_(d+2) S(B_hat) N + U_d,D.
```

This is a per-thermal-column bound. Eight independent SIMD lanes do not
introduce an additional sqrt(8). Rows with q=0 are exact copies.

Relative error alone is invalid for subnormal results. A safe general
model is |fl(z)-z|<=epsilon |z|+eta, with eta=2^-1074 (deliberately larger
than half the smallest subnormal). Each real row has at most 4d scalar
operations. A conservative absolute allowance for D complex outputs is

```text
U_d,D = sqrt(2D) * 4d eta / (1-(d+2)epsilon).
```

All scalar evaluations of gamma, Schur sums/products, roots and this
allowance must themselves round outward. Keeping eta symbolically or
using the smallest positive binary64 with upward operations avoids
rounding the allowance silently to zero. If any intermediate overflows or
becomes nonfinite, the certificate fails. Compiler contraction, a changed
dot-product order or FTZ/DAZ requires a new justified arithmetic contract.

For an ordinary center action y_hat=fl(A_hat x_hat), its local error is

```text
ell_A <= [delta_A + gamma_(d+2) S(B_hat)] N + U_d,D.
```

This compares A_exact x_hat with y_hat; x_hat itself is an exact dyadic
vector. For an input ball ||x_true-x_hat||<=e, the usual safe recurrence
is e_out<=S(A_exact)e+ell_A. However the next section is often tighter.

### 7.4. Do not amplify the input ball through all fourteen factors

Write beta=(beta_1,...,beta_7), g=exp(-||beta||^2/2). The true projected
displacement is P_G D(beta)P_L and has norm at most one. Therefore an
initial curve-evaluation ball e_0 contributes at most e_0 to the final
displacement error. It need not be multiplied by fourteen triangular
operator bounds. Bound only newly generated local arithmetic/coefficient
errors through their remaining exact suffixes.

Let b_<=j^2=sum_(m<=j)|beta_m|^2 and b_>j^2=sum_(m>j)|beta_m|^2. After
annihilation mode j, a local error still belongs to P_L. Including the
final Gaussian, its exact suffix can be written

```text
g P_G C_all A_>j P_L
 = exp(-b_<=j^2/2) P_G C_<=j D_>j P_L.
```

Here the already processed and remaining modes commute. Creation cannot
bring a component above G back into P_G, so P_G can be inserted between
C_<=j and D_>j. Since projected D_>j is contractive, a valid suffix norm is

```text
w_ann,j = exp(-b_<=j^2/2) S_G(b_<=j).
```

After creation mode j a local error is in P_G. Only remaining creation
factors and the Gaussian remain, with suffix norm

```text
w_cre,j = g S_G(b_>j).
```

These identities use the projected true displacement and monotone
creation, not exponentials of projected position operators. Thus

```text
e_D <= e_0 + sum_j w_ann,j ell_ann,j
            + sum_j w_cre,j ell_cre,j + ell_gaussian.
```

For an actual center scalar g_hat and final product center x_hat,
ell_gaussian <= (|g-g_hat|+epsilon |g_hat|)||x_hat||
               +sqrt(2D) eta.
Its factors are bounded outward. A direct fourteen-factor recurrence is
also rigorous but may be unnecessarily pessimistic.

The annihilation half needed by the outside-guard tail is not unitary.
For its center y_hat, a separate valid radius is

```text
e_annhalf <= S_L(||beta||) e_0
            +sum_j S_L(b_>j) ell_ann,j.
```

Each exact grade norm can then be bounded by
||P_j y_true||<=||P_j y_hat||_up+e_annhalf. This is conservative because
it gives every grade the whole error; grade-wise balls can improve it.
One must not substitute the final displacement's contractive input bound
for this nonunitary half. Insert these grade bounds into the unchanged
analytic infinite creation-tail formula.

The implementation can sharpen this without grade-wise balls. Let t_j
be the nonnegative, outward-enclosed coefficient multiplying the grade
norm in (9), including its Gaussian factor. Since the grade projections
are orthogonal, Cauchy-Schwarz gives

```text
sum_j t_j ||P_j y_true||
 <= sum_j t_j ||P_j y_hat||_up
    +sqrt(sum_j t_j^2)*e_annhalf.
```

This is the implemented tail form. It is valid for the global half-radius
from either the simple recurrence or a separately proved tighter one.

### 7.5. Curve evaluation, residual subtraction and norm reductions

The quintic coefficients are exact dyadic vectors. Evaluate a center at a
binary64 theta_hat and enclose its polynomial roundoff separately. Scalar
node uncertainty r_theta contributes at most

```text
r_theta sum_(j=1)^5 j ||c_j|| max(|theta|,|theta_hat|)^(j-1).
```

A non-FMA Horner bound uses gamma_10 times the corresponding coefficient
norm polynomial, plus absolute underflow allowances. Treat the derivative
and exact 1/h scaling similarly, including any rounding in integer-times-
coefficient operations. The existing small interval model preparation
still encloses all physical phases and scalar coefficients at the node.

Compute the center F_hat=i p_hat'-R_hat p_hat by the actual sequence of
complex scales and sums, retaining cancellation in that center. Bound its
error by the input and displacement balls, the small scalar-coefficient
uncertainties, ladder-action roundoff and final scaling/summing roundoff.
For a generic scalar product a v, a safe local coefficient contribution is
|a-a_hat| ||v_hat||, input contribution |a| e_v, plus the explicitly
bounded RN multiplication error. For a sum, add the operand radii and a
gamma bound on the actual center summation. No small observed cancellation
is used to reduce an error ball without proof.

The linear ladder part needs no exponential. On P_L,
||beta.a||<=||beta||sqrt(L),
||conj(beta).a^dagger||<=||beta||sqrt(L+1).
For interval/uncertain ladder coefficients use the same formulas with
the Euclidean coefficient-error norm. Their sparse row-dot rounding can
be bounded by the realified Schur construction above.

Finally ||F||<=||F_hat||_up+e_F. A cheap directed-up norm reduction of the
center is sufficient; it is not a full interval-vector evolution. An
ordinary RN reduction is usable only with its actual reduction-tree gamma
and underflow bound. The same requirement applies to every N and grade
norm above. No silent normalization is allowed.

The full node residual may combine the finite guard and analytic tail by
sqrt(guard_upper^2+tail_upper^2). Equivalently, the implementation may use
the more conservative separate weighted node norms
sqrt(sum w_j guard_j^2)+sqrt(sum w_j tail_j^2), as permitted in Section 6.
This is the chosen implementation form; the triangle inequality in the
weighted Euclidean norm proves it. The existing Gauss norm-interpolation
proof and full-Hilbert ellipse allowance still cover the continuum. A
pointwise center/ball estimate alone does not certify time integration.

### 7.6. What can and cannot be reused

The candidate's floating displacement routine can be reused as a center
calculation if its exact operation order and the exact stored coefficient
values are exposed to the checker. A candidate's already computed action
on a different RK stage vector cannot replace the action on the quintic
Gauss-node vector. Common routines are not an independent implementation;
small dense/collective exact or enclosed fixtures remain useful.

Small matrices are at most (G+1)x(G+1). Norm-ball validation removes large
interval endpoints, but still needs center displacement evaluations,
norm reductions and honest coefficient uncertainty. Efficiency and bound
sharpness have not been measured. Main possible failure points are
inflated coefficient balls, nonunitary tail-half bounds, scalar residual
cancellation error, large analytic continuum allowance and implementation
drift in the promised floating operation trace.

The unchanged final account uses unnormalized thermal weights, certified
approximate endpoint norms and the non-unit Gram inequality. The thermal
tail remains an independent floor. This proposal does not turn the
predecessor's incomplete run into a certificate, certify trap physics,
or justify replacement execution under that predecessor's identifier.



### 7.7 Frozen simple recurrence interface

The previous subsections prove both a simple product recurrence and
optional sharper suffix bounds. The planned implementation may use the
following deliberately conservative simple version. For each actual
stored small coefficient table Chat let

```text
S=Schur(|Chat|), E=Schur(entrywise complex coefficient-error radii),
q_max >= largest number of off-diagonal terms in a row,
k=4*q_max+8, epsilon=2^-53, eta=2^-1074,
gamma=k*epsilon/(1-k*epsilon), rho=sqrt(2)*gamma*S,
U=sqrt(2D)*k*eta/(1-k*epsilon),
r_new <= (S+E)*r+(E+rho)*N+U,
N_new <= (S+rho)*N+U.                                (B1)
```

Taking q_max=d+1 is safe. The actual row's longest relative-error path
is at most q+2 and its real scalar operation count at most 4q. Thus k
bounds both. The nonnegative realification matrix has norm at most
sqrt(2)S; this proves rho. The absolute underflow errors accumulate
through at most k relative factors, proving U. It is per thermal column,
not multiplied by the number of SIMD lanes. Formula (B1) needs no
intermediate high-dimensional center norm reductions.

The implemented sparse ladder uses another valid choice of S and E.
For a fixed mode its nonzero entries form an injective weighted shift:
distinct occupied inputs map to distinct outputs. Its norm is therefore
at most the largest magnitude of its stored entry, and the coefficient
error operator has the analogous maximum-radius bound. Summing over the
seven modes gives

```text
S=sum_m max_k |Chat_(m,k)|,
E=sum_m max_k coefficient_radius_(m,k).
```

These also bound the norm of the corresponding entrywise-magnitude
operators by the triangle inequality. Their nonnegative realifications
have norm at most sqrt(2) times these bounds. There are at most seven
complex summands per row, so (B1) with q_max=7 covers the implemented
sparse ladder, including restricted-support creation and annihilation.

Here E includes coefficient-center generation rounding, mathematical
coefficient uncertainty and the enclosed node's uncertainty. A small
complex-ball implementation of coefficient arithmetic is acceptable if
its primitive radii include all rounding and underflow. The center
coefficient must be exactly the dyadic value used in the vector kernel,
not an independently computed ideal or nearby value.

For the final real Gaussian scalar g with center ghat and radius rg,

```text
r_new <= (|ghat|+rg)*r+rg*N
         +epsilon*|ghat|*N+sqrt(2D)*eta,
N_new <= (1+epsilon)*|ghat|*N+sqrt(2D)*eta.             (B2)
```

The implemented real scaling uses the conservative replacements
epsilon -> gamma_1 and sqrt(2D)*eta -> U_1, where
U_k=sqrt(2D)*k*eta/(1-k*epsilon). Both replacements increase the bound.

For a real Horner scalar theta with center thetahat and radius rt,
stored exact coefficient vector c, and directed center norm bounds
Ny,Nc, define

```text
rho_H=gamma_2*(|thetahat|*Ny+Nc)
      +sqrt(2D)*2*eta/(1-2*epsilon),
r_new <= (|thetahat|+rt)*r_y+rt*Ny+rho_H,
N_new <= |thetahat|*Ny+Nc+rho_H.                       (B3)
```

The center is the actual non-FMA fl(thetahat*yhat+c). If c itself is
uncertain, add its radius. This includes the cross term rt*r_y. Dual
Horner evaluates the derivative using d_new=theta*d+p_old before the
polynomial update; then enclose multiplication by exact 1/h.

A generic complex scalar a with center ahat and radius ra multiplying
a vector ball has input/coefficient radius (|ahat|+ra)r+ra*N. Its
ordinary non-FMA complex multiplication adds at most
sqrt(2)*gamma_2*|ahat|*N+sqrt(2D)*3*eta/(1-2*epsilon).
A vector sum adds both operand radii and the ordinary addition error
epsilon*(Na+Nb)+sqrt(2D)*eta. These give a complete route for residual
subtraction without ignoring center cancellation or scalar uncertainty.
An implementation may use a proved larger operation count.

In particular, the implemented compound complex axpy updates
yhat <- fl(yhat+ahat*xhat). Each real output component uses two products,
one signed sum and one final addition, with a longest rounding path of
three operations. The conservative count k=12 bounds both this path and
the number of possible local underflow contributions. With directed
center-norm bounds Nx,Ny, define

```text
local=gamma_12*(Ny+sqrt(2)*|ahat|*Nx)+U_12,
r_new <= r_y+(|ahat|+ra)*r_x+ra*Nx+local,
N_new <= Ny+|ahat|*Nx+local.
```

The sqrt(2) factor comes from the nonnegative realification of complex
multiplication. The coefficient radius ra already includes the exact
stored midpoint's discrepancy from the coefficient interval. Operand
centers and radii are read before overwriting, including an aliased
input; thus the same bound applies to the actual compound operation.

Use directed norm reductions for coefficient vectors, residual centers,
annihilation-half grades and jumps. An RN reduction needs its own
operation-tree proof; no guessed tolerance is permitted. All nonfinite,
overflow, FTZ/DAZ or invalid-tail conditions prevent certification.
Scalar outward results must remain valid under actual scalar rounding,
including the smallest positive underflow allowance.

The jump compares the stored polynomial with the actual saved endpoint,
including the last serialized endpoint. Neither algebraic Hermite
interpolation nor small measured norm drift removes this obligation.
The full-Hilbert Gauss/ellipse allowance and analytic outside-guard tail
remain unchanged. Final restoration and complex-coherence intervals
retain their directed path, and their arithmetic halfwidth is included
in the total pair radius.

The reported sampled_arithmetic_node_L2 is the weighted node diagnostic
formed from e_F. This radius is already included in every guard bound;
the diagnostic is not added again to the total and has no independent
continuous-time enclosure. The same limited interpretation applies to
the separate sampled time and projection node diagnostics. Only the
combined guard/tail account plus its full-Hilbert continuum allowance
and endpoint jumps constitutes the branch certificate.

## 8. Thermal and observable error budget

Retain the original unequal thermal weights
`p_n=(20/21)^7(1/21)^|n|` for |n|<=3, without normalization. There are 120
columns and exact retained mass q. The omitted mass is
`p_tail=680046581/794280046581`. Thermal truncation is independent of the
dynamical and arithmetic account above.

For case z let e_(z,n) be the certified bound (7) to the saved endpoint,
and define outward bounds

```text
E_z=sqrt(sum_ret p_n e_(z,n)^2),
A_z=sqrt(sum_ret p_n ||y_(z,n)||^2).
```

Restore the branch-dependent linear frames:

```text
U_L,b^dagger U_L,a=exp(i theta_ab)D(alpha_a-alpha_b),
theta_ab=Phi_a-Phi_b+Im sum_m conj(alpha_b,m)alpha_a,m,
Gamma_hat_ret=sum_ret p_n <y_b,n|U_L,b^dagger U_L,a|y_a,n>,
Gamma_L=exp(i theta_ab)
         exp[-sum_m(nbar_m+1/2)|alpha_a,m-alpha_b,m|^2].
```

No independent branch phase fit is allowed. Exact nonlinear vectors have
norm one, but approximate vectors need not. The retained dynamical Gram
error is bounded by

```text
E_Gram <= min(sqrt(q) E_a+A_a E_b,
              sqrt(q) E_b+A_b E_a).                  (15)
```

This follows by adding and subtracting one mixed exact/approximate
overlap and applying weighted Cauchy-Schwarz. Replacing (15) by E_a+E_b
without controlling approximate norms is unjustified.

Add independently enclosed restoration/evaluation error E_restore and
linear-reference evaluation error E_linear. For an approximate complex
center Delta_hat=Gamma_hat_ret-Gamma_L_hat, the physical two-branch
Bell-input trace distance obeys

```text
R_pair=(p_tail+E_Gram+E_restore+E_linear)/2,
max(0,|Delta_hat|/2-R_pair) <= D_pair
 <= min(1,|Delta_hat|/2+R_pair).                       (16)
```

The center magnitude itself must be outward enclosed or its evaluation
error included. The numerical objective is R_pair<=1e-3 for both angle
envelopes on the frozen panel, not a promised outcome. Because the
thermal radius is already about 4.28e-4, the remaining error budget is
limited. A wider result remains a valid but unsuccessful closure attempt.

## 9. Scope, feasibility and failure conditions

This method can turn the former heuristic comparison into a controlled
infinite-harmonic-bus statement for the selected electronic panel. It
does not certify physical trap modes, laser implementation, finite
carrier pulses, heating, scattering, radial motion, anharmonicity or a
complete work reservoir. Protected electronic/source-reference identity
still follows only from exact darkness. The full informative-contact
source obstruction remains separate.

The main new cost is the validated residual at all quadrature nodes in
the guard space, not the 120 thermal labels by themselves. Sparse ladder
polynomials avoid dense displacement matrices. Per-node work scales with
the guard dimension binomial(G+7,7), the ladder order and the number of
columns; the proved norm-ball arithmetic also has overhead. A frozen workload
budget, if selected by PREREG.md, is a resource limit and not a guarantee
of a narrow bound. It is legitimate to finish with a finite but vacuous
bound, an unmet radius target, or an incomplete resource-limited record.

Do not infer rigor from step-size agreement, small norm drift, small
sampled residual, nominal guard closure or high precision alone. The
claim requires the explicit continuum remainder, infinite displacement
tail, arithmetic enclosures, endpoint jumps, restoration phase and thermal
mass account above, all evaluated for the same frozen pulse word.
