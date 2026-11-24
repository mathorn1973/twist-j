# Native exchange and the two-cell paid-record boundary

PUBLIC / NON-CANONICAL / L1. Authored candidate-T, not Canon adoption.
A. M. Thorn; Apache-2.0. Claim #1616. Prepared before the first audit run.

The question is whether the concrete N=2 paid work machine of #1612 can
be read directly in the actual native preparations of #1615. The fixed
checkpoint-only proposal fails after two ticks. A literal primitive lift
fails both on refusal and on a bank payment. These are scoped exclusions,
not a no-go for native physical interaction. The older native two-slot
exchange of #994 is retained as a positive comparison; it does not supply
the missing work-machine receiver or select physical energy.

## 1. Inputs, inheritance and complete states

SOURCES.tsv pins the definitions. Public Canon v103 supplies native U,
the stable-sheet laws, the exact field form and unit shell, the
source-factor noninterference theorem, and the arbitrary clocked-reader
classification. #1612 supplies the chosen work law. #1615 proves its
complete invariant carrier and the five actual native phase preparations.
The funded signed-swap construction and its refusal boundary already occur
in #1594/#1591. They are not discovered here.

Likewise, #994 already establishes the centered native block exchange,
source-sensitive fixed-slot transfer, occupied continuation, actual timing,
and pure transport without a permanent record. #975 already exhibits
positive conserved integer budgets and their nonselection. Sections 6--7
restate that exchange and add the specific normalized block-additive
classification used for the present comparison. They do not claim a new
native coupling or a general first proof of energy nonuniqueness.

Native state is (n,psi) in N_0 x F5^6, with
psi=(p1,p4,p1prime,p4prime,q,r), z=sum(psi), and
theta_n=popcount(n) mod2. At step n, U advances n and applies the letter
of index z+2theta_n modulo5, in order a,b,c,d,e. Writing
psi=(a,b,c,d,q,r) only in the following formulas, the five letters are

```
a: (b,a,d,c,q,r)
b: (-c,-d,-a,-b,-q,-r)
c: (2-c,1-d+r,2-a,1-b-r,1-q,-r)
d: (2-a,1-b,3-c,4-d,1-q,1-r)
e: (2-a,1-b,3-c,4-d,2-q,1-r).
```

All six coordinates are retained and arithmetic is in F5. Their induced
trace updates are respectively z,-z,2-z,2-z,3-z. On
X14={psi:z in {1,4}}, the selected transitions are

| Input z | Bit | Letter | Output z |
|---|---|---|---|
| 1 | 0 | b | 4 |
| 1 | 1 | d | 1 |
| 4 | 0 | e | 4 |
| 4 | 1 | b | 1 |

Each displayed letter is an involution on the full checkpoint space.
For a fixed bit, its restriction from a KNOWN input sheet is a bijection
onto the indicated output sheet. On the union X14 the selected map is
two-to-one, not a permutation. No global inverse of native U is asserted.

The comparison carrier Sigma2 uses the exact reduced coordinates

    s=(y,Rs,Rr,q,e,p),
    H(y)+Rs+Rr+q+2e=15,

where y in Z4, Rs,Rr,q are nonnegative integers, e in {0,1}, p in C5.
This is a bijective description of the full declared carrier of #1615,
not a projection throwing away moving registers. Source matter is ZM;
receiver matter is its literal R/AM tuple according to e; all spectators,
static fields and receiver active field vanish; source raw field is Py.
The receiver baseline contributes18 and the original pointer contributes1,
so the complete energy is34. The resources retain their original roles.

Write y=(a,b,c,d). The inherited field definitions are

\[
H(y)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
\]

\[
A=\begin{pmatrix}1&0&1&0\\0&1&0&1\\-2&1&-1&1\\1&-3&1&-2\end{pmatrix},
\qquad B y=(-c,-d,-a,-b).
\]

Direct multiplication gives A^5=I, B^2=I and H(Ay)=H(y). Define
f(a,b)=(a-b)^2+b^2. Expansion gives

\[
\Delta(y)=H(By)-H(y)=f(c,d)-f(a,b).
\tag{1}
\]

The guarded source contact is

\[
K(y,R)=\begin{cases}(By,R-\Delta(y)),&R\ge\Delta(y),\\
(y,R),&R<\Delta(y).
\end{cases}
\tag{2}
\]

It is a total involution preserving H+R. Indeed Delta(By)=-Delta(y);
an accepted image can pay its reverse because R-Delta>=-Delta iff R>=0.
An accepted image therefore cannot be a refused input. This also proves
invariance of D15={(y,R):H(y)+R<=15,R>=0}.

The receiver acts by

```
e=0,Rr>=2: (Rr,e,p) -> (Rr-2,1,p+1)
e=1:       (Rr,e,p) -> (Rr+2,0,p)
e=0,Rr<2:  fixed.
```

