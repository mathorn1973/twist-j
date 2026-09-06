# What the added preparation, incidence and storage assumptions establish

**NON-CANONICAL / retrospective scope audit / no new formal execution.**
Owner: A. M. Thorn. Date: 2026-09-06.
Authority checked against public main
`17264b4a7c967b216c7dd165bbf69b269200e349`, ACTIVE Public Canon v78.
This note corrects the scope and layer presentation of the #866/#867
summary. It does not amend the sealed probe, promote a registry claim,
change a threshold, declare a passed gate or change Canon v78.

## 1. Falsifiers before conclusions

Throughout this note, unless explicitly decorated with a subscript 5 or 31,

```text
v=(v0,v1,v2,v3),   i in {0,1,2,3},
s=sum_i v_i,      Q=sum_i v_i^2,      Delta=5Q-s^2.
```

The executable source domain is `V={-2,-1,0,1,2}^4`, using the fixed lift
`ell=(0,1,2,-2,-1)` of the four F5 piston coordinates. All sums above are
ordinary integer sums, not sums modulo five. The 31 analyzer channels are
outputs of a map on this source, not additional source coordinates.

The immediate tests and their dispositions are:

| Assertion under audit | Exact falsifier or counterexample | Present disposition |
| --- | --- | --- |
| Under the fixed incidence rule, an integer-zero-sum captured source never emits LOW | Any valid address with `s=0` and output LOW | No such output in the sealed finite domain; algebraically all LOW slots are empty. This is an explicit falsifier of the constructor. |
| Fixed incidence has `A=s^2`, `B=5 sum_(i<j)(vi-vj)^2`, `D=A+B=4 Delta` | Any count mismatch for an admitted source; any nonzero source with D=0 | Sealed finite audit passes; Section 3 gives the independent algebraic proof. |
| Whole-cycle LOW/accepted counts L,N satisfy `4 L Delta=N s^2` | A mismatch on a complete 1024-address cycle or concatenation of complete cycles | Follows from L=kA,N=kD. This is NOT an exact arbitrary-prefix identity. |
| The same identity holds at every prefix | Source v=1000, first address 0: L=N=1, Delta=4, so 16 is not 1 | This stronger statement is false. It was not the sealed theorem; the sealed theorem includes remainder terms. |
| Four-coordinate common shifts leave the read ratio unchanged | v=1000 to v=2111: LOW changes from 1/16 to 5/8 | Shift invariance is false even for this pair inside V. It was not assumed by the fixed construction. |
| The apparatus-only history can recover original QDD for every preparation | Equal admitted histories with different required QDD values | The sealed 1000/2400 witness has LOW 1/16 versus 1/96; Section 5 states the separately proved universal history factor. |
| A fixed-source long-run ratio fixes the first record of every fresh preparation | Same source v=1000, onsets 3072 and 3136: first LOW versus first HIGH, both subsequent ratios 1/16 | The implication is false. First-record selection and trial-law adoption remain separate obligations. |

The support distinction matters: `s=0,v!=0` gives HIGH events but no LOW;
`v=0` gives no accepted event and no defined accepted ratio. The sealed
output reports 84 supported sources with LOW value zero. Together with
the zero source, these are 85 integer-zero-sum sources by `A=s^2`.
This is readback of existing data plus the identity, not a new enumeration.
Neither `kappa=sum(p) mod 5=0` nor the zero sum of a centered five-vector
can replace the hypothesis `s=0`.

## 2. Separate proposed claim rows

The labels below are candidates in this NON-CANONICAL note, not public
registry statuses. Conditional resources belong in each scope row.
There is no single `T` label covering the implementation, physical apparatus,
stream interpretation and first-outcome law together.

