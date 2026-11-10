# A partner-funded relative J contact

NON-CANONICAL / L1. The complete rule and its mathematical reading are
candidate-D constructions. Statements proved below are candidate-T at the
explicit scopes given here. Finite audits do not prove physical realization.

## 1. Inputs and attribution

Use the ring O=Z[j], 1+j+j^2+j^3+j^4=0, conjugation j->j^4,
J=1+j^2, Jinv=-j-j^2, rho=j^2 and phi=-j^2-j^3. Direct multiplication gives
J*Jinv=1, phi^2=phi+1 and

    t=J*conjugate(J)=2-phi,  t^-1=1+phi,  t+t^-1=3.

The full Hermitian account and its positive half trace are inherited from
RELATIVE-CONTACT-INTEGRAL-LAW in the pinned public Canon. The original law
rotates relative differences by rho; its unit has h(rho)=1. The new relative
J step is a different operation and is not silently substituted into that
conservation theorem.

For a scalar z with canonical coefficients z0..z3, put

    h(z)=z*conjugate(z),
    q(z)=Tr_K/Q(h(z))/2
        =(5 sum_i zi^2-(sum_i zi)^2)/2.

The numerator is even and q(z)>=sum_i zi^2/2. Thus q is a nonnegative integer
with unique zero and finite bounded sublevel sets. The account E=sum q is
not identified here with measured energy.

FUNDED-CONTACT-INVOLUTION already supplies a different rational-store and
retained-direction construction. The present contribution is the exact
full-H balance surface for two reciprocal relative J steps on O^4 and its
completion with no extra register. Existing BOOST-READING-SPLIT and
BOOST-COUNT-LADDER already give algebraic hyperbolic identities and a declared
count reading. The squared-norm calculation in section 7 specializes that
algebra to this carrier; it is not a new derivation of relativity.

## 2. The balance surface is necessary and sufficient

Take four slots (x,y,u,v). Both parity gates are required:

    x-y in 2O,  u-v in 2O.

Then the centers c=(x+y)/2,e=(u+v)/2 and half-differences
 d=(x-y)/2,f=(u-v)/2 all belong to O. Define the reciprocal proposal Bplus
by fixing c,e and sending (d,f) to (Jd,Jinv f). Its complete inverse Bminus
uses (Jinv d,Jf). Both preserve the two parity-admitted domains.

The total Hermitian account is

    H=2h(c)+2h(e)+2h(d)+2h(f).

Consequently

    H(Bplus z)-H(z)
      =2[(t-1)h(d)+(t^-1-1)h(f)]
      =2(t-1)[h(d)-t^-1 h(f)].

The real field is a domain and t!=1. Therefore

    H(Bplus z)=H(z) iff h(f)=t h(d).                 (Dplus)
    H(Bminus z)=H(z) iff h(d)=t h(f).                (Dminus)

These are classifications for these specified reciprocal proposals, not
for all possible funding maps. Merely using opposite J directions is
insufficient: with (x,y,u,v)=(2,0,0,0), Bplus changes E from 8 to 10.

The identity h(z)=0 iff z=0 shows that either balance equality with one
zero half-difference has both half-differences zero. If both equalities
hold, h(d)=t^2 h(d); since t^2!=1, both half-differences are zero. Thus the
nonzero balance surfaces are disjoint.

## 3. Total law, exact inverse and all refusals

Define T4 on all O^4:

- if either parity gate fails, fix the whole state;
- if d=f=0, fix the whole state;
- on nonzero Dplus, apply Bplus;
- on nonzero Dminus, apply Bminus;
- otherwise fix the whole state.

On Dplus, the new half-differences have

    h(d')=t h(d)=h(f),  h(f')=t^-1 h(f)=h(d).

Thus the image is in Dminus, and Bminus restores the original state.
Conversely Bminus maps Dminus to Dplus and Bplus restores it. Refusals
and the zero case remain in their original fixed domains. Therefore

    T4^2=identity on every state of O^4.

All divisions are exact on the only branches which use them. The law is
bijective, preserves both pair sums separately, preserves H before taking
any trace and therefore preserves E. Each active relative difference is
multiplied by J or Jinv; its field norm and 2-adic valuation are unchanged.
This does not assert that differences along other pairings are invariant.

The absence of a separate direction bit is justified by the disjointness
of the two account surfaces. The direction is read from current state,
not from a hidden record. This is not the defective one-sided completion:
applying Bplus on Dplus and identity elsewhere maps z and Bplus z to the
same state. The second branch is essential for this rule.

More precisely, the relative Hermitian accounts are exchanged. The target
pair's q increment is 2(q(f)-q(d)) and the payer's is its negative; it need
not be positive for every admitted state. Forward means J on the first
relative coordinate, not an unconditional energy increase.

## 4. Explicit common-payer witnesses and a scoped sharp budget

Let a=+1 or -1 and R=rho. The payer preparation is independent of a.

### Blank target, centered payer

    (2a,0,RJ,-RJ)
       -> (a(1+J),a(1-J),R,-R).

