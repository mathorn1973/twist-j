# PHOTON-PROGRAM-CLOSURE-V74

**Status:** NON-CANONICAL SYNTHESIS / CLOSURE DISPOSITION / MEASUREMENT CONTRACT  
**Authority:** none  
**Public basis:** Public Canon v74  
**Issue lock:** #740  
**Date:** 2026-09-01  
**Owner:** A. M. Thorn

This note does not change Canon, Registry, Gates, Frontier, releases, workflow,
or any scientific status. It separates four questions that had been carried
under the single word *photon*:

```text
P1  exact free kinematics and light-cone germ,
P2  existence of a massless phase in the fixed Z5 action,
P3  identification of the measured long-distance pole with the v74 carrier,
P4  physical scale, polarization and apparatus reading.
```

The separation is binding. A proof or measurement at one line does not
silently close another.

## 1. Executive verdict

The Public Canon v74 photon program is now sufficiently complete to end its
construction-only stage.

```text
exact spatial carrier and symbol            CLOSED
exact temporal recurrence and branches      CLOSED
effective Minkowski characteristic          CLOSED at the quadratic germ
global single-chart Herm2 vector square root EMPTY in the natural class
fixed positive Z5 face action               AVAILABLE and ready to freeze
massless thermodynamic phase                 OPEN theorem / ready for measurement
L6 pole-to-L5 characteristic seam            MISSING and named below
physical scale and apparatus                 OPEN
scalar massive kinematics                    READY NOW
physical origin and reading of mass          OPEN and separate
```

The correct near-term declaration is therefore:

```text
PHOTON KINEMATICS:       CLOSED, after review/fold of PR #739
PHOTON CONSTRUCTION:     MEASUREMENT READY
PHYSICAL PHOTON:         NOT YET CLOSED
MASSIVE KINEMATICS:      RELEASED AS A SEPARATE LANE
```

This is not rhetorical compromise. The exact free propagation law is already
stronger than a guessed continuum dispersion. What remains is a phase and
readout problem.

## 2. Public v74 state

The authoritative v74 rows are:

```text
FCC-WEIGHTED-SHELL-SYMBOL [T]
FCC-WEIGHTED-SHELL-REMAINDER [T]
PHOTON-SPATIAL-TEMPORAL-TRANSFER [D]
PHOTON-TEMPORAL-CHARACTERISTIC [T]
PHOTON-CONE-CONVERGENCE [O]
PHOTON-MASSLESS-PHASE [O]
PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP [T]
PHOTON-Z5-STAR-QUADRATURE [C]
PHOTON-KAPPA-LEMMA [F]
PHOTON-WINDOW-PROOF [F]
```

The terminal `F` rows remain terminal. Nothing in this note repairs or
reopens the kappa route.

The v74 selected carrier is

```text
D3={x in Z^3:x1+x2+x3 is even}
```

with the exact normalized spatial symbol

```text
s(k)
 = (1/324) sum_(n in {2,4,8,10,16}) w_n
            sum_(v in S_n)(1-cos(<k,v>)),
(w2,w4,w8,w10,w16)=(6,1,15,1,1),
```

and temporal characteristic

```text
4 sin^2(omega/2)=s(k).
```

It has two real unit-modulus branches away from the unique momentum
character with `s=0`, and a non-identity parabolic double root at that apex.

For every `epsilon>0`,

```text
q_epsilon(Omega,k)
 =4 sin^2(epsilon Omega/2)/epsilon^2
  -s(epsilon k)/epsilon^2
```

obeys

```text
-(epsilon^2/12)Omega^4
 <=q_epsilon-(Omega^2-|k|^2)
 <=(11/27)epsilon^2|k|^4.
```

Thus the characteristic already has an effective, quantitative, parameter-free
Minkowski tangent.

## 3. Hermitian cone disposition

PR #739, probe
`P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1`, freezes the standard carrier

```text
H(Omega,k)
 =[[Omega+k3,k1-i k2],
   [k1+i k2,Omega-k3]],
det H=Omega^2-|k|^2.
```

It proves two different facts.

### 3.1 What closes

The v74 characteristic and `det H` agree as an exact quadratic germ, with the
same displayed global remainder. This is the correct local and scaling
light-cone statement.

Proposed row after review:

