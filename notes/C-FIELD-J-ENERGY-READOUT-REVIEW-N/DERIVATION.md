# Independent derivation for the frozen field-energy reading

**PUBLIC, NON-CANONICAL. Prospective independent L1 derivation, unexecuted.**
The immutable sources, author preregistration exposure and implementation
firewall are recorded in [PREREG.md](PREREG.md). All matrices named below
are the exact canonical matrices at its source pin. This derivation does
not rely on the candidate's proof, code, outputs or an unexposed census.

## 1. Scalar chart and a path quadratic form

Write C for canonical Jcyc and write a=(a0,a1,a2,a3). Its inverse is

    C^-1 = [[2,-2,1,-1],[1,0,0,0],[1,-1,0,-1],[1,-2,0,-1]].

Both integer products with C are identity, so this is an integral bijection,
with literal ordered equality. The canonical identity A_f C=C M_j implies
(I+A_f^2)C=C M_(1+j^2); thus the selected scalar J corresponds to the virtual
field operator J_f=I+A_f^2. It is not the actual chain's F operation.

For Q=sum a_i^2 and t=a0a1+a1a2+a2a3, multiply alpha by its conjugate.
The two adjacent differences contribute t(j+j^4); the other differences
contribute (a0a2+a0a3+a1a3)(j^2+j^3). Since j+j^4=phi-1 and
j^2+j^3=-phi, the universal coefficient identity is

    alpha bar(alpha)=u+v phi,
    u=Q-t,
    v=t-a0a2-a0a3-a1a3.

Direct pullback of the canonical B_f gives

    D=C^T B_f C = [[2,0,-1,-1],[0,2,0,-1],
                   [-1,0,2,0],[-1,-1,0,2]],
    e0=H(Ca)=Q-a0a2-a0a3-a1a3=u+v.

Using the multiplication matrix for 1+j^2 in the same quadratic form gives

    e1=H(J_f Ca)=Q-a0a1-a1a2-a2a3=u.

These are polynomial identities for every integral tuple. An independent
finite coefficient certificate is possible because all these expressions are
homogeneous quadratic: the four diagonal values and the six polarized cross
values determine every matrix entry. break.py implements exactly that
coefficient extraction, with cyclotomic multiplication as convolution in
five cyclic positions followed by subtracting position four. It does not
infer universality from a bounded census.

The real conjugate of phi is 1-phi; hence

    S(alpha)=2u+v=e0+e1,
    S(J alpha)=3u-v=4e1-e0.

The second identity follows from J bar(J)=2-phi and phi^2=phi+1, which
sends (u,v) to (2u-v,v-u). Multiplication by u+v phi on (1,phi) is
[[u,v],[v,u+v]]. Its determinant, or the product of the two positive real
embeddings, is the absolute cyclotomic norm

    N(alpha)=u^2+uv-v^2=-e0^2+3e0e1-e1^2.

This also proves the quartic identity, since the already proved u,v and
e0,e1 are homogeneous quadratics in a. The breaker pulls the 2-variable
norm matrix back along (e0,e1)->(e1,e0-e1); determinant norms over the full
finite box are a separate arithmetic audit.

Canonical A_f^T B_f A_f=B_f establishes actual conservation. Virtual J_f
changes y=(1,0,0,1)=C(1,1,0,0) from H=2 to H=1, with J_f y=(1,0,-1,0).
Therefore reading H(J_f y) does not justify replacing conservative F by J_f.

## 2. Complete small domain and image recognizer

In order (a2,a0,a3,a1), D is the positive A4 path Cartan matrix. Alternatively
its positive definiteness follows from the canonical positive H and C's
invertibility. An exact inverse certificate is

    D^-1 = (1/5) [[6,2,3,4],[2,4,1,3],[3,1,4,2],[4,3,2,6]].

Cauchy-Schwarz in the D metric gives a_i^2 <= (D^-1)_ii a^TDa. Thus
H<=5 implies (a0^2,a1^2,a2^2,a3^2) <= (12,8,8,12), componentwise.
Every integral domain element therefore lies in precisely the declared
containing box [-3,3] x [-2,2] x [-2,2] x [-3,3]. Its size is 1225.
This bound precedes and justifies exhaustive enumeration; it is not inferred
from finding no further points.

For alpha nonzero its two complex embeddings are nonzero, so N is a positive
integer. Complete the square:

    N = (5/4)e0^2 - (e1-(3/2)e0)^2 <= 125/4.

Consequently N<=31 on nonzero H<=5, and 5^4=625>496=16*31. Equal e0,e1
give equal ordered embedding magnitudes A,B. For two equal-residue scalars
alpha,beta, a nonzero difference gamma=5 eta would have N(gamma)>=625,
while the two embedding triangle inequalities give N(gamma)<=16AB<=496.
This contradiction proves injectivity on the nonzero domain. Zero has
e0=0 and positivity makes it unique, so adjoining zero preserves injectivity.
This is the admitted canonical norm-separation argument, specialized with
independently derived energy bounds, not a claim of minimal modulus.

The complete inverse can simply enumerate, for each residue coordinate,
every lift lying in the proved box, and retain exactly candidates satisfying
(u+v,u)=(e0,e1). It returns (a,Ca) if one survives, and otherwise rejects.
There are at most four residue-compatible tuples, since only the two
width-seven coordinates can have two lifts. The procedure terminates on
every correctly typed finite integer input. Rejection before enumeration is
safe for e0 outside [0,5] or e1 outside [0,13]: when e0>0, positivity of N
implies e1>0; if e1>=14 and 1<=e0<=5,

    N <= -25+15e1-e1^2 <= -11 < 0,

