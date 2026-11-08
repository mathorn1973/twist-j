# Analytical proof and exact boundaries

Status: NON-CANONICAL, L1, candidate-T for the conditional mathematical
statements below. All apparatus definitions remain NEW_DECLARED. This file
contains analytic proofs and predictions, not a record of execution or a
claim of native or physical realization.

The analytical reviewer read PREREG.md and the public Canon K1 definition,
but neither implementation. The model and its predicted outcomes were known
to the reviewer. This is analytical review within the same assisted session,
not external or result-blind confirmation. Source authority and custody are
specified by PREREG.md and SOURCE.md.

## 1. Ring, conjugation and Hermitian coordinates

Work in O=Z[j]=Z[X]/(1+X+X^2+X^3+X^4), with K=Q(j) and bar(j)=j^-1.
Write phi=-j^2-j^3, J=1+j^2, and K+=Q(phi). Direct multiplication gives

```text
phi^2=phi+1,          phi^-1=phi-1,
J^-1=-j-j^2,         J phi=j,
J bar(J)=phi^-2,     j+bar(j)=phi-1.
```

The representation of an element of O by four integer coefficients in
(1,j,j^2,j^3) is unique. If an element with coefficients (r0,r1,r2,r3)
is fixed by conjugation, comparison with its conjugate gives r1=0 and
r2=r3. It is therefore r0-r2 phi. Consequently the fixed integral subring
is exactly O+=Z[phi], and the eight coordinates H8 in PREREG.md are a
unique integral representation of every Hermitian matrix.

The field trace satisfies Tr(1)=4 and Tr(j^k)=-1 for k=1,2,3,4.
In particular Tr(phi)=2. Throughout this file, capital Tr is Tr_(K/Q)
and lower-case tr is ordinary matrix trace.

For any invertible M over O whose inverse also has entries in O, the map
rho(M)H=M H M^dagger is an integral Hermitian bijection, with inverse
rho(M^-1). It obeys the universal identity

```text
det(rho(M)H)=det(M) bar(det(M)) det(H).
```

For A=diag(J,phi), det(A)=j and det(A)bar(det(A))=1. Both upper shears
B(q) and lower shears L(q) have determinant one and integral inverse at
every integer q. This proves determinant preservation for every transport
used by the apparatus and for all six transport gates in the finite audit.
It applies to arbitrary Hermitian H, including singular and indefinite H.

## 2. Positive integer cost and finite shells: A2

For H=[[a,c],[bar(c),d]], put a=a0+a1 phi, d=d0+d1 phi, and
c=sum_(i=0)^3 c_i j^i. Then

```text
N(H)=Tr(tr(H^2))=Tr(a^2+d^2+2c bar(c)).
```

Since the traced element is an algebraic integer, N(H) is an integer.
The trace identities of section 1 give its complete coordinate expression:

```text
N(H)=4a0^2+4a0 a1+6a1^2
     +4d0^2+4d0 d1+6d1^2
     +2[5 sum_i c_i^2-(sum_i c_i)^2].
```

For the diagonal part,

```text
4a0^2+4a0 a1+6a1^2
  =2(a0+a1)^2+2a0^2+4a1^2
  >=2(a0^2+a1^2).
```

The same identity applies to d. The elementary inequality
(sum_i c_i)^2<=4 sum_i c_i^2 gives

```text
N(H)>=2 sum_(i=1)^8 H8_i^2.
```

Thus N is positive definite on the eight-dimensional integer module. This
is a statement about the quadratic cost, not positive semidefiniteness of
the matrix H. In particular it is valid for every allowed detector Z.

The source-link form Q(s,q)=s^2-sq+q^2 satisfies

```text
2Q(s,q)=s^2+q^2+(s-q)^2,
Q(s-q,s)=Q(s,q).
```

Hence E(x)=1+Q(s,q)+N(H)+N(R)+N(Z) is a positive integer. On a fixed
total-cost shell E(x)+b=W, with b>=0, the following bounds hold:

```text
s^2+q^2<=2(W-1),
2[sum H8_i^2+sum R8_i^2+sum Z8_i^2]<=W-1,
0<=b<=W-1.
```

There are only finitely many integer coordinates satisfying these bounds,
six phases, and two directions. Every such shell is finite. Once A1 is
proved below, F acts as a permutation on each shell. Every full F orbit
therefore is periodic from its initial state; there are no transient tails
feeding an attractor on this complete state space. An external unbounded
counter is not a coordinate of this apparatus.

