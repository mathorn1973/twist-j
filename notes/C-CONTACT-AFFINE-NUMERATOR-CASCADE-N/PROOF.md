# Direct contact affine synthesis and bounded division recording

Status: NON-CANONICAL / L1. Candidate C-CONTACT-AFFINE-NUMERATOR-CASCADE-N.
The symbolic results below are candidate-T proofs. A separately recorded
finite audit has only its stated candidate-C scope. No runtime output is
assumed or asserted in this proof.

The gain q and the source encoding E_q are supplied premises. The contact
word does not select q=3, derive Collatz arithmetic from J, prepare E_q from
one raw integer source, renew a source, or implement the original native U.
All source-dependent leftovers remain part of the complete state.

## 1. Contact, inverse and accounts

Work in O=Z[j], where 1+j+j^2+j^3+j^4=0. Put

    rho=j^2, J=1+rho, u=1-rho.

The total contact on labelled slots a,b is the identity when a-b is not
in 2O. Otherwise a=s+t and b=s-t with s,t in O, and

    C(a,b)=(s+rho*t,s-rho*t)
          =((J*a+u*b)/2,(u*a+J*b)/2).

An enabled contact stays enabled, and multiplies the relative coordinate
by rho. Since rho has order five, C^5 is the identity on the complete
pair carrier and C^{-1}=C^4. A refused pair is fixed. Hence every word used
below is a global permutation, including outside the positive arithmetic
contract.

For z=z0+z1*j+z2*j^2+z3*j^3, define

    Q(z)=(5*sum_i zi^2-(sum_i zi)^2)/2.

This equals Tr(z*bar(z))/2. It is integral and positive definite:
(sum_i zi)^2<=4*sum_i zi^2, and its numerator is even. Since
rho*bar(rho)=1, an enabled contact preserves Q(a)+Q(b). It also preserves
a+b. Both conclusions are immediate for a refused contact.

There is a ring map

    epsilon: O -> F5, epsilon(z)=sum_i zi mod 5,

given by j->1. A contact changes its first slot by (rho-1)*t and its
second by the opposite value. Therefore each fixed labelled slot preserves
its own epsilon residue. This is stronger than conservation of the total
residue, and remains true along the whole contact word.

We will use

    J+u=2, J-u=2rho, J^{-1}=-rho-rho^3.

The last identity follows by multiplication and
1+rho+rho^2+rho^3+rho^4=0. In particular J is an integral unit. Modulo two,
u equals J, so u is invertible modulo two as well. Consequently, for every
z in O and every k>=0,

    J*z in 2^k O iff z in 2^k O,
    u*z in 2^k O iff z in 2^k O.

For u, the k=1 assertion follows from invertibility modulo two, and higher
k follow by induction after dividing z by two. We do not assert that u is
a unit of O; its algebraic norm is five.

## 2. A supplied source encoding with a common reference

Fix a positive integer q and admit n>0. The declared source is

    E_q(n)=(2(q-1)u*n, 2((q-1)u+2)*n, 2J).

Only the first two slots depend on n. Each is a fixed linear multiple of
n; neither includes the affine offset one, a precomputed odd part, or a
valuation. The third slot is the same reference 2J for all n and q. All
following cascade slots are common zeros.

This loading interface is an explicit additional resource. The proof does
not synthesize its two correlated source values from one raw slot n, and
does not treat their preparation as free. Changing q changes the specified
linear source encoding. This supplies the gain, rather than proving a
selection principle for it.

The total source sum is

    S_q(n)=4[q-(q-1)rho]*n+2J.

For the account, Q(u)=5 and Q(J)=3. The first source slot contributes
20(q-1)^2*n^2. Writing ((q-1)u+2)=(q+1)-(q-1)rho gives account
(20q^2+12)*n^2 for the second slot. Thus

    Q(E_q(n))=[40q(q-1)+32]*n^2+12.

For q=3 this is 272n^2+12. Zero cascade slots add nothing. These are
complete accounts of the declared source, with no uncounted changing bank.
They vary quadratically with the input n.

## 3. Two contacts produce the affine numerator

Write (a,b,c)=E_q(n). Apply C(0,1) followed by C(0,2).

The first difference is a-b=-4n, so the first contact is enabled for
every admitted n. Its outputs are

    a1=2q*u*n,
    b1=2[q-(q-2)rho]*n.

Indeed

    (J*a+u*b)/2
      =u[(q-1)J+(q-1)u+2]*n
      =2q*u*n,

and the other output follows from the same formula and J+u=2.

Both a1 and the common reference c=2J are even in O, so the second
contact is also always enabled. It gives

    a2=u*J*(qn+1),
    c2=q*u^2*n+J^2.

This follows directly from

    (J*(2q*u*n)+u*(2J))/2=u*J*(qn+1),
    (u*(2q*u*n)+J*(2J))/2=q*u^2*n+J^2.

