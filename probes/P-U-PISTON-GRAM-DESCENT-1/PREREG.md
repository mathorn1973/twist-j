# P-U-PISTON-GRAM-DESCENT-1 preregistration

Status: PREREGISTERED / ANALYTICAL TARGETS EXPOSED / NO SCIENTIFIC RUN.
PUBLIC / L1. No Canon authority or status is created by this probe.
Owner: A. M. Thorn / ChatGPT-native-gram-20261107.
Reservation: issue #1949.
Branch: `probe/P-U-PISTON-GRAM-DESCENT-1`.
Base: `d4d363722f052141a4ce65e9da39f11a74b43b95`, Public Canon v109.
Content: `2b0f94ec1e0874bff9141259e0b7da80e6681ea6`.
Canon SHA-256: `035408ec79219cc72a7d3613cf1568154cca185137d2a2daa43b896aae0c6383`.
Canon bytes: 1464066. Declared tag: `canon-v109`.

## 1. Equation, domain and equality

Use the unchanged native checkpoint carrier S=F5^6, ordered as
`x=(p1,p4,p1p,p4p,q,r)`, and the full autonomous carrier N0 x S.
All checkpoint arithmetic is modulo five. The native counter is retained
literally, not replaced by a finite autonomous parity clock.

```
a(x)=(p4,p1,p4p,p1p,q,r)
b(x)=(-p1p,-p4p,-p1,-p4,-q,-r)
c(x)=(2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r)
d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r)
e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r)
T_t(x)=g_(sum(x)+2t mod5)(x), (g0,g1,g2,g3,g4)=(a,b,c,d,e)
U(n,x)=(n+1,T_theta_n(x)), theta_n=popcount(n) mod2.
```

Use exactly the existing DEF-PISTON-2X2-RESHAPE and balanced lift
`ell(0,1,2,3,4)=(0,1,2,-2,-1)`. For `v=(a,b,c,d)=ell(p)`, define

```
X=((a,b),(c,d))
A=a*a+b*b, B=a*c+b*d, C=c*c+d*d, D=a*d-b*c
H=X X^T=((A,B),(B,C))
R_H(x)=(q,r,A,B,C)
R_HD(x)=(q,r,A,B,C,D).
```

Equality is literal integer tuple equality. The complete compared reading
is `(n,R_i(x))`. No normalization or quotient by rotation, sign, phase or
scale is used. The ZERO matrix is included. This is real integer algebra,
not an identification of the piston with a complex physical amplitude.

### A. Full-domain descent decision

For each of H and HD, decide whether there exist total maps F0,F1 on the
realizable reading image satisfying `R_i(T_t x)=F_t(R_i(x))` for every
checkpoint and t=0,1. Since both bits occur at actual counters and R_i is
counter-independent, this is exactly descent on N0 x S with n retained.

The following analytical obstruction is exposed before computation:

```
x=(1,0,0,4,0,4), y=(4,0,0,1,0,4), n=0
R_H(x)=R_H(y)=(0,4,1,0,1), D(x)=D(y)=-1
T0 x=(1,1,3,0,2,2), H(T0 x)=(2,-2,4), D(T0 x)=2
T0 y=(3,1,3,3,2,2), H(T0 y)=(5,2,8), D(T0 y)=6.
```

Both inputs choose the actual generator e. The two positive assertions
H_RAW_DESCENT and H_ORIENTED_DESCENT are to be recorded FIRED if this
witness is confirmed. The probe's mathematical targets are the disclosed
negative statement and the complete classification below, not an assertion
that either positive descent survives.

### B. Coarsest common refinement and sharp extra-label capacity

Freeze the class of every counter-independent current-checkpoint map C_i
on S such that R_i factors through C_i and both T0,T1 descend through C_i.
Do not assume a particular coordinate form or auxiliary alphabet for C_i.
The same reading must work on the full N0 x S; n-dependent partitions and
restrictions to origin-reachable states are outside this comparison class.

Start with the equality partition P0 of R_i and repeatedly split a class by
the two successor class labels. Stop at the first stable partition P*.
Report the actual result. Singleton closure is NOT a frozen assertion.

The proof must establish that P* is the coarsest common congruence refining
P0. For each original fibre B, let m(B) be the number of P* blocks in B.
The sharp size of an extra label alphabet in a reading `(R_i,tag_i)` is
`M_i=max_B m(B)`: distinct P* blocks require different labels in B, and
labelling these blocks by increasing least checkpoint index attains M_i.
Verify both induced transition maps on every checkpoint. The label is a
derived present-state readout, not a clean initialized memory register,
native writing mechanism, reversible extension or physical information cost.

