# Preregistration: a material sideband writer

PUBLIC; L1 mathematical candidate and conditional engineering design;
NON-CANONICAL. Probe P-QDD-ION-SIDEBAND-WRITER-1.
Owner: A. M. Thorn / ion-apparatus session 2026-09-20.
Lock: https://github.com/mathorn1973/twist-j/issues/1091.
Base: 1511a2e56e302c415a8879ebfdca079c2190323a, Public Canon v90 ACTIVE.
The author authorizes the connected GitHub contributor identity.

## 1. Equation and implementation class

The proposed carrier uses three logical five-level 40Ca+ ions, called
source S, port P and archive M, with an auxiliary ground state g on each
ion and a common harmonic motional mode. The logical levels 0 through 4
are five declared D5/2 sublevels. The physical assignment is proposed,
not an adopted TWIST-J dictionary or a measured device in this project.

For each addressed ion i and logical level j, freeze the ideal
interaction-picture Hermitian Hamiltonians

H_R(i,j)/hbar = Omega_R/2 (exp(i phi)|j><g| + h.c.),
H_B(i,j)/hbar = Omega_B/2 (exp(i phi) a^dagger |j><g| + h.c.).

Omega_B includes the relevant Lamb-Dicke coupling. A carrier pulse R
has area integral Omega_R dt, while a blue pulse B has area integral
Omega_B dt, normalized on the |g,0> <-> |j,1> doublet. Pulse phases
are zero or pi; all executed durations are positive. The sideband
matrix elements at higher phonon number are not replaced by the
vacuum-doublet value. The proof must show they are never occupied by
the prescribed input and schedule. Finite thermal occupation, heating,
other modes, uncompensated light shifts and nonideal pulse envelopes
remain physical error sources, not exact-model conclusions.

At input, all three ions lie in their logical D levels and the common
mode is in |0>. Define X|e>=|e+1 mod5>. The writer target is

D|s,e,m;0> = |s,e+f_hw(s),m;0>,
f_hw(0)=1, f_hw(1)=f_hw(2)=f_hw(3)=f_hw(4)=2.

Hardware source s=0,1,2,3 corresponds to native h=1,2,3,4. Hardware
s=4 is an explicitly additional outside-code extension, not native h=0.
No identity with the old native f(0)=0 is asserted there.

Freeze the twenty-eight-pulse sequence in PULSES.tsv: twelve carrier
pulses implementing X_P^2, followed by a source-s=0 controlled X_P^-1
using fourteen blue-sideband and two carrier pulses. The controller
condition is carried coherently by a phonon during the latter block.
Its complete amplitude must be returned to the common vacuum, including
relative phases, rather than measured or discarded.

For the native comparison use only X_(h,e)(n)=T_e Y_h(n), h=1..4,
e in F5, n>=3, with T_e(p;q,r)=(p;q-e,r+e), from the accepted stable
transport theorem. The moving isometry maps X_(h,e)(n) to |h-1,e>.
It sends the restricted native step to I_S tensor NEG_P, where
NEG|e>=|-e>. Appending an arbitrary five-level archive gives a
100-dimensional comparison subspace inside the 125 logical states.
This moving representation is not a global unitary realization of U.

## 2. Code and immutable material

Freeze before any scientific execution: PREREG.md, PULSE-PROOF.md,
CHART-AND-CYCLE.md, APPARATUS.md, REVIEW.md, PULSES.tsv and verify.py.
Read all seven files back from the public pin. The verifier uses the
Python standard library and exact finite labels with Gaussian-unit
phases. No floating point, pulse fitting, random sampling, device
connection or third-party numerical package is used. Only static
syntax checks are permitted before pin.

The finite pulse model must fail explicitly if a reached addressed
sideband needs a doublet above |g,0> <-> |j,1>. Such a refusal is not
a proof about arbitrary hot-mode hardware; it protects the scope of
this exact audit. The universal vacuum-invariance argument is in the
written proof.

Primary papers identify a physical carrier, laser interaction and
control architecture. They are not data from a TWIST-J apparatus, and
their best parameters cannot be combined into one fictional device.
An independent reviewer reads the written arguments before verify.py.
No blind discovery is claimed; the candidates are exposed analytically.

## 3. Frozen exact audit targets

G1. The fixed TSV agrees exactly with the chronological writer compiler,
including all twenty-eight pulses, their addressed transitions, signed
areas through phase reversal and fourteen/fourteen count.

G2. Derive the local signed exchange Q_(u,v), X^2, and the eight-carrier
NEG with its two required 2*pi phase corrections. Check all five
logical inputs, phase +1 for the target permutations, and empty g.