```text
PHOTON-HERM2-TANGENT-GERM [T]
```

### 3.2 What does not close globally

A natural single-chart separated global lift would require a total map

```text
p:T_D3->R^3,
p(-k)=-p(k),
|p(k)|^2=s(k).
```

The complete reciprocal two-torsion census gives

```text
s=0       once,
s=1/3     four times,
s=32/81   three times.
```

Every two-torsion momentum is fixed by inversion. Oddness would force `p=0`
at all eight classes, contradicting the seven positive values. The frozen
global class is therefore empty.

A map such as

```text
p(k)=(sqrt(s(k)),0,0)
```

is not a solution to the physical dictionary problem. It merely hides the
scalar in one arbitrarily chosen direction and violates inversion and point
group covariance.

### 3.3 Required gate repair

The existing gate
`GATE-L4-L5-PHOTON-CONE-IDENTIFICATION` currently mixes a local physical
question with a global exact periodic parametrization and leaves the
admissible class too broad. It should be split, in a later Canon fold, into:

```text
GATE-L4-L5-PHOTON-CONE-GERM
  positive condition: the independently frozen Herm2 determinant equals
  the scaling germ of the L5 characteristic with an effective remainder

GATE-L4-L5-PHOTON-GLOBAL-CARRIER
  optional research gate: freeze and classify a multichart, twisted-bundle,
  higher-rank or other covariant global carrier
```

The first gate can close by PR #739. The second must not block measurements
or massive local kinematics. It remains a global-geometry research lane.

## 4. The fixed L4 action to measure

The primary finite-volume carrier is the periodic four-torus

```text
K_L=(Z/LZ)^4.
```

Let

```text
A in C^1(K_L;Z5),
F=dA in C^2(K_L;Z5).
```

For a plaquette value `f in Z5`, freeze the positive face weight

```text
W(f)=2+2 cos(2pi f/5)
    =(4,phi^2,phi^-2,phi^-2,phi^2).
```

Its unnormalised Fourier transform is exactly

```text
F_5 W=5(2,1,0,0,1).
```

The primary candidate measure is

```text
mu_L(A)
 =Z_L(1)^(-1) product_p W(F_p),

Z_L(1)
 =sum_(A in C^1(K_L;Z5)) product_p W(F_p).
```

All link variables, including all topological sectors, are summed. Gauge
fixing may be used only as an exactly compensated implementation device.
Every primary observable below is gauge invariant.

The optional diagnostic family is

```text
mu_(L,t)(A)
 proportional product_p W(F_p)^t,  t>=0.
```

The physical candidate point is fixed prospectively at

```text
t_physical=1.
```

A scan in `t` may map phase boundaries and test robustness. It may not move
`t_physical`, redefine `W`, choose a more favourable power, or turn a nearby
photon phase into evidence for the point `t=1`.

At `t=0` the face weight is uniform. As `t` grows, zero flux is increasingly
favoured. Those endpoints make the diagnostic family useful, but they prove
nothing about the phase at `t=1`.

## 5. Existing exact observable bridge

For `theta_f=2pi f/5`, define the total local score

```text
X(f)=sin(theta_f)/(1+cos(theta_f)),
kappa=tan(pi/5),
G(f)=X(f)/kappa.
```

The exact five values are

```text
G=(0,1,2+sqrt5,-(2+sqrt5),-1).
```

The character expansion gives the paired integer surface ensemble

```text
n in {-1,0,1}^P,
partial n=0 mod 5,
weight proportional 2^(-|supp n|),
j=partial n/5.
```

The existing non-canonical exact notes prove a contact Ward identity and,
for distinct plaquettes,

```text
Cov_mu(G_p,G_q)
 =-kappa^(-2) Cov_nu(n_p,n_q).
```

Thus absolute summability or its failure is equivalent between the score and
dual surface variables, orientation by orientation. The exact
`PHOTON-DEFECT-SCREENING-CRITERION` further reduces masslessness to a strict
infrared screening inequality for the defect fields. That strict inequality
has not been proved. Positivity and the Ward identity alone do not imply it.

This is the right analytic boundary. The last theorem is no longer “find an
action” or “guess a photon observable”; it is a quantitative infrared
estimate for one fully displayed fixed action.

## 6. Why the phase must now be measured

