# Public Canon v101 raw-residue fold review

**Release preparation; NON-CANONICAL until the ordinary activation.**
Date: 2026-10-09. Author: A. M. Thorn.
Reservation: [#1435](https://github.com/mathorn1973/twist-j/issues/1435).
Public basis: `c164b79ce134152ac7cd600421791df74113f29f`, Public Canon v100.

## Decision and scope

The fold proposes four proof-backed T claims at L1:

- U-NATIVE-RAW-RESIDUE-READOUT: the explicit receiver/counter inverse on all
  625 raw sources at ready (0,1), for every n>=3.
- U-NATIVE-RECEIVER-ONLY-RESIDUE-NOGO: actual recurrent support excludes any
  nonconstant eventually persistent original-sum reading from current (q,r)
  alone at every common ready, even with source-dependent waiting times.
- U-NATIVE-RAW-RESIDUE-PRESENCE-BOUNDARY: identical receiver histories cannot
  distinguish absence; reserving one raw input does not reserve its class.
- U-J-POWER-CHECKPOINT-NOGO: the early universal native collision and an
  integral unit certificate force zero for checkpoint-only J-equivariant
  readings modulo every 5^m, when the recurrence holds from n=0.

All four proofs are included directly in canon/CANON.md. Their proposed T
status rests on these written arguments. The minimal reproduction is a
supplementary exact finite audit, following the v99 proof-fold route; it is
not a new formal P-probe or retrospective preregistration.

The requesting discussion already exposed the formulas and exploratory
checks. It also corrected two overstatements before this fold: the full
unbounded counter was not proved necessary, and reserving one piston input
was insufficient to distinguish absence. The accepted scopes retain both
corrections. The current-sum variable z is explicitly distinguished from the
original source label kappa(P).

## Proof and code review

Separate agents in the same collaborative session authored the written
proofs and supplementary audit. A further read-only cross-review checked the
proofs against the final registry, and the proof author separately reviewed
the audit source and its boundaries. The integrating reviewer inspected both.
This is separately authored review within one assisted session, not an
external referee, blind confirmation, or independent empirical experiment.

The review checked the n=3 inverse base, the exact alternating-floor-sum
increment, both synchronized induction cases, every five-row source table,
projection of actual recurrent sign fibres (including the zero fibre),
overlap connectivity, source-dependent waiting quantifiers, the complete
history equivalence, the absence class restriction, the integral certificate
and inverse of J, and the every-step recurrence domain. No mathematical
blocker was found. A wording correction clarified that z uses current
coordinates rather than the original source sum.

The exact audit has separate full-state and quotient implementations. Static
review found no file writes, network operations, external data, random or
floating-point arithmetic, or repository-verifier imports. It refuses -O.
The source was stored as public Git blob
`5e757ae82934fc2e8e610ddac69f81f0ae47904b` and its complete contents read back
equal to the reviewed local source before execution. It has 10977 bytes and
SHA-256 `f555b53e5647e17da978568ebc2d495a4c286ba2445bd35487aa067218523c6e`.
The subsequent Linux x86_64/Python 3.12.15 run exited zero with empty stderr;
the exact 714-byte output has SHA-256
`9e2865bc0ef5392c2cb80ee3519b7e2702cf43f14c6c87e6426c5c52b32678b2`.
The reproduction README records its environment and custody.

## Boundaries preserved

The twenty-valued context is sufficient for evaluation only; no minimum-size
claim is made. Its exhibited successor ambiguity excludes an autonomous
update using only that particular context, not an implementation supplied
with additional state or input. Recognizing the initial readiness period is
a separate task. PRESENT(0), BLANK and absence remain distinct concepts.

Five present residue values plus absence do not fit the at-most-five
observable source classes. An enlarged preparation must add information
actually reaching the declared reader. Reserving a class alone supplies no
persistent absence implementation or repeated-write mechanism.

The factor 2^n dresses a recovered payload only for n>=3, where payload is
defined. It selects no physical J law. The ring no-go requires the recurrence
through the early collision and does not claim an arbitrary delayed-only
obstruction. Larger receiver and other preparation-family results retain
their original scopes. No native reader implementation, physical instrument,
source clearing, occurrence law, reset, occupied-record continuation or
cross-layer lift is established.

## Release integrity

The new registry and evidence rows are appended with INLINE_CANON scope
hashes. All 510 previous claim rows, the statuses and decisions of all 26
H/O owners, all gate contracts and scheduler rows are retained. Four T claims
give 514 total claims and 371 T; one supplementary reproduction gives 36
directories. The architecture graph remains at 200 direct architecture
dependents and 70 terminals, with 361 transitive dependents.

The release-accounting reproduction adds a reversible layer that validates
the complete current inputs, reconstructs the exact thirteen v100 files,
and then runs all 153 historical predicates unchanged. Five new guards bind
the additional proofs, ledger rows, source files and inventory. This is
release integrity checking, not a replacement of mathematical evidence or
a relaxation of a historical scientific threshold.

Before its first execution, the updated accounting source was publicly
stored as Git blob `0b9b39e882d36fae214a4f2078b104c96eba73f4` and read back
byte-identically. Its SHA-256 is
`de57d64369d091709e890cdfb2a3c14f451e8ed49407dcf7a7d2f61f28dc1292`.
The Linux x86_64/Python 3.12.15 execution passed all 158 guards with zero
exit status and empty stderr. Its 25884-byte output exactly matches
EXPECTED.txt, SHA-256
`28d08ebb1913413af4ec7232ec418cf82da514ca4098a3b223a591a632ca7191`.

The release follows the existing two-commit form: complete content, then
exactly STATUS.md, README.md and CITATION.cff. Required repository, full
scientific replay, both architecture checks, immutable tag and publication
readback retain their ordinary acceptance conditions. The live authority
remains v100 until those activation conditions are fulfilled.
