# P-U-ION-LS-LOCAL-EXCHANGE-1: source provenance

NON-CANONICAL. Read/rechecked 2026-10-04. Descriptions below identify the
limited inputs consumed by MODEL.md. Equations derived in this probe, its
affine echo and its constructive pulse word are not attributed to external
experiments. No third-party image or copied supplement is included.

## S0. Fixed logical dictionary and inherited contact inputs

Repository note `notes/C-U-ION-OFFSET-GLOBAL-AUDIT-N/README.md`, public
PR [#1363](https://github.com/mathorn1973/twist-j/pull/1363), supplies the
fixed preparation-time `K`, the conjugated whole-history law and the physical
input families `(s,1)` and `(s,4)`. It is a mathematical audit, not external
evidence of an ion apparatus. The earlier same-dictionary boundary is
`probes/P-U-ION-LS-CONTACT-BOUNDARY-1/`, public
PR [#1361](https://github.com/mathorn1973/twist-j/pull/1361).
Neither closed item is altered or reopened by this probe.

## S1. One experimental platform: Hrmo et al.

P. Hrmo et al., *Native qudit entanglement in a trapped ion quantum
processor*, Nature Communications **14**, 2242 (2023), published 19 April
2023. DOI [10.1038/s41467-023-37375-2](https://doi.org/10.1038/s41467-023-37375-2).

Primary reading surfaces:

- [Publisher article](https://www.nature.com/articles/s41467-023-37375-2).
- [Publisher Fig. 1](https://www.nature.com/articles/s41467-023-37375-2/figures/1):
  the five label-to-level assignments were visually checked.
- [Author preprint, arXiv:2206.04104v1](https://arxiv.org/html/2206.04104v1),
  8 June 2022, including Appendix AI and AII. Version is explicit because
  the preprint organization differs from the published article.
- [Published article at PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10115791/).

Consumed facts: Eq. (1) gives the one-COM effective force; Eq. (5) and the
experimental pulse description give common 729 nm star rotations. The
experiment uses 401.2 nm travelling-wave beams and reports a half-period
spacing calibration; Appendix AI states equal illumination and spatial
phases `phi_N=N pi`. The large S-versus-D shift establishes a non-scalar
profile without establishing five independent controls. The source's
cyclic-echo gate motivates, but is different from, the present affine echo.

The reported two-ion experiment does not certify the new contact word,
an occupied archive or fourteen-ion selective support. Absolute carrier
rates, an admissible intensity box for this word and its accumulated error
are not supplied as numerical inputs here. The measured short-gate
performance is not a bound for the present construction.

## S2. Microscopic dependence of light shift on beam controls

B. C. Sawyer and K. R. Brown, *A Wavelength-Insensitive, Multispecies
Entangling Gate for Group-2 Atomic Ions*, Physical Review A **103**, 022427
(2021). DOI [10.1103/PhysRevA.103.022427](https://doi.org/10.1103/PhysRevA.103.022427).
This is a theoretical source cited by S1, not another imported gate library.
Read [arXiv:2010.04526v1](https://arxiv.org/html/2010.04526v1),
9 October 2020.

Appendix A, Eqs. (7)-(10), expresses fixed-frequency Stark shifts through
intensity, polarization, transition frequencies and dipole matrix elements.
Appendix C.2, Eqs. (36)-(39), separates the travelling-wave shift amplitude
from the stationary shift; the former uses the geometric mean of individual
beam shifts. These give the fixed-profile scalar-intensity law adopted in
MODEL.md. The independently calibrated coefficients retain all five levels.

Appendix C.3, Eqs. (44)-(49), identifies the Lamb-Dicke and rotating-wave
steps and the closed-loop phase. The discussion after Eq. (52) explicitly
distinguishes closing the chosen mode from closing a spectator mode.
Section VI and Appendix C.3 also discuss stationary and oscillating Stark
phases. Their suppression is an approximation unless explicitly included
and compensated; carrier errors are not covered by diagonal LS twirling.

## S3. Scope check for multimode and local phases

P. Kamenskikh et al., *Analysis of the action of conventional trapped-ion
entangling gates in qudit space*,
[arXiv:2602.21886v1](https://arxiv.org/html/2602.21886v1), 25 February 2026,
DOI [10.48550/arXiv.2602.21886](https://doi.org/10.48550/arXiv.2602.21886).
This preprint is used to delimit approximations, not as evidence of an
experimental implementation of the present sequence.

Section II.2, Eqs. (14)-(21), separates AC shifts, multimode force and
one-ion phases. Appendix A, Eqs. (50)-(51), gives the state- and
mode-resolved residual displacement. It supports requiring all relevant
displacements to vanish or be bounded before claiming a physical error
certificate. Its added control proposals are not imported into this model.

## Independence and unresolved calibration

The level dictionary, form of interaction and elementary carrier support
come from S1; scalar intensity dependence is grounded by S2. Choosing
`lambda_*` for a desired phase is synthesis of a prescribed function, not
an independent prediction of that function. No coefficients are fitted
to the original histories. The mathematical construction is uniform over
every fixed non-scalar profile satisfying the frozen admissibility inputs.
Numerical values and uncertainties of that profile, powers, Rabi rates,
switching latency and whole-word error remain unprovided device inputs.