Arbitrary binary words may be used to certify the common refinement. This
does not claim that every such word is a Thue-Morse segment. It proves the
stated common counter-independent reading property, which requires both
one-step maps, not a minimum for arbitrary counter-dependent readers.

### C. Separately declared centered stable-sheet comparison

Set `z=sum(x) mod5` and S14={x:z in {1,4}}. The common fixed piston of
b,d,e is `p*=(1,3,4,2)`. Uniqueness follows already from d(p*)=p*.
Define `w=ell(p-p*)` componentwise AFTER the field subtraction, reshape w
in the same order, and call its four invariants `A*,B*,C*,D*`.
Retain `(n,z,A*,B*,C*,D*)`. Neither raw R_i nor its full-domain class is
replaced by this centered comparison.

The prospective exact native table is:

| t | z | selected generator | next z | H* update | D* update |
|---|---|---|---|---|---|
| 0 | 1 | b | 4 | swap the two rows and columns | -D* |
| 0 | 4 | e | 4 | unchanged | D* |
| 1 | 1 | d | 1 | unchanged | D* |
| 1 | 4 | b | 1 | swap the two rows and columns | -D* |

At the lifted matrix level b sends W to -sigma_x W and d/e send W to -W.
For the integer quadruple

```
Q=(A*+C*, A*-C*, 2B*, 2D*)
Q0^2-Q1^2-Q2^2-Q3^2=0,
Lambda=diag(1,-1,1,-1),
```

b acts by Lambda and d/e by identity. This is a specified quadratic map to
an integer null cone, not an identification of H*=W W^T with a general
complex Herm2 matrix. The raw real Gram alone has three coordinates.
No adjoining i or selecting a complex corner phase is used.

With chi(1)=1, chi(4)=-1, the vector
`Q_flat=(Q0,chi(z)*Q1,Q2,chi(z)*Q3)` is invariant under both controls.
This is a specialization of the already registered
U-NATIVE-INVARIANT-AND-NOWRITE mechanism. It supplies no boost, propagating
photon, physical time coordinate, measured energy, occurrence law or
apparatus. The apparent two-valued motion has an explicit sheet-dependent
constant frame. Audit all 15625 origin-zero inputs through the actual first
three bits 0,1,1; their final trace must be 1. This entrance is an inherited
control, not a newly claimed synchronization theorem.

## 2. Code and exact finite data

The accepted `verify.py` uses Python standard-library integer arithmetic.
No predecessor executable is imported. States are in lexicographic order
on {0,1,2,3,4}^6, equivalently the ordinary six-digit base-five index.
All 15625 states, both controls, and all 625 piston values are included.
No random search, float, tolerance, network or target fitting is allowed.

The independent `break.py` must be written by a different agent from this
frozen preregistration without reading verify.py or its output. It must use
an independently assembled native map and a different refinement method,
such as pair distinguishability propagated backwards, then freeze its code
publicly before either program is executed or their scientific outputs are
compared. Static syntax inspection is permitted before pinning. Its author
must report exactly what sources were read. No independence claim follows
merely from executing the builder's verifier or changing architecture.

### Deterministic output contract

Each program emits exactly one compact JSON object followed by LF, using
sorted keys, separators comma and colon, and no timestamp or runtime.
The object fields are:

- `probe`: this probe identifier; `state_count`: 15625;
  `controls`: [0,1]; `piston_identity_count`: 625;
  `generator_involution_checks`: 78125; `status`: COMPLETE.
- `witness`: keys `left`, `right`, `initial_H`, `initial_D`,
  `next_left`, `next_right`, `next_left_H`, `next_right_H`,
  `next_left_D`, `next_right_D`, containing the displayed full tuples or
  integers (H is encoded [A,B,C]).
- `readers`: keys GRAM and ORIENTED, each with the fields below.
- `stable_sheet`: `count`=6250; `step_checks`=12500;
  `centre`=[1,3,4,2]; `origin_heads_verified`=15625;
  `origin_final_trace`=1; `cone_identity_checks`=6250;
  `flat_invariant_checks`=12500; `cone_images` is the number of distinct
  `(z,Q0,Q1,Q2,Q3)` records on S14; `cone_zero_states` counts checkpoints
  whose Q is zero; `action_table`=[[0,1,1,4,-1],[0,4,4,4,1],
  [1,1,3,1,1],[1,4,1,1,-1]], with entries (t,z,g-index,next-z,Q1/Q3 sign).

