# Independent breaker freeze

Status: NON-CANONICAL / L1. No authority or Canon promotion.

Breaker owner: independent child session `/root/synthesis_breaker`.
The parent author did not open this implementation before its freeze. The
breaker read the frozen contract only and did not read or import `verify.py`,
author stdout, or author boundary states.

## Frozen sources

- Public author source pin: `5aef722e8f1c3d5cd3c9c25b164b5ed91f660aa2`.
- `PREREG.md` SHA-256:
  `e03e59bc29aa6b159321805cb5a869ecba45cecc7e0b8eeec80458a79fb711fa`.
- Accepted independent `break.py` SHA-256:
  `5fe58620266b6c49a83cbbc6f3ce8fc374e277bff74de66da6819c502710bf32`.

Only `python -m py_compile break.py` was run before this freeze. No scientific
code, word constructor, primitive contact, or test case was executed. This
implementation must be published with this scope before scientific execution;
the frozen breaker is not subsequently edited to match author results.

## Independent construction

The internal basis is `(1,rho,rho^2,rho^3)`, not `(1,j,j^2,j^3)`.
Multiplication by rho is the integer map
`(a,b,c,d) -> (-d,a-d,b-d,c-d)`. Primitive integrality is tested directly in
this basis. Boundary conversion to the j basis is
`(a,b,c,d) -> (a-c,d-c,b-c,-c)`.

The implementation first builds a tape of independently assembled V and D
macros, then lowers that tape into literal edges. Minterm controls are the
selector followed by bit rails in increasing bit order. Multi-output XORs
write Y bits in increasing order, then archive bits in increasing order.
Borrowing is undone by the same V macros in reverse order. Transfer is
interleaved per bit: Y to X, then X to Y. These ordering conventions were
confirmed by the parent before either source was executed or compared.

The edge digest hashes the ASCII concatenation `i,j\n` for every chronological
edge, with a final newline. The boundary digest hashes compact JSON with no
whitespace and no final newline, of the form
`[[initial_n,state_after_W,state_after_W2,state_after_W3],...]`.
Starts are in the frozen increasing order. A state is the 49-slot list; each
slot is its four canonical j-basis integer coefficients.

## Positive and negative scope

The frozen program must check:

1. All six control/target V rows by literal contacts and their full native
   inverses; also the three unconditional D rows used by selector movement.
2. Every distinct ordered primitive pair encountered in any replay, including
   inverse replay: fifth power, exact four-contact inverse, sum, Q, and both
   labelled residues modulo five.
3. Eight full three-word trajectories, all boundary registers, exact source
   recovery from the final current value and ordered depths, and full native
   inverse replay to the initial 49-slot state.
4. Eighty full-contact occupied-A continuations and their native inverses.
5. Exactly 4096 skip states through separately validated V/D macro semantics.
   This part is expressly not a full primitive-contact census.
6. At least one common first output associated with distinct stored depths.

The two active arithmetic inputs must belong to D. The second arithmetic
output need not belong to D; the third word skips the arithmetic modules.

Each native inverse explicitly traverses reversed edges and applies C four
times per reversed edge. Pair memoization caches already audited exact C
transformations; it does not replace whole-word or boundary replay.

Inactivity for arbitrary binary register contents follows separately by the
zero-selector induction: the first borrow gate is inactive, every subsequent
scratch control stays zero, and both borrowing and output gates are identity.
This does not assert successful active operation with an occupied selected
archive or a dirty buffer.

Any assertion, exception, timeout, or wrong digest comparison is retained as
a failed attempt. No threshold is changed after execution. Agreement between
the two implementations on this host remains a single-architecture result;
it is not the public two-architecture scientific gate.

This finite truth-table experiment does not establish an unbounded Collatz
algorithm, a contact derivation of 3n+1, indefinite archive renewal, physical
time, measured energy, or the bridge from native U.
