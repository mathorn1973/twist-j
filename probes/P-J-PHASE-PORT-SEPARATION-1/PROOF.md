# Exact obstruction for the specified phase preparations and port

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, Apache-2.0.
Proof status: AUTHORED_PROOF / SELF_REVIEWED; no Canon promotion.
This is a special-case application of the existing
U-CONTACT-SOURCE-NONINTERFERENCE theorem, with an explicit phase witness.

## 1. The source distinction and its existing native preparation

Let O=Z[j], Phi5(j)=0, with j a primitive fifth root, and let
tau_a(j)=j^a. For alpha define L=alpha*tau4(alpha) and
X=alpha*tau3(alpha). In the selected embedding L is the first squared
magnitude, tau2(L) is the second, and X is the mixed term C.

For alpha+=j and alpha-=j^-1=j^4, direct multiplication gives

    L(alpha+)=L(alpha-)=1,
    tau2(L(alpha+))=tau2(L(alpha-))=1,
    X(alpha+)=j^4, X(alpha-)=j.

The two X values are distinct, since j has order five. Both scalars and
both X values are units of norm one. This is an algebraic distinction,
with no physical momentum, phase instrument or photon identification.

The already declared coefficient map is

    ell=(0,1,2,-2,-1),
    Amp(p)=ell(p0)+ell(p1)j+ell(p2)j^2+ell(p3)j^3.

It gives the exact preparations

    p+=(0,1,0,0),
    p-=(4,4,4,4),
    Amp(p-)=-(1+j+j^2+j^3)=j^4.

This identifies two inputs of the existing declared preparation function.
It does not construct a physical preparer or a new source encoder.

## 2. The autonomous source quotient loses that distinction

For a native checkpoint x=(a,b,c,d,q,r), put z=sum(x) in F5 and
Q(x)=(z,q,r). The five actual native generators induce, respectively,

    (z,q,r), (-z,-q,-r), (2-z,1-q,-r),
    (2-z,1-q,1-r), (3-z,2-q,1-r).

All coordinates in this display are reduced modulo five. These formulas
follow by summing the six output coordinates of each declared generator
and retaining its last two. Selection is `(z+2*theta_n) mod5`, which
depends only on Q and the native counter. Therefore equal Q at a common
counter produces equal next Q and equal next counter. Induction proves
equality at every common native time, for any common driver word.

Both prepared sources have piston sum one: `1=4+4+4+4 mod5`.
With the existing common ready `(q,r)=(0,1)` their common quotient is
Q0=(2,0,1). Consequently their complete (q,r) histories coincide.
The first selected generator is g2, giving `(q,r)=(1,4)` and hence

    eta(q,r)=(ell(q)/2,(ell(r)+1)/2,0,0)=(1/2,0,0,0).

The excitation is nonzero. No property of a later decoder is used here.

Although the quotient coincides, the two source heads stay distinct.
They undergo the same successive generator indices, each of which is
bijective. A composition of these common bijections cannot identify two
different input checkpoints. This argument does not assert global
bijectivity of the state-selected U on its entire domain.

## 3. Composition with the complete continuing receiver

Write the complete receiver/protocol state as

    Y=(n,c,Xwave,W,b,B,sigma_A,sigma_B,d),
    Xwave=(u,v,A0,A1,B0,B1,k).

The two native heads are separate source states. All receiver coordinates,
including the pointer, budget, signs and captured second-source buffer,
are included in Y. Its initial value is common for all four ordered
choices in `{p+,p-}^2`.

The pair `(Q_A,Q_B)` and Y form a closed factor of every row of the
unchanged coupled program. Native rows update the two quotients by the
law above and advance the common counter. Wave/tape rows use only
Xwave. The capture row adds only the second head's (q,r) to d. Contact A
uses `S eta(q_A,r_A)`, while contact B uses `S eta(d)`.

Assume two runs have equal factor states before a row. Their next source
vectors agree. Their candidate wave shifts and energy changes agree;
both lower and upper stock guards therefore make the same decision.
Acceptance gives equal wave, work, stock and sign updates; refusal
leaves equal states equal. Buffer, pointer and phase updates also agree.
This proves factor equality after the row. Starting at their common
factor state, induction proves equality after every future program row.

Thus every fixed function of the actual retained record and common
context has identical outputs. The same argument covers a common
adaptive controller whose choice depends only on its receiver history:
equal histories give equal next choices. A controller which can consult
different source pistons or a supplied phase label violates this premise.

This is the all-future obstruction. The finite executable audit checks
the particular seven-step, cold, capacity-4/5 realization, both accepted
contacts and actual record retention. It does not promote eight equal
boundaries to an infinite theorem without the induction above.

## 4. Why the whole five-root source family is invisible here

In the same coefficient basis the five roots have residue vectors

    1   -> (1,0,0,0),    j   -> (0,1,0,0),
    j^2 -> (0,0,1,0),    j^3 -> (0,0,0,1),
    j^4 -> (4,4,4,4).

Each is its exact balanced lift and each has sum one modulo five. All
have L=1, while X(j^k)=j^(-k) takes five different values. The preceding
argument therefore applies to this complete five-root family with the
same ready and receiver. The runtime trajectories test its nominated
pair; the extension to all five is this finite algebraic proof.

Equivalently, evaluation j->1 defines the augmentation O->F5 because
Phi5(1)=5=0 in F5. It sends every j^k to one. The native source quotient
retains this augmentation and the common ready coordinates, not the
complete coefficients. It is smaller than O/(5). Indeed

    j-j^4=1+2j+j^2+j^3

is nonzero in O/(5^k) for every k>=1, since O is free over Z on the
displayed four-element basis. The full modular register retains this
particular distinction even when the native source quotient loses it.
For a general scalar, reduction followed by balanced lifting can change
its exact value; the five displayed root identities have no such gap.

## 5. What this decides

No reader acting only on this receiver's actual record and common context
can distinguish the nominated phase preparations. The positive control
in the verifier changes the transmitted quotient and shows a real second
record difference. It does not encode the missing mixed term secretly.

Multiplication by J in a separate scalar register can preserve and permit
calculation of X. That algebraic statement is compatible with the present
negative port result. An actual U-to-J bridge, physical preparation,
source-sensitive contact, independent late arrival, renewal, physical
photon or mass reading, and SI interpretation need separate premises.
None is supplied or ruled out in general by this special-case obstruction.
