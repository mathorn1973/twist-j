# Exact classification by affine parity cylinders

NON-CANONICAL / L1. Method proof for P-POLE-HEIGHT-INTEGER-DOMAIN-1.
This proves the classifier's mathematical reduction, not a precomputed
success domain of W. A concrete complete domain needs the completed run.

## Integral bases and contact

Phi_5(j)=1+j+j^2+j^3+j^4=0. Every element of O has a unique four-integer
power representation. In that basis multiplication by p=j^2 sends
(a,b,c,d) to (d-c,-c,a-c,b-c).
The change to u=1-j is integral and unimodular: u^m is the binomial expansion
of (1-j)^m for m=0,...,3, with diagonal entries (-1)^m. Thus equality and
membership in 2O can be checked coefficientwise in either basis.
Substitution gives u^4-5u^3+10u^2-10u+5=0 and

    B=2u-u^2,  X=5u-6u^2+2u^3,  p=1-2u+u^2.

On admission x-y is even; x+y is even too. Both contact outputs belong to O.
The sum is fixed and the difference becomes p*(x-y). Since p is a unit,
admission is preserved along a contact orbit. On this orbit p^5=1, so
C^5=identity. Refused contacts are already identity. Therefore C^(-1)=C^4
as a total map, proving the literal inverse construction for any integer t.

## Affine parity lemma

Suppose the current six-slot state is A+nD on t=r+2^k*n, n in Z. For the
next label (i,j), put a=A_i-A_j and b=D_i-D_j modulo 2O. Admission is the
four-coordinate equation a+n*b=0 over F_2. It depends only on n modulo 2.
There are exactly four possibilities: admitted for both parities, refused
for both, admitted only for even n, or admitted only for odd n.

For a uniform branch, the same linear contact formula acts separately on A
and D, or both remain fixed on refusal. Uniform admission implies both a
and b vanish modulo 2, so all divisions by two are integral. If admission
is not uniform, substitute n=2m+epsilon for epsilon=0,1:

    A' = A+epsilon*D, D'=2D,
    r' = r+epsilon*2^k, k'=k+1.

The two cylinders are disjoint and cover their parent. Their next admission
is uniform. After at most one such split the next contact can be consumed.
Induction gives an exact finite partition for any finite word, at depth at
most its length. A bounded implementation may leave an explicit frontier;
this does not change the already established terminal maps.

For an anchored branch t=t0+2^k*n, retaining even n at every split keeps
n=0. All discarded children have a different admission trace from that
point onward. The surviving cylinder is exactly the set following t0's
trace. The output labels this cylinder by canonical r=t0 mod 2^k, while
its A,D coefficients explicitly retain the coordinate t=t0+2^k*n.
If one instead used t=r+2^k*m, the intercept would be shifted by
((r-t0)/2^k)*D; the underlying terminal map would be unchanged.

## Exact terminal equality

On a terminal cylinder, write W(I_(r+2^k*n))=A+nD. The target has constant
G_r and slope 2^k*V, where V=(B,-B,0,0,0,0). Equality is the conjunction
of 24 integer equations

    E_l+n*F_l=0, E=A-G_r, F=D-2^k*V.

If E=F=0, every point in the cylinder succeeds. If some F_l is nonzero,
that equation fixes n=-E_l/F_l. It succeeds exactly when this is an integer
and all other equations agree; there is at most one successful t. If F=0
and E is nonzero, or the equations disagree, the cylinder has no success.
Thus a complete finite-word domain is a finite union of dyadic cylinders
and isolated integers. The two implementations solve these equations by
different routes. The statement concerns this fixed word only.

## Invariants and independent arithmetic

Write Q(z)=Tr(z*conjugate(z))/2. In the j basis, using a fifth coefficient
zero, Q(a)=(5*sum(a_i^2)-(sum(a_i))^2)/2. The trace identities Tr(1)=4 and
Tr(j^m)=-1 for m=1,...,4 establish this expression. Its integrality follows
from a_i^2=a_i modulo 2. The sum and summed Q are preserved by each contact,
because the mean is fixed and the difference is multiplied by p with
p*conjugate(p)=1. Also p=1 modulo u, so each labelled output agrees with its
own input modulo u. O/(u)=F_5 and 2 is invertible there.

For A+nD the summed Q is a quadratic polynomial. The independent u-basis
checker uses the trace Gram matrix H_ab=Tr(u^a*conjugate(u)^b):

    H = [[4, 5, 5, 5],
         [5,10,15,20],
         [5,15,30,50],
         [5,20,50,100]].

Indeed s=u+conjugate(u)=u*conjugate(u), s^2-5s+5=0,
Tr(u^m)=5 for m=1,2,3, and Tr(s),Tr(s^2),Tr(s^3)=10,30,100. These identities
and conjugation symmetry give H. The constant, linear and quadratic Q
coefficients are respectively sum(A^T H A)/2, sum(A^T H D), sum(D^T H D)/2.
No floating point enters either route. For the preparation the total is
10*t^2+33, its ring sum is (5,-1,0,-2) in the j basis, and its six residues
are (0,0,0,0,0,2). Checking full polynomials checks every integer parameter,
not only the sample values used in the additional scalar audit.

## Exhaustiveness certificate and caps

Depth-first traversal starts with the cylinder (r,k)=(0,0). Each operation
either advances its program position without changing its domain or replaces
it by its two parity children. A finished leaf is removed only after its
terminal classification has been recorded. A cap leaves the pending node
unclassified on the frontier. Consequently completed leaves and pending
nodes remain a disjoint cover of all integer inputs.

The verifier independently checks this cover by mapping each canonical
residue r modulo 2^k to the interval with length 2^(-k) and left endpoint
rev_k(r)/2^k, where rev_k reverses the k binary digits. All intervals are
scaled to one exact common denominator 2^K, sorted, and checked for adjacent
endpoints from 0 to 2^K. Binary-prefix overlap corresponds precisely to
congruence-class overlap. The integral interval check detects both holes
and duplicates; an additional exact Kraft sum must equal 1. Finite dyadic
partitions here contain no extra classes without integer representatives.

The traversal hashes every classified leaf including its cylinder, affine
terminal coefficients, target differences and classification. All nonempty
solutions and the complete unresolved frontier are printed. Hashes bind a
deterministic replay; they do not replace the explicit arithmetic or cover
checks. COMPLETE requires an empty frontier. PARTIAL reports exact decided
sets and unresolved cylinders and never excludes unvisited solutions.
