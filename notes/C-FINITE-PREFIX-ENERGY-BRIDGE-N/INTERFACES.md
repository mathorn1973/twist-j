# Compatibility and the next bounded admission contract

**NON-CANONICAL, L1. Conditional analytical candidate-T; independent
acceptance of this successor is pending.** Author: A. M. Thorn.
License: Apache-2.0.

This note identifies the interfaces between the coefficient and spectral
results of #1771, the finite prefix model, the funded decoder and the
thermal apparatus. It supplies no new claim that their remaining physical
interfaces have been closed. The comparison concerns the stated exact
models and their specified input families.

## 1. Immutable sources and separate review scopes

- Public Canon v105 is read at
  [892a0b11089d34e241e1eb76d2c03247022d18e6](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
  Its content commit is b8cdfd6ea58ae798545bc6000c817147fa0f0dcc.
- The twenty-two-file source in
  [#1768 at 811daddc3b2f085ee5bc6f50261ac95a4c11fe44](https://github.com/mathorn1973/twist-j/tree/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N)
  has a separate-session
  [PASS review of its three extensions](https://github.com/mathorn1973/twist-j/pull/1768#pullrequestreview-5642715718).
  That verdict preserves the source's conditional NON-CANONICAL L1 scope.
- The local two-attempt successor
  [#1770 at e23b0a08ed24667dfbedf948588211f977428d8e](https://github.com/mathorn1973/twist-j/tree/e23b0a08ed24667dfbedf948588211f977428d8e/notes/C-LOCAL-TWO-ATTEMPT-REUSE-N)
  has a separate-session
  [PASS review of its fifteen obligations](https://github.com/mathorn1973/twist-j/pull/1770#pullrequestreview-5642782034).
  Its reviewed tree is 2e3f01b5737c440c7755052ff19913a132219131.
- The public #1771
  [SPECTRAL.md record](https://github.com/mathorn1973/twist-j/issues/1771#issuecomment-6396916668)
  has SHA-256
  9966cb1bb90f39d4ef5a435549126874fbb441df565b95f53b0d4dfed4a56e76.
  Sections 4-7 contain the strong Borel-limit lemma, no-atom proof,
  configuration-kernel obstruction and surviving energy-branch shift.
  The companion
  [PROOF.md record](https://github.com/mathorn1973/twist-j/issues/1771#issuecomment-6396916409)
  has SHA-256
  f7946237e6498cd7ff99ccee3253c10bc8645fe8bc8cbaf41fd6022cc235a8e9.
  Its sections 4-5 distinguish configuration-local coefficient updates
  from physical digit operations and prove exact denominator growth.
  The original commit is now preserved unchanged in draft
  [PR #1772](https://github.com/mathorn1973/twist-j/pull/1772), at
  `3abf054e435e31c51e6e50528b09fe3cf7cffe13`, parent
  `892a0b11089d34e241e1eb76d2c03247022d18e6`. Its verified Git bundle and
  the issue records agree on all seven file bytes. Transport and CI do
  not constitute independent mathematical acceptance.

The supplied original dossier has PROOF.md SHA-256
e9ac1a0dbc4b29eb7551584fc0af1a160985ce926bfdd79ef3a7b588878a80c2.
Its separate seventeen-obligation PASS is documented by the
authoring-session transcription [SOURCE_REVIEW.md](SOURCE_REVIEW.md).
That transcription is not another independent review. The original
dossier's verdict accepts neither the stronger new results of #1771 nor
this finite-prefix successor. The #1771 results remain candidate-T with
same-session analysis and external acceptance pending. Review of a frozen
source, repository integrity checks and consistency of a new composition
are three different records.

## 2. The energy being compared

The fixed input of this directory is

    U=U_rec,       H_*=f(U),       Q=E0 H_*,
    f:unit circle -> [0,2pi),      exp(-i f(z))=z,
    Delta=2pi E0.

In [FINITE_PREFIX.md](FINITE_PREFIX.md), the phrase original-energy
comparison means comparison with this specified full-step Q:

    q_phys=J*QJ,       ||QJ-J h_N||<=d,
    q_phys=q_d+r,      0<=r<=dI.

It does not mean a global comparison with the older additive reference
H_0 formed from the isolated-object logarithm and the carrier energy.
The safe-channel identity is specifically

    H_* Omega_(rec,+/-) P_safe
        =Omega_(rec,+/-) H_0 P_safe,
    P_safe=1_((5pi/4,7pi/4))(H_0) P_(ch,0),

with the memory/reference identities included. It identifies energies
through the calibrated wave operator on that channel; it is not equality
of H_* and H_0 on the entire physical space.

Section 7 of the pinned #1771 spectral record gives normalized negative-
additive-band packets and translations S_L away from the contact and
receiver for which

    lim_(L->infinity) ||E0(H_*-H_0) S_L psi||=2pi E0.

This difference survives already in the completely free translated
limit. It is an energy-branch difference, not the finite model's binning
residual. Taking d to zero does not remove it. The current O(d) bounds
cannot be advertised as a global identification with the old additive
account, or as a proof that the entire energy difference is concentrated
near the contact.

The full-circle spectrum in #1771 also does not invalidate the bin
construction. Although 2pi is in the spectrum of H_* by closure, its
spectral projection at 2pi is zero because f never takes that value.
Thus the half-open bins cover Q and the strict finite upper-endpoint
argument in FINITE_PREFIX.md applies.

## 3. Different dynamical and locality statements

| Construction | Declared conclusion | Interface that it does not supply |
| --- | --- | --- |
| #1771 coefficient law | A total reversible update of eight integer coordinates and one exponent per coefficient, with configuration radius at most two | Bounded material digit registers, bounded carry latency or original-native admission of the arithmetic gates |
| #1771 selected energy | H_* is conserved, but lacks the specified uniform exponential pulse kernel in configuration distance | A classification excluding every other logarithm or every physical notion of locality |
| FINITE_PREFIX.md | One finite h_N and V reproduce U^n A0 for every uninterrupted integer prefix 0<=n<=N | An all-time finite invariant spatial model, arbitrary intervening measurements or a local embedding J into the original lattice |
| FUNDED_DECODER.md | A counted sharp-sector dilation transfers one selected original receiver channel to an occupied archive, including selector and reference correlations | Preparation of the original Q-bearing spatial state on its original physical degrees of freedom |
| THERMAL_REALIZATION.md | A positive local qubit Hamiltonian produces that archive channel in a finite completed window from counted thermal hardware and admitted information | Identification of its Hamiltonian with H_* on the original configuration lattice, or indefinite retention and resource regeneration |

The #1771 locality obstruction transfers an assumed uniform exponential
kernel bound through a strong translated free limit, then contradicts a
transverse branch-cut jump in the free Fourier symbol. Its no-atom
condition is proved for the limiting free operator. Nothing in the
finite-prefix proof assumes the excluded kernel bound. Its spectral
vectors can have infinite coordinate support, and its exact compressed
matrices are supplied specifications.

The thermal construction has a different code, graph and generator. Its
local data gates, controller and residual correction realize a selected
output channel. Their locality does not imply locality of J, Q or a
material implementation of #1771's coefficient field. In particular the
inclusive apparatus identity

    E_phys=H0_apparatus+R_all,
    H_int=Hprop-R_all,       0<=R_all<=d C_charge

uses the apparatus's rounded H0_apparatus. It must not be confused with
the canonical additive H_0 above.

The finite model's integer time n hbar/E0, the thermal controller's
completion latency, and a prospective digit machine's microtick are also
different clocks. The present thermal latency grows with the compiled
path at fixed g0. Configuration radius two is not a proof that an
arbitrary carry or exponent-alignment operation finishes in one such
physical tick.

## 4. One selected snapshot is not two completed source attempts

For each fixed input family A0 I and horizon N, the prefix theorem is the
joint identity J V^n alpha=U^n A0 for 0<=n<=N. The terminal selector can
be coherent. The common decoder and occupied SWAP then define one joint
channel to selector C, archive A and reference R. Tracing C produces the
diagonal mixture; retaining it is necessary for the off-diagonal
selected-time contract. A separate discarded record of the selection is
not allowed beyond the prescribed dilation.

The thermal read predicate certifies completion of that simulation
channel. Its ideal p0=1 is not a unit capture probability. Returning its
source label and sharp battery leaves the helper bank, changed donors and
controller consumed or correlated. The unmeasured return at 3T_h also
prevents interpreting the completed window as permanent storage.

By contrast, the reviewed #1770 device runs the frozen #1768 source
twice, exports two seven-factor outputs, performs two complete core
replacements and returns the banks to specified sites. It retains the
first output during the forward reset and second attempt, with one common
outer activation probability and its own eventual recurrence. Its source
channel, site inventory, product-approximation errors, timing and capture
thresholds belong to that frozen construction. They cannot be inherited
by substituting the present decoder or a changed source word. Repeating
this selected-snapshot apparatus requires a new combined schedule and
resource/error account; no such schedule is proved in this directory.

## 5. Dimension, arithmetic precision and thermal error

The bound D<=ceil(Delta/d)(N+1)dim I is a Hilbert-space dimension bound.
It is not a bound on the digit description of its basis vectors, matrix
entries or exact gate angles. Nor is it the actual physical qubit count:
the declared realization includes one-hot labels, battery, decoder,
workspace, all data rows, donors and controller sites.

The #1771 trajectory with least common denominator 25^n is a statement
about exact arithmetic representation. Finite Hilbert dimension does not
make that classical coefficient precision free. Conversely, exact
denominator growth alone does not exclude a future finite-resource
approximation at a specified nonzero error. Such an approximation needs
its own uniform input, time and instrument contract.

[ARITHMETIC_RESOURCES.md](ARITHMETIC_RESOURCES.md) supplies a separate
finite-horizon upper bound for bounded arithmetic input. In its notation,
each signed integer coordinate uses at most
b_N=1+ceil(log2(H+1))+18N bits, and the current numerator uses at most
64896 V_N b_N bits, with its common exponent counted separately. This is
completed-macrostep storage, not a digit circuit, carry-workspace or
spectral-coupling precision bound. It retains the unreduced common scale
e0+2n. The proposed per-coefficient canonical-register contract below is
a different implementation choice; its intermediate capacities cannot
be inferred merely by renaming that common-scale allocation.

The following parameters therefore remain distinct:

| Parameter or resource | What it controls here |
| --- | --- |
| d | Spectral bin width and original-Q comparison bounds |
| N and dim I | The fixed uninterrupted prefix horizon and admitted input family |
| k in THERMAL_REALIZATION.md | Counted preparation defects and the conditional archive-channel error |
| Numerator/exponent digit capacities | No finite material implementation is supplied by the current dimension or k bounds |
| Exact spectral vectors and coupling angles | Mathematical input specifications; no finite manufacturing precision is proved |
| Gate perturbation tolerance | A separate stability bound, not automatically d or 2^(-k) |

The sharp decoder avoids a coherent battery for its stated archive
contract by storing the encoded state in a zero-energy helper dictionary.
It does not evade the stationary-preparation obstruction for a standalone
energy-coherent source. Assigning Q to those helpers after the proof would
change the Hamiltonian. Admitted information and exact couplings are not
thermal resources manufactured by the two-temperature reset panel.

## 6. A bounded contract for the next material-digit candidate

The next candidate can be made reviewable by freezing the following
finite data before any claimed execution. This is a proposed admission
contract, not a completed compiler, native derivation or physical gate.

1. **Input and time domain.** Fix integers N_ar>=1, R_in>=0, L_in>=1,
   e_in>=0 and L_work>=L_in. Admit only finite-support coefficient fields
   in the declared configuration basis, initially inside the cube
   |R|,|r|,|c|<=R_in, with each of the eight signed numerator coordinates
   represented in L_in balanced base-five digits from {-2,-1,0,1,2}
   and exponent at most e_in. Retain #1771's canonical convention:
   zero is (0,0), and a nonzero numerator at positive exponent is not
   divisible by five. Freeze the receiver and all label factors. A
   different or noncompact quantum input family needs a separately
   stated approximation and reference contract.
2. **Registers and overflow.** Use explicit finite local digit sites,
   eight numerator lanes of L_work balanced base-five digits per active
   coefficient, and a fixed-width nonnegative exponent register. Choose
   its capacity at least e_in+2N_ar, following the inherited forward
   exponent bound. Provide and prove bounds for all intermediate aligned
   numerators, cyclotomic reductions and carries, not merely final
   canonical outputs. Prove that no admitted run overflows. Give a full
   reversible action on unused codes, overflow flags and dirty workspace;
   those branches cannot be erased or silently removed.
3. **Support and placement.** Freeze the finite configuration region and
   its boundary rule. A box containing the radius-two causal expansion
   through N_ar steps, with a further two-site guard, is an explicit
   starting layout requirement. Supply the actual material placement of
   all configuration, internal-label and digit sites. No periodic wrap,
   remote common-scale division or identification of a configuration
   coefficient with one original physical site is implicit.
4. **Allowed elementary operations.** Specify the complete finite gates
   for signed addition, multiplication by the fixed cyclotomic entries,
   exponent comparison/alignment, divisibility tests, exact division and
   canonical zero handling. Include carry propagation, inverse gates,
   work-bit cleanup and nearest-neighbor routing. If original-native
   admission is claimed, exhibit those operations and their controller in
   the fixed original update law; generic universality or agreement with
   the desired output is not that derivation.
5. **Timing and strengths.** Freeze local dimension, degree, support,
   coupling bound, number of digit microsteps and physical completion
   time as functions of the declared finite capacities and horizon.
   Count both directions of every carry path. A variable carry length
   may use a bounded worst-case schedule, but cannot be counted as one
   original macrostep without proving the stated timing relation. Supply
   controller readiness and any switching resource in the same account.
6. **Fixed reader and comparison.** Specify the classical register
   decoding separately from any physical quantum preparation or read
   instrument. Freeze domain, codomain, normalization, accepted/rejected
   records and the common reference. The algebraic coefficient identity
   does not copy unknown quantum amplitudes into classical digit sites,
   and nonlinear canonicalization is not itself a linear quantum
   isometry. Prove the required complete joint map at every admitted cut,
   or state a uniform trace-distance bound and success denominator before
   conditioning. Do not choose a new reader after inspecting the output.
7. **All resources and continuation.** Count every digit, exponent,
   carry, route, clock, input, old archive and failure register, their
   spectra and initial states, any coherent phase supply, all donor/work
   stock, and the complete interaction energy. Bound capacity, energy
   moments, entropy transfer and error from finite gate specification.
   State where old values and rejected branches remain. A further use
   needs its own counted fresh stock or proved regeneration process.

Before an execution claim, the candidate must replace these capacity
parameters by fixed finite choices and prove that its full word and raw
extension meet them. Falsifiers include an overflowing intermediate,
unfunded carry/control, altered physical clock, missing inverse sector,
unretained reference correlation or readout depending on the desired
answer. No bound on such a machine is established merely by proposing
this contract.

## 7. What consolidation leaves open

The compatible results provide a specified spatial step, a reversible
coefficient representation, a delimited full-step energy reading, a
finite uninterrupted-prefix model and a separately funded archive
channel. Original-native derivation, physical selection of energy and
units, material preparation of the original spatial state, finite
precision manufacture, a physical outcome rule and complete resource
regeneration remain distinct open interfaces.

This consolidation changes no frozen proof, source review or acceptance
status. It records analytical compatibility within the authoring session.
No scientific executable, expanded arithmetic circuit, matrix simulation
or material preparation experiment was run for it.
