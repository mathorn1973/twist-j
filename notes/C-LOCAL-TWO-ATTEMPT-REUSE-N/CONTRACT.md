# Prospective contract: a bounded local two-attempt device

**NON-CANONICAL, L1. Prospective analytical construction contract.**
Author: A. M. Thorn. License: Apache-2.0. Public reservation: #1769.
These targets are not accepted results. This file is pinned before the
completed construction and is not silently edited to accommodate it.

## 1. Frozen source and allowed change

The immutable source is PR #1768 at
`811daddc3b2f085ee5bc6f50261ac95a4c11fe44`, tree
`ca833c1ecb88ee230c18484818b071fe1f930b8f`. It contains twenty-two notes
in notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/. Its local layer was added at
`7550a73d02fbb6a85d73b77e027671a42970ffbc`, thermal layer at
`485f907531ab329b3aabc08d0a1bf594ae987c80`, and reuse layer at the frozen
head. Those three layers await independent acceptance. The separate
PASS for `d13851796d5e7a316e1f628407e1bedef04f9bad` does not accept them.

Only the new directory notes/C-LOCAL-TWO-ATTEMPT-REUSE-N/ is changed,
on branch notes/c-local-two-attempt-reuse-n. The new PR is initially
based on the frozen source branch so its review diff contains only this
successor. No source edits, Canon change, registry change, merge or
scientific promotion are part of this task.

Fresh authority is public main/canon-v105
`892a0b11089d34e241e1eb76d2c03247022d18e6`, with declared content
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`. Canon has 1295029 bytes and
SHA-256 `73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.
The governing rules and overlapping live claims were checked. Older
rational two-use, work-record cartridge and physical-readout owners
retain their distinct models and files.

## 2. The exact two-attempt endpoint

D is the complete S-qubit thermal core of the frozen THERMAL_CLOCK.md.
It includes all old rows, work, donors, source, clock, fuel, sink and
latch. Its fixed fifteen information-input sites are in its initial
row. The final physical archive/pointer sites are in its final row;
these physical tensor factors must not be identified by their logical
names. The output B consists of five archive qubits, P and L, with
physical energy d n_L.

Supply two entire same-spectrum cartridges F_1,F_2, and two seven-qubit
same-spectrum output slots O_1,O_2. The three packages have independent
copies Omega of the declared thermal hardware and an arbitrary joint
valid-code information input rho_(I_0,I_1,I_2,R). R is passive throughout.
I_2 is the explicitly supplied future input left after the final reset.
It may retain its original correlations with the outputs and R.

At the abstract endpoint the ordered operations are

    V_D; export B to O_1; replace D from F_1;
    V_D; export B to O_2; replace D from F_2.

V_D=exp(-i H_D tau/hbar), tau=3 T_h,D/2, is the full raw core unitary.
The new law implements its endpoint, not its entire continuous old
trajectory. Exports are complete seven-site-pair SWAPs with the latch
pair last. Resets exchange all S corresponding sites, including on
rejected or dormant inner attempts. Old destination values, spent
cartridges and all transport junk remain in the complete model.

The new local routing must return the working D state to its original
physical sites after the second reset. The two saved output blocks are
fixed physical blocks after their completed exports and are untouched
by every subsequent forward transfer, reset and run instruction.

## 3. Bounds fixed before enlargement

All physical sites are qubits on the three-dimensional integer lattice.
Each explicitly listed Hamiltonian term has:

- support on at most nine sites;
- Manhattan radius at most 256;
- operator norm at most J_*;
- site incidence at most 64, including onsite and diagonal terms.

Let E_* be the largest physical onsite gap of the frozen core and g_D
its frozen local propagation scale. Set once, before choosing the
approximation depth or the new geometry,

    J_*=E_*+g_D+d,        g_out=J_*/4.

E_* includes the old fuel gap G+r_*>=4d. Thus the outer gap-3d fuel,
gap-d sink/latch and gap-d/2d cursors fit the same bound. Residual
counterterms remain explicit. Splitting a growing interaction into an
unbounded number of terms at one site cannot evade the incidence cap.

