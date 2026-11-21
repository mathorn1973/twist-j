# Neutral stock orientation and a translated alphabet obstruction

NON-CANONICAL / L1 / analytical candidate for T. The fresh probe's finite
audit is pending. These exact arguments use no orbit count or shortest-word
report as a premise. No scientific program was executed or imported while
writing them. They establish neither a Canon promotion nor a physical
charge, energy unit or action normalization.

## 1. Integral contact and a reversible closed alphabet

Let O=Z[j], Phi_5(j)=0, p=j^2, u=1-j, B=1-p and J=1+p. Write

    H(x)=x conjugate(x),       Q(x)=Tr(H(x))/2.

The integral contact C fixes (x,y) if x-y is not in 2O. Otherwise

    C(x,y)=((x+y+p(x-y))/2,(x+y-p(x-y))/2).

It conserves the pair sum, sum H and sum Q, preserves each labeled
residue modulo u, and satisfies C^5=I. Its inverse is C^4.
For e_a=j^a, with subscripts modulo five, put

    N={0} union {e_a-e_b:a!=b},       |N|=21,
    R={e_a+e_b:a,b in Z/5Z},         |R|=15.

N consists of neutral values with Q=0 or 5. R consists of residue-two
values, with Q(2e_a)=8 and Q(e_a+e_b)=3 for a!=b. The five-root relation
has coefficient vector (1,1,1,1,1); comparison of equal listed values has
coefficient sum zero, so it creates no additional identifications.

For nonrepeated unordered pairs, the sums e_a+e_b modulo 2O are distinct
and nonzero. Indeed a relation between two such pairs has even support
size at most four, whereas the only nonzero relation of degree at most
four over F2 is Phi_5, with five nonzero coefficients. Doubled pairs have
zero parity and are handled separately.

Thus an admitted unequal neutral pair is necessarily opposite and obeys
C(d,-d)=(pd,-pd). Equal pairs are fixed. The complete nontrivial
neutral/charged cases, with the neutral slot written first, are

    C(0,2e_a)=(e_a-e_(a+2),e_a+e_(a+2)),
    C(e_a-e_b,e_a+e_b)=(e_a-e_(b+2),e_a+e_(b+2)).

Exchange a,b for the other neutral orientation. These outputs lie in
N x R, including the case of a zero neutral output. All other pairs
refuse. Reversing the slot order reverses the output because C commutes
with pair exchange.

It follows that configurations with exactly one R slot and every other
slot in N form a closed alphabet under every contact, every inverse and
whole-slot permutations. Its complement cannot enter it: an alleged
entry could be reversed by allowed contacts. This inverse closure is
essential to the obstruction below.

## 2. Translation commutes with the complete gated law

For any fixed w in O,

    C(x+w,y+w)=C(x,y)+(w,w).

The difference, and hence the parity decision, is unchanged; on admission
the pair center translates by w. Therefore subtracting the same u from
every slot conjugates every contact word to the identical word. The
statement includes refused contacts and inverse contacts. Whole-slot
permutations also commute with this common translation.

For t=+1 or -1 consider a stock S in the six-slot preparation

    I_t(S)=(tB,-tB,u,u,S,2).

After subtracting u, its first two values are tB-u and -tB-u. One is a
short root difference and the other has Q=15:

    B-u=j-j^2,       -B-u=-(u+B),       Q(u+B)=15.

Thus the translated initial configuration is outside the closed alphabet,
regardless of the stock. The translated required first four outputs are

    (tB,-tB,-u,-u),

all in N. A no-go follows whenever the required translated helper
endpoints complete this configuration to the closed alphabet.

## 3. Stock 2u: even unrestricted helper endpoints cannot load

Take S=2u. The input sum is 4u+2 and its total Q is 48. At a putative
first-four target (u+tB,u-tB,0,0), the main-slot sum and Hermitian account
are the same as those of the initial first four slots. The remaining two
helpers h5,h6 must therefore satisfy

    h5+h6=2u+2,
    H(h5)+H(h6)=4H(u)+4.

Their labeled residues are respectively zero and two. Put c=1+u=2-j
and write h5=c-z,h6=c+z, with z=c-h5 in O. Since

    H(c)=1+2H(u),
    H(c-z)+H(c+z)=2H(c)+2H(z),

conservation forces H(z)=1 and hence Q(z)=2.

For completeness, the integral Q=2 values are exactly +/-j^r. Represent
z by five integers a0,...,a4, choosing a4=0. Then

    2Q(z)=sum_(i<j)(a_i-a_j)^2=4.

If the coefficient range is at least two, the extreme pair contributes
at least four and each of the other three coefficients contributes at
least two through its pairs with the extremes, a total at least ten.
The range is therefore one. With m coefficients at the higher value the
sum is m(5-m), equal to four only for m=1 or 4. Subtracting a common
coefficient leaves one signed fifth root of unity.

Now c is one modulo u and h5 is zero, so z is one modulo u. This selects
the positive roots. The complete helper endpoint list is consequently

    (h5,h6)=(2-j-p^k,2-j+p^k),       k=0,...,4.

Exact restoration to (2u,2) is k=3, because p^3=j. No restoration has
been presumed in deriving the list.

Subtracting u makes each eligible helper pair (1-p^k,1+p^k), in N x R.
Every possible target is therefore inside the translated closed alphabet,
while the initial state is outside. Inverse closure proves that no word
can load either odd input, even with unrestricted final helpers. No orbit
size, search depth or computational non-finding is needed. If whole-slot
permutations are additionally supplied, the two helper residues may
exchange places, but the same global alphabet obstruction remains.

