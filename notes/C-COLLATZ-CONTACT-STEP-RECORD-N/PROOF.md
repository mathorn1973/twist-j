# Finite contact compilation of an odd Collatz step and its depth record

Status: NON-CANONICAL / L1. Candidate C-COLLATZ-CONTACT-STEP-RECORD-N.
The statements below are candidate-T mathematical proofs. Any finite runtime
evidence has only the separately recorded candidate-C scope. No execution
result is asserted in this file.

The construction implements a supplied finite table. It proves contact
programmability on the stated prepared family, not emergence of Collatz
arithmetic from J, derivation of the table, realization by the original native
U, a physical instrument, or a convergence theorem.

## 1. Integral contact and conserved accounts

Let O=Z[j], with 1+j+j^2+j^3+j^4=0, and put

    rho=j^2, u=1-rho, w=1+rho=J.

For a,b in O, define the total contact C by leaving the pair fixed when
a-b is not in 2O, and otherwise writing a=s+t, b=s-t and returning

    C(a,b)=(s+rho*t,s-rho*t).

The enabled condition remains true after an enabled contact. Its relative
coordinate is multiplied by rho, and rho has order five. Disabled pairs
remain disabled. Consequently C^5 is the identity on the complete pair
carrier and C^{-1}=C^4. Every finite word in contacts is therefore a global
permutation; this statement does not require a binary preparation.

For z=z0+z1*j+z2*j^2+z3*j^3, use the account

    Q(z)=(5*sum_i zi^2-(sum_i zi)^2)/2.

This is one half of Tr_{Q(j)/Q}(z*bar(z)). It is integral: the numerator is
even modulo two. It is positive definite: (sum_i zi)^2<=4*sum_i zi^2, so
Q(z)>=sum_i zi^2/2. Since rho*bar(rho)=1, the parallelogram identity gives

    Q(s+rho*t)+Q(s-rho*t)=Q(s+t)+Q(s-t).

Each contact preserves the pair sum and the sum of the two Q accounts.
It also preserves the residue of each labelled slot. Indeed the ring map

    epsilon: O -> F5, epsilon(z)=sum_i zi mod 5

sends rho to one. The two slot changes are respectively (rho-1)*t and its
negative, both of epsilon zero. These statements also hold for disabled
contacts, which are identities.

## 2. A nine-contact token swap and the six-row controlled macro

Chronological products below are executed from left to right. Put

    D(h;c,d)=C(h,c)^3 C(h,d)^3 C(h,c) C(h,d) C(h,c).

The target pair is restricted to (0,0), (u,0), or (0,u). Define

    w2=1+rho^2, u2=1-rho^2.

The complete local D table is

| Helper | Initial targets | Final helper | Final targets |
|---|---|---|---|
| w | (0,0) | w | (0,0) |
| w | (u,0) | w | (0,u) |
| w | (0,u) | w | (u,0) |
| w2 | (0,0) | w2 | (0,0) |
| w2 | (u,0) | w2 | (u,0) |
| w2 | (0,u) | w2 | (0,u) |

Here is a direct proof, independent of a runtime table. Modulo 2, rho is a
unit of order five, and is not one. Thus w, w2, 1+rho^4, and rho+rho^2
are nonzero modulo 2. With helper w and targets (0,0), every contact is
disabled. With initial state (h,c,d)=(w,u,0), the first third power gives

    (1+rho^4,1-rho^4,0).

The next third power is disabled. The following C(h,c) gives (2,0,0),
C(h,d) gives (w,0,u), and the last contact is disabled. Starting instead
at (w,0,u), the first third power is disabled, the second gives
(1+rho^4,0,1-rho^4), the following C(h,c) is disabled, C(h,d) gives
(2,0,0), and the last C(h,c) gives (w,u,0). With helper w2, its difference
from either possible target value is odd in O, so all contacts are disabled.
This proves every row of the displayed D table.

For a separate control g in {0,u}, let A=C(g,h) and set

    V(g;c,d)=A D(h;c,d) A^4 D(h;c,d).

This is a fixed 23-contact word. When g=0 and h=w, A is disabled. Both
D occurrences exchange the target pair and restore w, so their composition
is the identity. When g=u, the first A sends (g,h) to (u2,w2). The first D
is then the identity, A^4 restores (u,w), and the final D exchanges targets.
Thus the complete six-row V contract is

