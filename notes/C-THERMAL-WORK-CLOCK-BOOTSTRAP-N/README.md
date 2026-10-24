# Thermal preparation of the charged work store and polarized clock

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Independent mathematical acceptance is pending.
Public reservation: [#1763](https://github.com/mathorn1973/twist-j/issues/1763).

The charged work site and polarized master-clock input supplied in
[#1761][prior] can be prepared approximately by a finite thermal start.
One local reaction charges the actual old work site, creates the actual
old master entry, and creates a loading cursor. That cursor is initially
empty with the stated thermal accuracy; it is populated by the reaction,
not supplied as a second running timer.

One positive, time-independent local Hamiltonian includes that reaction,
the guarded loading interval, and the preceding finite preparation and
capture program. Every thermal defect, inactive input and entropy-bearing
label stays in the physical system.

The remaining input is explicit: finite Gibbs factors at three temperatures,
their product/contact condition, the admitted logical input and precise
couplings. No initial work peak or inverted clock qubit remains, but the
temperature contrast and nonstationarity under the full interacting
Hamiltonian remain supplied. This is not a derivation from unchanged U_rec.

## 1. Concrete thermal resources

Keep the old payload, retained rows and unused work heads at their
specified common temperature beta_0 epsilon=ln2. Replace the distinguished
work seed and all master-clock sites by cold Gibbs states. Add a cold
loading rail and two finite multilevel sites:

| Site | Physical spectrum | Thermal input |
| --- | --- | --- |
| Hot h | one ground state; D states at (R+3)epsilon | beta_h(R+3)epsilon=ln2 |
| Cold sink c | one ground state; D states at epsilon | beta_c epsilon=b ln2 |
| Distinguished work | levels 0,...,2R in units epsilon | same beta_c |
| Every master/loader cursor bit | levels 0,epsilon | same beta_c |

Let D=2^84. The hot excited population is D/(D+2); each of its D excited
states is separately less populated than its ground state, as required
by positive-temperature Gibbs weights. The sink's ground population is
1/(1+Dz), where z=2^-b.

For each hot label a, the resonant transition is

```text
(a,0,0,0,0) <-> (0,a,R,1,1)
```

in the order h,c,work,old-master-entry,loader-entry. It conserves physical
bare energy because

\[
 (R+3)\epsilon=\epsilon+R\epsilon+\epsilon+\epsilon.
\]

The output sink retains the label a. The high launch weight is paid for
by two sites of dimension D+1, a specified hot gap and a specified cold
temperature, rather than by erasing the hot state's entropy.

## 2. Joint preparation and handoff

Let L be the old completion index, extend the old main tail to length 3L,
and use L loader sites. The complete active history has K=4L edges and
K+1 physical cursor bits. Fix

\[
 b=84+\lceil\log_2(D+K+3)\rceil.
\]

The joint nominated input component has exact weight

\[
 q=\frac{D}{D+2}\,
   \frac1{1+Dz}\,
   \frac{1-z}{1-z^{2R+1}}\,
   (1+z)^{-(K+1)},
\qquad
 1-q<3\,2^{-84}<2^{-82}.
\]

This counts hot-ground failure, the sink, every original and new clock
site, and every nonzero level of the physical work ladder.

The loader's final hop is controlled by the old master entry. The old
first hop is controlled by the loader endpoint. During a proved finite
loading window the actual old work site is near level R, the entire old
master is near its one-entry configuration, and the old payload and
logical reference are unchanged. The loading packet and thermal labels
are retained.

[PREPARATION.md](PREPARATION.md) proves this as a bound on the complete
joint reduced input, not merely agreement of separate marginals.
The extra history error is less than 2^-255. After handoff the old finite
program runs, while the loader remains at its endpoint.

A good forward reaction leaves h in its ground state, and all later
gates leave h,c alone. It therefore cannot launch again. The reverse
reaction remains part of the legal return path.

## 3. One Hamiltonian and inclusive energy

[HAMILTONIAN.md](HAMILTONIAN.md) gives a positive full-space law

\[
 H=H_0+H_{\mathrm{prop}},\qquad [H_0,H_{\mathrm{prop}}]=0.
\]

The inherited finite program and dirty-row implementation are kept.
The clock coefficients and loading controls are new. The maximum term
support remains seven physical sites within Manhattan radius four;
the large dimensions of the physical work and thermal sites are counted.

On a good input, the hot site transfers (R+3)epsilon: the work receives
R epsilon, two clock excitations receive 2epsilon, and the entropy sink
receives epsilon. Interaction energy is an additional part of the same
Hamiltonian. The actual mean and variance include all thermal defects,
all auxiliary rows and every propagation term.

[ENVIRONMENT.md](ENVIRONMENT.md) supplies the exact finite whole-state
energy formulas. It distinguishes an active-component transfer from
the actual mixed-input energy and from a minimum cost of manufacturing
the reservoirs. No rare high-energy component is assigned zero cost.

## 4. Complete output and remaining boundary

The inherited ready-bit compression still has error xi<2^-80. Including
the new thermal defects and finite timing windows gives a pre-conditioning
error budget below 2^-79. After normalization, the accepted-state trace-
distance error is below 75000 times 2^-79.
Under the fixed preceding source and spectral premises, whole-input
accepted weight remains greater than 1/75000 and unwanted accepted
fraction remains below 1/10^6. The occupied-memory/reference channel is
approximate for the actual thermal input.

The near-unit factor q here concerns the new thermal preparation.
It does not remove the old environmental activation factor 4/15 or turn
the capture experiment into a near-unit-success experiment.

All nonlogical input factors are full-rank Gibbs states at positive finite
temperatures. They commute with the additive bare energy. Nevertheless
the resonant input/output weights differ, so the full generator has a
strictly nonzero initial commutator. The exact witness is in
ENVIRONMENT.md.

The initial temperature contrast, cold preparation, hot degeneracy,
product boundary and physical couplings have not been produced from a
stationary total state. There is no bath refresh, useful reset, permanent
halt, physical occurrence law or material implementation. [NATIVE.md](NATIVE.md)
separates those additions from the original law and explains why the
parallel [#1762](https://github.com/mathorn1973/twist-j/pull/1762) capacity
result does not transfer automatically to this changed resource class.

[VALIDATION.md](VALIDATION.md) records fixed inputs, the actual checks and
falsifiers. This is an analytical candidate; no new scientific executable,
simulation or gate-enumeration run was performed.

[prior]: https://github.com/mathorn1973/twist-j/tree/32c17259c4baf40bb6d08b521adc642956b57e94/notes/C-THERMAL-REGISTER-PREPARATION-N
