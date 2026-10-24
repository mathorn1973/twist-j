# Forward filtering with an autonomous finite clock and battery

**NON-CANONICAL, L1, conditional candidate-T. Independent acceptance pending.**
Author: A. M. Thorn. License: Apache-2.0. [Claim #1747](https://github.com/mathorn1973/twist-j/issues/1747).

## Result and its boundary

There exists a complete ideal filter using only forward controlled object
steps, with every history retained. A finite internal clock executes its
whole preparation/filter/read/release word. A further, explicitly declared
finite battery extension conserves a nonzero additive energy account exactly
and approximates the complete ideal state uniformly, including references.
For the specified basis-source input its acceptance weight, logical-memory
SWAP and finite record protection are exact; bound-band selectivity uses the
explicit approximation bound.

These are existence statements for a **new discrete model**. The battery
couplings, diagonal energy account, initially coherent battery, initialized
clock, and addressed operations are supplied model data. Neither a local
physical Hamiltonian nor a derivation from the original occupation or
checkpoint law is established. The conserved account is not identified with
the canonical spectral energy or with a generator of physical time.

| Requested question | Result at the stated scope |
| --- | --- |
| Are forward controlled object steps sufficient? | Yes for the ideal complete filter; its auxiliary Fourier inverse is not an inverse object step. |
| Can holding and release belong to one autonomous law? | Yes, a fixed finite cyclic clock schedules them. The law is an extension, with a finite guaranteed window and no absorbing halt. |
| Can all outputs and resources be counted? | Yes for the named-operation clock, finite spatial carrier and selected positive energy/battery account. Local interaction strength, physical duration and native admission remain open. |

## Read the proofs

- [FORWARD.md](FORWARD.md): the full Fourier block, Kraus-history grouping,
  distinction between effect and output state, energy demand, and a general
  reference-uniform error contract. It also states a restricted exact
  universal-battery obstruction, which is not a no-go for this fixed source.
- [CLOCK.md](CLOCK.md): full autonomous law and inverse, explicit Boolean
  circuit, all-branch spatial completion, holding, release, and finite-clock
  and continuous-Hamiltonian boundaries.
- [ENERGY.md](ENERGY.md): complete finite energy sectors, common-battery
  representation, conserved clock/data/battery energy, uniform error and
  exact diagonal observables for the initialized source.
- [VALIDATION.md](VALIDATION.md): source custody, review scope and the checks
  actually performed. There is no new scientific executable or numerical
  experiment in this analytical note.

## One complete specified device

Let D=327680 and B_bits=2D+3=655363. Include D filter pentits, one loader
pentit, every B_bits binary target, and all the original object, token/pulse,
label and occupied-memory degrees of freedom. No branch register is erased.
Use T=H+1 native target steps from source position s=99, followed by the
filter and predicate, then H release steps. The useful program length is

    L_prog = T+5D+8,
    M = L_prog+H+1.

For T=2,H=1 this is L_prog=1638410 and M=1638412 clock states. These are
named-operation ticks, not local elementary gates or seconds. The word is
hardwired into the new law; its addressing and finite description are part
of the supplied control structure.

CLOCK.md fixes a finite odd ring size N=2R_box+1 sufficiently far outside
every reachable branch. A complete data-space dimension for that chosen
finite coordinate completion is

    dim Dcal = 12 N^3 26^2 5^(D+1) 2^B_bits.

Here the object has four coin states and two coordinates, the carrier has
one token or two pulse-bank arrangements at each coordinate and 26 labels,
and the receiver has 26 labels. The clock multiplies this by M. This is a
complete finite carrier, not a claim of minimal storage or finite classical
bit precision for arbitrary amplitudes.

Define a diagonal integer account on the whole finite clock/data carrier:

    N_S = c + (R-s)^2 + r^2 + (x-s)^2 + I_pulse
          + sum_(all pentits) [a != 0] + sum_(all bits) b.

Coordinate differences use the fixed representatives. It is identity on
object coin and logical labels. Let Q be a positive integer upper bound on
N_S, as made explicit in ENERGY.md, and choose L_bat=Q 5^22. With battery
levels n=0,...,L_bat+2Q-1, the new law is

    U_funded = Gamma(U_clock),
    E_total = epsilon (N_S+n),       epsilon>0.

Gamma is the complete sector construction of ENERGY.md. In each full
energy sector it applies U_clock coherently; in the remaining sectors it
is identity. This is one total unitary on every state. The prepared domain
stays in full sectors at every tick. The initial battery is the normalized
flat vector on levels Q,...,Q+L_bat-1; it is a supplied coherent resource.
The exact account and the general full-state comparison are

    U_funded* E_total U_funded = E_total,
    Delta<E_battery> = -k epsilon - Delta<E_data>  (initial clock 0, before wrap),
    ||U_funded^k(Psi tensor b) - (U_clock^k Psi) tensor b||
        <= sqrt(8Q/L_bat) < 3/5^11 < 1/6000000.

This bound holds for every input and passive reference, without a multiplier
by the number of gates. The single battery retains correlations; it is not
reset between operations. The exact battery dimension is L_bat+2Q, its
capacity is epsilon(L_bat+2Q-1), and its initial mean is half that capacity.
These very large finite costs are not optimized.

## Consequences for the supplied source

Before the loader, the prescribed source is one coordinate/coin basis state,
all control registers and the clock are zero, and the carrier is a token.
Its N_S eigenvalue is zero for every logical label/old-memory/reference
input. The acceptance flag commutes with N_S. The exact energy-eigen-input
lemma therefore preserves its ideal acceptance weight. The same lemma
preserves the ideal occupied-memory SWAP because the energy account acts
trivially on those logical factors.

Conditional on the preceding candidate's source and spectral proofs:

    p_basis > 1/20000,
    conditional outside-bound-band weight < 1/10^6,
    accepted logical map = SWAP_(incoming label, old memory),
    receiver = d1 through H release steps when incoming label = 1.

The last statement protects the record for this finite horizon. It does not
claim perpetual binding or permanent memory. The band projector is a proof
observable of the infinite ideal model, used on the finite states by zero
extension; it is not a sharp projector executed by the device.

The stronger source-specific proof in ENERGY.md controls the normalized
accepted state directly, so it does not pay an inverse acceptance-weight
factor. FORWARD.md retains the more general error bound for inputs or
implementations without that special structure. All weights remain L1
squared norms; no event-selection or empirical-frequency law is added.

## Inputs, attribution and open physical work

The numerical source and selectivity premises are the unmerged
[PR #1746 at 01acc42b78f75095587765e9a5b91ee70dc28f37](https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md),
not newly canonical results. Their existing 788-check reproduction is not
an execution or independent acceptance of this note.

Public authority is main/canon-v105
[892a0b11089d34e241e1eb76d2c03247022d18e6](https://github.com/mathorn1973/twist-j/tree/892a0b11089d34e241e1eb76d2c03247022d18e6).
The canonical FIELD-FETCHED-PROGRAM-CONTROL and
SELECTED-SPECTRAL-ENERGY-SOURCE results already provide the general clock
and energy-reference ideas. This note specializes and composes them using
a finite commensurate battery and a specified source. It does not claim
invention of either general technique. [PR #1743](https://github.com/mathorn1973/twist-j/pull/1743)
retains its separate native-admission audit and is not amended here.

The remaining physical problem is specific: realize the declared coherent
energy exchanges, addressed forward controls, source preparation and clock
with local bounded-strength interactions under one physically identified
energy and time law. In particular, conserving the selected E_total is not
a proof that E_total generates U_funded. The nearest-neighbour history
Hamiltonian shortcut necessarily includes reverse clock edges; CLOCK.md
states its restricted obstruction. No Canon, frontier, detector threshold,
existing branch or scientific status is changed by this proposal.
