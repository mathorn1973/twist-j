# P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1

NON-CANONICAL / L1 / prospective composition check with disclosed exposure.
Owner: A. M. Thorn, common-apparatus continuation, 2026-11-03.
Public reservation: https://github.com/mathorn1973/twist-j/issues/1870.
Base: main 0c33e2b281e39127c269ef5dd7f5b529a62e9e65, ACTIVE Public Canon v107.

## 1. Question, action layer and prior exposure

Does one fully counted carrier and one fixed complete program perform two
independently selected arrival experiments through the same read core, load
the second input without external intervention, retain the first experiment's
records at their literal addresses, and admit an exact complete inverse?

This is one finite L1 computation claim. It addresses a stricter loading
interface than the ten-input single-experiment witness in PR #1857. Its
components, source code and source results have been read. The composition
and its analytical predictions have been designed before execution, but no
claim of blind discovery or independent-author reproduction is made.
PROVENANCE.md and SOURCE-MAP.md delimit the inherited material.

The complete scientific source set in this directory must be committed,
pushed and read back byte for byte before executing verify.py. Static source
inspection, hashing and AST parsing are permitted before the pin; importing
or executing the scientific module is not part of that static review. The
first actual result is appended separately as EXPECTED.txt, RUN.md and
RESULT.md. Never alter a frozen source or threshold to rescue an outcome.
A failed or incomplete execution retains its source and follows the existing
repository failure/abandoned-pin rules. No Canon or workflow change is made.

## 2. Equation and complete operation alphabet

Let O=Z[j], 1+j+j^2+j^3+j^4=0, rho=j^2. In the basis (1,j,j^2,j^3),

    Q(a)=(5*sum(ai^2)-(sum(ai))^2)/2.
    C(a,b)=(a,b) if a-b is not in 2O;
    C(a,b)=((a+b+rho*(a-b))/2,(a+b-rho*(a-b))/2) otherwise.

The second primitive is a literal whole-slot SWAP(i,j). Its inclusion is
explicit. This is the contact/permutation alphabet allowed by the declared
model, not a claimed contact-only compilation of that swap. Both primitives
are total bijections on the complete carrier. C inverse is C^4; SWAP is its
own inverse. Both preserve the full sum and account. Contacts preserve each
labelled residue modulo 1-j; swaps transport those residues. On this admitted
family the five swapped pairs have equal residues, which is separately checked.

Chronological operations act left to right. S_A is exactly the 535-contact
word WORD535.txt copied from PR #1857, SHA-256
ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b.
That file uses one-based addresses. Equations and code use zero-based slots.
S_B is the fixed relabelling i->i+20 for memory addresses 11<=i<=30,
with every other S_A address unchanged. Pi is the five swaps (i,51+i),
i=0,1,2,3,4 in that order. The one complete law is

    P = S_A^10 Pi S_B^10.

Every admitted input receives this identical full program, with no runtime
choice of edges, bank, word or length from an observed result. Stage labels
in the verifier are checkpoint bookkeeping for this frozen word, not an
unmodelled adaptive controller. The supplied schedule is not identified
with the Canon's native U or an intrinsic physical clock.

## 3. Carrier, data, preparation, loading and horizon

The carrier is O^56. The shared core is 0..10: five active input slots plus
marker, three selector slots, helper and sampling gate. First archive banks
occupy 11..30, fresh second banks 31..50, and the queued next input 51..55.
Let u=1-rho, w=1+rho, b=1+rho^2, F=C(0,1)C(1,2),
Y_n=F^n(0,2,0) with period nine, X_k=(rho^k*w,-rho^k*w).

Admit exactly (n,k,m,l) in {0,1} x Z/5 x {0,1} x Z/5, all 100 ordered
input pairs. Active input is (Y_n,X_k), queued input is (Y_m,X_l).
The remaining 46 slots have one identical preparation: marker/gate zero,
selector (u,0,0), helper w, and twenty fresh (-b,b) memory pairs.
All common auxiliaries have account 128; each five-slot input has account 14.
Every complete preparation has account 156 and total ring sum 6. The queued
input is part of the initial state, not an input-dependent auxiliary bank.
The full Cartesian product prevents correlation between the two choices.

Run exactly ten S_A steps, perform Pi once, then ten S_B steps. There is no
external loading or disposal. Pi parks the actual spent first input in
51..55 while loading the queued input into the same active input slots.
The core controls are already ready at this boundary; the second pair of
banks supplies fresh capacity. This is finite stock-funded readiness, not
regeneration of the four spent banks. No third experiment is promised.
The detailed full-state formulas are fixed in CONTRACT.md.

