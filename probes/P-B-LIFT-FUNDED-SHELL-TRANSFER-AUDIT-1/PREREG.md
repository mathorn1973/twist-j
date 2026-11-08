# Six-field independent audit preregistration

PUBLIC / NON-CANONICAL / L1. Owner and exposure: README.md. Claim #1593.
Probe: P-B-LIFT-FUNDED-SHELL-TRANSFER-AUDIT-1.
Base: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, Public Canon v103 ACTIVE.
The complete authority and admitted specification files are in SOURCES.tsv.

## 1. Equation and fixed question

Independently decide G1-G5 of P-B-LIFT-FUNDED-SHELL-TRANSFER-1/PREREG.md
at 7449b22d4ea3d23a0954d2b22f57215525f63abb, not a revised future target.
Use precisely its unchanged Af,L,V,Bf,H, Lambda=LZ4 and S(a,b,c,d)=(-c,-d,-a,-b).
Cell C=(y,q,r) is in Lambda x F5^2; beta=(Sy,-q,-r).
Projection pi=(y1,y0,y3,y2,q,r) mod5.
Full selected carrier X=C x C x N0 x C2, energy H(ys)+H(yr)+B.
K exchanges complete cells. F beta-transforms the receiver exactly when
the available receiver-plus-bank energy can pay H(Syr), otherwise fixes
all state. This is the same frozen funding law B>=H(Syr)-H(yr), implemented
without using the author's code. Ustar applies K at controller0 or F at
controller1, then toggles the controller. Literal full-state equality.

Fixed mathematical targets: generator b intertwining; integral S action
on Lambda; exact coset minimum15 at native rho4; total inverse/energy/
nonnegative-bank law including occupied/refused states; two actual native
source trajectories with equal quotients and initial field energy5,
common ZERO receiver/B30/controller0, emptied source and receiver field
energies15/35 with bank20/0; exact sharp common bank30; omitted-F and
eight-step-return limitations. Unbounded conclusions require PROOF.md.

## 2. Code and independence

Freeze this file, PROOF.md, README.md, SOURCES.tsv and verify.py in one
public Git pin before any scientific run. Read back each file's actual
bytes before executing. Source author proof/code/output/run/result remain
unread until after this independent first execution and its recorded
hashes. No imports or execution of author code, no cherry-picking result
logic. Numerical targets already exposed in the author specification are
not blind predictions. The reviewer is a different session from #1591;
prior own #1592 work means this is not independent of that earlier idea.

verify.py uses the standard library and exact integers/Fraction only.
It derives its own complete enumeration box from the inverse Gram matrix
rather than the author's square-fiber enumeration. Finite states use a
controller-first tuple and independent energy-budget transition code.
No random sampling, floating point, network, subprocess or file output
occurs in the scientific verifier. Matrices are explicit public inputs.

## 3. Carrier and finite inventory

A. Exact matrix identities and principal-minor positivity. All625 raw
four-residues for the integral image test and S closure; all25 source
fiber pairs at those residues for pi beta=b pi, hence15625 projections.
All quadratic/coset coefficients are fixed with zero, basis and pair sums;
a further625 integer coset vectors in [-2,2]^4 audit the exact polynomial.

B. For H(u)<=4 use the proved coordinate bounds
u_i^2 <= 2*4*(Bf^-1)_ii and exact integer square roots. Enumerate that full
box, retain H<=4, and map by L. This exhausts every Lambda field with
H(y)<=20. Require20 unit preimages and20 distinct unit image residues.
Within the complete H<=15 subset classify rho4 minimizers and print them
without freezing their unknown multiplicity as a numerical target.

C. Every ordered field pair in Lambda with H(ys)+H(yr)<=20, every bank
0..20-H(ys)-H(yr), both controller phases, common fixed source fiber(1,2)
and receiver fiber(3,4): K^2,F^2, both Ustar inverse directions, positive
bank, actual total energy and lattice closure. Counts are printed as actual
results, never used to shrink a failed domain. Separately exhaust all625
four-fiber tuples, both phases and the five receiver/bank controls
(Y1,10),(Y1,9),(Y2,30),(Y2,29),(0,0), with occupied source Y2.
This product is not falsely called the full fiber product of every pair
in C; universal fiber/occupied-state assertions use the proof.

D. Both fixed actual native preparations through boundary4, common
quotient histories, both full K;F executions at bank30, every bank0..40,
exact first common acceptance threshold30, complete source depletion,
occupied receiver contents retained by K, eight-step returns and five
receiver-only Af steps after completion. A missing F must leave the two
field energies equal5. The constant reader is current H(yr), with no
source/controller/message/history argument. Negative controls explicitly
reject receiver overwrite and the wrong-sign bank compensation.

## 4. Systematics and scope guards

This is a selected pair-cell extension, not a complete compiler of
state-selected native U. The comparison is one accepted generator b after
an additional whole-cell exchange. Underfunding cannot be reported as
original-U continuation. The source integer lift, energy form, bank,
controller with zero chosen energy, exchange and scalar read access are
premises. Common total energy35 does not mean two unequal total-energy
messages: only field/bank distribution differs. Old rational q/r-port and
old resource-only chain have different carriers and permissions.

No present-zero/absence detector, physical clock, permanent record, new
native gate, Hodge action, SI units, Born/occurrence law or L2-L6 lift.
The boundary-four minimum is not asserted unique. Ustar eight-step return
is tested/proved for the nominated preparations, not assumed on all X.
No author/result exposure before independent freeze and first run.

## 5. Failure threshold and execution

Any exact contradiction to a target is SCIENTIFIC_FAIL with its named
falsifier and no PASS. Threshold is zero. The verifier catches only its
explicit scientific discrepancy exception to print AUDIT FAIL and exit0;
an unexpected runtime error is an execution failure, not scientific PASS.
Every completed scientific failure and first capture is retained unchanged.
No source, target, threshold or pin repair is allowed.

First run from the clean pinned repository root by the PUBLIC procedure:
python3 probes/P-B-LIFT-FUNDED-SHELL-TRANSFER-AUDIT-1/verify.py
Use the deterministic environment and600-second timeout of the current
repository verifier checker, capture actual stdout/stderr and all run
fields, then apply tools/check_verifier.py on this changed probe. Required
PR workflow replays the same frozen source on x86_64 and aarch64; the local
architecture and all replays are disclosed. EXPECTED.txt is the genuine
first completed stdout, not a manufactured successful transcript.

F1 matrix, image, intertwining or cost/coset identity failure.
F2 a lower-energy admissible rho4 vector or missing bound completeness.
F3 any full-state K/F/U inverse, energy, bank, image or occupied-state failure.
F4 any actual fixed-source prefix/contact/readout or bank-threshold mismatch.
F5 any claimed negative/return control mismatch or scope overstatement.

## 6. Action layer and ownership

L1 only, independent conditional proof and exact finite audit. No public
status promotion. Only this one probe path changes. No author edits,
Canon/registry/frontier/gates/policy/workflow changes, merge or release.
The independent audit owns no wider physical or native admission question.
