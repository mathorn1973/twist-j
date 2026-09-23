# Gaussian-control audit of the frozen photon production design

- **Working item:** C-PHOTON-PRODUCTION-REACHABILITY-N
- **Audited object:** `notes/canon/PHOTON-PRODUCTION-PREREG-FREEZE-1.md`
  ([#757](https://github.com/mathorn1973/twist-j/issues/757), parent #742),
  sections 9, 11, 13 and 15
- **Author:** A. M. Thorn, drafted with AI agent sessions
- **Date:** 22 September 2026; publication review 23 September 2026
- **Scope:** PUBLIC, NON-CANONICAL; no authority. This note does not edit,
  reopen or re-score #757.
- **Scientific ceiling:** candidate-T for the written Gaussian-control bound
  in `REVIEW-ADDENDUM.md`; candidate-C for the supplied engineering data,
  based on one architecture, floating point and seeded Gaussian sampling.
- **Publication owner:** Codex-review-publication-pr1-20260923,
  [#1145](https://github.com/mathorn1973/twist-j/issues/1145).

Public basis: Public Canon v91, main/tag commit
`11b66d4755a697031157f0e10dc1898a7d5b6379`, declared content commit
`b89b0c80bb5cebddade567f31a979aaf42f1d9dd`. The publication coordinator
checked the five normative hashes, ancestry and required architecture checks.
This note does not change that basis or earn a public scientific status.

## Result and scope

The unchanged incubation transcript records:

```text
TERMINAL   DESIGN_POLYAKOV_UNREACHABLE
SECONDARY  CORRELATOR_TARGET_BIAS_HIGH   (max |D| = 0.18426 at L = 24, n = 3)
```

**[candidate-C; NON-CANONICAL]** The first terminal applies to the declared
finite coupling set `B* = {1/2, 3/4, 1, 3/2, 2}`, volumes
`L = 12, 16, 24, 32`, and constant-relative-error WLS family `SE_L = r R_L`.
It is not an impossibility theorem for all real couplings below two or all
production uncertainty profiles. Production #757 obtains its errors from
chain-preserving analysis; that uncertainty model has not been reproduced by
this Gaussian-control audit.

**[candidate-T; NON-CANONICAL]** Separately, the exact second-moment identity
and a lattice maximum-principle argument imply `R_L -> 0` for every fixed
finite positive coupling in this isotropic Gaussian control. Thus a genuinely
positive thermodynamic Polyakov radius is not a necessary property of this
massless control. A positive fitted intercept at finitely many volumes is
compatible with that vanishing true limit.

**[candidate-C; NON-CANONICAL]** The second terminal measures deterministic
target-shape bias. It is not an executed `CORRELATOR_REJECTS_PHOTON` gate.
No TWIST phase, full #757 production terminal, or guarantee against a false
confinement classification follows from either terminal.

The original incubation `PREREG.md`, engineering scripts and transcripts are
retained byte for byte. Its question and systematics contain broader
motivation, including transfer to every Coulomb phase at the same coupling.
Those statements are **not established by the finite audit** and are not
adopted by this note. This publication supplies no public probe pin and
changes no frozen threshold.

## 1. Polyakov radius and finite regressions

The control is the free non-compact Maxwell field on the periodic isotropic
four-dimensional torus of integer side `L >= 3`, with action
`(beta/2) sum_p F_p^2`. Write `beta` for its coupling; the archived table calls
it `beta_R`. No renormalized coupling for the TWIST weight is identified.
With the mean-zero three-dimensional nearest-neighbour Green function `G_L`,

$$
\mathbb E|\bar P|^2=L^{-3}\sum_r
\exp\!\left[-\frac{L}{\beta}\left(G_L(0)-G_L(r)\right)\right].
$$

The full proof in [REVIEW-ADDENDUM.md](REVIEW-ADDENDUM.md) gives

$$
R_L=\mathbb E|\bar P|
\leq\left[L^{-3}+(1-L^{-3})
\exp\!\left(-\frac{L(1-L^{-3})}{6\beta}\right)\right]^{1/2}
\longrightarrow0.
$$

This conclusion holds at fixed finite `beta > 0` when all four dimensions
grow together. It makes no claim for fixed temporal extent, a coupling
growing with `L`, or the compact interacting TWIST measure.

The finite audit uses `y_L = y_inf + a/L` (M1) and
`y_L = y_inf + a/L^2` (M2). The following are **WLS intercepts from the seeded
first-moment estimates under the declared error profile**, rounded from
`STDOUT.txt`. The second-moment identity is exact; its floating-point
implementation, sampled first moments and fitted intercepts are not exact
Maxwell expectation values.

| beta | R_12 | R_32 | M1 intercept | M2 intercept | Both intercepts positive in this profile? |
|---|---|---|---|---|---|
| 1/4 | 0.0216 | 0.00490 | -0.0046 | +0.0022 | no |
| 1/2 | 0.0628 | 0.00494 | -0.0150 | -0.0027 | no |
| 3/4 | 0.155 | 0.00698 | -0.0567 | -0.0158 | no |
| 1 | 0.246 | 0.0200 | -0.1051 | -0.0195 | no |
| 3/2 | 0.393 | 0.0727 | -0.1259 | +0.0193 | no |
| 2 | 0.496 | 0.140 | -0.0814 | +0.0882 | no |
| 3 | 0.627 | 0.270 | +0.0550 | +0.2303 | yes |
| 5 | 0.755 | 0.456 | +0.2868 | +0.4356 | yes |

The couplings `1/4, 3, 5` are supplementary scan points outside `B*`.
Individual intercepts need not both be negative: M2 is positive at `beta=2`.
Scaling every assumed standard error by the same `r` leaves these intercepts
unchanged, but changes their reported interval classification. The transcript
contains the normal and Student-t readings for the preregistered values of
`r`; none is substituted for a production covariance analysis.

The review's exact rational witness uses the rounded `beta=2` means from this
same transcript with `SE=(0.001,0.001,0.05,0.05)`. Both fitted intercepts then
exceed ten times their inverse-information standard errors. This different
error family lies outside the original frozen test and does not fire its
falsifier. It does show why the restricted terminal cannot be generalized to
universal finite-fit unreachability. The script and exact stdout are under
`verification/`; they execute no production or formal public probe.

## 2. Correlator target-shape bias

For this Gaussian control, the lattice ratio differs from the continuum
image target based on `n^-4 + (L-n)^-4`. The computed engineering deviations
`D_L(n) = Q_L(n)/Q4_L(n) - 1` at `beta=1` are:

| L | n | D |
|---|---|---|
| 24 | 3, 4, 5, 6 | +0.18426, +0.16551, +0.10395, +0.06114 |
| 32 | 4, 5, 6, 7, 8 | +0.16425, +0.10210, +0.05877, +0.03538, +0.02332 |

The archived comparison at `beta=1/2` changes these values by less than
`0.001` in these windows. This finite comparison is not exact independence
from the coupling. The maximum in the frozen secondary-terminal domain is
`0.18426`; the `L=16` scan is outside that terminal's maximum.

These discrepancies motivate a successor's target-calibration study.
Translating them into a production classification still requires the frozen
covariance, fit, precision and integrity gates. None of those gates is
executed here.

## 3. Scope of companion diagnostics

The separate `C-PHOTON-PHASE-ORIENTATION-N` note studies finite,
sector-filtered local-heat-bath trajectories. Those are engineering
orientation, not phase evidence for this Gaussian audit or a reproduction of
#757. Sector trapping makes identification with the full equilibrium measure
an additional obligation. Sector conditioning cannot replace the prescribed
full measure without an explicit comparison and controlled error.

## 4. Successor questions, not adopted protocol changes

A successor could test an observable with a controlled infrared limit and
calibrate its finite-size decision rule on both massless and massive
controls. The exact/coexact contrast associated with #1108 and reserved by
#1116 is a possible candidate, but the prescribed joint ordered limit, full
measure and P1/P2/S7 obligations remain necessary.

A successor could also compare the correlator target with the exact lattice
Gaussian formula, or place windows where the evaluated lattice bias lies
below its frozen precision. Coupling dependence, covariance and sector
mixing would need explicit treatment. No suitability or phase-detection
power for a complete successor is proved here.

By #757's freeze clause, changes belong to a successor identifier. This note
neither reclassifies the existing production nor changes F3/CROSSCHECK-3.

## 5. Audit support and custody

The supplied `break_check_reachability.py` has alternative code paths for
real-space versus Fourier second moments, plaquette covariance, Gaussian
sampling and a lattice-to-continuum comparison. `BREAK_STDOUT.txt` records
the corresponding engineering comparisons. They are not a frozen blind
second-agent confirmation or a public two-architecture gate. The publication
review does not claim to have rerun the long sampling audit.

The original supplied run is recorded as Linux x86_64, Python 3.11,
NumPy 2.4, exit 0 and empty stderr. Its scripts require NumPy and are
engineering scripts, not registered public verifiers. The exact rational
review script uses only the Python standard library. Its publication-review
replay on Linux x86_64, Python 3.12.14, exited zero with empty stderr and
matched the supplied 565-byte stdout exactly. This is an unpinned note
replay, not a public computation gate. From the repository root:

```sh
python notes/C-PHOTON-PRODUCTION-REACHABILITY-N/verification/review_exact_wls.py
```

The five original evidence files retain these SHA-256 hashes:

```text
PREREG.md                    8d98687d8e763bffe5330d66ca40dc4a6b76b455f627f688156e5263b3f5dcf5
verify_reachability.py       44da9fcb4ccd5533446730d0f1e8cf247ab9617a6954307d978a14ab17e4aba2
STDOUT.txt                   bbb28ac8d0d2c406491d1df27098b122dd54ad143d4c04f5f2036bdfe75a400f
break_check_reachability.py  26985981ee70f0bcfcbab293525de83b133efed24137831d97920c04828fda34
BREAK_STDOUT.txt             e444d2c3fc75d6416e837ec3003f4c46b62487cbedf6de50b8e0ffc48f3b4a32
```

`SHA256SUMS` covers the evidence, review addendum and WLS support. It is a
note-local custody manifest, not a Canon manifest. All included material is
project-authored and distributed under the repository Apache-2.0 license.
No third-party source code, private machine record or external dataset is
imported.
