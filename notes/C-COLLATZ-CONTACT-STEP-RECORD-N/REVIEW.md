# Independent mathematical and implementation review

Status: NON-CANONICAL / L1. Candidate-T symbolic review and candidate-C finite
runtime evidence only. No Canon promotion, native-U realization, or physical
apparatus closure.

Reviewer: child session `/root/synthesis_breaker`.

## Verdict

The frozen finite supplied-rule contact compiler passes the independent
implementation attack at its declared scope. No preregistered falsifier
fired. This is an independently written implementation of the specified
construction, not an independently discovered Collatz mechanism.

The positive result is concrete: a single 18,280-contact word on 49 slots
performs the two admitted arithmetic transitions with ordered depth writes,
preserves an occupied prior archive on all 80 admitted continuations, and
performs the declared skip. The complete account is Q=98. Every complete
native inverse restores the full prepared state.

The actual rule is supplied by a ten-row finite arithmetic table compiled
into the contact word. Consequently this result establishes finite contact
programmability with explicit memory. It does not establish that the contact
law itself selects 3n+1 or produces an unbounded arithmetic algorithm.

## Independence and execution order

The breaker read PREREG.md, wrote its own compiler and contact arithmetic in
the basis `(1,rho,rho^2,rho^3)`, and froze before author code or author stdout
was opened. Only syntax compilation occurred before the freeze.

- Author source pin: `5aef722e8f1c3d5cd3c9c25b164b5ed91f660aa2`.
- Independent breaker pin: `17caea0066ec0dff2d5c2b8227e352edb0653023`.
- Frozen breaker SHA-256:
  `5fe58620266b6c49a83cbbc6f3ce8fc374e277bff74de66da6819c502710bf32`.
- Frozen scope SHA-256:
  `d3ab5f7bd1df35c9f96a61b2f76b58aae3a3d7fef59973f77b46133a5602fe03`.

Only after its source and scope had public byte-identical readback did the
breaker execute. Its complete own execution finished before the author
implementation and output were read. The subsequent comparison changed
neither frozen scientific program.

The breaker run used Linux, x86_64, Python 3.12.14. It started at
`2026-11-02T22:21:55.700296Z`. The exact relative command was

    python break.py --boundaries-out break-boundaries.json

Exit code was zero. Stdout was 2554 bytes with SHA-256
`62d90565fe7a21532de212d94b53e1c465c96967abebc9535ce1f2645d8966b7`,
and is retained as `BREAK-EXPECTED.txt`. Stderr was zero bytes, whose
SHA-256 is
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
Engineering elapsed time was 2.1833251819989528 seconds. This time is runtime
metadata, not an exact scientific quantity. No internal interpreter path or
machine identifier is required to reproduce the stated integer calculation.

## Independent checks and comparison

The breaker completed all six literal V rows and their native inverses,
plus three D rows and their inverses. It replayed eight complete three-word
trajectories and 80 occupied-A continuations, then inverted every case by
reversing edges and applying four literal contacts per reversed edge.

Every distinct ordered primitive input pair encountered was checked for
sum, Q, both labelled residues, fifth power, and the exact inverse. There
were 15 such distinct pairs. The complete breaker performed 9,506,425
primitive applications. Its 135 extra applications relative to the author
are exactly the three additional nine-contact D rows with their native
inverses: 3*9*(1+4)=135.

The 4096 skip cases were checked through the separately validated token
semantics. They were not claimed as 4096 primitive-word replays. The inactive
module statement also has a direct proof: a zero selector prevents the first
borrow, so every successive scratch control remains zero and all borrowed
or target operations restore their boundary inputs.

Both compilers produced the identical chronological edge word:

    contacts: 18280
    edge SHA-256:
    92fcd3f9f267dd5ff5be76327680bbe02d39e87f58bed0c395e3e03904722460

The author counts 794 V macros; the breaker counts those 794 V macros plus
the two final D macros. This is a reporting convention, not a word mismatch.

The independent boundary output uses `[n,s1,s2,s3]`, whereas the author
uses `[n,[s1,s2,s3]]`. After changing only that outer JSON grouping and
converting the breaker states to the canonical j basis, all complete
49-slot boundary states have the same digest:

    ca60bf44b6234819e41435a7032661b5cecb428f602fbeda2df00e406dcef1dd

The original breaker boundary digest remains independently recorded as
`c8786d113be89372f8ebc132d6e63967e958a1bf3a2aa5db31558df7719c543e`.
No frozen source or stdout was rewritten to align the formats.
`COMPARISON.json` records the comparison.

