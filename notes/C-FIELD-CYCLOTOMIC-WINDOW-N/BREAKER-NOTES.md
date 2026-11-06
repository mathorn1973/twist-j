# Independent challenge notes

PUBLIC / NON-CANONICAL. Action layer L1. No earned public status is asserted.

The challenger wrote `break.py` from the frozen preregistration and public
definitions without reading `verify.py`, `PROOF.md`, builder calculations or
scientific outputs. The targets were exposed, so this is implementation
independence rather than independent discovery. Only AST parsing occurred
before the joint public source freeze
`40b30d87b617bf412980dcf8368f46b57407ad95`. The frozen breaker SHA-256 is
`20028cf14b2aabaa87ec01de182a1e62ecd5443a914d4bd2aa82a3e7ab8cd023`.

The independent mathematical sections below were initially authored after
that freeze and before reading either implementation's scientific stdout or
the builder proof. The execution disposition and certificate explanation
were added after the coordinator reported the first executions and the
challenger inspected the frozen primary source and breaker transcript.
Run custody and execution limits belong to `RUN.md` and the exact
transcripts.

## Execution disposition and primary defects

The independently frozen breaker completed its first official execution
with exit zero and empty stderr. Its stdout is 3154 bytes and 52 lines,
SHA-256 `9bd3fb7fb790083d9afbbe26b7b4ad57e904018db2c751151b73b5d88811bb7f`.
This is one successful local exact audit, not a second architecture or a
successful primary run.

The frozen primary stopped at its image-equivalence assertion, line 290.
Its hand-entered second image condition was

    3a-b+c-d = 0 mod5,

combined with `a+2b=0 mod5`. This predicate is false. For
`y=(0,0,1,1)` it accepts, but the exact inverse numerator is
`(3,1,-2,1)`, which is not divisible by five. The correct criterion,
independently derived and exhaustively audited by the already-frozen
breaker, is

    a+2b = 0 mod5,       c+2d = 0 mod5.

Post-failure source review identified a second incorrect assertion in the
primary's unreached code: it labels `(0,0,1,2)` an H=5 nonmember. That
vector is actually

    L(1,0,-1,1) = (0,0,1,2),

and the displayed preimage has H=1. The breaker's independently frozen
nonmember `(0,0,1,-2)` is valid, as proved below. The second defect is a
static, exact counterexample; the primary run did not reach that assertion.

Neither frozen source was repaired or rerun. The primary has no complete
successful transcript; its later controls and planned PASS lines are
unexecuted. The candidate disposition remains partial, with no promotion
readiness, no two-architecture scientific gate, and no successor code
introduced by these notes. A corrected future primary would require a new
explicit successor pin under the frozen failure rule.

After these outcomes the challenger reviewed `PROOF.md` Sections 1-8.
No mathematical blocker was found in the universal window proof, the
critical induction, the integer unstable-orbit argument, or the stated
incidence and reversal boundaries. This proof review does not convert the
failed primary into a successful run.

## Universal window and its quantifier

For any finite integer C, completing the square gives

    H(E,M) = ||E + C M/2||^2 + M^t (I - C^t C/4) M.

Consequently max spec(C^t C)<4 makes H positive definite. The forward
and backward shear formulas are integral and mutually inverse, and direct
expansion gives H(Tx)=H(x). Each fixed energy then bounds an integer orbit
inside a finite set. Invertibility makes every orbit periodic. Applying
this to the finitely many standard basis vectors and taking their common
period proves T has finite order. The zero-dimensional carrier has order
one, and zero/rank-deficient/rectangular matrices cause no exception.

Conversely a positive singular value sigma gives a real invariant
two-plane with matrix

    [[1,sigma],[-sigma,1-sigma^2]].

Its characteristic equation is

    mu^2 - (2-lambda) mu + 1 = 0,       lambda=sigma^2.

At lambda=4 this matrix has a nonzero Jordan part at -1. Above 4 it has
a real eigenvalue of modulus greater than one. Either case has an
unbounded real orbit. If every full integer orbit were bounded, in
particular each standard basis orbit would be bounded. Linear combination
of their finitely many bounds would bound every real orbit, a
contradiction. Thus the universal quantifier in the frozen equivalence is
essential: for C=diag(3,0), the nonzero electric second-coordinate orbit
is fixed even though the first singular block is unstable.

Finite order implies boundedness, closing all three implications. On a
nonzero stable singular block, mu is on the unit circle and a common
finite order N gives mu^N=1. The characteristic equation yields

    mu + mu^-1 = 2-lambda,
    lambda = (1-mu)(1-conjugate(mu)) = |1-mu|^2.

This argument decomposes real vector spaces only. It supplies no integral
direct-sum decomposition.

For the specified Ccrit, Ccrit^t Ccrit v=4v and ||v||^2=2. Substitution
in one shear step carries the frozen formula at n to the formula at n+1,
starting from n=0. Its energy is

    8 n^2 + 2(2n+1)^2 - 8n(2n+1) = 2.

This is an all-n derivation; the thirteen preregistered values only audit
it. Two ordinary signed triangular columns with one common unit edge
have Gram matrix [[3,s],[s,3]], s=+1 or -1. Its eigenvalues are 2 and 4.
The conclusion concerns precisely those columns, not arbitrary face
constructions.

## Integral active lattice and actual charges

The candidate embedding K has an integer left inverse

    (E0,E1,E2,E3,M0,M1) -> (-E1,E2,M0,M1).

