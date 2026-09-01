# PHOTON-PRODUCTION-PREREG-FREEZE-1

**Status:** FORMAL PRODUCTION PREREGISTRATION / FINAL FREEZE / UNEXECUTED / NON-CANONICAL  
**Owner:** A. M. Thorn  
**Issue:** #757  
**Parent experiment:** #742 `E-PHOTON-Z5-PHASE-MEASUREMENT-1`  
**Public basis:** Public Canon v74  
**Freeze base:** `3bb9087cdea293c494ae86b5824e9d8d221fbbfb`  
**Date:** 2026-09-01

This document prospectively freezes the production experiment at the fixed
physical candidate point `t=1`. It is written after the successful zero-weight
mixing pilot #755 and after the independent dual implementation freeze #767,
but before any production state, statistic, histogram or phase output exists.

Nothing in this note changes Canon, Registry, Gates, Frontier or a scientific
status. No production run is authorized merely by merging this note.

The production execution firewall is stricter than the minimum issue #757
entry condition:

```text
PRODUCTION_START requires all three:
  F1 this preregistration merged and publicly read back,
  F2 issue #748 independent saved-state reader frozen and its exact fixtures PASS,
  F3 issue #756 zero-evidence L=6,8 dual/Ward cross-check returns DUAL_CROSSCHECK_PASS.
```

Until all three hold, production under #742 is forbidden.

---

## 1. Fixed scientific question

For each production size

```text
L in {8,12,16,24,32},
K_L=(Z/LZ)^4,
A in C^1(K_L;Z5),
F=dA in C^2(K_L;Z5),
```

sample the exact finite-volume measure

```text
mu_L(A) = Z_L^(-1) product_p W(F_p),
W(f)=2+2 cos(2 pi f/5)
    =(4,phi^2,phi^-2,phi^-2,phi^2).
```

The physical candidate point is permanently

```text
t_physical = 1.
```

No production `W^t` scan is permitted. No coupling, exponent, lattice size,
observable, fit family, window, threshold or terminal may be changed after the
public freeze because a result is favourable or inconvenient.

All link fields and all periodic holonomy sectors are included. Gauge fixing is
not part of the sampled measure and may not be used to discard sectors.

---

## 2. Frozen numerical dependencies

The primal transition law is the exact implementation already accepted by the
successful pilot lineage:

```text
exact local heat-bath kernel:       PR #760 merge 5c2d469880828f29023e3cf592e86abbe352cd59
successful successor pilot:         #755 / PR #765 / PR #766
pilot integration on main:          a91ec3c2a38c64a9c0b1be4db55947ce0c97e937
pilot immutable source pin:          b43ba8c33d244961783c0de42c89b7038fefe561
pilot SHA256SUMS:                    07ee9dbd69f34875af1e7e1a1cf41e8284217e58c2807dfd57babcbc5e3bf6d2
independent dual source freeze:      PR #767 merge 3bb9087cdea293c494ae86b5824e9d8d221fbbfb
independent dual formal source pin:  fe74bf9d9cc8666b569d4618efd2149215c19c3d
```

The production sampler may wrap the accepted primal implementation for larger
`L` and for state custody, but it may not alter any categorical decision,
random-bit refinement rule, local/line orbit mass, flat holonomy move or charge
conjugation rule. Any scientific need to alter a transition kernel consumes a
new experiment identifier and invalidates this production freeze.

The independent reader #748 must consume only saved link states. It may not use
the sampler's in-memory observable values. The independent dual implementation
#767 uses a separate state space, proposal law and SHA-256 counter bitstream;
it shares no primal transition code.

---

## 3. Exact production transition macrocycle

One production macrocycle is exactly the successful pilot-2 macrocycle:

```text
1  one complete exact single-link heat-bath sweep over all 4L^4 links,
2  one complete exact noncontractible-line heat-bath sweep over all 4L^3 lines,
3  one exact-uniform flat holonomy sheet in each direction mu=0,1,2,3,
4  one exact-fair global charge-conjugation decision.
```

Even macrocycles use forward lexicographic order; odd macrocycles use exact
reverse order. The local and line heat baths use the exact `Z[phi]` prefix
comparison. No fixed-width probability table, floating-point categorical draw,
rounding fallback or approximate acceptance is allowed. Failure to resolve a
prefix by the inherited 256-bit cap is `STOP_INTEGRITY`.

