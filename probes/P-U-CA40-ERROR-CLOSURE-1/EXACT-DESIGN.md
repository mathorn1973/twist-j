# Exact audit and numerical-certificate boundary

PUBLIC NON-CANONICAL. Conditional L1 mathematics. Apache-2.0, A. M. Thorn.
Reservation: https://github.com/mathorn1973/twist-j/issues/1458.
Authority baseline: `287494a553963c8fa254d085a9a8358b1a3fe83a`.

The pulse envelopes and conditional sine/full-linear question are inherited
from `P-U-CA40-SINUS-COMPARISON-1`. A larger motional carrier and a validated
error account are new work. This file and its verifier were prepared without
scientific execution or importing candidate scientific code. The complete
new source/data/certificate contract must be publicly pinned before a run.

There are two different checks. The standard-library `verify.py` audits
finite exact identities and counterexamples supporting the error account.
The interval implementation must separately validate the actual recorded
trajectories. An exact fixture PASS does not imply a valid trajectory
certificate, a successful numerical tolerance or a physical result.

## 1. What must be certified

For each declared branch z, retain the full-linear moving frame
`U_S,z=U_L,z W_z` and the exact seven-mode generator R_z in DERIVATION.md.
The approximate curve p_z,n(t) lives in total-occupation space P_L and
starts from a specified retained thermal Fock input n. It may come from
AVX-512/OpenMP computation. Treat every recorded finite binary coefficient
as an exact dyadic datum when reconstructing that curve.

For a piecewise continuously differentiable finite-Fock curve, unitarity
and variation of constants give

```text
||psi(T)-p(T)|| <= ||psi(0)-p(0)||
                    + sum_j ||p(t_j+)-p(t_j-)||
                    + integral_0^T ||i p'(t)-R(t)p(t)|| dt.       (1)
```

The initial mismatch, jumps and residual are all needed. No stability
exponential is necessary for the exact self-adjoint Schrödinger generator.
Finite Fock polynomials lie in the required oscillator domains; the
conditional full dynamics and their unitary moving frame are as derived
in DERIVATION.md. An artificial finite matrix is not substituted for that
generator in the full-space residual.

Equation (1) accounts for propagation roundoff without assuming that the
propagator used correctly rounded elementary functions: the recorded
curve is merely the proposed approximation. The certificate evaluator,
however, must rigorously enclose R, the residual and its integral. An
ordinary floating residual calculation cannot serve as that evaluator.

The current candidate uses the quintic Hermite reconstruction in
DERIVATION.md. The verifier checks its six exact endpoint value/slope/second-
derivative identities without assuming the supplied derivative estimates are
accurate. It also audits the following simpler cubic RK4 reconstruction in
local coordinate theta in [0,1], to expose endpoint/jump bookkeeping:

```text
b1=theta-3theta^2/2+2theta^3/3,
b2=b3=theta^2-2theta^3/3,
b4=-theta^2/2+2theta^3/3.
```

Its exact endpoint is the exact dyadic expression of the recorded stage
data, and need not equal the recorded rounded update. Either retain that
jump in (1), or add theta times the endpoint discrepancy to the polynomial
and include its time derivative. The verifier checks both the endpoint
identity and the nonzero correction; it does not assert a dense-output
accuracy order or excuse its residual.

An explicit sampling counterexample uses H=0 and
`p'(t)=t^2(t-1/2)^2(t-1)^2` on [0,1]. The residual vanishes at 0, 1/2 and 1,
but its integral is exactly 1/840, greater than 1/1000. A small residual at
the RK nodes cannot certify a continuous integral.

## 2. Finite guard and the infinite displacement tail

Let B=`sum_m conj(beta_m) a_m`, b=`||beta||`, and p in P_L. Define
`v=exp(-B)p=sum_(j=0..L) v_j`, where v_j is its total-degree-j shell.
The annihilation exponential is finite on P_L. Normal ordering gives

```text
D(beta)p = exp(-b^2/2) exp(B^dagger)v.                  (2)
```

A unitary rotation of the oscillator modes writes B^dagger=b c^dagger
for one normalized mode c. On the total-degree-j subspace its occupation
is at most j. Therefore, for every integer k>=0,

```text
||(B^dagger)^k v_j||
 <= b^k sqrt((j+k)!/j!) ||v_j||.                       (3)
```

The bound is attained by a state with all j quanta in that one mode.
For a guard G>=L, put K_j=G-j+1. All terms with k<K_j remain inside P_G,
so the omitted tail is bounded by

```text
||Q_G D(beta)p||
 <= exp(-b^2/2) sum_j ||v_j|| sum_(k>=K_j) t_(j,k),
t_(j,k)=b^k sqrt((j+k)!/j!)/k! .                       (4)
```

