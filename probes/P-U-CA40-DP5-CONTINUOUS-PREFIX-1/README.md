# Short continuous-prefix DP5/RK4 comparison

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Apache-2.0, A. M. Thorn, 2026-10-12.
Reservation: https://github.com/mathorn1973/twist-j/issues/1470.
Authority base: `200ebb118bc62b02c634afa9e68bd91a7de3191b`.

The preceding DP5/N384 study improved local bounds and measured speed,
but reset its state between four separated windows. This new probe tests
accumulation along four consecutive blocks with no state or certificate
reset. Pulse input, compensated parent, seven modes, L8/G10, all 120
retained thermal columns, both angles and 80 AVX-512 workers stay fixed.

| Arm | Cells per original segment | Cells / substeps / RHS per checkpoint block | Total cells / substeps |
|---|---:|---:|---:|
| A: inherited RK4 | 512 | 4 / 4 / 36 | 16 / 16 |
| C: two DP5 halfsteps per cell | 384 | 3 / 6 / 39 | 12 / 24 |

Each block is exactly 48.828125 ns; the tested active prefix is
195.3125 ns. Initialize each case/thermal trajectory once at its first
occupied cell, carry the same state and accumulated defect certificate,
and record four checkpoints. All preceding inactive segments have exactly
zero coupling in the model, so this is a prefix of the actual declared
initial-value problem. It is not a fresh seed inserted into an evolved
nonlinear state. Polynomial endpoint jumps and all intermediate defects
remain in the cumulative account.

The first active time is 100 us for labels (4,3)/(4,4) and 400 us for
(1,1), for each sign. Compare A/C at matching case-specific absolute times.
These endpoints are not simultaneous across cases; no intercase coherence
or full thermal state is inferred. The inherited full-program linear
endpoint fields must not be substituted for prefix endpoints.

The unchanged DP5 step uses the Hairer-Wanner
[DOPRI5 coefficient table](https://www.unige.ch/~hairer/prog/nonstiff/dopri5.f)
and the predecessor's original three-point quintic Hermite curve. Formal
order alone is not an error certificate. DERIVATION.md explains the
unitary additive defect bound; EXACT-DESIGN.md describes its exact support
and the separate role of the numerical program.

Freeze A,C,C,A, two observations per arm, with 300 seconds per child,
90 seconds per comparison and 1200 seconds for the campaign. No pilot,
retry, adaptive extension, discarded warmup or pulse retuning is allowed.
Runtime checks cover single initialization, exact checkpoint continuity,
polynomial starts, cumulative accounting, 80-worker placement and custody.

Joint local engineering success requires all 2880 checkpoint columns in
both pairs to have compatible directed endpoint enclosures and e_C<=e_A,
byte-identical same-arm repeats, intact continuity/custody and a strictly
smaller two-observation program end-to-end time for C. Report each bound's
growth through the four checkpoints without a fitted growth law. These
are upper-bound ratios, not actual-error or infidelity measurements.

After pinning all fifteen sources and their manifest publicly and reading
them back byte for byte, run the exact support gate:

```sh
python3 probes/P-U-CA40-DP5-CONTINUOUS-PREFIX-1/verify.py
```

The separate bounded numerical runner takes three executables built from
the public pin and a new output directory:

```sh
python3 integrator_run.py --baseline /absolute/path/baseline \
  --candidate /absolute/path/candidate --comparator /absolute/path/compare \
  --output /absolute/path/new-directory
```

First outcomes are retained, including negative or incomplete ones. Exact
CI replay does not rerun the floating solver. Successful runtime enclosures
certify only the declared prefix columns/checkpoints conditionally on the model;
complete-pulse error, final coherences, complete-source preservation and
physical realization remain open. No long run or automatic successor.
