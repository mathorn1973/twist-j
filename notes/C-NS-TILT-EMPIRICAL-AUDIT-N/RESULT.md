# NS-TILT: measured-summary comparison and physical boundary

**NON-CANONICAL. Layer NOT_APPLICABLE. Candidate-C arithmetic on published
summaries. NS-TILT remains H.** No physical or canonical closure is claimed.
Reservation #1400. Exact code, sources and interpretation: CONTRACT.md,
inputs.json, audit.py, EXPECTED.txt and RUN.md.

## 1. Result of the first frozen execution

The existing inverse-alpha rounding witness implies the exact numerical
interval

    264071998379/274071998379 <= n_star <= 264071998381/274071998381.

Computed outward decimal enclosure:

    0.963513237181671 <= n_star <= 0.963513237181938.

This encloses evaluation of the literal hypothesis, not unknown physical
corrections to it. The coefficient five and alpha were not fitted to CMB.

All following m +/- s entries are MEASURED, ROUNDED LITERATURE SUMMARIES.
The z column is a COMPUTED Gaussian-summary diagnostic (m-n_star)/s,
not a measured significance or a posterior probability of NS-TILT.
The last column encloses sensitivity to half-last-digit rounding of both
m and s, and is not a physical confidence interval.

| Data/model context | Reported n_s | Approximate z | Computed outward rounding envelope for z |
|---|---|---:|---|
| Planck 2018 TT,TE,EE+lowE+lensing; base LambdaCDM | 0.9649 +/- 0.0042 | 0.33018 | [0.314532427779, 0.346207908032] |
| P-ACT DR6; base LambdaCDM, without added BAO/lensing reconstruction | 0.9709 +/- 0.0038 | 1.94388 | [1.905652680016, 1.983136751555] |
| SPA+BK; LambdaCDM+r | 0.9682 +/- 0.0032 | 1.46461 | [1.426696251711, 1.503734228041] |
| Same SPA+BK plus DESI DR2 BAO; LambdaCDM+r | 0.9728 +/- 0.0029 | 3.20233 | [3.131106040021, 3.276057129239] |

The common literature pivot is 0.05 Mpc^-1. The first two rows are
contextual, not two independent trials in addition to the main pair.
The exact rational nominal intervals and rounding boxes are in EXPECTED.txt.

The main CMB-only distance is about 1.46 quoted halfwidths; the CMB+BAO
distance is about 3.20. The latter remains above three throughout the
reporting-precision box, but this does NOT evaluate the registered
falsifier. No Gaussian tail probability or full-likelihood conclusion was
computed. In particular there is no multiplied significance from the
four overlapping rows.

## 2. What the measurements actually condition on

Planck's baseline value comes from equation (21), Section 3.4 of
[Planck 2018 VI, v4][planck]. Its pivot is specified in Section 3.3.
It is a base-LambdaCDM scalar power-law inference, not a direct, theory-free
reading of an instrument register.

The ACT context is the P-ACT joint result in Section 8.3 of [Louis et al.,
v2][act]. It combines ACT DR6 and truncated Planck PR3 primary spectra,
with Sroll2 optical-depth information. It is neither ACT alone nor the
P-ACT-LB result with DESI. This distinction is retained before arithmetic.

The main comparison uses equations (1) and (2) of [Balkenhol et al.,
v2][combined], revised 29 June 2026. Their model is LambdaCDM+r with the
single-field slow-roll tensor consistency condition. The scalar index and
r share pivot 0.05 Mpc^-1. Their SPA primary and lensing combination uses
Planck, SPT and ACT, with BK18 B-modes and a Planck-based optical-depth
prior; DESI DR2 BAO is added only in the second row. The paper reports
means and 68 percent intervals, with best fits separately parenthesized.
The means, not best fits, were used here.

The authors explain the BAO-induced shift through correlations with
background parameters and caution about CMB/BAO differences within the
adopted standard model. This does not establish an instrumental error,
a new cosmology or a resolution favourable to TWIST-J. It does make
"CMB alone already rejects the number at 3.2 sigma" an incorrect summary.
The larger distance belongs to the specified CMB+BAO combination.

## 3. Two physical tasks must not be confused

**Conditional empirical test.** One can test the fixed scalar constraint
inside a fully declared, adopted effective cosmology. Standard transfer
functions, recombination, late-time evolution, priors and nuisance models
then remain explicit external inputs. A positive fit would demonstrate
conditional empirical compatibility, not derive those inputs from J.
A poor fit would challenge this specified reading and model combination.

**Integer-derived cosmology.** The scalar formula alone does not supply
an independently admitted integer source for primordial perturbations,
its preparation/measure, spatial mode identification, covariance, amplitude,
scale dependence, tensor counterpart or transport to measured sky spectra.
The present public COSMOLOGY-READING-DICTIONARY is D and explicitly does
not claim a unique decoder or full perturbation theorem. The separately
adopted TT-VECTOR-STATE-NORMALIZATION witness is finite-band and planar;
its registry explicitly excludes an isotropic primordial spectrum.
Those source scopes cannot be enlarged by inserting n_star into a
standard cosmological inference pipeline.

There is also no valid cure by defining a power law with the desired slope
and calling it an integer derivation. To move this physical obligation,
the same admitted source and reading must determine the observable
correlations without using the desired tilt as an input. Its normalization
and at least one consequence beyond that slope must remain testable.
No such source-to-CMB theorem is supplied by this audit.

Thus the work reveals a live empirical tension and a concrete distinction
between testing a scalar hypothesis and deriving a cosmological model.
It closes neither distinction by relabeling algebra or a successful fit.

## 4. The named future test needs an explicit new disposition

The [official CMB-S4 page][s4], checked on 6 October 2026, reports the
9 July 2025 end of DOE/NSF support and an orderly project shutdown. The
separate Science Collaboration continues. That administrative outcome
is not evidence against the equation.

The public NS-TILT row still names CMB-S4. This note changes neither the
wording nor the status. Continuing to describe the row simply as waiting
for that funded project would omit material information. An alternative
measurement/model contract must be explicitly accepted, not silently
substituted into the old rule after looking at these results.

## 5. Reproducibility and limits

First execution: exit 0, empty stderr, exact JSON stdout 3653 bytes;
SHA-256 `4d14c741c6bc2a25014fa5569770725e854fbe44f64d39c3d63aa3445cac4942`.
No corrective execution or fit. All arithmetic is Fraction/integer.
One x86_64 lane, CPython 3.13.5. No independent reviewer, MCMC rerun,
raw-posterior reconstruction or scientific two-architecture gate.

Primary equation text and model descriptions were checked; web PDF
screenshot attempts failed internally. No number was read from an
uninspected chart or table cell. The input manifest hashes a factual
transcription, not the raw experiments. No paper, figure or chain is
redistributed. All comparison selection was retrospective and disclosed.

The [authors' public products][products] make a stronger next analysis
concrete: they provide full-chain archives and best-fit points for
LambdaCDM+r, as well as thinned plotting chains. Their availability is
not an execution or license clearance of that future task. Use the full
analysis products and pinned model/configuration, not plotting contours
or a one-dimensional Gaussian surrogate, for that stronger test.

Disposition: retain this as candidate-C with the physical hypothesis H
unchanged. The next contract is proposed in PROMO; it has not been run.

[planck]: https://arxiv.org/abs/1807.06209v4
[act]: https://arxiv.org/html/2503.14452v2
[combined]: https://arxiv.org/abs/2512.10613v2
[s4]: https://cmb-s4.org/
[products]: https://github.com/Lbalkenhol/r_ns_2025
