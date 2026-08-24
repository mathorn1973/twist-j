# P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2 preregistration

Status: **PREREGISTRATION. FROZEN BEFORE FIRST FORMAL EXECUTION. NO FORMAL RESULT YET.**
Mode: **RESULT-EXPOSED / EVIDENCE-MAINTENANCE.**

```text
CLAIM ISSUE     #543
BRANCH          probe/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2
PATH            probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2/
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
PREDECESSOR     P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-1 STOP
```

The predecessor stopped on a public-pin/local-byte mismatch. A wrapper defect then
executed the local development file after the mismatch. That process is invalid and
supplies no evidence, but it exposed the expected result. This successor is therefore
not blind confirmation. It is a fresh evidence-maintenance probe for an already public
T theorem.

Collision search before claim found no issue, branch, probe directory, Registry row,
or v62 release lock using this successor identifier.

## 1. Equation and frozen obligation

The target is exactly the current Public Canon v61 Registry scope of
`J-ODD-MOTOR-MEDIATED-BRIDGE [T]`, with no extension.

Let

```text
M_J = multiplication by J = 1 + zeta_5^2,
D   = M_J - I,
A   = D - D^-1,
G   = I - (1/5) 11^T,
X^sharp = G^-1 X^T G.
```

The accepted decision must cover all current clauses:

```text
G1  over Q(sqrt5), exactly two complementary primitive nonzero rank-two
    native sectors, with discriminants (-5-sqrt5)/2 and (-5+sqrt5)/2,
    negative in both real embeddings, and explicit CRT ranks 2,2;
G2  on all five frozen affine tokens, P <-> C <-> R with zero diagonal
    and direct P-R blocks and rank-one P/R-C blocks;
G3  B=P A C A R has rank one, B^sharp B=(5/4)R, BB^sharp=(5/4)P,
    and the active C-line squared overlap is 1/5;
G4  D,D^2,D^3,D^4,D+D^-1 fail the same mediated-zero pattern;
G5  H=g+g^-1 has sector eigenvalues +2,-2,0 and exact block elimination
    of L=zI-H-tA gives S_PR=-(t^2/z)PACAR and squared magnitude
    (5/4)t^4/z^2 on all five tokens;
G6  at token 2, det L = z^4+(5t^2-4)z^2+5t^4;
G7  Sym^2(V)=1+epsilon+2V, dim End_G(Sym^2 V)=6, and the registered
    pairwise Hom vanishings hold;
G8  q_plus is invariant, q_minus is epsilon-covariant, and the frozen
    trilinear census holds.
```

The repeated `2V` remains a nonselection boundary. The 624-channel-box uniqueness
classification from the later hardening probe is explicitly excluded and its value is
not a decision input.

## 2. Code

Accepted verifier:

```text
probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2/verify.py
```

Python standard library only. The verifier is a deterministic coverage auditor. It
checks the bytes of two frozen public exact implementations before executing either,
suppresses their own stdout, and consumes only the preregistered namespace booleans.
It uses no network, randomness, tolerance, external dataset, or environment-dependent
scientific input.

Run from repository root:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2/verify.py
```

Exit 0 and empty stderr are required for certification.

Before the pin only `py_compile` and static AST/security checks are allowed. Before
first execution the local accepted file must equal the public pin by both Git blob SHA
and SHA-256. Any mismatch is STOP and Python must not be invoked.

## 3. Carrier or data

There is no external data. The two frozen repository source inputs are:

```text
probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2/verify.py
SHA256 78b5ae47fbede9449e0a7c706dc12e00661a0d3d63227c57ee6a35de84f3ef42

probes/P-J-ODD-MOTOR-BRIDGE-HARDENING-1/verify.py
SHA256 682e1ccdbdc61597d9c08d594c9ea8a9c56b9364e419bc0c0e893c908977c2c8
```

The first public implementation supplies the full affine token/block, bridge, controls,
determinant, Sym2, covariance and trilinear calculations. Its weak historical native
placeholder is not consumed. The second supplies the corrected native discriminant/CRT
hardening and explicit Schur calculation. Its `h3_ok`, survivor list, box count and final
decision are not consumed.

## 4. Systematics

This is evidence synthesis, not independent scientific confirmation. The scientific
content is already public at T. The coverage verifier enforces:

1. both source hashes before execution;
2. exact presence of the frozen decision namespaces;
3. H1-H2 only from the hardening implementation;
4. G2-G8 only from the original implementation;
5. no dependence of the coverage decision on H3 or the 624-channel-box value;
6. one deterministic stdout for public x86_64 and aarch64 replay.

No result from the stopped predecessor is used as evidence.

## 5. Failure threshold

No numerical threshold. Every gate is an exact boolean.

```text
COVERAGE-CERTIFIED
  G1 through G8 all pass and both frozen input hashes match.

ROUTE-FALSIFIED
  frozen inputs match and at least one exact G1 through G8 mathematical
  condition is false.

STOP
  authority, collision, source hash, pin/readback, exactness, mutation,
  namespace, stderr, security, workflow or provenance fails.
```

No threshold may move. This probe is never repaired, renamed or resumed after sealing.

## 6. Action layer

**L1 only.** Exact finite representation theory and linear algebra. No material,
resonance, frequency, Born, probability, decoder, apparatus, force, spacetime, SI, or
L2-L6 statement is assumed or concluded.

Maximum later fold effect: `J-ODD-MOTOR-MEDIATED-BRIDGE` remains `[T]` with identical
scope, falsifier and dependencies and receives one `EVIDENCE_CHANGE` to this complete
coverage bundle. No new scientific Registry row is authorized.