| Claim | Candidate status | Exact scope and evidence | Falsifier |
| --- | --- | --- | --- |
| Finite implementation agreement | candidate-C | The one fixed 31-channel/1024-address algorithm on the 624 nonzero members of V, plus a separate zero-source disposition, PROVIDED the original balanced source is captured and retained, Cartesian incidence and the fixed address order are available, native bits are acquired in order and observation is on consecutive ticks; fresh cells/archive are additionally required for persistence. Sealed EXPECTED verifies all 640000 source/address pairs and 14 finite record streams; it does not test all integer sources or all record streams. | Any admitted source/address mismatch, wrong zero disposition, or failure in a frozen record case. |
| Quadratic identities and positivity | candidate-T from algebra | For every v in R^4, `sum_(i<j)(vi-vj)^2=4Q-s^2` and `Delta>=Q`; for every v in Z^4, the symbolic complete Cartesian fibres have A=s^2,B=5 sum differences squared,D=4Delta. The fixed 544-slot embedding is claimed only on V. Proof: Section 3 and sealed INCIDENCE-PROOF section 2. | An algebraic counterexample in the stated dimension; a truncated slot embedding inside V. |
| Zero-sum exclusion | candidate-T from algebra; finite audit candidate-C | For every integer four-vector with s=0, the declared complete LOW incidence fibre is empty; in the executable protocol the source must also lie in V. No valid addressed LOW event is possible, for any invocation calendar. | Any LOW event for such a valid captured source/address. |
| Exact witness comparison | candidate-C as a finite audited result | Balanced sources 1000 and (2,-1,0,0), with the same integer s=1 and Q=1 versus 5, have the displayed weights and agree on the frozen native quotient checks. The universal time statement is in the next row, not inferred from a sample. | A wrong weight, source sum, quotient identity or finite comparison. |
| Complete apparatus-history obstruction | candidate-T from commuting identities and induction | All 625 piston preparations, any fixed common ready in F5^2, every common binary driver, all codomains Y and all functions F from the resulting entire `(q,r)` history into Y; no extra source-dependent input or feedback. Equal kappa gives equal histories and equal F values. For fixed-origin TM, the stronger five/four-class criterion is exactly that of NATIVE-PROOF sections 3 and 5. | Failure of the commuting identity, equal-kappa histories that diverge under a common driver, or failure of the stated complete TM class criterion. |
| Fixed-source periodic-word count lemma | candidate-T for the mathematical lemma; L5 realization gate OPEN | Conditional source/slot/clock hypotheses above, every fixed v in V and every consecutive-tick prefix after valid warmup, with the exact remainder formulas in INCIDENCE-PROOF section 6. Interpreting this as an apparatus EventRecord stream and its long-run frequency is an L5 target, not an earned consequence of the blanket L1 tag. | A wrong periodic-word count or limit under the frozen hypotheses; a claimed apparatus realization without the separately resolved stream gate is outside the earned result. |
| Fresh symbolic archive persistence | candidate-T from induction; finite implementation audit candidate-C | Given the admitted source, selected symbol, fresh BLANK cells and archive, the controlled cell swap and tuple append preserve each prior record. This does not derive physical storage, erasure/reset, source capture or post-measurement dynamics. | A changed old record, a nonblank accepted fresh-cell input, duplicate append on passive reread, or failure of the controlled permutation. |

The 624-case result alone establishes no theorem for all integer vectors.
Conversely, the universal history obstruction is not merely H: the exact
quantifiers and induction are already present in the frozen proof.

## 3. Index set, algebra and the scope of count identities

For exactly four coordinates, expansion gives

```text
sum_(i<j)(vi-vj)^2
 = 3 sum_i vi^2 - 2 sum_(i<j) vi vj
 = 4Q-s^2.
```

Hence the separately declared complete-square incidence rule gives

```text
A=s^2,  B=5(4Q-s^2),  D=A+B=20Q-4s^2=4Delta.
```

These polynomial equalities hold on R^4. Their interpretation as
cardinalities uses integer v and the declared Cartesian rule. Cauchy--Schwarz
in dimension four gives `s^2<=4Q`, so `Delta>=Q>0` for every nonzero v.
Only v=0 has Delta=0. A nonzero constant four-vector is supported; its
Delta is `4c^2`, not zero. The Gram matrix is `I4-(1/5)11^T`, which is
positive definite. The five-dimensional matrix `I5-(1/5)11^T` is a
different, singular projection.

The 31-channel output is not a legal substitution for v in this formula.
Already on v=1000 it contains 16 unit amplitudes and 15 zeros. Substituting
that list would give `s31=Q31=16` and `5Q31-s31^2=-176`. This is an exact
counterexample to the dimension-confused interpretation, not a failure of
the frozen four-coordinate construction.

