# Preregistration: affine control and conserved energy

PUBLIC; L1; NON-CANONICAL. Probe P-QDD-AFFINE-ENERGY-CONTROL-1.
Owner: A. M. Thorn / affine-energy-control session 2026-09-20.
Lock: https://github.com/mathorn1973/twist-j/issues/1089.
Base: b61e3801725bc22c98bfeb33460fa738f0b4eff7, Public Canon v90 ACTIVE.
The author authorizes the connected GitHub contributor identity.

## 1. Equation and decision classes

Use the accepted entrance of P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1 (#1088).
All point arithmetic is in F5, with x=(a,b,c,d,q,r), s=a+b+c+d,
z=s+q+r. The four code points are Y_h=(h,0,0,0,1-h,0), h=1,2,3,4.
The response is f(1)=1 and f(2)=f(3)=f(4)=2; C_3 Y_h shifts q by
-f(h), r by +f(h). The accepted identity is F_1 B F_0 A = C_3 on
this code; actual counter ticks three and four have bits zero and one,
and the two-step free target N_(3,2) C_3 equals C_3 here.

A(x)=(a,b,c,d,q+s+2,r).

B(x)=(a+b+3c+r+3, 3a+3c+3r, 4a+2r+3,
      4a+2c+d+r, q+4c, 3a+3c+4r+3).

Freeze two different classes, with no assertion that either is the full
physical family owned by QDD-INSTRUMENT-APPARATUS:

* Controlled model: six five-level Hilbert carriers with the declared
  computational basis, exact local unitary control, and independently
  switchable pair interactions -hbar*g*N_i*N_j. N has ordinary integer
  eigenvalues 0,1,2,3,4. Drift compensation and the physical control source
  are assumptions. Prove a finite-duration phase/SUM identity and the
  fixed all-state netlists for A and B. This is an explicitly supplied
  quantum control model, not a derivation from native U.
* Conserved-energy class: a complete unitary on checkpoint and prepared
  independent environment strongly commutes with the additive cut energy.
  The environment can have arbitrary self-adjoint energy and any normal
  state. Require the exact coherent target on its declared code, hence a
  common output environment after purification. Decide the code entrance
  for equally spaced q and r energies, and separately the entire global
  permutation B for arbitrary additive diagonal energies on six carriers.
  No global-B conclusion is applied to a code-only implementation.

ENERGY.md states the exact conservation and coherence hypotheses. A
constant total Hamiltonian does not by itself imply conservation of the
bare additive cut energy if interaction energy changes. There is no
claim that conservation of a sum modulo five is physical energy
conservation. No energy dictionary is adopted by this comparison.

## 2. Code and immutable inputs

Freeze PREREG.md, NETLIST.md, CONTROL-MODEL.md, ENERGY.md, REVIEW.md and
verify.py together before the first scientific execution. Read the public
pin back and record every file hash. The verifier uses only the Python
standard library, exact finite-field and integer arithmetic, including
cyclotomic reduction and Gaussian elimination modulo the prime 101.
No floating point, external data, fitting, random samples or external
scientific executable is admitted. Compilation/static checks are allowed
before the pin; no gate execution is allowed before it.

An independent reviewer attacks the written proof before reading the
verifier. This is independent reasoning, not an independent experiment.
The analytic candidates are exposed before pin, so no blind prediction
is claimed. The universal results rest on their written proofs; finite
checks audit premises and concrete constructions.

## 3. Carrier and frozen exact audit targets

G1. Check the fixed five-operation A and nineteen-operation B netlists
against their displayed maps on every one of the 15625 native points,
including bijectivity. All elementary point permutations extend with
phase +1 on the quantum basis. No gate-count minimum is claimed.

G2. Check the phase/Fourier SUM identity on all 125 triples of input
labels and output target label by exact arithmetic in Z[omega],
Phi_5(omega)=0. The Fourier-pair normalization is exactly five.

G3. Check every fixed gain 0 through 4 on all 25 pair basis inputs and
all 625 pair matrix units per gain. Check the specified Bell-pair
calibration image as an exact symbolic superposition. This is a proposed
external calibration, not a performed measurement.
Also check the interregister swap synthesis from three gain-SUM operations
and one local negation on all 25 pair inputs; no additional swap
interaction is assumed by the Hamiltonian model.

G4. Check the actual two native ticks on all four code inputs, distinct
prefix supports, and all sixteen matrix units against the properly
completed target. No global unitarity of the selected native map is
asserted or used.

G5. Check the ordinary port-energy coefficient changes (4,1) for h=1
and (-2,2) for h=2,3,4, giving (5,0,0,0) for equal positive gaps.
Check that the alternative gap ratio Delta_r=6 Delta_q gives the common
change 10 Delta_q, and that A alone changes q energies in the proportions
(3,-1,0,1). Equal changes are a necessary condition only, not a sufficiency
or physical selection claim.

G6. Check the six linear rows of B, invertibility and determinant 2,
and the 24 distinct nonzero row-line frequencies, disjoint from every
coordinate axis. This audits the Fourier proof that global clean B
forces each additive diagonal local energy to be constant.

G7. Preserve exact negative controls for deleting Fourier conjugation,
omitting an affine offset in the accepted routing, changing the first
B gain from 4 to 3, and confusing modular
port conservation with ordinary integer energy conservation. A negative
control is not an extra physical no-go.

G8. Independently audit the global energy result: the 15625 equations
E(Bx)-E(x)=0 in the thirty real unknowns e_i(v) have rank 24 modulo 101.
Six independent constant-local-energy vectors lie in the exact rational
kernel, so rational rank is at most 24; the modular rank certificate
gives at least 24. Thus this finite audit also proves exact rational rank
24. The all-real-spectrum conclusion is the same linear system over R.

The accepted verifier fixes enumeration order and exact deterministic
stdout. No search chooses A, B, a spectrum or a control family after
execution. Full coherence follows from exact linear maps and the
common-environment hypothesis, not from comparing just probabilities.

## 4. Systematics and excluded inferences

The positive construction and negative result have different resource
assumptions. Prescribed external pulses need not conserve the checkpoint
bare energy; a total conservation claim must include their controller.
A map on the entire six-register space is stronger than the required
four-point action. The global B theorem must not become a no-go for all
entrances or for all possible physical embeddings.

Neither finite pulse durations nor an algebraic schedule identify them
with native ticks. The native selected map is not globally invertible;
the used four-point supports are injective. A complete physical account
of its environment is not supplied by the unitary realizations of A,B.
There is no claim about exact autonomous implementation, physical
spatial locality, uncontrolled noise, an actual experimental carrier,
single-event occurrence, archive persistence or source reset.

Changing the energy gaps, using degenerate logical levels, retaining an
input-dependent environment, supplying external control, or changing
the physical energy decomposition changes the tested class. These are
explicit boundaries, not purportedly derived escape mechanisms.

The interaction family has a target-independent definition and an
outside-target calibration consequence. Its selection in this note is
nevertheless a conditional comparison made after the QDD target was
known, not independent physical evidence selecting a TWIST-J decoder.

Related #539, #990 and #1038 keep their existing ownership and scope.
No Canon file, registry row, physical gate or entropy source changes.

## 5. Failure threshold and disposition

Every asserted identity is exact. One admitted counterexample refutes
the corresponding mathematical target. Any error in a universal proof
is a stop for its candidate-T conclusion even if finite checks pass.
No tolerance, finite depth, changed spectrum or revised gate list may
repair a claim under this pin.

Incomplete execution, runtime/syntax error, changed frozen bytes,
public readback mismatch or architecture/stdout mismatch is STOP, not
a physics falsifier. A pin whose first formal gate does not complete
is ABANDONED under POLICY and its identifier cannot be reused.

After completion add exact EXPECTED.txt, neutral RUN.md, RESULT.md and
ACCEPTANCE.md. Require both architecture jobs and aggregate check at
the accepted head. Keep the immutable scientific pin and merge without
amendment, rebase, squash or force-push. A separate fold owns any future
Canon promotion.

## 6. Action layer and physical boundary

All results are conditional mathematical statements at L1, with possible
candidate-T proof status. No L1-to-L5 apparatus gate is earned. The
physical origin of the interaction and the physical carrier dictionary
remain STOP-DEFINITION under QDD-INSTRUMENT-APPARATUS. The point of this
probe is to specify an exact control witness and conservation exclusions
that a future physical assignment must respect, not to declare that
assignment completed.