The successive ratio is `q_(j,k)=b sqrt(j+k+1)/(k+1)` and decreases in k.
If a certified upper bound qbar for q_(j,K_j) is strictly below one, then
the series is at most `t_(j,K_j)/(1-qbar)`. If not, a predeclared finite
prefix must be included before a valid geometric tail begins. A failed
denominator or exhausted bound computation means NOT_CERTIFIED.

For interval b use its upper endpoint in the powers and ratios and its
lower endpoint in `exp(-b^2/2)` when constructing an upper bound. Shell
norms must also be upper bounds for the same time/node/model domain.
Discarding high shells, substituting shell populations for displacement
tails, or treating a finite guard as the complete Hilbert space is invalid.

The exact verifier compares guard normal-order coefficients with an
independent multinomial formula and a larger ambient carrier. It uses the
unnormalized Fock basis `(a^dagger)^n|0>` with metric n!, avoiding square
roots in those comparisons. There are 16 columns and 300 entries. It also
checks 25 shell-power bounds, their aligned saturation and rational
decreasing-ratio inequalities for 117 guard/shell choices. The Gaussian
prefactor remains formal; the verifier does not evaluate transcendental
displacements or actual trajectory tails.

For G>=L+1, the linear quadrature and constant terms of R p cannot reach
Q_G. Compute the finite guard defect

```text
d_G=i p'-P_G R p,
T_R=|u| sum_i |s_i| (T_i,+ + T_i,-),
||i p'-R p|| <= sqrt(||d_G||^2+T_R^2),                (5)
```

where T_i,+/- bound (4) for the two displacement signs. P_G and Q_G are
orthogonal, explaining the square sum. This preserves cancellation of
sine and linear terms inside the guard without subtracting two nearly
equal full/projected norms. It also avoids requiring an exact cancellation
between the separately bounded tails outside the guard.

Using no explicit guard and a triangle bound at G=L is mathematically
possible, but it discards potentially important sine/linear cancellation.
The actual guard and all resource caps belong to the frozen PREREG.

## 3. Validated time integration of the defect

For a cell, let F(t)=i p'(t)-R(t)p(t). A sufficient quadrature lemma uses
its Hilbert-valued holomorphic extension to a Bernstein ellipse E_rho,
rho>1, after mapping the cell to [-1,1]. Suppose ||F||<=M throughout that
ellipse, with M certified for the full Hilbert space.

Let q be the degree-N interpolant of F at the N+1 Gauss-Legendre nodes.
For the normalized positive weights w_j, sum w_j=1,

```text
||q||_(L2 average)^2 = sum_j w_j ||F(x_j)||^2.          (6)
```

This holds because ||q(x)||^2 is a real polynomial of degree at most 2N.
A degree-N Chebyshev truncation a has uniform error
`E<=2 M rho^(-N)/(rho-1)`. Gauss exactness and positive weights imply
`||I(F-a)||_(L2 average)<=E`; hence `||F-q||_(L2 average)<=2E`.
If b_j are rigorous upper bounds on the full node norms, then

```text
integral_cell ||F|| dt
 <= h [sqrt(sum_j w_j b_j^2)+4 M rho^(-N)/(rho-1)].     (7)
```

The real integration cell cannot straddle an amplitude/response switch.
The ellipse uses analytic continuation of that same fixed segment formula,
even beyond its real segment boundary; it never switches to the next
piecewise formula inside the ellipse. All conjugated real-time expressions
must use their holomorphic reflected
continuations; complex conjugation of the time argument is not analytic.
Real-time unitary displacement norm one cannot be reused at complex time.
The full-space M bound and complex continuation are substantive obligations,
not inferred from small real-node values.

Node/weight enclosures, model arithmetic and bounds on M require validated
arithmetic. An enclosing node interval may be passed through the residual
evaluator, accounting for node-location uncertainty. Ordinary approximate
nodes or weights are not made exact by calling a rule Gauss-Legendre.

The exact audit uses the three-point algebraic rule with nodes
`0,+/-sqrt(15)/5` and weights `4/9,5/18,5/18`. Arithmetic in Q(sqrt(15))
checks all moments through degree five and a vector-polynomial norm square.
It also checks positive-weight stability and the factor four in (7).
The actual high-order node enclosures and ellipse majorant are deliberately
outside this fixture verifier and must pass the certificate preparer.

## 4. Thermal, endpoint and pair error budgets

The retained thermal set K=3 contains 120 initial vectors with exact
weights `p_n=(20/21)^7(1/21)^|n|`. Its retained mass q and omitted mass are

```text
q=793600000000/794280046581,
p_tail=680046581/794280046581.                          (8)
```

Use the unnormalized weights. The omitted contribution to any normalized
unitary branch overlap lies in a complex disc of radius p_tail. The
retained overlap itself is not normalized, and the bus purification echo
is not an Uhlmann fidelity or a direct protected-source measurement.

Let e_z,n certify `||psi_z,n-p_z,n||` and A_z,n bound `||p_z,n||` at the
endpoint. For exact unitary frame restoration V_ab, the error of one
approximate Gram matrix element is at most