For k complete clock periods the LOW and accepted counts are
`L=kA,N=kD`, so `4 L Delta=N s^2`. For an arbitrary prefix there are the
explicit occupied-residue remainder terms of the sealed proof; deleting
them gives the false first-address statement in Section 1. Dividing and
taking the limit is justified by bounded remainders and D>0, not by the
finite list of 624 preparations. The universal integer polynomial identity
does not extend the fixed slot capacities beyond V.

## 4. Common shifts, reference choice and the balanced lift

For the actual four-coordinate shift v'=v+c1_4,

```text
s'=s+4c,  Q'=Q+2cs+4c^2,  Delta'=Delta+2cs+4c^2.
```

All pair differences and therefore B are unchanged; A usually changes.
The within-domain hand example v=1000 to v=2111 gives
`(A,B,D)=(1,15,16)` to `(25,15,40)`. Thus this apparatus distinguishes
addition of a common background to its four coordinates. V is not globally
closed under any nonzero integer translation. The F5 operation followed
by rebalancing is a different operation: for example p=2000 to p=3111
changes the balanced vector from (2,0,0,0) to (-2,1,1,1), not to (3,1,1,1).

The correct five-coordinate reformulation makes the reference explicit.
For w in R^5 choose distinguished index 4 and put `vi=wi-w4` for i=0,...,3.
With `S=sum(w), Q5=sum(wi^2)`, direct expansion gives

```text
s=S-5w4,  Q=Q5-2w4*S+5w4^2,
Delta=5Q5-S^2,
LOW=(S-5w4)^2 / [4(5Q5-S^2)].
```

Both numerator and denominator in this correctly referenced expression
are invariant under w to w+c1_5. Constant w corresponds to v=0 and
ZERO_SUPPORT. On the chart w4=0 it reduces to the frozen four-vector
formula. The expression with numerator S^2 and unrestricted five-vectors
omits the reference term and is not this QDD reading. This reformulation
does not enlarge the executable domain: the four differences must lie in V.

There is nevertheless a real, declared lift choice. The same field source
p=1400 has balanced lift (1,-1,0,0), with LOW=0. Substituting its least
nonnegative representatives (1,4,0,0) instead gives the rational expression
5/48. This second vector is outside the frozen source contract. The formula
does not descend through arbitrary coordinatewise integer-lift changes.
The balanced lift, distinguished reference and analyzer are adopted
dictionary/design choices; no independent physical selection was proved.

## 5. The orbit-functional fork needs its observation domain

To avoid overloading Q, write the native quotient as
`pi(x)=(z,q,r)` and the apparatus history as `H_(a,b)(p)`, where a is the
common ready and b is the common driver. The frozen generator table proves

```text
pi(U_b(x)) = T_b(pi(x))   for every x in F5^6 and b in {0,1}.
```

Induction gives `H_(a,b)(p)=H_(a,b)(p')` whenever their field sums kappa
agree. Therefore the actual universal statement is

```text
for every a, every common infinite driver b, every p,p' with equal kappa,
every set Y and every F: image(H_(a,b)) -> Y,
F(H_(a,b)(p)) = F(H_(a,b)(p')).
```

No continuity, linearity, finite-memory or causality restriction is needed
for this extensional statement. The causal processor version additionally
allows arbitrary memory spaces, fixed update/output functions, common
source-independent initial memory and common time/context inputs. Equal
states and inputs give equal next states and outputs by induction. It
excludes additional source information and interventions. A random device
would require its own typed inputs; common independent randomness cannot
be silently treated as a source-specific information channel.

For the witness v=1000 versus (2,-1,0,0), s=1 in both and Q=1 versus 5.
Thus Q is precisely a missing datum for this pair, and no apparatus-only
history functional recovers it. The phase is not the missing distinction.
In the conditional incidence construction, source capture is an additional
assumption at this scope, not a promised consequence of better phase recovery.

The same conclusion does not apply to every meaning of 'U-orbit':

