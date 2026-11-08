# Mathematical attack on the independent two-input reload contract

Status: NON-CANONICAL / L1. Symbolic review of PR #1871 at exact head
26731e2bd7f1394b4d274528525e6d78cbe6bbf9. Authority comparison:
mathorn1973/twist-j main 0c33e2b281e39127c269ef5dd7f5b529a62e9e65,
Public Canon v107. No Canon status or repository disposition is changed.

## Exposure and method

I read the target PREREG.md, CONTRACT.md, PROOF.md and SOURCE-MAP.md at the
stated head, and the actual current registry row for
RELATIVE-CONTACT-COMMON-APPARATUS-OPEN. There is no README among the target
probe files. I did not read either executable checker, the literal
WORD535.txt, EXPECTED.txt, RUN.md or RESULT.md. The PR body already discloses
the author's claimed success and hashes; this is a result-exposed independent
symbolic attack, not a result-blind discovery.

No scientific runtime or enumeration is a premise of this review. The
independently reconstructed program still has to be frozen and executed
under the review's own preregistration. In particular this document does
not announce that execution's result. Composition statements below refer
to the oriented block word declared in the contract. Agreement with the
actual frozen word file and the complete reached-state replay are separate
audit obligations.

## 1. Carrier and common preparation

The allocation is internally consistent:

| Region | Slots | Count |
|---|---|---:|
| Shared source, clock and read controls | 0..10 | 11 |
| First experiment's two record banks | 11..30 | 20 |
| Second experiment's two fresh record banks | 31..50 | 20 |
| Queued independently prepared input | 51..55 | 5 |
| Total | 0..55 | 56 |

Each experiment's input has three source coordinates and two clock
coordinates. Ten slots are allocated to the two inputs, and all variation
is confined to those slots. In fact slots 2 and 53 are zero throughout the
admitted family, so eight input coordinates actually vary. The 46 designated
auxiliary coordinates have one common initial value; 46 is this interface
partition's auxiliary count, not the maximal count of literally constant
coordinates. With Q as defined
in the contract, each source has account 8, each clock account 6, each
ten-slot bank account 30, and the six common control coordinates account
5+3=8. Therefore

    common auxiliaries: 4*30+8=128;
    complete preparation: 128+2*(8+6)=156.

The source sums are two each, both clocks and all banks sum to zero, and
the controls sum to u+w=2. The complete ring sum is six.

The 100 cases are the full Cartesian product of two ten-input families,
not a next input computed from the first output. The second cartridge is
supplied initially and delivered later; it is not an arbitrary external
arrival chosen after execution starts. This is an explicit scope restriction,
not a failure of a contract that admits precisely these prepared inputs.

## 2. Independent local algebra attack

The total contact has inverse C^4 on the whole integral pair carrier.
Enabled relative differences stay enabled and are multiplied by rho;
refused pairs stay fixed. Both contact and supplied SWAP preserve the
complete sum and Q. Contacts preserve every labelled residue under j->1;
SWAP transports those residues. No contact-only implementation of SWAP is
used in this argument.

The following checks attack the selective controls rather than assuming
that a high-level WRITE is automatically a permitted primitive.

### 2.1 Source marker and the two-control gate

Write w_e=1+rho^e and u_e=1-rho^e. On source phase zero, the first O=C(1,5)
acts on (2,0), producing source coordinate w and marker u. At other source
phases its source coordinate is a nonzero w_e modulo 2O, so it refuses and
the marker remains zero.

For g,c in {0,u} and h=w, the commutator

    E_c=A0 B_c A0^4 B_c^4

is identity except when g=c=u. In that case it maps

    (g,c,h)=(u,u,w) -> (u,0,2).

Indeed A0 first changes (u,w) to (u_2,w_2), so B_c refuses. A0^4 restores
(u,w), then B_c^4 changes (c,h)=(u,w) to (0,2). If g=0,c=u, B_c's temporary
change is undone by B_c^4 because A0 refuses at both helper values. The two
remaining input cases are immediate refusals or inverse cancellations.

Consequently O2=C(9,10), acting on h and fresh gate t=0, creates (h,t)=(w,u)
exactly when both the source marker and that bank's selector were u. In
all other cases it refuses at (w,0). This explicitly identifies the work
resource that supplies the sampling gate; no selector token is cloned.

### 2.2 The scan distinguishes an active gate from an occupied record

The raw first clock coordinate is rho^k*w. With t=u, C(3,10) is enabled
precisely at phase k=0, since u=w modulo two and rho has order five there.
At that phase it changes (w,u) to (b,u_2), with b=1+rho^2. At other phases
it refuses.

With t=0 the sampling contact refuses. Also every raw clock residue rho^k*w
is distinct from every memory-phase residue rho^r*b modulo two. One way to
see this is b=w^2 modulo two and w is not in the order-five group generated
by rho. If w were rho^t, then w^3=rho^4 would force t=3 modulo five.
But 1+rho=rho^3 together with the cyclotomic identity would imply
rho^2+rho^4=0, then rho^2=1, contradicting its order five. Thus both
clock-to-memory contacts in K_p
refuse on an ungated scan. Its memory-only fourth power and first power
cancel, even if the memory pair already has phase one.

