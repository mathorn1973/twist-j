# Conditional finite-horizon reserve enclosure

**NON-CANONICAL / SOFTWARE DEVELOPMENT / conditional mathematical relation.**
No physical component is qualified here. No formal prospective scientific run
has been reserved or performed. The numerical budgets are hypothetical inputs,
not inferred efficiencies, measurements, or an alternative to the #1318 limits.

## Fixed scope and three different sets

The law is #1316 at `312d0a90b24d5f9e743096f0ee2a477cda719a10`, with the
#1318 apparatus proposal at `4756a3df650b91fb1d30806b0fb2aaac00e50cc2`.
The certifier reads `primary.py` with SHA-256
`11009d50a61a6e158aeffd9f1fde5bd867ccfb286b38029f985774d9155eb705`;
that source checks its inherited local arithmetic at SHA-256
`42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59`.
Neither source's `main`/scientific audit runs. These are declared logical inputs,
not an independent implementation of the integer law or a physical trace.

Let the bank order be `(B0,Z0,r0,B1,Z1,r1,B2,Z2,r2,q0,q1)`. Counts sum to 41;
epsilon is the stipulated 1/2 J. The separate C5 pointer offset is not a twelfth
capacitor or a donor. Each energy is relative to its physical serial's fixed
reference energy. Its baseline remains in the apparatus balance.

* `Dec(x)` is the broad #1318 relation, including the digital state, physical
  pointer, identity permutation, READY auxiliary phase, valid volts and
  `abs(E_inc - n/2) + U_E <= 0.240 J` at settled boundaries.
* `Prepare(x)` is a chosen nonempty initial true-energy box `E_inc=n/2+e`, `abs(e)<=b_prepare`,
  with `b_prepare+2*U_E<=0.020 J`, correct registers/docks/p, and READY auxiliaries.
  The supplied independent boxes also obey the conservative source-equality
  bound `6*b_prepare+2*U_difference<=0.010 J` across positive/offimage trials.
* `Enc_oper(x; schedule, budgets, assumptions)` is the part of `Dec(x)` covered
  by this finite-horizon enclosure and **all** the stated physical transition,
  calibration and timing assumptions. A software result can establish only
  the conditional implication. Calling this set physically qualified requires
  independent qualification of every assumption for the actual units/history.

The known broad-decoding counterexample is compulsory: initial `(B,Z,r)`
energies `(8.780,0,0.780)` at counts `(18,0,2)` meet the broad bands when
`U_E=0.020`. Their sum is 9.560 J. A count-20 B endpoint requires at least
`10 - 0.240 + 0.020 = 9.780 J`. Without injected energy or commanded baseline
borrowing, even a lossless operation cannot produce it. The 0.220 J shortfall
refutes universal invariance of Dec. Permitting negative zero-account energy
cannot repair this example by *commanded* baseline withdrawal; that remains
prohibited. The certifier's preparation assumption is materially narrower.

## Local identity, including zero accounts and signed input

For a local accepted reaction define `d_a=n_a/2-E_a`,
`S=sum(n_a)=sum(n'_a)>0`, and the signed net reduction
`L=sum(E_in)-sum(E_out)`. Define actual residuals by

```
E'_a = (n'_a/S) * sum(E_out) + xi_a.
```

Summing the defining equations gives `sum(xi_a)=0` exactly, including all
zero-count accounts. Substitution of `sum(E_in)=S/2-sum(d_a)` proves

```
d'_a = (n'_a/S) * (sum(d_a)+L) - xi_a.
```

No efficiency assumption is used in this identity. More generally,
`L=D+Delta A-I`, where `D>=0` is actual dissipation/output work, `Delta A`
is increase of separately accounted auxiliary storage, and `I` is signed
external injection. The three terms must not be conflated or replaced by a
net loss fitted after seeing a result. Gross dissipation limits are checked
without subtracting injection.

