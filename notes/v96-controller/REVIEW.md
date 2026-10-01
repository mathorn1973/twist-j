# Independent source review and arithmetic bounds

NON-CANONICAL / STATIC review with separately attributed SOFTWARE/SIMULATION
receipts. Date: 2026-10-01. No physical qualification or HIL result.

The reviewer did not author runtime.py, law.v, controller.v or their tests.
It read those sources against the complete #1316 definitions, #1318's
encoding and calendar, and the pinned scalar reference used by the tests.
The mathematical targets and both old implementations were exposed. This
is a separate adversarial source review, not clean-room development or
independent discovery of the law. The reviewer changed only this review.

## Scope and correspondence

The digital arithmetic supports 2<=N<=16 on the H_N=41 shell, with a
separate physical p in {0,1,2,3,4}; its concrete apparatus target is N=3.
It is not an implementation of every unbounded integer input of Xhat_N.
The mathematical theorem remains broader than this finite implementation.

For every valid input, the source structure matches the fixed law:

* Both R and AM use literal equality of all twelve ordered reacting
  coordinates. Spectators remain in the output and in the energy account.
* The four exact split numerators are checked for divisibility by five.
  R additionally tests every coordinate of Vinv*y before its division by
  five. AM uses its low active coordinate directly. Negative exact multiples
  are safe under either Python floor division or Verilog truncation.
* Runtime `2*quadratic(H,low)` is 4H(low), since the displayed matrix
  quadratic is twice the active energy. RTL `4*hform` is the same quantity.
  Funding rejection retains all old coordinates and does not increment p.
* Field reconstruction retains the exact static coordinates. Forward F
  applies the electric shear before the magnetic shear; inverse F recovers
  the old magnetic vector before the old electric vector.
* A and B exchange complete old values on disjoint supports, including
  occupied channels and cell resources. Fixed cuts suppress both contacts
  without clearing the channel.
