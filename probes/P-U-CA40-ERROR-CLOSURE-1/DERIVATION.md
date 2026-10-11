# A posteriori error closure for the frozen sine comparison

PUBLIC NON-CANONICAL. Conditional L1 mathematics for reservation #1458,
`P-U-CA40-ERROR-CLOSURE-1`. This proof was prepared without scientific
execution or imports. Earlier finite calculations are exposed inputs, not
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

## 7. Floating-point enclosure is part of the theorem's premises

The fast AVX-512/80-worker propagator may use ordinary floating arithmetic
to propose p. The certificate may not assume its transcendental functions
are correctly rounded. Scalar model data, trigonometric/exponential
coefficients, Gauss nodes/weights, prefactors, tails and tube constants
are enclosed by directed MPFR arithmetic, then converted outward to
binary64 endpoints. The
[MPFR manual](https://www.mpfr.org/mpfr-current/mpfr.html#Rounding)
specifies its directed rounding semantics; importing a runtime through
an ABI binding does not itself verify the surrounding interval code.

The guard residual uses audited outward vector arithmetic, including
complex products, square roots of Fock ladder factors, polynomial
evaluation, all sums and final norms. Embedded directed AVX operations
or an independently proved normwise error analysis must cover every
operation actually used. Ordinary round-to-nearest plus a guessed epsilon
does not suffice. Disable flush-to-zero/denormals-are-zero, disallow
unaccounted reassociation and contraction, and check each worker's mode.
Any NaN, overflow, unsupported rounding instruction, failed coefficient
enclosure or non-positive tail denominator prevents a finite certificate.

The jump norms, final complex overlaps, restoration displacement and
Gaussian linear reference require the same care. A proof of the interior
defect does not cover an unvalidated endpoint reduction. Report the
separate error components so a wide enclosure is distinguishable from
a detected physical-model difference.

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
columns; interval arithmetic has additional cost. A four-hour workload
budget, if selected by PREREG.md, is a resource limit and not a guarantee
of a narrow bound. It is legitimate to finish with a finite but vacuous
bound, an unmet radius target, or an incomplete resource-limited record.

Do not infer rigor from step-size agreement, small norm drift, small
sampled residual, nominal guard closure or high precision alone. The
claim requires the explicit continuum remainder, infinite displacement
tail, arithmetic enclosures, endpoint jumps, restoration phase and thermal
mass account above, all evaluated for the same frozen pulse word.