The production random source is the same counter-based Philox4x32-10 design as
the successful primal pilot. Every use remains a pure function of

```text
(seed, kind, macrocycle, ordinal, block)
```

with disjoint namespaces. Variable bit consumption in one decision cannot
shift later decisions.

---

## 4. Frozen production chains and public seed schedule

There are exactly four primal chains per lattice size: two cold and two hot.
The twenty seeds are:

```text
L=8  cold r1  0xE757080000000101
L=8  cold r2  0xE757080000000102
L=8  hot  r1  0xE757080000000201
L=8  hot  r2  0xE757080000000202

L=12 cold r1  0xE7570C0000000101
L=12 cold r2  0xE7570C0000000102
L=12 hot  r1  0xE7570C0000000201
L=12 hot  r2  0xE7570C0000000202

L=16 cold r1  0xE757100000000101
L=16 cold r2  0xE757100000000102
L=16 hot  r1  0xE757100000000201
L=16 hot  r2  0xE757100000000202

L=24 cold r1  0xE757180000000101
L=24 cold r2  0xE757180000000102
L=24 hot  r1  0xE757180000000201
L=24 hot  r2  0xE757180000000202

L=32 cold r1  0xE757200000000101
L=32 cold r2  0xE757200000000102
L=32 hot  r1  0xE757200000000201
L=32 hot  r2  0xE757200000000202
```

A cold start is the all-zero link field. A hot start is the exact-uniform `Z5`
link initialization already defined by the primal implementation. No failed
chain is replaced by a new seed. No chain extension after the frozen maximum is
permitted.

---

## 5. Frozen thermalisation rule

Thermalisation is allowed to adapt only through a prospective convergence rule,
never through a phase value. The only candidate thermal endpoints are

```text
1024, 2048, 4096, 8192 macrocycles.
```

At each endpoint the automated convergence checker uses exactly the most recent
512 macrocycles from each of the four chains at that `L`. Human inspection of
phase histograms is forbidden while this decision is being made.

The sixteen mixing sentinels are inherited unchanged from pilot 2:

```text
logw
polyakov_radius_mean
polyakov_radius_0
polyakov_radius_1
polyakov_radius_2
polyakov_radius_3
vortex_density
monopole_density
score_mean
flux_asym_14
flux_asym_23
flux_fraction_0
flux_fraction_1
flux_fraction_2
flux_fraction_3
flux_fraction_4
```

The earliest endpoint is accepted only if, for every sentinel:

```text
unique state fraction per chain                 >= 0.99
strictly positive finite variance               PASS
Geyer IMS ESS per chain                         >= 64
rank-normalized split Rhat                      <= 1.05
folded rank-normalized split Rhat               <= 1.05
pooled rank-normalized bulk ESS                 >= 400
pooled 5%/95% tail ESS                          >= 200
hot/cold mean separation                        <= z 4
first-half/second-half drift in every chain     <= z 4
```

and all exact cache, line-move, prefix-depth, counter and state-custody checks
pass. If no candidate endpoint passes by 8192 macrocycles, the terminal is
`STOP_MIXING`. The thermal block is not restarted with new seeds.

The rank, tie, quantile and Geyer conventions are exactly those frozen by the
successful pilot #755. They may not be redefined here.

---

## 6. Frozen measurement block

After the earliest accepted thermal endpoint, each of the four chains produces
exactly

```text
1024 recorded production samples,
1 complete macrocycle between consecutive samples,
no sample at the thermal endpoint itself.
```

Every sample must be saved in the canonical link-state format frozen by #748,
with independent state hash and chain/sample identity. The #748 reader owns the
second reconstruction of plaquette flux, Polyakov loops, periodic topology and
connected-correlation sufficient statistics.

The complete 1024-sample block must then satisfy stricter post-measurement
mixing gates on the same sixteen sentinels:

```text
unique state fraction per chain                 >= 0.99
Geyer IMS ESS per chain                         >= 128
rank-normalized split Rhat                      <= 1.03
folded rank-normalized split Rhat               <= 1.03
pooled bulk ESS                                 >= 800
pooled tail ESS                                 >= 400
hot/cold mean separation                        <= z 3
first-half/second-half drift in every chain     <= z 3
```

