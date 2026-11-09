# P-J-SIGN-REMOTE-HOLD-1: prospective exact apparatus audit

PUBLIC / NON-CANONICAL / L1. Reservation:
https://github.com/mathorn1973/twist-j/issues/1972.

Authoring session: sign-channel consolidation, 2026-11-09.
Basis: public main 629a9d4058501f938dc91a690c3eb59a914493d1,
ACTIVE Public Canon v110, content
c8197bcc807de1f62248463aec77f7ac7ab46f85.

This is a new probe. No sealed predecessor is resumed or modified. The
question is one complete apparatus from an unknown local sign through
paid encoding and transport to a remote finite retained record, including
the actual continuing occupied state and later returns.

## 1. Prior exposure and scientific scope

The complete analytical proposal was derived before this preregistration.
It includes the encoder, source transition table, data-return certificates,
the unclocked reader's later opposite-sign alias, and the counted clock
completion. Author-side collaborators examined these formulas. This is not
a blind discovery test, an independent review, or a search whose outcomes
were hidden from the authors.

The authors inspected predecessor proofs, code, saved results and custody
records. The funded primitive is inherited from
[P-J-PAIRED-FUNDED-CONTACT-1](https://github.com/mathorn1973/twist-j/blob/a3f39b61223eb976a57f3d76272053fa617fcc31/probes/P-J-PAIRED-FUNDED-CONTACT-1/PROOF.md).
The four-cell writer, binary conveyor and fixed-pair no-export theorem
are inherited from
[P-J-FUNDED-PAIR-NETWORK-1](https://github.com/mathorn1973/twist-j/blob/e671a759481588e29bdc4b869d42254f39113694/probes/P-J-FUNDED-PAIR-NETWORK-1/PROOF.md).
The six supplied network files were matched to that public result commit.
No import, simulation, scientific execution or numerical search of the new
apparatus has occurred before this freeze. Only text inspection, algebra,
source authoring and static parsing are permitted before public readback.

The supplied law, geometry, preparation and reader are candidate-D. The
conditional all-parameter proof is candidate-T pending independent
mathematical review. The prospective finite audit is candidate-C at its
explicit parameter ranges. Two architecture executions reproduce the same
frozen audit; they do not create independent proof authorship.

## 2. Six frozen fields

### Field 1: equation and claimed behavior

Use O=Z[j], 1+j+j^2+j^3+j^4=0,
rho=j^2, J=1+j^2, Jinv=-j-j^2, phi=-j^2-j^3,
g=J conjugate(J)=2-phi and W=Jrho.

For a raw array z, S=sum z_i, H=sum z_i conjugate(z_i),
E=Tr_{Q(j)/Q}(H)/2. For one cell c=(c0,c1,c2,c3),

    q(c)=(5 sum_i c_i^2-(sum_i c_i)^2)/2.

The total four-cell primitive B first requires even differences in both
marked pairs. On the admitted carrier, let c,d be the two centers and u,v
the two half-differences. Keep c,d fixed. If u!=0 and h(v)=g h(u), send
(u,v) to (Ju,Jinv v). If v!=0 and h(u)=g h(v), send it to (Jinv u,Jv).
Otherwise apply identity. Reject by identity when either parity gate fails.
The two nonzero branches are disjoint; every refusal and occupied state
belongs to the total map. PROOF.md restates and proves the full rule.

For integers d,h>=1 put

    L=2d+h+3, m=2L, P=2L+4, tau=d+2.

Prepare four source cells A_a=(2a,0,W,-W), a in {-1,+1}. Only the first
source coordinate depends on a. The data rail has m marked pair sites:
launch site0 is high=(J,-J), every other site is low=(1,-1). The clock
rail has 2P sites, also with one high at0 and all other sites low.

B0 acts on source order(0,1,2,3); B1 on order(1,2,3,0); I acts on
source payer cells(2,3) and data launch pair0. K0 applies B to adjacent
even-start site pairs of both disjoint rails, and K1 to adjacent odd-start
site pairs with periodic boundaries. A full tick is

    F=K1_joint K0_joint I B1 B0,

with the rightmost factor first. All five layers repeat unchanged.

The data receiver is the whole arc R_data=[2d,2d+2h+3].
Its reader requires canonical pairs and exactly two highs at s<t, with
2d<=s<=2d+2h-1. It returns VALUE(+1) for t-s=4, VALUE(-1) for t-s=2,
and BLANK otherwise. The clock receiver arc is
R_clock=[2tau,2(tau+h)-1]. ENABLE means that this arc contains canonical
pairs and exactly one high. The total reader returns the data tag only
when ENABLE, and BLANK otherwise. It reads only these two fixed local arcs;
the two arcs are co-located in the supplied apparatus layout.

The exact full-boundary prediction, including every later return, is

    R(F^n z_a)=VALUE(a) if tau<=n mod P<=tau+h-1,
    R(F^n z_a)=BLANK otherwise.

At the first four layer boundaries following a full boundary n, the same
prediction uses n; the fifth layer gives full boundary n+1. Thus the reader
has no intermediate hole within the h-tick hold interval. The statement
concerns declared discrete boundaries, not an unspecified physical
interpolation within a layer.

The complete data array returns after P ticks for a=+1 and after P/2 for
a=-1. The clock returns after P. Only these return certificates, not
minimal periods, are claimed. The entire apparatus inverse is

    F^-1=B0 B1 I K0_joint K1_joint.

All five layers preserve S,H,E on the full raw carrier. The declared
preparations have

    raw cell count=12L+20,
    H=12L+28-6phi, E=24L+50, S=2a.

The data receiver is at least 2d data-ring bonds from launch along either
ring route. The receiver is occupied regional delay memory with a counted
phase reference, not a stationary single-cell latch or a raw-zero pair.

### Field 2: code

The accepted source is verify.py in this probe directory, Python standard
library only. It contains the complete exact arithmetic and full gates;
there are no runtime imports from another probe or from mutable notes.
Integer/fraction equality has zero tolerance. No floating point,
randomness, network, subprocess, external dataset or scientific file output
is part of the verifier.

The prospective implementation compares the literal raw-cell update to a
separately derived symbolic source-state and binary-shift oracle, expanded
back into every raw coordinate at every layer. A further closed-form
return/shift oracle supplies the complete expected state at every full
boundary. The oracle must not obtain expected states
by invoking the literal gate under test. These implementations are authored
within one session, so their agreement is not independent authorship.

The complete scientific source set is PREREG.md, PROOF.md and verify.py.
No additional helper is authorized by this text unless explicitly added to
this source set before the public pin. Static parsing is permitted before
the pin; importing or executing the scientific code is not.

### Field 3: carrier and exact finite inventory

The theorem concerns the full integral carrier for inverse/conservation,
and the two declared preparations for the all-time readable-history
statement. The finite audit does not exhaust either infinite carrier.

The main grid uses d=1,...,8, then h=1,...,8, then a=+1,-1 in that order.
For every preparation, follow exactly 3P full ticks from n=0 and inspect
all five layers. Compare the literal complete raw state to the independent
symbolic oracle, account and reader prediction at every boundary.
This gives 128 preparations, 14208 full updates, 14336 full boundaries
including each initial state, and 71040 layer updates.

Require the literal full inverse to restore each preceding full state.
Check full returns at P,2P,3P and explicitly the first negative-data return
at P/2. The complete full-state oracle also checks all subsequent P/2
multiples. Check the known three-tick encoder and complete data-return event
tables without discarding the returning occupied source/interface states.

The exact small-control and negative-control inventories are specified
below before the source pin. Their counts are separate from the main grid
and may include overlapping states.

### Field 4: systematics and controls

Compare full H in O, positive E and S separately. All payer, background,
clock and receiver cells are counted before taking a trace. Compare the
two initial arrays directly: all coordinates except the single source
coordinate must coincide, and complete H/E must agree.

The actual reader may inspect only the two declared receiver arcs. Its
implementation must not access a, a tick number, full source, payer,
launch or an oracle label. Freeze the canonical-pair, anchor, gap and clock
masks before execution. BLANK is a tagged value, not numeric zero.

A separate five-term cyclic arithmetic implementation audits the 6561
small raw four-cell cases against the four-coefficient implementation. The
large apparatus audit uses cached exact four-coefficient gates; its two
state oracles are logically separate from those gate calls. All paths are
written within this authoring session.

Keep the positive input's unclocked false-passage control. At positive
ticks L+d+4 through L+d+h+3 the ungated data reader must report -1, while
the final clock-qualified reader must report BLANK. The full positive
data rail at L+5 equals the negative data rail at3, despite the different
source sign. Compare the complete raw rail, not only its decoded tag.
This establishes the intended control, not failure of the final apparatus.

All other controls must retain literal refusal, occupied and invalid-code
states; a successful intended trajectory alone cannot establish a total
map or a total reader.

### Field 5: failure threshold, freeze and disposition

Tolerance is zero. Any unexpected raw coordinate, state count, branch,
account, inverse, period return, tag, early reading, wrong sign, hold length,
expiry, boundary stability or negative-control outcome defeats the affected
claim. No finite failure is converted into an all-carrier no-go theorem.

Before the first scientific execution, publish the entire accepted source
set, record its immutable commit and file hashes, and fetch/read back all
exact bytes. Require a clean checkout and assertions enabled. The first scientific run
has a 600-second process budget; exceeding it is not a pass. Record the
first exact stdout, exit code, stderr bytes/hash and neutral platform
metadata. Preserve nonzero exits, timeouts, missing cases and failed
controls under the repository's unchanged disposition procedure.
No source, inventory, reader, parameter range or threshold may be changed
after inspecting the result.

After the first completed run, append EXPECTED.txt, RUN.md and RESULT.md
without changing frozen sources. Required x86_64 and aarch64 jobs must use
the identical accepted verifier and expected bytes. Record actual receipts
only after they exist. A same-architecture repetition is not the second
architecture, and neither architecture is independent mathematical review.

### Field 6: action layer and exclusions

L1 only. B, the graph, five-layer order, common initial stock and semantic
reader remain supplied ingredients. No native-rho compilation, native-U
realization, physical detector, measured energy, proper time, gravity,
radiation, Born occurrence, resource optimality or stationary point-memory
claim is tested. Later correct windows recur with the original sign and
are not new independent messages. Canon, registry, workflows, existing
scientific owners and sealed predecessor sources remain unchanged.

## 3. Exact supplementary inventory

1. **Total B controls.** Enumerate all 6561 ordered raw four-cell tuples
   from the alphabet [0,1,-1,j,-j,J,-J,Jinv,-Jinv], with the rightmost slot
   changing fastest. Compare the complete output in four-coefficient and
   five-term cyclic arithmetic; check the full involution, both pair sums,
   S,H,E, and record the forward, reverse, parity and balance-refusal
   branch counts; the zero-relative case is included in balance refusals.
   These are overlapping property checks on the same 6561
   cases, not a full-carrier exhaustion.
2. **Complete continuing trajectories.** For the 128 main preparations,
   execute 14208 complete ticks and 71040 literal layer updates, inspecting
   the initial 128 boundaries as well. There are 71168 account/state/tag
   checks at initial or layer boundaries and 14336 complete full boundaries.
   At each layer compare every raw coordinate with the separately derived
   source-label and occupation-shift oracle. At every full boundary also
   compare with the independent closed-form return/shift oracle.
3. **Literal inverses.** Apply the same literal involutive layer to each
   just-produced layer state and require exact recovery of its preceding
   state: 71040 layer-inverse checks. From each produced full-tick state
   apply the five inverse layers in their literal reverse order and require
   the preceding full state: 14208 complete inverse checks. These auxiliary
   checks do not replace or alter the continuing forward trajectory.
4. **Exact recurrence event tables.** For every (d,h), check the eleven
   positive events at n=0,1,2,3,L+1,L+2,L+3,L+4,L+5,2L+3,2L+4 and the
   six negative events at n=0,1,2,3,L+1,L+2 against the source labels and
   complete rail configurations in PROOF.md. This gives 1088 event checks,
   all within the first positive common period. The separate full-state
   oracle also checks all subsequent periods.
5. **Ungated-reader failure and full-rail alias.** For each (d,h) and
   j=0,...,h-1, compare the complete positive data rail at L+d+4+j with
   the complete negative data rail at d+2+j. They must be identical.
   The ungated positive data reader must return VALUE(-1); the qualified
   positive reader must be BLANK. There are 288 such paired first-period
   points. This control preserves the exhibited defect of the unclocked
   design and the need for an additional distinction at this scope.
6. **Remove the common launch high.** For all 128 main initial inputs,
   replace only data launch site0 by low and leave the clock and other
   preparation unchanged. Continue the literal full law through ticks
   1,...,tau+h, including the intended expiry: 1408 control ticks in total.
   At every such full boundary require S=2a, E=24L+48 and full Hermitian
   account H=12L+26-4phi, whose four-coefficient form is
   (12L+26,0,4,4). Require all data pairs to remain canonical with at most
   one high, and the qualified reader to remain BLANK throughout. In
   particular all 576 boundaries in the originally promised hold windows
   must be BLANK. At tick3 check the exact source D_a and one high at data
   site2 for positive input or site4 for negative input: 128 encoder checks.
   These controls demonstrate loss of the actual two-pulse readable record
   when the declared common launch stock is removed. They do not prove
   failure of every other possible preparation.
7. **Direct fixed-pair graft.** Inspect the two payer pairs from the
   isolated writer outputs T4(A_+) and T4(A_-). They are (W,0) and
   (rho,-rho), respectively, and neither is a canonical low/high rail pair.
   Pair each payer with a canonical low=(1,-1) site and apply B. The
   positive payer has odd difference, so its output is unchanged by parity
   refusal. The negative payer and low site have equal relative Hermitian
   accounts, so their output is unchanged by balance refusal. Audit these
   two controls without relabelling either output as a canonical outgoing
   message. No universal impossibility result about changing-pair encoders
   is inferred.
8. **Frozen-reader perturbations.** On the 128 intended first-arrival
   states, change only the data anchor mask by shifting it one site
   forward: the perturbed reader must return BLANK. On the same 128
   states, instead interchange the two gap-to-sign assignments: the
   perturbed reader must return the opposite sign. The accepted reader
   remains unchanged. These controls are not post-result decoder tuning.

9. **Invalid observed code states.** On each of the 128 first-arrival
   states, replace the guaranteed low data pair at receiver site r+1 by
   (0,0), keeping both data highs and the clock marker unchanged. The
   final reader must return BLANK. Separately start again from each same
   unmodified first-arrival state and replace the guaranteed low clock pair
   at site 2tau+1 by (0,0), keeping the clock marker and complete data word
   unchanged. The final reader must again return BLANK. These are 128
   invalid-data and 128 invalid-clock reader cases. They audit the total
   reader's out-of-code rejection, not conservation or reachability of the
   mutated states; no evolution is asserted for these reader-only controls.
All loop order, report fields and compact JSON hashing conventions are
part of the accepted verify.py bytes. The verifier prints one sorted-key
compact JSON report with one LF, including counters and deterministic
SHA-256 digests of its exact state streams. No specific digest is asserted
before execution. Counts above are prospective consequences of the frozen
loops, not claimed observations.

The hypotheses are fixed independently of the outcome of this new exact
audit. A negative control failing to display its predicted mismatch is
itself a failed assertion. The first run and any failure disposition are
retained; there is no hidden search-and-retry stage.
