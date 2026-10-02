# Exact internal-control audit

**PUBLIC, NON-CANONICAL. Conditional L1 mathematics; no actual outcome,
native realization, physical clock/work law or empirical result.**
Original work by A. M. Thorn / control_builder, Apache-2.0.

The complete specification and occurrence-boundary annex were publicly
frozen and read back at
`e5ff31fd7296df4bf740fd27c1ac3de14b5c8148` before this program was written:

| File | Bytes | SHA-256 |
|---|---:|---|
| notes/C-FIELD-J-INTERNAL-CONTROL-N/PREREG.md | 42875 | `ebc473f087158e382fbf4864b4f20676848b1c04821dbaafba53adfffd3ea40f` |
| notes/C-FIELD-J-INTERNAL-CONTROL-N/OCCURRENCE_INTERFACE.md | 11565 | `64277d3cd9389584e8a32ec0d7d80589c9f83d46a2b466c2464a7ee83777ae91` |

The accepted receiving pins are Stage C
`024936502544c2ec45acc8890a052c7b3aca26be` and approximate preparation P
`1f88665ce8646cdf134cb4366958db0ca2d302d7`. The earlier one-head classical
construction at `fd792d32b3efa90c15a46e065d6637ac8600cdcf` is credited in
PREREG; it is not rediscovered here. These are proof/background sources,
not runtime dependencies. No predecessor or independent verifier is
imported, copied or executed by this program.

The coordinator is a disclosed author-side proof/specification coauthor.
An attempted author proof-helper spawn failed at the concurrency limit;
no such helper contribution occurred. The coordinator writes PROOF.md
while control_builder writes this program and README. Neither author-side
contribution is the fresh independent review. The reviewer receives only
the publicly frozen specification and admitted old sources before its own
proof/program freeze and first run; no new reviewer source or output has
been used to write this implementation.

