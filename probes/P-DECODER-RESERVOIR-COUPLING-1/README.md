# P-DECODER-RESERVOIR-COUPLING-1

**NON-CANONICAL / PRE-PIN CANDIDATE / NO SCIENTIFIC STATUS ASSIGNED**

Public reservation: [issue #824](https://github.com/mathorn1973/twist-j/issues/824).
Proposed claim: `DECODER-RESERVOIR-RECORD-ACCOUNTING`.
Action layer: L1 exact mathematical coupling and record accounting.

This probe connects the existing D3 scalar wave recurrence to a chosen
reversible port law. With a fresh zero incoming field on every transition,
wave energy moves into signed outgoing port fields stored on an immutable
tape. Exact per-site heat accounts yield threshold records in atomic
batches. This is a mathematical apparatus adapter, not a completed physical
detector or the L4/L5 profile of issue #539.

## Construction

The context fixes a finite positive rational conductance field `Gamma`
and one positive rational threshold `q`. For old pair `(u,v)` and incoming
port field `a`, solve

```text
p=(w-u)/2,
f=Gamma*(2a-p),
b=a-p,
w=[2v-Lv-(1-Gamma/2)u+2Gamma*a]/(1+Gamma/2).
```

The complete map `((u,v),a) -> ((v,w),b)` is reversible when the signed
outgoing field is retained. Its energy identity is

```text
E(v,w)+sum_x Gamma(x)*b(x)^2
 = E(u,v)+sum_x Gamma(x)*a(x)^2.
```

The cold process uses `a=0` on every step and never recycles outgoing ports.
It accumulates `h_x=sum_t Gamma(x)*b_t(x)^2`, then derives
`N_x=floor(h_x/q)` and `r_x=h_x-q*N_x`. All ordinals from the old `N_x+1`
through the new `N_x` are emitted together in that transition's batch.
The tape energy, heat and threshold ledger describe the same energy;
they are not three stores to be added.

Preparation is the prior probe's centered five-site source `P_0=(0,S(z))`
with `E(P_0)=m(z)/2`. It precedes coupling. Batch tick zero records the
first coupled transition from that post-kick pair. A zero source or empty
conductance support emits empty batches. An empty batch can also mean
positive subthreshold transfer and does not identify a zero source.

Histories retain signed ports and exact post-states. Continuation appends
immutable records; passive rereading does not interact again. No reset or
mutating history truncation is supplied. Queries on overlapping regions of
one history use inclusion-exclusion. Distinct coupler contexts define
distinct evolutions and are not silently combined.

## Frozen source package

- `CONTRACT.md` fixes carriers, coupling, clock, context, choices and scope.
- `PROOF.md` supplies the conditional mathematical proof.
- `PREREG.md` fixes the exact verifier, dependencies, gates and failure rules.
- `coupling.py` supplies the typed coupling, reverse map, cold transition,
  ledger and history API over the immutable predecessor's wave module.
- The verifier and its exact dependency inventory are fixed by the
  preregistration.

The accepted source bundle must be committed, pushed and read back before
formal execution. Later `EXPECTED.txt`, `RUN.md` and `RESULT.md` record the
exact transcript, immutable pin and earned disposition. This README is a
source specification and makes no claim that a formal gate has passed.

## Python API after the public pin

The following is a usage example, not a pre-pin execution instruction or
a reported result. From the repository root, after the accepted source
bundle has been pinned and publicly read back:

```python
from fractions import Fraction as F
import sys

sys.path.insert(0, "probes/P-DECODER-RESERVOIR-COUPLING-1")
from coupling import Context, prefix, extend, threshold_counts

context = Context(gamma=(((0, 0, 0), F(1)),), quantum=F(1, 10))
history = prefix((F(1), F(0), F(0), F(0)), context, 3)
longer = extend(history, 2)
counts = threshold_counts(longer.state.heat, context)
```

The original history remains unchanged. `couple` and `reverse` expose the
general incoming/outgoing port map separately from the cold `advance`.
`Batch.crossings` contains inclusive `Crossing(site, first, last)` ranges;
`.count` gives the number of ordinals in a range. A batch kind is
`THRESHOLD_CROSSINGS` or `NO_CROSSINGS`. The latter can have a positive
deposit. `threshold_counts` includes zero counts for all conductance sites.
No command-line interface is required by this contract.

## Interpretation boundary

The conductance field, threshold and unlimited fresh cold-port capacity are
declared model choices. Threshold labels count units of the chosen energy
account; they are not photons, LOW/HIGH outcomes, Born probabilities or
independent trials. Finite source energy does not imply complete absorption
or threshold crossing in finite time.

The coupling changes the derived wave state, never autonomous `U`. It
does not select a physical source, detector, environment, calibration,
instrument, occurrence law or complete apparatus family. It does not prove
physical terminality, COMM-SAT, a sampling law or an L6 measure.
[#539](https://github.com/mathorn1973/twist-j/issues/539) and the QDD apparatus
obligations remain open; [#744](https://github.com/mathorn1973/twist-j/issues/744)
remains the separate photon-identification boundary.
[#756](https://github.com/mathorn1973/twist-j/issues/756#issuecomment-5500304645)
remains F3 NOT_SATISFIED and
[#742](https://github.com/mathorn1973/twist-j/issues/742) production remains
FORBIDDEN. This work changes no Canon, previous probe or production freeze.