For `n'_a=0`, the equation is `E'_a=xi_a`, `d'_a=-xi_a`. A negative residual
is a below-reference baseline deviation, not a negative physical capacitor
energy. Its voltage floor and idle drift remain constrained. Its residual is
included in the zero-sum constraint; dropping it corrupts the positive-bank
allocation. The accepted #1316 endpoints have matter energy at least 18 and
therefore S>0. An alleged accepted S=0 input is rejected by the software before
division. A rejected G, including S=0, is identity followed only by declared
idle/measurement disturbances; it does not redistribute its local energy.

The supplied G relation has READY auxiliary energy exactly zero at both ends.
It permits up to 32 donor starts. Each start has a separately bounded donor-fed
storage charge, subsequently discharged as metered heat before another donor
starts. There is no returned startup energy credit in this conservative model.
The entire G's conversion loss and each start's startup, tail and switching
loss are charged independently. Thus

```
D_G <= b_conversion + 32*(b_startup+b_tail+b_switching).
```

Here the per-G conversion category must include **all remaining G losses**,
including equalization, converter conduction, bank ESR/dielectric heat and
work-port sensing burden not already assigned to an explicit category. It
must not be fitted only to a converter efficiency curve while omitting bank
losses. Measurement-window draw is separately added after that operation.

An aggregate startup variable in `[0,32*b_startup]` is the exact projection of
32 independently bounded charges onto their sum. Each individual storage peak
is separately enclosed by `[0,b_startup]`; its READY end value is zero. The
event record reports the count, peak and reset. Starting a donor without the
reset or carrying nonzero READY energy is outside the relation and rejected.
The chosen relation spends every startup charge, so it overestimates loss
when a qualified implementation returns energy. A future return-credit model
requires explicit metered storage correlations, not silently reducing this one.

Within a G there is no unaccounted injection. Signed probe/contact coupling is
modeled separately at the declared events. The relation abstracts the unknown
servo dynamics and requires a qualified endpoint residual. It is not a proof
that the proposed analog equalizer converges.

## Exact reachable enclosure and its proof

Represent each physical incremental energy by a rational affine form in
independent uncertainty groups. Each scalar loss group is `[0,b]`, each signed
preparation/injection group is `[-b,b]`, and each G residual group is

```
Xi(b) = { (x0,x1,x2): sum(x)=0, -b<=xi<=b }.
```

Xi is a hexagon with vertices given by the six permutations of `(-b,0,b)`.
The exact support in direction `(a0,a1,a2)` is
`b*(max(a)-min(a))`; the minimum is its negative. Scalar box supports are
equally exact. Because groups are independent, the support of their affine
sum is the sum of supports. Equal and opposite coefficients of the same
group cancel before supports are taken. Correlations created by past gates,
shared startup losses, contact permutations and residual sums are retained.
Loss of correlation is not used to turn an interval into a favorable result.

**Conditional finite-horizon proposition.** Fix one of the supplied logical
traces and a budget model admitted by the schema. Suppose the initial physical
state lies in Prepare, every primitive satisfies its stated relation, all
calibration/voltage/transient/timing/interlock assumptions hold, and all exact
inequalities in the generated certificate are satisfied. Then every physical
settled bank state after every prescribed primitive is in its Dec interval;
all bank voltages satisfy 4.7..50 V throughout the schedule under the transient
assumption, and no reset of the finite-horizon reserve is required. The
no-commanded-baseline and no-external-replenishment requirements are explicit
physical premises, not conclusions inferred from favorable final energies. A
nonzero incidental-coupling envelope does not establish zero external input;
the supplied successful example has zero such injection bounds. The
separate work conclusions hold only where their additional inequalities are
included. The proposition does not imply that the device assumptions hold.

