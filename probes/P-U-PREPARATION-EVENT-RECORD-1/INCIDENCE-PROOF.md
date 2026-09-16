# Prepared source, causal incidence address and fresh record

**PROSPECTIVE / PROOF-FIRST / RESULT-EXPOSED / L1 ONLY.** Public claim lock:
issue #866, P-U-PREPARATION-EVENT-RECORD-1. This is a conditional mathematical
construction awaiting the pinned audit, not a physical realization certificate.
Public Canon v78 and the native state space and update U are unchanged.

The existing QDD formula was known when the channel construction below was
designed. No blind discovery, independent physical preselection certificate,
or derivation of a physical Born law is claimed. The source snapshot,
Cartesian incidence rule, ordered slot carrier, observation convention and
fresh record supply are explicit premises. The algorithm has no supplied
probability ratio and no reduced-probability-keyed carry bank; that fact does
not make these premises consequences of U.

## 1. Source capture and exact equalities

Let the native origin-zero head be h=(p1,p4,p1p,p4p,q,r) in F5^6. Before its
first U transition, the model observer captures

    v=(ell(p1),ell(p4),ell(p1p),ell(p4p)),
    ell(0),...,ell(4)=(0,1,2,-2,-1).

The captured vector is an immutable member of {-2,-1,0,1,2}^4. Capture is
an admitted preparation map. It is not late recovery of the original head
from a synchronized checkpoint, nor a native memory coordinate. The
native-information theorem in NATIVE-PROOF.md and the merger in the public
native-readback proof remain applicable when this additional input is absent.

The model support predicate is v!=0; zero is also admitted with the explicit
no-event disposition below. Source equality is literal ordered integer-vector
equality. In particular v and -v are distinct captured sources even though
their incidence outcome words agree. They can be distinguished by the signed
channel fields in the complete record. The auxiliary native q,r coordinates
are not input arguments to this incidence construction.

The observer transition retains v unchanged. This means its captured model
source is unchanged, not that the four moving native piston coordinates are
constant. Native U continues to update its own checkpoint independently.
Neither the selected label nor the observer buffer, record cell or archive
is fed back to U: feeds_U=false.

## 2. One fixed integer-channel map

Number the source coordinates 0,1,2,3. Fix, once and for all,

    Pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)),
    s=sum_i v_i,                       d_ij=v_i-v_j.

The 31 channels are one LOW channel of signed amplitude s and, for every
pair in that order, five distinct HIGH channels indexed by c=0,1,2,3,4,
each of signed amplitude d_ij. The five copies are distinct model channels,
not a weight normalization performed after observing an output.

For an integer amplitude a, the complete incidence fibre is the Cartesian
square of {0,...,|a|-1}; its members retain the common sign sign(a). The
empty amplitude has the empty fibre. This square-incidence assignment is
a declared model rule. Arithmetic proves its cardinality a^2; arithmetic
does not identify a physical detector that implements that rule.

Hence the occupied LOW and HIGH cardinalities are

    A(v)=s^2,
    B(v)=5*sum_{i<j}(v_i-v_j)^2.

Writing Q=sum_i v_i^2, expansion of the six differences gives

    sum_{i<j}(v_i-v_j)^2=4Q-s^2,
    D(v)=A(v)+B(v)=20Q-4s^2.                         (1)

Both A and B are nonnegative integers. D=0 implies s=0 and every difference
vanishes, so v=0; conversely v=0 gives D=0. Thus support is decided before
any ratio is formed. Also D<=20Q<=320. Equation (1) is an identity of
quadratic forms for every rational or real v, although this finite slot
construction has the explicitly bounded integer source domain above.

For comparison with the inherited QDD reading, and only for that comparison,

    m=Q-s^2/5,       wL=s^2/20,       wH=Q-s^2/4.

Consequently D=20m, A=20wL and B=20wH. For supported v,

    A/D=wL/m,                    B/D=wH/m.           (2)

Equation (2) is an exact agreement with the known QDD pair. It is not a
claim that the incidence rule was selected independently of that target.
No reduction of A/D and no lookup indexed by a reduced fraction is needed
to prepare, address or update the model.

## 3. Fixed 544-slot carrier, padded to 1024

