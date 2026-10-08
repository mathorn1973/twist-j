# C-FIELD-STATIC-TRANSPOSITION-COMPLETION-N

**NON-CANONICAL. Conditional candidate-T proofs; candidate-C finite audits;
L1. No public gate, source-derived physics or Canon promotion.**

This continuation completes the static contacts involving vertex 2 that were
left open in the supplied C-FIELD-STATIC-CONTACT-SYMMETRY-N bundle. It also
strengthens the contact-context obstruction of PR #1424: requiring the
completed contacts to commute with both G and F still allows identical
complete final old states with different last receiver energy changes.

## Main result

For each pair ij in {01,02,12}, let P_ij be the unique static electric-field
correction accompanying the entire-register swap b_i <-> b_j, compensated
by r'=r-kappa in the selected H1 account. Write aG(s)=1 exactly when the
inherited complete reaction G accepts. Define

```text
S_ij(s) = P_ij(s), if the proposal is integral, its stock is nonnegative,
                      and aG(P_ij(s))=aG(s);
          s, otherwise on the entire state.
```

All three S_ij are complete involutions preserving H1, the full Gauss defect,
matter, magnetic field and the rational active field coordinates. They
commute with complete G and F and, leaving every pointer value unchanged,
with the recorded reaction Ghat.

For an accepted reaction input the exact condition is

\[
5\mid t,\qquad \kappa\le\min(r,r+\delta_G),\qquad
\delta_G=r(Gs)-r(s).
\]

The rule funds both sides of the complete reaction/contact square. It also
allows contacts between G-rejected states when both remain rejected. A
proposal that changes G acceptance is entirely refused.

For the fixed proposal, S_ij is the unique map with the greatest nonidentity
support among complete proposal-or-identity maps commuting with G. The
competitors need not be assumed bijective. This is precisely scoped
maximality; proposal choice and a maximal-support occurrence rule are still
premises.

## Nonzero static price is compatible with F

At m=R, b=(5v,-5v,0), E=(2,2,1,1), M=0, r=7 and v=(1,0,0,0), the active
field is zero. Both S02 and S12 have price +5, change stock to 2 and are
accepted on the full G square. The total cell energy is 335 throughout.
Their electric outputs are (1,1,-2,3) and (1,1,3,-2), respectively.

At r=5 or6 the same raw proposal is individually funded but would change
G acceptance. The completed contacts correctly refuse it. Both independent
programs find the prescribed failure of the naive own-stock-only rule.

| Complete law | Conserved members of the specified Hc family |
|---|---|
| S01 | Every admissible c |
| S02 | Exactly c=1 |
| S12 | Exactly c=1 |

Here Hc=H1+(c-1)(r mod2), and the specified admissible parameter domain
contains 1. The +5 witness gives Delta Hc=1-c. Sufficiency of c=1 follows
from the universal proof, not the finite audit. Since the stock compensation
was defined using H1, this is not an independent derivation of that energy.

## A new exact readout obstruction

Let T be the inherited complete two-cell step and apply receiver S01 or S12
after it. The two frozen histories reach the same complete final source,
receiver, link eta=0 and pointer p=0. The receiver is the common PR #1424
state with energy 424. Their accounts are:

| Quantity | T followed by S01 | T followed by S12 |
|---|---:|---:|
| Initial source energy | 81 | 86 |
| Initial receiver energy | 343 | 338 |
| Initial receiver matter | AM | AM |
| Initial receiver stock | 6 | 6 |
| AM funding remainder | 0 | 0 |
| Final receiver energy | 424 | 424 |
| Last receiver energy increase over the whole step | 81 | 86 |
| Field price of the final contact | 0 | 5 |
| Full old-carrier energy including the same pointer energy 1 | 425 | 425 |

Both completed contacts commute with G and F. Their input fields, all
intermediate full states, acceptance checks and final coordinate equality
are explicit in ADDENDUM-READOUT.md and proved in PROOF.md section 9.

There is no exact context-free function of that final old state returning
both last changes. Every real common estimate has worst-case error at least
5/2 on this pair. A retained, accessible binary contact label suffices for
the abstract two-law controlled inverse, while physical preparation and
implementation of that label remain open. The expanded complete states
include the label, so reversibility of one specified complete law is intact.

## Completed verification

The specification was frozen first, the additive readout witness was recorded
before execution, and both independent source programs, the proof and a
separate text-only assistant review were jointly pinned before the first
run. All seven frozen claims survived both first audits:

| Audit | Input cases | Complete contact cases | First result |
|---|---:|---:|---|
| Exact rational split and quadratic forms | 14513 | 43539 | PASS, exit0, empty stderr |
| Independent raw integer residues and field updates | 74384 | 223152 | PASS, exit0, empty stderr |

Counts are visits in explicitly frozen domains, including repeated states
in different checks. Every contact case checks all five pointer values.
Both runs used Ubuntu 24.04.3 LTS, x86_64, Python 3.12.14; durations were
15.065681 and13.230204 seconds. No scientific source was corrected after
the pin, and no first failure or rerun was discarded. Full first outputs,
all branch counts, hashes and timestamps are retained.

REVIEW.md is an exposed review by a separate assistant context that did not
read the programs or their outputs. It checked every proof and both full
T7 histories by hand and found no substantive defect. The participants had
discussed the analytic construction, so this is not blind discovery or
external peer review. One local architecture is not the public
two-architecture gate.

## Remaining exact boundary

These laws do not generally commute with the incident stock swap B. A
specific occupied-stock counterexample is proved and audited. They also
cannot be implemented by finite words in the audited old G/F/stock-swap
alphabet on the same carrier: those primitives preserve each actual node
charge, whereas the new contacts move charge.

A physical closure must still provide an independently admitted source
transition, its actual contact selection and full stock outputs, a physically
available apparatus/interface with readable context, and calibration of the
quantities. Greatest-support completion and H1 funding supply a consistent
mathematical law, not its native source occurrence. Geometric metric/unit
questions, Hilbert coherence and the complete-model photon phase are unchanged.

The supplied bundle's fired S3 and S4b claims stay fired. Its zero-price and
nonzero-charge wording requires the nonzero-charge restriction; no source
file or first-run record was rewritten. PR #1424 and Public Canon v100
retain their existing public state; this package has not been published.

## Package map

| File | Purpose |
|---|---|
| PROOF.md | Universal arguments, explicit witnesses, maximality and physical limits |
| PREREG.md | Original frozen carrier, equations, six claims, domains and failure rules |
| ADDENDUM-READOUT.md | Additive T7 and both complete histories, frozen before execution |
| REVIEW.md | Separate text-only assistant proof review with exact reviewed hashes |
| FREEZE.md / FREEZE.json | Pre-execution custody of texts and sources |
| verify.py / break_check.py | Separately authored exact audit implementations |
| run_once.py | First-run custody wrapper; it refuses to overwrite existing first records |
| RUN.md / AUDIT-SUMMARY.json | Actual environments, counts, status and reproduction commands |
| *.first.stdout / *.first.stderr / *.run.json | Complete first outputs and machine run records |
| SOURCES.md | Checked public authority, immutable links and attachment custody |
| PROMO-C-FIELD-STATIC-TRANSPOSITION-COMPLETION-N.md | Precisely scoped proposal for later public review |
| SHA256SUMS | Integrity manifest for every other package file |

For replay, use the ordinary interpreter commands in RUN.md and compare to
the respective first stdout. No third-party packages, network, hidden data,
or original uploaded programs are needed. The SHA256SUMS manifest excludes
itself and the outer ZIP to avoid recursive hashing.