Its true inverse sends (Rr,1,p) to (Rr+2,0,p-1), sends
(Rr,0,p) with Rr>=2 to (Rr-2,1,p), and fixes the remaining inputs.
Both preserve Rr+2e. One complete T applies K, then the receiver, swaps
Rs with q, swaps q with Rr, and finally applies A to y. Reversing those
layers with A^-1=A^4 gives T^-1. Every primitive and its inverse preserves
Sigma2, including arbitrary occupied pointer values and returned resources.
This restates #1615's all-carrier proof at N=2; the finite audit is not
its only evidence.

## 2. The frozen checkpoint reader cannot write the required HIT

For a in F5 take the #1615 origin-zero native preparation
xi_a=(a,-a,0,0,0,0). The actual first letters are a,c,e and their states are

```
psi1=(-a,a,0,0,0,0)
psi2=(2,1,2+a,1-a,1,0)
psi3=(0,0,1-a,3+a,1,1).
```

The last state has z=1. Since theta3=0 and theta4=1, the next actual
letters are b,b, and

\[
\psi_4=(a-1,-a-3,0,0,4,4),\qquad \boxed{\psi_5=\psi_3}.
\tag{3}
\]

This is equality of all six checkpoint coordinates. The native counters
3 and5 remain different.

For the work machine put v0=(2,-1,0,0), v_a=A^a v0 and
s_a=(v_a,0,0,0,0,0). The fields and changes Delta are

| a | v_a | Delta |
|---|---|---|
| 0 | (2,-1,0,0) | -10 |
| 1 | (2,-1,-5,5) | 115 |
| 2 | (-3,4,5,-10) | 260 |
| 3 | (2,-6,-5,10) | 225 |
| 4 | (-3,4,5,-5) | 60 |

All have H15. Thus the nonemitting states simply advance along A until
they reach s0, after [-a]_5 full steps. Put y0=Bv0=(0,0,-2,1), H(y0)=5.
The first step releases10 from source field, and delivers it to Rr after
the receiver has already acted. At the second step the receiver consumes2
and writes p=1. Explicitly

\[
Ts_0=(Ay_0,0,10,0,0,0),\qquad
T^2s_0=(A^2y_0,0,0,8,1,1).
\tag{4}
\]

For the second expression the source remains fixed before free evolution:
Ay0=(-2,1,3,-4) has Delta55 and zero source resource. Hence the five
first HIT times are2,6,5,4,3.

Suppose any fixed function O:F5^6->{0,1} realizes the frozen comparison

\[
O(\psi_{3+t}(\xi_a))=1[p(T^t s_a)\ne0]\quad(a\in F5,t\ge0).
\tag{5}
\]

Equations (3)--(4), already for a=0,t=0,2, demand that the same input
have outputs0 and1. This is impossible, regardless of O's nonlinearity
or use of all current residues. This is the primary negative result.

It applies to this initialization, tick alignment and checkpoint-only
reader. It does not exclude a reader using the existing counter, a
different native carrier, additional physical state, different cuts, a
macrostep protocol or other preparations. In particular it does not
contradict #1615's clocked free-phase factor. The old common-(z,q,r)
noninterference theorem is a different, inherited obstruction.

## 3. Literal piston and bank identifications fail at the primitive level

Native b sends the four pistons by the signed swap B. Nevertheless the
whole guarded K does not reduce to b under the literal projection y mod5.
At v1=(2,-1,-5,5),R=0, Delta115 causes refusal, so K fixes its input,
while

\[
v_1\bmod5=(2,4,0,0),\qquad Bv_1\bmod5=(0,0,3,1).
\tag{6}
\]

No encoding of the two remaining native coordinates repairs this piston
inequality for a proposed b implementation on the whole local domain.
Choosing a different native letter after the refusal is another proposal.

Even on an accepted branch, identifying native r with R mod5 would
require R-Delta=-R mod5, or Delta=2R mod5. The legal witness
u=(-3,0,1,0),R=2 has H13, Delta=-8 and output resource10. Its residue0
differs from native b's -2=3. This is the earlier #1615 equal-energy
payment witness applied to the literal bank port. It lies in D15 and in
full Sigma2, but not in the five prepared trajectories or their Lambda
field sublattice. No reachability assertion for that witness is made.

## 4. Exact affine bank obstruction, and the nonlinear exception

Consider the declared class h(y,R)=u.y+vR+c in F5, with equality of
values, on every (y,R) in D15. The equation required by a native b
coordinate is

\[
h(K(y,R))=-h(y,R).
\tag{7}
\]

Six legal inputs force h=0. The fixed inputs (0,0),(0,1) force c=v=0.
For coordinate vectors e1,...,e4, (e3,0),(e4,0) are refused because their
Delta are1 and2. They force u3=u4=0. The accepted images

    K(e1,0)=(-e3,1), K(e2,0)=(-e4,2)