because N increases with e0 throughout that rectangle and the final
quadratic decreases for e1>=14. For e0=0 positivity requires a=0 and e1=0.

Soundness is direct re-encoding, and completeness follows from the containing
box and the retained exact equalities. Uniqueness is the preceding norm
argument. No assumption of prior scalar realizability enters this recognizer.
The syntactic contract accepts a tuple of length three, two actual Python
ints (not booleans), and a tuple of four actual ints in 0,...,4; all other
listed syntactic forms reject. Tuple subclasses remain tuples. The statement
is mathematical image recognition, not an all-corruption detector: exchanging
the valid residues of 1 and j leaves e0=e1=1 and yields another accepted scalar.

## 3. The fixed-context comparison

The selected w1=(0,0,1,0) is C(1,0,0,0). With
ell=(1-j)(1-j^2)=1-j-j^2+j^3, the canonical factorization
L=(I-A_f)(I-A_f^2) gives C^-1 Lw1=ell. Since w2=A_f w1,
C^-1 Lw2=j ell. Their coefficient tuples are respectively

    (1,-1,-1,1), (-1,0,-2,-2).

Both are in the registered balanced cube. Their (u,v)=(5,0), so each has
(e0,e1,S0,S1,N)=(5,5,10,15,25). The registered fixed trace pairing and LOW
line give q_LOW=s^2/[4(5Q-s^2)]. For these tuples (Q,s)=(4,0),(9,-5),
so Tr(alpha bar(alpha))=20 in each case and q_LOW=0,5/16 respectively.

The LOW line is held fixed while multiplying the source by j. This is a
change of a real four-coordinate vector relative to that line; neither a
global complex Hilbert phase nor a simultaneous change of measurement
context is being quotiented out. The field equality and QDD record equality
are different notions. The comparison stipulates field chart coefficients
as QDD pistons; it derives no physical dictionary.

## 4. All-time receiver blindness, including all actual substeps

Fix arbitrary finite N>=2 and any H(w)=1 seed. Put t=N-1. At a layer boundary
let k count completed F layers. The following invariant is sufficient:

- Source matter R means source field PL A_f^k w; source matter AM means
  source field P A_f^k w. All source spectators vanish.
- Intermediates retain literal ZM. Every other field and every spectator
  is zero. Receiver matter is R or AM.
- All matter, resources, channels and p have a common evolution independent
  of w, starting with their prescribed identical preparation.

Initially these statements hold. At the source, commutation A_fL=LA_f and
H(A_f^k w)=1 mean that R always passes the image check with preimage
A_f^k w. R releases two resource units and changes to AM. AM needs r0>=2;
when funded it changes back to R, restoring PL A_f^k w and subtracting two.
Otherwise AM keeps its complete input. In either branch the decision uses
the common resource only. This explicitly includes all later reversals:
one must not assume the source remains AM forever.

At every intermediate, literal ZM rejects regardless of carried resource.
At the receiver the field is zero forever, so h=0: R accepts exactly when
rt>=2, consumes two and increments p modulo five; AM always reverses,
releases two and leaves p unchanged; unfunded R retains the entire input.
These decisions are independent of w. This proves closure under the full
actual Ghat layer, including every funding rejection.

Both contact layers swap whole common resources with their old channels;
they do not inspect or transport fields. Hence equality persists after A
and after B even with occupied contacts. F maps the source field by
T_fP=PA_f and commutation with L, increments k, and fixes every zero field;
it leaves common coordinates and p unchanged. Induction on the actual
Ghat;A;B;F chronology proves equality of every stored coordinate except
the source raw field at every finite forward substep, for every N>=2 and
every unit-energy seed. In particular the receiver's literal 31 coordinates
and p coincide. Pointer reductions, including 4->0, use the same accepted
event sequence, so no late pointer wrap creates seed information.

A read-only subreview derived a useful stronger certificate. Exactly one
two-unit packet is either bound in source R (label S), bound in receiver AM
(label T), or occupies one coordinate r_i or q_j. Initially it is S.
Ghat exchanges S<->r0 and T<->rt, increments p only on input rt, and fixes
the other labels. A exchanges r_j<->q_j; B exchanges q_j<->r_(j+1); F
leaves the packet label fixed. These are direct case substitutions into
the canonical law, including N=2 empty ranges, and preserve this invariant
at every layer. They justify the single-packet audit without inferring it
merely from total energy (which alone would permit 1+1 splitting). This
certificate includes arbitrary resource returns and intervening rejections.
No additional claim about chain periods is needed for the review.

The initial total is 23+18+1=42. Canonical conservation holds at each layer;
the independent raw simulation audits that account and compares every
stored nonsource-field coordinate. Its 160-step horizon is an audit, not
the logical reason for all-time blindness. Distinct source seeds remain
distinct in the retained source field because P is injective, A_f is an
automorphism and L is injective; the receiver is simply insensitive to them
in this prepared family under this fixed law.

## 5. Scope and prospective review outcome

The derivation supports testing A-D at their frozen L1 scope. No test has
yet run and no author proof/code comparison has occurred at the independent
freeze. Historical census values remain exposed targets, not deductions
claimed before enumeration. This small sector neither changes the norm-941
codebook/modulo-25 theorem nor supplies field transport, acquisition of
virtual observations, native-U/J selection, physical energy, event law,
apparatus reset or a cross-layer realization. Final disposition requires
the pinned run and post-freeze author comparison.
