# Independent review of the native receiver and marked carry mirror

Status: NON-CANONICAL / L1. Candidate C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N.
Owner: Claude Code session on branch `claude/fervent-hawking-5kp9fb`,
2026-11-03. Review lock: issue #1885.
Authority base: `main` 17de90b58f814238e151aac77badde6654b52627, ACTIVE
Public Canon v108 (`canon/CANON.md` SHA-256
c2c4a1ef4ad8859b4b9e9e92022bdd3528c641a3e426df66dc4ade640a5b862a).
Target: PR #1884, head c9bd0bc5ac97ad034be399e6619695c7fc2c4a61, probe
P-NATIVE-RECEIVER-CARRY-MIRROR-1, scientific source pin
aaf3ec7e925c2c0261604179ee4166d542233e14.

## Exposure and source boundary

The target's results were published before this review began, in the PR
body, the author's PR comment, RESULT.md and EXPECTED.txt. This review
therefore does not discover them blind.

The coordinator of this review (this session) read the target verify.py,
compiled_audit.py, EXPECTED.txt, RUN.md, RESULT.md and the PR comment before
writing this file. It also replayed the target verifier once, locally, for
the CI audit. The coordinator's symbolic review is therefore exposed to both
the results and the target code. That exposure is recorded here, not hidden.

The checker `review.py` is written in a separate, fresh agent context. Its
writer may read only:

- target PROOF.md, PREREG.md and PROVENANCE.md at the pin above;
- target arithmetic_compiler.py, which is the declared compiler source. The
  writer may use it for its schedule builder and the meaning of its six
  primitives;
- the native generator definitions in `canon/CANON.md` (section 2 and the
  generator table);
- this file.

The writer must not read the target verify.py, compiled_audit.py,
EXPECTED.txt, RUN.md, RESULT.md or RUNTIME_SOURCES.json, any PR or CI text,
or the coordinator's scratch files. Before the pin, the only permitted work
is syntax compilation and static inspection. No scientific check is run.

Before the pin, the coordinator's static inspection of the checker is limited
to whether it conforms to this file. RUN.md records any change that the
coordinator requested.

This file and review.py are committed, pushed and read back byte for byte
from GitHub before the first execution.

## Independent arithmetic

- **Native U.** U is encoded from the canonical form
  `(p1,p4,p1p,p4p,q,r)` in `canon/CANON.md`. The (A,B,C,D) transcription in
  PROOF.md is encoded separately, and the two are compared on every state.
- **Integral ring.** O=Z[j] is represented by integer coordinate vectors.
  Membership in a power of lambda=1-j is decided with exact norms: for
  y != 0, v_lambda(y) = v_5(N(y)), where N(y) is the exact integer determinant
  of multiplication by y. This is a different decision procedure from
  long division by lambda. Any exact quotient by lambda is certified by
  multiplying back.
- **Compiled word.** It is executed by the checker's own six-primitive
  interpreter. The inverse word is built independently, by reversing the
  word and inverting each primitive. The compiler's own `execute` and
  `reversed_blocks` are not used to produce scientific results.

## Frozen checks

Tolerance is zero throughout. Each item is a falsifier. Every "all" ranges
over the complete finite set named.

- **R1 Native transcription and first-tick rows.** The canonical form and
  the PROOF.md form agree for all five generators on all 5^6 states. On all
  625 ready states (A,B,C,D,0,1) at counter zero:
  - s=A+B+C+D+1 selects generator g_s;
  - the post-tick receivers are s=0:(0,1), 1:(0,4), 2:(1,4), 3:(1,0),
    4:(2,0);
  - each s has 125 preparations;
  - the five receiver pairs are distinct.
- **R2 Port.** Among all 125 affine maps alpha*q+beta*r+gamma, exactly
  (1,1,2) returns s on the four admitted rows. It sends the s=0 row to 3. The
  q-reader (1 -> -1; 0,2 -> +1) equals chi(s) on the admitted rows.
- **R3 Trace port.** The trace of g_i(x) depends only on z(x), for all
  states and all i, and has the form z,-z,2-z,2-z,3-z. The trace maps are
  tau_0=(0,4,0,4,4) and tau_1=(2,1,1,3,1) for both clock bits, over all
  5^6 states. On {1,2,3,4} each image has cardinality 2. As an independent
  finite sanity check, no binary clock word of length 1 to 10 realizes
  s -> 2s on all four nonzero sheets.
- **R4 Ring.**
  - J*J^-1=1;
  - J=2-2l+l^2 and J^-1=-2+3l-l^2 in powers of l=lambda;
  - v_lambda(5)=4;
  - the 25 classes lo+hi*lambda are pairwise incongruent modulo lambda^2;
  - F(lo,hi)=(2lo,3lo+2hi) and I(lo,hi)=(3lo,3lo+3hi) are recovered by
    valuation search, not assumed;
  - F and I are mutually inverse on all 25 pairs.
