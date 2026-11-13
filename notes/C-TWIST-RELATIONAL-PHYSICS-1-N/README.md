# C-TWIST-RELATIONAL-PHYSICS-1-N

**NON-CANONICAL candidate.** Author: A. M. Thorn. Apache-2.0.

One finite relational quantum physical model with a fixed stationary state,
the complete public source/contact/occupied-memory apparatus, two explicitly
counted clocks, and a complete clock/pointer observation law.

The candidate makes the physical choice that time is read from a correlated
subsystem. The native integer counter is not silently used as a universal
physical time. States, preparation, energy, readout and calibration are stated
as explicit physical postulates. Mathematical composition is proved separately.

## Main result

The existing 561-level program cursor and 140-gate apparatus have energies
`E_s=E_ctl(2s+1)/561`. Add a distinct 561-level reference clock with energies
`2E_ctl q/561`, pair `q=560-s`, and prepare
`V rho_0 V*`, where `V=sum_s |560-s> tensor P_s`.
The whole is stationary with total energy `1121 E_ctl/561`.
Fourier-clock conditional statistics reproduce the complete apparatus at
`tau_j=pi hbar j/E_ctl`, with every reference correlation retained.

The two prescribed source settings predict a difference for the complete
event **clock 187 through 374 and pointer one** of

```text
delta_joint = (Delta/561) sum_(j=187)^374 B_j > 47/14025.
```

Every other result is retained. A fixed sufficient preparation/effect error
budget gives an actual-model lower bound `1/400`; no achieved precision or
experimental data are claimed.

## Read and reproduce

- [THEORY.md](THEORY.md): physical postulates, state and measurement law,
  interpretation, empirical prediction and applicability.
- [PROOF.md](PROOF.md): analytical construction, all resources, exact window,
  arbitrary mixed/reference scope and measurement boundary.
- [PREREG.md](PREREG.md): fixed six-field contract and exact failure gates.
- [verify.py](verify.py): builder's standard-library exact check.
- [break_check.py](break_check.py): independently written countercheck.
- [BREAK_REVIEW.md](BREAK_REVIEW.md): independent derivation and countercheck scope.
- [PHYSICS_BOUNDARY.md](PHYSICS_BOUNDARY.md): analytic failure of a naive
  common relativistic particle identification; separate from this clock result.
- [SOURCES.json](SOURCES.json): immutable public input pins and hashes.

Run each checker from the repository root with Python 3:

```sh
python3 notes/C-TWIST-RELATIONAL-PHYSICS-1-N/verify.py
python3 notes/C-TWIST-RELATIONAL-PHYSICS-1-N/break_check.py
```

The first execution is allowed only after the contract and both checkers have
been committed, pushed and read back. A later validation record gives the
actual pin and outcomes. This initial package itself asserts no executed run.

## Fixed scope

This is a conditional L1 mathematical construction with a proposed effective
physical interpretation. No Canon or registry status changes. The physical
measurement uses a global energy-shell POVM; its conditional statistics are
not a claim to prepare a free coherent apparatus state after a local read.

The result does not derive the complete apparatus from native `U`, identify
real particles, derive SI units, produce Lorentz or gravitational clock laws,
or make a finite record permanent. It supplies one concrete, falsifiable
physical candidate instead of leaving those identifications implicit.