The Fröhlich-Spencer 1982 theorem proves an intermediate QED phase for
four-dimensional `Z_N` models with `N` large. Its published abstract does
not supply an exact `N=5` instance, and the present `W` is not a finite
Wilson or Villain weight. It cannot be imported as closure.

Reference:
J. Fröhlich and T. Spencer, *Massless phases and symmetry restoration in
abelian gauge theories and spin systems*, Commun. Math. Phys. 83 (1982),
DOI `10.1007/BF01213610`.

Modern lattice work gives numerical evidence that four-dimensional
`Z_N` gauge theories possess a photon phase, and uses three particularly
useful classifiers: the distribution of a smeared Polyakov loop, the
proliferation of center vortices versus monopole junctions, and a connected
plaquette correlator with `1/n^4` decay.

Reference:
J. Giansiracusa, D. Lanners and T. Sulejmanpasic,
*Emergent photons and mechanisms of confinement*,
arXiv `2505.00079v2` (2025).

Neither source proves the phase of the exact TWIST-J weight at `t=1`.
Together they justify a measurement program, not a theorem promotion.

## 7. Prospective measurement contract

No production output may be generated before the code, statistics, random
seed schedule, lattice sizes, update rule, equilibration rule, and decision
grammar are frozen in a dedicated experiment preregistration.

### 7.1 Pilot and production separation

```text
pilot:
  L in {6,8}
  diagnostic t scan permitted
  purpose: code, mixing and autocorrelation only
  evidential weight: zero

production at the fixed point:
  t=1
  L in {8,12,16,24,32}
  at least two independent hot starts and two independent cold starts
  production begins only after all starts agree within the frozen
  equilibration and autocorrelation tests
```

A larger holdout lattice may be added prospectively before opening its data.
A size may not be dropped because its result is inconvenient. A failed
mixing test returns `STOP`, not a phase label.

### 7.2 Reproducibility and numerical integrity

The implementation must freeze:

```text
counter-based random generator and public seed schedule
link-update order
heat-bath or Metropolis transition probabilities
numeric precision and summation order
checkpoint format
autocorrelation estimator
blocking or jackknife rule
complete stdout schema
source and output hashes
```

At least one independent implementation must reproduce the primary
statistics within the preregistered uncertainty budget. Gauge-invariant
observables are computed without gauge fixing.

### 7.3 Primary observables

#### A. Smeared Polyakov loop

For a chosen direction `mu`, let `P_mu(x_perp)` be the product of link phases
around that noncontractible cycle and define

```text
Pbar_mu=L^(-3) sum_(x_perp) P_mu(x_perp).
```

Record

```text
R_L=E|Pbar_mu|,
A5_L=|E(Pbar_mu^5)|/E(|Pbar_mu|^5).
```

Interpretation in the thermodynamic trend:

```text
confined:        R_L -> 0
photon/U(1):     R_L -> nonzero, A5_L -> 0, annular distribution
Z5-broken:       R_L -> nonzero, A5_L -> nonzero, fivefold peaks
```

The histogram is a diagnostic image. `R_L` and `A5_L`, with uncertainties,
own the numerical comparison.

#### B. Vortex and monopole-junction geometry

Choose the principal integer plaquette representative

```text
f_p in {-2,-1,0,1,2}.
```

Define the integer monopole-junction current on cubes by

```text
m_c=(d f)_c/5.
```

Measure separately:

```text
vortex occupied-face density
vortex wrapping probability
monopole occupied-link density on the dual lattice
monopole wrapping probability
largest monopole component divided by four-volume
monopole loop-length tail
```

The expected three-way distinction is:

```text
confined:     vortices proliferate, monopoles proliferate
photon:       vortices proliferate, monopoles do not proliferate
Z5-broken:    vortices do not proliferate
```

Density alone is insufficient. Wrapping and component tails are primary.

#### C. Connected plaquette correlator

For oriented plaquettes use the connected functions

```text
C^+_(x-y;mu,nu)
 =<W_p(x) W_p(y)>-<W_p(x)><W_p(y)>,

C^-_(x-y;mu,nu)
 =<W_p(x)^(-1) W_p(y)>-<W_p(x)^(-1)><W_p(y)>.
```

