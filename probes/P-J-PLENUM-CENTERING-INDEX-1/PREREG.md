# P-J-PLENUM-CENTERING-INDEX-1 preregistration

Status: **FROZEN TARGET / PUBLIC STATUS NONE / NO FORMAL RUN**.

Disclosure: **RESULT-EXPOSED / PROOF-FIRST / L1 ONLY**.

Owner: A. M. Thorn.

```text
probe:           P-J-PLENUM-CENTERING-INDEX-1
claim:           J-CENTERING-IMAGE-INDEX
public issue:   https://github.com/mathorn1973/twist-j/issues/814
public base:    fbf33fa1116d9e3526ac4ae057356cf2d2bddb6e (Canon v75)
formal runs:    0
public status:  NONE
branch:         probe/P-J-PLENUM-CENTERING-INDEX-1
path:           probes/P-J-PLENUM-CENTERING-INDEX-1/
```

This target and its accepted exact verifier are reserved under issue #814.
Authority and collision checks used the public base above. Both files passed
independent static proof and code review without execution or import. The
first formal execution requires their immutable commit to be pushed and read
back byte for byte. The source commit and file hashes are recorded in RUN.md.

## 1. Predecessor and exposed result

The predecessor is `P-J-PLENUM-POLAR-GAUSS-1`, public issue #804 and PR #805.
Its immutable G02 compared the determinant of an operator restriction with
the index of a different image lattice. The public result is
`CLAIM A SCIENTIFIC-FIRED`; that identifier, verifier, threshold and result
remain unchanged. The predecessor's `RESULT.md`, section "Exact G02
diagnosis", already exposes both correct determinants and their distinction.
Its `PREREG.md`, section 4.1, supplies the exposed image-lattice proof.

This successor tests one new, separately bounded claim. It does not repair,
resume, rename or reclassify the predecessor. In particular it does not
promote the predecessor's combined polar-Gauss claim A, its other passed
components, or any physical reading. The outcome is not a blind prediction.

The coordinator must search the current public Registry, probes, open issues,
pull requests, local refs and `git ls-remote --heads origin` for collisions.
An unresolved competing claim or probe is a stop condition. The expressly
disclosed completed predecessor above does not reserve this successor.

## 2. Equation and exact carrier

Work only at p=5. Let E=Z^5 have the ordered basis e_0,...,e_4, let
`u=(1,1,1,1,1)^T`, and define

```text
epsilon(c) = sum_i c_i,
V_Z = ker epsilon,
f_i = e_i-e_4                     for i=0,1,2,3,
F = [f_0 f_1 f_2 f_3],
N = u u^T,
D = 5 I_5-N,
D(c) = 5c-epsilon(c)u.
```

Vectors are columns, matrix action is on the left, and equality is literal
integer vector or matrix equality. The matrices of maps on V_Z use the
ordered basis `(f_0,f_1,f_2,f_3)` on both sides. No quotient by relabelling,
rescaling or physical equivalence is implicit.

The auxiliary cycle is `g e_i=e_(i+1 mod 5)`; write `J=I_5+g^2` only for the
commutation identity below. This five-dimensional group-ring action is not
identified with a physical update, apparatus or state population.

## 3. One frozen claim and complete elementary proof

The claim consists exactly of the following clauses.

### 3.1 Kernel and image

```text
ker_Z D = Z u,
im_Z D = {d in V_Z : d_i=d_j mod 5 for every i,j}.
```

If D(c)=0, then `5c_i=epsilon(c)` for every i, so all c_i are one integer
and c is an integer multiple of u. Conversely D(u)=0.

Every D(c) sums to zero and all its coordinates are congruent modulo five.
For the converse, let d sum to zero with all coordinates congruent to an
integer r modulo five. Then `c=(d-r u)/5` is integral, `epsilon(c)=-r`, and
`D(c)=d`. This is a universal integral preimage construction, not a finite
sample of possible d.

### 3.2 Image-generator basis and determinant

Let `B_image=[D(e_0) D(e_1) D(e_2) D(e_3)]`. All five columns of D generate
its image, and their sum is zero. The first four therefore generate it. In
the f basis their coordinate matrix is

```text
M_image = 5 I_4-u_4 u_4^T
        = [[4,-1,-1,-1],[-1,4,-1,-1],
           [-1,-1,4,-1],[-1,-1,-1,4]],
F M_image = B_image,
det M_image = 125.
```

Here `u_4=(1,1,1,1)^T`. Over Q the u_4 line has eigenvalue one and its
sum-zero complement has eigenvalue five, proving determinant `1*5^3=125`.
Thus the four image generators are independent and
`[V_Z:im_Z D]=125`.

### 3.3 Smith certificate and quotient

Use the two explicitly integral matrices

```text
U_smith = [[1,1,1,1],[1,2,1,1],
           [1,1,2,1],[1,1,1,2]],
V_smith = [[1,-1,-1,-1],[0,1,0,0],
           [0,0,1,0],[0,0,0,1]].
```

They satisfy

```text
det U_smith = det V_smith = 1,
U_smith M_image V_smith = diag(1,5,5,5).
```

An elementary derivation first adds rows 1,2,3 to row 0, then subtracts
column 0 from each of columns 1,2,3, then adds row 0 to each of rows 1,2,3.
These are unimodular operations and yield the displayed diagonal. Its
positive diagonal entries form a divisibility chain, hence the Smith data
are exactly `(1,5,5,5)` and

```text
V_Z / im_Z D is isomorphic to (Z/5Z)^3.
```

This is an isomorphism of finite abelian groups, not an equality of a
quotient with the chosen coordinate presentation.

### 3.4 Operator restriction is a different matrix