**Proof.** Initially, the forms parameterize exactly the declared independent
preparation box. At an accepted G, conservation plus the displayed identity
maps old forms to `(n'/S)*(sum(E)-D_G)+xi`. The allowed losses and xi add exactly
the declared new uncertainty sets. At a rejected G the forms remain unchanged
before passive drift. A/B permute entire bank forms and serial identities,
then add separately bounded contact dissipation and signed disturbance. A cut
is identity on its two contacts and retains the original channel. F preserves
bank counts/energies before passive drift. At every layer add each serial's
idle loss for that exact duration, one fixed measurement-window load and signed
probe coupling. This proves enclosure by induction for either layer order.
Exact support gives upper/lower energies and both Dec inequalities. The
calibrated inverse-map envelope implies the voltage bounds at those energies.
The assumed path lies inside the endpoint hull plus the bounded sag/overshoot;
testing both endpoints therefore bounds every intermediate energy. Timing and
controller assumptions fix the duration without changing clocks after a
failure. This completes the induction over the finite schedule. No claim on
later steps, all S42 states, or unconstrained auxiliaries follows. QED.

The preparation box is nonempty: all initial errors zero, every bank exactly
n/2 J above reference, READY storage zero, and p=0 is an explicit witness for
every declared preparation. No numeric conclusion relies on an empty set.

The affine energies are **true physical energies**, rather than meter centers.
Assume each reported estimate differs from its true quantity by at most its
declared uncertainty U. To guarantee the frozen measured predicate
`abs(estimate-n/2)+U<=tolerance` for every possible estimate, this certifier
requires `max(abs(true-n/2))+2U<=tolerance`. One U covers a possible estimate
error and the other is the U explicitly added by the predicate. The analogous
doubling is used for work, source equality, swap disturbance and idle hold
differences. The complete A/B-slot disturbance of the same physical serial is
bounded by `b_swap_dissipation+b_swap_injection+2.5*b_idle_per_second+
b_read_dissipation+b_read_injection+2*U_swap<=0.005 J`. This includes its
settled-read window and does not subtract a fitted passive drift from the
frozen endpoint difference. Each cumulative per-serial hold constraint is
`t*b_idle_per_second + reads*b_read + 2*U_idle_difference <= 0.020 J`.
The separate hold-difference uncertainty is not inferred from bank-map U_E
or treated as zero; the hypothetical supplied value is 1 mJ. Gross losses
enter this inequality before any injection credit. It is a
conservative sufficient condition, not a change to the original measured
threshold. The supplied energy U is 5 mJ and work U is 10 mJ. The counterexample
above chooses a zero-error meter realization with U=20 mJ, so its original
9.560/9.780 arithmetic remains unchanged.

## Continuous-time and calibration assumptions

The supplied energy-map envelope is **hypothetical** for every serial, allowed
temperature and frozen settling history. Its lower voltage threshold is
`-3201/125000 J`, its upper threshold `1089/50 J`, and each reference baseline
lies in `[11/50,33/100] J`. These numbers can be motivated by capacitor sizing
but are not a calibrated CV-squared law. They must be replaced by qualified
conservative bounds on actual U(V,T,history), while retaining the frozen
physical thresholds. Baseline ranges travel with physical serial identity.

Every operation's actual incremental energy must stay between its two
endpoint energies, widened by `b_sag` below and `b_overshoot` above. This is a
qualification assumption including inductor/filter energy, switching spikes,
donor changes and measurement windows. Endpoint voltage checks alone do not
prove it. Withdrawals commanded by the servo stop at reference; negative
reference deviations are passive/measurement residuals only. Those separate
assumptions are not inferred from the affine endpoint certificate.

The model requires G <=32 transfers and <=1.7 s, A/B operation <=2.2 s, F
<=0.1 s, and timestamp uncertainty <=1 ms. Slots remain G=2 s, A=B=2.5 s,
F=3 s, in either chronology. These are explicitly unqualified assumptions,
not measured runtimes or a convergence theorem. The final relative residual
must include its own calibration uncertainty and be <=5 mJ; control resolution
is separately <=1 mJ. A 20 mJ absolute bank-map uncertainty cannot establish
either relative requirement.

The three donor-fed converter assemblies and their internal rail/storage
energy are included. The isolated fixture, wheel, FPGA/readout and host rails
remain externally powered auxiliary systems with independent apparatus
ledgers; the declared no-hidden-path assumption and signed coupling budgets
bound any route from them into banks. This certifier does not establish their
total energy balance, safety, mechanical completion or physical pointer
qualification. Those remain separate apparatus prerequisites.

