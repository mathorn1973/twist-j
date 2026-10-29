# Scoped mathematical and implementation review

2026-10-29. **PASS within the declared NON-CANONICAL L1 supplied-control model.**

Public pre-run source pin: `58ae23f4f6fbf4ef3b9338cbd63faaf01df87b36`.
Reservation: #1818.

This review was prepared by a separate assistant subagent in the same
conversation as the construction. It is a separate reasoning pass, not an
external human review, an independent-account approval, or canonical
acceptance. The reviewer read the mathematical arguments and implementation
before the first new run, then inspected the retained first-run evidence.
The reviewer did not execute or import the new scientific programs.

## Reviewed inputs

The four preceding files in `notes/C-J-LAMBDA-CARRY-N` retain their disclosed
2026-10-28 bytes. The old carry proof, compiler, both arithmetic representations
and recorded local evidence were reviewed first. The new review covers
`PROOF.md`, `PREREG.md`, `arithmetic_compiler.py` and `verify.py`.

| New input | SHA-256 |
|---|---|
| `PROOF.md` | `31c96297a283a7135b69608dc9cc9d3dd6209be0ac9f505d7d5fc49f955aed06` |
| `PREREG.md` | `f75705a4a532de091b8366ce1457e5eecb790526a66d9a220b7ced3b22991fb8` |
| `arithmetic_compiler.py` | `0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027` |
| `verify.py` | `b33c1993723c8e1e42b0d7cb0946f7eea7f0b3efcdb2d3da5066690b35c64f0f` |

The final pre-pin verifier adjustment preserves failed child stdout/stderr,
classifies a child timeout as INCOMPLETE, and checks the arithmetic helper's
exact hash. It does not change the mathematical schedule. The final proof
wording correctly distinguishes all short word-map checks from the smaller
set of complete generated-program checks.

## Mathematical and code findings

1. **All-length carry bound.** The preceding exact division by lambda,
   telescoping invariant, positive trace form and contraction estimate prove
   `Q(C)<=3134` and `|c_j|<=35` for every reachable carry. The conclusion does
   not extrapolate finite word tests. The duality between J and J inverse
   correctly swaps input/output labels. The 1649 states describe this exact
   reachable carry representation; minimality over all implementations is
   not asserted.
2. **Small carry function.** The binomial identity for
   `h(x,y)=floor((x+y)/5)` is correct modulo five. The four generated terms
   restore both helpers and implement a phase-free target translation.
3. **Ripple cleanup.** For final digit z and incoming bit c, the identity
   `c_next=[z<A]+c[z=A]=h(A,4-z)+c[z=A]` is correct, including the equality
   boundary. The emitted backward order retains the needed earlier carry.
   The temporary reflections and source subtractions are restored.
4. **Shifted coefficient arithmetic.** With `d_j=c_j+35`, S equals the old
   coefficient sum plus 175. Thus `a=S mod5` and `Q=q+35`. All four successor
   formulas follow. The proof gives `27<=S<=323<625`; the resulting
   `d'_j` lie in `0..70`, so modulo125 arithmetic returns the exact codes.
5. **Prepared interface and aliases.** The offset35 operations act on the
   prescribed initially zero banks. C0 is initialized to four codes35 and
   returned to physical zero. Repeated padded zero addresses are read-only;
   targets, carries and predicate helpers are disjoint. The emitted reverse
   coefficient schedule restores the following carry bank without changing
   the output digit.
6. **Inverses and physical primitives.** Logical inverse blocks are lowered
   through the existing positive-duration constructions. Changing the sign
   of H is a full inverse: its terms restore their controls/helpers and are
   commuting translations of the same target. The old equality and cubic
   primitives have exact phase-free decompositions. Their conditional local
   and pair controls are supported by the pinned source model, with the
   enlarged addressed apparatus explicitly supplied.
7. **Resource formulas.** Direct counting of the emitted schedule agrees
   with `136917N` pair pulses and `255187N+32` local operations per
   multiplication, `14N+22` data/work cells, and `15N+22` including archive.
   Whole-word counts are `136917N^2+N` paired and `392104N^2+36N` total
   instructions including direct Fourier preparation. These are construction
   bounds, not laboratory speedups or optimality results.
8. **Archive and controller scope.** The preceding triangular readout
   bijection and conditional flat preparation justify the formal uniform
   archive and prime-five return weights. The finite clock unitary is
   mathematically well defined. Its physical realization, source purity,
   work, routing, actual errors and a law for one occurred outcome remain
   separate assumptions or obligations.

## Inspected first-run evidence

The retained execution record reports Python 3.12.14 on Linux x86_64,
exit 0, empty stderr, and 67.434186 seconds. Scientific stdout is 8354 bytes
and 293 lines, SHA-256:

`7d02438c04094fc09b0b77965d572b9655776438c3d033ae55242372a6e06bc4`.

Reading that output confirms the following recorded outcomes:

- Both freshly rerun preceding arithmetic representations agree.
- All 250 signed H input/target cases pass.
- All 406900 adder pairs for widths 1 through 4 pass forward and inverse;
  another 668 cases use fully expanded elementary permutations.
- All 16490 reachable coefficient transitions agree with the complete
  preceding closures; 30 predeclared steps also pass primitive expansion.
- All 97655 short word maps and 175 fixed longer inputs preserve the exact
  ring identities and previous hashes.
- All 330 complete generated multipliers and 1320 signed dirty-target
  evaluations return their admitted workspaces to zero.
- Every length-five archive is distinct: 3125 words, 120 exact zero root
  sums. All shorter archive hashes also agree.
- Every preregistered generated resource inventory matches its formula.

These are inspected run results, not a personal rerun by the reviewer.
The verifier uses independently represented old arithmetic as a reference;
it does not claim a second independently implemented new circuit compiler.

## Acceptance boundary

No mathematical or implementation blocker was found. The computed evidence
is a local candidate-C result; the all-N statement rests on the conditional
analytical construction. The retained first run covers one architecture.
Required repository replay, any x86_64/aarch64 qualification and external
review remain distinct from this document. Large circuits are checked
compositionally through exact primitives, exhaustive small blocks and every
reachable coefficient edge. No full large-circuit amplitude simulation,
native-U realization, physical occurrence law, L1-to-L6 lift, canonical
promotion, registry change or frontier change is certified here.