```text
min(e_a,n+A_a,n e_b,n, e_b,n+A_b,n e_a,n).              (9)
```

The often used e_a+e_b bound presupposes normalized approximate vectors.
The verifier's counterexample psi_a=psi_b=1, p_a=p_b=6/5 has vector errors
1/5 each but Gram error 11/25, larger than 2/5. Equation (9) is attained.

Sum (9) with the exact p_n. Alternatively put
`E_z=sqrt(sum p_n e_z,n^2)` and `A_z=sqrt(sum p_n ||p_z,n||^2)`;
the aggregate is bounded by
`min(sqrt(q) E_a+A_a E_b, sqrt(q) E_b+A_b E_a)`.
No extra thermal-rank or seven-mode dimension multiplier is introduced.

The different full-linear frames must still be restored:

```text
V_ab=exp(i[Phi_a-Phi_b+Im(conj(alpha_b).alpha_a)])
     D(alpha_a-alpha_b),
Gamma_S,ret=sum p_n <p_b,n|V_ab|p_a,n>.                (10)
```

For finite endpoint vectors the true projected displacement matrix
elements can be evaluated directly by normal ordering. Their numerical
evaluation, parameter and frame uncertainty must be bounded. Denote the
combined bound on retained dynamics/restoration/evaluation by E_S and the
certified error in the full analytic linear overlap by E_L. With center
`dhat=|Gammahat_S,ret-Gammahat_L|/2`, a total pair-distance enclosure is

```text
[max(0,dhat-r), min(1,dhat+r)],
r=(p_tail+E_S+E_L)/2,                                 (11)
```

including the rounding of the center itself or using a complex-ball
modulus enclosure directly. Reporting a total interval requires every
term; an omitted error source cannot be silently set to zero.

For threshold 1/1000, upper endpoint <= threshold means WITHIN_TARGET;
lower endpoint > threshold means EXCEEDS_TARGET; otherwise UNRESOLVED.
This decision is separate from certificate validity and resource completion.
The verifier's rational decision fixtures are toys, not angle predictions.
Actual two-sign claims require actual certificates and the frozen branch
panel. They do not cover all 25 branches or the full 56-G contact.

## 5. Full roundoff and custody obligations

The exact model definition must be frozen. In particular, the input contains
rounded spatial eta coefficients as well as data from which kappa and
`exp(i k x)` are reconstructed. A numerical 1e-12 consistency tolerance is
not an exact identity. The interval checker must enclose the model actually
declared in PREREG/DERIVATION, including the interpretation of decimal data,
pi, square roots and redundant coefficients. Certifying a rounded surrogate
requires explicitly naming that different target; it cannot happen silently.

The certificate also covers arithmetic in vector norms, linear phases,
Gaussian factors, tail denominators, weights, quadrature remainders and
final accumulation. Reject nonfinite data. Freeze precision, deterministic
subdivision/precision caps, node preparation and all library/build versions.
If a required enclosure cannot be established or its precision/resource cap
is exhausted, retain NOT_CERTIFIED or INCOMPLETE as appropriate. A valid but
wide final enclosure remains a valid bound; its accuracy/target verdict may
be UNRESOLVED. None of these outcomes licenses changing a frozen tolerance.

MPFR provides correctly rounded operations with specified rounding modes:
https://mpfr.org/mpfr-current/mpfr.html. FLINT/Arb ball arithmetic describes
rigorous error propagation and its dependency limitations:
https://flintlib.org/doc/using.html. Its integration discussion is at
https://flintlib.org/doc/arb_calc.html. These are framework references, not
claims that merely using a named library validates this application.
Converting a double to an exact ball certifies its stored value, not the
unknown mathematical value that originally produced it.

This implementation computes the interval certificate online. Retain the
frozen source and input, binary, endpoint states, per-column error bounds
and components, environment, failure and output receipts. The complete
quintic coefficient arrays and node interval arrays are not retained.
Consequently, auditing those intermediate curves requires recomputation;
the retained endpoint and bound records alone do not permit an independent
offline replay of every certificate step. A deterministic full replay from
the pinned sources and declared environment is possible, but is not a
blinded audit or an independent replication. Large retained data need the
repository's declared source/version/license/hash manifest route; do not
publish private infrastructure metadata or arbitrary binary payloads.
An exact CI fixture replay must never be described as replaying the much
larger interval calculation when it does not consume its evidence.

The auxiliary protected-register identity remains conditional on exactly
zero response and ideal return. The unknown-source/full-informative-contact
obstruction, physical realizability and complete work accounting are unchanged.
No hardware admission or Canon promotion follows from this audit.

The verifier accepts no arguments, reads no files and prints one sorted
ASCII JSON line with explicit LF. Its output expressly denies having
checked an actual trajectory certificate. EXPECTED.txt must come from the
first completed publicly pinned exact run, never an invented pre-run output.