Use the reflection-positive orientation sum `C(n)` of
arXiv `2505.00079v2`, equation (8). On a periodic lattice, the massless
four-dimensional target is

```text
C_asym(n)=K[n^(-4)+(L-n)^(-4)].
```

The amplitude-free primary statistic is

```text
Q_L(n)=C(n)/C(n+1),

Q4_L(n)
 =[n^(-4)+(L-n)^(-4)]
  /[(n+1)^(-4)+(L-n-1)^(-4)].
```

A photon verdict requires a stable long-distance window in which
`Q_L(n)-Q4_L(n)` tends to zero with increasing `L`, while the signal remains
resolved. The window-selection rule must be frozen before production data.

#### D. TWIST score and dual-current checks

Measure the same-orientation connected covariance of `G_p`. In an
independent dual implementation, measure `n`, `j=partial n/5`, and the
registered screening statistic

```text
R(q)
 =[25 tr S_j(q)+tr S_rho(q)]/lambda(q).
```

The exact Ward identities must hold within the preregistered numerical error
at every checked momentum. Failure is an implementation `BREAK` or `STOP`,
not evidence against the phase.

The primary analytic target is the low-momentum behaviour needed by
`PHOTON-DEFECT-SCREENING-CRITERION`. A strict observed gap is evidence only;
it is not a proof of the infinite-volume inequality.

### 7.4 Phase decision grammar

The production report returns exactly one of:

```text
PHOTON_EVIDENCE
CONFINED_EVIDENCE
Z5_BROKEN_EVIDENCE
MULTIPHASE_OR_TRANSITION
AMBIGUOUS_FINITE_SIZE
STOP_MIXING
STOP_INTEGRITY
```

`PHOTON_EVIDENCE` requires all of the following to point in the same
finite-size direction:

```text
P1  nonzero limiting Polyakov radius with vanishing fivefold anisotropy
P2  proliferating/wrapping vortex surfaces
P3  non-proliferating, non-wrapping monopole-junction worldlines
P4  long-distance plaquette-correlator ratio consistent with the
    finite-periodic 1/n^4 target
P5  exact score/current Ward checks pass
```

No single pretty histogram closes the phase. Conflicting indicators return
`AMBIGUOUS_FINITE_SIZE` or `MULTIPHASE_OR_TRANSITION`.

A numerical result may support a `C` or `D` physical claim at its measured
scope. It cannot by itself promote `PHOTON-MASSLESS-PHASE` to theorem `T`.

## 8. The missing pole-identification seam

Even a proof that the L4 action has a massless phase would not automatically
show that its long-distance pole is the exact D3 temporal characteristic of
v74. The current gates omit this seam.

A later Canon fold should open:

```text
GATE-L5-L6-PHOTON-POLE-IDENTIFICATION
```

Its input is the measured or proved long-distance gauge-invariant
field-strength covariance. Its positive condition must freeze all of:

```text
S1  exact L6 observable and orientation tensor
S2  Fourier convention and Euclidean-to-counter continuation
S3  location and order of the infrared pole
S4  finite positive nonzero residue
S5  transverse projector and rank-two polarization content
S6  normalization map to the unit tangent coefficients of v74
S7  control of lattice anisotropy and irrelevant corrections
```

The result grammar should be:

```text
AGREE       the pole, tensor and normalization map to the v74 germ
DIFFER      an exact or statistically decisive mismatch is exhibited
NONUNIQUE   more than one inequivalent map survives
STOP        continuation, normalization or observable ownership is missing
```

This gate, not the bare existence of a gapless phase, is the final bridge to
a physical photon candidate.

## 9. Scale and apparatus

The coefficient one in

```text
Omega^2-|k|^2
```

is a dimensionless time/space normalization inside the selected dictionary.
It is not yet the measured SI speed of light. A physical scale statement
requires the existing metrological tick/edge lanes and an apparatus
readout. That calibration is downstream of the pole seam.

The phase may be measured in lattice units before SI calibration. The two
tasks must not be conflated.

## 10. Matter can start now

PR #739 also proves the conditional scalar massive extension

```text
4 sin^2(omega/2)=s(k)+mu^2.
```

With `mu=epsilon M`, the same exact error bound gives

```text
Omega^2-|k|^2-M^2
```

