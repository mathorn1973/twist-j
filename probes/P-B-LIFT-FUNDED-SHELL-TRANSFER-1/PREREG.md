# Six-field preregistration: funded b-lift on the fixed integer field shell

PUBLIC / NON-CANONICAL / L1. P-B-LIFT-FUNDED-SHELL-TRANSFER-1.
Owner ChatGPT-b-lift-shell-contact-20261017. A. M. Thorn, Apache-2.0.
Reservation https://github.com/mathorn1973/twist-j/issues/1591.
Authority: Public Canon v103, main/tag dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d;
content 01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. CANON.md SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b,
1052518 bytes. Five hashes, ancestry and main two-architecture checks passed.

New narrow constructive application, not a takeover of #1589 or native/
physical owners #1398/#1498. No premise from the unreviewed #1583/#1585
area probes is used. Source definitions come from the current Canon.
Prior signed-affine lifts (#972), integer packet transfer (#1327), and
v103 interface classification (#1551) are credited as existing ideas.
Only the new probe path may change. No scientific program has yet run.

## 1. Equation

Use the unchanged canonical matrices

 Bf=((4,-2,2,-1),(-2,6,-1,3),(2,-1,2,0),(-1,3,0,2)),
 L=((1,-3,-1,-2),(-3,4,-2,1),(0,5,1,2),(5,-5,2,-1)),
 V=5L^-1=((1,2,1,2),(2,-1,2,-1),(0,-5,1,-3),(-5,5,-3,4)),
 Af=((1,0,1,0),(0,1,0,1),(-2,1,-1,1),(1,-3,1,-2)).

H(y)=y^t Bf y/2 is the public positive integer form. Lambda=L Z^4 is exactly
{y:y0+2y1=y2+2y3=0 mod5}, and H(Lu)=5H(u). Define

 S(a,b,c,d)=(-c,-d,-a,-b),
 beta(y,q,r)=(Sy,-q,-r),              q,r in F5,
 pi(y,q,r)=(y1,y0,y3,y2,q,r) mod5.

G1: S preserves Lambda and is an involution; pi beta=b pi for the actual
native generator b, not generally for the full state-selected native U.
The conjugate BL=L^-1 S L is integral and involutive. Its actual field
cost is

 Delta(y)=H(Sy)-H(y)=f(y2,y3)-f(y0,y1), f(a,b)=(a-b)^2+b^2.

G2: rho4=(2,4,0,0), yb=(2,-1,0,0)=S(0,0,-2,1). Prove exactly

 H(yb+5v)=15+25[H(v)+(2,-2,1,-1).v] for all v in Z^4.

Positivity and H(yb)=15 give minimum15 on the whole rho4 coset, all of
which lies in Lambda. This strengthens the prior lower bound from5 to10
for the increase from the unique boundary-three minimum H=5. It asserts
neither uniqueness of the boundary-four minimizer nor physical energy.

Full selected two-cell carrier is

 C=Lambda x F5^2,         X=C x C x N0 x C2,
 s=(Cs,Cr,B,c),          E=H(ys)+H(yr)+B.

K exchanges the two COMPLETE cells. F acts on the receiver: if B>=Delta(yr),
apply beta and set B'=B-Delta; otherwise fix the complete state. Source
and controller are spectators of F. G3: K and F are involutions on all X,
including occupied receivers and inadequate bank. At c=0 apply K; at c=1
apply F; then toggle c. Ustar is a total autonomous permutation with inverse
obtained by toggling c first and applying the same corresponding involution.
This is a selected two-step contact, not the original native U or the old
field-chain interaction. Its scalar H and bank are exact mathematical
accounts. The finite controller has zero assigned energy, disclosed.

G4: two source unit seeds are U1=(0,-1,-1,2), U2=(0,-1,-1,1), with
Y1=(0,0,-2,1)=LU1, Y2=(2,-1,-4,2)=LU2. Both have H=5. At q=r=1 their
native projections x3 have common Q=(z,q,r)=(1,1,1), but distinct pistons.
Their actual origin-sheet histories under original U begin with x0=0 and
x0=(3,1,2,4,0,0); both have Q0=(0,0,0) and the common selected prefix a,c,e.
At n=3 the actual selected next generator is b for both.

The COMPLETE receiver is common ZERO=(0,0,0,0;0,0), the bank is common30,
and c=0. Execute K and F literally, never load a calculated endpoint.
The source must become exactly ZERO, the receiver native projection must
equal the original x4, and actual receiver H must be15 or35 while bank
becomes20 or0. Source labels select only the two source preparations and
independent comparisons, not the transition or reader. Fixed readout is
H of the actual CURRENT receiver field. It has no source, native Q, history,
message or controller input. Both receiver native quotients at the end are
identical. Total E=35 in both runs; total receiver energy including the bank
also agrees. The message controls an internal work distribution, not unequal
total source energy transfer. Both original sources deliver5 by exchange;
subsequent field work10 or30 is paid by the common bank.

G5: both messages follow the intended b continuation exactly iff B>=30;
smaller B can reject one or both. Under rejection, the model must NOT claim
original-U continuation. Omitting F leaves equal receiver field energies5;
the full receiver fields still differ, so no universal no-read claim follows.
Eight Ustar steps return each of the two nominated preparations completely,
so a forever-retained record under Ustar is not claimed. A separately chosen
receiver-only free Af continuation preserves receiver H (Af^5=I); this is
not later native U and is not an autonomously derived switch of evolution.

## 2. Code

verify.py is the sole runtime input, Python standard-library integer code.
It uses a direct signed-swap and H difference, and an independently written
same-author comparison via BL on the integer preimage and the expanded
Delta polynomial. No old scientific program is imported or run as new work.
No runtime data files, floats, random inputs, network or subprocesses.

Freeze PREREG.md, PROOF.md, verify.py, SOURCES.tsv and README.md together in
Git before first execution. Static AST/security reading and algebraic work
are allowed; no dry run or scientific import before the public pin. Read
back all source bytes/hashes and publish a receipt before first execution.
Do not alter a frozen input, range, witness, equality or threshold afterwards.

## 3. Carrier and finite inventory

The universal claims use the written proof. The exact bounded audit is:

A. Matrix identities VL=LV=5I, L^t Bf L=5Bf, S^2=I, BL integral,
L BL=S L and BL^2=I. Compare the H/Gram and Delta quadratic polynomials
on zero, basis vectors and basis sums, enough to fix all coefficients.
Verify the shell membership/inverse criterion and S closure on all625
four-coordinate residues. No fixed finite table is a physical dictionary.

B. Complete square-fiber enumeration for H(u)<=4 using
4H=Q(a,b)+s1^2+s2^2, Q=3a^2+2ab+2b^2,
2Q=5a^2+(a+2b)^2, 3Q=5b^2+(3a+b)^2,
s1=2c+2a-b, s2=2d-a+3b. Thus |a|<=floor sqrt(8cap/5),
|b|<=floor sqrt(12cap/5), |s1|,|s2|<=floor sqrt(4cap), with the
literal parity constraints. This exhausts all field Y=Lu of H(Y)<=20.
The H=5 shell must contain exactly the public twenty fields. Audit the
rho4 minimum on the complete H(u)<=3 set and print its minimizers without
an a priori multiplicity assertion. Test the universal coset polynomial on
all625 v in {-2,-1,0,1,2}^4 as a finite audit only.

C. For every ordered pair of field vectors with H(Ys)+H(Yr)<=20, every bank
0..20-H(Ys)-H(Yr), both controller phases, and fixed source/receiver fibers
(1,2)/(3,4), check K,F, opposite implementations, both full inverse
compositions, energy/bank and lattice membership. Report actual counts.
Separately exhaust all625 four-fiber tuples for the five representative
receiver/stock cases (Y1,10),(Y1,9),(Y2,30),(Y2,29),(zero,0). Guard and
integer action are fiber-independent, and the complete fiber action is
only exchange/sign; their general product proof covers arbitrary fibers.
Do not call the executed product the entire unbounded carrier or claim
that the code actually enumerates all625 fibers at every integer pair.

D. Execute both original native prefixes through boundary4, both literal
common-receiver contacts at B=30, each B=0..40 with the frozen two sources,
the omitted-F control, both eight-step returns and five free Af steps on
each completed receiver. The bound30 is fixed by the explicit costs10/30,
not retuned from a run. Raw inputs outside the advertised source family
still have total transitions, but no binary message-decoding promise.

## 4. Systematics and physical guards

The source integer lift is unique on the DECLARED H=5 source sector for
each of the two residues, by public unit classification. This is not a
procedure that physically prepares an integer Y from an F5 checkpoint.
The signed-permutation b formula is inherited, but choosing its unwrapped
integer lift and the canonical field H on this lift is a new comparison
choice, not a uniqueness theorem. Whole-cell exchange is a selected
contact whose residue projection is ordinary exchange; funding and the
bank read are further mathematical resources. No physical admission of
those resources is derived from their algebraic consistency.

The reader is a current scalar field-energy value, not a separately
materialized instrument output or append-only archive. Subsequent steps
may move or undo it. Dirty receiver contents move into the source under
K; they are not erased. Present zero and absence have no independent
occupancy tag here, so no absence detector is claimed. The original
q/r-only rational contact has not changed and remains blind to the two
same-Q histories. Extra field-energy read access changes that premise.

The two-step controller is not the native counter n. Exchange is an added
contact prefix; only the succeeding accepted beta is compared with the
native generator at n=3. No full original-U lift for every time, refusal,
source or off-preparation controller phase is claimed. Field-chain latency,
Hodge locality, classical rational wave/tape, W_b, Ucal, Born law, actual
phase, S/hbar, SI units, a complete admissible physical class and all
L1-to-L2/L4/L5/L6 lifts are excluded. No area-probe result is assumed.

## 5. Failure threshold and execution

Any discrepancy in G1-G5 fires its exact zero-tolerance falsifier. The
script prints FALSIFIER and AUDIT FAIL and exits zero so a completed
scientific failure is retained, never followed by PASS. Unexpected runtime
exception, nonzero exit, stderr, altered source or timeout is an execution
failure and must be disposed of under the repository rule; no pin repair.

From the clean pinned repository root run exactly

    python3 probes/P-B-LIFT-FUNDED-SHELL-TRANSFER-1/verify.py

with LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
and unchanged 600-second timeout. Capture genuine stdout/stderr separately,
UTC start/end, actual OS/architecture/Python, exit, bytes and SHA-256.
EXPECTED.txt is that first completed stdout. RUN.md records the exact pin
and command. Use the existing repository runner/checkers and require
x86_64/aarch64 PR replay before claiming a two-architecture audit. Same-author
proof and alternate implementation are self-review, not a distinct author.

## 6. Action layer and ownership

L1 only, conditional exact arithmetic/construction. Candidate-T proof and
candidate-C finite audit pending independent review; no Canon promotion.
The broader native/physical source, contact, energy and readout remain
UNSUPPLIED/OPEN, not a complete-class negative. This construction is a
scoped candidate input to #1589, which remains unclaimed here and is not
closed. No alteration of #1583/#1585 or their pending independent reviews.
No merge, old-source edit, new registered obligation or change outside
this single new probe directory.