then force u1=u2=0. Conversely zero solves (7). All six inputs have
H+R<=3, so no boundary approximation or unbounded-energy premise is used.

The affine conclusion cannot be extended to all scalar functions. Since
K is an involution, for ANY f:D15->F5,

\[
h_f=(f-f\circ K)/2
\tag{8}
\]

solves (7). Every solution occurs this way, by choosing f=h. Equivalently,
h vanishes at K fixed points and has opposite values on each nontrivial
two-cycle. For f(y,R)=R mod5 this is the explicit global guarded solution

\[
h(y,R)=3(R-R_K)\pmod5.
\tag{9}
\]

For instance h(e1,0)=2, so it is nonzero. At u,R2 of section3 it is1,
and on its reverse it is4. Refusal gives zero automatically. Equation(9)
is only a scalar intertwining character: it does not store the exact
resource, encode the full receiver, establish native selection or supply
an injection of full states. It marks the precise boundary of the affine
negative, rather than implementing a nonlinear native bank.

## 5. A complete Sigma2 cannot fit in one checkpoint at common counter

This independent counting obstruction applies even to nonlinear
injective encodings. The positive quadratic form has the square identity

\[
4H=Q(a,b)+(2c+2a-b)^2+(2d-a+3b)^2,
\quad Q=3a^2+2ab+2b^2.
\tag{10}
\]

It is positive definite: 2Q=5a^2+(a+2b)^2 and
3Q=5b^2+(3a+b)^2. H0 therefore contains only zero. If H1, Q<=4 forces
|a|,|b|<=1. The square fibers give exactly the following20 unit vectors,
the same inventory as Canon FIELD-UNIT-RESIDUE-CLASSIFICATION:

```
(0,0,+/-1,0), (0,0,0,+/-1)                         [4]
+/-(1,0,-1,0), +/-(1,0,-1,1)                      [4]
+/-(0,1,c,d), c in {0,1}, d in {-1,-2}             [8]
+/-(1,-1,c,2), c in {-1,-2}                       [4].
```

For completeness: Q(0,0)=0 leaves four solutions of two squares summing4;
Q(0,+/-1)=2 leaves four fibers for each sign; Q(+/-1,0)=3 leaves two
each; Q(1,-1)=Q(-1,1)=3 leaves two each. Same-sign nonzero a,b have Q7
and are excluded. The parity of each displayed linear square fixes the
listed c,d. Thus the count uses an exact finite classification, not an
unjustified box search. Only distinctness and H1 are needed for the lower
bound below; the audit also checks those facts directly.

For a fixed field of energy h=0 or1 and receiver bit e, the three
resources sum to15-h-2e. Stars and bars, including all5 pointer values,
gives

\[
N_h=5\left[\binom{17-h}{2}+\binom{15-h}{2}\right].
\tag{11}
\]

These are different COMPLETE legal Sigma2 states. Consequently

\[
|\Sigma_2|\ge N_0+20N_1=1205+20(1055)=22305>15625=|F5^6|.
\tag{12}
\]

No injection of full Sigma2 into a single native checkpoint exists at
a common native counter. This already holds before imposing any dynamics.
The H0/H1 subset itself is not invariant: its full forward/backward
images may have other field energies, still within Sigma2. The verifier
checks both compositions and admissibility of those continuations without
mistaking the subset for the whole carrier.

Equation(12) is not a minimum memory theorem for the five preparations,
a weaker observation, multiple native checkpoints, or source-dependent
counter encodings. In particular it does not conflict with #1615's
lambda6 field precision: that representation retains the machine's other
coordinates as well, and equal field-quotient cardinalities never supplied
a full native-machine identification.

## 6. The inherited native exchange, with actual preparations

On X14, the common piston center of b,d,e is p*=(1,3,4,2). Set
uL=(p1-1,p4-3), uR=(p1prime-4,p4prime-2). Direct substitution in the
original letters gives the #994 normal form

\[
b:(u_L,u_R)\mapsto(-u_R,-u_L),\qquad
d,e:(u_L,u_R)\mapsto(-u_L,-u_R).
\tag{13}
\]

These are two internal piston blocks of ONE checkpoint, not two spatial
field-chain cells or two copies of native U. The actual q,r and selector
remain present. Let ell:F5->{-2,-1,0,1,2} be the balanced representative.
Since ell(-v)=-ell(v), (13) is also an exact equality for the balanced
integer vectors. Every even block function therefore transfers with the
block on b and stays in place on d/e.

Here is an explicit origin-reachable comparison with a blank right block
at cut3. For t in F5 use

\[
x_0(t)=(0,3,2-t,1+t,0,4).
\]

The actual a,c,e prefix gives