as the massive tangent germ. The public bound `s<=16/9` gives the sufficient
all-momentum real-branch condition

```text
mu^2<=20/9.
```

This releases an immediate exact matter-kinematics lane:

```text
P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1
```

with the following strict boundary:

```text
derived:      characteristic, branches, gap and scaling remainder
not derived:  value of mu, species, spin, interaction, occurrence,
              calibration, stability or physical mass
```

The physical mass program remains a separate source/read problem. In
particular, inserting `mu` does not solve `C-MASS-READ-N`, select a species,
or derive a mass ratio.

The spinor matter lane may consume the same Hermitian tangent carrier, but it
must prove its own typed relation between the existing Dirac ladder and the
D3 photon characteristic.

## 11. Analytic theorem lane remains alive

`PHOTON-MASSLESS-PHASE [O]` should remain open as a mathematical theorem
program. Its exact current boundary is:

```text
known:
  positive full-support Z5 face weight
  exact character expansion
  exact score/current Ward identity
  exact defect-screening criterion
  exact finite suppressions and negative results for several naive routes

missing:
  a strict infrared estimate at the fixed weight t=1 strong enough to
  force non-summability of the photon score covariance, or another complete
  theorem chain with explicit N=5 hypotheses
```

A successful measurement should guide this proof but must not replace it.
The preferred analytic attack after measurement is to prove the observed
monopole-junction non-proliferation and the simultaneous vortex roughening in
a theorem-preserving comparison class, with constants evaluated at `t=1`.

## 12. Closure states

Use the following vocabulary.

### `PHOTON_KINEMATICS_CLOSED`

Requires:

```text
v74 temporal characteristic [T]
Herm2 tangent-germ theorem [T]
global separated obstruction recorded [T]
```

It does not require a thermodynamic phase.

### `PHOTON_CONSTRUCTION_FROZEN`

Requires:

```text
PHOTON_KINEMATICS_CLOSED
exact L4 measure at t=1
periodic boundary conditions
primary observables
measurement code and decision grammar pinned
```

This is the state needed to begin production measurement.

### `PHOTON_PHASE_EVIDENCE`

Requires a completed production report returning one of the empirical phase
labels. It carries only the earned evidential status.

### `PHYSICAL_PHOTON_CANDIDATE`

Requires:

```text
PHOTON_PHASE_EVIDENCE=PHOTON_EVIDENCE
GATE-L5-L6-PHOTON-POLE-IDENTIFICATION=AGREE
rank-two transverse polarization evidence
declared scale/readout boundary
```

This may earn `C` or `D`; it is not automatically `T`.

### `PHYSICAL_PHOTON_THEOREM`

Requires a complete theorem chain for the fixed action, thermodynamic limit,
massless pole, tensor structure and typed identification. This remains open.

### `MATTER_KINEMATICS_OPEN`

Begins immediately after the Herm2/massive-germ result is reviewed. It does
not wait for `PHYSICAL_PHOTON_THEOREM`.

### `MATTER_PHYSICS_OPEN`

Requires at least a frozen interaction/readout relation to the measured
photon phase and the separate mass-origin program.

## 13. Immediate repository disposition

The clean order is:

```text
1  review and merge PR #739
2  fold the two photon Herm2 theorems and conditional massive germ in a
   later Canon release
3  split the present cone gate into germ and optional global-carrier gates
4  add GATE-L5-L6-PHOTON-POLE-IDENTIFICATION
5  preregister and implement the fixed-action measurement experiment
6  run pilot with zero evidential weight
7  freeze production thresholds and run t=1 finite-size measurements
8  launch the separate scalar massive characteristic probe
9  use the measured phase structure to choose, not retrofit, the next
   analytic massless-phase theorem attack
```

## 14. Final disposition

The photon is no longer blocked by lack of a propagation law or lack of a
light cone. Those are exact.

It is blocked by one physical question and one dictionary question:

```text
Does the exact fixed Z5 measure at t=1 possess the photon phase?
Does its infrared pole map uniquely to the exact v74 D3 characteristic?
```

Both are now measurable. Neither should be answered by importing a theorem
for another action or by drawing an arbitrary square root of the symbol.

This is enough to move from construction to measurement and, in parallel, to
open exact massive kinematics. It is not enough to call the physical photon
or physical mass proved.
