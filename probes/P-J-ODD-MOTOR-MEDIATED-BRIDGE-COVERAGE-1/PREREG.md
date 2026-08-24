# P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-1 preregistration

Status: **PREREGISTRATION. FROZEN BEFORE FIRST EXECUTION. NO RESULT YET.**

```text
CLAIM ISSUE     #542
BRANCH          probe/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-1
PATH            probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-1/
STATE           ACTIVE
CANON           Public Canon v61
AUTHORITY       mathorn1973/twist-j main
TAG             canon-v61
CONTENT_COMMIT  76b405033b41397cd62217bf3998ac9c26111964
CANON_SHA256    e9ee0781e489e1c3951b978be567a19c5c7370708095631f966561efe03b6cb5
CANON_BYTES     334100
PIN PARENT      9d384ecc8c539433936df995fd94d4016c01e6e7
TARGET CLAIM    J-ODD-MOTOR-MEDIATED-BRIDGE [T]
LAYER           L1 exact arithmetic only
```

Collision search before this preregistration found no existing issue, branch,
probe directory, Registry row, or v62 release lock with this identifier. This
probe is evidence coverage only. It does not extend the current theorem scope,
move a status, add a dependency, create a gate, or make a physical claim.

## 1. Equation

Freeze the current Public Canon v61 theorem scope exactly. Let

```text
M_J = multiplication by J = 1 + zeta_5^2,
D = M_J - I,
A = D - D^-1,
G = I - (1/5) 11^T,
X^sharp = G^-1 X^T G.
```

For each affine token k in F_5, let P_k, R_k, C_k be the frozen
multiplier-stabilizer sectors already used by the public theorem. The accepted
verifier must establish all of the following without strengthening them:

1. Over Q(sqrt(5)), the native characteristic factorization has exactly two
   complementary primitive nonzero rank-two sectors. The two quadratic
   discriminants are

   ```text
   delta_u = (-5-sqrt(5))/2,
   delta_s = (-5+sqrt(5))/2,
   ```

   and both are negative in both real embeddings. Explicit CRT idempotents are
   complementary and have ranks 2 and 2.

2. For A=D-D^-1 and every token, the exact block graph is

   ```text
   P <-> C <-> R,
   ```

   with zero diagonal blocks, zero direct P-R and R-P blocks, rank-one P/R-C
   cross blocks, and

   ```text
   B = P A C A R,
   rank(B)=1,
   B^sharp B=(5/4)R,
   B B^sharp=(5/4)P.
   ```

   The two active C-lines have squared overlap 1/5.

3. The frozen control family D,D^2,D^3,D^4,D+D^-1 does not exhibit the same
   direct-zero / one-mediator-nonzero pattern.

4. With H=g+g^-1, the token sectors have eigenvalues +2,-2,0. For the formal
   pencil L=zI-H-tA, exact elimination of C gives

   ```text
   S_PR = -(t^2/z) P A C A R,
   S_PR^sharp S_PR = (5/4)(t^4/z^2) R,
   S_PR S_PR^sharp = (5/4)(t^4/z^2) P.
   ```

   At token 2 the full determinant is exactly

   ```text
   z^4 + (5t^2-4)z^2 + 5t^4.
   ```

5. For G=AGL_1(F_5) on V, the exact character calculation gives

   ```text
   Sym^2(V) = 1 + epsilon + 2V,
   dim End_G(Sym^2 V)=6.
   ```

   The invariant quadratic form q_+ and epsilon-covariant q_- retain their
   frozen transformation laws, the pairwise Hom vanishings used by the public
   theorem hold, and the frozen trilinear census is unchanged. The repeated
   2V is explicitly retained as a nonselection boundary.

The 624-channel-box uniqueness classification from
`P-J-ODD-MOTOR-BRIDGE-HARDENING-1` is excluded. It is later theorem content,
not part of this evidence-replacement obligation.

## 2. Code

Accepted verifier:

```text
probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-1/verify.py
```

Python standard library only. Exact `Fraction` and exact Q(sqrt(5)) pair
arithmetic only. No float literals, tolerance, randomness, file input,
environment input, network access, or third-party package. Run from repository
root as

```text
python3 probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-1/verify.py
```

under deterministic locale/hash/timezone settings. Exit 0 and empty stderr are
required.

Before the pin, only `py_compile` and static AST scans are permitted. The
static scan must report only imports from `fractions` and `itertools`, no float
literal, and no calls to `float`, `open`, `input`, `eval`, `exec`,
`__import__`, or `random`.

## 3. Carrier or data

No external data. The carrier is the frozen rational four-dimensional
`M_J` representation and its five affine token sectors. The matrices,
normalization G, affine action, Q(sqrt(5)) factorization, q_+, q_-, formal
variables z,t, and token set F_5 are constants inside the accepted verifier.
No alternative basis, normalization, token subset, control family, or channel
box is admitted after the pin.

## 4. Systematics

The verifier uses independent exact routes where the public scope has two
representations:

- native sectors: polynomial factorization plus Bezout/CRT idempotent matrices;
- mediated bridge: direct rational block multiplication and G-adjoint norms;
- Schur clause: explicit formal Laurent block elimination, not inference from
  the determinant;
- determinant clause: independent permutation expansion of the full 4x4
  formal determinant;
- Sym^2 clause: finite-group character inner products, separately from the
  explicit q_+/q_- covariance matrices;
- trilinear clause: direct exact character average on all twenty group elements.

The raw-power/even controls are mandatory negative controls. The repeated 2V
is a mandatory nonselection conclusion, not a positive selector.

## 5. Failure threshold

No numerical threshold. Every decision is exact. The route falsifier fires if
any one of these frozen groups fails:

```text
G1 native discriminants / embedding signs / CRT rank-two idempotents
G2 five-token P,C,R decomposition and odd A block graph
G3 bridge rank, 5/4 adjoint norms and 1/5 active-line overlap
G4 raw-power and even-channel controls
G5 explicit five-token Schur elimination
G6 token-2 determinant polynomial
G7 Sym^2 character decomposition, End dimension and pairwise Hom vanishings
G8 q_+/q_- covariance and frozen trilinear census
```

Any integrity, authority, readback, mutation, stderr, security, or workflow
failure is STOP rather than a mathematical falsifier. No threshold may move and
this probe may not be reused under another name.

## 6. Action layer

**L1 only.** Exact arithmetic, finite representation theory and exact linear
algebra. No L2-L6 lift. No material, resonance, frequency, Born, probability,
decoder, apparatus, observer, force, spacetime or SI reading is assumed or
concluded.

## Decision

```text
COVERAGE-CERTIFIED
  G1 through G8 all pass exactly and the required public x86_64 and aarch64
  jobs reproduce one committed EXPECTED.txt byte for byte.

ROUTE-FALSIFIED
  carrier integrity holds and at least one exact G1 through G8 clause fails.
  Preserve the witness. Do not move a threshold.

STOP
  authority, collision, hash/readback, exactness, mutation, stderr, security,
  workflow or provenance requirement fails.
```

Maximum later fold effect: `J-ODD-MOTOR-MEDIATED-BRIDGE` remains `[T]` with
identical scope and dependencies and receives one `EVIDENCE_CHANGE` to this
probe. No new scientific Registry row is authorized.
