# P-U-POINT-SOURCE-READOUT-DICHOTOMY-1

Status: FORMAL PUBLIC PROBE preregistration. No run recorded here.
Owner: A. M. Thorn / Codex-v86-point-source-20260915. Lock: #1010.
Authority: Public Canon v85, main a0fd0a9c1b8bb48126dd2d6bd6d6f712814a9da0.
Content: f7b98cb701f120d1cf807955aea1ee035d8376fe.
Canon SHA-256: c96d06521305c7c6ab046de0be62a3309f05908eb8a82ed1f1f1c86575718a41.
Action layer: L1 only; no physical cross-layer gate.

## 1. Frozen equation and scope

The single prospective claim is U-POINT-SOURCE-SHARP-READOUT-NOGO.
Choose any five distinct native preparations at a common clock phase and
any finite deterministic native protocol. Each mark s has one complete
endpoint f(s). A deterministically assigned finite history or terminal time
may be an enlarged comparison label, without asserting material recording.

Use the FREE counting-form representation N_f e_s=e_f(s),
H=ker(sum:Q5->Q), Pi=I5-ones5/5, and its real or complex scalar extension
for general real response weights. Completeness requires N_f to preserve
the norm on all H. The endpoint pointer is any diagonal effect 0<=D<=I,
including classical randomized postprocessing. Non-diagonal coherent
readout, different encodings and coherent correlated preparations are
outside this class.

Prove exactly: N_f|H is isometric iff f is injective. A collision kills a
nonzero contrast of squared norm two. If f is injective, every endpoint
effect is Pi diag(w) Pi restricted to H, with arbitrary w in [0,1]^5,
and conversely every such tuple is a mathematical endpoint effect. The
only sharp orthogonal projectors in this continuous class are 0 and I_H.
No placement or finite duration within the stated class realizes a
nontrivial sharp projector, including the marked simplex LOW/HIGH pair.

The proof uses the complete positive identity

    F-F^2=V^*D(I-D)V+V^*D(I-P_C)DV,
    P_C=VV^*, F=V^*DV,

for an isometry V. For binary D, sharpness iff [D,P_C]=0 is a proof lemma,
not another prospective Canon claim. On the simplex every coordinate is
active, and D preserving H forces all binary entries equal.

## 2. Accepted code

The new verify.py in this first pin uses only standard-library integers
and Fraction. It imports no predecessor code, executes no incubation audit,
and reads no moving Canon file or external input. The self-contained proof
is committed with it. Static parsing is allowed before pin; execution is
not. Commit, push and public readback must precede the first formal run.

## 3. Complete finite audit carrier

Enumerate the 52 restricted-growth partitions of five marks, representing
every endpoint map up to output relabeling. Check the full Gram on a basis
of H; exhibit a killed norm-two contrast for every noninjective partition.
Audit all 25 ordered quadratic coefficients of the continuous compression
identity, all 32 binary simplex masks and their exact defect
tr(F-F^2)=k(5-k)/25. Check the binary commutation lemma also on a positive
control with two disconnected active blocks, which has four distinct sharp
effects. This control creates no separate result or physical scope.

## 4. Systematics and completeness

The finite partition enumeration is complete modulo endpoint relabeling.
The continuous effect theorem relies on the proof and positivity, not on a
finite weights grid. Deterministic native evolution is consumed only as a
point map, so no duration sample or native census is needed. The contrast
argument holds for every noninjective map. The Gram and operator equalities
are full equalities on H, not selected weight ratios. No amplitude repair,
coherent output gate or physical ensemble is inserted.

The actual sixteen-state Galois-fiber code has a different coherent
encoding and lies outside this five-point representation. Its success is
compatible with this theorem. No complete physical apparatus family,
all-deterministic-theories obstruction or physical occurrence law is
asserted. Apparatus preparation/adoption, actual event, occurrence,
persistence/reset, complete family and L1-to-L5/L6 gates remain open.

## 5. Failure threshold and execution

Exact equality is required for every frozen assertion. Any failed assertion
rejects its target and is retained without changing source, domain or
threshold. Nonzero exit, stderr or absent completed stdout receives the
disposition required by POLICY.md. No random run, tolerance, floating point
or target tuning is allowed.

The first local run follows AGENTS.md section 6 from the repository root.
RUN.md records the public pin, source hashes, neutral environment, exit,
exact stdout and stderr. Replays use tools/check_verifier.py, its fixed
environment and timeout. Both clean GitHub architectures and their
aggregate check must match the same committed EXPECTED.txt. A local
same-architecture run is reproduction only, not independent confirmation.

## 6. Provenance

Completed source mathematics: #1005, PROOF Git blob
2644a8766d2b3fb5681875020acdaaeb97c8fc86; SHA-256
4fa81a861d9c3281f7cc946ca3161ab8f936d4d9527ab9f832605e5ba5dca7ec.
Its old audits are not formal evidence here. No #996 computation is used.
The author approved the connected account's default commit identity for
this work. Original new proof and code: A. M. Thorn, Apache-2.0.