| Input to a proposed functional | Exact decision |
| --- | --- |
| Complete apparatus-only history, common ready | Negative for universal original Q or QDD recovery, by the quantified factor theorem and the same-s witness. |
| Full pointed U-orbit retaining x0 | Positive: evaluate Q or QDD directly on its first four head coordinates using the fixed lift. Existence of this mathematical map does not implement physical capture. |
| Indexed full checkpoint at a specified time, restricted to the same-kappa witness pair | The two full states stay distinct because they select the same bijections. Pair separation is possible, unlike apparatus-only separation. |
| Entire full-state tail after the original head is discarded, on the full preparation domain | Original QDD need not factor through it because conflicting full-head mergers exist, including the common-ready example below. |

An additional hand-derived check, not a new preregistered computational
case, uses common ready (q,r)=(3,0):

```text
x=(2,0,0,0,3,0),  z(x)=0,  a(x)=(0,2,0,0,3,0),
y=(2,1,2,4,3,0),  z(y)=2,  c(y)=(0,2,0,0,3,0).
```

At the initial TM bit zero these are their actual selected generators.
The balanced sources have (s,Q)=(2,4) and (4,10), hence LOW=1/16 and
2/17. Their entire indexed full-state tails from tick one agree. This
explicit algebraic counterexample excludes universal original-QDD recovery
from that tail even with the same apparatus ready. It does not exclude
full pointed-orbit reading or every alternative apparatus/observation split.

Finally, a quadratic quantity's absence from a linear span excludes only
that linear reader class. All real-valued functions of the observable
history form the algebra of real-valued functions constant on its fibres.
Nonlinear functions of the observable label are allowed. Here balanced s^2
and Q fail to descend to those fibres; their degree alone is not the proof.
For example p=1400 and p=1112 both have kappa=0 but balanced s^2=0 and 25.
Integer s must also be kept distinct from its field residue kappa.

## 6. The assumptions' roles, without comparing unlike denominators

The old 0/900 counts record-map/delay pairs: 180 record maps times five
delays, tested with particular finite windows, state conditioning and
post-object requirements. The new 624/624 counts supported source vectors
for one different conditional constructor. In particular the new archive
preserves the captured source; it does not implement the old post-state
instrument requirement. Subtracting these ratios does not quantify the
causal cost of three assumptions. No controlled premise-ablation experiment
was performed, and no minimality claim is earned.

The costs can instead be assigned to explicit operations:

| Admitted resource or convention | What it supplies | What it does not prove |
| --- | --- | --- |
| Balanced source capture and retention before tick one | s, Q and channel data that do not factor through the apparatus-only port | Native capture, its physical carrier, or its necessity among all alternative interfaces |
| Complete Cartesian squares, five copies per pair and the fixed slot order | Exactly A=s^2 and B=5(4Q-s^2); the known QDD ratio follows algebraically | Independent selection of the squared form, coefficients or physical analyzer |
| Ordered clock acquisition, phase reader and consecutive-tick calendar | Equal traversal of the 1024 slots and the fixed-source count limit | Arbitrary invocation-rank accuracy or a fresh-preparation first-outcome law |
| Fresh BLANK cells and an archive | Writing and preserving the selected records | The event ratio: e_v(r) and its counts are already defined without a persistent archive; physical reset or a closed native storage supply |

Thus the stated capture/incidence/clock assumptions suffice for this form
of frequency; storage supplies persistence. They were designed with the
QDD target known. The old 0/900 negative result remains intact, and the
new finite agreement is not its conversion into 624 successful instruments.
The chosen slot order fixes timing and first-hit behavior; the occupied
cardinalities and full-cycle ratio are unchanged by a permutation of all
slots when every slot is still visited once per cycle.

## 7. Layer correction and separately named open targets

The single `L1 ONLY` banner on the sealed package is too broad if read as
a typing declaration for its apparatus streams and frequency claims.
Finite-state commuting identities and arithmetic remain L1 results. This
corrective presentation places ordered EventRecords, counts, frequencies
and normalized rational count fields at the proposed L5 target. This agrees
with the existing apparatus-contract proposal, which is itself explicitly
NON-CANONICAL / STOP-DEFINITION and has no scientific authority. The
binding POLICY requires a separately named gate for cross-layer claims;
calling these count fields probability or measure would require a further
L5-to-L6 gate. No such promotion follows from the algebraic ratio.

