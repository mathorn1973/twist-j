# PREREG: C-PENTIT-REAL-SUMZERO-SHARP-COUNTEREXAMPLE-N

**NON-CANONICAL / L1 notes incubation. No formal public-probe promotion.**
Date: 2026-10-02. Owner: authorized TWIST-J continuation session.
Object lock: https://github.com/mathorn1973/twist-j/issues/1344.
Branch: `notes/c-pentit-real-sumzero-sharp-counterexample-n`.
Path: `notes/C-PENTIT-REAL-SUMZERO-SHARP-COUNTEREXAMPLE-N/`.

## Authority, input custody and exposure

Public authority remains Canon v97. Input main is
`01821412879dba442e1c864c61855fb4a4dfea99`, merge of #1343; public tag
`canon-v97` peels to `738e0421bd15aaea5bb6ef2a56f1cab752d44de5`.
Canon content commit is `82ecf0aac0ee79c947000968e71573d4c65d386d`,
SHA-256 `257f83a386aad7d309f7017bd719b6212e3cffea60e4986caa5169d6543f108d`,
897762 bytes. `STATUS.md`, `POLICY.md`, `AGENTS.md`, CORE and FRONTIER were
read. The complete merged original Wigner note is an immutable input.

Before claiming this lane, exact issue and branch queries, the complete main
tree and all 194 remote head refs were checked. No matching live lane, path
or claim lock was found. The issue was created before any commit.

**All targets were exposed before this freeze.** The cosine witness,
its 25-cell Wigner table, negativity radical and squared gap were derived
analytically by the coordinator and checked separately by two collaborating
agents, before any new executable gate. The improved lower-bound argument
was also derived and reviewed before the pin. No blindness, independent
software implementation, physical measurement or architecture independence
is claimed. The verifier is a confirmation audit of these known targets.
Independent reasoning here means separate proof checks within this same
collaborative session, not an external referee or independent laboratory.

The public pin will contain this file, `verify.py`, `PROOF.md` and
`LOWER-BOUND.md`. Their commit, Git blobs, SHA-256 and byte counts are to be
read back before the first scientific execution and recorded in `RUN.md`.
Frozen files will not be rewritten after execution.

## 1. Equation

Keep exactly the original convention
`A(q,r)|j> = zeta5^(2*r*(q-j)) |2*q-j>` and
`W(q,r)=Tr(rho*A(q,r))/5`, negativity `sum max(0,-W)`.
The target state is
`psi_j = sqrt(2/5)*cos(2*pi*j/5+pi/20)`, `j in F5`.
The proposed universal value `(1+sqrt(5))/10` is rejected if this normalized
real sum-zero state has smaller negativity, with exact signs and arithmetic.
The separate general statement to proof-review is
`N >= (1/2)*tan(pi/10)` for every normalized real sum-zero pentit state.

## 2. Code

`verify.py`: Python 3.12, standard library only, exact `Fraction` arithmetic
in `Q[t]/(t^16-t^12+t^8-t^4+1)` with `t=exp(i*pi/20)`.
Represent the unnormalized real cosine vector, whose norm squared is `5/2`,
and form its normalized density operator without square-root approximation.
Construct all phase operators and compute all Wigner cells directly from the
trace, independently of the displayed closed-form table. Require exact
equality to that table and the radical/gap identities.
No floats, random sampling, external packages, native generators, files,
network, imports of the original implementation or numerical optimization.
The general lower bound is a proof, not a finite software census.

## 3. Carrier and data

`F5^2` phase-point labels, the declared pure real sum-zero state and the
exact cyclotomic field above. Read-only original premise:
`notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/PREREG.md` and README at input main.
No imported datasets and no rerun of the original 624-preparation census.
The known sign support is supplied by first-quadrant positivity in the
exposed proof, not inferred from a floating approximation.

## 4. Systematics and bounded claims

Index arithmetic is modulo five. Constant Wigner strips are `r=1,4`.
Fix the specified embedding `t=exp(i*pi/20)`; algebraic conjugates must not
be mistaken for this embedding. The exact audit checks algebraic identities;
the proof supplies real-root signs. Distinguish the finite balanced-source
class from all real-source states. The counterexample is not a new global
minimizer and not a native state-preparation procedure.
Only one local x86_64 run is planned. Notes-only repository CI does not
replay this verifier and cannot earn a two-architecture scientific gate.
Do not change the original note, public Canon, Registry, Frontier, workflows
or any gate/threshold. No claim of a native occurrence law or Gate 0 closure.

## 5. Failure thresholds and fixed targets

Zero tolerance for any incorrect identity. Abort with nonzero exit on a
failed assertion, preserving the pin and recording the failure.
Require: real zero sum, norm squared `5/2` before normalization; normalized
rank-one density; Hermitian involutive phase operators; all 25 trace-derived
cells equal the analytic table; 12 positive, 2 negative and 11 zero cells
using the proof's fixed signs; total Wigner weight 1 and squared sum `1/5`;
`N^2=(5+2*sqrt(5))/100`; proposed-bound squared minus `N^2 = 1/100`.
A convention mismatch, omitted premise or missing factor in either proof
rejects the corresponding claim even if the program passes.
No target, threshold, sign convention or verifier changes after the pin.

## 6. Action layer and disposition

L1 exact representation and analytical bound only. Accepted proof plus an
exact passed audit supports candidate-T within this NON-CANONICAL note.
The disproved proposed global bound is a mathematical negative result, not
a public Registry F promotion. The general sharp minimum remains open.
After the run add `EXPECTED.txt`, `RUN.md`, `RESULT.md`, `README.md`,
`REVIEW.md` and a SHA-256 custody manifest. Publish a draft notes-only PR.
Formal probe or Canon promotion, if wanted later, requires its own declared
scope and procedure.