This is not a prohibition on producing a Q=15 value. In fact

    C^3(2u,2)=(2-j-j^2,2-j+j^2)=(u+B,2-j+j^2).

Its output accounts are 15 and 13, preserving 20+8. The failure concerns
the complete target and its conserved resources, not an isolated output.

## 4. The general exact-restoration obstruction

Suppose every neutral helper Y is required to return exactly and obeys
Y-u in N, while the sole charged helper Z returns exactly and obeys
Z-u in R. The required translated target then has one R slot and all
other slots in N. Its translated odd input still has a Q=15 source slot.
No contact word can perform this catalytic loading.

In particular, with the restored charged helper 2, every restored stock
S in u+N is excluded. Any finite number of further restored blanks or
stocks in u+N is also excluded: a blank translates to -u in N. This
statement concerns exact helper restoration. It does not assert that
arbitrary nonrestored extra helpers must end in the translated alphabet.
The unrestricted-helper conclusion of section 3 used its separate,
six-slot endpoint classification.

The same catalytic argument applies to the A-family A=j-j^3=jB:
Tr(A conjugate(u))=-5, so one of A-u,-A-u has Q=15, while the translated
required values +/-A remain in N.

## 5. Equal trace account does not fix the stock orientation

The 21 stocks in u+N have this exact account distribution:

| Q(stock) | 0 | 5 | 10 | 15 | 20 |
|---|---:|---:|---:|---:|---:|
| Number | 1 | 7 | 6 | 6 | 1 |

For S=u+e_a-e_b with a!=b,

    Q(S)=10+5(delta_(a,0)-delta_(a,1)-delta_(b,0)+delta_(b,1)).

This follows from Tr(u conjugate(e_a))=5delta_(a,0)-5delta_(a,1).
The ordered pairs give respectively one, six, six, six and one entries
at accounts 0,5,10,15,20; the remaining stock S=u contributes the seventh
account-five entry. The unique account-20 stock in this excluded family
is 2u.

For comparison, the complete neutral ball {S in uO:Q(S)<=20} has 171
members, with shell counts 1,20,30,60,60 at Q=0,5,10,15,20. Every neutral
field value has a unique zero-sum integer five-coefficient representative:
its initial coefficient sum is divisible by five, so subtract that sum
divided by five from every coefficient. In this representative,

    Q(S)=(5/2) sum a_i^2,       sum a_i=0.

The bound Q<=20 gives sum a_i^2<=8 and each a_i in [-2,2]. The complete
patterns are zero; (1,-1,0,0,0); (1,1,-1,-1,0); the two signs of
(2,-1,-1,0,0); and, at account20, (2,-2,0,0,0) together with the two signs
of (2,1,-1,-1,-1). Distinct permutations give respectively 1,20,30,60,
and 20+20+20 members. This proves the finite ball count without an orbit
search. The reported 142-stock sample is not treated as a complete survey
of this ball; its selection rule and omitted members would need to be
specified before making that comparison. The new finite audit uses the
explicit 171-member definition above.

Now define

    A=j-j^3,       D=1-j^3,       X=1+j-2j^3=u+2A.

Although Q(X)=15 and Q(2D)=Q(2u)=20,

    X-u=2A has Q=20,
    2D-u=X has Q=15.

Neither translated value belongs to N. These stocks escape the stated
translated-alphabet obstruction. Escaping a necessary obstruction is not
a reachability proof, a catalytic construction or a common-word result.

## 6. A positive local clearing operation

There is a concrete orientation-dependent mechanism for X:

    J A=-u,       u+A=D,       C(u,X)=(2D,0).

The pair admits because X-u=2A. Its center is u+A and its half-difference
is -A; the second output is u+JA=0 and the first equals its conserved
sum u+X=2D. The accounts are 5+15=20+0.

More generally J is an integral unit, with J^(-1)=-j-j^2. For a fixed
first input w, the unique second input on the admitted branch that makes
the second output zero is

    X_w=-(1-p)J^(-1)w.

Indeed that output is [(1-p)w+J X_w]/2. The candidate always admits,
since w-X_w=2J^(-1)w, and

    C(w,X_w)=(2pJ^(-1)w,0).

Uniqueness refers to admitted clearing. An already-zero second slot
could also remain zero under refusal and is not such a clearing event.

This local conversion consumes a supplied u reference. It does not make
the complete six-slot X preparation equivalent to the preparation with
stock 2D and two untouched u references. Their odd-input total accounts
are respectively 43 and 48. A complete loader must account for the blank,
the consumed reference, the remaining stock and its exact endpoint.

## 7. Scope of a common-word argument

For restored helpers the five-state Gram matrices already agree between
the initial and desired families: their field-valued entries are

    2ts H(B)+2H(u)+H(S)+4.

Thus polarization of that ensemble supplies no further obstruction. A
common word with the same admission history on all five inputs is still
excluded: the two variable slots remain +/-p^r tB with zero intercept,
because a uniformly admitted contact with a fixed helper would require
p^r B in 2O. Their reference bias cannot be loaded on a uniform history.

One must not extend that argument by treating different branch histories
as one unitary matrix. For example C refuses (1,0) but admits (2,0).
Their squared Q-distance changes from 2 to 7. The full gated map is
reversible and account-preserving, but is not a global linear isometry
between arbitrary different input states.

The results here concern specified integral encodings, local moves and
preparations. Arithmetic neutrality is a residue condition; it is not
identified with physical electric charge. Neither stock orientation nor
a clearing identity selects a physical energy reading, action quantum,
electron sector or electromagnetic coupling.