Thus its integral image is saturated. Combining Phi5(T)K=0 with the
four-dimensional rational kernel proves equality with the definition
`ker_Q(Phi5(T)) intersect Z^6`. Merely checking rational rank would not
suffice: doubling K's first column preserves that rational kernel while
missing K(1,0,0,0) with index two. The breaker includes this specific false
basis as a control.

The static integer lattice consists exactly of

    (E,M) = (r,r,s,r-s,0,0),       r,s in Z.

For a raw integer electric vector E, its rational active electric
coordinates are

    a = (2E0-3E1+E2+E3)/5,
    b = (-E0-E1+2E2+2E3)/5.

The numerator of b is twice the numerator of a modulo five. Hence the
active plus static integral sublattice has exactly the congruence

    2E0-3E1+E2+E3 = 0 mod5,

and index five in the raw lattice. This is an obstruction to an integral
direct sum even though the real and rational decompositions are direct.

The actual graph divergence is

    rho = (E0+E1+E2, -E0-E1-E3, -E2+E3).

Its image is every integer zero-sum charge triple: the electric choice
`(0,0,rho0,-rho1)` realizes such a triple. Its integer kernel is exactly
the electric image of C5, so each actual charge sector is an affine
translate of the active lattice. The gluing congruence depends only on
the actual charge:

    2rho0+rho2 = rho0-rho1 = 0 mod5.

The static basis charges are `(2,-3,1)` and `(1,1,-2)`. Therefore a charge
sector has an integer static representative precisely when this
congruence holds. Every sector has a unique rational static
representative. None of these statements replaces D by an abstract
auxiliary charge map.

## L5 image and rejected extensions

Writing t for the frozen active T, Phi5(t)=0 and t^5=1 imply

    L = 1-t-t^2+t^3,
    L^2 = 5t^3,
    L^-1 = t^2 L/5.

Since T preserves the actual energy form B, its B-adjoint is T^-1.
Consequently L^*=t^2 L and L^*L=5I. An ordinary transpose cannot replace
this adjoint. In the declared cyclotomic module the determinant is
`Norm(1-zeta5) Norm(1-zeta5^2)=25`. The integral inverse numerator makes
the quotient have exponent five; determinant 25 then gives exactly
`(Z/5Z)^2`. The breaker separately constructs a column Hermite
certificate and computes the determinantal divisors from integer minors.

Membership is necessary and sufficient precisely when every coordinate
of T^2 L y is divisible by five. Rejecting before division prevents a
rational inverse from masquerading as an integer operation. The frozen
audit tests every one of the 625 residue classes and contains no shell
enumeration.

The independently emitted inverse numerator is

    N = T^2 L = [[ 1, 2, 1, 2],
                 [ 2,-1, 2,-1],
                 [ 0,-5, 1,-3],
                 [-5, 5,-3, 4]],
    NL = LN = 5I.

Let A=a+2b and B=c+2d modulo five. The four coordinates of Ny are,
respectively, `A+B`, `2A+2B`, `B`, `2B`. Thus Ny is divisible by five
if and only if A=B=0. This derives the corrected necessary-and-sufficient
criterion directly, without a changed threshold or a re-execution.

For a constructive lattice certificate, the independently frozen breaker
produced

    H = [[5,3,0,0],       V = [[ 1, 1, 1, 1],
         [0,1,0,0],            [ 2, 1, 2, 1],
         [0,0,5,3],            [ 0,-1, 1, 0],
         [0,0,0,1]],           [-5,-2,-3,-1]],
    LV = H,       |det(V)| = 1.

The columns of H generate exactly the two congruences above. The minor
gcds for sizes zero through four are `(1,1,1,5,25)`, giving Smith
invariants `(1,1,5,5)`. These are consistent independent explanations of
the index and admission rule, not an amended primary verifier.

Whole-shell surjectivity fails already from H=1 to H=5. The explicit
active vector

    y = (0,0,1,-2)

has H(y)=5 but

    T^2 L y = (-3,4,7,-11),

so y has no integral L-preimage. The H=1 source shell is nonempty,
containing `(0,0,1,0)`. This is an algebraically selected counterexample,
not a post-selected finite count. It does not contradict injectivity or
the exact inverse on the admitted image.

J is a unit, but it is not an energy isometry. For
`x=(1,0,0,0)`, Jx=`(0,1,1,-3)` and H changes from 2 to 3.

On the full carrier, L(T) kills every static vector. In particular it
sends `(1,1,0,1,0,0)`, of energy 3 and actual charge `(2,-3,1)`, to zero.
Therefore neither the active energy multiplier nor charge retention
extends to this full-carrier polynomial map.

The rational extension that acts as L on active states and identity on
static states is

    F = L(T) + Phi5(T)/5.

It retains actual divergence over Q. It fails to preserve the raw
integer lattice: on the raw E0 unit vector its static projector is
`(2,2,1,1,0,0)/5`, and L(T) of that vector is integral. An integral
summand cannot remove those fractional coordinates. More generally F is
integral on a raw integer input exactly when that input satisfies the
gluing congruence. Preserving rational divergence is insufficient to
establish an integer field operation on every charge sector.

The valid interface is therefore a total injection on the declared
active integer lattice, an admitted partial inverse, and energy change
`h -> 5h`. A future reverse reaction releases `4h`, four units at h=1.
It still needs its own resource, phase, residue, branch and raw-register
contract; the existing two-unit activation does not supply that contract.
No coupling, particle identification, physical Gauss law, or cross-layer
promotion follows from these L1 results.