The six phase states and two direction states share the chosen baseline
cost one. No separately positive switching or reflection toll is imposed.
These are NEW_DECLARED cost conventions, not a derivation that physical
control, switching, or reflection has this cost.

## 3. Bare and funded bijections: A1

At phase zero the source-link map has inverse

```text
(s',q')->(q',q'-s').
```

At the four transport phases the inverse is the inverse congruence from
section 1. At the detector phase, H and R are unchanged, so the inverse is
Z<-Z-H+R. The output phase identifies the preceding phase uniquely.
Decrementing phase and applying this preceding operation's inverse proves
that the bare map T is a total bijection of its declared carrier.

Now let x=(s,q,H,R,Z,p), let epsilon be +1 or -1, and put

```text
y=T^epsilon x,            c=b+E(x)-E(y).
```

If c>=0, F sends (x,b,epsilon) to (y,c,epsilon). Otherwise it sends it
to (x,b,-epsilon). The new bank is nonnegative in both branches, and
E+b is unchanged in both branches. The reference R is retained by all
bare operations and by the rejection branch.

To prove the claimed inverse, start with any (x,b,epsilon), put

```text
z=T^(-epsilon)x,          d=b+E(x)-E(z),
```

and return (z,d,epsilon) if d>=0, otherwise (x,b,-epsilon).

If d>=0, the proposed predecessor has a funded forward move to x because
its resulting bank is d+E(z)-E(x)=b>=0. A reflected predecessor with the
same x and opposite direction is impossible: its test would be exactly
the nonnegative quantity d, so it would move rather than reflect.

If d<0, the same-position predecessor (x,b,-epsilon) fails its attempted
move to z and reflects to (x,b,epsilon). A moving predecessor with
direction epsilon would necessarily be z and would require bank d<0,
which is outside the carrier. These two cases give exactly one predecessor
to every state and prove both inverse compositions universally.

A rejection changes only the stored direction. In particular it retains
s,q,H,R,Z,p,b, but is not the identity on the full state. It is an atomic
refusal of one microstep, not of the entire six-phase cycle. Accepted
earlier phases are still present when a later phase is refused.

## 4. Source-controlled loop: A3

The exact constants reduce to

```text
u=J/phi=-1+j-j^2,
v=u-1=-2+j-j^2,
w=v bar(v)=9-5phi=9+5j^2+5j^3.
```

For example, u=j phi^-2 and

```text
w=phi^-4-phi^-3+1=9-5phi.
```

Conjugating the upper shear by A gives B(q u). Therefore the four
successive transport phases, whose action order is from right to left in
the product, give

```text
C_q=A B(q) A^-1 B(-q)=[[1,qv],[0,1]].
```

The source update occurs before these phases, and q is unchanged during
all four. Thus this is the loop corresponding to the actual stored q.
For q!=0, qv!=0 in the characteristic-zero integral domain O. The action
is nontrivial: on D=diag(0,1) it gives

```text
rho(C_q)D=[[q^2 w,qv],[q bar(v),1]],
```

whose off-diagonal entry differs from that of D. This proves
nontriviality as an action, not that every individual H changes.

The source-link update s'=s-q, q'=s has both dependencies: changing s at
fixed q changes q', and changing q at fixed s changes s'. This is exactly
the reciprocal coupling claimed. The kick does not use H,R,Z or a
curvature tensor. Their role in deciding motion is limited to the
funding test. A gravitational source law is not inferred from this
two-register map.

## 5. Occupied detector, budgets and reversals: A4

Take a in {-1,+1} and the frozen ready state

```text
s=a, q=0, H=R=D=diag(0,1),
Z=Z0=[[1,j],[bar(j),1]], p=0, epsilon=+1.
```

The first phase sends (s,q) to (a,a); it does not empty the source.
The successive H matrices in the four transport phases are

```text
H1=[[1,-a],[-a,1]],
H2=[[phi^2,-a j^-1],[-a j,phi^-2]],
H3=[[4-phi,a(phi^-2-j^-1)],
    [a(phi^-2-j),phi^-2]],
H4=[[w,av],[a bar(v),1]].
```

Each has determinant zero by section 1. For a two-by-two matrix of
determinant zero, tr(H^2)=(tr H)^2. Their ordinary traces are respectively
2, 3, 6-2phi, and 10-5phi. Consequently

```text
N(D)=4,
N(H1)=16,
N(H2)=36,
N(H3)=Tr(40-20phi)=120,
N(H4)=Tr(125-75phi)=350.
```

Also N(Z0)=16, Q(a,0)=Q(a,a)=1, and N(R)=4. These identities give all
prefix costs through the final transport phase:

```text
(26,26,38,58,142,372).
```

At the detector phase,

```text
Z_a=Z0+H4-R=[[1+w,j+av],[bar(j)+a bar(v),1]].
```

Since w^2=106-65phi, the preregistered constant traces are

```text
Tr(w)=26,                  Tr(w^2)=294.
```

The mixed term is

```text
c=j bar(v)+bar(j)v=5-3phi,   Tr(c)=14.
```

Direct multiplication, using a^2=1, gives

```text
tr(Z_a^2)=w^2+4w+4+2a c,
N(Z_a)=414+28a,
E_final=770+28a.
```

Thus the complete bare prefix costs are exactly

```text
a=-1: (26,26,38,58,142,372,742),
a=+1: (26,26,38,58,142,372,798).
```

Every difference in either displayed sequence is nonnegative. Therefore
the maximum prefix increase, rather than only the final increase, equals
716 for a=-1 and 772 for a=+1. These are the sharp banks needed for six
consecutive forward successes from the frozen ready states.

All four audit banks 715,716,771,772 are at least 346, the cost increase
through the fifth microstep. The first five steps therefore succeed in
each frozen experiment. At p=5 the bank is b_initial-346. The final
detector gate costs 370 for a=-1 and 426 for a=+1, proving the exact
success thresholds in PREREG.md. If refused, the state retains H=H4,
Z=Z0, p=5 and that bank, and epsilon becomes -1. The general inverse in
section 3 reverses the entire six-step recorded history, including a
last-step reflection, without any additional history tape.

For common initial bank 772 the final banks are 56 and 0 for a=-1 and
a=+1. The initially nonzero coefficient of j in Z01 starts at 1 and
ends at 1+a. The fixed reader coeff_j(Z01)-1 therefore returns a. The
same read coordinate is changed, and old detector data remain recoverable
as Z_old=Z_new-H+R from the retained full state.

One necessary carrier boundary is explicit:

```text
det(Z_a)=-a(5-3phi).
```

The positive-sign output is indefinite at the principal real embedding.
The proof requires the declared full Hermitian detector carrier, not a
positive-semidefinite detector class. Positive definiteness of N(Z) does
not impose positive semidefiniteness on Z itself.

## 6. Six loops and the finite cost of a record: A5

For the source-link map, its integer two-by-two matrix has third power
-I and sixth power I. Starting at (s,q)=(a,0), the six successive pairs
after the source phase are

```text
(a,a), (0,a), (-a,0), (-a,-a), (0,-a), (a,0).
```

Thus the q values in the six transport loops are a,a,0,-a,-a,0.
The loop matrices are upper shears and satisfy C_r C_t=C_(r+t).
The cumulative controls after those loops are a,2a,2a,a,0,0.
It follows that H returns to D and the other retained registers s,q,R,p
return to their initial values after 36 bare phases.

At the detector phase following a cumulative control r, the increment is

```text
rho(C_r)D-D=[[r^2 w,rv],[r bar(v),0]].
```

The sums of the six cumulative controls and their squares are 6a and 10.
Hence the total detector increment is exactly

```text
Delta Z_a=[[10w,6a v],[6a bar(v),0]].
```

In the fixed H8 coordinates it is

```text
a=-1: [90,-50,0,0,12,-6,6,0],
a=+1: [90,-50,0,0,-12,6,-6,0].
```

The increment is nonzero. Bare repetition returns the source, link and
transported register to the same values at every 36-phase boundary, so it
would produce Z=Z0+m Delta Z_a after m such blocks. Since N is positive
definite, N(Z0+m Delta Z_a) is a quadratic polynomial in m with strictly
positive leading coefficient N(Delta Z_a). It is unbounded as m grows.
Therefore a fixed finite total E+b cannot support this all-forward
continuation forever. The 36-phase calculation concerns bare T, not an
assertion that every one of these phases is funded in F.

This record construction is reversible accumulation with a finite account.
It is not an irreversible detector, a permanent monotone archive, or a
derivation of time orientation. The full funded dynamics remains periodic
on each finite shell by A1 and A2.

## 7. The four negative controls

First, M=diag(J,1) has field norm N_(K/Q)(det M)=N_(K/Q)(J)=1, but

```text
det(rho(M)I)=J bar(J)=phi^-2!=1.
```

Indeed the norm of J is the product of phi^-2 and its real conjugate,
which is one because phi(1-phi)=-1. A scalar's absolute field norm one
does not replace the stronger element identity det M bar(det M)=1
required for this determinant-preserving Hermitian action.

