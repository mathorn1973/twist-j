# Four finite charts for the affine contact cascade

**Status: NON-CANONICAL / L1, candidate-T analytical construction.**

This note gives four predetermined contact words, indexed by a supplied
chart. It does not construct an autonomous chart selector or renew a
source from its occupied output. The gain, source loading and depth cap
remain declared premises. All identities below are analytical; no
verifier execution is used in their proofs.

## 1. Ring, native contacts and four code vectors

Work in O=Z[rho], where rho has order five and

    1+rho+rho^2+rho^3+rho^4=0.

Here rho=j^2, so this is the same ring Z[j]. The native contact C on two
labelled slots is the identity if their difference is not in 2O. If
a=s+t and b=s-t with s,t in O, it sends

    (a,b) -> (s+rho*t,s-rho*t).

An enabled pair stays enabled. Consequently, for d in {1,2,3,4}, the
power C^d means exactly d repetitions of this same native contact and
acts on an enabled pair as

    C^d(a,b)=((J_d*a+U_d*b)/2,(U_d*a+J_d*b)/2),
    J_d=1+rho^d, U_d=1-rho^d.

A refused pair remains fixed throughout those repetitions. Each C^d
is therefore a global permutation, not a new primitive gate. Its
inverse is C^(5-d).

Subscripts of U and J are taken modulo five in {1,2,3,4}. The key
identity is

    U_d*J_d=U_(2d).

Doubling cycles through all four nonzero residues modulo five. In
particular,

    J_d*J_(2d)*J_(4d)*J_(3d)=1.

This follows by telescoping the four U identities. Every J_d is an
integral unit. Also N(U_d)=5, so multiplication by U_d is invertible
modulo two. These facts imply, for every z in O and k>=0,

    U_d*z in 2^k O iff z in 2^k O,
    J_d*z in 2^k O iff z in 2^k O.

For the first assertion, invertibility modulo two gives the k=1 case,
and induction after exact division by two gives every k. The same
argument applies to J_d, which is already an integral unit.

For z=z0+z1*rho+z2*rho^2+z3*rho^3, put

    Q(z)=(5*sum_i zi^2-(sum_i zi)^2)/2=Tr(z*bar(z))/2.

This is a positive definite integer account. Native contacts preserve
Q(a)+Q(b), a+b, and each labelled slot's residue

    epsilon(z)=sum_i zi mod 5.

The first two invariances follow from the center/relative form and
rho*bar(rho)=1. For the residue, a contact changes one slot by
(rho-1)t and the other by its negative, both killed by epsilon.
The same invariances hold for every power C^d and every word below.

The four code vectors have rho-basis tuples

| d | U_d |
|---|---|
| 1 | (1,-1,0,0) |
| 2 | (1,0,-1,0) |
| 3 | (1,0,0,-1) |
| 4 | (2,1,1,1) |

All four satisfy

    Q(U_d)=5, Q(J_d)=3, Q(U_d^2)=15.

For example Tr(rho^e)=-1 whenever e is nonzero modulo five.
Expanding (1-rho^d)(1-rho^-d) gives Q(U_d)=5, and changing
both minus signs to plus signs gives Q(J_d)=3. Squaring
2-rho^d-rho^-d gives

    6-4(rho^d+rho^-d)+rho^(2d)+rho^(-2d),

whose half trace is 15. Thus the code vectors have equal account,
even though their individual Archimedean embedding moduli differ.

## 2. A source whose first port already has the output code

Fix a supplied positive integer gain q, a supplied chart d in
{1,2,3,4}, and a positive integer n. Define

    F_(q,d)(n)=(U_d*n, (4q-J_d)*n, 2J_d).

The second and third ports are additional supplied resources. In
particular, this definition does not prepare them from the first port.
All subsequent cascade ports start at zero.
It also does not convert the earlier E source's occupied output into
this new F preparation; F is a newly declared initial interface.

Apply C_(01)^d and then C_(02)^d. The first difference is

    U_d*n-(4q-J_d)*n=2(1-2q)*n,