| Control | Initial targets | Final control/helper | Final targets |
|---|---|---|---|
| 0 | (0,0) | (0,w) | (0,0) |
| 0 | (u,0) | (0,w) | (u,0) |
| 0 | (0,u) | (0,w) | (0,u) |
| u | (0,0) | (u,w) | (0,0) |
| u | (u,0) | (u,w) | (0,u) |
| u | (0,u) | (u,w) | (u,0) |

In particular V restores the control and helper, and is a controlled swap
on this local family. Its local action is an involution. On arbitrary
occupied O-valued states we use the inverse obtained by reversing primitive
contacts and replacing each C by C^4; no unrestricted involution claim for
the complete V word is needed. D with helper w provides a nine-contact
unconditional swap on a binary token pair.

## 3. Borrowed-token conjunctions

Encode a bit b by (u,0) for b=0 and (0,u) for b=1. Exchanging its rails
therefore implements XOR with one. The rail that represents a specified
bit value contains u exactly when the value matches.

Suppose the distinct control slots c0,...,c(k-1) each contain 0 or u, the
helper is w, and k-1 scratch slots are zero. First apply

    V(c0; c1,scratch0),

then V(scratch0; c2,scratch1), and continue in this way. Induction proves
that scratch(r-1) contains u exactly when c0,...,cr were all u at entry.
The last scratch is therefore the conjunction control. Use it to exchange
each desired target bit, then reverse the borrowing macros.

This procedure borrows tokens; it does not clone them. Whenever a token
enters a scratch slot it leaves the corresponding control slot. Earlier
scratch tokens retain the successive conjunction controls. Reversing the
macros restores every borrowed control and clears every scratch slot.
Target operations restore their control and helper, so they do not disturb
the unborrowing argument. All controls used in this construction are
distinct from the target rails. A single control uses V directly.

For a multi-output minterm, one borrowing chain may be shared by all target
bit exchanges: its last control is restored by each V. False bit literals
use their zero rail; no bit-value-dependent auxiliary preparation is used.

The largest minterm below has ten controls, hence needs nine scratch slots.
When its first control is zero, induction gives all scratch controls zero,
and the complete macro is identity on all its target bits. This inactive
identity holds for arbitrary binary target and control registers with the
declared blank scratch and common helper. It is a boundary statement about
the complete macro, not about every intermediate primitive contact.

## 4. A fixed, target-independent binary interface

The 49 slots are allocated exactly as in PREREG.md:

| Slots | Purpose | Preparation |
|---|---|---|
| 0..11 | Six-bit current register X | Ordinary binary input |
| 12..23 | Six-bit buffer Y | Binary zero |
| 24..29 | Three-bit depth archive A | Binary zero |
| 30..35 | Three-bit depth archive B | Binary zero |
| 36..44 | Nine individual scratch slots | All zero |
| 45..47 | Three-state selector | One u token, initially A |
| 48 | Helper | w |

All bit registers use the same little-endian code. This code is a generic
binary integer representation and is the same for input and output. Neither
its rails, slot allocation, helper, selector nor work preparation depends
on T(n), v(n), or the chosen input. There are eighteen bit tokens and one
selector token. Since Q(u)=5 and Q(w)=3, every prepared state has

    total sum = 19u+w, total Q = 19*5+3 = 98.

These complete accounts remain true after every primitive contact. In
particular Q=98 is the account of an encoded binary register, not a claim
that the encoded numerical value has quadratic account 2n^2.

The supplied arithmetic table is

| n | m=(3n+1)/2^v | v=v2(3n+1) |
|---:|---:|---:|
| 1 | 1 | 2 |
| 3 | 5 | 1 |
| 5 | 1 | 4 |
| 7 | 11 | 1 |
| 9 | 7 | 2 |
| 11 | 17 | 1 |
| 13 | 5 | 3 |
| 15 | 23 | 1 |
| 17 | 13 | 2 |
| 23 | 35 | 1 |

Each row follows directly by multiplication by three, addition of one, and
exact division by the displayed power of two. The six-bit and three-bit
widths contain all displayed values. The table is a declared part of the
program. Compiling it is not a derivation of the Collatz rule.

## 5. One selected-bank module

Let Z denote the selected three-bit archive, initially binary zero. The
selector token is always the first control of each minterm.

In the first stage, process the ten n rows in increasing order. Match the
selector and all six X bits, then XOR that row's m into Y and its v into Z.
X is unchanged. On an admitted selected input exactly one minterm matches,
so the ready state (X,Y,Z)=(n,0,0) becomes (n,m(n),v(n)). Seven controls
need six scratch slots. A nonselected module is identity regardless of the
binary contents of X,Y,Z, including an occupied Z.