A failed post-measurement gate returns `STOP_MIXING`. Samples are not extended,
thinned differently or selectively discarded.

---

## 7. Frozen uncertainty treatment

All primary uncertainties are computed from chain-preserving blocks.

For a scalar observable at fixed `L`, compute the Geyer IMS integrated
autocorrelation estimate separately in each chain and put

```text
tau_max = max_chain tau_int,
b = max(16, ceil(4 tau_max)).
```

Round `b` upward to the next power of two. Blocks never cross chain boundaries.
If this leaves fewer than 16 complete blocks in any chain, the observable is
not considered resolved and the production terminal cannot be a positive phase
label; if the failure affects a mixing sentinel, return `STOP_MIXING`.

Complete blocks only are used. The estimator and covariance are obtained by a
chain-preserving delete-one-block jackknife. Report 99% Student-t intervals.
Different `L` values use independent seed families and are treated as
independent in cross-size fits.

No standard error may be replaced by the naive independent-sample error.

---

## 8. Independent-reader integrity gates

Before any phase classifier is evaluated, #748 must reproduce from saved link
states, independently of the sampler:

```text
oriented plaquette fluxes,
all four Polyakov directions,
R_L and A5_L sufficient statistics,
principal-flux integer monopole current m=df/5,
exact local current-closure checks,
periodic homology/wrapping of vortex surfaces,
periodic wrapping and connected components of dual monopole current,
termwise block sufficient statistics for connected plaquette covariance.
```

Sampler and reader state hashes, exact flux counts and all exactly shared
integer quantities must agree. A mismatch is `STOP_INTEGRITY`, never a physical
phase result.

Support-graph connectivity is not accepted as periodic wrapping. Configuration
centering before connected covariance is not accepted; covariance must be built
from the frozen block sufficient statistics.

---

## 9. Polyakov classifier

For each `L`, define exactly

```text
R_L  = E |Pbar|,
A5_L = |E(Pbar^5)| / E(|Pbar|^5),
```

using the four directions and chain-preserving uncertainty construction frozen
above.

The asymptotic decision uses only

```text
L in {12,16,24,32}.
```

For each of `R_L` and `A5_L`, fit both predeclared correction families

```text
M1(p=1): y_L = y_inf + a/L,
M2(p=2): y_L = y_inf + a/L^2,
```

by weighted least squares using the jackknife standard errors. The intercept is
not constrained during fitting.

Classify a quantity as

```text
POSITIVE_LIMIT
  iff the lower 99% confidence bound for y_inf is > 0 in BOTH M1 and M2;

ZERO_COMPATIBLE
  iff 0 lies inside the 99% confidence interval for y_inf in BOTH M1 and M2;

UNRESOLVED
  otherwise, including a significantly negative fitted intercept or singular fit.
```

The Polyakov vote is then exactly

```text
POLYAKOV_PHOTON:
  R_L  = POSITIVE_LIMIT
  A5_L = ZERO_COMPATIBLE

POLYAKOV_CONFINED:
  R_L  = ZERO_COMPATIBLE

POLYAKOV_Z5_BROKEN:
  R_L  = POSITIVE_LIMIT
  A5_L = POSITIVE_LIMIT

POLYAKOV_UNRESOLVED:
  every other combination.
```

No absolute radius or anisotropy cutoff is introduced.

---

## 10. Periodic topology classifier

The #748 reader must return a Boolean periodic wrapping indicator per saved
configuration for vortex surfaces and for dual monopole components. Wrapping
probabilities are analyzed with the frozen block jackknife.

For either object, use only `L=24` and `L=32` for the terminal vote:

```text
WRAPPING
  iff the lower 99% confidence bound exceeds 1/2 at BOTH L=24 and L=32;

NONWRAPPING
  iff the upper 99% confidence bound is below 1/2 at BOTH L=24 and L=32;

WRAP_UNRESOLVED
  otherwise.
```

For each configuration also record the largest monopole component divided by
four-volume, `M_L`. Fit `M_L` with the same two asymptotic families and the same
`POSITIVE_LIMIT / ZERO_COMPATIBLE / UNRESOLVED` rule as section 9. The complete
monopole component-size tail is retained as a primary reported observable; no
post-hoc tail cutoff may be invented.

The topology vote is exactly