so the first powered contact is enabled. Its outputs are

    a1=2q*U_d*n,
    b1=2(q*J_d-rho^d)*n.

The first identity follows from cancellation of the two J_d*U_d
terms in the contact formula. For the second, use

    U_d^2-J_d^2=-4rho^d.

Both a1 and the common reference 2J_d are even. The second powered
contact therefore gives

    a2=U_d*J_d*(qn+1)=U_(2d)*(qn+1),
    c2=q*U_d^2*n+J_d^2.

After this prefix the complete core is

    (U_(2d)*(qn+1), 2(q*J_d-rho^d)*n,
     q*U_d^2*n+J_d^2, 0,...,0).

Thus the affine numerator is created by actual contacts. The first
port now uses another member of the same four-element code family.
The other source ports still contain the old n.

The ready source's sum and complete account are

    S(F_(q,d)(n))=2(2q-rho^d)*n+2J_d,
    Q(F_(q,d)(n))=K_q*n^2+12,
    K_q=32q^2-12q+8.

Indeed Q((4q-J_d)n)=(32q^2-12q+3)n^2, which adds to
Q(U_d n)=5n^2; the reference contributes 4Q(J_d)=12. In
particular every q=3 ready chart has account

    260n^2+12.

## 3. A predetermined powered-contact cascade

Declare a depth cap D>=0, set

    x=qn+1, v=v2(x), m=x/2^v,

and append D+1 zero target ports. Put

    e_s=2^s*d mod 5 in {1,2,3,4},  1<=s<=D+1.

After the two-contact prefix, apply in order

    C_(0,3)^(e_1), C_(0,4)^(e_2), ...,
    C_(0,D+3)^(e_(D+1)).

The complete list of primitive contacts is fixed once d and D are
specified. None of its edges or exponents is selected from the
observed n, v, or m during execution.

For an active value U_e*y with y even and a zero target,

    C^e(U_e*y,0)=(U_(2e)*y/2, U_e^2*y/2).

Every such powered contact lowers the divisibility by exactly one.
It changes the chart by doubling e modulo five and writes a nonzero
record. It is still a single division, even though its native
implementation repeats C e times on the same occupied pair.