The second stage matches the selector, all six Y bits and all three Z bits,
then XORs the corresponding n into X. The pair (m,v) is injective on the
table, since

    n=(2^v*m-1)/3.

Thus exactly one inverse minterm matches, and X clears to zero. Ten controls
need nine scratch slots. Y,Z and the selector are restored after every
minterm. The old source n is therefore cleared by the physical contact word,
not left in an unreported source register.

In the third stage, for each bit apply selector-controlled Y-to-X XOR,
then selector-controlled X-to-Y XOR. On the ready layer (X,Y)=(0,m), the
two operations give (m,m), then (m,0). This is a transfer on the stated
ready layer; it is not asserted to be a general SWAP on arbitrary X,Y.
Every stage clears its scratch slots and restores the common helper.

The selected module consequently realizes

    (n,0,0) -> (m(n),0,v(n))

for every n in D, on its declared common-ready layer. Each inactive module
is identity for arbitrary binary X,Y and archive values with the same ready
work slots. All these conclusions are consequences of one fixed compiled
contact word. Its edge choices and length are not chosen during execution.

## 6. Two writes, occupied continuation and one skip

The complete word W is module A, then module B, then unconditional selector
token exchanges (B,S) and (A,B). Those last exchanges cycle the selector

    A -> B -> S -> A.

Both modules see the same selector value within one W. Thus only A operates
in the first word, only B in the second, and neither in the third. For

    I={1,3,5,7,9,11,13,15}

the first two active input values belong to D, as the following direct
arithmetic table shows:

| Initial n | After first word | After second word | Ordered depths |
|---:|---:|---:|---|
| 1 | 1 | 1 | (2,2) |
| 3 | 5 | 1 | (1,4) |
| 5 | 1 | 1 | (4,2) |
| 7 | 11 | 17 | (1,1) |
| 9 | 7 | 11 | (2,1) |
| 11 | 17 | 13 | (1,2) |
| 13 | 5 | 1 | (3,4) |
| 15 | 23 | 35 | (1,1) |

The final 35 need not belong to D: it is produced at the end of the second
active word, and the third word skips arithmetic. The domain obligation is
membership of the value received by an active arithmetic word.

At each W boundary Y and scratch are blank, the helper is w, and the
selector advances as displayed. The first depth archive is retained at
the second boundary, and both archives at the third. Retention is not
claimed at every primitive contact: the compiled inactive macros can move
target tokens temporarily before restoring them.

More generally start at selector B with any n in D, any prior three-bit
archive A in 0..7, and fresh B,Y and scratch. Module A is inactive even with
that occupied A. Module B writes m(n) and v(n), preserves A at the boundary,
and W advances to S. This proves all 10*8=80 occupied-continuation cases
symbolically. A recorded complete-contact census is a separate finite audit.

At selector S, both modules are inactive for every six-bit X and every pair
of three-bit A,B values. Hence all 64*8*8=4096 such ready-work combinations
are unchanged except for the selector advancing to A. This consequence may
be checked through the already proved macro semantics; such a check is not
a claim to replay 4096 primitive-contact words.

The complete final current value and the two ordered archives recover the
original input by applying n=(2^v*m-1)/3 twice, in reverse archive order.
Equal first outputs are distinguished by their depths: 1 and 5 both give
output 1 with depths 2 and 4, while 3 and 13 both give output 5 with depths
1 and 3. In addition, reversing all primitive contacts exactly restores
every slot of the initial 49-slot state. These are compatible statements:
the readout pair reconstructs arithmetic data, while the inverse word
reconstructs the complete encoded apparatus state.

The selector has returned to A after three W words, but its A archive is
occupied. A fourth word therefore lies outside the fresh-selected-bank
arithmetic contract. No indefinite renewal, fresh loading, permanent latch
or physical apparatus completion follows.

## 7. Distinct obstructions for other encodings

These boundary results concern their own hypotheses, not the finite binary
compilation just proved.

### 7.1 Odd scaling does not expose an odd scalar head

For every odd rational integer r and every complete O-valued state x,

    C(r*a,r*b)=r*C(a,b).

Indeed r is a unit modulo two, so the enabled condition is identical, and
the enabled formula is linear. Induction gives W(r*x)=r*W(x) for any fixed
contact word; slot permutations also commute with this scaling. The entire
enabled/refused pattern is the same. First-return times to sections invariant
under odd scaling are the same as well.