For a gated phase-zero scan and a fresh selected pair, the local K_p input
is (clock,a_p,b_p)=(b,-b,b). Its first fourth power changes the first two
values to (rho^4*b,-rho^4*b). The next fourth power refuses; the following
clock contact restores (b,-b), and the last memory contact writes
(-rho*b,rho*b). The clock remains b. The inverse sampling contact restores
(w,u), and T then advances the raw clock phase.

Scanning p=0..4 visits phase zero exactly once and returns the clock to its
original phase. It writes precisely bank pair p=-k modulo five. At a
complete bank module the sampling gate and helper are undone, and E_c^{-1}
restores the borrowed selector value. The other bank's inactive module is
identity at its boundary, including on its already occupied phase-one pair.

An active overwrite of that same occupied pair would not satisfy the fresh
write formula. The contract never demands it: A and B are selected while
fresh, and the third event selects skip. Repeating the program on spent
banks is therefore not a legitimate test of the stated positive contract.

### 2.3 Selector and restoration

For helper w, the declared nine-contact D swaps a target token pair (u,0)
or (0,u) and restores w; it fixes (0,0). With helper w_2 it is identity
on all three pairs. Therefore the 23-contact V=A0 D A0^4 D is a controlled
token exchange: it exchanges its target pair when marker g=u and is the
identity when g=0, restoring g and the helper in both cases.

The two V blocks send selector A to B, B to skip, and skip to A on a source
event. The last O^4 returns source phase zero's temporary (w,u) pair to
(2,0). These local checks support precisely the five reached-state R facts
listed in the target proof. They do not assert arbitrary occupied-state
writing or a binary marker at every internal primitive boundary.

For the subsequent complete-state replay the R facts remain explicit
obligations about the actual oriented word and actual reachable states.
They must not be substituted for executing that word in the checker.

## 3. Stage composition and timing

Assuming those R facts for the actual read word, a macrostep beginning at
source/clock phases (a,r) reads phase a, then phase a-1 after F^{-1}.
It finishes at phases (a+1,r+1). For source input zero, the three events
within ten steps occur at (0,1,9); for input one at (0,8,9). They select A,
B, then skip. At the final event the selector was skip at the write modules
and returns to A only afterwards; there is no fourth event in this horizon.

Thus one stage writes (-r,-(r+Delta_s)) with Delta_0=1 and Delta_1=8,
ends at source Y_(s+10) and clock X_r, and restores the six controls.

The block lengths are consistent: E has 10 contacts, K has 10,
one scan position has 1+10+4+1=16, SCAN has 80, each W has 105,
R has 1+105+105+23+23+4=261, and

    |S|=261+8+261+2+2+1=535.

The R offsets in S are 1..261 and 270..530. Hence the first two onsets
and completions are (1,805)/(261,1065) for source zero and
(270,4281)/(530,4541) for source one. The contact gaps are 804 and 4011.
These are designated-read ordinal differences, not all changes of g and
not the free-clock gaps 1 and 8.

## 4. Literal reload and retention

The second embedding changes only memory addresses 11..30 to 31..50.
It shares the same eleven core addresses, with no second disconnected
read core. After ten first-stage steps, its fresh banks and queued input
are unchanged.

Pi consists of five explicit whole-coordinate swaps between slots i and
51+i, for i=0..4. It loads the queued input and parks the actual spent
source and clock. It touches no archive or control. Each swapped pair has
equal residues: all source phases have residues (0,2,0), and all clock
phases residues (2,3). Thus even the labelled residue vector is unchanged
on every admitted loading state.

The second stage has a ready shared core and fresh selected memory, so the
same stage implication applies independently. Its complete endpoint is

    (Y_(m+10),X_l,0,u,0,0,w,0,
     M[-k],M[-k-Delta_n],M[-l],M[-l-Delta_m],Y_(n+10),X_k).

Within either stage, retention is promised at complete R and S boundaries,
not at every primitive contact. Inactive scan macros can temporarily rotate
an occupied pair and restore it. After the first stage, its old archive
addresses are excluded from every swap and every second-stage contact.
They are then literally unchanged throughout every remaining primitive.
The parked old input is also outside every second-stage edge.

Core readiness and fresh-memory consumption are distinct. Four initially
fresh ten-slot banks are consumed, with no change to their account 30.
Their availability falls from four to zero. This is fully funded finite
renewal of the usable read interface, with old information parked and retained;
it is not regeneration of spent memory.

## 5. Reader, counts and inverse

Each valid bank M[p] is distinct from blank and from the other four labels.
For a stage's two labels (x,y), the difference x-y is Delta_s modulo five,
namely one for s=0 and three for s=1. The difference recovers s, and -x
recovers the initial clock phase. Thus the four present bank states alone
identify all 100 initial ordered input pairs. This requires no parked input,
counter, expected output or initial enumeration label. It recovers only the
two admitted gap alternatives; it is not an arbitrary interval decoder.

The counts follow from the complete fixed program:

| Quantity across 100 preparations | Derived count |
|---|---:|
| Complete S boundaries | 2000 |
| Complete R boundaries | 4000 |
| Loading boundaries | 100 |
| Designated events, including skips | 600 |
| Complete inverse restorations | 100 |
| Contacts, forward plus primitive inverse | 5350000 |
| SWAP applications, forward plus inverse | 1000 |

Per preparation there are 10700 forward contacts and five swaps; replacing
each contact in the reversed mixed word by C^4 gives 42800 inverse contacts
and five inverse swaps. The separate 18-contact nine-source-cycle fixture
is not part of those trajectory counts. Stage-two contact ordinals shift
by 5350, whereas whole-operation ordinals shift by 5355.

These are symbolic predictions to be checked, not a report that our checker
has passed. The exact inverse exists globally, but its actual implementation
must still restore all 56 coordinates in each new replay.

## 6. Mapping to the actual current common-apparatus owner

The current registry row RELATIVE-CONTACT-COMMON-APPARATUS-OPEN is at L1.
It asks for one specified carrier and common law combining preparation,
input-sensitive response, retained distinguishable recording and funded
renewal, for at least two inputs and a declared horizon. Its positive
condition is one complete same-carrier construction and proof meeting every
frozen field for all admitted inputs and occupied continuations.

The following is a field comparison, not a registry update:

| Owner field | Candidate #1871 supplies | Exact audit obligation |
|---|---|---|
| Compatible complete carrier | O^56, with every input, control, old bank and parked source | All 56 coordinates at checkpoints and inverse |
| Predeclared input family | I x I, 100 ordered independent prepared pairs | No omitted or correlated pair |
| Common law/controller | One P=S_A^10 Pi S_B^10 for every input | Same oriented edges and schedule on every trajectory |
| Common initial resources | The same 46 auxiliary coordinates, Q=128 | Literal preparation equality and full account156 |
| Admitted operation alphabet | Total integral contacts and five declared whole-slot swaps | Correct total counts, inverses and invariants |
| Loading interface | Two queued input systems initially supplied; fixed Pi after stage one | Park actual spent input; load actual independent queued input |
| Input-sensitive response | Source-dependent event gaps1/8 and clock-dependent bank labels | Exact R/step phases and onset/completion states |
| Output equality | Complete displayed endpoint and four literal one-hot phase banks | Full-state equality and reader on actual banks only |
| Retention window | R/S boundaries within a stage; every primitive after first-stage completion | Correct boundary retention and protected-address exclusion |
| Funded renewal | Restored shared read core, fresh second banks and retained first records | Actual occupied continuation on the shared carrier |
| Reuse horizon | Exactly two ten-step input experiments | Both stages, including the occupied first history |
| Final disposition | Four used banks, parked old input, current second input and all controls | No omitted spent source, bank or archive |
| Residue/capacity compatibility | Equal-residue loader swaps, constant complete accounts, explicit spent stock | No hidden residue transport, closed reset or uncounted exchange |

Prepared inputs, a finite horizon and the supplied permutation alphabet are
allowed by this L1 owner. Raw-input synthesis, indefinite regeneration,
contact-only SWAP compilation and measured physical time are not additional
conditions in its current row. Their absence cannot refute this candidate's
fit to that row. Conversely, satisfying this row would not prove any of
those stronger statements.

The occupied continuation here is the actual second stage, retaining the
first stage's reachable histories for all ten-by-ten ordered choices. The
first archives and parked input are structurally excluded from the second
stage; this retention fact even holds for arbitrary values in those excluded
slots. No unrestricted active overwrite of an arbitrary occupied selected
bank is part of the frozen family.

Subject to correct implementation of the declared read word and successful
complete evidence at the frozen scope, this is a direct positive candidate
for the current owner's finite same-carrier contract at horizon two. A
separate reviewed Canon fold is required to change the registry. The fact
that the row remains open before that fold is not itself an additional
mathematical shortfall in the candidate.

## 7. Remaining falsifiers and conclusion

The decisive potential counterexample is an admitted input pair whose
actual oriented primitive word fails a stated ready/occupied R transition,
retention window, full loading state, four-bank injection, invariant or
complete inverse. Another would be a hidden difference between the block
expansion and the frozen535-contact word, or an input-dependent program
choice. These are tests of the positive contract and cannot be replaced
by a test requiring a third experiment or a raw-input loader.

The target proof's sentence that exactly ten coordinates vary should be
read as an input-slot allocation statement: slots 2 and 53 stay zero, so
only eight actually vary. The explicit loading formula, 56-slot allocation,
46-slot auxiliary partition and all accounts are unaffected. This is a
wording correction, not a failed trajectory or missing resource.

This symbolic attack found no contradictory account, carrier allocation, reload
disposition, decoder ambiguity, event count or stage-composition equation.
It gives no runtime verdict. The independent full implementation attack must
still discharge the fixed-word and reached-state obligations.

What #1871 adds at its stated scope is an independently variable second
input passing through the same ready core while the first experiment's
records remain at their original addresses, on one fully counted carrier
and one complete mixed word. Fresh memory and both prepared inputs are
explicitly supplied. The present mathematical owner can ask exactly for
that finite composition; canonical acceptance remains a separate act.
