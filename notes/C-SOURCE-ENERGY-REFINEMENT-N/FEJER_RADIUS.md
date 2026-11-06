# Positive Fejer energy and a smaller certified physical radius

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1782](https://github.com/mathorn1973/twist-j/issues/1782).
The prospective [CONTRACT.md](CONTRACT.md) is frozen at
`d69ff34274ffce191055df7fd44e092366e20819`.
Independent scientific acceptance is not asserted.

This note keeps the original energy branch, source pair and physical
occupation encoding. It replaces the predecessor's sufficient polynomial
degree by a smaller proved degree. The new estimate integrates the squared
energy error directly against the source measure, rather than first
requiring a tiny separate finite-moment certificate. All formulas below
are analytical; no moments, matrices or numerical spectra were computed.

## 1. Fixed source measure and the positive polynomial

Use the frozen U=U_rec and Q=E0 f(U), where

    f(exp(-i theta))=theta,  0<=theta<2pi,  f(1)=0.

The exact source family is

    psi_±(Xi)=[I±(U²-U^-²)]chi(Xi)/sqrt(Z),
    Z=(39521+154 sqrt(5))/15625.

Its common normalized spectral measure mu is independent of all 26
old-memory labels and arbitrary passive references. With an orthogonal
retained setting register, the same measure and every bound below apply
to coherent setting-memory-reference inputs; mixed inputs are covered
by purification. The original fresh-write contrast additionally requires
the stated 25-label old-memory subspace excluding d0. An arbitrary
unmarked superposition of the two phase vectors is not added to this
contract.

The [sharpened source estimate](SHARP_SPECTRAL.md) supplies

    F(x):=mu{|1-z|<=x} <= A x,
    A=512,       0<x<=h=1/1000.                     (F1)

In particular mu({1})=0. No fitted density or altered source is used.

For an integer J>=2 define the Fejer kernel and finite energy polynomial

    K_J(t)=(1/J)|sum_(k=0)^(J-1) exp(ikt)|²,

    q_J(z)=pi-i sum_(k=1)^(J-1)
                     (1-k/J)(z^k-z^-k)/k.          (F2)

The polynomial has Laurent degree D=J-1. The kernel is nonnegative and
even, has integral 2pi on [-pi,pi], and has Fourier coefficients
1-|k|/J for |k|<J and zero otherwise. The Fourier coefficients of the
sawtooth give the exact convolution identity

    q_J(exp(-i theta))
      =(1/(2pi)) integral_(-pi)^pi
           K_J(t) f(exp(-i(theta-t))) dt.           (F3)

The assigned value of f at its one discontinuity does not affect this
Lebesgue integral. Since 0<=f<=2pi, positivity of the kernel gives

    0<=q_J(z)<=2pi,       |z|=1.                    (F4)

The finite coefficients are exact rational expressions and pi, not
coefficients claimed to lie in the native cyclotomic integer ring.

## 2. A pointwise error identity and its source L2 bound

For 0<theta<=pi, the only wrap of theta-t with t in [-pi,pi] occurs when
t>theta. Apart from endpoints of measure zero,

    f(exp(-i(theta-t)))=theta-t+2pi 1_(t>theta).

The first moment of the even kernel vanishes. Subtracting theta from
(F3) therefore gives the exact identity

    q_J(exp(-i theta))-theta=integral_theta^pi K_J(t) dt.

For pi<=theta<2pi, reflection gives its negative counterpart. Put
d=min(theta,2pi-theta) and x=|1-exp(-i theta)|=2sin(d/2). Then

    |q_J(exp(-i theta))-theta|=integral_d^pi K_J(t) dt
      <= min(pi, 2cot(d/2)/J)
      <= min(pi, 4/(J x)).                          (F5)

Indeed half of the total kernel mass is pi, and
K_J(t)<=1/[J sin²(t/2)] gives the second bound by direct integration.
This derivation keeps the cancellation of the linear part of f; no
additional tail or truncated-series error is needed.

At z=1, q_J(1)=pi while f(1)=0. This is not a change of the original
energy convention. The error at that single point is pi, consistent
with the first bound in (F5); (F1) proves that the actual source has no
weight there.

Set delta_J=||[q_J(U)-f(U)]psi|| on any admitted normalized source.
The common spectral measure makes this quantity independent of the
setting and old-memory/reference input. The layer-cake formula, (F5)
and (F1) imply

    delta_J² <= 8pi A/J + 16/(J²h²).                (F6)

Here is the full estimate. The squared pointwise error is at most pi².
For 0<u<=pi², its superlevel set lies in
{|1-z|<4/(J sqrt(u))}. Split the integral over u at
u0=16/(J²h²). Below u0 use total mass at most one. Above u0 use (F1),
giving an integral at most

    u0+(4A/J) integral_(u0)^(pi²) u^(-1/2) du
       <= u0+8pi A/J.

If u0>=pi², the trivial bound delta_J²<=pi² already proves (F6).
This uses only the stated cut-mass bound, including its finite window;
no bound on the rest of the spectral density is required.

## 3. One fixed degree with the original energy tolerance

Choose

    J=2^35,       D=2^35-1.                        (F7)

Equations (F1) and (F6), with pi<4 and 16*10^6<2^24, give

    delta_J² < 2^-21+2^-46
       < (4/3)2^-21
       = 1/(3*2^19)
       < 1/1200².                                  (F8)

The final comparison is the integer inequality
3*2^19=1572864>1440000=1200². Thus the fixed positive polynomial obeys

    ||[E0 q_J(U)-Q]psi|| < E0/1200.                (F9)

This is a completed analytical sufficient bound. It is not an executed
moment test, a numerical optimization, or a lower bound on the degree
that is actually necessary. Since q_J(U) and f(U) commute,

    ||[exp(-is q_J(U))-exp(-is f(U))]psi||
       <= |s|delta_J,       s=E0 t/hbar.             (F10)

Both phase settings have exactly the same complete E0 q_J(U) spectral
law, because q_J is one fixed function of the same U and their complete
U laws agree. This does not identify that common law exactly with the
original-Q law.

There is still no global operator-norm convergence. In fact (F5) gives
||q_J(U)-f(U)||<=pi, and equality holds when sigma(U) is the full circle.
The continuous q_J has value pi at one, whereas the two one-sided limits
of f are zero and 2pi. Every nonempty open arc has a nonzero spectral
projection for a full-circle spectrum. Taking shrinking arcs gives the
lower bound pi, even if there is no spectral atom at one. This statement
concerns the infinite-coordinate polynomial, not optimality of its
finite physical realization.

## 4. Centered time comparison and a smaller spatial block

Use the exact periodic coordinate unitary U_L and basis inclusion A_L
of
[PR1781 PHYSICAL_BLOCK.md](https://github.com/mathorn1973/twist-j/blob/5f7301e4d891596628cb25c6e735a7e4cd9004a8/notes/C-FINITE-OCCUPATION-ENERGY-N/PHYSICAL_BLOCK.md).
The source vectors are unchanged whenever L>=7. That proof gives

    A_L U_L^k chi_L=U^k chi       for |k|<L.

Choose the Taylor order and radius

    m=47,       L=47D+3.                            (F11)

Then every polynomial power of degree at most mD, applied to either
source whose defining powers are at most two, agrees exactly between
the finite and infinite systems. This includes powers of

    p_J=q_J-pi I,       ||p_J||<=pi.

Centering is only a comparison device. The physical energy remains the
positive h_L=E0 q_J(U_L); it is not shifted to E0 p_J(U_L). In the two
exponentials the same scalar phase exp(-is pi) cancels. Comparing the
centered exponential series through order 47 therefore gives, for
|s|<=3,

    ||A_L exp(-is q_J(U_L))psi_L
                    -exp(-is q_J(U))psi||
       <= eta_47(3pi),
    eta_47(x)=2 sum_(k=48)^infinity x^k/k!.           (F12)

There is a short exact bound. Since 3pi<12, the ratio of successive
terms from index 48 onward is less than 12/49<1/4. Also
48!>(48/e)^48 and e<3. Consequently

    eta_47(3pi)<4*(36/48)^48
       =4*(3/4)^48
       <4/3^12
       <2^-17.                                     (F13)

The last two comparisons use 3^5=243<256=4^4 and
3^12=531441>524288=2^19. No numerical exponential-tail calculation
is used.

Combining (F10)-(F13) yields the full finite-time bound

    ||A_L exp(-it h_L/hbar)psi_L-exp(-itQ/hbar)psi||
       < 3/1200+2^-17,       |E0 t/hbar|<=3.         (F14)

It includes unknown occupied memory, passive references, retained
orthogonal settings and every outcome branch. The vector bound implies
the same trace-distance bound and is preserved by any common complete
output instrument. It does not control normalized states after an
arbitrarily rare selected outcome.

At s=3, the original endpoint is U^3. Each of the two receiver
probabilities changes by less than 3/1200+2^-17. The inherited write
contrast therefore satisfies

    Delta_L > 1/50-6/1200-2^-16
            =3/200-2^-16 >1/100.                   (F15)

The same final receiver effect and the same 25-label memory condition
are used. The exact full energy-law equality of the two finite sources
also remains valid: U_L^2-U_L^-2 is skew-adjoint and commutes with every
spectral function of q_J(U_L), as in the predecessor proof.

## 5. Original occupation support, imperfections and scope

The original occupation isometry places this finite coordinate box in
the physical interval

    Lambda_L={97-2L,...,97+2L},
    |Lambda_L|=4L+1=188(2^35-1)+13
                     =6459630813009.               (F16)

This is about 6.46*10^12 lattice sites. The same finite code has dimension
8112(2L+1)^3, retains its original phase gauge and receiver at 100, and
has active occupation charge 10. The positive finite-block extension
of PR1781 transfers (F9) and (F14)-(F15) to the original physical
occupation space. Any other raw extension that intertwines that entire
code exactly has the same comparisons on these inputs. A different
completion on other charge sectors must be separately specified.

For the same additional imperfections allowed in the predecessor, take
complete input trace-distance error zeta<=1/8000, a self-adjoint actual
generator with ||H_actual-H_ideal||<=E0/24000, and final receiver-effect
operator error at most 1/4000. Duhamel's bound adds at most
zeta+3/24000<=1/4000 to the state error through |s|<=3. The two-setting
contrast then loses at most 4/4000=1/1000 in total, giving

    Delta_actual>3/200-2^-16-1/1000>1/100.           (F17)

These are sufficient tolerance requirements, not achieved precision.
Generic perturbations need not preserve the exact equality of the
entire energy distributions; that identity belongs to the ideal law.

The source error target and the >1/100 contrast are unchanged. The
explicit boundary allowance is now 2^-17 rather than the predecessor's
much smaller 2^-62; this deliberate reallocation is included in (F14)
and leaves the complete contrast budget valid. The polynomial degree
falls from 1024*10^25 to 2^35-1, and the sufficient spatial count falls
from 520192*10^25+13 to (F16). These are reductions of upper bounds,
not a proof that trillions of sites are necessary or a hardware plan.

This note supplies neither a short-range decomposition nor source
preparation, a terminal clock, a funded detector, renewal or a native
six-pentit derivation. The independent interaction construction must
count its raw supports, norms, incidence and geometric diameter without
changing the meaning of (F9).

## 6. Separate review obligations

1. Check the common source measure, the all-26-label versus fresh-write
   memory scopes, and applicability of the sharpened cut-mass estimate.
2. Check the Fourier signs, convolution identity, finite degree and
   positivity on the whole unit circle.
3. Check the exact wrap identity, the half-kernel bound pi, the constant
   4 in (F5), and the retained value f(1)=0.
4. Check the squared-error layer-cake estimate including the finite
   window h, possible endpoints, and the case u0>=pi².
5. Check the dyadic degree and every strict inequality in (F8), with
   no moment calculation or fitted constant.
6. Check source/reference uniformity, continuous-time comparison and
   exact equality of the two complete setting energy laws.
7. Check finite prefix agreement, centered polynomial powers, the
   scalar-phase cancellation and the factorial tail at order 47.
8. Check the original occupation radius and site count, full-state
   comparison, two-setting contrast and additional error budget.
9. Check the exact global norm statement only for q_J(U), the changed
   boundary allowance, and the distinction between a sufficient size
   bound, interaction geometry and practical realization.

All new conclusions remain conditional analytical candidates. These
same-session derivations do not constitute independent acceptance.
