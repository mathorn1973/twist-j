# Result: concrete sideband writer and apparatus profile

Status: **PASS; candidate-T; L1; NON-CANONICAL** for the conditional
mathematical theorem. Physical apparatus status: **NOT_RUN**.

Verdict: **IDEAL-ION-WRITER**. All eight preregistered exact gates
completed at public pin d928961aea0c939d0abe057fa2149dffa82c5056.
No scientific file, target, pulse or threshold changed after the pin.
The local output and environment are in EXPECTED.txt and RUN.md;
public two-architecture acceptance is recorded in ACCEPTANCE.md.

## What is established

Under the explicitly stated resolved-sideband Hamiltonians, the
28 fixed laser pulses realize

    |s,e,m;0> -> |s,e+f_hw(s),m;0>,
    f_hw(0)=1, f_hw(1)=...=f_hw(4)=2.

The carrier is three logical five-level calcium ions, with auxiliary
ground levels and a shared cold motional mode. The program is identical
for every source amplitude. A temporary phonon carries the coherent
condition and is removed at the end. All relative phases are +1 and
all helper levels are empty. This is a full isometry identity, including
inputs entangled with the port, archive or an external reference, not
merely a population truth table.

The writer uses fourteen carrier and fourteen blue-sideband pulses.
The written proof shows that no occupied addressed doublet reaches
the higher phonon sectors at any time during those ideal pulses. The
verifier guards the declared domain rather than silently truncating it.

The native comparison has source h=1..4 represented as s=h-1 and a
five-valued port deviation. The moving chart maps the admitted native
step to port negation. Including an arbitrary archive gives a faithful
100-dimensional subspace of the 125-dimensional logical carrier. The
additional source state s=4 is an explicit hardware extension, not a
claim about native h=0.

A pulse-compiled archive exchange gives, after k encoded waiting steps,

    (s,e,m) -> (s,(-1)^k m,e+f_hw(s)).

For ready port and empty archive, the final port is ready and the
archive contains the LOW/HIGH label. For other inputs, old archive
content returns to the port and the initial port deviation contaminates
the record. Nothing is erased. The compiled cycle uses 266 blue pulses
and 58+8k+16*(k mod2) carrier pulses, excluding preparation, cooling,
phase compensation, detection and reset. No claim of optimality,
wall-clock duration or adequate physical fidelity is made.

## Exact evidence and negative controls

The verifier audits the writer on all 125 logical triples and all
10000 matrix units of the admitted code. It checks 6200 moving-chart
cases and 500 full-cycle inputs with 40000 code matrix units for the
registered waits. Matrix-unit checks include phases and preserve HIGH
coherence; the joint source/archive state before measurement also
retains LOW--HIGH coherence. All-time statements rest on the written
pulse identities and induction, not finite extrapolation.

The frozen negative controls detect missing phonon removal, a wrong
sideband sign, the missing odd-wait correction, and missing NEG phase
corrections even when populations agree. An excited-mode input causes
an explicit model-domain refusal; this is not a theorem excluding all
hot-mode hardware schemes. No registered positive identity was refuted.

REVIEW.md independently checks the written derivation and physical
scope without reading or running the verifier. Both the proof and the
finite replay are necessary parts of this result.

## What remains physical work

APPARATUS.md identifies a material interaction and the origin of its
controls: external electronics, frequency and phase references, lasers,
trap motion, cooling and detection. These are standard quantum-optical
resources supplied to this proposal. The target pulse program is
designed for the required operation; it is not derived from J or U.
The moving chart absorbs the free native source trajectory and ready
reference. Fixed hardware source labels do not demonstrate natural ion
evolution by U, and the native counter does not supply laboratory time.

The first laboratory target is the 28-pulse writer. Actual device access,
transition calibrations, thermal and spectral errors, independently
calibrated phase corrections, quantitative acceptance limits, source
preparation, archive detection and source-preserving reset are unfilled.
The much longer full archive sequence may exceed the available coherence
budget; no apparatus performance or feasibility verdict is inferred from
ideal algebra or from numbers reported for other devices.

Archive readout and its macroscopic persistence need physical evidence.
Repeated reading of the same source yields correlated records, not
fresh preparations. This construction supplies no native first-event
law, autonomous controller, complete physical apparatus family or
L1-to-L5 acceptance. The intermediate interaction changes the checkpoint;
returning to its free endpoint does not establish feeds_U=false.
The previous clean-energy obstruction is unchanged: externally driven
classical-field control is not a finite clean energy-conserving apparatus.

No Canon file, authority, registry row, decoder contract or existing
apparatus ownership is changed. Public Canon v90 remains active.