The second source slot stays b1. Thus the complete state after the prefix is

    (u*J*(qn+1),
     2[q-(q-2)rho]*n,
     q*u^2*n+J^2,
     0,...,0).

The affine numerator is now actually present, in the fixed residue-neutral
code uJ. It was produced by two admitted contacts from separate n-dependent
source slots and the common reference. This is a direct algebraic synthesis,
not a finite truth-table compilation. It remains conditional on E_q and q.

The factorization also exposes where the gain is supplied: the single
contact C(2q*u*n,2J) already creates uJ(qn+1). The first contact of our
declared source prepares that linear active input. It is therefore not a
selection of q by the word. The same word serves every supplied q, while
changing q changes the chosen source encoding. No minimal-prefix or
minimal-source claim is made.

## 4. The division cascade is a fixed word

For a nonzero even active value x and a fresh zero target,

    C(x,0)=(J*x/2,u*x/2).

For an odd active value the same contact is refused. Because J preserves
every power-of-two divisibility class, each accepted cascade contact reduces
the active divisibility by exactly one and multiplies its remaining value
by the integral unit J. Its new target is nonzero: O is an integral domain
and u and x are nonzero.

Set

    x=qn+1, v=v2(x), m=x/2^v.

Here x>0, v>=0 and m is a positive odd integer. Section 1 shows that the
prefix active value uJx has exactly the same two-adic divisibility v.

For any predeclared D>=0, append D+1 zero slots and apply, in order,

    C(0,3), C(0,4), ..., C(0,D+3).

If v<=D, exactly the first v contacts are accepted. By induction, after
s<=v accepted cascade contacts,

    active_s=u*J^(s+1)*x/2^s,
    slot(2+s)=u^2*J^s*x/2^s.

After the v-th acceptance the active slot is odd, so all remaining contacts
are refused. Its final value and all targets are therefore exactly

    slot0=u*J^(v+1)*m;
    slot(2+s)=u^2*J^s*2^(v-s)*m, 1<=s<=v;
    slot(2+s)=0, v<s<=D+1.

The first v stored targets are all nonzero. This includes v=0, in which
case every cascade contact is refused and every target remains zero. Slots
1 and 2 retain b1 and c2 throughout the cascade.

Together with the two prefix contacts, the complete word has D+3 contacts
and uses D+4 core slots. The frozen contract takes D=12, giving 15 contacts
on 16 slots. Edge order and word length are independent of n, q and v;
there is no runtime selection of an edge, table row, or stopping time.

## 5. Current-state reader and exact inverses

The reader examines only the current active slot and the current D+1 cascade
targets. If all targets are nonzero it returns DEPTH_LIMIT. Otherwise let
v be their nonzero prefix length and require all following targets to be
zero. On the positive family of Section 4 this is precisely v2(qn+1).

The reader computes, in the integral ring,

    r=J^(-(v+1))*slot0=u*m.

Since u=1-j^2, its j-basis tuple is (m,0,-m,0). Checking that tuple shape
and reading the constant coefficient gives m. This uses neither division
by the nonunit u nor access to n, q-dependent source leftovers, a hidden
history, a free counter, or a target truth table. The depth is physically
encoded by the present nonzero target prefix.

The unit normalization is a mathematical reading. It has not been
implemented as a physical contact operation in this construction. The
actual active slot remains uJ^(v+1)m. Arithmetic integrality of J^{-1}
does not assert that multiplication by it is a Q-preserving physical gate.

For supplied q, the arithmetic output pair has inverse

    n=(2^v*m-1)/q.

The divisibility and positivity hold on every admitted source by construction.
Thus (m,v) identifies the initial n within this source family. Separately,
the complete-state inverse reverses the entire chronological edge list and
replaces each contact by four repetitions of the same contact. It restores
every source and cascade slot on the whole carrier, even outside the
arithmetic contract. These two inverse statements have different scopes:
one recovers arithmetic input from a readout pair, the other reverses the
complete physical construction including every occupied leftover.

## 6. Infinite conditional family and the frozen finite audits

The positive theorem allows every n>0 with v2(qn+1)<=D, without an upper
bound on n. Equivalently qn+1 is not divisible by 2^(D+1). This is a fixed
congruence condition. For even q, v=0 for every n. For odd q it excludes
the one deep-divisibility residue class modulo 2^(D+1). All admitted
inputs use the identical word and common reference, with their explicitly
input-dependent source accounts.

The corpus in PREREG.md is a finite audit of these symbolic formulas, not
the definition of the theorem's infinite conditional family. Its depth
admission can also be checked without a runtime enumeration. For q=3 and
odd n<=4095, x<=12286<2^14. Depth 13 would require x=2^13 in this interval,
but this number is 2 modulo three, whereas 3n+1 is 1 modulo three. Thus
every such n has depth at most 12. Every depth 1..12 occurs: for even v
choose n=(2^v-1)/3, and for odd v choose n=(5*2^v-1)/3. These are positive
odd integers, at most 1365 and 3413 respectively in the stated range, and
their odd parts are exactly 1 and 5. For q=1..9 and odd n<=127,
qn+1<=1144<2^11, so all depths are less than 11 and fit D=12.