Second, jI is a nonidentity matrix, but

```text
rho(jI)H=j H bar(j)=H
```

for every H. Its central phase is invisible to the Hermitian action.

Third, C_1 and I both have ordinary matrix trace two, while section 4
exhibits different actions on D. Trace alone does not detect this shear
holonomy.

Fourth, for any invertible frames g0,g1,g2,

```text
(g0 g2^-1)(g2 g1^-1)(g1 g0^-1)=I.
```

This applies in particular to the frozen I,A,B(1) frames. Pure frame
differences telescope around their loop; merely changing frames does not
supply nontrivial loop curvature.

These are exact counterexamples to four shortcuts, not counterexamples
to the selected apparatus.

## 8. All-counter K1 denominator theorem

Use precisely DEF-K1-LINEAR-METRIC in the pinned Public Canon v103.
Its ten words and both initial slices are the ones reproduced in
PREREG.md. No word weights or stochastic assumptions enter this proof.

Let S act on five coordinates cyclically and write

```text
C=460I+29(S+S^-1)+65(S^2+S^-2),
h_(n+1)=C h_n/324-h_(n-1).
```

Every row and column sum of C equals 648. Since both initial h slices
have sum one, induction gives sum h_n=1 for every n>=0. Set

```text
z_n=10h_n-2 ones.
```

Then sum z_n=0, and C ones=648 ones gives the same homogeneous recurrence

```text
z_(n+1)=C z_n/324-z_(n-1).
```

Both initial z slices have two entries 3 and three entries -2. They
therefore have minimum 3-adic coordinate valuation zero, for every one
of the ten fixed words, regardless of whether its initial two slices
happen to coincide.

Define nu_3(z)=min_r v_3(z(r)) for a nonzero rational vector and
v_3(0)=+infinity in coordinate comparisons. Let E5 denote the all-ones
five-by-five matrix. The coefficient reductions give

```text
C mod 3=-(I+E5).
```

On the sum-zero subspace, E5 z=0. For any rational sum-zero vector z,
multiply it by 3^(-nu_3(z)) to obtain a vector over Z_(3) with at least
one unit coordinate. Its C-image modulo 3 is its negative, so it still
has a unit coordinate. Scaling back proves the exact universal identity

```text
nu_3(Cz)=nu_3(z).
```

Since v_3(324)=4, the first recurrence step compares valuations -4
and 0; they cannot cancel. Thus nu_3(z_2)=-4. Inductively, for n>=2,

```text
nu_3(C z_n/324)=-4n,
nu_3(z_(n-1))=-4(n-2).
```

These valuations are unequal. In a vector difference, a coordinate
attaining the smaller valuation cannot be canceled by coordinates all
having greater valuation. Therefore

```text
nu_3(z_n)=-4(n-1),       n>=1.
```

For n>=2, this value is negative. Adding 2 ones cannot cancel it, and
division by 10 does not change a 3-adic valuation. Hence the same minimum
valuation holds for h_n. For n=0,1 the initial half-valued slices have
minimum valuation zero directly.

If d_n is the least positive common denominator of the five reduced
rational coordinates of h_n, then

```text
v_3(d_n)=max(0,-min_r v_3(h_n(r))).
```

We obtain exactly

```text
v_3(d_0)=0,
v_3(d_n)=4(n-1),         n>=1,
```

for every fixed word in the declared ten-word set. This proves the
all-counter statement independently of the finite n<=24 audit. It is
an exact assertion about the power of three in the least denominator;
it does not state that no other prime divides that denominator.

### Fixed denominator and fixed polynomial readings

A rational-valued reading whose denominator always divides one fixed
positive integer D has v_3 of its denominator bounded by v_3(D). It
cannot return the exact K1 five-vector at all counters for any one of
the declared words, by the preceding unbounded formula.

In particular, take finitely many fixed polynomials in integer state
coordinates, with rational coefficients. Choose D divisible by every
coefficient denominator. Every value of each polynomial lies in (1/D)Z,
regardless of the size of the state coordinates or polynomial degree.
The same obstruction applies. More generally, if coefficients lie in
a fixed number field and D clears their algebraic-integer denominators,
evaluation on algebraic-integer state coordinates gives an algebraic
integer after multiplication by D. Whenever the output is rational,
it is then an ordinary integer divided by D.

This argument does not exclude rational division by a state-dependent
denominator, a stored numerator/denominator pair, variable precision,
or a different construction and reading contract. Merely permitting
unbounded integer numerators in a fixed polynomial does not evade it.

### Every fixed current-state reader on a finite shell