If v<=D, induction gives the exact final ports

    slot0=U_(d')*m,  d'=2^(v+1)*d mod 5;
    slot(2+s)=U_(e_s)^2*2^(v-s)*m,  1<=s<=v;
    slot(2+s)=0,  v<s<=D+1.

Slots 1 and 2 retain b1,c2 from the prefix. After the v-th accepted
powered contact, the active slot is odd in O. Every later contact
with a zero target is refused, so the unused suffix cannot alter
the actual output chart.

For D=12 these words use the same 16 core slots, with the following
primitive C counts:

| Initial d | Prefix count 2d | Cascade count | Total |
|---:|---:|---:|---:|
| 1 | 2 | 32 | 34 |
| 2 | 4 | 34 | 38 |
| 3 | 6 | 31 | 37 |
| 4 | 8 | 33 | 41 |

Each cascade consists of three complete four-exponent cycles of
sum ten and one additional first exponent. These are four
predetermined chart-indexed words, not one already constructed
autonomous selector among those words.

For v>=D+1 every target is nonzero. The depth reader must return
DEPTH_LIMIT. Native conservation and invertibility still hold on
those states, but the bounded arithmetic success contract does not.

### Exact Galois intertwining at macro boundaries

Let sigma_d be the ring automorphism rho -> rho^d. It preserves
the ideal 2O, so it preserves enabledness. On an enabled pair,
applying it to the center/relative form of C gives

    sigma_d(C(a,b))=C^d(sigma_d(a),sigma_d(b)).

The same identity holds on a refused pair, because both sides
are then fixed. More generally sigma_d transports C^e to
C^(de mod 5), with the nonzero exponent represented in {1,2,3,4}.

Let W_d be the whole chart-d word, grouped into its two powered
prefix contacts and its D+1 powered cascade contacts. Since
F_(q,d)(n)=sigma_d(F_(q,1)(n)) and sigma_d fixes the zero ports,
composition gives

    W_d(F_(q,d)(n),0,...,0)
      =sigma_d(W_1(F_(q,1)(n),0,...,0)).

This equality holds at every corresponding powered-contact
boundary, not only at the final output. It is an algebraic
intertwining between four native words on corresponding
source states. It does not supply a physical Galois gate or
an autonomous selector. The primitive word lengths differ,
as the preceding table explicitly records.

## 4. Reading the current output without unit normalization

The current archive's nonzero prefix gives v when at least one
zero target follows it. The current active tuple is exactly one
positive odd multiple m of a U_d tuple in the table of Section 1.
Those four shapes are disjoint for m>0, so they determine both m
and the current chart d'. Equivalently m is the positive gcd of
the active rho-basis coefficients, followed by a check of the
normalized tuple against that table.

This mathematical reader uses only the active port and present
cascade records. It does not multiply the active state by a
growing inverse unit, inspect the n-dependent source leftovers,
or receive an external old chart. On admitted outputs it can
also recover the arithmetic and chart inputs exactly:

    n=(2^v*m-1)/q,
    d=2^(-(v+1))*d' mod 5.

The inverse here is an arithmetic readout statement. Reversing
the complete primitive contact word gives a separate native
inverse on every slot of the whole carrier.

If d=2^r modulo five, its finite chart update is simply

    r'=r+v+1 mod 4.

The full unbounded v is still present in the archive. Reduction
modulo four is only the code orientation and cannot replace the
depth record in the arithmetic inverse.

## 5. Exact accounts of the active value and fresh records

Because every U_d has account five, the final active account is

    Q(slot0)=5m^2,

independent of d and v. Each accepted division writes a record
of account

    15*4^(v-s)*m^2.

Consequently all fresh depth records together have exact account

    R_new=15m^2*sum_(s=1)^v 4^(v-s)
         =5(4^v-1)m^2
         =5((qn+1)^2-m^2).

The formula includes v=0, where the sum is empty. It agrees with
conservation of the prefix active account 5(qn+1)^2 during the
cascade. Preserving a numerical readout does not make these
nonzero records free.

Sum conservation during the same cascade also gives its exact
fresh-record sum:

    sum_(s=1)^v slot(2+s)
      =U_(2d)*(qn+1)-U_(d')*m.

Thus both the account and the ring-valued sum of the retained
new records are fixed, rather than freely adjustable reset
resources.

For q=3 the initial source residues are

    (epsilon(U_d*n),epsilon((12-J_d)*n),epsilon(2J_d))
    =(0,0,4),

for every n and d. All cascade records have residue zero. Thus
the particular first-residue obstruction n=m modulo five of
the earlier E_3 source does not apply to this family. This does
not assert that all other invariants or reachability constraints
have disappeared.

## 6. What remains to renew

The current active output U_(d')*m already equals the first port
of F_(q,d')(m). A next ready source would still require the two
other ports

    (4q-J_(d'))*m,  2J_(d').

They are not the actual occupied b1,c2 above. This note supplies
no contact word that renews them while retaining the old and
new records. Also, reading d' does not by itself implement a
native controller that selects the next one of the four words.

A necessary resource bound is explicit. Suppose the complete
input consists of F_(3,d)(n), an additional account B, and old
archives that must be restored literally. Require the complete
output to contain F_(3,d')(m), all new depth records literally,
the same old archives, and other slots of nonnegative account.
Conservation then requires

    B >= 260(m^2-n^2)+5((3n+1)^2-m^2).

The old archives cancel exactly. For 3->5, the ready-source
increase is 260(25-9)=4160 and the fresh record account is
5(100-25)=375. Hence

    B >= 4535.

This is a necessary lower bound, not a proved attainable
minimum. Sum conservation, finer arithmetic constraints, the
literal occupied banks and actual contact reachability still
have to be satisfied. The construction removes the growing
unit reading and the earlier input-dependent first residue
from this declared chart family; it does not solve source
renewal, autonomous repetition, gain selection, unbounded
depth with a fixed finite bank, physical energy calibration,
occurrence, or Collatz convergence.
