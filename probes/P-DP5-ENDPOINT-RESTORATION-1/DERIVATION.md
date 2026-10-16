# Enclosure proof and implementation contract

**NON-CANONICAL / conditional L1 derivation; no execution result.**

For delta in C^7 define A_plus=sum delta_j a_j^dagger and
A_minus=-sum conjugate(delta_j) a_j. Their commutator is the scalar
[A_plus,A_minus]=||delta||^2 I, so the central-commutator exponential
identity gives D(delta)=exp(-||delta||^2/2) exp(A_plus) exp(A_minus).
On finite number-state matrix elements the identity is well defined.
Let Pi_L project onto total occupation<=L. Lowering preserves this subspace
and products of degree>L vanish on it. Subsequent raising can leave it,
but never return, and its products of degree>L have zero projection back.
Consequently on V_L the exact identity is

    Pi_L D(delta) Pi_L = exp(-||delta||^2/2)
       [sum_(k=0)^L (Pi_L A_plus Pi_L)^k/k!]
       [sum_(k=0)^L (Pi_L A_minus Pi_L)^k/k!].

The degree-zero identity is I_(V_L), not identity on the full Fock space.
This finite polynomial equality has no omitted displacement tail. In one
mode, lowering n to ell and then raising ell to m separately gives

    <m|D(delta)|n> / exp(-|delta|^2/2)
      = sqrt(m! n!) sum_(ell=0)^min(m,n)
        delta^(m-ell)*(-conjugate(delta))^(n-ell)
         / (ell! (m-ell)! (n-ell)!).

In the factorial-normalized basis f_n=sqrt(n!)|n>, the ladder coefficients
are n downward and 1 upward, and the corresponding coefficient replaces
sqrt(m! n!) by n!. Thus the independent exact-rational coefficient fixture
does not depend on numerical square roots. Seven-mode coefficients are
products of one-mode coefficients; the collective lowering and raising
operators give the same multinomial expansion. The proof covers arbitrary
finite bra/ket vectors, without assuming unit norm.

Write Q=2^192. An interval `(a,b)` denotes [a/Q,b/Q], with arbitrary-
precision signed integer endpoints. Addition and subtraction are exact on
this grid. Multiplication forms all four integer products, divides the
minimum by Q downward and the maximum upward. Division by a positive
integer uses the same directed rule. These operations enclose their exact
real counterparts, including negative operands. Complex rectangles use
the usual four real interval products. A decoded finite binary64 is first
an exact signed rational obtained from its sign/exponent/fraction bits,
then rounded outward to the grid; subnormals are never dropped. Signed
zero is the same mathematical zero. Nonfinite bit patterns are rejected.

For a nonnegative integer n, q=isqrt(n Q^2) satisfies
q^2 <= n Q^2 < (q+1)^2. Thus `[q,q+1]` encloses the positive sqrt(n),
and is `[q,q]` when equality holds. For a nonnegative rational x, integer
square root of floor(x Q^2) gives the same proof. Real interval squaring
uses zero as the lower bound exactly when the interval contains zero;
the two endpoint squares give the upper bound. This is tighter than
dependency-blind interval multiplication and remains sound.

The independently generated occupation basis is graded first by total
occupation, then recursively ascending first coordinate. A lowering edge
from n to n-e_j has coefficient -conjugate(delta_j)*sqrt(n_j); a raising
edge from n to n+e_j has coefficient delta_j*sqrt(n_j+1). Edges beyond
total degree L=8 do not exist. Each ladder action allocates a fresh output
array. Starting from term=v, total=v, the recurrence
term <- A term/k and total <- total+term for k=1,...,8 evaluates
sum A^k v/k! with enclosures. Apply lowering first and raising second.
The normal-ordering theorem B1 proves this is the exact projected finite
matrix element after multiplication by exp(-||delta||^2/2); no finite-
degree displacement approximation is introduced. Zero input coefficients
may be skipped only when all four rectangle endpoints are exactly zero.
There is no tolerance, normalization or removal of a nonzero component.

For real c and N=256 the complex Taylor polynomial for exp(ic) is evaluated
with exact fractions. The integral remainder is at most
abs(c)^257/257!. For theta in [c-r,c+r], the additional error is at most r
by the real-path Lipschitz constant one. Add both bounds in each coordinate,
round outward, and intersect with [-1,1]. For nonnegative x, the polynomial
for exp(-c) has the same magnitude remainder and exp(-x) is also Lipschitz
one. Add the argument radius and intersect with [0,1]. The input guards
abs(c)+r<=64 and 0<=x<=64 are exact rational comparisons. No phase is
reduced, fitted or selected after viewing the legacy output.

The midpoint denominator divides 2^193 and its guarded numerator has
magnitude <=2^199. The degree-257 remainder numerator and denominator are
less than 2^51500, hence need at most 15504 decimal digits; the same
32768-digit finite limit covers the sum with the argument radius.
Python's default 4300-digit guard is therefore explicitly replaced by 32768
before controls and production, with a near-unit 192-bit midpoint control.
No unlimited integer-string conversion is enabled.

Complex inner products conjugate the bra. The six frozen pairs use
delta=alpha_a-alpha_b and theta=Phi_a-Phi_b+
Im sum conjugate(alpha_b)*alpha_a. Each of the 120 terms carries the exact
unnormalized rational weight (20/21)^7*(1/21)^|nu|. The all-thermal linear
reference has exp(-(11/20)||delta||^2) and the same Weyl phase.

For new retained and linear rectangles, subtract them, square each real
interval with its dependency-aware rule and add. The positive square-root
interval divided by two encloses the witness center magnitude. Its midpoint
and halfwidth have exact rational values. The old numerical radius and
thermal radius are separate declared dependencies. The final distance
interval is [max(0,center.lo-numerical-thermal),
min(1,center.hi+numerical+thermal)]. The arithmetic halfwidth is included
once in the separately reported total radius numerical+thermal+halfwidth.
The final interval must never expand the already bounded center by its
halfwidth a second time.

`COVERED` requires whole-new-rectangle containment in the old rectangle.
Disjointness of either coordinate is `CONFLICT`. All other comparisons
are `NOT_DECIDED`. A valid new enclosure and a legacy comparison are
separate output fields. The 1/1000 precision decision compares the total
radius; the discrepancy decision compares the final distance endpoints.
Neither uses a floating midpoint comparison.

Required controls include exact rational coefficient comparisons of B1
against B2 in the factorial-normalized one-mode basis, vacuum and first-
excitation values, zero displacement, a nonunit stored vector, phase sign
and conjugate/adjoint/swapped-branch conventions, exact retained mass,
understated elementary remainder, malformed/nonfinite binary payloads,
reordered basis, wrong weights, and the center-width double-count trap.
The controls are not run until a new accepted public pin exists.
