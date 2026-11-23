# Source symmetry and affine branch bounds for the binary quadratic lift

**NON-CANONICAL / L1 / analytical note**

Public Canon v116, activation commit
[93c36089db57032a6cbca482ff62c95884567d0f](https://github.com/mathorn1973/twist-j/commit/93c36089db57032a6cbca482ff62c95884567d0f).
The source results are
[DEF-QUADRATIC-MEMORY-L5](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#def-quadratic-memory-l5),
[QUADRATIC-L5-INITIALIZED-CAPACITY](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#quadratic-l5-initialized-capacity-t)
and
[QUADRATIC-L5-NATIVE-OBSTRUCTIONS](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#quadratic-l5-native-obstructions-t).

Fix a symmetric form C over F5 on V = F5^6 of rank r >= 4. Read
G(x,y) = (x^T C x, x^T C y, y^T C y). The fixed marked B identifies this
with D_C. The Gram target is M(a,b,c) = (3b, 4a+4b+4c, 3b+3c).
The carrier is V^2 times {0,1}, with the whole bit-0 layer ready once.

## A source reflection must be broken

Every such C has a vector u of norm 1. Indeed, diagonalize C. If a nonzero
diagonal entry is square, rescale its basis vector. Otherwise rescale two
entries to 2 and add their two basis vectors after multiplying each
by 2. The resulting norm is 2*4+2*4 = 1 modulo five.

Put R(v) = 2(u^T C v)u - v. This is a C-isometric involution, including
when C has a radical. Writing v = (u^T C v)u + w with w perpendicular to u
gives R(v) = (u^T C v)u - w. Its fixed space is span(u).
Let S act diagonally by R on the two cells and trivially on ignored
memory. This complete action depends only on C and u.

Every complete transition T commuting with S fails on the ready state
z = (u,0,0). Since S(z) = z, its image is S-fixed, so both output cells
are multiples of u. Their Gram matrix therefore has rank at most one.
But the required Gram value is M(1,0,0) = (0,4,0), with determinant
-4^2 = 4 in F5, hence rank two. The argument permits nonlinearity,
arbitrary full-state words, and any ignored register cardinality on which
S acts trivially. Reversibility is unnecessary for the contradiction.

Consequently an independent alphabet whose complete primitive maps commute
with this S cannot realize the target. This applies in particular to a
diagonally O(C)-equivariant alphabet with trivial action on memory. More
locally, every contact that succeeds at z satisfies S(Tz) != T(Sz).
The required symmetry breaking concerns the full maps of gates and
register controls, so a control can break the condition even where the
underlying data moves preserve it.

## A minimal abstract lift can keep common scalar symmetry

Let H = F5* act by s(x,y,eta) = (sx,sy,eta), so G(sz) = s^2 G(z).
For each nonzero Gram point g, write n(g) for its data fibre size.
Each H-orbit over {g,-g} meets each of the two Gram fibres in exactly
two states, since the scalar action is free there and the square map
has kernel {1,-1}. The nonzero sign-pairs form M-orbits of length d = 1
or 5, by M^5 = -I. For each such orbit, take the lexicographically least
Gram point in its union as g_0 and set g_j = M^j g_0 for 0 <= j < d.
Then M^d g_0 = -g_0, since M^5 g_0 = -g_0 and 5/d is odd.

For this orbit put k = max_j n(g_j)/2. At sign-pair j, choose k distinct
H-orbits of full states, with all ready H-orbits included. This is possible
because there are n(g_j)/2 ready orbits and n(g_j) total orbits there,
and the Canon capacity inequality gives k <= n(g_j). Specify the order
by ready first, then the lexicographically least state in each H-orbit.
For each chosen orbit i, let v_{j,i} be its least complete state above
g_j. Define T by the matching index on successive sign-pairs and by a
common scalar at the wrap:
$$
T(sv_{j,i}) =
\begin{cases}
s v_{j+1,i}, & j<d-1,\\
2s v_{0,i}, & j=d-1 .
\end{cases}
$$
On unchosen orbits and the zero-Gram states use the identity.

The representation sv_{j,i} is unique, and all designated representatives
lie over the declared g_j. T is a complete permutation. Its inverse steps
back at fixed i and s, except that crossing from j=0 to d-1 replaces s by
3s. It commutes with the common scalar action on all states. At the wrap,
the Gram is multiplied by 2^2 = -1, so the required equation holds on
every chosen orbit and every zero-Gram state. The actual reachable set
consists of exactly the chosen nonzero orbits and the ready zero-Gram
states. In each nonzero sign-pair orbit, some j has n(g_j)/2 = k, so all
chosen orbits there are ready and their full images under both directions
of the cycle cover all chosen states. The unchosen orbits are fixed.

Each nonzero Gram point in this reachable set therefore has exactly
2k = max_j n(g_j) states. The zero fibre contributes n(0). This is the
unrestricted minimum reachable size in the Canon, now attained subject
to the common scalar symmetry. The map has T^20 = I on the full carrier
and T^10 acts as simultaneous multiplication by -1 on the chosen nonzero
orbits because a traversal of a sign-pair orbit multiplies both cells by
2 and 10/d equals 2 modulo 4. The Gram orbit still returns within ten steps.
The index and scalar in the formula are coordinates assigned to existing
states. Neither is a separate run-time register.

The matching in this construction is determined from the target. This
gives abstract existence and a symmetry comparison. Native use would
require a word in an independently admitted alphabet with the same
complete action or its own continuation proof. The period statements
describe this particular lift.

## Four affine branches cannot cover the common-ready layer

Suppose the ready data projection selects arbitrarily among m affine
maps f_i(z) = A_i z + t_i on V^2. The selection rule may use nonlinear
predicates and writes. Its only restriction here is the number of
distinct affine alternatives.

Use the scalar test $\lambda=(1,1,2)$ in the marked reading. The
quadratic matrices of lambda D_C(z) and lambda L5 D_C(z) are Q1 and Q2,
with ranks r and 2r. Explicitly, $Q_1=\begin{pmatrix}1&1\\1&1\end{pmatrix}\otimes C$ and $Q_2=\begin{pmatrix}3&2\\2&1\end{pmatrix}\otimes C$ in the two-cell input coordinates. For each branch the scalar residual has homogeneous
quadratic matrix S_i = A_i^T Q1 A_i - Q2. Its rank d_i is at least r
because rank(Q2) <= rank(S_i) + rank(A_i^T Q1 A_i).

For a quadratic polynomial on F5^n with quadratic rank d, isolate its
radical. A nonzero linear term there gives fraction 1/5 of zeros. In the
other case complete the square on the d nondegenerate coordinates.
Dividing the norm counts in QUADRATIC-L5-INITIALIZED-CAPACITY by the size of the nondegenerate domain gives the upper bounds 1/5 + 4/5^(d/2+1)
for d even and 1/5 + 1/5^((d+1)/2) for d odd. Free radical coordinates cancel in these fractions. Thus the uniform per-branch
bound is 29/125 for d >= 4 and 26/125 for d >= 5. The vector agreement
set is contained in the scalar zero set. For m <= 4 their union has
fraction at most 116/125 when r=4 and 104/125 when r=5 or 6. This excludes
all selectors using at most four affine alternatives and strengthens
the Canon two-choice obstruction on the full common-ready layer.
The proof allows singular and translated branches and arbitrary finite
ignored memory. It does not restrict programs by length or impose a
trace quotient. Five alternatives are a necessary lower bound; their
sufficiency is open in this class.

## Falsifiers and boundary

A reflection-commuting transition that sends the specified ready witness
to the required Gram value would disprove the first result. A nonzero
sign-pair orbit with a missing slot at the stated count, a failure of the
inverse or the equivariance, or an initially ready state outside the
stated reachable union would disprove the construction. Four explicit
affine branches covering every ready input for the fixed Gram target
would disprove the branch bound.

These are analytical results conditional on the marked reader and C.
Independent admission of C and the gate alphabet, and a native
occupied-memory continuation certificate, are still required by
QUADRATIC-MEMORY-NATIVE-CONTACT [O]. The proofs concern the three specified classes at L1.