G3. Check the source-conditioned X^-1 and its inverse for each of the
five control levels and all 25 source/target basis pairs, including
each intermediate occupation guard and common final motional vacuum.
Check all pair matrix units by their exact input/output amplitudes.

G4. Check the full writer on all 125 logical triples, including its
outside-code extension, helper cleanup and +1 phase. On the 100-state
admitted source/port/archive domain compare every matrix unit. No
classical source-conditioned choice of pulses is permitted.

G5. Check the admitted native formulas, stable paired transport,
twenty-point moving chart and actual counter starts 3 through 12.
For the finite word audit use every binary word through length four.
The all-time statement is an induction from the accepted one-step
transport identity, not an extrapolation of these finite words.

G6. Compile SUM and inverse SUM from controlled cycles with the fixed
balanced representatives 1,2,-2,-1, six controlled cycles per SUM.
Compile SWAP by y+=x; x-=y; y+=x; x=-x. Audit every pair basis input,
all phases and vacuum cleanup. No unspecified two-ion SWAP primitive
is admitted.

G7. For waits k=0,1,2,3, audit the entire pulse-compiled block on every
logical triple and every matrix unit of the admitted 100-state domain.
Its exact action is (s,e,m)->(s,(-1)^k m,e+f_hw(s)); the port is restored
only for the declared input conditions. Count 266 blue pulses and
58+8k+16*(k mod2) carrier pulses in this deliberately unoptimized
implementation. Arbitrary waiting k follows by the written parity law.
Repeated waiting ticks are implemented, not silently replaced by a
different elapsed-time schedule.

G8. Freeze negative controls for an omitted phonon-uncompute stage,
one wrong sideband phase, omitted odd-wait sign correction, and the
omitted NEG phase corrections which preserve populations but alter
coherences. Preserve the explicit model-domain rejection for an
initially excited mode. Distinguish an exact false identity from a
refusal to model an unregistered physical input.

The accepted program fixes enumeration and output order. No waveform
calibration or measured fidelity threshold is inferred from these
finite algebraic checks. A future physical experiment needs its own
frozen raw-data, uncertainty and decision contract before acquisition.

## 4. Systematics and physical boundaries

The exact theorem is conditional on the ideal resolved-sideband,
rotating-wave and Lamb-Dicke model, a cold selected mode, spectral
addressing, known drift frames and compensated light shifts. It does
not claim those approximations are exact in a material ion trap. The
controller, lasers, oscillators, cooling reservoir and detector are
external physical resources described in APPARATUS.md.

The sideband interaction derives from driven ion motion in a common
trap, rather than a newly postulated N_i*N_j interaction. The particular
pulse program is constructed for the registered target. It does not
derive its own controls or the choice of a physical decoder from J.

The moving chart absorbs the nontrivial native source trajectory and
ready reference. Keeping the physical source label fixed therefore
does not show that natural ion evolution equals U. A programmed NEG
is not an autonomous native clock. Duration inside the two coupling
blocks and the relation of laboratory time to native n remain part of
the explicitly external intervention schedule.

Mapping the writer back changes the checkpoint by C_n. Consequently
the proposal cannot populate #539 with feeds_U=false or silently change
the accepted architecture. Existing #830, #832, #834 and #1038 retain
their scope. This is an engineering comparison profile under the open
apparatus owner, not an assertion of physical ownership or completeness.

The full coherent block is checked before archive detection. Measuring
the archive subsequently transfers LOW/HIGH information to the detector;
it is not a common-environment unitary on the source alone. HIGH
coherence and, before readout, joint LOW--HIGH coherence need distinct
physical tests. The old clean-energy theorem remains valid. An ideal
classical laser field is not a fully accounted finite clean energy store.

## 5. Failure threshold and disposition

One exact counterexample refutes its registered mathematical identity.
An error in the all-input proof blocks candidate-T even if finite checks
pass. No phase, threshold, pulse list, target extension or model scope
may be repaired after the pin. Preserve falsifiers.

Runtime/syntax failure, incomplete first execution, changed frozen bytes,
pin/readback failure or architecture/output mismatch is STOP. A pin
whose first formal gate does not complete is ABANDONED under POLICY;
its identifier is consumed and cannot be resumed or renamed.

After completion add EXPECTED.txt, neutral RUN.md, RESULT.md and
ACCEPTANCE.md. Require the same verifier and stdout on both public
architectures and aggregate check. Merge without rewriting the pin.
No laboratory experiment, hardware availability, procurement or physical
acceptance is implied by a successful mathematical replay.

## 6. Action layer

All new exact conclusions remain L1 and NON-CANONICAL until a separate
fold. The physical design is explicitly untested. No L1-to-L5 gate,
native first-event law, source preparation from U, persistence/reset
theorem for a real device or complete apparatus family is supplied.
Canon v90 and its physical open obligations remain unchanged.