- **R5 Four-register circuit.**
  - On all 625 (q,r,h,k), L equals (q,r,b+3k,3b+2h) and L^2=id.
  - L equals the conjugate of SWAP(h,k) by F after the shear.
  - With blank h=k, the intermediates are as declared.
  - I(F(b,0))=(b,0), the full-word control.
- **R6 Integral carries.** For both integer sections (counting and balanced)
  and every b in the section:
  - C=(Jb-a)/lambda is integral;
  - the paired return is exactly b;
  - C_mirror=-J^-1*C holds exactly;
  - res C=3b, res C_mirror=b, and the signs are as declared;
  - the same-input control gives residue 3b;
  - for both reader lifts, the second coefficients are u=b for J and u=-b
    for J^-1, so u/v is 2 for J and 3 for J^-1 when b != 0;
  - every carry is zero when b=0.

  Proof-argument stress test: the PROOF arguments do not depend on the
  section. For every integer b and every integer lift a of the output
  residue with |b|,|a|<=30, check the same integrality, the exact mirror
  identity, the residues and the two second-carry coefficients.
- **R7 Omitted offset.** Using q+r without +2 gives the wrong mark for all
  500 admitted preparations. The sign-only comparison chi(q+r)=chi(s) agrees
  for exactly 125 of them, the s=1 sheet.
- **R8 Second native device.** Prepare (4,0,0,0,0,1) at counter zero and add
  a in {1,2,3,4} to the first piston. One origin tick then gives a q-reader
  value of chi(a). For a=2b this equals -chi(b).
- **R9 Compiled components.**
  - The compiler file has 13728 bytes and SHA-256
    0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027.
  - The word comes from layout(2), multiplier_blocks and primitive
    expansion. It uses only the six-primitive alphabet. Its length is 40348
    and its inventory is EQ 30368, MUL 5840, REFLECT 1168, SCALE 2,
    SHIFT 112, SUM 2858.
  - Every primitive has distinct wires inside 0..49.
  - On all 25 inputs, the word gives F and its independent inverse gives I.
    Cells 2..49 return to zero and an external sentinel is unchanged.
- **R10 Compiled occupied circuit.** This check is stronger than the
  target's audit. Start from all 625 (q,r,h,k) with clean work cells and run
  shear, word, the four-primitive swap gadget, the inverse word and the
  inverse shear. The result equals the closed L, and a second pass restores
  the state. The gadget exchanges all 25 (h,k).
- **R11 Integrated 62 cells.** The layout follows PROOF.md section 8:
  - cells 0,1 hold data;
  - cells 2..49 are work cells;
  - cell 50 is the archive;
  - the primary machine is (51,52,53,54,0,55);
  - the secondary machine is (56..61).

  The 58 non-piston cells have one common preparation. Run the PROOF
  section 8 schedule for all 625 piston tuples. Each tuple uses 80705
  primitives and two native origin ticks.

  For each of the 500 admitted tuples:
  - the primary post-tick checkpoint is restored;
  - the archive holds 3s and the high cell holds s;
  - the secondary checkpoint equals U at the origin applied to
    (4+2s,0,0,0,0,1);
  - the work cells are zero at every multiplier boundary;
  - the sign relations hold.

  The admitted tuples fall into four boundary classes of 125 each. For the
  125 s=0 controls, the closed L predicts mark 3, high 3 and archive 4, with
  the checkpoint restored. That prediction is asserted.

## Output, execution and failure handling

Stdout is one line of JSON with sorted keys. It contains no paths, times or
platform values.

The command, run once from the repository root, is:

`python3 notes/C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N/review.py [--compiler PATH]`

The compiler bytes are read from PATH. The default is
`probes/P-NATIVE-RECEIVER-CARRY-MIRROR-1/arithmetic_compiler.py`. Before
import, the bytes must match the frozen size and SHA-256 in R9, so the path
does not affect the compiler's identity. The target is not merged into this
branch, so the recorded run passes the path of a clean checkout of the
target pin. RUN.md records that path. No other target file is read at run
time.

The environment is LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1, with assertions enabled. Only the Python
standard library is used.

The local run uses a single x86_64 lane. The target's two-architecture gate
is audited separately from the actual CI job logs.

An exception, a nonzero exit or nonempty stderr is not a pass. A fired check
is recorded unchanged. If a failure is a checker defect rather than a
property of the target, RUN.md says so and keeps the frozen file. Any
correction is a new, separately pinned revision, and both runs are retained.
Known target results never justify dropping a case or moving a threshold.

## Interpretation

MATHEMATICAL-REVIEW.md reviews PROOF.md section by section. It gives a
verdict on each of the four declared v109 scopes: accept, accept with stated
corrections, or reject. A mathematical fit is not a Canon fold. This review
changes no registry row, status, Canon text or release.

The interconnection, the second origin, the routing and the schedule remain
supplied. Native time reversal, a physical time direction, archive
regeneration and any L1-to-L4 bridge stay outside this review. Accepting
the review and folding it into a future Canon are decisions for the Canon
owner.
