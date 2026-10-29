# Small reversible adders for all finite J digit carriers

**NON-CANONICAL, L1 conditional construction.** Reservation #1818.

The generic finite carry compiler is now replaced by a coefficient circuit.
It stores four bounded carry coefficients and computes their next values
using reversible base-five adders of widths three and four. Every helper
is explicitly returned to zero. The new compiler does not use a large
carry-transition table as an input.

`PROOF.md` gives the all-N construction and its resource account.
`PREREG.md` fixes the finite audit and all failure conditions before the first
public run. `arithmetic_compiler.py` generates the complete coefficient
program and can expand it to the existing phase-exact physical primitives.
`verify.py` checks the pinned old independent representations, the new
small adders, carry transitions, complete finite multipliers and archives.
Subsequent `EXPECTED.txt`, `RUN.md` and `RESULT.md` record the first run.

The preceding frozen construction is in
[`notes/C-J-LAMBDA-CARRY-N`](../../notes/C-J-LAMBDA-CARRY-N/README.md).
Its already known local runs are disclosed preparation. They are not
retroactively described as prospective public evidence.

## Reproduction

From the repository root:

```bash
python3 probes/P-J-LAMBDA-CARRY-ARITHMETIC-1/verify.py
```

For a concrete program, for example N=8:

```bash
python3 probes/P-J-LAMBDA-CARRY-ARITHMETIC-1/arithmetic_compiler.py --length 8
```

`--pulses` expands each operation down to individual physical primitives;
the resulting output can be large. The frozen verification uses exact
primitive matrices and exhaustive small block laws, then checks large
programs compositionally. It does not simulate every quantum amplitude
of every pulse of a large device.

## Scope

The proposed pair-pulse bound is `136917 N` per multiplication, with
`14N+22` five-level cells for data and work, or `15N+22` including the
archive. These are bounds for the stated concrete supplied-control model.
Clock/program hardware, routing, clean-source preparation, energy/work and
protection from physical gate errors are separate resources.

No native-U realization, J-selection principle, physical occurrence law,
L1-to-L6 lift, canonical promotion or status change is asserted.
Required repository CI and mathematical review have distinct roles.

Copyright 2026 A. M. Thorn. Apache-2.0, under the repository license.