Runtime is derived from the constructed outer cursor length K_out:

    T_hold=pi hbar(K_out+1)/(3g_out).

The larger program does not increase J_* or g_out. Coupling precision,
onsite spectra, geometry and the local Gibbs boundary condition remain
specified physical premises rather than a manufacturing result.

## 4. Local compilation and shared errors

Use the complete local terms of the frozen core generator, including
its raw invalid sectors. Local product-formula gates act on at most
seven qubits; adding a two-site cursor transition gives the nine-site
target. Include the onsite-Q phases if an operator comparison to the
literal V_D is made on all raw inputs. Dropping them needs a separate
state-family symmetry proof and is not silently an operator equality.

Target operator error for each compiled V_D is below 2^-120. The complete
two-run word then has reference-uniform trace-distance error below
2^-119 before outer thermal/control errors. Exact matched-spectrum
transport, export and reset SWAPs introduce no approximation error.

The final completion instrument must compare one JOINT physical state:
O_1, O_2, the reset hardware at the original D sites, I_2 and R. The
comparison target uses the two actual thermal one-core channels on the
admitted joint input, tensor the restored Omega hardware. The completed
normalized joint-state error target is at most 2^-96. The target hardware
factor is independent; I_2 need not be independent of the records.

A stronger comparison after BOTH records are accepted uses the
specified joint ideal-ready source instrument, not a tensor product of
separately normalized marginal outputs. Its trace-distance target is
at most 2^-60, with a derived lower bound on the actual joint acceptance.
Any old unwanted-band estimate must be proved again for this stronger
conditioning, or omitted. No independent two-launch success law is
permitted: the shared outer thermal launch occurs once.

## 5. Preparation, retained interval and resource account

One explicitly counted two-temperature controller executes the complete
program. Its launch belongs to the same static Hamiltonian. No additional
pure timer, pure scratch, discarded preparation branch or renewed bath
is supplied. The original three hardware packages retain their actual
thermal states. New positive-gap transport copies may be cold; zero-gap
copies are Gibbs I/2. The next information input is separate from these
thermal resources.

After fixing the complete finite geometry, choose the one cold
temperature so that the stated cold-defect budget for the complete
inventory is below 2^-120. The old reset depth and its error remain
counted. This temperature choice must not determine the inventory it
is supposed to bound.

A counted identity buffer follows the first completed export and
precedes the first reset. It must permit a quantitative early interval
in which the first record is available before appreciable reset
progress, and remains protected throughout the first reset and second
run. A literal prefix-identity proof alone is distinguished from a
physical-time availability guarantee.

The final finite window is [T_hold,2T_hold]. The complete law also
specifies its later recurrence. Permanent closed retention is excluded
as a goal by the frozen obstruction theorem. Robustness to perturbations
is a separate later problem, not established by exact couplings.

Count every core and cartridge site, input, output slot, transport copy,
clock/launch/latch site, helper, hot/cold factor and dirty sector. Give
complete initial entropy and energy moments, finite capacity and the
residual-inclusive unconditioned energy account. Preserve all old
values and their reference correlations. No conditional energy bound
is inferred from an unconditional conserved quantity.

## 6. Evidence and failure conditions

The work is analytical. No new scientific executable, numerical
simulation, expanded circuit or exhaustive matrix check is planned.
Any later computation requires its own prospective public code/protocol
pin. Repository integrity tests do not independently prove the mathematics.

Specific falsifiers include exceeding the fixed range/support/strength/
incidence bounds; a hidden pure controller; failure on raw thermal
sectors; erasing or moving the fixed first output after export; a missing
transport or reset resource; a joint-reference or normalization failure;
or raising couplings to keep the runtime constant. If a target fails,
record the failed obligation rather than quietly widening it.

The prior three-layer review is a separate task for another eligible
session. This session's subagents and cross-reading are authoring work,
not independent acceptance. The new proof retains its conditional
NON-CANONICAL L1 status until separately reviewed.
