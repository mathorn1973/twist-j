# Native fiber transport and the counter boundary

**PUBLIC / NON-CANONICAL / prospective candidate-T / L1.**
Reservation: [#1481](https://github.com/mathorn1973/twist-j/issues/1481).
Adapted from the supplied exploratory `NATIVE_EXTENSION_PROOF.md` on
2026-10-13. The supplied calculations are result-exposed premises, not a
formal execution of this probe. Formal audits await the new public source
pin. No Canon promotion or operation implementation is asserted here.

All vectors, matrices and scalars below are over F_5. The declared native
state is Omega=N_0 x F_5^6. Its counter n is part of the state:

    theta_n = popcount(n) mod 2,
    z(x) = sum(x) mod 5,
    U(n,x) = (n+1, g_(z(x)+2 theta_n mod5)(x)),
    (g_0,g_1,g_2,g_3,g_4) = (a,b,c,d,e).

The checkpoint alone is not an autonomous state. These are the unchanged
canonical generator formulas, in coordinate order (p1,p4,p1p,p4p,q,r):

    a(x)=(p4,p1,p4p,p1p,q,r),
    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

The inherited authority is Public Canon v101, content commit
`421a4ec1daf07c04d19022c1ee219607e83c09a8`. The bracket and automorphism
inputs are TRACEKERNEL-F5-HODGE-BRACKET and
TRACEKERNEL-F5-AUTOMORPHISM-BOUNDARY. Active conservation is related to
U-NATIVE-INVARIANT-AND-NOWRITE. The uniform sharp nine-letter sheet result
is already TM-SHEET-SYNCHRONIZING-GRAPH, including clauses G3, G4 and G7;
Section 4 supplies another direct proof, not a newly discovered bound.

## 1. Exact fiber coordinates

Write the four piston coordinates as p and set

    s=sum(p),  z=s+q+r,
    W={v in F_5^4 : sum(v)=0}.

Since 4 is the inverse of 4 in F_5, every p has the unique decomposition
p=4s*1+w. Use the ordered difference basis

    u1=(1,-1,0,0), u2=(0,1,-1,0), u3=(0,0,1,-1).

If w has four-coordinate entries w_i, its three coordinates are
(w1,w1+w2,w1+w2+w3). Conversely (a,b,c) gives (a,b-a,c-b,-c).
Thus (n,p,q,r) <-> (n,s,q,r,w) is an exact bijection. Each fiber over the
base b=(n,s,q,r) has 125 points. In this basis the restricted dot product is

    B=[[2,4,0],[4,2,4],[0,4,2]], det(B)=4,
    B^-1=[[2,3,4],[3,1,3],[4,3,2]].

Define

    A=[[4,1,0],[0,1,0],[0,1,4]],
    P=[[0,4,1],[0,4,0],[1,4,0]],
    t=(2,3,1)^t,  h(r)=(3,r,3+r)^t.

Direct substitution in the five displayed six-coordinate formulas gives:

| Generator | New (s,q,r) | New w |
|---|---|---|
| a | (s,q,r) | A w |
| b | (-s,-q,-r) | -P w |
| c | (1-s,1-q,-r) | -P w+h(r) |
| d | (-s,1-q,1-r) | -w+t |
| e | (-s,2-q,1-r) | -w+t |

For example c has new piston sum 1-s; subtracting 4(1-s)*1 and
converting to the difference basis gives -P w+h(r). The other rows follow
in the same way. The selector depends only on the base. Every fiber map
is an affine bijection, although the selected map of different bases can
merge states.

The following identities follow by multiplying the displayed matrices:

    A^2=P^2=I, AP=PA=[[0,0,4],[0,4,0],[4,0,0]],
    A^t B A=P^t B P=B, det(A)=det(P)=1, Pt=-t.

## 2. Homogeneous image of all five-generator words

The homogeneous fiber parts are A,-P,-P,-I,-I. Therefore the homogeneous
image of the monoid of fixed words in all five named generators is exactly

    G_tan=<A,P,-I>={+/-I,+/-A,+/-P,+/-AP} ~= C_2^3.

Containment follows from the five parts. Equality follows because a
supplies A, the two-letter b,d product supplies P, and d supplies -I.
The four matrices I,A,P,AP are distinct determinant-one involutions;
multiplication by -I gives four determinant-minus-one matrices. Hence
there are exactly eight elements, all of exponent two.

This exact image concerns unrestricted fixed generator words. It does not
assert that a selected U trajectory realizes every such word. On any one
starting fiber all U trajectories have the same base and selector history,
so their actual homogeneous transport lies in G_tan as well.

For beta(x,y)=B^-1(x cross y), a B-isometry L satisfies

    beta(Lx,Ly)=det(L)*L beta(x,y).

Indeed (Lx cross Ly)=det(L)L^-t(x cross y), and B^-1 L^-t=L B^-1.
More generally bracket preservation by an invertible C is equivalent to
C^t B C=det(C)B. Taking determinants gives det(C)^2=det(C)^3, hence
det(C)=1 and C^t B C=B. Conversely these two conditions imply bracket
preservation. Thus Aut(beta)=SO(B,5), consistently with the Canon.

Consequently

    G_tan intersect Aut(beta)={I,A,P,AP} ~= C_2^2.

The remaining four matrices are bracket anti-automorphisms. An affine map
preserving an affine bracket based at a chosen origin must fix that origin:
substitute the origin twice into the preservation equation. Translations
therefore cannot enlarge this homogeneous automorphism image.

No fixed word has homogeneous order three or five. In the faithful intrinsic
five-triple action established by the geometry proof, no such word gives a
three-cycle or five-cycle. This excludes neither order-five translations,
nonlinear decoders, counter-dependent relabelings nor added contacts.

## 3. Active fibers, common center and conservation

On z in {1,4} only b,d,e fire. Their sheet maps are: b exchanges 1 and 4;
d preserves 1; e preserves 4. Let

    w_star=3t=(1,4,3)^t, chi(1)=0, chi(4)=1.

Since Pt=-t, both -P w_star=w_star and -w_star+t=w_star. This is the
common center of the active affine maps; uniqueness already follows from
the -I map, since 2w_star=t.

Define on active fibers

    K_b(w)=(-1)^n P^chi(z)(w-w_star).                         (1)

This is an affine bijection. For d/e, z does not change and w-w_star is
negated, canceled by the counter increment. For b, z switches and the
centered part is -P; because P^2=I, the same cancellation gives

    K_(U_base b)(U_fiber,b(w))=K_b(w).

For every C in GL(W), the active action

    Phi_C,b(w)=w_star+P^chi(z) C P^chi(z)(w-w_star)           (2)

is K_b^-1 C K_b; the scalar (-1)^n cancels. It fixes the base and
commutes with U on the active domain. Its action is faithful.

This conservation is not a new information-retention theorem. The canonical
active four-vector uses the centered piston sums and signed differences.
Removing its all-ones component and changing to the difference basis gives
(1), with the centered four-coordinate piston (1,3,4,2). The center does not
depend on q or r. Canonical source merger and no-writing conclusions keep
their stated ports and domains.

## 4. Every arbitrary initial counter reaches active sheets within nine steps

Summing the generator formulas and using the selector gives

    f0(z)=(0,4,0,4,4)_z,
    f1(z)=(2,1,1,3,1)_z.

Once in {1,4}, a sheet stays there. Sheet 3 enters on its next zero bit.
Both sheets 0 and 2 enter by the end of a consecutive pair 11.

The Thue-Morse recursion is theta_(2m)=theta_m,
theta_(2m+1)=1-theta_m. No three consecutive bits agree: any three
positions include one complete complementary even/odd pair. An 11 pair
starts precisely at an odd position 2m+1 with (theta_m,theta_(m+1))=01.
Consecutive 01 starts have distance at most four, since the intervening
block is a run of ones followed by a run of zeros, each of length at most
two. Thus consecutive 11 starts have distance at most eight. The first
11 starts at position one. From any n>=0, the next complete 11 finishes
within at most nine consumed bits. Sheet 3 encounters a zero within at
most three bits. This proves entrance <=9 for every initial n and sheet.

The bound is attained at n=14,z=0. The nine bits are 101001011 and the
successive sheets are

    0 -> 2 -> 0 -> 2 -> 0 -> 0 -> 2 -> 0 -> 2 -> 1.

There is no earlier active sheet. This is a symbolic witness, not a claim
that a new formal census has run. The Canon already proves the stronger
full sheet synchronization for every length-nine Thue-Morse factor, and
identifies the nonsynchronizing length-eight word 10100101. Origin n=0
has the stronger familiar three-step synchronization through 011.

## 5. Unique counter-dependent extension of the prescribed active action

Let tau(b) be first entrance into {1,4}, including tau=0 on active
fibers. It is determined by the base and lies in 0..9. Let H_b be the
affine fiber transport through these tau steps and z_tau its final sheet.
Set

    mathcalK_b(w)=(-1)^(n+tau) P^chi(z_tau)(H_b(w)-w_star).   (3)

It is an affine bijection. On a transient base, first entrance after one
step has tau reduced by one and the same terminal active transport.
On an active base use (1). In both cases

    mathcalK_(U_base b) U_fiber,b=mathcalK_b.                (4)

For each C in GL(W), define the full-state map

    widehatPhi_C(b,w)=(b,mathcalK_b^-1 C mathcalK_b(w)).      (5)

Equations (4)-(5) imply

    widehatPhi_C U=U widehatPhi_C,
    widehatPhi_C widehatPhi_D=widehatPhi_(CD),
    widehatPhi_C^-1=widehatPhi_(C^-1).

Thus these maps give a faithful GL(W) action by base-preserving bijections
of the complete Omega. Faithfulness follows on any active fiber. On that
domain they agree with (2).

Uniqueness requires the stated active action and base preservation. If
another such map commutes with U, applying U^tau to it gives the prescribed
action on the terminal active fiber. Since H_b is bijective on the fiber,
its inverse forces exactly (5). This argument does not require U to be
bijective between bases and does not classify base-changing centralizers.

For the bracket, let m_b=mathcalK_b^-1(0) and let L_b be the homogeneous
part of mathcalK_b. Every factor of L_b is a B-isometry. The lift fixes
m_b and its homogeneous part is L_b^-1 C L_b. If C belongs to SO(B,5),
so does this conjugate. Therefore it preserves beta on displacement
vectors based at m_b, equivalently the affine operation

    beta_m(x,y)=m+beta(x-m,y-m).

It need not preserve a bracket based at an unrelated coordinate zero.

The coordinate change (b,w)->(b,mathcalK_b(w)) conjugates U to its base
dynamics times the identity on W. In particular every permutation of the
125 labels, not just every bracket automorphism, also has a faithful
counter-dependent lift. Commuting with U therefore selects neither the
bracket nor the GL action, and supplies no native word or physical contact.

## 6. Complete checkpoint-only extension class

Now require a single map Phi(p,q,r), independent of n, fixing (s,q,r)
and agreeing with (2) on every active fiber, for one fixed C in GL(W).
Require commutation with U at every n and checkpoint. Both driver bits
occur, so this is equivalent to commuting with both checkpoint kernels
F0 and F1 on their complete domains.

No assumption that transient maps are affine is necessary. Invertible
fiber transport to the prescribed active affine maps forces them to be

    Phi2(w)=w_star+C(w-w_star),
    Phi3(w)=w_star+PCP(w-w_star),
    Phi0(w)=o_r+PCP(w-o_r),
    o_r=w_star+Ph(r)=(4,4-r,1-r)^t.                         (6)

These follow respectively from the e edge 2->1, the d edge 3->4 and the
c edge 0->2. Their base arguments are transformed by those edges; (6)
states the forced map on each original base. Since c is an involution,
the opposite c edge 2->0 then automatically intertwines.

At z=0, F0=a fixes the base and acts as A. Equating homogeneous and
constant terms in Phi0 A=A Phi0 gives

    [C,A]=0, C P(A-I)o_r=P(A-I)o_r.                         (7)

Here AP=PA was used. Direct evaluation gives

    P(A-I)o_r=(2+r,0,1-r)^t.

Every r in F_5 is allowed on z=0, by choosing q=-s-r. These vectors span
the whole plane E_minus=ker(A+I)={(x,0,z)}: at r=0 take (2,0,1),
and their consecutive difference is (1,0,-1), an independent vector.
Thus C fixes E_minus pointwise. Commutation with A preserves the other
eigenspace E_plus=ker(A-I)=<(3,1,3)^t>. The eigenvalues are distinct in
F_5, so all possibilities are exactly

    C_lambda=I+(lambda-1)(I+A)/2, lambda in F_5^x.          (8)

There are four, forming a cyclic group of order four. Each commutes with
P. In (6) and on active fibers its extension has the explicit formula

    Phi_lambda(w)=w+(lambda-1)(w2-c_z(r))(3,1,3)^t,
    c_z(r)=4-r if z=0, and 4 otherwise.                    (9)

For completeness this intertwines all ten sheet/bit edges without an
enumeration assumption. The four active edges follow from (2). The three
forced entrance edges follow from (6), the opposite c edge follows from
c^2=I, and the a self-loops at z=0 and z=3 follow because A preserves
w2, fixes (3,1,3), and fixes the base. This proves sufficiency as well as
necessity for all checkpoints and both bits.

The eigenspaces E_minus and E_plus are B-orthogonal and nondegenerate;
B(3,1,3)^t=(0,1,0)^t, so the plus vector has norm one. Consequently

    C_lambda^t B C_lambda=B iff lambda^2=1,
    det(C_lambda)=lambda.

Only C=I among SO(B,5) admits this specified checkpoint-only extension.
The orthogonal possibilities are I and -A; the complete GL class is the
four matrices (8). This class fixes the entire base and extends one fixed
prescribed active action. It is not the full centralizer of U. On the
restricted active domain alone all C in GL(W) already admit (2).

A concrete obstruction is C=P, a legitimate bracket automorphism. On the
base s=q=r=0, (6) sends w=0 to t=(2,3,1). But a fixes zero and sends t
to At=(1,3,2). The conflicting four-piston outputs are (2,1,3,4) and
(1,2,4,3). Thus the same checkpoint cannot carry that prescribed action
under both possible time contexts.

## 7. Context, reversibility and existing negative results

The first-entry chart reads the existing integer n and at most nine future
driver bits determined by it. For the lifted LINEAR C action, less input
suffices. Put epsilon=(-1)^(n+tau) and

    J_b(w)=P^chi(z_tau)(H_b(w)-w_star),
    mathcalK_b=epsilon J_b.

Linearity of C gives the exact cancellation

    mathcalK_b^-1 C mathcalK_b
        =J_b^-1 epsilon^-1 C epsilon J_b=J_b^-1 C J_b.       (10)

The first-entry time, H_b and J_b are determined by (s,q,r) and the
length-nine future word theta_n...theta_(n+8). Canonical
TM-SHEET-SYNCHRONIZING-GRAPH G3 gives exactly 24 admitted length-nine
factors. Therefore at most 24 EXTERNALLY SUPPLIED time-context values,
together with the checkpoint, suffice to evaluate the entire action for
every linear C in GL(W) on every fiber. This counts the time-context
alphabet, not the complete state or source carrier. It is an upper bound;
equivalent contexts may reduce it. For arbitrary nonlinear permutations
of the invariant labels, the scalar cancellation is not automatic.

A finite collection of possible length-nine windows is not an autonomous
finite controller with a common initial state. Shifting such a window
requires its new future bit. No window-acquisition or closed finite update
law is supplied. An autonomous finite orbit has ultimately periodic output,
so it cannot generate the aperiodic Thue-Morse windows. The construction
therefore does not contradict T1's all-finite autonomous-context no-go:
T1 also observes the raw receiver (q,r), whereas (5) uses the full piston
fiber and preserves its base. It does not prove minimal necessity of the
entire integer n for any implementation.

Likewise a bijective symmetry commuting with U does not make U reversible.
For example, at n=0 the driver is zero and the distinct checkpoints

    (0,0,0,0,0,0) and (2,1,2,1,1,0)

both map to (0,0,0,0,0,0): the first selects a and the second selects c.
The chart leaves this base merger in place. Thus it supplies neither a
bijective complete apparatus evolution nor T3's impossible exact reversible
lift of the literal nonsurjective fixed-bit context transition on the full
context/helper product. T3's factor-of-surjection proof is unaffected.

The native all-word image, counter-dependent symmetry lift and checkpoint
extension class answer different questions. No apparatus, occurrence law,
original-residue receiver reader, energy account, characteristic-zero Hodge
realization, curvature-forcing result or L2-L6 bridge follows.

## 8. Supplied exploratory evidence and pending formal audit

The supplied `native_fiber_audit.py` and `native_fiber_output.json` report
78125 literal checkpoint/generator substitutions, 125000 checkpoint/bit/
lambda checks, 16000 counter-chart affine-basis instances for n=0..31, and
20480 entrance instances for n=0..4095, including n=14,z=0. They are
attributed, result-exposed exploratory records. This preparation does not
assert that they were reproduced, imported or executed here.

The bounded counter ranges cannot establish arbitrary n, and the lambda
checks establish sufficiency only for the four candidates. Universal
entrance, uniqueness and necessity of the complete extension classification
rest on Sections 4-6. Formal audit execution and its actual outcome belong
to the new pinned probe and remain pending at this proof's preparation.
