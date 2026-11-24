# Frozen finite contact Collatz step and occupied depth archive

Status: NON-CANONICAL / L1. Candidate C-COLLATZ-CONTACT-STEP-RECORD-N.
Owner: Codex session /root. Public lock: issue #1860.
Base: mathorn1973/twist-j main 0c33e2b281e39127c269ef5dd7f5b529a62e9e65,
Public Canon v107. This is incubation, not a formal public probe or Canon fold.

## Equation and carrier

O=Z[j], 1+j+j^2+j^3+j^4=0, rho=j^2, u=1-rho, w=1+rho.
Use the total integral relative contact C(a,b): if a-b is in 2O, put
s=(a+b)/2, t=(a-b)/2 and return (s+rho*t,s-rho*t); otherwise return (a,b).
Q(z)=(5*sum(z_i^2)-(sum(z_i))^2)/2 in basis (1,j,j^2,j^3).
Every primitive contact has order five and preserves pair sum, Q and
each labelled residue sum(z_i) modulo five.

All integers in the computing interface use ordinary little-endian binary,
with bit b stored on two slots (u,0) for b=0 and (0,u) for b=1.
This chart, and the identical current/output chart, are independent of T.
There are no input-dependent auxiliary preparations.

Zero-based slots: current X uses 0..11 (six bit pairs), buffer Y 12..23
(six pairs), archive A 24..29 (three pairs), archive B 30..35 (three pairs),
scratch 36..44 (nine individual zero slots), selector 45,46,47 (one u token),
helper 48=w. Initial selector is A=(u,0,0). All auxiliary bit registers start
at the binary zero code. Total 49 slots, sum 19u+w, Q=98 for every input.

The admitted arithmetic domain is D={1,3,5,7,9,11,13,15,17,23}.
For n in D define v=v2(3n+1) and m=(3n+1)/2^v. Depth fits three bits;
output fits six bits. Initial experiments use I={1,3,5,7,9,11,13,15}.
Every n in I and its first Collatz output belong to D.

## Literal compilation, not an emergent arithmetic law

The rule T and finite domain D are supplied. The implementation is an openly
declared finite truth-table compiler into contacts. This does not derive T
from J, supply an unbounded arithmetic algorithm, or make a native-U claim.
The table is generated from 3n+1, not encoded into input preparation.

Chronological words are left to right. For control g in {0,u}, helper h=w,
and targets (c,d) in {(0,0),(u,0),(0,u)}, define
 A=C(g,h),
 D(h,c,d)=C(h,c)^3 C(h,d)^3 C(h,c) C(h,d) C(h,c),
 V(g;c,d)=A D(h,c,d) A^4 D(h,c,d).
V has 23 contacts, restores g,h, and swaps c,d exactly when g=u.
D(w,c,d) alone supplies the nine-contact unconditional token swap.

A minterm-controlled bit XOR is compiled with a list of control slots
c0,...,c(k-1). Borrow the token of c1 into scratch0 controlled by c0;
borrow c2 into scratch1 controlled by scratch0; continue. The last scratch
holds u exactly when every control is u. Use it to V-swap the target bit
rails, then undo all borrowing V gates in reverse. A single control needs
no scratch. False controls use the zero rail of the same bit. Multi-output
minterms share one borrowing/unborrowing chain. Nine scratch slots suffice.

One selected-bank module performs:
1. For n in increasing D, controlled by selector token and six input-bit
   minterm rails, XOR the binary bits of (m(n),v(n)) into Y and that archive.
2. For n in increasing D, controlled by selector token, six Y-bit minterm
   rails and three archive minterm rails, XOR bits of n into X. The inverse
   arithmetic pair is injective, so this clears X on the declared ready layer.
3. For each bit, XOR Y into X controlled by selector, then X into Y controlled
   by selector. Since X was cleared, this transfers m to X and clears Y.

The same complete word W contains module A, module B, then unconditional
token swaps (B,S) and (A,B). Thus selector A->B->S->A. An inactive module
must be identity for arbitrary binary X, Y and archive values, including
occupied archives; the contract only claims fresh selected-bank operation.
The word never chooses an edge or a length from its running input.

## Frozen positive scope and resource disposition

Run exactly three identical W words. First word: X=T(n), A=v(n), B blank.
Second: X=T^2(n), A unchanged, B=v(T(n)). Third: selector S skips both
modules, X,A,B unchanged and selector returns to A. At every W boundary,
Y and scratch are blank, helper is w, and the complete stated sum and Q hold.
Archive retention is at word boundaries, not at each primitive contact.
All input source bits are changed to the new value; the old n is not kept
in an unreported source or work register. The final X and ordered depths
restore the initial input by the exact inverse equation.

The fourth step is outside this contract. No indefinite renewal, permanent
latch, arbitrary second post-start loading or physical apparatus closure.

Occupied-continuation audit: start at selector B for every n in D and every
three-bit prior A value 0..7, with B and all work ready. One W must compute
(T(n),v(n)) into X,B, preserve A exactly, and advance selector to S.
Skip audit: selector S, X in 0..63, A and B each in 0..7; all 4096 combinations
must be unchanged except selector A. This check may use the separately proved
conditional-swap semantics rather than replaying every primitive contact;
that scope must be labelled. Full-contact replay is required for the eight
three-word trajectories and all 80 occupied-continuation cases.

## Verifier, systematics and failure threshold

The accepted standard-library verify.py is frozen with this file before its
first scientific execution. Exact integer tuples only. No floating point.
Check the complete six-input V contract, inverse, sum/Q/per-slot residues
for every distinct primitive pair actually used; the eight complete
three-word trajectories and their full contact inverses; all 80 occupied
continuations and their inverses; the declared 4096 abstract skip cases;
output-depth inverse recovery; identical first outputs with different depths.
Record the actual edge-word digest, complete boundary fingerprint, counts,
platform and actual stdout, exit status and empty stderr. A timeout or exception
is a failed attempt, not a scientific pass. Do not modify a frozen threshold.

Falsifiers: any wrong local V row, output/depth mismatch, occupied archive
change, dirty work boundary, broken inverse, failed conservation or labelled
residue check, word differing by input, or an active arithmetic word receiving
X outside D in the first two words. The second output may be 35, outside D;
the third word skips arithmetic. Any one fires the candidate as stated. Preserve that result;
a repaired successor requires a new candidate identifier and pin.

Independent breaker: write from this frozen contract without reading the
author verifier. Freeze break.py before any comparison or author output is
opened. It must use an independently constructed word and cyclotomic
representation. Both lanes here are x86_64; agreement is not a two-architecture
public computation gate. Word construction, compiler and primitive tests are
part of this finite research contract, not repository integrity CI.

## Separate symbolic boundary statements

The note may prove raw-slot residue and fixed-account obstructions, the
finite-affine-branch obstruction and the contact halving-with-J-twist lemma.
They must remain distinct from the finite binary computation and must not
pretend that x=3n+1 was physically generated by the halving lemma itself.
No prime-selection, global Collatz convergence, measured energy or occurrence
conclusion is included. No status exceeds candidate-T proof / candidate-C
finite evidence before a separate reviewed public fold.