Before either scientific program ran, the fresh reviewer identified a
paper-level overstatement in PREREG section 8: repeated-context changing
parity words remain exactly forbidden on the declared even-supported
D=I domain, despite approximate within-HIGH coherence. The coordinator
records the public correction in PROOF section 10a and issue #1333
[comment 5947804711](https://github.com/mathorn1973/twist-j/issues/1333#issuecomment-5947804711).
That disclosed paper finding is known to this author; no reviewer proof
file, checker or execution output was exposed. The immutable specification,
operational law, audit input domains and error threshold are unchanged.
The general preparation error allowance is not an assertion that every
ideal-zero branch becomes positive in this particular device.

## Execution and evidence custody

Before the first scientific execution, the coordinator must commit and
push the complete author proof, unchanged specification/annex, verify.py
and README, and read back their exact public blobs. Static AST parsing is
allowed beforehand; importing this module or running any of its functions
is not. This README records no execution result or anticipated PASS.

From that exact clean pin, the registered command is:

```text
python3 reproduce/C-FIELD-J-INTERNAL-CONTROL-N/verify.py
```

The deterministic environment is LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. The first-run limit is
120 seconds. Success requires exact assertions, exit zero and empty
stderr. There is no floating-point tolerance, randomness, fitted threshold,
runtime input file, network access or generated fixture. The only imports
are fractions.Fraction and itertools.product from the standard library.

Actual stdout must be captured after execution as EXPECTED.txt, with
RUN.md recording the full public source pin, command, environment, exit,
byte counts, hashes and runtime. No expected output is invented here.
A failed first execution is preserved under the repository procedure;
frozen scientific sources are not silently repaired or rerun. The fresh
independent audit runs first, before author-source release to its reviewer.

Existing unchanged repository CI must actually replay this exact program
against its own captured EXPECTED on x86_64 and aarch64 before the
two-architecture gate is claimed. Green document checks alone do not
establish that gate. Later RESULT records must cite the actual tested
commit and decoded reproduction entries.

## What the program represents

A sparse vector key contains the complete packet bank, latch, pointer
bank, flags, metadata, fresh/spent baths, immutable program, immutable
descriptor, all eleven head-position/control fields, all eight operand
buses and a reference label. Packet tuples keep their presence, field and
reserve even when inactive. Program and data banks are tuples representing
their separate tensor factors; no logical register is discarded by that
storage convention. Amplitudes are exact integers/Fractions.

`station`, `step` and `tour` implement the actual stationary local rule:
program fetch by local pc comparison; PRE; typed addressed GET swaps;
decoded processor gate; reverse PUT swaps; POST; unfetch; pc advance.
The all-state inverse moves the head back and applies the adjoint of the
actual old station gate. It does not rerun a clean-input recipe.

The direct expected-side functions `reference_command`,
`reference_counter`, `reference_gate` and `reference_receiver` are a
separately expressed logical target law. They access the named logical
operands directly and contain no port traversal, selector or bus-routing
call. The actual side must reach the same full output by its fetched
command and stored cursors. Collision reflection columns on the actual
side are compared with independently expressed Q/J bath blocks on the
reference side. Context columns use a binary-character sign formula
versus the literal registered Hadamard table. The test thus does not
compare two calls to the same routing implementation.

`tour` coalesces only stations whose complete data gate is proved identity
from the common classical controls. It visits and checks every station
index, verifies common controls at entry and after every active station,
performs the exact intervening head translations, executes every selected
local gate and counts every tick. The final identity
microticks = active_stations + proved_identity_stations is asserted.
No active address or processor is skipped, and this optimization is not
an endpoint lookup. The separate microstep audit uses literal single F
and F-inverse calls at every registered station without coalescing.

During the C/read portion, every bath port is checked unselected. Every
executed basis transition is also checked to retain the complete bath
tuple. This is an all-microtick identity claim on bath memory, stronger
than restoration of a reduced bath marginal at the end.

Full source matrix units use exact factored dyads: equality of the complete
output column for source i and source j certifies the complete operator
image |output_i><output_j|, including all reference and bath cross terms.
No dense matrix with exponentially repeated entries needs to be allocated.
Additional correlated vectors explicitly exercise off-diagonal source,
bus and reference blocks. The ideal-history calculation separately checks
each output matrix coefficient of every source matrix unit.

## Frozen finite domains

The implementation follows PREREG section 9 without an output-dependent
domain choice.

* The compiler enumerates 180 labeled descriptors at actual L=613:
  N=2,3,4; K=0,1,2,3; h=0,...,K; all-zero, all-one or alternating n_i;
  W=1,2; contexts t mod2. It constructs actual words, descriptor encoding,
  distinct ordered bath addresses, cursor-selected archives, the read
  window, inverse tail and all resource/timing equations. It does not
  execute an enormous sufficient-precision L=613 trajectory.
* The microstep inverse audit uses the four exact parameter tuples in
  PREREG, every rail station and pc, all five fully specified dirty
  fixtures, twelve instruction patterns and both polarities. It checks
  both inverse compositions, exact norm and the complete bare energy on
  every resulting term. Invalid words, dirty scratch, occupied flags,
  exhausted cursors and dirty buses are included.
* The addressed-command audit executes all 6400 registered Cartesian
  cases at actual L=613, plus forty correlated vectors and their factored
  off-diagonal units. It checks the full output and bus restoration,
  including inverse-address recovery and raw exhausted requests.
* The complete measurement audit uses fourteen program/fixture pairs:
  the seven frozen context words with two pointer/bus fixtures at actual
  L=613. Every source basis column is executed through the forward word,
  read window and complete inverse tail, and is compared with the logical
  oracle at every command boundary. All sixteen source units and exact
  invocation/context metadata are retained.
* A separate ideal-C symbolic calculation uses the exact E/O record
  symbols and the same seven context words. It checks all histories and
  all source units against ordered projector products. Repeated-context
  changing-label branches vanish there; changed contexts retain ordered
  post-state dependence. This ideal comparison is not substituted for
  the actual n_i=0 basis-pointer device.
* Four labeled L=3 loader/program analogues execute every one of their
  three collisions, keep all bath amplitudes, and compare their full
  internal/external maps and inverse. All source columns, the registered
  correlated reference vector and the three separate negative-domain
  variants are included. These toy shifts (1,0,2,4) modulo six are not
  C's physical comparison code. They audit composition without asserting
  a new small-L readiness classification or extrapolating P's rate.

All fixtures, packet-field definitions, bus values, argument overrides
and reference-vector coefficients are literal implementations of the
frozen specification. Counts printed by the program describe these
registered loops; their actual output and hash are recorded only after
the first public pinned run.

## Limit of the evidence

Finite audits supplement the universal proof. They cannot by themselves
prove the countable-carrier inverse, all-reference complete-map equality,
uniform approximation bound or graph locality. The proof must establish
those claims with their fixed domains. The exact control comparison
sets epsilon_control to zero only as an operator theorem.

The inherited pointer-loading error remains epsilon_prep, charged once
for the bank against the actual retained remainder. Exact phase/pulse
and context gates, fresh bath purity, initialized program/controller,
source code and the declared port graph remain supplied. The buses need
not be fresh or pure because their entire joint state is restored at
completed commands. Physical timing, drive work, source renewal and
initial program origin are not derived.

The density evolves coherently through its formal records. No target
outcome tape, random sampler, actual-record selection map or independent
occurrence measure is supplied. epsilon_occurrence remains undefined.
The inverse tail returns the complete **unmeasured** joint state; it does
not undo an external measurement whose apparatus has been discarded.
Public Canon v96 and all three QDD physical obligations remain unchanged.