Thus a scalar family r*x0 with all variable data obtained by odd scaling
cannot by these decisions alone expose v2(3r+1), which varies with r. A
common nonzero reference that is not scaled can break this hypothesis.
The binary compiler has such supplied structure and is not an odd scalar
family. The obstruction does not apply to it.

### 7.2 Labelled raw residues

A contact-only word preserves epsilon in each fixed labelled slot. It
cannot turn a raw scalar n in that slot into the raw scalar T(n) whenever
the two residues differ. For example 3 maps to 5 arithmetically, but their
residues are 3 and 0. This is a fixed-labelled-slot statement; adding slot
permutations changes it to a residue-multiset statement and must be treated
separately. The binary token rails all have epsilon zero and evade this
raw-scalar obstruction by an explicitly different representation.

### 7.3 A fixed auxiliary account cannot fund every raw-scalar expansion

Suppose the input is one raw integer slot n plus a common auxiliary state
of finite account E, and an output slot must contain the same raw scalar
encoding of m=T(n). Positivity and conservation imply

    2*m^2 <= 2*n^2+E.

For n congruent to 3 modulo 4, m=(3n+1)/2, so the required difference is

    2*(m^2-n^2)=(5*n^2+6*n+1)/2.

It is unbounded on this input family. No fixed E supplies the required
raw-scalar outputs for every such n, regardless of execution time. This
does not exclude another input encoding whose account grows with n^2,
a different output chart, or a bounded input family. The constant-account
binary code belongs to the latter explicitly specified alternatives.

### 7.4 Fixed finite words on affine raw inputs

Let a complete prepared state be affine in an unbounded integer n, with
common auxiliary constants, and let a fixed finite contact word be followed
by one fixed affine scalar reading. Each enabled/refused itinerary gives
an affine output alpha*n+beta over Q(j). There are only finitely many
itineraries.

For every v>=1, there are infinitely many positive odd n with exactly
v2(3n+1)=v: take the unique residue satisfying 3n+1=2^v modulo 2^{v+1}.
On an infinite subset of that family some one itinerary occurs. If its
output equals T(n), agreement at two distinct n forces

    alpha=3/2^v, beta=1/2^v.

Distinct v require distinct affine expressions. Finitely many itineraries
cannot supply them all. Therefore this class cannot implement T on every
positive odd n. Variable unbounded execution, a non-affine input chart,
a different reading class, and finite domains are outside this obstruction.
In particular ordinary binary digits are not an affine raw-scalar chart.

## 8. Separate contact halving with a J twist

There is also a direct arithmetic contact lemma that is not the finite-table
compiler. For an even x in O,

    C(x,0)=(J*x/2,(1-rho)*x/2),

whereas an odd x is left fixed. The identity

    J^{-1}=-rho-rho^3

follows by multiplying and using 1+rho+rho^2+rho^3+rho^4=0. Thus J is a
unit of O, and multiplication by J preserves membership in every 2^k O.

Let nonzero x have finite 2-adic divisibility v, and prepare an active slot x
with D+1 distinct zero slots, where v<=D. Apply the fixed contact cascade
(active,1),...,(active,D+1). An induction gives, for s<=v,

    active_s=J^s*x/2^s,
    slot_s=(1-rho)*J^{s-1}*x/2^s.

These first v stored slots are nonzero because O is an integral domain.
After v successful contacts the active value is odd; every later contact
is refused and its target remains zero. The final current state therefore
contains v as the length of its nonzero stored prefix, and contains the
normalized odd part as J^{-v}*active. No discarded history is required to
read this pair. The full cascade remains a conservative global permutation.

If x=3n+1 had first been produced by an admitted common preparation, this
would read the Collatz pair (T(n),v2(3n+1)). The lemma itself does not produce
3n+1 from a raw n and a common reference. Supplying that numerator at the
input is not a proof of the missing synthesis. No such synthesis, unbounded
bank renewal or derivation of Collatz dynamics is claimed here.

## 9. Status and scope

The positive result is a finite, reversible, conservative contact compilation
of a supplied arithmetic table, with a common binary interface, two actual
depth writes, an occupied-record continuation, and one skip. Its supplied
rule and preparation are explicit. It does not promote any Canon claim.

Exact runtime transcripts and independent comparisons, when present, must
be read at their declared finite scope. Two implementations on x86_64 do
not constitute a two-architecture public computation gate. No claim here
selects a prime, proves global Collatz convergence, identifies a conserved
account with measured energy, supplies an occurrence law, or closes a
physical apparatus owner.