Set M=1024. Every phase r in {0,...,1023} has one fixed slot interpretation.

* LOW slots have r=8a+b with a,b in {0,...,7}. The slot is occupied exactly
  when a<|s| and b<|s|. Its signed channel is s.
* HIGH slots have

      r=64+16*(5*j+c)+4*a+b,

  where j=0,...,5 indexes Pairs, c=0,...,4 and a,b=0,...,3. The slot is
  occupied exactly when a<|d_ij| and b<|d_ij| for that indexed pair.
  Its signed channel is d_ij, and its record retains j and c separately.
* Slots 544,...,1023 are permanently empty.

These ranges are disjoint and exhaustive. The bounds |s|<=8 and |d_ij|<=4
ensure that every incidence pair has exactly one slot and that no pair is
truncated. There are 64 LOW slots and 6*5*16=480 HIGH slots. The incidence
sign does not alter occupancy, but it remains part of an occupied slot's
complete record.

Define the single-valued label function e_v(r) to return LOW or HIGH for
an occupied slot of that channel, and SILENT for every empty slot. Exactly
one slot is inspected per invocation; it cannot yield simultaneous LOW and
HIGH. This is single-valued symbolic output, not an asserted physical
exclusive occurrence. Distinct slots with the same coarse label are not
identified in complete record equality.

## 4. Causal phase ownership and acquisition

The public P-U-FINITE-HISTORY-EVENT-1/CLOCK-PROOF.md proves a fixed function
R_k on the legal length L_k=5*2^(k-1) Thue-Morse words, for k>=1, which
recovers the endpoint's index modulo 2^k. It never receives that index as
an argument. Here k=10, M=1024 and L=2560. The length is a sufficient bound,
not a minimal-memory claim.

There are two explicitly related acquisition conventions:

1. A direct chronological bit window ending with theta_n gives
   r=R_10(window)=n mod M. Origin-zero bit capture first fills at n=L-1.
2. On the guaranteed synchronized native checkpoints n>=3,

       z_n=4-3*theta_(n-1) in F5.

   Read z=4 as bit zero and z=1 as bit one. A full window ending at native
   cut n gives theta_(n-L),...,theta_(n-1), so use

       r=(R_10(window)+1) mod M=n mod M.             (3)

   If acquisition begins at cut 3, the first full window ends at
   n=L+2=2562. Cuts before the complete synchronized window are warmup.
   Beginning the synchronized acquisition at cut 3 is a declared protocol
   convention, not an inference of absolute time from an unfilled window.

The native bridge (3) is a proved mathematical map from checkpoint history;
the verifier audits its bit conversion and endpoint shift on every frozen
generating context. The executable observer/record stream wrapper uses the
direct successive theta bits in convention 1, as frozen in PREREG.md. No
separate end-to-end operational z-history record wrapper is claimed. The
source snapshot was already captured before tick 1 in either case.

The buffer state is a chronological binary word of length at most L. Each
proper acquisition appends one actual successive bit and drops the oldest
bit if the length would exceed L. Before it fills the readout is
UNAVAILABLE, which is administrative and is neither SILENT nor a written
event. Full illegal words or nonbinary acquisitions return ERROR, with the
rejected input or bounded word retained as evidence, and do not emit an
event. Dropping or reordering source acquisitions is outside the asserted
native-stream theorem; it cannot be repaired by postselecting a legal-looking
subsequence. Legality has the inherited exact finite substitution-language
decision procedure, not an empirical frequency test.

Once a correct window is full, apply e_v to the recovered phase. The
interpretation uses the captured source, the current full word and the fixed
slot table; no rational occurrence parameter, future bit, per-context rank,
output history or absolute source counter is an input to the phase reader.
Retaining output records, as specified next, is a separate resource.

## 5. Fresh cells, complete transitions and append-only records

Let the record-cell alphabet be C={BLANK,LOW,HIGH}. Define permutations

    W_LOW=(BLANK LOW),       W_HIGH=(BLANK HIGH),
    W_SILENT=identity.

For each fixed label, W is a bijection and its own inverse on all of C.
The selected-label-controlled map (o,c)->(o,W_o(c)) is therefore reversible.
This algebraic statement does not make the entire acquisition protocol
reversible: sliding-buffer overwrite and source preparation are separate
operations, with no unmentioned inverse-erasure claim.