| Initial | First current | First depth | Second current | Second depth |
|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 1 | 2 |
| 3 | 5 | 1 | 1 | 4 |
| 5 | 1 | 4 | 1 | 2 |
| 7 | 11 | 1 | 17 | 1 |
| 9 | 7 | 2 | 11 | 1 |
| 11 | 17 | 1 | 13 | 2 |
| 13 | 5 | 3 | 1 | 4 |
| 15 | 23 | 1 | 35 | 1 |

The second output 35 is permitted: the following third word skips arithmetic.
Only the inputs to the two active arithmetic words must belong to D. The
first archive is preserved at the second word boundary, and both archives
at the third. Primitive-contact permanence was neither claimed nor tested.

## Mathematical review of the construction

The contact's totality and order-five property hold on the complete O-valued
pair carrier. The enabled condition is preserved when the relative part is
multiplied by rho, while a disabled pair remains unchanged. Thus every
compiled word is a global permutation, even outside the prepared arithmetic
layer. Its interpretation as an arithmetic operation is restricted to that
layer.

The six-row V argument is valid. With a zero control the two D words cancel
on the admitted token targets. With a u control, the helper becomes
1+rho^2, for which all D contacts are disabled, then returns to w before the
last target exchange. The borrowing chain moves tokens rather than cloning
them; reversing the macros restores all controls and scratch positions.

The inverse table stage is justified by

    n=(2^v*m-1)/3.

It therefore clears the source register without retaining an unreported n.
The independent full-state inverse and output-depth reconstruction verify
different facts and both succeed. The proof appropriately states that the
two XOR transfers are not an unrestricted SWAP and that V is not claimed to
be an involution on arbitrary O-valued targets.

The separate halving lemma is also valid. For even x,

    C(x,0)=(J*x/2,(1-rho)*x/2),
    J^{-1}=-rho-rho^3.

Thus J does not alter the divisibility depth, and a fixed bounded zero-slot
cascade stores exactly the nonzero prefix corresponding to the successful
halvings. This lemma starts from x. Substituting x=3n+1 does not prove that a
common contact preparation generated that numerator.

## Hard boundaries that the binary contract correctly avoids

For raw pure-integer slots, the smallest direct residue falsifier is
3->5: epsilon changes from 3 to 0 in F5. A contact-only word cannot make
that replacement in one fixed labelled slot. A separate pure-integer depth
slot with common preparation cannot serve both n=1 and n=3, whose depths
have different residues. These are raw-slot statements; the binary token
code explicitly uses a different chart in which all token rails have residue
zero.

A fixed auxiliary account cannot fund all raw scalar expansions, since
T(n)=(3n+1)/2 for n congruent to 3 modulo 4. Positivity makes the required
extra quadratic account unbounded. Similarly, a fixed finite contact word
on affine raw inputs has only finitely many affine branches and cannot
produce all Collatz valuation branches. Neither argument applies to the
declared finite binary code and its supplied truth-table word.

The depth statement has an especially direct finite falsification family.
For p_a=(4^a-1)/3, the depth is 2a. One affine scalar branch hits at most
two such input-depth points, because consecutive p_a increments are 4^a.
A word of L binary-decision contacts has at most 2^L affine branches;
therefore among the first 2^(L+1)+1 members of this tower at least one raw
depth output must fail. This concerns a fixed affine raw input/output
class, not ordinary binary registers.

## A separate target-designed two-point illustration

This small symbolic illustration was derived separately from the accepted
binary compiler. It is not evidence for its generality or a missing native
arithmetic law. Let

    E(n)=(n,7,14+rho+20*j^3),
    W_small=C(0,1) C(0,2).

Read m as the constant j-basis coefficient of slot 0, and v as the rho
coefficient of slot 2. The fixed preparation and two-contact word give:

    n=1:
      (1+2*j-4*rho+12*j^3, 4+3*rho, 17-2*j+2*rho+8*j^3),
      hence (m,v)=(1,2).
    n=3:
      (5-2*rho, 5+2*rho, 14+rho+20*j^3),
      hence (m,v)=(5,1).

The constants were designed for this two-point target. The helper positions
do not reset, the outputs are coefficients of nontrivial O-valued states,
and the same word already fails at n=5: it reads (1,3) instead of (1,4).
It must therefore remain a labelled illustration of a finite interface,
not the main result or a proposed general Collatz mechanism.

## Remaining obligations

The fourth word encounters an occupied selected archive and is outside the
contract. No indefinite reset, fresh reload, or permanent latch follows.
The word's arithmetic table and available interaction sequence are supplied;
their native selection remains open. Q is a conserved mathematical account,
not a measured energy identification. The word-boundary count is not by
itself an operational physical time standard.

Two independent implementations on this x86_64 host remain one architecture.
Ordinary repository CI does not automatically replay this notes-only science
and cannot be cited as its two-architecture scientific confirmation.
