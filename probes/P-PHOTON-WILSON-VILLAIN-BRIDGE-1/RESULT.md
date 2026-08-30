# P-PHOTON-WILSON-VILLAIN-BRIDGE-1 result

Status: **candidate-T / L4 / FINITE-COUPLING-NONMEMBER / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable public verifier exited zero,
wrote empty stderr, and produced the exact committed `EXPECTED.txt` bytes.
All 13 frozen gates passed. No scientific falsifier fired and no family,
endpoint, bridge operation, or outcome predicate moved.

## Result

For `phi=(1+sqrt(5))/2`, the public one-face datum and its unnormalised
`Z_5` Fourier transform are exactly

```text
w  = (4,phi^2,phi^-2,phi^-2,phi^2),
Fw = (10,5,0,0,5).
```

Consequently its unordered bi-support invariant is

```text
Sigma(w) = sort(|supp w|, |supp Fw|) = (3,5).
```

For every finite Wilson coupling `beta>0`, both `W_beta` and `F W_beta` have
full support, so `Sigma(W_beta)=(5,5)`. At the admitted endpoint `beta=0`,

```text
Sigma(W_0) = (1,5).
```

For every finite Villain parameter `t>0`, both its character coefficients and
its position vector are strictly positive, so

```text
Sigma(V_t) = (5,5).
```

Positive normalization and each `Z_5` automorphism preserve both support
sizes, while optional Fourier exchange only swaps them. Therefore no element
of the exactly frozen orbit

```text
O(f) = {c P_u F^epsilon f : c>0, u in F_5^x, epsilon in {0,1}}
```

of any finite-coupling Wilson or Villain vector equals `w`.

## Proof and audit split

The universal proof in `PREREG.md` derives Wilson positivity from the
absolutely convergent two-exponential residue series. It derives the exact
Villain position formula from the Gaussian Fourier transform and Poisson
periodisation, including convergence and the zero boundary term. It then
uses the support-pair invariant to cover every finite parameter and every
allowed bridge word.

The verifier exactly audits the `Q(sqrt(5))` Fourier arithmetic, support
pairs, automorphism and Fourier actions, positive-term residue witnesses,
endpoint control, mutation control, and deterministic transcript. It is not
the source of the analytic universal quantifiers.

## Status ceiling and rejected interpretation

This result proves direct finite-coupling nonmembership only. It closes the
literal equality route from the displayed Wilson and Villain families under
the displayed finite operation class. It does not turn failure of an
auxiliary lemma into a false membership claim: `FINITE-COUPLING-MEMBER` would
require an exact admitted equality, as frozen by issue #692 and its public
correction.

The written proof supports a later public row

```text
PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP [T], L4
```

after required pull-request integrity checks and only through a separate
sealed Canon fold. Public Canon v71 is unchanged by this probe.

## Scope firewall

The theorem excludes neither a broader action class nor a limit point. It
proves no domination, comparison, blocking, RG, universality, or
Fröhlich-Spencer bridge.

It establishes no Gibbs measure, thermodynamic limit, roughening, Coulomb or
massless phase, massless pole, propagator, continuum limit, polarization,
apparatus, physical readout, or photon. It performs no L4-to-L6 lift and does
not complete `PHOTON-MASSLESS-PHASE`; those remain separate obligations.

## Pin and local run

```text
public claim issue:       #692
public outcome correction: issue comment 5469082766
preregistration pin:      05bc49339fb87aedef19ebb465251872c87265b5
verifier sha256:          30af41ce20eb122405b130a8cb21bd4d55e1b0b53a749f57f655241179e19cc8
local architecture:       x86_64
local exit:               0
local stderr bytes:       0
local stdout bytes:       798
local stdout sha256:      3f7e5bd8ce69cb9f01bfc1826c7e38ab3ab56a245b8d1b41b0907c71e4c5b01d
```

The local run is one architecture lane only. The proposed theorem status is
proof-first; the pull-request workflow remains the required repository
integrity and independent two-architecture audit.
