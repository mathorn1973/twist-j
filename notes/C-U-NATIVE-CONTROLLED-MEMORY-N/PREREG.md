# C-U-NATIVE-CONTROLLED-MEMORY-N: frozen exact audit

**NON-CANONICAL. L1 analytical candidate; no registry or physical promotion.**
Author: A. M. Thorn. Date: 2026-10-29.

This is a new notes candidate, not a continuation or reuse of a sealed probe.
The equations were derived and reviewed analytically before this audit was
written. No claim of blind prediction or independent external acceptance is
made. Both audit implementations and this contract must be committed, pushed,
and publicly read back at one immutable commit before their first execution.
The exact pin and SHA-256 values will be recorded in RUN.md after execution.
Compilation and syntax inspection before that pin are not scientific runs.

## 1. Equation and frozen question

Use the unchanged six-coordinate native law, all arithmetic in F5:

    z=sum(x), theta_n=popcount(n) mod2,
    U(n,x)=(n+1,g_(z+2 theta_n mod5)(x)).

The five generators are explicitly transcribed in PROOF.md and both programs.
At the common counter zero admit the product family

    x_(lambda,mu,chi)=(lambda,mu,4-lambda,1-mu,chi,0),
    lambda,mu in F5, chi in {0,1}.

The source and old memory occupy the fixed raw pairs (p1,p1p) and (p4,p4p).
The control occupies q. There is no added register or inserted gate. The
candidate logical law, read at every counter at least three, is

    chi=0: (source,memory)=(mu,lambda),
    chi=1: (source,memory)=(lambda,mu).

Both fixed readers and their complete domains are frozen in PROOF.md. Each
uses its own piston pair plus shared original q,r, never the other pair,
the counter, a saved preparation, or historical observations. Write readers
are pending at counters 0,1,2; hold readers retain their labels from zero.
Pending is not an empty raw memory and is distinct from a recorded zero.

With A=p1+p1p, B=p4+p4p, C=p1-p1p-2, D=p4-p4p-1, the closed tail is

    E0: z in {1,4}, A=B, B^2=4;
    E1: z in {1,4}, A=-B, B^2=1.

The candidate includes the complete fixed-raw-support response identities
for the actual three-step endpoint E3, not physically supplied output gates:

    E3 P_S,delta = P_M,-delta E3 (write),
    E3 P_S,delta = P_S,-delta E3 (hold),

and the analogous memory-to-source / memory-to-memory equations. P changes
the two named raw coordinates by (+delta,-delta). Input changes are admitted
preparation alternatives; endpoint P is an algebraic comparison operation.

BOUNDARY.md freezes a separate continuation statement: for any origin-zero
preparation family, common m>=3, and fixed affine target with a completely
common state at m, no current-target reader, even supplied the counter,
can later retain a nonconstant payload forever. Its proof uses the common
signed permutation and explicit infinitely many equality times. The finite
audits do not replace this unbounded-time proof.

## 2. Code

- verify.py: direct coordinate formulas, exhaustive product preparations,
  complete shell parametrization and raw-state comparison.
- break_check.py: separately written affine-matrix implementation and direct
  raw-state shell scan. It imports neither verify.py nor a predecessor.
- PROOF.md and BOUNDARY.md: the complete analytical statements and proofs.

Only the Python standard library and exact integer arithmetic modulo five
are admitted. There are no floats, random seeds, fitted constants, external
datasets, network calls, downloaded packages, or imported scientific helpers.
Runs use python3 with deterministic environment settings and no optimization
flag that would disable assertions. The two programs need not have identical
stdout to each other. Each program must reproduce its own first exact stdout
byte for byte on each architecture.

## 3. Carrier, inputs, and authority