The following are **proposed identifiers, OPEN and unregistered**. They
name review obligations under the existing QDD-INSTRUMENT-APPARATUS/O1
owner, not new owners or passed Canon gates:

| Proposed gate | Endpoints/type | Required decision |
| --- | --- | --- |
| GATE-L1-L5-PREPARATION-INCIDENCE-RECORD | L1 to L5, OPEN_LIFT | Resolve the actual source access, complete apparatus/record carrier and equality, physical context, phase selection, acquisition/calendar, zero/no-event dispositions, persistence/update/reset and realization map; prove its declared event stream is realized. The current conditional construction supplies no such closure. |
| GATE-L5-L5-PREPARATION-FIRST-RECORD | L5 to L5, OPEN_DECISION | Freeze complete fresh-trial preparation, onset/calendar, history equality, first-hit/empty handling and retention semantics, then decide the claimed deterministic first-record behavior. An asymptotic count ratio is not this decision. |
| GATE-L5-L6-PREPARATION-FIRST-OUTCOME-LAW | L5 to L6, OPEN_LIFT | Independently specify a trial/phase ensemble and normalized measure with zero/empty handling, then prove exactly the proposed first-outcome law. No ensemble or Born law is adopted here. |

Any later registration must also declare the correctly typed concrete child
obligation under that existing parent. In particular the L5-to-L5
OPEN_DECISION requires an L5 open owner: the parent's MULTI designation
cannot satisfy or evade that rule. This note creates no registry owner
or gate row.

A first-record query on an already admitted L5 history is not automatically
a different protocol layer; it is a different typed observable and may
require a same-layer decision. Exclusive physical event realization belongs
in the unresolved event-stream gate, and a probability law is a further L6
claim. The policy distinguishes OPEN_DECISION from OPEN_LIFT explicitly.
The generic log-projection gate does not authorize this enlarged source,
incidence or storage protocol by renaming it a log.

## 8. Evidence and audit boundary

All existing evidence is read from the stated public main, whose Canon
hash remains `82b29c75eb007c71d73dc33e63270d0e0895fdf41886499fcf79b928826855b5`
at 473631 bytes. Public main checks, tag/content ancestry and normative
hashes were verified before this audit.

- [Sealed #866 source and proofs](../probes/P-U-PREPARATION-EVENT-RECORD-1/PREREG.md):
  public pre-execution pin `19b69962ba0365d39546029a3f02dd7e05e38ba5`.
  [INCIDENCE-PROOF](../probes/P-U-PREPARATION-EVENT-RECORD-1/INCIDENCE-PROOF.md)
  sections 1--3 fix the four-coordinate carrier and prove the identities;
  sections 5--7 prove symbolic storage, exact prefix counts and onset controls.
- [NATIVE-PROOF](../probes/P-U-PREPARATION-EVENT-RECORD-1/NATIVE-PROOF.md)
  sections 2,5--8 contain the all-driver factor proof, explicit arbitrary
  function/processor quantifiers, witnesses and full-state nonmerger result.
- [EXPECTED](../probes/P-U-PREPARATION-EVENT-RECORD-1/EXPECTED.txt) is the
  unchanged 8352-byte result with SHA-256
  `5d56f69ce88fff71c433903cfa95305c2c5c7e51c1db16fb7064715f7338d7ef`.
  No verifier was executed or imported for this retrospective note.
- [Old finite U-induced result](../probes/P-QDD-INSTRUMENT-U-INDUCED-1/RESULT.md)
  and the current registry row QDD-U-INDUCED-FINITE-NONSELECTION fix what
  the 900 cases and their post-object predicates mean.
- [Original native readback proof](../probes/P-QDD-U-NATIVE-READBACK-1/PROOF.md)
  distinguishes the full pointed head from conflicting later fibres.
- [Proposed typed apparatus contract](canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md)
  is NON-CANONICAL / STOP-DEFINITION and proposes counts/frequencies in L5
  while excluding unapproved L6 interpretation. It supplies no scientific
  authority. Binding [POLICY](../POLICY.md) governs named layer gates.

New examples in this note were checked by direct displayed algebra and
independent static review. They are not relabelled as part of the earlier
preregistered case inventory. This correction leaves every pinned scientific
file and output intact and provides no new physical decoder closure.