* At the target, accepted R increments p only in forward mode; accepted AM
  decrements it only in inverse mode. This equals subtraction of e(Gc') in
  the recovered-input inverse, not applying the forward writer twice.

Within the stated parameter and input domain, these are structural
correspondence arguments over every input, not extrapolation from a finite
vector sample. They depend on exact arithmetic and the width argument below.
They do not establish device convergence, measurement correctness, pointer
mechanics, or the physical truth of a healthy interface signal.

## Bounds before narrowing

Both implementations check the #1318 box before multiplying incoming words:
matter/spectator components |v|<=6; field component bounds
(15,9,11,11,12,18); nonnegative resource/channel bounds 41. They also
require the full energy sum 41, so the box alone never admits a state.

The bounds cover the complete shell. From Q(v)>=||v||^2, each matter
component has absolute value at most floor(sqrt(41))=6. Put
u=2E+CM, a=M0, b=M0+M1. Then

```text
||u||^2+a^2+b^2<=164,
2E0=u0-2a+b, 2E1=u1+a,
2E2=u2+a-b, 2E3=u3+a-b.
```

Cauchy-Schwarz gives |E0|<=floor(sqrt(6*164)/2)=15,
|E1|<=floor(sqrt(2*164)/2)=9,
|E2|,|E3|<=floor(sqrt(3*164)/2)=11,
|M0|<=12 and |M1|=|b-a|<=floor(sqrt(2*164))=18.
Nonnegative resources are each at most 41.

Conservative bounds also cover invalid energy sums that are still inside
the checked box, before the shell test rejects them:

| Quantity | Absolute upper bound and reason |
| --- | --- |
| One four-coordinate Q expression | 1584 = 44*6^2, where 44 is the sum of absolute K entries |
| Six matter/spectator Q expressions per cell | 9504 |
| Raw field energy expression | 1970 = 15^2+9^2+11^2+11^2+12^2+18^2+15*(12+18)+9*12+(11+11)*18 |
| Cell contribution including resource | 11515 |
| Full validation accumulator, N<=16 | 184855 = 16*11515+15*41, less than 2^18 |
| Integral split (a,b,u,v) | (15,13,14,15) in absolute value |
| R-side Vinv*y numerators | (89,85,131,248) |
| R-side divided low coordinates | (17,17,26,49), including harmless truncated rejected-image candidates |
| AM-side L*y coordinates | (102,139,113,182) |
| R-side hform expression | 9758 by summing its absolute monomial bounds |
| R-side candidate resource before rejection | 39075 = 41+4*9758+2 |
| AM-side hform expression | 3303 |
| AM-side candidate resource before rejection | 13255 = 41+4*3303+2 |
| Reconstructed raw coordinate | At most 255 under these coarse pre-acceptance bounds |
| Forward F intermediate field bounds | E' <= (45,21,29,29), M' <= (78,121) componentwise in absolute value |
| Inverse F intermediate field bounds | recovered M <= (36,55), recovered E <= (106,45,66,66) |

All arithmetic-core products, partial sums and accumulations are far inside
signed 64-bit range. In particular a rejected image candidate may be divided
and inspected in RTL, but its accept flag remains false and nothing is
written. There is no overflowing product before the input box guard.

After acceptance, mathematical energy conservation returns the output to
the same H_N=41 shell. The proven shell bounds therefore justify narrowing
every committed state coordinate back to signed 16 bits. A coarse candidate
resource bound above 32767 is not a narrowing permission: rejected candidates
are never committed, and accepted ones have resource <=41. The Python
runtime additionally validates the output; the RTL relies on this exact
accepted-law argument. WORDS is derived from N as a local parameter, avoiding
an inconsistent separately configurable stored dimension.

The controller's tick arithmetic is a separate domain: the start guard
requires a ticks-per-second multiple of ten in [100,1000000000]. The largest
displayed intermediate product is 22*1000000000, far below 2^64. The
MACROSTEPS and TURNAROUND_AT parameter guards keep the campaign counter
inside the declared 1..20-step run and permit a fixed midpoint reversal.
These parameter checks are not oscillator calibration or placed timing.

## Adversarial findings and repairs reviewed

| Finding in the initial implementation | Disposition observed in current source |
| --- | --- |
| Overridable WORDS could disagree with N and omit stored words | WORDS is now derived locally; port dimension uses 32N-1 directly |
| Invalid physical p in `plan` left the Python controller READY | Validation failure now enters absorbing ERROR |
| Boolean/float pointer and cut values could compare equal to valid integers | Exact types and ranges checked at confirmation |
| BREAK could ignore pointer change or stale completion | Input p retained; BREAK requires unchanged valid p and operation_done false |
| Operation completion and the final calibrated window were conflated | Separate break/execute/settle phases and operation deadline; Python commit at slot end |
| RTL committed before the complete final 100 ms read window passed | Pending state now remains uncommitted until the fixed slot end; whole window checked |
| Host restarts inserted variable gaps between macrosteps | RTL now advances continuously through fixed MACROSTEPS with optional fixed TURNAROUND_AT |
| Unbounded tick parameter could overflow products | Explicit supported upper bound added |
| Within-operation voltage interlock was missing | Independent voltage_ok input monitored while busy |
| Finite law suite lacked higher-h underfunded and ordered-permutation controls | Added targeted rejection cases; tests remain finite audit, not exhaustive S42 proof |

The current source retains stale digital words after a partial physical
failure but invalidates the state, disables actuation and enters ERROR.
Those words are not a physical rollback. Starting another trial requires
the surrounding acquisition/custody system to preserve the failed attempt;
the controller alone does not maintain that evidence roster.

## Verification receipts and their limits

The coordinator reported actual Icarus Verilog 11.0 law simulation with
10948 finite vectors, including the added rejection controls. The last
complete integration replay after all edits remains the coordinator's
responsibility; this review does not relabel an earlier run as a final-head
run. `rtl_vectors.py` obtains expected transitions from the separately
hash-pinned #1316 scalar challenger, not from runtime.py or law.v.
Some fixture selection uses the new constants; that exposure is explicit
and does not turn the vectors into an exhaustive independent carrier census.

The coordinator also reported this actual Icarus 11.0 supervisor receipt:

```text
SIMULATION controller 200s roundtrip +12 fault cases PASS; no HIL
```

The originally inspected controller_tb.v covered a simulated 10-step forward
then 10-step inverse block, continuous 200000 ticks at the deliberately
scaled 1000-tick-per-second test parameter, 80 layer completions, complete
95-register return and p=0. The twelve cases inject ADC, samples, dock,
reserve, both cut inputs, operation timeout, invalid pointer, missing
confirmation, voltage, energy-bound and stale-completion faults, with
absorbing-ERROR checks. This does not test every combination or every
campaign preparation, and it does not use a calibrated physical clock.

### Final coordinator replay after review

The coordinator subsequently extended the testbench to check both inverse
orders and actually ran the complete `check.py` entry point on Ubuntu 22.04 /
WSL2 x86_64, CPython 3.10.12 and Icarus 11.0. Exit status was 0: all six
software tests, all 10,948 reference vectors, both continuous 200 s roundtrips
and the twelve fault cases passed. Each roundtrip completes 80 layer
operations in 200,000 simulated ticks and returns all 96 coordinates.
This receipt is the coordinator's integration execution, separate from the
reviewer's static inspection. The tested core and testbench hashes are:

| Source | SHA-256 |
| --- | --- |
| runtime.py | bffeb8142384bcfc77610ff34ffc3a1ec5e17c33075c5d6f1de05e320074dbf5 |
| law.v | 6828a3990064ed5985b3f0cfaefe62c43e4b7d7c63d670afa881a7cc4e7b221c |
| controller.v | 2d5cbc360bed02e3b4e7ada9d61e13e984cc0cc13e63df7840097903be3fc538 |
| controller_tb.v | 99435096db99f91f890c1e8108d906f34f28923ec21cbe3041a6a67d06533a97 |

The separate C03 reviewer then checked this final testbench and `check.py`:
scenario 0 covers forward/inverse, scenario 13 covers inverse/forward, and
scenarios 1..12 cover the stated faults. It verified the quoted current
hashes, counts, output-path guard and subprocess failure handling. No
regression was found; this was a final static check of the integration delta.

The reviewer performed source inspection only for C03; it did not independently
rerun Icarus or fabricate synthesis/timing output. Generic synthesis, placed
resource/timing reports, I/O assignments, instrument drivers, independent
measurement acknowledgements and physical interlocks retain their separately
reported or unfinished scopes. No assertion here is a hardware PASS.

## Disposition

No remaining blocking arithmetic or supervisor-logic defect was found in the
reviewed supported domain after the listed repairs. The mathematical
correspondence and width proof support a source-level exact implementation
claim for the selected shell, subject to ordinary compiler/RTL/toolchain
correctness. Finite software/simulation results are separate evidence.
Fabrication readiness, placed clock closure, qualified instruments, analog
budget convergence, physical swaps/wheel and actual HIL remain open. Their
absence must stay visible in any C03 result or fold proposal.
