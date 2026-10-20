# Autonomous reciprocal integer model with conserved total energy

NON-CANONICAL, L1. Ownership:
https://github.com/mathorn1973/twist-j/issues/1649.

This successor to #1648 closes a specific open obligation: it replaces
the counter-dependent coupling by constant reciprocal coefficients and
constructs an interaction-inclusive, exactly conserved positive
quadratic bond energy on the fixed-mean physical sector.

    (Delta_c^2+L)h_n = chi_n ell/324,
    (Delta_c^2+1)chi_n = a/4 + <ell,h_n>/324,
    ell=(1,-1,0,0,0), a in {-1,0,1}.

Both reduced kinetic terms are positive. The actual coupled equilibrium,
the discrete Legendre map and the energy are derived from the stated
joint quadratic action. The total is conserved for each autonomous step
and its inverse, and under the declared bank/domain reflection.

The 21-integer core has two six-component slices at a common denominator
D, plus an eight-component Hermitian monitor. Its rule is autonomous:

    Z'=BZ-324R+81aD e6, R'=324Z, D'=324D,
    H'=M(Y'-Y) H M(Y'-Y)^dagger.

No additional history counter is stored. Thirteen exact image
divisibilities give the partial inverse. A nonnegative bank and direction
complete a total reversible 23-coordinate map conserving the arithmetic
account E+b separately from the decoded total bond energy.

## Main exact results

- Continuous joint stationarity, including the source, and the full
  metric/lapse/shift variation evaluated on the selected TT representative.
- A conserved interaction-inclusive quadratic energy, positive definite
  about the coupled equilibrium at fixed mean; a canonical discrete map
  with a tangent/equilibrium-centered symplectic invariant.
- All-counter Lorentz signature for the explicitly attenuated thirty
  prepared histories: -1/4<h_n(r)<13/20 and |chi_n|<3/4.
- Joint least-denominator valuation v3(d_n)=4(n-1) for all n>=1,
  despite bounded conserved quadratic energy.
- Genuine continuing reciprocal witnesses, closed three-component
  energy exchange, exact image rejection and funded bounce cycles.

The quarter-amplitude preparation and force a/4 are declared choices.
The all-counter signature theorem does not cover the original
unattenuated family. The denominator valuation concerns all six current
field/source readings jointly.

## Read and reproduce

| File | Purpose |
| --- | --- |
| PREREG.md | Prospective carrier, action, fixtures, falsifiers and certificate |
| PROOF.md | Complete analytical derivation and all-counter scope |
| SOURCE.md | Authority bytes, companion provenance and new modeling choices |
| verify.py | Integer recurrence, polynomial-ring matrix implementation |
| breaker.py | Separate rational evolution and direct-coordinate implementation |
| FROZEN.sha256 | Five-file prospective manifest; itself frozen at the pin |
| EXPECTED.txt | Unmodified first formal stdout, 808 bytes and 29 lines |
| RUN.md | Actual timestamps, environment and prospective custody |
| RESULT.md | Observed finite audit, exact witnesses and earned scope |
| REVIEW.md | Analytical/static roles, checks and predecessor corrections |

From the repository root, Python 3.12 and the standard library suffice:

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 probes/P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1/verify.py

The primary launches the breaker with the same Python executable and
-I and compares all 768 raw certificate bytes. Successful output ends:

    CERTIFICATE_RESULT=PASS
    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

The full 808-byte stdout must match EXPECTED.txt exactly. The unchanged
PR workflow replays on x86_64 and aarch64.

## Limits

This is a selected autonomous linear TT/scalar model on five marked
sites. Nonlinear Einstein equations, nonlinear constraints with matter,
three spatial dimensions, a continuum manifold limit, native-U
realization and experimental interpretation remain open obligations.

The bank is an arithmetic precision budget. Conserved quadratic energy
does not cap exact denominator size. The canonical alternating form is
defined on physical tangent or centered data; the entire bank/monitor
carrier is not claimed symplectic. The bond invariant is not claimed
to generate this map as its own unit continuous Hamiltonian flow.
