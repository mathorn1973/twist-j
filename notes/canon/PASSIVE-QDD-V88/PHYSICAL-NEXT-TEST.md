# Next physical test: predict one spatial energy output

**NON-CANONICAL / PROSPECTIVE DESIGN / NO DATA OR TEST EXECUTION.** The
completed algebraic calibration probe supplies a falsifiable conditional
prediction. It supplies no device, physical dictionary, uncertainty budget
or occurrence law. This note starts no probe and authorizes no acquisition.

Basis: the #830 [port calibration contract](https://github.com/mathorn1973/twist-j/blob/fd512f50d90382124e7c00afa926c8083fd56e06/notes/DECODER-PORT-OBSERVABLE-CALIBRATION-1.md),
the #832 [finite passive realization design](https://github.com/mathorn1973/twist-j/blob/fd512f50d90382124e7c00afa926c8083fd56e06/notes/DECODER-PASSIVE-REALIZATION-BRIDGE-1.md),
and P-QDD-PASSIVE-QUADRATIC-CALIBRATION-1, PROOF.md sections 3–5. Prior
issue readbacks retain these as physical definition lanes. The earlier
bounded signed-response source audit qualified none of its inspected
archives; that is not a search of every possible archive.

## 1. The concrete target and measurements

Test the **first cold transition**, with the five-site centered preparation
`P0=(0,S(z))`, the specified sixty-displacement stencil and nominal
conductance one at the seven calibration sites
`(110),(101),(011),(200),(-1,-1,0),(-1,0,-1),(-1,0,1)` and origin. These
eight ports can coexist at this first cut. Preserve their marking and order.

A possible classical analogue follows #832's energy-coordinate construction,
using a finite Dirichlet domain containing `(source sites union ports)+B`,
where B is zero plus the complete stencil. Keep the full boundary diagonal
8/9. Its existing one-cell, g=2, three-mode component is **not this test**;
the five-source, g=1 finite map and its implementation require their own
certificate. Optical modes need not be physical local D3 sites.

Before outcome access, fix the device or archived apparatus, source-state
map, finite domain, port order, reference planes, phase/polarity, observation
band, amplitude range, cold-input bound, first-cut window and normalization.
Fix an independently calibrated `E_star>0` in joules. In #832's convention
`alpha=sqrt(E_star/2) J(u,v,a)`, prepared input energy is `E_star*m(z)/2`
and each g=1 exported-port energy is `E_star*D_j`. Measure:

- The launched signed/complex source coefficients independently of the
  tested response; convert to z and compute the three dimensionless atom
  weights t,l,r. These are source quadratic estimates, not automatically
  three measured fragments of input energy.
- Exported energy `mathcal E_j` in joules at all eight marked outputs;
  use `Dhat_j=mathcal Ehat_j/E_star`. The origin is the validation output.
  Preserve raw traces, calibration provenance, losses and invalid records.

An energy channel must not define its output by squaring the response that
it purports independently to test. If a mechanical route is selected
instead, #830 separately requires `A0` in metres, `tau` in seconds,
`E_star` in joules, signed force/motion calibration and a work/heat bridge;
discrete energy is not automatically the measured work integral or heat.

## 2. Separate calibration, identification and validation

**Sensors:** establish gains, phases/polarities, offsets, delays, energy
integration and E_star from independent references. Retain shared-reference
correlations. Do not calibrate sensors by imposing the target matrix.

**Apparatus identification:** characterize the actual transfer, source map,
conductances and leakage on separately identified records. Freeze their
joint admissible set and the extraction pipeline before the validation
records are acquired or opened. A measured interval near gamma=1 is not an
exact rational value. Its deviation needs a model-error allowance. In #830,
a signed warm ratio can identify conductance conditionally; energy-only
identification retains the g versus 4/g ambiguity. Do not choose its branch
from the target output.

**Validation:** use predeclared source preparations, with unchanged settings.
Extract the atom estimates and seven calibration-output energies without
fitting to the origin, then compare the independently retained origin.
“Held out” here means excluded from fitting and context selection; the
mathematical target was already explored and is not empirically blinded.
Keep every attempted record and its disposition, including invalid ones.

## 3. Exact residual and ownership of every error

For unscaled `xhat=(that,lhat,rhat,Dhat_1,...,Dhat_7)`, use the frozen vector

```
c=(-6480865109/82312993800, 6549292699/49387796280,
   6551015617/49387796280, -111027113/111030330,
   -111027113/111030330, -9409883/9409350, 1556538/1568225,
   -11092/313645, -11092/313645, 0).
Rhat=Dhat_0-c*xhat;                 ideal R=0.
```

For independently justified componentwise readout bounds epsilon_a on each
atom estimate, epsilon_d on each calibration deposit and epsilon_0 on the
origin, the proved algebra gives

```
|Rhat| <= epsilon_0+A*epsilon_a+B*epsilon_d+S_sys,
A=84944136907/246938981400,
B=751911453/185050550.
```

The sum A+B is `64211196595109/14569399902600`; it is an exact additive
error gain, not an empirical tolerance. S_sys must be independently bounded
before validation. Define it as an upper bound on
`|Delta_0-c*Delta_x|`, where Delta is the physical-to-ideal mismatch over
the admitted source/context set. Its owners are: source preparation and
mode leakage; actual geometry/stencil and boundary; conductance, losses,
crosstalk and device drift; timing/window and continuous-to-discrete map;
and normalization/energy-boundary correspondence. Assign each uncertainty
once, preserving joint dependence; no unexplained remainder is set to zero.

With complete certified bounds, an observed residual exceeding this allowance
rejects that specified device/dictionary/context claim. Otherwise it is
bounded compatibility on the tested scope. Undefined bounds mean STOP,
not rejection or agreement. Any statistical decision rule additionally needs
its own sampling assumptions and error level fixed before data inspection.

## 4. What can proceed now

The first target can be a **deterministic classical analogue**, tested
pointwise on controlled source vectors. No random head selection, trials,
Born rule or photon interpretation is needed. Demonstrating a manufactured
analogue would validate its admitted map, not identify autonomous U with
Nature. For ensemble means, the same identity follows by linearity only
under a common independently specified preparation law. Repeated contexts
need evidence of that common law; neither independent sampling nor
frequency convergence follows from the theorem. Threshold counts require
additional information and are outside this energy-only test.

**GO for a later measurement protocol** requires an actual device or a
qualified public archive supplying the mapped preparation, eight outputs,
independent calibrations, complete uncertainty/custody record and frozen
decision rule. #832's full finite-map and #830's metrology certificates
must refer to that same instance. The prior public-archives-only scope
does not authorize new laboratory acquisitions. The actionable next step
within it is metadata qualification against this explicit input list,
before opening any new outcome payload. Currently missing instance,
physical source/readout certificates and numerical budgets keep the
measurement at **NO-GO / INPUTS NOT YET QUALIFIED**. No new acquisition,
payload opening, formal probe or physical owner closure is performed here.
