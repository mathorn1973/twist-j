# P-NATIVE-RECEIVER-CARRY-MIRROR-1

NON-CANONICAL / L1 / exposed-result formal publication replay.
Owner: A. M. Thorn, v109 integration, 2026-11-03.
Reservation: https://github.com/mathorn1973/twist-j/issues/1883.
Base: ACTIVE Public Canon v108 at
17de90b58f814238e151aac77badde6654b52627.

## Question and exposure

Does the actual first native tick, on one common receiver preparation, supply
the low digit for an explicitly routed forward/archive/inverse carry circuit,
with exact marked return and opposite paired carry character? Can the circuit
be executed with the pinned discrete arithmetic compiler on the same addressed
memory, with its complete workspace restored? What additional carry precision
distinguishes J from its inverse when the INPUT letter is held fixed?

All these results and the source outputs were exposed in the supplied
C-NATIVE-RECEIVER-CARRY-MIRROR-N attachment before this formalization. This is
not prospective discovery or independent mathematical acceptance. PROVENANCE.md
records exact custody and public dependencies. The new verifier consolidates
and strengthens finite checks; it does not import a historical run archive.

All files in this directory are committed, pushed and publicly read back
before the first execution of verify.py. Pre-pin work is limited to reading,
proof construction, hashing and AST/static checks. After the completed run,
append only EXPECTED.txt, RUN.md and RESULT.md. Frozen source and thresholds
are not changed to rescue a failure. The repository abandoned-pin rule applies.

## Exact carrier, code and common preparation

Native coordinates x=(A,B,C,D,q,r) lie in F5. The original update is
T_t(x)=g_(sum(x)+2t mod5)(x), with the five generators written in PROOF.md.
Use its genuine origin-zero first tick t=0, with receiver (q,r)=(0,1) for all
625 piston tuples. Put s=A+B+C+D+1 mod5 only in the validation oracle.
Admit s!=0: 500 preparations, 125 for each of four boundary classes. The other
125 preparations are zero-TRACE controls; they are not zero piston tuples.
No input trace, selector index or character is passed to the carry circuit.

The receiver shear is q <- q+r+2, keeping r. In O=Z[j], Phi_5(j)=0,
lambda=1-j, J=1+j^2 and J_inverse=-j-j^2. A depth-two word lo+hi*lambda
has two F5 digits. Multiplication and inverse are

    F(lo,hi)=(2lo,3lo+2hi), I(lo,hi)=(3lo,3lo+3hi).

Apply shear, F, SWAP(high,archive), I, and inverse shear in that order.
High and archive are initially zero, independently of the input. The live
forward low is the inverse low. The receiver q cell IS the multiplier low cell;
it is not copied from an externally calculated s. Retain both carries.
Read the admitted native sign by q=1 -> -1, q in {0,2} -> +1 and carry
sign by -chi_5(residue). Other q values are outside this native reader contract.

For the separately counted second native reading, allocate one additional
six-cell native machine with fixed pistons (4,0,0,0), receiver (0,1) and its
own enabled origin. A SUM from the actual forward low into its first piston
precedes its first native tick. This declared write and independent timing are
not consequences of bare U. Its resulting six cells remain in the final state.
No global inverse of the native tick is assumed or executed.

## Frozen finite audits

1. Construct all 625 native ready states and both bit updates directly from
   the five generators. Derive the two complete trace-sheet maps, and confirm
   rank two on nonzero sheets after either first symbol. Check all 500 admitted
   source tuples, zero-sheet controls, the four exact receiver rows and the
   unique affine port (1,1,2) among all 125 affine scalar maps. This rank
   obstruction concerns the CURRENT TRACE port under a common nonempty clock
   word, not the full checkpoint or every possible receiver decoding.
2. Audit all 25 two-digit words in both multiplier compositions and all 625
   occupied (q,r,high,archive) states through the complete reversible circuit.
   Compare its closed affine formula and its involution. The marked contract
   still requires initially blank high and archive cells.
