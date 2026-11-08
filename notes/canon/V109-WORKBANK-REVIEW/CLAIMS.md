# Exact proposed proof scopes for v109

NON-CANONICAL / L1. These are candidate claims awaiting independent
mathematical acceptance, not new Registry entries. Source: PR1879 at
`d6a5f77169d1027a22959c41aa5a45a783643a3e`; all mathematical and executable
sources are unchanged from pin `6f6570bbbddfc496131dd31c5fdacaaa9e1cd9e5`.

## 1. Positional-bank copying

O=Z[j], rho=j^2, b=1+rho^2. A fresh bank is M_empty=(-b,b)^5 and M[p]
rotates only its labelled pair p by rho. On two disjoint ten-slot banks,
one fixed 60-contact word K satisfies

    K(M[p],M_empty)=(M[p],M[p]) for every p in Z/5.

Its source is restored at each 12-contact module boundary; 41 of the 60
contacts are admitted for each code input. Its literal inverse has 240
contacts. At the stated endpoints the two-bank account is 60, and every
contact preserves the complete sum, Hermitian account and labelled residues.

Review PROOF sections 1-3: the actual parity guard on this b-family, all three
local phase cases, the cyclic-neighbour embeddings, restoration needed by
induction and the fresh-target condition. The explicit word is an upper
bound, not a minimum. An occupied target, arbitrary phase code or source
constancy inside a module is outside the positive copying contract.

Falsifier: failure of any local row, edge embedding, complete copy identity,
restoration boundary, admitted count or exact inverse on the stated family.
Do not infer full timing-trace privacy from a constant admission count.

## 2. Four-place literal-copy obstruction

For any nonzero b in O, set

    E=(-b,b,-b,b), A=(-rho*b,rho*b,-b,b), T=rho*E.

No fixed word of total contacts on these four places can satisfy both
F(E)=E and F(A)=T. Every contact commutes with simultaneous multiplication
by rho, including its guard, so F(T)=T; injectivity then contradicts A!=T.

Review PROOF section 4. The restriction b!=0 is essential. There is no
auxiliary reference in this statement. It does not prohibit a different
output code or the twenty-place copier, and requires no BFS or minimality
claim from the supplied witness package.

Falsifier: failure of total-contact equivariance or bijectivity, or a word
meeting both displayed conditions with b!=0 under the same alphabet/carrier.

## 3. Finite reuse with retained archives

For every specified finite k>=1, the supplied contact/SWAP alphabet admits
one fixed program on 26+25k slots. It accepts all 10^k independently prepared
input tuples from I={0,1} times Z/5, with the same 26+20k auxiliary slots
initially prepared identically. Complete account is 68+74k, auxiliary
account 68+60k and ring sum 2(k+1).

Each cycle writes the actual two v108 working records, copies them into two
fresh permanent banks and reverses the work. The complete 31-slot working
core, including source, clock, controls and the SAME two working banks,
returns to the corresponding prepared input. Fixed five-slot exchanges load
prequeued next inputs and park the actual restored earlier inputs. No
expected-state assignment occurs in the primitive evolution.

The 2k permanent banks alone decode every ordered input tuple. Each is
untouched after its completed copy through the rest of the forward program.
The literal inverse intentionally removes records and restores every
initial coordinate. The specified program uses 26870k contacts and 5(k-1)
supplied swaps; its unreduced inverse uses 107480k contacts and 5(k-1) swaps.

Review PROOF sections 5-8: the full read interface, exact occupied core before
uncompute, disjoint supports, induction with actual used states, complete
input parking, resource formulas and the decoder's injectivity. The frozen
k=3 audit covers all 1000 tuples, 101 slots, account 290, all complete core
recoveries and all full inverses. The supplied extra k=1,2,4,5 tests audit
instances; the finite-k proof must rest on induction, not those samples.

For a reader restricted to B five-valued marked banks, distinguishing 10^k
histories requires 5^B>=10^k. The construction's 2k banks are an upper bound;
for k=3 the counting bound requires at least 5 and the construction supplies 6.
No optimal storage code or word length follows.

Falsifier: an admitted tuple violating a complete endpoint, core-restoration,
parked-input, retention, account, current-bank decoding or inverse identity,
or failure of the induction's ready-input/fresh-target premise at a stage.

## Explicit derivation of the finite read event table

The canonical v108 common-apparatus proof contains the complete ten-input
stage identity, including the controlled read action and nine-/five-state
source/clock orbits. Its active claim is
RELATIVE-CONTACT-COMMON-APPARATUS-OPEN [T] in Canon section 2, with its original
finite two-experiment scope unchanged. The following is an expositional
expansion for a later fold, not a change to its frozen evidence.

At step t, 0<=t<=9, starting from s in {0,1}, the first read is active exactly
when s+t=0 modulo 9. The second, after F^-1, is active exactly when
s+t-1=0 modulo 9. For s=0 the first equation gives t=0,9 and the second t=1.
For s=1 the first gives t=8 and the second t=0,9. Ordering these reads gives

    s=0: (0,first), (1,second), (9,first);
    s=1: (0,second), (8,first), (9,second).

Both reads see clock phase r+t. The selector visits A,B,skip in order;
the first two writes therefore have labels -r and -r-Delta_s, with
Delta_0=1 and Delta_1=8. The third event skips. These are all solutions
in the declared ten-step interval. The full W=S^10 endpoint is

    (Y_(s+10),X_r,0,u,0,0,w,0,M[-r],M[-r-Delta_s]).

This explanation supplements the exhaustive finite audit and accepted v108
interface. It does not assert arbitrary input phases, occupied-bank
overwrite or an unbounded extension of the read schedule.

## Preserved boundaries

The family scales its initially prepared inputs and fresh permanent archive
stock with k. No one fixed finite carrier is claimed to retain unlimited
independent history. No raw-input synthesis, post-start external loading,
autonomous next-input selection, contact-only SWAP compilation, regeneration
of occupied retained archives, global monotone freshness, native-U realization,
Collatz completion, calibrated physical energy/time or thermodynamic law is
proved. Source-renewal PR1867/1869 have different interfaces and remain
separate until an actual common contract is established.