The scientific source is mathorn1973/twist-j main
a193e389fb1ddb0bdc89165b015c95a17eb1e425, ACTIVE Public Canon v106.
The annotated canon-v106 tag resolves to that main commit. Content commit
9242db4f040d67d9417eacd06612230b74248cff is its ancestor. The canonical
SHA-256 is 52302c640033dd15d4a7a075cad16fa48b1473b7396d1f7413536a9ec45422e7,
1370107 bytes. The five-file canonical manifest matches. The main architecture
jobs and aggregate check of run 40556926452 passed; publication run
40557096572 passed. These are inherited authority checks, not new executions.

Native data are the 15625 raw heads, the 6250-point stable union, the complete
50-point product preparation, and the proposed 1000-point closed tail.
The programs encode the frozen law directly, so later Canon additions do
not alter their replay inputs.

The source audit includes the current Canon, PR #1430, issue #991, the native
occupied-exchange note, and the native-memory-composition note identified in
PROOF.md. Earlier native occupied operations and 50-point retained-context
families already exist. No first-native-control or first-occupied-memory
claim is admitted. The distinct target is this raw-q selection of two actual
native words and their fixed-piston-pair swap/hold response.

Before reservation, all 327 remote heads were scanned, together with relevant
open issues and the registry. No exact candidate identifier or exact selected
swap/hold contract was found. Related work remains credited and untouched.

## 4. Systematics and exposed choices

Preparations are admitted, not produced by a preceding native process. The
offsets 4 and 1 are a chosen encoding: in the displayed opposite-sum family,
the chosen condition of equal write-output pair sums selects them. This is
not a physical uniqueness or preparation theorem.

The control migrates from q into piston-sum sectors. It is not an unchanged
raw control register. Both readouts share q,r. Classical label routing is
not a coherent quantum gate, a Born law, a spatial locality theorem, or a
physical detector. The old memory is moved, not erased. A write is one-shot;
the native tail does not supply another independently selected operation.

The two authors of audit code and the analytical reviewers participate in
the same authoring session. Separate implementations and architecture replay
are useful checks but do not constitute independent project acceptance.

## 5. Frozen failure thresholds

Every claimed finite identity is exact. One counterexample fails that target.
No inequality tolerance, resampling, omitted input, changed readout, or moved
threshold is permitted after the immutable pin.

The required primary checks are:

1. All 50 product preparations, all 200 prefix checkpoints, the actual ace/bbd
   words, and the full pending/hold chronology agree with the frozen formulas.
2. Parametrization and direct raw scan agree on exactly 1000 closed-tail
   states, with exactly 50 logical outputs and 20 states for each output.
3. All 2000 shell state/bit transitions preserve the sector, both labels,
   control, and the displayed invariant products.
4. All 500 complete-state source/memory perturbation equalities hold.
5. All 5000 paired-port translations leave the full logical reading unchanged.
   This is a blindness / retained-record result, not a pulse-event record.
6. All 15625 origin-zero heads synchronize after three actual ticks to the
   trace-one sheet of 3125 states, with five heads per image.
7. All 12500 stable state/bit cases satisfy the selected affine block law.
   Dependencies are checked separately within each fixed trace sheet.
8. The finite coefficient/driver identities supporting BOUNDARY.md are
   checked; the infinite-time conclusion is carried only by its proof.
9. Negative controls reject a changed control, discarded old-memory label,
   wrong raw transport sign, and confusion of pending with recorded zero.

The separately implemented audit checks its explicitly frozen complete
domains and assertions. Every assertion in either frozen program is a gate.
Any exception or assertion failure is retained and reported; source is not
silently repaired under the same pin. A defect and a mathematical falsifier
must be distinguished in the result.

## 6. Action layer and disposition

Everything new is conditional L1 mathematics in a NON-CANONICAL note. A pass
means that the specified finite construction survived these exact audits.
The proof, shared-session reviews, first stdout and environment metadata are
reported separately. A two-architecture byte match is reported only if it
actually occurs; a one-architecture result is not renamed as such a match.

No Canon, registry, frontier, workflow, release, physical outcome law, SI
calibration, native-to-Hamiltonian bridge, Lorentz geometry or proper-time
claim is changed. A draft pull request is a review surface, not acceptance.