Here c=a,d=a,e=0,f=RJ and h(f)=t h(d). Initial accounts of target and
payer are 8 and 6; final accounts are 10 and 4. The full H is 4+2t,
E=14, and the complete sum is 2a. There are no discarded coordinates.
The initially blank target has trace Tr(a(1-J))=a after one invocation.
A second invocation restores all four slots, so this is not retained
history or an independent new input.

Within this exact reciprocal/full-H model, any payer for the target
(2a,0) must have h(f)=t. Therefore q(f)=3 and its whole pair account is
2q(e)+6>=6, attained by the displayed e=0 payer. This is the sharp initial
payer account at this scope. It is not a minimum over other contact laws,
new scalar batteries or additional carriers. The amount transferred is 2,
not 6.

### Two other full-state checks

    (2a,0,2RJ,0)
       -> (a(1+J),a(1-J),R(J+1),R(J-1)),

with accounts (8,12)->(10,10), total 20; and

    (a,-a,RJ,-RJ) -> (aJ,-aJ,R,-R),

with accounts (4,6)->(6,4), total 10.

The relative source signs are not prewritten in the common payer.
Conversely, the payer's nonzero ready state is genuinely supplied stock.
Its arithmetic preparation is not derived here.

## 5. What the new primitive does not compile

In O/(1-j)=F5 the original rho contact fixes each labelled residue, and
whole-slot permutations preserve their histogram. For a=1 the centered-
payer blank-target example has input residues (2,0,2,3) and output
residues (3,4,1,4). The histograms differ. Hence no word in that original
alphabet realizes this complete four-slot transition. Adding auxiliaries
which all return exactly cannot repair the histogram mismatch, since their
identical initial/final histograms cancel.

The construction is therefore an explicit NEW four-slot primitive, not a
proof that the old rho-only machine already contains it. Its marked grouping
of two pairs and its exact balance guard are model ingredients. A four-slot
block can be placed on four adjacent sites, but a continuing whole-network
schedule, or a native-U compiler, requires a separate construction.

## 6. Finite acceleration words and the unavoidable stock cost

Fix K>=1 before choosing the source sign. Prepare target (a,-a) and K
payer pairs

    (rho^i J^i, -rho^i J^i), i=1,...,K.

Apply T4 to the target and payer i in increasing i order, keeping every
other slot unchanged. Before step i, target half-difference is a J^(i-1)
and payer half-difference is rho^i J^i. Their Hermitian accounts satisfy
Dplus. The target becomes a J^i and payer i becomes rho^i J^(i-1).
This proves every forward step and the exact complete final state by
induction. Applying the same involutions in reverse i order restores
all coordinates.

There are 2+2K slots. Since q(J^m)=L_(2m), the initial account is

    E=4+2 sum_(i=1)^K L_(2i)=2+2 L_(2K+1).

The equality follows by telescoping L_(2i)=L_(2i+1)-L_(2i-1).
The payer stock is finite for each fixed K and grows with K. Its preparation
and the successive-payer word remain supplied; this is not an autonomous
reservoir-selection law.

A finite reservoir with conserved nonnegative proper E cannot support the
unchanged target trajectory (a J^k,-a J^k) for every k, since the target
account 2 L_(2k) is unbounded. This excludes perpetual exact acceleration
with finite stock at this scope, not conservative propagation or exchange.
An isolated T4 block is only a two-cycle. No positive-entropy or all-order
independence conclusion follows from its existence.

## 7. Exact hyperbolic reading and its physical boundary

For every scalar z, its conjugation-invariant h has unique form

    h(z)=A+B phi, A,B integers.

The full field norm is N(z)=A^2+AB-B^2. With T=2A+B=q(z) and formal
X=sqrt(5)B one has

    T^2-X^2=4 N(z).

Multiplication by J induces h->(2-phi)h, equivalently

    (A,B)->(2A-B,B-A),
    (T,B)->((3T-5B)/2,(-T+3B)/2).

The apparent halves are exact on T=B mod 2. On (T,X) the matrix is

    [[3/2,-sqrt(5)/2],[-sqrt(5)/2,3/2]],

which has determinant 1 and preserves T^2-X^2. Its rapidity magnitude is
2 log(phi), since cosh(2 log(phi))=3/2. Starting at z=1 gives
T=L_(2k), B=-F_(2k), and q(J^k)=phi^(2k)+phi^(-2k).
This algebraic 1+1 reading is exact. In the funded rule the two relative
h values, and hence their (T,X) values, are exchanged. This is stronger and
more specific than saying merely that opposite boosts cancel.

The reading is quadratic in the four raw coefficients. N(z) is quartic,
and is proportional to the squared invariant of this constructed reading,
not automatically to physical mass. Identifying T and X with physical
energy and momentum, assigning units and physical proper time, showing
Lorentz covariance of the full interacting system and deriving free fall
are separate obligations. Equal rapidity increments per abstract step do
not by themselves give constant proper acceleration. Period-15 parity
return is not a radiation law, and a Lorentz algebraic identity is not an
equivalence-principle derivation.

The earlier statement about no alternative account must keep its scope:
an unbounded orbit cannot preserve a proper account with finite bounded
sublevels. Additive conserved quantities such as the pair sum still exist.
Likewise conservation alone does not forbid support motion into a formerly
zero cell. This probe neither revives a fired spatial-horizon claim nor
interprets a zero cell as a physical empty vacuum.
