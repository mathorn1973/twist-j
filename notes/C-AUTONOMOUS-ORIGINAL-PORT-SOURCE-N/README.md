# Autonomous thermal preparation and readout at the original ports

**NON-CANONICAL, L1, conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. Date: 2026-10-25.
License: Apache-2.0.

This successor connects the frozen original-port source preparation to
one local, positive, time-independent Hamiltonian. Its initial source,
work ladder, clocks and helpers are supplied as independent local Gibbs
states at two temperatures. An original occupied memory and an optional
setting are admitted information inputs. One thermal launch prepares the
specified source, returns it to its original ports, executes three
compiled original steps, and returns their output to those same ports.
Both availability windows have physical flags and joint error bounds.

The construction conserves the stated occupation-based energy H_0 and
the complete interaction energy. It does not identify this energy with
the original spectral Q=E_0 f(U_rec), derive the hardware from the original
six-pentit transition, or supply a factory that prepares the initial
thermal banks under the interacting Hamiltonian.

## Target, inherited premises and new conclusion

The target is the active-contact source pair of
[#1775](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399173427),
with the original receiver at100 and arbitrary old memory/reference.
Writing chi=alpha_(97,0), its two states are

```text
psi_±=[I ± (U_rec^2-U_rec^(-2))]chi/sqrt(Z),
Z=(39521+154sqrt(5))/15625.
```

Their equality of initial configuration probabilities and complete
U_rec spectral measures, and their three-step write contrast

```text
Delta_p=65536(48533-10985sqrt(5))
        /[5^9(39521+154sqrt(5))] > 1/50,
```

remain conditional source premises. The predecessor
[source-preparation package](../C-ORIGINAL-PORT-SOURCE-PREPARATION-N/README.md)
provides the exact unitary word and its complete funded local gates.
It is preserved byte for byte. The present result supplies their common
autonomous schedule and actual thermal readiness contract.

For every admitted setting, old memory and passive reference, choose
integer k>=8. The actual finite-temperature evolution has:

- A predetermined early source window, with first-flag probability
  p_A>1/4 and conditional joint distance less than 6*2^(-k-1) from
  the prepared source channel at the original physical ports.
- A later window [T_h,2T_h], with final-flag probability p_B>1/4 and
  the same joint error bound from the complete U_rec^3 output channel
  at the original physical ports. All old-content/reference branches
  are retained, including unsuccessful writes.
- Exact return of the cold-ground comparison density at3T_h. The
  actual probability of either raised flag then is at most2^(-k-1).
  The useful outputs are undone by this recurrence.

The flags certify completion, not successful capture or a successful
write. The dormant fuel branch is retained. Their probabilities are not
two independent opportunities to start: both programs share one fuel
activation of probability1/3 in the comparison state.

For k=40 and old memory in K_mem=span(d1,...,d25), the final receiver
contrast conditional on completion remains greater than1/100. The
source preparation itself is valid on the full26-state memory code.
A fully thermal setting C=I/2 is also possible: retain C and compare
the two settings in a final joint query, with the extra conditioning
normalization proved explicitly. This supplies a random retained
setting, not a freely selected setting from a thermal bit.

The two windows are separate cuts of the unmeasured evolution. A
physical measurement of the early flag generally changes the clock.
No sequential measured-experiment claim is inferred by concatenating
the two endpoint bounds.

## Fixed local law and complete resource count

[PROGRAM_RESOURCES.md](PROGRAM_RESOURCES.md) specifies the exact word,
original occupation ports, thermal launch and physical inventory.
There are1102 four-level occupation factors with native charges
(0,2,2,8), 4414 ladder factors of dimension26469, and2210 zero-energy
qubits per payload row. Of these qubits2209 are cooled helpers and
one is the retained setting. With

```text
n=2208, M=2209,
r=2(k+ceil(log2 M)+1),
G_star=512n^4 4^n,
P1=M(2r^2-r)+G_star, P2=3G_star, P=P1+P2,
S=7726+2Mr,
```

the total site count is

```text
N_total=S(P+1)+K-r1-r2+3.
```

The last terms count the colored cursor, fuel and two flags. The exact
raster lengths r1,r2, padding and K=12B are given in
[STATIC_CONTROLLER.md](STATIC_CONTROLLER.md). Future copies start in
Gibbs states; complete whole-site SWAPs restore them exactly after each
excursion without assuming pure or uncorrelated transport contents.

Fix epsilon>0 and g>0 before enlarging the construction. The Hamiltonian
is positive on its entire finite raw space. Each displayed summand has:

```text
support <=9 physical sites,
Manhattan radius <=1024,
incidence at each site <=64,
norm <=J=max(26468epsilon,g).
```

Here the geometric units and site dimensions belong to the explicitly
declared added implementation. A site can have dimension26469; this is
not an all-qubit or nearest-rung interaction claim. The exact clock law
has

```text
T_h=pi hbar(K+1)/(3g).
```

The growing apparatus is not accelerated by increasing g. At k=40 even
the original payload row has476034 sites, including468308 reset donors.
The P copy rows and all cursor sites are additional. The bound is a
finite existence construction, not an economical physical design.

Section7 of PROGRAM_RESOURCES also gives a sufficient finite-time
perturbation budget. If the complete input/evolution/readout error is
at most1/4000, the contrast remains greater than1/100 in both setting
variants. The sufficient per-term coupling tolerance scales inversely
with T_h times the number of Hamiltonian terms. This is a continuity
bound, not evidence that the required calibration has been achieved.

[THERMAL_CHANNEL.md](THERMAL_CHANNEL.md) fixes the two temperatures only
after this inventory, proves the helper/donor comparison, counts every
cold defect and supplies the complete flagged channel bounds. The hot
fuel and reset donors have gap17643epsilon and excitation probability
1/3. A local resonant launch converts one fuel excitation into the
charge-eight source seed, work level17632 and first cursor charge3.
Both reset donors have that same gap; their spent states remain counted.

[ENERGY_ACCOUNT.md](ENERGY_ACCOUNT.md) includes every onsite and
interaction term, exact finite input energy moments, capacities,
entropies, nonstationarity and the recurrence. The independent Gibbs
product is stationary under H_0 but not under the interacting H.
It is an admitted initial boundary condition, not equilibrium of H.
An external preparation/switching procedure would need its own account.

## What this closes and what remains open

The added Hamiltonian now schedules the original source preparation,
helper cooling, work-ladder loading, transports and the three compiled
steps without an external gate clock during the run. It returns both
outputs to the nominated original occupation ports and includes all
auxiliary registers and rejected thermal branches.

It does not reconstruct uninterrupted evolution under the original
spectral generator between compiled cuts. The initial occupation vacuum
is outside that generator's original one-pair/one-carrier domain. Its
extension, physical energy selection, and a local interaction account
relating it to epsilon H_N remain open. The earlier original-energy
stationarity obstruction is not evaded within its hypotheses.

The native six-pentit admission of the gates, an incoming-unbound capture
preparation, fabrication/calibration, a physical read-and-retain device,
and renewal of spent thermal stocks remain additional obligations.
Reversal restores the input only while erasing the record. It cannot
serve simultaneously as free reset and retained-output operation.

Evidence pins, falsifiers and external review obligations are in
[VALIDATION.md](VALIDATION.md). This is analytical work with same-session
cross-reading, not independent acceptance. No expanded circuit,
scientific executable, simulation or experiment was run. No Canon,
registry, source proof, scientific status or merge is changed.