```text
TOPOLOGY_PHOTON:
  vortices = WRAPPING
  monopoles = NONWRAPPING
  M_L = ZERO_COMPATIBLE

TOPOLOGY_CONFINED:
  vortices = WRAPPING
  monopoles = WRAPPING
  M_L = POSITIVE_LIMIT

TOPOLOGY_Z5_BROKEN:
  vortices = NONWRAPPING

TOPOLOGY_UNRESOLVED:
  otherwise.
```

---

## 11. Long-distance plaquette correlator

The connected orientation sum is reconstructed only from #748 termwise block
sufficient statistics. For periodic separation `n`, define

```text
Q_L(n) = C_L(n)/C_L(n+1),

Q4_L(n)
 = [n^(-4)+(L-n)^(-4)]
   /[(n+1)^(-4)+(L-n-1)^(-4)].
```

`L=8,12` are diagnostic only. The decision sizes are `L=16,24,32`, with the
window fixed before data as

```text
n_min(L) = max(2, ceil(L/8)),
n_max(L) = floor(L/4).
```

Thus the exact windows are

```text
L=16: n=2..4
L=24: n=3..6
L=32: n=4..8.
```

A ratio enters the fit only if both `C_L(n)` and `C_L(n+1)` are resolved at at
least four jackknife standard errors from zero. If a predeclared window loses
an unresolved point, the entire correlator vote at that `L` is `UNRESOLVED`;
the window is never shortened after inspection.

For each decision size, form the jackknife covariance matrix of the vector
`Q_L-Q4_L` and its generalized least-squares chi-square. Also fit one common
amplitude `K_L` in

```text
C_L(n)=K_L[n^(-4)+(L-n)^(-4)]
```

over the same window.

Classify

```text
CORRELATOR_PHOTON
  iff at BOTH L=24 and L=32:
    chi-square compatibility p >= 0.01,
    and the 99% confidence interval for K_L excludes 0;

CORRELATOR_REJECTS_PHOTON
  iff p < 1e-4 at BOTH L=24 and L=32;

CORRELATOR_UNRESOLVED
  otherwise.
```

A visually straight log-log plot has no decision authority.

---

## 12. TWIST score/current and dual firewall

The production report must include the primal score observables and the defect
screening statistic prospectively named in #742. The statistic

```text
R(q)=[25 tr S_j(q)+tr S_rho(q)]/lambda(q)
```

is reported at every predeclared lowest nonzero momentum and with the same block
uncertainty rules. It is an infrared diagnostic and theorem guide. This
production preregistration does **not** invent a new numerical screening
threshold and does not promote a finite-volume observation to the strict
infinite-volume screening theorem.

Before production may start, the independent dual implementation #767 must
have completed the separate zero-evidence `L=6,8` cross-check under #756 and
returned

```text
DUAL_CROSSCHECK_PASS.
```

That cross-check must include the frozen contact identity and the distinct-face
covariance identity

```text
Cov_mu(G_p,G_q) = -kappa^(-2) Cov_nu(n_p,n_q)
```

at its preregistered separations. If #756 returns any other terminal,
production does not start.

Within production, exact saved-state score/current reconstruction checks are
integrity checks. A reproducible exact mismatch is `STOP_INTEGRITY`; a
statistical Ward residual is reported with its 99% interval and may not be
silently absorbed into a phase label.

---

## 13. Frozen phase-vote logic

A phase label is available only after all integrity and mixing gates pass.

### Photon vote

```text
PHOTON_VECTOR = PASS
iff all are true:
  POLYAKOV_PHOTON
  TOPOLOGY_PHOTON
  CORRELATOR_PHOTON
  #756 prerequisite = DUAL_CROSSCHECK_PASS
  all exact reader/state/Ward integrity checks PASS.
```

### Confined vote

```text
CONFINED_VECTOR = PASS
iff all are true:
  POLYAKOV_CONFINED
  TOPOLOGY_CONFINED
  CORRELATOR_REJECTS_PHOTON.
```

### Z5-broken vote

```text
Z5_BROKEN_VECTOR = PASS
iff all are true:
  POLYAKOV_Z5_BROKEN
  TOPOLOGY_Z5_BROKEN
  CORRELATOR_REJECTS_PHOTON.
```