The fresh-cell protocol requires c=BLANK. An occupied input cell is a
protocol error, not permission to overwrite an old record. On LOW or HIGH
the step writes that label into its fresh cell, retains v, and appends one
complete record to the archive. On SILENT it returns the explicit NO_EVENT
disposition, leaves the offered blank cell blank, and appends no accepted
record. UNAVAILABLE and ERROR likewise append no accepted record and remain
distinct administrative outcomes. The all-zero source returns NO_EVENT at
every complete valid invocation, with no LOW/HIGH record and no defined
accepted ratio.

A complete accepted record contains the captured v before and after
(identically equal), recovered phase r, exact slot descriptor (LOW,a,b) or
(HIGH,i,j,c,a,b), where i,j are the corresponding pair coordinates, nonzero
channel sign, coarse label, input cell BLANK and output cell equal to the
label. The implementation codes cell symbols BLANK,LOW,HIGH as 0,1,2;
event code 0 denotes SILENT in its separately typed event position.
Literal equality of this full tuple is the
record equality. The full observer transition additionally retains its
actual pre/post chronological buffer and its pre/post archive, including
the explicit no-event or administrative disposition. Projective equality,
equal effects and equal coarse labels do not replace these equalities.

The pre-archive is a finite ordered tuple H. An accepted step returns
H concatenated with its one record; every other step returns H itself.
All old cells are fixed. Induction on steps proves that every earlier
archive is an exact prefix of every later one, that the j-th accepted
invocation writes precisely its j-th cell, and that passive rereading
neither invokes the transition nor appends another record. Output history
does not control the next source map, phase or slot choice.

