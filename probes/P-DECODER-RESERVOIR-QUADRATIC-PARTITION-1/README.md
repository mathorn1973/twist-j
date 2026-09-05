# Reservoir-induced quadratic partition

**NON-CANONICAL / SOURCE CANDIDATE / PUBLIC STATUS NONE AT PIN.**

This directory defines a new exact L1 probe following the completed
[wave transport](../P-DECODER-RETARDED-ENERGY-TRANSPORT-1/RESULT.md) and
[reservoir coupling](../P-DECODER-RESERVOIR-COUPLING-1/RESULT.md). It does not
change or resume either input probe. The physical mapping proposal is in
[the decoder map](../../notes/DECODER-PHYSICAL-BORN-MAP.md).

Two conditional claims are preregistered:

- `DECODER-RESERVOIR-QUADRATIC-PARTITION`: on the chosen rational source and
  fixed cold finite-port context, every finite horizon yields positive
  deposit forms and an independently defined positive residual form whose
  sum is the exact QDD source metric. Grouped normalized energy shares and
  the rational G-metric trace spelling follow on nonzero sources.
- `DECODER-RESERVOIR-QDD-POSTPROCESSING-OBSTRUCTION`: if the origin is an
  active port and the horizon is positive, no state-independent nonnegative
  complete two-output processing of this energy partition yields the sharp
  algebraic QDD LOW/HIGH pair. Two exact balanced sources already force
  incompatible coefficients for the first origin port.

The first is an energy accounting statement, not an occurrence law. The
second is a boundary for a complete, narrowly defined mathematical processing
class, not a physical Born falsifier or an impossibility result for all
apparatuses. The source norm match and port law are disclosed choices.

## Files and execution

`PROOF.md` gives the uniform argument. `PREREG.md` freezes equations, code,
carrier, systematics, thresholds and L1 scope. `partition.py` constructs
the four-dimensional port/residual matrices using the pinned predecessor.
`audit_partition.py` gives an independently written pointwise wave audit.
`verify.py` enforces immutable dependencies and prints deterministic exact
gate and claim outcomes.

Only after the complete source candidate is committed, pushed and publicly
read back, run from a clean Linux repository root:

```text
python3 probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/verify.py
```

Before that pin, only static inspection and compilation are allowed. After
the initial formal run, `EXPECTED.txt`, `RUN.md` and `RESULT.md` supply its
exact stdout, provenance and earned conclusion. Frozen source documents keep
their pre-execution labels; they must not be rewritten to report later runs.
The ordinary required workflow replays the verifier on x86_64 and aarch64.

## Reading the output

The verifier distinguishes mathematical gate outcomes from physical scope.
Any required scientific assertion failure produces `FIRED` and a completed
exit-zero transcript. An unexpected error or integrity mismatch is not a
scientific counterexample and follows the abandoned-pin policy if no complete
formal record exists. No threshold, witness, implementation or scope is
repaired in place after the pin.

There is no scientific network access, random sampling, external dataset,
floating tolerance or physical measurement. This is repository-authored
standard-library rational code and proof text under the repository license.
Only exact immutable local source files are consumed.

Physical source/clock/context selection, detector realization, records,
post-state instruments, occurrence and L6 measure are not supplied here.
The sibling physical-profile proposal has its own definition scope and is
not a dependency of this verifier. Canon v76 remains unchanged and public
claims remain unregistered until a separate earned fold.
