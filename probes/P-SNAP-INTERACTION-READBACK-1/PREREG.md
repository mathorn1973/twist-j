# P-SNAP-INTERACTION-READBACK-1 preregistration

**Do not execute before immutable commit, push and accepted-byte readback.**

Mode: PROOF-FIRST / RESULT-EXPOSED / NON-CANONICAL MATHEMATICS.
Owner: A. M. Thorn. Public lock: [#895](https://github.com/mathorn1973/twist-j/issues/895).
Base: `40f6d140db9e4cbe37848a8a653125a6415d9e8a`.
Authority: ACTIVE Public Canon v80, tag `canon-v80`, content commit
`b00171ef21ecb0d905593224f66f5e8a0f6c28e5`, Canon SHA-256
`8b076ee3d940e4a3639d3ffca06ae86e7df69dfc87f90d06ea99d4f9fca6b66c`,
541516 bytes. No accepted verifier has been executed or imported in preparation.

## 1. Equations and exact targets

The concrete question is whether a new equal-payload interaction and passive
rereading can be distinguished from an independently specified transition,
instead of being distinguished only by the caller's operation label.

1. **Existing zero-batch erasure boundary.** The admitted zero DEPOSIT in
   `P-QDD-STABILIZER-APPARATUS-1/RECORD-CONTRACT.md` appends a batch, whereas
   READ does not. Freeze the observation pi as the ordered incoming/receiver
   amplitudes before and after the port transition and their energies;
   represent READ by the identity on the same idle zero ports.
   It omits operation label, presence flag, call/pulse ordinal, new-slot
   address, archive shape/length and administrative history. At zero input,
   both observed tuples are all zero, while batch deltas are one and zero.
   Therefore that batch delta cannot factor through pi. This does not erase
   those fields from the existing full protocol or allege its inconsistency.
   Threshold marks have a different zero disposition.
2. **Every rational orthogonal two-port perfect loader.** Let V be a nonzero
   finite-dimensional rational space with positive Gram matrix G. Classify
   all linear T on V orthogonal-sum V that satisfy T(x,0)=(0,x) for all x:
   exactly `T=[[0,B],[I,0]]`, where `B^T G B=G`. Reuse gives
   T(0,x)=(Bx,0), so the same two-port map cannot also retain every old record
   passively. More generally an injective map cannot both load a distinct
   state into y and fix y. A changing cursor/controller/environment enlarges
   this exact complete-state contract.
3. **Protected old records and fresh loading.** On the finite-dimensional
   rational positive orthogonal sum H=S+O+F, require W to fix old records O
   pointwise and load W(s,o,0)=(0,o,Js). Such an orthogonal W exists exactly
   when J:S->F is a rational isometric embedding. With Gram adjoint J*,
   `W(s,o,f)=(J*f,o,Js+(I-JJ*)f)` is an explicit orthogonal involution.
   Necessarily dim F>=dim S; a Gram-isometric copy attains equality.
   Dimension alone is insufficient over Q: source form <1> and fresh form
   <2> admit no such embedding. Finite invariant record sectors cannot receive
   orthogonal transfer from their complements. Hypotheses concerning positive
   forms, finite dimension or pointwise protection are not silently dropped.
4. **A fixed recording update and its exact limit.** For each N>=1 use
   C={BLANK} disjoint-union Q^m, a head j in Z/N, and two length-N banks I,R.
   A single fixed update swaps I_j and R_j, then advances the head. It is
   bijective; its inverse retreats the head and swaps. It preserves total
   amplitude energy and occupancy, and its 2N-th power is identity.
   Starting at j=0 with R all BLANK, the first N transitions preserve earlier
   receiver entries. An emitter inspecting the active receiver transition
   BLANK->PRESENT(x) issues the tag (j,x); other transitions issue nothing.
   Two equal arrivals, including PRESENT(0), have different first-pass tags.
   Passive queries are stipulated state projections; repeated queries do not
   execute the update or emit new records. The recording update consumes no
   READ/DEPOSIT opcode, but its carrier explicitly supplies presence, routing,
   incoming packets and fresh receiver capacity.

At wraparound the same map removes old receiver content, and after 2N steps
the full bank state returns. It is not an indefinitely persistent recorder.
Arbitrarily large first passes are not one fixed finite realization. If BLANK
is identified with zero amplitude, absence and a zero-valued arrival again
coincide. A cold nonzero SWAP has positive receiver-energy gain, but a warm
SWAP of +1 and -1 changes signed values at zero net gain. Thus energy gain,
arrival batches, threshold marks and physical events are distinct contracts.

## 2. Accepted code and proof

`verify.py` is standalone Python >=3.10, using only the standard library and
exact integers/rationals. It reads no repository file or external data,
performs no network access or random sampling and emits one deterministic
JSON record. `PROOF.md` supplies the uniform arguments and inherited inputs.

A mathematical mismatch is retained as FALSIFIED with explicit failure data
and exit 0. An uncaught unexpected exception or unfinished process is
integrity STOP, not scientific falsification. Such an uncompleted public pin
is consumed under POLICY.md and cannot be repaired or reused. No accepted
code or threshold changes after pinning. Static inspection and AST syntax
parsing are permitted before execution; scientific dry runs and imports are not.

## 3. Frozen carriers and audit ranges

No experimental dataset is used. All finite fixtures are disclosed in the
accepted code and audited against the written equations:

- The all-zero DEPOSIT/READ port-transition collision and distinct batch
  counts. Cold zero/nonzero and warm equal-energy SWAP controls separate
  signed changes, incoming occupancy and energy-based emissions.
- Two-port loaders for all signed permutation matrices in dimensions 1..3,
  rotations with (cos,sin)=(3/5,4/5),(5/13,12/13),(8/17,15/17), and
  G=diag(1,4) conjugates of the eight signed two-dimensional permutations
  and these rotations. Verify exact positive orthogonality, all basis loads,
  reuse and the block classification.
  Independently exhaust every signed permutation on total port dimensions
  two and four, including nonloaders, to test the loader iff condition and
  invariant-record/no-transfer boundary on the whole finite families.
- Protected-old/fresh constructions with fixed small rational positive Gram
  matrices and explicit isometric embeddings, including matched copies,
  source <1> into <2,2> by (1/2,1/2), and a two-dimensional source into three
  fresh standard coordinates using the first two columns of
  `I-2vv^T/9`, v=(1,2,2). Each uses protected old dimension 0,1,2 with the
  corresponding prefix of Gram diagonal (3,5). Check the Gram adjoint,
  projection, loading, old-record preservation, rank and orthogonal involution
  identities. The rational search p/q, p=-12..12, q=1..12, for <1> into <2>
  only audits the all-rational parity proof; it is not that proof.
- For the packet alphabet {BLANK,PRESENT(0),PRESENT(1),PRESENT(-1)}, all
  preloaded input banks of lengths N=1..6 with blank receivers; inspect the
  entire first pass, old entries, emitted tags and passive queries, then
  the wrap/return behavior. Also exhaust all input/receiver bank pairs and
  head positions for N=1..3 to audit the total update and its inverse.

Every detailed rational fixture and loop bound belongs to the accepted source.
Finite coverage does not classify all rational orthogonal maps or prove an
unbounded occurrence or physical law; the block and embedding proofs do.

## 4. Systematics and prior exposure

Run on Linux or Linux-compatible WSL with LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. Record actual platform,
architecture and Python version; required CI uses Python 3.12. Require
deterministic UTF-8 stdout, empty stderr, exit 0 and a 600-second ceiling.

The proposed conclusions and discriminating controls are exposed before the
pin. No blind prediction or historical novelty of swaps, orthogonal linear
algebra or the fibre criterion is claimed. Existing fresh-record writers
and reservoir energy accounting are dependencies, not new discoveries here.

Relevant public inputs are the shared apparatus contract's record-field and
ordered-history clauses; `P-QDD-STABILIZER-APPARATUS-1/RECORD-CONTRACT.md`
for DEPOSIT, READ and the zero batch; `P-DECODER-RESERVOIR-COUPLING-1/PROOF.md`
for cold ports, retained signed tape and chosen threshold accounting;
`P-BINARY-RECORD-QUADRATIC-SELECTION-1/PROOF.md` for the existing symbolic
fresh writer; and `P-SNAP-OCCURRENCE-IDENTITY-1/PROOF.md` for the address/log
boundary. None supplies the new apparatus's physical preparation or routing.

The new core is the exact operation-erasure counterexample, complete two-port
loading classification and necessary/sufficient fresh-space criterion,
tested against a single specified state update and its finite-capacity failure.
The generic fibre test and existence of a fresh-cell writer are not rebranded
as new results. The source is transferred, not universally copied. Symbolic
presence tags have no derived physical energy or memory cost. No inference
from m rational amplitude dimensions to physical bits is made.

## 5. Threshold and disposition

Threshold: zero exact mathematical mismatches. Any violation of a frozen
classification, construction or negative control must be retained; no
retargeting after observation is permitted. A proof defect without an exact
negation leaves the affected statement unresolved. Integrity failures are
not falsifications of physics.

Complete proofs plus byte-identical x86_64/aarch64 reproduction support only
the declared NON-CANONICAL mathematical result. The attempted amplitude-only
replacement of the zero-batch contract is excluded; a chosen zero=NO_EVENT
contract is a different admissible question. The conditional bank is a
positive existence construction, not an accepted physical Snap mechanism.
Its failure after capacity reuse is an exact scope boundary, not a defect
to hide by changing the acquisition schedule after pinning.

## 6. Action layer and immutable procedure

Action layer: L1 mathematics of rational port maps and symbolic bank dynamics.
No native U implementation, L4 physical apparatus, admitted L5 event stream,
L6 probability, Born law, SI calibration or new physical event equality is
adopted. The physical definition and realization obligations stay with #539
and the existing decoder owners, at STOP-DEFINITION.

Publish PREREG.md, PROOF.md and verify.py at an immutable pin and read back
all three before the first formal execution. Append exact EXPECTED.txt,
RUN.md and RESULT.md without changing the accepted sources. Require both
architectures, audit public readback and merge without squash or rebase.
Only this new probe and its occurrence-note extension are in scope. Canon,
Registry, Frontier, gates, authority, release, workflows and older probes
remain unchanged; a later Canon fold is separate.