The defect-screening statistic and complete component tails are always
reported. They may strengthen interpretation, expose a contradiction or guide
a later theorem attack, but they cannot rescue a failed frozen phase vector.

---

## 14. Finite-size transition rule

`MULTIPHASE_OR_TRANSITION` is reserved for a specific finite-size pattern, not
for generic disagreement. It is returned only if all integrity and mixing
checks pass and one complete phase vector is supported on the lower decision
sizes while a different complete phase vector is supported on the higher
sizes, with the crossover occurring inside the frozen production set.

A hot/cold disagreement at one fixed `L` that violates the mixing gates is
`STOP_MIXING`, not evidence for coexistence.

Any other incomplete, contradictory or insufficiently resolved set of phase
votes returns `AMBIGUOUS_FINITE_SIZE`.

---

## 15. Exact terminal precedence

Exactly one production terminal is emitted, in this precedence:

```text
1  STOP_INTEGRITY
2  STOP_MIXING
3  MULTIPHASE_OR_TRANSITION
4  PHOTON_EVIDENCE
5  CONFINED_EVIDENCE
6  Z5_BROKEN_EVIDENCE
7  AMBIGUOUS_FINITE_SIZE
```

Definitions:

```text
STOP_INTEGRITY
  any source/pin/state hash, exact transition, prefix, cache, reader,
  serialization, exact reconstruction, process exit/stderr or exact Ward
  ownership check fails.

STOP_MIXING
  integrity passes but thermal or final frozen convergence gates fail.

MULTIPHASE_OR_TRANSITION
  section 14 is satisfied.

PHOTON_EVIDENCE
  PHOTON_VECTOR = PASS and neither earlier terminal fires.

CONFINED_EVIDENCE
  CONFINED_VECTOR = PASS and neither earlier terminal fires.

Z5_BROKEN_EVIDENCE
  Z5_BROKEN_VECTOR = PASS and neither earlier terminal fires.

AMBIGUOUS_FINITE_SIZE
  integrity and mixing pass but no earlier finite-size label is fully earned.
```

No terminal may be renamed after production opens.

---

## 16. Data custody and blindness

Before the first production macrocycle, the execution package must publish and
read back:

```text
sampler source hashes,
#748 reader source hashes,
#756 cross-check receipt,
this preregistration commit hash,
all twenty seeds,
all schedules and namespaces,
compiler/interpreter versions,
state serialization contract,
analysis source hashes,
terminal grammar hash.
```

The automated pipeline owns the thermal checkpoint decisions. Humans may inspect
integrity failures but may not inspect phase histograms and then alter a
schedule or threshold. Raw states and sufficient-statistic files are immutable
once written and receive SHA-256 custody manifests.

A lattice size is never dropped because it disagrees with the others. A chain
is never replaced because it mixes poorly. A failed production run is a result,
not an invitation to rewrite this preregistration.

---

## 17. Scientific status ceiling

Even the strongest positive terminal means only

```text
PHOTON_EVIDENCE at the frozen finite-size production scope.
```

It does not prove `PHOTON-MASSLESS-PHASE [T]`, does not close the thermodynamic
limit, and does not identify the measured infrared pole with the exact v74 D3
characteristic. The latter remains the separate pole-identification gate #744.
It also does not establish SI light speed, apparatus calibration, polarization
as a physical readout, matter mass, contraction/expansion or any cosmological
claim.

The maximum evidential status is the one actually earned by the frozen
finite-size experiment.

---

## 18. Freeze declaration

After this note merges, the scientific degrees of freedom owned by #757 are
consumed:

```text
action              FIXED at t=1
sizes               FIXED {8,12,16,24,32}
starts              FIXED 2 cold + 2 hot per L
seeds               FIXED above
thermal endpoints   FIXED {1024,2048,4096,8192}
measurement count   FIXED 1024 per chain
measurement spacing FIXED 1 macrocycle
mixing gates        FIXED sections 5-6
uncertainty rule    FIXED section 7
Polyakov fits       FIXED section 9
wrapping rule       FIXED section 10
correlator windows  FIXED section 11
phase vectors       FIXED section 13
terminal precedence FIXED section 15
```

The only remaining legitimate pre-production work is implementation and exact
verification of already frozen obligations #748 and #756, followed by an
execution-package hash/readback. None of that may alter the scientific decision
rules above.