Since epsilon vanishes on V_Z,

```text
D F = F R_restriction,
R_restriction = 5 I_4,
det R_restriction = 625.
```

The image of this restricted operator is `5 V_Z`, not `im_Z(D:E->V_Z)`.
Its determinant must never be compared with 125 as an image-index test.
The frozen negative control requires precisely that the false equation
`det R_restriction=125` be rejected, while the correct index test passes.

### 3.5 Centering identities

`N^2=5N` gives `D^2=5D`. Since g fixes u and preserves epsilon, `Dg=gD`;
therefore also `DJ=JD` for the declared J. These are L1 identities only.

## 4. Code and proof-to-audit correspondence

The accepted program is the separately pinned `verify.py` in the future
formal directory `probes/P-J-PLENUM-CENTERING-INDEX-1/`. It uses only the
Python standard library, integer arithmetic, bounded matrices and an exact
Leibniz determinant on matrices of size at most four. It has no file input,
network, subprocess, environment read, clock, randomness or external data.

The complete universal proofs are section 3. The verifier audits their
finite matrices and unimodular certificates; finite tests are not offered
as the proof of a statement about all integer vectors.

All six gates own the one claim:

```text
G01 CARRIER                 basis, zero sum, cycle of order five
G02 KERNEL_IMAGE_PREMISES   D u=0, row differences, image congruences,
                           zero column sums and D F=5F
G03 IMAGE_BASIS_INDEX       fifth-column relation, F M=B, image det125
G04 SMITH_COKERNEL          unimodular U/V and Smith(1,5,5,5)
G05 RESTRICTION_DISTINCTION D F=F R, R=5I, restriction det625,
                           false restriction-det125 control rejected
G06 CENTERING_COMMUTATION   D^2=5D, Dg=gD and DJ=JD
```

## 5. Systematics and fixed failure threshold

- The image-generator domain is E=Z^5; the restriction domain is V_Z.
  Their matrices are constructed separately and never substituted.
- Basis coordinates are the first four entries only because the fifth is
  their negative sum; the verifier also checks the complete embedding F.
- Smith transformations must be integral with determinants exactly one;
  rational similarity or determinant alone is not a quotient certificate.
- Congruence is modulo five; equality elsewhere is literal integer equality.
- There is no tolerance, fitted parameter, selected range or adjustable
  failure threshold. Any false exact gate fires the one claim.
- A validly constructed negative gate is recorded as `FIRED` with exit zero;
  the program continues through all gates and emits one terminal. A malformed
  program, structural runtime error or custody failure is integrity `STOP`,
  not scientific refutation.
- An independently established defect in the universal written proof blocks
  confirmation even if the finite audit passes.

No gate, predicate, scope or output rule may change after the public pin.

## 6. Frozen transcript and decision grammar

The program writes ASCII/LF stdout: one identity line, one disclosure line,
six gate lines in G01,...,G06 order, one claim line and one terminal line.
Gate lines contain the exact identifier, name and `PASS` or `FIRED`; they
do not print success metadata when that gate failed.

```text
CLAIM J-CENTERING-IMAGE-INDEX CONFIRMED
TERMINAL CONFIRMED
```

are emitted exactly when all gates pass. Otherwise the final two lines are

```text
CLAIM J-CENTERING-IMAGE-INDEX FIRED
TERMINAL SCIENTIFIC-FIRED
```

The scientific status ceiling is publicly unregistered `candidate-T / L1`
only when the proof is valid, every gate passes and all required custody and
architecture checks pass. A scientific mismatch is recorded without repairing
the verifier. An integrity failure follows the separate STOP route.

## 7. Action layer and scope exclusions

Action layer: **L1**. Inputs and outputs are exact integer lattices and
finite integer matrices. No L2--L6 gate is used or earned.

No polar decomposition, Gauss sum, finite polar group, coordinate-square
probability, Born selection, unit population, preparation, apparatus, event,
record, occurrence law, sampling, self-location, decoder completion, physical
time, photon, gravity, scale or SI claim is included. No conclusion repairs
the predecessor's combined claim A. No Canon or frontier status changes merely
because this successor is confirmed or merged.

## 8. Public pin, one execution and custody

Before execution the coordinator must finish the authority and collision
checks, reserve the public issue, create the formal `probe/` branch and
directory, resolve the preparation fields, statically review both files,
then commit and push the exact preregistration and verifier. Record their
SHA-256 values and the full immutable source commit, and read the exact bytes
back from GitHub before the first gate execution.

The formal invocation from the repository root is

```text
python3 probes/P-J-PLENUM-CENTERING-INDEX-1/verify.py
```

Use Linux or a Linux-compatible environment and capture raw stdout, stderr
and exit status without an output-rewriting pipeline. Hash the verifier
immediately before and after its sole local formal execution. Preserve exact
stdout as `EXPECTED.txt` only after that execution; record neutral environment,
pin, hashes, byte counts and exit status in `RUN.md`, and the scientific or
integrity disposition in `RESULT.md`. Do not execute or import the accepted
verifier during preparation; no such run has been made here.

Required public x86_64 and aarch64 jobs must replay the same verifier and the
same committed `EXPECTED.txt` byte for byte with exit zero and empty stderr.
Require the aggregate `check` and named manual security review. The pull
request changes at most this one probe directory and merges with a merge
commit, never squash/rebase. No amend, rerun under this identifier, force-push,
threshold repair or deletion of a negative result is allowed after pinning.

If the formal run never completes with a valid scientific transcript,
disposition follows POLICY.md's abandoned pin rule. Once a complete exact
formal transcript exists, the result must be recorded;
it cannot be relabelled abandoned. Any later scientific registration requires
a separate reviewed Canon fold.