## 4. Predictions, exact outputs and timing

Each ten-step stage has three designated events, at ticks (0,1,9) for its
source phase zero and (0,8,9) for phase one. First and second events write
that stage's A and B bank; the third bypasses both. Define Delta_0=1,
Delta_1=8. The four final record labels must be

    (-k, -(k+Delta_n), -l, -(l+Delta_m)) modulo five.

A bank is the literal ten-slot one-hot phase code defined in CONTRACT.md;
a present zero label is distinct from a blank bank. The reader must parse
the actual final bank coordinates and recover (n,k,m,l) without consulting
the initial labels or parked input. All 100 four-record outputs must be
distinct. Full endpoints include every input, control, helper and archive.

During each stage, acquired records are retained at every subsequent full
read and step checkpoint. First-stage archives are then literally untouched
by every loading swap and every second-stage primitive. Second banks and the
queued input remain unchanged through stage one; the parked old input stays
unchanged through stage two. Inverse execution deliberately removes records
and is not called retention-preserving renewal.

Each stage has 5350 contacts. The full forward word has 10700 contacts and
five swaps, hence 10705 elementary operations. Its full inverse has 42800
contacts and five swaps. Second-stage onset/completion contact ordinals
add 5350 to the local values; elementary-operation ordinals add 5355. Within
either stage the first two onsets are (1,805) or (270,4281), and read
completions are (261,1065) or (530,4541). Gaps 804/4011 count contacts;
clock gaps 1/8 count free macro increments. Other internal marker changes
are not new events. No arbitrary interval measurement is inferred.

## 5. Accepted code, finite inventory and systematics

verify.py is self-contained standard-library Python 3, assertions enabled,
exact integer tuples only, no random search, floating point, external data,
network, scientific imports from other probes, or file writes. It reads only
the immutable word file beside itself and prints deterministic ASCII/UTF-8
JSON with a final newline. The fixed block expansion must equal that word
contact for contact, including orientation, before it is relabelled.

The formal inventory is exhaustive on all 100 preparations: 2000 complete
step boundaries, 4000 complete read endpoints, 100 complete loading boundaries,
600 designated events and 100 complete inverses. Trajectories perform exactly
5350000 contact applications and 1000 swaps across both directions. The
separate 18-contact source-orbit fixture is outside that trajectory count.
Both four-coefficient polynomial arithmetic and five-coefficient cyclic
arithmetic calculate each contact and must agree after every application.
Cached maps are immutable exact pair maps whose invariants were checked;
memoization does not replace trajectory traversal. Expected states derive
from closed checkpoint formulas, not a second run of the candidate program.

Check common preparation, all 56 coordinates at every complete checkpoint,
full-state account/sum/residues, fixed word, actual bank decoding and joint
injection, untouched regions, onset/completion timing and exact full inverse.
Report complete-state/checkpoint/operation-word fingerprints with their
serialization fixed by verify.py. Those new output fingerprints are not
known before execution and are not borrowed from #1857.

One recorded Linux run supplies the exact EXPECTED.txt. The unchanged public
runner has its existing 600-second verifier limit. A nonzero exit, timeout or
nonempty stderr is not a scientific pass. Required CI must replay the exact
same head, verifier hash and EXPECTED bytes on x86_64 and aarch64 with
Python 3.12; both architecture jobs and aggregate check must pass. Windows
or same-architecture checks alone do not discharge this gate.

## 6. Failure threshold and scope

Tolerance is zero. Any missing input, inconsistent common bank or word,
wrong contact/SWAP count, arithmetic disagreement, wrong complete checkpoint,
wrong loading disposition, changed protected archive or input, incorrect
record/event/timing, failed decoder injection, conservation/residue error or
failed inverse falsifies the corresponding frozen prediction. No case is
removed and no threshold or claimed scope is silently repaired afterward.
Reproduction requires exit 0, empty stderr and byte-identical stdout.

This is at most a NON-CANONICAL L1 candidate-C witness for one declared finite
common-apparatus contract. A pass is not an independent mathematical verdict,
registry closure or release. It does not supply raw-state preparation,
permutation compilation into contacts, arbitrary later external arrivals,
regeneration of spent banks, an optimal account/word, indefinite operation,
physical energy/time, native U, cross-layer occurrence or a Collatz theorem.
