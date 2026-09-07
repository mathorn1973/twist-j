# From registration pairs to detector recovery

NON-CANONICAL. Exact measurement-inference boundary; no new detector experiment
or admitted experimental payload. Public Canon v80 unchanged.

The [physical registration audit](C-SNAP-PHYSICAL-REGISTRATION-N.md) identified
detector recovery and retained history as different physical obligations. Its
successor [probe #899](https://github.com/mathorn1973/twist-j/issues/899),
[P-REGISTRATION-PAIR-RECOVERY-1](../probes/P-REGISTRATION-PAIR-RECOVERY-1/PROOF.md),
addresses a necessary intermediate question: what does the measured temporal
statistic actually identify?

## 1. The external observable that motivated the attack

Mark et al. describe a multiple-start/multiple-stop histogram of all detection
pairs, normalize at 800 ns, and exclude early electronic artifacts below 20 ns.
This differs from asking when the first registration after a reset occurs.
Their NbTiN apparatus and fitted results are a published external example,
not a TWIST-J realization. Its modest-rate empirical interpretation is not
asserted false by the exact counterexamples below.
[Primary paper, arXiv 2407.20682v1, section III C and Fig. 4](https://arxiv.org/pdf/2407.20682v1).

The [Zenodo 12773197 catalogue](https://zenodo.org/records/12773197) supplies
named bias-current histograms and separate calibration files. Metadata-only
inspection verified v1, CC-BY-4.0, data.zip size 1389937 bytes and provider MD5
`1cac3138ca3d00657d57ae2722a81fbe`. No archive bytes were downloaded or opened,
no SHA-256 custody was established and no measurement file was admitted.
The primary paper, published results and catalogue values were already exposed;
any future reanalysis is retrospective, not blind.

## 2. The exact distinction

In a stipulated discrete renewal model, let h_k be the registration hazard
at age k since the last registration, w_k the first-gap weight and u_k the
probability of a registration at lag k from an initial one. Then

```
w_k = h_k product_(j<k)(1-h_j),
u_0 = 1,
u_k = w_k + sum_(j=1)^(k-1) w_j u_(k-j).
```

The convolution counts histories with intervening registrations. It cannot
generally be dropped. For one dead step followed by constant hazard 1/2,
the stationary intensity is 1/3 and

| Lag | Normalized hazard | Pair probability u_k | Pair probability / intensity |
|---|---:|---:|---:|
| 2 | 1 | 1/2 | 3/2 |
| 3 | 1 | 1/4 | 3/4 |
| 4 | 1 | 3/8 | 9/8 |

Thus structure in a pair histogram is not automatically structure in the
detector's recovery law. This is a conditional coefficient counterexample,
not a prediction for the externally documented device.

## 3. What can be recovered

Within the independently admitted renewal class, complete absolutely scaled
pair data have a unique first-gap inverse:

```
w_k = u_k - sum_(j=1)^(k-1) w_j u_(k-j),
h_k = w_k / [1-sum_(j<k)w_j], if the denominator is positive.
```

The reconstructed w must be nonnegative with cumulative weight at most one.
A zero denominator marks an unreachable age, not zero efficiency. A failure
of these inequalities rejects the stated renewal-prefix model; it does not
alone prove the physical measurements wrong. Finite prefixes and arbitrarily
normalized curves leave additional scale and tail ambiguity.

Without the renewal premise, even complete pair information need not suffice.
The two patterns {0,1,4,6} and {0,1,3,7} on a 12-step circle, each observed with
uniform phase, have identical all-lag pair laws and the same intensity 1/3.
Their successive gaps are (1,3,2,6) and (1,2,4,5). This is an exact example of
different event histories hidden behind identical complete pair statistics.

A positive approximation result also survives. If h_k=a eta_k with
0<=eta_k<=1 and 0<a<=1, then at finite lag k

```
|u_k/a-eta_k| <= 1-product_(j<k)(1-h_j) <= a(k-1).
```

This supplies an explicit dilute-input condition. It uses the independently
specified opportunity rate a, not a finite-lag normalization or the observed
registration intensity. Actual time binning, electronics and source statistics
require their own physical justification. Registrations alone also cannot
separate a and eta: every a>=max h in the admitted product model gives
eta=h/a and the same registration law.

## 4. Consequence for the physical program

Before interpreting an archive as detector recovery, freeze whether its rows
define first gaps, all-pairs counts, or triggered probe outcomes. Bind that
observable to timing, scale, coverage and artifact handling. Independently
specify which detector/source history changes the response. If a renewal
model is used, say why it is admissible; equal pair curves cannot certify it.
Removing early artifact bins does not supply a complete first-gap inverse.

The next physical test can then compare a specified response model with the
correct observable, with uncertainty and missing inputs explicit. It must not
convert a source-dependent counting artifact into an inferred physical Snap
law. A native U source, coupling and material record map remain unprovided.

This probe supplies the exact conversion, its validity conditions and explicit
counterexamples to overinterpretation. It does not close the physical owner
[#539](https://github.com/mathorn1973/twist-j/issues/539) or source lane
[#834](https://github.com/mathorn1973/twist-j/issues/834), derive Born, or report
a newly performed detector measurement.
