# Exact arithmetic and timed physical-commit supervisor

NON-CANONICAL / SOFTWARE + SIMULATION development candidate, 2026-10-01.
Target: #1316 at312d0a90b24d5f9e743096f0ee2a477cda719a10;
device contract: #1318 at4756a3df650b91fb1d30806b0fb2aaac00e50cc2.
No source pin, law, tolerance or workflow is changed. This is not a bitstream,
an Arty qualification, or a MEASURED result.

`runtime.py` is a matrix implementation of every layer on the H_N=41 shell,
N=2..16. `law.v` is its signed scalar RTL counterpart with the same domain.
N=3 has exactly95 signed16-bit stored model words, in DESIGN's prescribed
order; physical p is a separate validated input. Both recognize the complete
ordered matter triples, retain all spectators/static fields, reject failed
split/image/funding guards, swap occupied channels, and implement both F
directions and recovered-input Ghat inverse. They contain no experiment
trajectory lookup table. State checking precedes nonlinear arithmetic.
The pointer-only reader has no time/configuration argument.

The mathematical case for all valid inputs is the structural equivalence and
width argument in REVIEW.md. Tests are finite audits. The independent pinned
scalar challenger supplies expected transitions; test construction also uses
the new matrix constants and is not claimed independently sampled. Shared
logical h=0..4/p tests are disclosed. The designated w=(0,0,0,1) is not used
for end-to-end trajectory tuning in this development fixture.

## Physical transaction and clock

`controller.v` stores preparation only after independent completion flags,
then executes fixed G;A;B;F or reversed F;B;A;G slots. It freezes direction
and both-contact cut masks at start. At100MHz each macrostep has exactly
one billion clock ticks. Defaults are10 forward macrosteps; set
MACROSTEPS=20, TURNAROUND_AT=10 for either200s inverse block and select its
initial direction with inverse_mode. No host call or log controls the
intermediate inverse or inserts inter-step pauses. N and timing parameters
are bounded. Calibration of the physical oscillator remains an assumption.

The supervisor latches a proposal, observes both terminals disconnected,
enables physical execution, demands a fresh operation_done before the
1.7s/2.2s/2.2s/0.1s deadline, monitors voltage/ADC/missing-sample/dock/reserve
and physical-cut interlocks, waits until the fixed final100ms read interval,
requires valid feedback throughout that interval, and commits only at its
end. The physical executor must advance the wheel only after completed
accepted receiving work; desired_p is a request, never an observed pointer.
The controller never commits a mismatched physical pointer. A partial
failure disables actuation, invalidates the stored state and latches ERROR
until reset. Old register bytes retained in ERROR are stale, not rollback.

`runtime.Controller` is the corresponding per-layer software protocol:
BREAK acknowledgment, fresh EXECUTING completion, then SETTLE confirmation
at the fixed slot boundary. It verifies timestamps/word types, cut masks,
original p before connection and final p before commit. Whole-window sample
completeness is an acquisition obligation, not inferred from one reading.
The continuous hardware calendar lives in the RTL supervisor.

**Integration boundary:** flags must come from separately calibrated physical
interfaces, not from a host assertion or the mathematical model. No real
ADC, dock-ID, wheel-actuator, relay, or reserve-verifier binding is supplied
by this module. In particular the executor must inhibit wheel motion until
accepted bank work completes and independently enforce safe switching. The
generic RTL has no reviewed Arty pin constraints or placed timing result.
These omissions block connection to apparatus and any full digital/analog
implementation claim; they do not turn simulated feedback into a measurement.

## Reproduction

Only Python standard library and Icarus Verilog are needed for tests. Actual
development environments: CPython3.12.10 on Windows x86_64; CPython3.10.12 on
Ubuntu22.04/WSL2 x86_64; Icarus11.0 (Ubuntu package11.0-1.1). Generated
vectors and vvp binaries must remain outside the repository.

```sh
python3 -B notes/v96-controller/check.py --output /tmp/twistj-v96-controller
```

If the tool is unpacked rather than installed, add
`--tool-root /absolute/path/to/extracted` (the prefix containing usr/bin and
usr/lib/x86_64-linux-gnu/ivl). No installation or network operation is done by
the checker. The underlying simulator commands are:

```sh
python3 -B notes/v96-controller/rtl_vectors.py /tmp/v96-vectors.txt
iverilog -g2012 -s law_tb -o /tmp/v96-law.vvp notes/v96-controller/law.v notes/v96-controller/law_tb.v
vvp /tmp/v96-law.vvp +vectors=/tmp/v96-vectors.txt
iverilog -g2012 -s controller_tb -o /tmp/v96-controller.vvp notes/v96-controller/law.v notes/v96-controller/controller.v notes/v96-controller/controller_tb.v
vvp /tmp/v96-controller.vvp
```

Actual current results:6 software tests;10,948 independent-reference layer
vectors; both continuous200s logical roundtrips and12 injected fault cases
pass. Faults include ADC saturation/health, missing samples, dock identity,
reserve, each physical cut contact, deadline, invalid physical p, missing
window confirmation, voltage, energy acceptance and stale completion.
The clock test checks200,000 ticks at simulated1kHz with80 completed layer
operations, followed by exact96-coordinate return. This accelerates time
only in the simulator, not in the proposed physical100MHz build.

Synthesis/resource disposition is recorded separately in SYNTHESIS.md.
These notes-only tests are not automatically executed by the unchanged
repository CI. A green repository check is not an HDL or apparatus result.