3. Compute integral carries in both j and lambda polynomial bases, using exact
   integer division with recomposition. For counting and balanced digit sections,
   compare full coefficients, exact paired-letter return and
   C_pair=-J_inverse*C_forward. For the SAME input letter, confirm equal first
   carry residues 3b. For both reader lifts compute the second carry coefficient
   and slopes 2 (J) and 3 (J_inverse), for b!=0; both carries vanish at b=0.
   The extra coefficient is an audit of the integral carry, not a free readout
   from the two-digit compiled device.
4. Preserve controls: direct inverse with unchanged low has no first-residue
   sign flip; inverse on the FULL forward word erases the carry; deleting +2
   gives the wrong marked digit in all 500 cases despite 125 incidental sign
   agreements; extending the affine port to s=0 routes all 125 controls to 3.
5. Expand the exact pinned arithmetic compiler at depth two into only SUM, EQ,
   MUL, SHIFT, REFLECT and SCALE. Require 40348 primitives per multiplier,
   50 compiler cells including two data and 48 workspace cells. Check every
   two-digit input in each direction, an untouched external archive sentinel,
   all five marked mirror inputs and literal reversal of their reversible
   circuit. Workspace must be zero at each multiplier boundary.
6. Execute all 500 admitted preparations in one mutable 62-cell memory. The
   compiler's low wire is primary q from initialization. Allocate exactly
   50 compiler cells, one carry archive, five other primary native cells and
   six secondary native cells. Check actual intermediate digits, both carries,
   complete restored primary post-tick checkpoint, complete secondary output
   and clean 48-cell workspace. Count literal expanded multiplier and routing
   gates; no ADD/H shortcut or physical pulse evaluation is allowed. Both
   origin ticks remain native basis-state transitions, outside that gate count.

No random samples, floating-point arithmetic, fitted threshold, environment
chosen result or network fetch enters the scientific run. Execution uses only
Python's standard library and the local public pinned source. Runtime helper
hashes and byte lengths in RUNTIME_SOURCES.json are checked before import;
the manifest itself is frozen in the same public commit. Optimization is
rejected. No external compiler checkout is needed.

## Falsifiers and execution

Any wrong native row, port/digit/sign, ring identity, carry coefficient,
full-state inverse, trace map/rank, primitive alphabet/count, wire boundary,
workspace reset or complete primary/secondary endpoint is a failure. The
negative controls must exhibit their specified failures. There is no tolerance
and no post-pin threshold adjustment. Report nonzero exit/stderr faithfully.

Command from the repository root:
`python3 probes/P-NATIVE-RECEIVER-CARRY-MIRROR-1/verify.py`, with Python 3.12 or
newer, assertions enabled, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0,
LC_ALL=C, LANG=C and TZ=UTC. Remove inherited PYTHONIOENCODING,
PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR for the first recorded run. The normal repository verifier runner has a 600-second limit. Scientific
stdout excludes paths, wall time and platform-dependent values. Record exit,
stderr, byte counts and SHA-256 in RUN.md; commit one exact EXPECTED.txt and
require the normal x86_64/aarch64 PR jobs to match it. Do not call notes-only
integrity checks a scientific replay.

## Intended v109 scope and limits

Candidate-T: the stated conditional port/paired-carry/depth/trace-obstruction
proofs, pending independent mathematical review. Candidate-C: the enumerated
finite addressed-memory execution, pending its actual recorded runs and
required architecture gate. Neither label is a Canon promotion.

This is a supplied interconnection of native state transitions and discrete
arithmetic gates. It does not derive routing, archive allocation, second
origin, inverse scheduling, pulse dynamics, a physical apparatus, the Hermitian
time step or an observed arrow of time. Distinguishing two multiplier labels
at fixed input is not measuring time direction. No continuous or experimental
calculation is performed. The fixed-input and paired-edge protocols remain
distinct. This F5 carrier and alphabet are not the contact-bank carrier of
PR1879: no shared-device interface, archive renewal or autonomous repeated
operation follows. Canon, registry, policy and workflows stay unchanged.