Each reader object has:

1. `initial_classes`, `initial_size_histogram`, `refinement_class_counts`,
   `stable_classes`, `stable_size_histogram`. A histogram is a sorted list
   of [class_size,number_of_classes]. The count sequence starts at P0 and
   appends only strict refinements, with no repeated terminal count.
2. `first_split_controls`: two counts, one per t, of original P0 fibres
   whose successors have more than one P0 label.
3. `required_extra_labels`=max m(B), `ambiguity_histogram` the sorted list
   [m(B),number_of_original_fibres] and `tagged_transition_checks`=31250.
4. `partition_sha256`: hash of the ASCII string of all P* least-member
   indices in checkpoint order, joined by commas, followed by LF.
5. `transition_sha256`: hash of one ASCII line per P* block, increasing
   least-member index, with comma-separated least-member indices
   `representative,T0-successor-block,T1-successor-block`, each ending LF.
6. `maximal_fibre_witness`: keys `reading` and `representatives`. Select
   the first P0 fibre by least checkpoint index with maximal m(B).
   `reading` is its full R_i tuple; `representatives` contains the full
   checkpoint tuple of each P* least member in that fibre, increasing.
7. `descent`: YES iff neither first_split_controls count is positive,
   otherwise NO; `positive_hypothesis`: SURVIVES or FIRED accordingly.

## 3. Systematics and proof obligations

- Audit all five generator involutions on all checkpoints; do not assume
  the selected T_t itself is a permutation.
- Audit AC-B^2=D^2 on all 625 balanced pistons and all centered checkpoints.
- Keep q,r in both raw readings, z in the centered reading and the full
  native n in the complete model. No uncounted clock or selector is used.
- Do not confuse a generator counterexample with native descent; the
  displayed obstruction uses the actual selector at n=0.
- Certify both directions of minimal refinement and sharp label capacity.
  A finite table without the refinement proof does not establish minimality.
- Keep centered and raw readers and their domains separate. The centered
  positive result does not retract the full-domain raw obstruction.
- Do not claim that a null-cone identity supplies a metric selection,
  dynamical boost, physical dimension, photon or local measurement.

## 4. Failure threshold and disposition

Any exact counterexample to a disclosed identity, the native witness,
stable-sheet table, null identity, flat-frame invariance, or constructive
completion invalidates that corresponding target. Preserve it unchanged.
The partition size and capacity are decision outputs, not presupposed
targets; a non-singleton terminal partition is not a failure.

Any discrepancy between independently frozen program outputs is STOP for
the combined result until explained without changing either frozen source.
A pin, authority, provenance or environment mismatch, missing evidence,
nonzero exit, nonempty stderr or stdout byte mismatch is integrity STOP.
No threshold, carrier, equality, input family or source may move after pin.
The existing repository 600-second verifier timeout is binding. A timeout
does not establish or refute a mathematical claim.

## 5. Layer, lineage and scope

L1 exact finite and integer algebra only. Dependencies are the stated native
architecture, DEF-QDD-BALANCED-PISTON, DEF-PISTON-2X2-RESHAPE and the exact
identities above. Predecessors are P-PISTON-RELATIONAL-WEDGE-1,
QDD-DIRECT-RECORD-E-NONCONGRUENCE and U-NATIVE-INVARIANT-AND-NOWRITE.
The separate contact Gram question in issue #1844 and two-cell compiler
factor in ALGEBRAIC-RESIDUAL-REALIZATION are not taken over.

The native centre is selected by simultaneous affine fixed-point equations
in the declared stable-sheet scope. No global physical uniqueness is
claimed. There is no identification with the cyclotomic QPAIR carrier,
the Hodge E+ carrier or a measured Lorentzian manifold. Apparatus, actual
record writing, preparation, occurrence, Born law, energy scale, physical
time and every L2-L6 lift retain their existing obligations.

## 6. Run and publication procedure

Publish and read back PREREG.md, PROOF.md and verify.py before execution.
Publish and read back the independent breaker before any comparison.
Run the exact pinned programs from a clean repository root with
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Record the first author stdout, pins and hashes, then use the unchanged
tools/check_verifier.py and required x86_64/aarch64 workflow.
Same-architecture replay is reproduction. A separate fold alone can promote
results into Canon. This branch changes one probe directory only.