Fix one total resource W and one complete F orbit. By A2 it lies in a
finite shell. Every fixed, single-valued current-state reader from this
shell to Q^5 has finite image. The least common multiple of the reduced
coordinate denominators over that image is one fixed finite integer D.
The K1 denominator theorem therefore excludes exact all-counter K1
reading on that orbit for every declared input word, even if the reader
is nonlinear and not polynomial.

The state already includes all admitted phase and direction storage.
Adding an external counter, an unbounded record, more total resource,
or a horizon-dependent reading changes this contract. This result is a
boundary of the selected finite-resource apparatus, not a no-go for
every integral realization with growing precision or another carrier.

## 9. A fixed-form square-class obstruction

The K1 metric matrices are

```text
g_h=diag(-1,1+h,1-h,1),       det(g_h)=-(1-h^2).
```

Every initial K1 slice contains both h=0 and h=1/2. Consider the restricted
proposal that there is one fixed nonsingular symmetric form Q0 over
K+=Q(sqrt(5)) and frames E0,Ehalf in GL_4(K+) satisfying

```text
g_0=E0^T Q0 E0,
g_(1/2)=Ehalf^T Q0 Ehalf.
```

Taking determinants forces

```text
3/4=det(g_(1/2))/det(g_0)=(det(Ehalf)/det(E0))^2.
```

But 3/4 is not a square in K+. If (a+b sqrt(5))^2=3/4 with a,b rational,
the sqrt(5) coefficient gives ab=0. If b=0, a^2=3/4 has odd 3-adic
valuation and cannot be a rational square. If a=0, b^2=3/20 also has
odd 3-adic valuation and cannot be a rational square. Both possibilities
are excluded.

Thus this one-fixed-form, K+-frame proposal already fails on the initial
K1 slice. The proof does not prohibit real frames, a suitable larger
coefficient field, a varying base form, or another metric construction.
It does not identify the apparatus H with a four-dimensional metric.

## 10. Rank-eight integrality is not a rank-four spacetime lattice

At the principal complex embedding, the real vector space Herm_2(C) has
dimension four. In coordinates a,d,Re(c),Im(c), rho(A) acts by

```text
a->phi^-2 a,       d->phi^2 d,       c->j c.
```

Its real linear trace is consequently

```text
tr_R(rho(A))=phi^-2+phi^2+j+bar(j)=2+phi.
```

This is not an integer. If a full rank-four lattice in this real vector
space were preserved by rho(A), a lattice basis would give an integer
four-by-four matrix for rho(A), whose trace must be an integer. The
contradiction excludes such an invariant rank-four lattice. Even an
inclusion rho(A)Lambda subset Lambda would suffice for this argument.

There is no contradiction with the preserved rank-eight module
Herm_2(O). Its two complex places together have real dimension eight;
the two four-dimensional traces are 2+phi and 2+(1-phi), with sum five.
The principal image of the integral module alone is not discrete in its
four-dimensional real target. Already Z+Z phi on a diagonal contains
arbitrarily small nonzero elements by rational approximation to the
irrational number phi.

The two-place trace cost N is coercive on the full integral module. It
is not invariant under the principal Lorentz-type transport. For example
H=diag(1,0) has N(H)=4, whereas rho(A)H=diag(phi^-2,0) has
N(rho(A)H)=Tr(phi^-4)=14. The bank compensates this chosen arithmetic
cost change. No native or measured energy, physical second-place
interpretation, rank-four lattice, or spacetime metric follows from that
bookkeeping.

## 11. Audit scope and protocol checks

The preregistered finite counts are exact cardinalities of the declared
test inventories:

```text
Hermitian rows: 3^8=6561,
transport evaluations: 6*6561=39366,
complete-step rows: 3*3*6*2*10*4=4320,
ready experiments: 2*4=8,
K1 rows: 10*25=250.
```

No test window here is claimed to be an invariant complete state carrier.
The universal statements rely on the proofs above; the finite audits
check the separately implemented arithmetic and explicit fixtures. The
digests and successful stdout are not predicted by copying another
implementation and are not supplied by this proof.

The conditional apparatus has a complete update, an internal program
phase, reciprocal source/link controls, nontrivial recorded loop action,
occupied readout, a positive account and a proved inverse. Its additional
definitions do not supply original-U admission, a matter or clock law,
general local gravitational dynamics, a soldering or connection law,
Einstein constraints, continuum behavior or physical predictions. The
K1 and lattice boundaries explicitly limit the most direct attempted
bridges. No Canon status or cross-layer gate changes through this proof.
