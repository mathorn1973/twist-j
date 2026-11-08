# Exact finite audit inventory

Status: prospective, NON-CANONICAL, L1. These are disclosed analytical
witnesses, not blind predictions. No scientific execution preceded the pin.
The universal assertions and the s -> 0 limit require PROOF.md.

The accepted standalone `verify.py` uses only standard-library Fraction,
integer square root, and degree-two one-variable formal Taylor arithmetic.
It neither integrates an orbit nor fits floating-point data. It reads no
external file, invokes no process and writes no file. The command is
`python3 -I probes/P-RELATIONAL-MASS-INERTIAL-RESPONSE-1/verify.py`.

## Complete deterministic inventory

1. **24 full-action field fixtures.** Six matrices L, in this order:
   `I, diag(2,1), [[1,1],[0,1]], [[1,0],[1,1]], [[0,-1],[1,0]],
   [[2,1],[1,1]]`. For each use all four Euclidean stream pairs
   `((3,4),(5,12)), ((5,0),(-3,4)), ((0,2),(0,-3)),
   ((3,4),(-3,-4))`. Set G=LL^T, Pi=L^-T [[1,-1],[-1,2]] L^-1,
   r=L(2,-1), X=L(1,3), p_i=L^-T q_i, P=p1+p2, rho=p1-p2.
   Differentiate the complete Hamiltonian coordinate by coordinate by exact
   automatic differentiation, with the Frobenius off-diagonal factors 1/2.
   Compare the resulting field to the closed equations; check Pdot=0,
   Hdot=0, full Jdot=0 and internal jdot=-Xdot P^T.
2. **54 directional Hessian fixtures.** For each of the six L use q in
   `{(3,4),(0,6),(5,12)}`, rho=L^-T q, P=0, the same remaining internal data,
   and directions `{(1,0),(0,1),(1,1)}`. Compare the second Taylor
   coefficient of the unreduced Hamiltonian to one half of the declared
   Hessian quadratic form. Check zero first derivative, determinant zero,
   positive trace and kernel rho of that Hessian (18 matrix cases).
3. **Six fixed-charge energy witnesses.** The original rest preparation,
   its four initial preparations P=(0,s) with s in `{1,2,3,-3}`, and
   P=(9/2,0). Verify the exact J*= [[0,4],[-2,0]], energies 10 and 23/2
   respectively, and witness Hessian diagonal `(1/6,0)`.
4. **Three charge-exact preparation sections.** For c in `{-1,0,1}` use
   P=epsilon e1, G=I, r=e1, X=c epsilon e2,
   rho=(6+c epsilon^2)e2, Pi off-diagonal `-1-c epsilon^2/2` with
   diagonal zero. Check J=J* through degree two and energy coefficients
   `-23/12,1/12,25/12`. Exact charge constancy at all epsilon is polynomial
   and proved separately. These are initial-state sections; none is called
   a stable moving orbit.
5. **Four mean/phase algebra checks.** Check Omega^2=-2I; the mean tensor
   from the analytically proved moments of sine and cosine is
   diag(1/12,1/24); the mean G is diag(3/2,3/4) and its ratio is 18;
   the rational Cayley matrix `(-I+2Omega)/3` gives response
   `[[1,-2],[-2,4]]/54`. This checks polynomial coefficients and declared
   exact moments, not an independently computed trajectory or long-time
   approximation.
6. **12 collapse-family states.** eps in `{3,-3,16/3,-16/3}` and
   s in `{1,1/2,1/4}`. Set G=diag(s^2,s^6), Pi=0, r=s^2 e1,
   rho=(0,4/s^2), X=(0,-2/eps), P=eps e1. Check full J=J*,
   H=s sqrt(eps^2+16)+3s^2, positivity and strict decrease with s.
   Rational square roots exist at every chosen eps. This finite audit
   checks the formula, not the universal infimum statement.

## Falsifiers and negative controls

Any mismatch in a declared exact equality fires its named `FALSIFIER` and
prints `RESULT=FAIL`; the first failure is retained. Unexpected exceptions
also produce a distinct failure transcript, never PASS. No tolerance,
adaptive fixture, optional case or fit is admitted. A failure consumes the
pin; code is not edited and rerun under that identity.

Seven negative controls explicitly reject: a generally conserved internal
charge; scalar instantaneous Hessian; positive-definite instantaneous
Hessian; inheritance of the old H>=10 full-charge minimum; omission of
XP^T from the full charge; reuse of the invertible old generator at P=e1;
and uniqueness of the energy curvature across charge-exact preparation
sections. A negative-control failure means the asserted counterexample
was not detected, not a scientific victory for the rejected inference.

Successful stdout has nine lines: field count 24, Hessian directions 54,
fixed-charge witnesses 6, preparation sections 3, mean/phase checks 4,
collapse cases 12, negative controls 7, rest Hessian 1/6,0, RESULT=PASS.
Actual stdout is captured only after public pin/readback.