\[
x_3(t)=(1+t,3-t,4,2,1,0),\quad
x_4(t)=(1,3,4-t,2+t,4,0),\quad x_5(t)=x_3(t).
\tag{14}
\]

The last two letters are the actual b,b at n3,4. At preparation cut3
the entire right block and raw q,r are common, and uL=(t,-t),uR=0.
At cut4 the source block is zero and the right block contains -uL.
The next actual contact returns it. With the DECLARED reading
F2(u)=||ell(u)||^2, source loss equals receiver gain2ell(t)^2, giving
0,2,8,8,2 for t=0,...,4. The same equality holds for occupied inputs:

\[
\Delta E_R=F(u_L)-F(u_R)=-\Delta E_L.
\tag{15}
\]

This is an actual source-sensitive transfer under the inherited fixed
slot observation. No counter evaluating a target trajectory produces the
output. But the multiset of the two sign-orbit messages never changes;
iterating (13) only changes signs and placement. It is the pure transport
already emphasized in #994, with no creation of new packet values and
no permanent BLANK-to-HIT archive. A subsequent exchange reverses it.

Source/receiver roles in (14) are specified at cut3. The varying payload
in x0 lies in the other raw block, so the preparation prefix must not be
called a source-local loader with fixed roles. No conservation of F2
over the transient a,c,e prefix, preparation payment or physical loading
mechanism is asserted. Origin reachability and conserved stable-tail
exchange are different statements.

## 7. Exact block-additive energy family: twelve independent values

Freeze readings E=L(uL)+R(uR) with L,R:F5^2->R and L(0)=R(0)=0.
Require invariance under EVERY selected stable update for both bits on
the entire X14. All pairs u,v occur on either sheet: choose q after
fixing pistons and r. Thus the d/e conditions imply

    L(-u)+R(-v)=L(u)+R(v) for all u,v.

Setting v=0 or u=0 forces each function to be even. The b condition,
with the other block zero, then forces L(u)=R(u). Conversely every
common even F obeys (13). Therefore the complete answer in this class is

\[
\boxed{E=F(u_L)+F(u_R),\quad F(-u)=F(u),\quad F(0)=0.}
\tag{16}
\]

There are (25-1)/2=12 nonzero sign orbits, whose values can be assigned
independently. Nonnegative or strictly positive-on-nonzero readings give
the corresponding cone, without fixing the12 values. This is a restricted
block-additive corollary, not a classification of all native invariants.
It is different from #975's eight-parameter separated protected-coordinate
class and sits inside the older general native invariant theory.

Concretely F4=F2^2 is equally admissible and yields0,4,64,64,4 on(14),
not a constant multiple of its F2 output. Even if one restricts to positive
quadratic expressions in balanced coordinates, every positive-definite
symmetric metric G gives an even F_G=ell(u)^T G ell(u). G=I and
G=diag(1,2) agree at(1,0), but assign1 and2 to(0,1).

Both sources u=(1,0),(0,1) can be placed at native cut3 with right block0
and the SAME raw q=r=0: their piston sums both give z1. Actual b therefore
transfers them with work readings(1,1) for I and(1,2) for diag(1,2), while
the complete native transition is unchanged. This disproves uniqueness
in the declared reading class, even after fixing the first source's unit.
It does not declare all readings physically inequivalent after every
possible physical symmetry; no such equivalence or independent selection
has been supplied for this frozen fixed-coordinate class.

## 8. What this decides, and what would close the next step

The comparison now has explicit outcomes rather than an unspecified
native bridge. The frozen checkpoint reader cannot implement even the
first work HIT; the literal signed-swap lift fails; all affine odd bank
ports vanish, while nonlinear odd scalar ports exist. Full Sigma2 also
exceeds one checkpoint's capacity at common counter. None of these facts
constitutes a universal obstruction to a richer native apparatus.

The native exchange that does exist carries a chosen conserved value,
but it is the older signed block swap and does not realize the field
release H15->5 plus bank10, its receiver's payment2, or its pointer.
The12-value classification prevents conservation alone from selecting the
physical energy in this comparison. No equality of the integer payment10
with 2sqrt(1+m^2)-2m, no E=h nu, no entropy cost, no inertial mass and no
physical spatial partition follows.

A next constructive claim must specify a complete native carrier and
independently admitted interaction, source-dependent actuation of a real
receiver, actual resources and inverse/occupied continuation. It must say
which information channel avoids (3) and which state capacity avoids(12).
A desired work law encoded in a reader through the counter is insufficient:
the Canon's reachable clocked-reader classification already permits chosen
target bijections through that route. A physical energy assignment also
needs an independent selection or equivalence rule within a frozen class.

No new scientific executable was used in deriving this proof. verify.py
audits its preregistered finite witnesses and inventories after the public
pin. The all-domain arguments above are algebraic; successful computation
does not by itself promote them or supply external independent review.