The first-hit record is the first element of H when H is nonempty; before
then it is UNAVAILABLE (the implementation's None sentinel). Once present
it is retained by the prefix property.
No extra hidden sticky first-label register is required. This permanent
retention uses the admitted archive or retained first cell, and is not a
fixed finite-window function of the native checkpoint. It therefore does
not contradict the native finite-history no-write theorem.

Any retained-first-cell-only variant must keep that cell separate and stop
writing it; reading it repeatedly is not an event-counting experiment. The
frequency theorem below counts fresh accepted invocations, not passive
rereadings of one first-hit record. No reset of an occupied physical cell
is supplied. A fresh blank cell and an archived earlier run are different
objects from erasure or reset of the old apparatus.

The complete model post-state preserves the prepared vector and all old
records. There is no projection of v onto the selected channel, no removal
of an unselected amplitude, and no inferred Lueder or saturation map.
No energy or microscopic physical cost is assigned to these symbolic cells.
Identifying a native physical carrier for them is a further premise.

## 6. Exact counts for every fixed-source prefix

Hold v fixed and invoke once at every consecutive native cut after correct
history acquisition. Let O_L and O_H be its occupied slot sets, with sizes
A and B. They are disjoint and O=O_L union O_H has size D. Equation (3)
makes the output sequence exactly M-periodic, irrespective of how long a
window is needed to recognize its phase.

For any starting native cut t0 and any N>=0, write N=qM+t, 0<=t<M. Put

    T={t0,t0+1,...,t0+t-1} modulo M.

The residue set T contains t distinct slots, and the exact counts are

    C_LOW(N)=q*A+|O_L intersect T|,
    C_HIGH(N)=q*B+|O_H intersect T|,
    C_ACCEPTED(N)=q*D+|O intersect T|.               (4)

These formulas follow by partitioning N consecutive cuts into q complete
cycles and one remainder. They cover every N and every finite start,
not only aligned periods or a long numerical sample. The warmup discards
a fixed finite initial segment and therefore changes no limit.

It follows for each fixed source that the natural-cut densities are

    LOW: A/1024,       HIGH: B/1024,
    accepted: D/1024,  SILENT: 1-D/1024.

For v!=0, D>0 and C_ACCEPTED is positive for sufficiently large N. Dividing
(4) gives the accepted ratio limit A/D, which equals the inherited QDD
LOW reading by (2). No ratio is assigned to an empty accepted prefix.
For v=0 acceptance is identically empty and the limit ratio is UNDEFINED.

This proves a deterministic all-time counting identity and a limiting
accepted ratio. It does not assert Bernoulli independence, a probability
measure on trials, stochastic occurrence, or a physical rate. It also does
not make the sequence invariant under an arbitrary invocation schedule or
under source changes during the run.

## 7. Exact schedule and first-hit counterexamples

Take the supported vector v=(1,0,0,0). Then s=1; exactly three pair
differences, those involving coordinate 0, have absolute value 1. Therefore
A=1, B=15, D=16 and the continuous accepted LOW ratio is 1/16.

Its only occupied LOW slot is phase 0. Phase 64 is occupied HIGH: it is
pair (0,1), copy 0, row 0, column 0. Keep acquiring every native bit, so
the phase reader remains valid, but invoke the selected-slot observation
only at cuts congruent to 0 modulo 1024. Every such invocation is accepted
LOW. Invoking only at cuts congruent to 64 gives only accepted HIGH. Each
invocation schedule has positive natural-cut density 1/1024; acceptance
among its invocations is one. Thus the two accepted ratios are 1 and 0,
not 1/16. The continuous-cut hypothesis in (4) is essential.

Even with subsequent continuous observation, the first record depends on
the observation onset. With native acquisition already complete, begin at
cut 3072 (phase 0): the first accepted record is LOW immediately. Begin
instead at cut 3136 (phase 64): it is HIGH immediately. Both onsets are
beyond 2562 and both continuing runs satisfy the same limiting ratio 1/16.
With the origin-zero convention that begins invoking at the very first
full native window, cut 2562 has phase 514. All occupied HIGH slots for
this source lie between 64 and 288, so the first later occupied slot is
phase 0 at cut 3072, and the first record is LOW.

Consequently a count-frequency theorem for one fixed prepared source does
not specify the frequencies of first-hit records over fresh preparations.
Repeating the same complete deterministic preparation and onset repeats
the same first result. Any claimed trial law needs its own preparation,
onset/phase and persistent-versus-fresh convention. Choosing those inputs
to obtain 1/16 would be an additional selection rule, not a deduction from
the native clock or from the asymptotic count identity.

## 8. Public overlap and physical ownership

The public pointed decoder already reads a captured head and forms complete
Cartesian pair banks; its apparatus.py explicitly calls incidence and
atomic batch writing model choices. P-QDD-STABILIZER-APPARATUS-1 already
supplies exact coherent E/R analyzers and a signed reservoir/threshold
record protocol. Its E output retains both coherent components, and its
threshold protocol permits zero and multiple marks. P-QDD-FRESH-RECORD-
NOFEEDBACK-2 already supplies a reversible three-symbol fresh-record
extension at L4. None of those storage or squaring ideas is claimed anew.

The present positive composition supplies one fixed bounded source-to-slot
algorithm, the newly available causal native phase address, a single
symbol per occupied addressed slot, and its explicit fresh-cell transition
and first-hit semantics. It does not use the supplied-rational interface
of P-U-FINITE-HISTORY-EVENT-1 or the per-probability invocation-rank bank
of P-QDD-EVENT-CARRY-BANK-1. The already known scheduling boundary from
P-QDD-DETERMINISTIC-EVENT-SAMPLER-1 is exhibited concretely above.

The physical owner remains issue #539 and
notes/canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md. In particular that
contract requires separate carrier equalities, preparation and ready-state
selection, complete step and record field ownership, append/persist/reset
laws, and the relevant L4-to-L5 gate. Its forbidden dependency cycle
`normalized occurrence target -> transition rule -> same normalized target`
prevents promoting agreement (2) into a physical derivation. Our disclosed
knowledge of the target is not a passed preselection certificate.

notes/TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md and its JSON companion
retain ownership of their own realization/readout/post-state certificates.
This construction supplies none of their unissued physical identifiers and
does not replace or silently modify their reset disposition. Mathematical
symbol selection, storage of a number, and a physical completed event are
different claims. The conditional chain is fully specified here; deriving
its premises and its single-trial physical interpretation remains open.

No new scientific execution or import was used in preparing this proof.
Its exact identities, slot bijection, acquired-phase composition, fresh-cell
laws, prefix counts and counterexamples are prospective audit targets under
the complete public pin, not claims of a completed verification run.