Any optional occupied archive slots are disjoint from all edges. Therefore
every old value stays exactly equal in its labelled slot, and its sum and Q
are added unchanged to the complete account. This holds for arbitrary O
values, beyond the finite occupied-archive corpus. It does not assert that
these old values or the new source leftovers have been renewed.

For the fixed outside-depth witness q=3,n=5461, x=2^14. All thirteen cascade
contacts are accepted. The thirteen targets are nonzero and the final active
slot is 2uJ^14, which is even. The prescribed reader therefore returns
DEPTH_LIMIT. Sum, Q, labelled residues and the complete-state inverse still
hold. This saturation is an expected boundary witness, not an arithmetic
success within v<=12. More generally, all v>=D+1 saturate the current
nonzero-prefix test and are outside this positive contract.

## 7. What has been paid for and what has not been renewed

The prefix and cascade conserve the total sum, Q and all labelled residues
at every primitive boundary. They do not erase their source/reference
leftovers. In particular the final slots 1 and 2 still equal

    2[q-(q-2)rho]*n,
    q*u^2*n+J^2.

These n-dependent values are included in the apparatus. Calling their
restoration to a common ready state would contradict the actual formulas.
The output is not E_q(m). Appending an untouched old archive provides
retention, not a ready source for another affine step.

There is an exact residue obstruction to one proposed reset in this same
encoding. Initially slot 1 has epsilon=4n modulo five, and its final b1
has the same residue. No further contact-only word can set this labelled
slot to one common value on a family containing different n modulo five.
Likewise replacing its contents by the corresponding slot of E_q(m)
requires n=m modulo five. For q=3,n=3 the result m=5 fails this necessary
condition. This excludes that particular fixed-slot renewal route, not all
future encodings, slot-permutation interfaces or externally supplied sources.

There is also a separate necessary account bound for reloading this exact
source family. For q=3 its ready account is 272n^2+12. If the complete
initial system has that source and an additional nonnegative account B,
and the final system is required to contain E_3(m) plus any other slots
of nonnegative account, conservation requires

    272*(m^2-n^2)<=B.

Any old archive required to remain unchanged contributes the same account
on both sides and cancels from this inequality. Extra retained new records
can only increase the final requirement. For n congruent to 3 modulo four,
m=(3n+1)/2, so this necessary additional funding is

    272*(m^2-n^2)=68*(5n^2+6n+1).

It is unbounded on that input family. With B=0, the single transition
3->5 already requires an unavailable increase 4352. Thus a direct recurrent
connection that demands a fresh E_3(m) after every output has no account
justification. This bound does not exclude a different carrier, a supplied
larger source, or an explicitly funded finite input family.

The account also makes the cost explicit. Starting with one raw scalar n
and a common finite auxiliary account E, conservation and positivity would
require 2(qn+1)^2<=2n^2+E to leave the raw numerator in an output slot.
For fixed q>=2 the difference is unbounded with n. For q=3 it is
16n^2+12n+2. The present construction supplies a larger n-dependent
two-port source and changes to a residue-neutral output code; it does not
evade the raw-source obstruction without paying these declared costs.

Odd-scaling symmetry is also consistent with this result. Contacts commute
with odd integer scaling of the complete state. Without a non-scaled
reference, their enabled/refused pattern on a purely scaled source family
would be input-independent. Here the common reference 2J is not scaled
with n and supplies the affine offset. Source loading and that reference
are premises, not an emergent preparation law.

A fixed finite affine-branch word cannot cover all unbounded raw-scalar
Collatz depths under one fixed affine scalar reading: there are only finitely
many affine itineraries, whereas the slopes 3/2^v are distinct for unbounded
v. The present theorem bounds v in advance, uses an explicit current-state
depth code, and applies a specified depth-dependent unit reading. It makes
no contrary claim about the unbounded-depth problem.

## 8. The exact connection and the remaining repeated-step obligation

For the supplied q=3 source family, two actual contacts now create the
encoded numerator 3n+1, and the same fixed contact word writes its bounded
division depth and an active encoded odd part. This closes the previously
missing numerator interface for E_3(n). No finite table of individual n
or individual Collatz answers appears in the word or reader.

What remains is a complete next-step interface: prepare E_3(m), or a
separately declared repeatable encoding, from the actual occupied output
while retaining old depth records, accounting for the n-dependent banks,
and respecting the proved residue and account boundaries. The code must
also say how deeper divisions are handled beyond the fixed D. No such
renewal, source loader, indefinitely growing archive, autonomous repeated
Collatz map, physical unit identification, occurrence law, global convergence
or Canon promotion is supplied by this one-pass construction.
