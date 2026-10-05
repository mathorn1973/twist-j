# P-U-ION-LS-CONTACT-BOUNDARY-1 preregistration

2026-10-04. Author of record: A. M. Thorn. PUBLIC; NON-CANONICAL; L1.
Reservation: [#1360](https://github.com/mathorn1973/twist-j/issues/1360).
Branch: `probe/P-U-ION-LS-CONTACT-BOUNDARY-1`.

This is the prospective freeze of a new exact audit of a specified effective
physical model and its contact obstruction. The accepted scientific programs
have execution count zero before the public pin. Static syntax and source
review are permitted. No import or execution of either scientific program is
permitted until the accepted files are committed, pushed, and read back.

## Authority and exposed reasoning

Public main is `2973a432303e046aacb2cee3cea97254ea3ab8eb`; Public Canon v97
remains authoritative, with content commit
`82ecf0aac0ee79c947000968e71573d4c65d386d`, SHA-256
`257f83a386aad7d309f7017bd719b6212e3cffea60e4986caa5169d6543f108d`, 897762 bytes.
Neither Canon nor its registries are changed by this probe.

The proposed symmetry bound, symbolic energy formula and fourfold merger
were already discussed in the user-visible preceding review. The recorded
HISTORY.csv was previously read and grouped; its counts are known. This is
not a blind discovery, fresh experiment, or retrospective claim that those
observations were preregistered. The new formal evidence is exclusively the
subsequent execution of the newly frozen audits. The analytical proofs are
protocol content, not quantities estimated by a numerical pulse search.

## Field 1: equation and frozen target

At the actual second entry, `kappa=0,r=4,q=0,s=a2+1 mod5`. The isolated
target on the two active ports is

```
C4(s,q)=(q+4,s+1) mod5.
```

Require all 25 original label histories and a real disconnected checkpoint
after C, before the native continuation. At a2=4 the exact input ports are
|00> and the required output is |41>. The complete original state and all
other outputs remain obligations; matching only one bit is insufficient.

MODEL.md fixes the direct calcium-ion levels, common port dictionary, drift,
effective light-shift Hamiltonian, completed-loop control class and physical
approximations. PROOF.md derives the endpoint propagator from that Hamiltonian.
Its spatial laser phases may differ. Its per-level light-shift profile and
mode-coupling magnitude on the two ports are the same. No simultaneous or
interleaved data rotation inside an unfinished loop is admitted. Completed
loops, identical local rotations, common drift, and remainder-only operations
generate the declared class.

The consequent full operation commutes with P_ports tensor I_remainder.
The predicted negative decision is unconditional success probability at most
1/2 for each of the five histories with a2=4. Define worst input write error
as max over histories of one minus the probability of the correct ordered
port pair. Failed detection, leakage and discarded shots are failures, not
postselected successes. Requirements on the archive can only reduce complete
success. The criterion tested is whether this class can meet error <1/2.

For an approximate complete output within trace distance delta_out of the
ideal symmetric output on every admitted inherited input, PROOF.md gives
error >= max(0,1/2-delta_out). No finite-device value of delta_out is supplied or
computed. Approximate entry errors need a separate term; the primary theorem
has an exact rank-one coded entry.

## Field 2: code

`verify.py` is a standard-library exact audit using integers and Fraction.
It checks the pinned input manifest before importing `verify_independent.py`.
The independent program was written by a separate reviewer from this scope
without reading the primary implementation. It uses a separate orbit and
symbolic representation and must agree on the complete shared report.

The primary program constructs an exact projector certificate for
P_plus E41 P_plus <= (1/2) P_plus. Both programs audit the swap orbits,
the C4 permutation/involution, symbolic common-rotation and closed-phase
symmetries, actual stored contact entries, full-state historical fibres and
symbolic endpoint-energy coefficients. No sampled pulse list stands in for
the all-sequence proof. The real-time Magnus integration, arbitrary-state
argument and robust error inequality are analytical proofs in PROOF.md;
the finite verifier does not independently measure or integrate a device.

Accepted files: PREREG.md, MODEL.md, PROOF.md, SOURCES.md, README.md,
REVIEW-PREREG.md, verify.py, verify_independent.py, INPUTS.json. The input
manifest binds the supporting texts, independent verifier and all read
source files by raw-byte SHA-256 and length; verify.py pins the manifest
SHA-256. Neither verify.py nor INPUTS.json hashes itself through that
manifest. The public Git commit pins the entire set, including those two
files, whose identities are also recorded in RUN.md. Any accepted-content change after pinning
invalidates this prospective execution; do not repair it in place.

## Field 3: carrier and data

The planned data carrier is fourteen directly encoded five-level ions: two
source ports and two ordered sextuples (p1,p4,p1p,p4p,q,r). The same level
dictionary is fixed at preparation. The original counter is represented by
a counted physical controller over the finite horizon, whose dynamics are
not constructed in this negative result. All motion, history memory, work
sources, controller and environment belong to the included remainder.

For the impossibility proof, this remainder is deliberately allowed arbitrary
dimension and arbitrary history-dependent states. This favourable enlargement
does not claim finite resource sufficiency or identify a physical battery.
The theorem excludes the mandatory contact even with that extra freedom.
An actual finite model lying in the specified class inherits the exclusion.

Runtime source files are the already accepted
`probes/P-U-TWO-TRACE-PORT-CONTACTS-1/evidence/primary/HISTORY.csv`,
`CONTACTS.csv`, and its `CONTRACT.md`, pinned in INPUTS.json to their bytes at
the stated base. The verifier reads the stored rows, not the predecessor
verifier, and does not rerun or alter the predecessor dynamics.

The history audit includes all 250 rows and all 50 contact rows. At each
n=0..9 it groups the complete original state, excluding only input labels.
It verifies the fourfold n=9 merger for {0,1}x{0,1}. The dimension-four
remainder consequence assumes a fixed tensor factor and identical pure data
codeword; equal coarse readings alone give a fibre-capacity bound instead.

The energy audit uses independent symbolic level energies. Under identical
spectra and E0=0 it produces the five coefficient vectors in E1..E4. It
does not convert endpoint energy into consumed laser work or use the
isolated-C ledger for a hypothetical combined U6*C step.

## Field 4: systematics and scope controls

- Raw light-shift H(t) need not commute with port swap. Only the derived
  completed-loop endpoint is used. Unclosed/interleaved pulses are excluded.
- The Lamb-Dicke, rotating-wave, adiabatic-elimination and mode-selection
  conditions are physical limitations, not exact features of every apparatus.
  Unmodelled modes and model error are not assigned an invented bound.
- Common spectra include free drift. Differential drift or addressing,
  asymmetric ancillary couplings and unequal fixed dictionaries change the
  class. The control encoding K(s,q)=(s,q+4) conjugates C4 to SWAP and is
  explicitly checked as a boundary, not claimed implementable here.
- Symmetry is P_ports tensor I_remainder, never a simultaneous exchange of
  ports and their potentially different environments. No fresh remainder at
  time six is assumed. A pure coded active pair factors from its inherited
  remainder, which may itself have arbitrary correlations.
- No isolated post-C physical time is required by the general predecessor
  contract. It is required only by this candidate. Combined U6*C candidates
  are outside the exclusion. No general fourteen-ion pulse schedule is built.
- The finite source audit is disclosed reuse of old data. The result is a
  mathematical statement in an external quantum model, not a TWIST-J Born
  derivation, physical occurrence claim, L1-to-L6 lift or Canon promotion.

## Field 5: thresholds and decisions

Every executable check has exact equality and zero tolerance. Any source
hash/length drift, incomplete input coverage, wrong permutation, failed
symbolic identity, failed projector certificate or disagreement between
audits rejects this candidate execution. Preserve an actual failure under
POLICY.md; never move the threshold or patch frozen code after inspecting it.

Successful verifier completion supports the decision
`SYMMETRIC-ISOLATED-CONTACT-EXCLUDED-BELOW-1/2` at the explicitly restricted
scope. This is a negative feasibility outcome with a successful audit, not
physical realization PASS. The bound need not be attainable by the actual
LS control library. A symmetry-sector saturation vector proves only the
sharpness of that larger algebraic sector.

No feasible full-history point in R is certified. Within this candidate,
the portion with exact entry, exact model, isolated contact and worst write
error <1/2 is empty for every permitted finite sequence duration and resource
state. At model error delta_out the corresponding excluded threshold is
max(0,1/2-delta_out), conditional on a separately established delta_out.

## Field 6: action layer and execution protocol

L1: exact state-space and operator consequences of an explicitly adopted
external effective Hamiltonian and already recorded logical history. No
registered owner closes and no new cross-layer gate is claimed.

1. Obtain static independent review; do not import or execute the programs.
2. Commit accepted files as A. M. Thorn, push the named new branch, and read
   its exact public commit/tree/blobs back against local raw bytes.
3. Verify clean accepted content and no prior EXPECTED/RUN files. Execute
   `python3 probes/P-U-ION-LS-CONTACT-BOUNDARY-1/verify.py` from the repository
   root on Linux, with LC_ALL=C, LANG=C, PYTHONHASHSEED=0,
   PYTHONDONTWRITEBYTECODE=1 and TZ=UTC.
4. Preserve actual stdout as EXPECTED.txt and record exact pin, file hashes,
   environment, timestamps, exit and stderr in RUN.md. Write RESULT.md after
   execution. Do not claim CI success before it occurs.
5. Open a separate PR. Repository checks replay the pinned audit on x86_64
   and aarch64. No old probe, Canon, registry or workflow file is edited.