## Work is an additional constraint, not a decoding consequence

In positive forward-first schedules, the receiving step-3 G uses signed work
over its entire 2 s slot. The conditional balance is

```
W_B = Delta E_B + passive/read dissipation + B-internal heat - probe injection.
```

B-internal heat has its own nonnegative bound. This relation assumes every
remaining B energy route is measured or bounded; it is not an actual VI
measurement. B-internal heat is already a portion of total G dissipation;
its separate bound is needed to enclose terminal work and is not added twice
to the gross bank ledger. Treating this bound independently of total G loss
enlarges the enclosure conservatively; it does not assert that a corner with
positive B heat and zero total loss is physically attainable. The frozen
predicates use the measured W and subtract/add U once.
For the true-work enclosure require `W_lower-2*U_W>=0.950`,
`W_upper+2*U_W<=1.050`, `E_other<=0.010` and
`W_lower-2*U_W-E_other>=0.950`, in joules, so every admissible measured estimate
satisfies those predicates. The conservative other-energy bound
includes all five initially model-zero r/q cartridges and the receiver's Z2
positive preparation error (`6*b_prepare`), every possible positive injection
into any bank since source startup, and an explicit unresolved contribution.
This deliberately overcounts routes that cannot reach the target. No loss is
credited against it. Baseline borrowing, precharged donor auxiliaries and
unbounded other sources are forbidden, not fitted away.

For controls the separately supplied bounds are **integral abs(VI)** including
uncertainty, per complete G and over all eight non-G seconds of each macrostep.
The latter includes leakage/switching current during A/B/F and their read
windows. Isolation and unchanged endpoint energies do not imply zero absolute
work: an out-and-back current can have zero signed integral. The supplied
zero non-G bound is an explicit unqualified hypothetical premise, requiring
independent evidence before it can be used for an apparatus. Both the <=10 mJ
G-slot bound and `10*(b_abs_G+b_abs_outside_G)<=0.020 J` whole-100 s block
bound are checked, the latter at complete macrostep boundaries in either
chronology. Summing uncertainty-inclusive subinterval bounds is conservative;
a small net integral is never substituted. There is no VI acquisition in this
package. The inverse-first block has its own full
bank certificate and does not assert the forward step-3 work/arrival rule.

## Coverage, maximum budgets and failure meaning

The program covers positive, the one fixed equal-energy offimage preparation,
cut0 and cut1, each for forward100, forward/inverse200, inverse/forward200.
The 20 known H(w)=1 vectors are checked against the same count/admission trace
for positive/cuts. Offimage is one repeated logical preparation, not 20 new
controls. The pure mathematical class check includes the publicly known
holdout orientation; no end-to-end device tuning or physical holdout trial is
performed. Both inverse orders recover all 96 logical words. Every layer,
every read window, occupied contact, rejected G and cumulative idle exposure
is represented. In cut0, ten/20 accepted Gs consume ten/20 independent gate
budgets without an external recharge.

For each category, the program holds the other input budgets fixed and solves
the rational linear certificate inequalities for the admissible interval of
that category. It reports the exact upper endpoint, limiting bank/operation/
time, once for encoding and once including work. These are maxima **for this
sufficient enclosure and conditional relation**, not optimal physical loss
tolerances. Taking all individual maxima simultaneously is invalid. Temporal
and calibration constants remain fixed while loss categories are varied.

`NOT_CERTIFIED` gives the first violated constraint in check order with its
exact rational margin and, for affine bank/work failures, an attaining
uncertainty corner. This corner is a witness inside the declared abstract
relation, not observed hardware failure. A corner need not be realized by a
particular more constrained analog implementation. Failure of this sufficient
enclosure therefore does not prove impossibility of all implementations.
Even a successful result is always `CONDITIONAL`, never `QUALIFIED`.

The generated report's supports and rational inequalities are a reviewable
certificate of this implementation and proof; they are not an independent
second implementation of affine propagation. Independent numerical/proof
review is recorded in REVIEW.md. A separately reserved formal audit is still
required before a computational or theorem-status promotion.
