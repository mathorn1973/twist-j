# P-PURE-QUBIT-RELATIONAL-GEOMETRY-2 preregistration

Status: `PREREGISTERED CANDIDATE / RESULT-EXPOSED / NO FORMAL RUN`

This is a fresh exact L1 attack after
`P-PURE-QUBIT-RELATIONAL-GEOMETRY-1` fired its frozen R1 falsifier. The failed
probe is lineage only and supplies no premise, code, pin, run or evidence.

This document freezes one exact L1 probe connecting the public determinant
line of `QPAIR-SYM2-TENSOR-DEFECT` to standard pure two-qubit geometry after,
and only after, an orthonormal complex bipartite factorization has been
supplied externally. It proves the determinant-area identity, the pure-state
local/relation Pythagorean identity, and an external standard-QM comparison
with the Horodecki maximum-CHSH criterion. It also freezes three scope
breakers: determinant phase is not a local-`U(2)` invariant, the pure-state
Pythagorean law does not extend to mixed states, and one second exterior
scalar does not classify Schmidt spectra once Schmidt rank three is allowed.

This file and `verify.py` form the zero-run initial pin. They confer no
scientific or Canon status. Formal execution is forbidden until both files
are committed to the public branch, their immutable commit and SHA-256 values
are recorded, and the exact remote bytes are read back.

## Public identity, authority, and action layer

```text
probe:               P-PURE-QUBIT-RELATIONAL-GEOMETRY-2
public claim lock:   issue #430
probe owner:         A. M. Thorn / delegated session
branch:              probe/P-PURE-QUBIT-RELATIONAL-GEOMETRY-2
path:                probes/P-PURE-QUBIT-RELATIONAL-GEOMETRY-2/
initial base:        e1fc4677d72eaef5851b103d1fbcbf95cf4dd38f
Public Canon:        v52, tag canon-v52
content commit:      6fc6923f727edacf55d511ec30eee2c7461ac497
Canon SHA-256:       b496e4e73a2b06167a981b75a5ea651591db383a9c7f222e0075eb8bb6f1ee03
Canon bytes:         261476
action layer:        L1 exact state geometry only
mode:                result-exposed, proof-first; verifier is an exact audit
formal runs:         none
static check:        Python ast.parse only; no import or execution
```

Candidate rows and immutable ceilings:

```text
PURE-QUBIT-RELATIONAL-AREA               ceiling T
PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS     ceiling T
PURE-QUBIT-RELATIONAL-CHSH               ceiling T
PURE-QUBIT-RELATIONAL-READING            ceiling D
```

The first three rows are theorem candidates. The fourth is a deliberately
narrow dictionary candidate, not a theorem that TWIST-J creates a physical
qubit. No row may be promoted above its ceiling by rewriting the conclusion.

Proposed dependency edges for a later Canon fold:

```text
PURE-QUBIT-RELATIONAL-AREA
    REQUIRES QPAIR-SYM2-TENSOR-DEFECT
PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS
    REQUIRES PURE-QUBIT-RELATIONAL-AREA
PURE-QUBIT-RELATIONAL-CHSH
    REQUIRES PURE-QUBIT-RELATIONAL-AREA
PURE-QUBIT-RELATIONAL-READING
    REQUIRES PURE-QUBIT-RELATIONAL-AREA
```

There is no dependency edge to the rational piston carrier, QDD, the finite
`BELL-MAGIC-BOUNDARY` functional, or any L2-L6 object.

## Collision and lineage boundary

At lock time the new probe path and branch are absent from public `main`. The
four candidate IDs remain unearned. Issue #428 and PR #429 preserve the closed
failed first attack; issues #419 and #422 are earlier non-canonical linguistic
and mathematical lineage. None of their code, pins, scratch/symbolic runs or
results is evidence for this probe. The merged probe-only results in PRs #426
and #427 explicitly exclude qubits, concurrence and CHSH; they neither imply
nor earn these rows.

The public theorem `QPAIR-SYM2-TENSOR-DEFECT [T]` supplies exactly one
algebraic premise: for a coefficient matrix `A` in a declared `2 x 2`
factorization, the alternating-alternating component of the symmetric square
has determinant coefficient. This probe does not alter that theorem and does
not identify its integral carrier with a laboratory system.

## External standards, pinned as definitions or comparison theorems

1. R. Horodecki, P. Horodecki and M. Horodecki, *Violating Bell inequality
   by mixed spin-1/2 states*, Physics Letters A 200 (1995) 340-344,
   DOI `10.1016/0375-9601(95)00214-N`. This supplies the standard two-qubit
   maximum-CHSH criterion used only in R3.
2. W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two
   Qubits*, Physical Review Letters 80 (1998) 2245-2248,
   arXiv `quant-ph/9709029`, DOI `10.1103/PhysRevLett.80.2245`. This pins the
   standard concurrence convention. Only its pure-state specialization
   `C = 2 |det A|` is used in the theorem rows; the mixed-state formula is
   used only for the frozen Werner breaker.

The exact algebraic statements R1 and R2 have self-contained proofs below.
R3 includes the full two-setting qubit optimization and the pure Schmidt-state
specialization; the Horodecki paper pins attribution and the standard-QM
comparison rather than replacing the proof. No external software or dataset
is used.

## The six frozen fields

### 1. Equation

#### 1.1 Carrier and conventions

Supply externally two orthonormal complex two-dimensional Hilbert spaces
`H_A` and `H_B`. Let

```text
|psi> = a |00> + b |01> + c |10> + d |11>,
A = ((a,b),(c,d)),
Tr(A A^dagger) = |a|^2 + |b|^2 + |c|^2 + |d|^2 = 1,
rho_A = A A^dagger,
D = det A = ad - bc.
```

Use the public unhalved alternating tensors

```text
e0 wedge e1 = e0 tensor e1 - e1 tensor e0,
f0 wedge f1 = f0 tensor f1 - f1 tensor f0,
kappa = (e0 wedge e1) tensor (f0 wedge f1),
||kappa||^2 = 4.
```

After reordering `(H_A tensor H_B) tensor 2` to
`H_A tensor 2 tensor H_B tensor 2`, define

```text
r = P_-- R(|psi> tensor |psi>) = (D/2) kappa,
P_-- = (1-alpha)(1-beta)/4,
```

where `alpha` swaps the two `H_A` positions and `beta` swaps the two `H_B`
positions. Thus `r` is the public determinant-line component and its phase is
oriented-coordinate data; only its Hilbert norm is used as the invariant.

For a standard qubit density matrix define the Bloch vector `b_vec` by

```text
rho_A = (I + b_vec dot sigma)/2.
```

Let `C` denote standard pure-state two-qubit concurrence. Let
`A_0,A_1` on `H_A` and `B_0,B_1` on `H_B` range over Hermitian observables
with spectrum `{+1,-1}`. In standard two-qubit quantum mechanics define

```text
B_max = max |<psi| A_0 tensor (B_0+B_1)
                    + A_1 tensor (B_0-B_1) |psi>|.
```

This is an optimized model value, with the usual local bound 2, not a
fixed-apparatus event statistic.

#### R1. PURE-QUBIT-RELATIONAL-AREA

For every normalized pure state in the declared factorization,

```text
||r||^2 = |D|^2 = det(rho_A),
C = 2 |D| = 2 ||r||,
0 <= ||r|| <= 1/2.
```

Moreover:

```text
r = 0             iff |psi> is a product vector;
||r|| = 1/2       iff rho_A = I/2, equivalently |psi> is maximally entangled;
same ||r||        iff two normalized pure two-qubit states are locally
                  unitary equivalent.
```

The last equivalence concerns the norm. It does not concern the complex phase
of `D` or the oriented vector `r`.

Exact `2 x n` algebraic extension, audited but not used to widen the
concurrence or CHSH rows: if `A` has two row vectors `u,v in C^n`, then

```text
det(A A^dagger)
  = ||u||^2 ||v||^2 - |<u,v>|^2
  = sum_(i<j) |u_i v_j - u_j v_i|^2
  = (1/2) ||u wedge v||_tensor^2,

u wedge v = u tensor v - v tensor u.
```

For a normalized pure `2 x n` vector this determinant fixes the two Schmidt
eigenvalues, including a possible zero, but no standard two-qubit CHSH
statement is claimed for `n != 2`.

#### R2. PURE-QUBIT-LOCAL-RELATION-PYTHAGORAS

For the same normalized pure two-qubit state,

```text
|b_vec|^2 + C^2 = 1,
Tr(rho_A^2) = 1 - C^2/2,
1 - |b_vec|^2 = 4 ||r||^2.
```

In Schmidt gauge, with `0 <= theta <= pi/4`, these become

```text
|psi_theta> = cos(theta)|00> + sin(theta)|11>,
||r||       = (1/2) sin(2 theta),
C           = sin(2 theta),
|b_vec|     = cos(2 theta).
```

This is a pure-state complement between local polarization and relational
area. It is not a conservation law for mixed states or an autonomous
dynamical claim.

#### R3. PURE-QUBIT-RELATIONAL-CHSH

Under the external standard-QM definition and Horodecki criterion above,

```text
B_max = 2 sqrt(1 + C^2)
      = 2 sqrt(1 + 4 ||r||^2),
B_max^2 - 4 = 4 C^2 = 16 ||r||^2.
```

Hence the product endpoint has `B_max^2 = 4`, while the maximally entangled
endpoint has `B_max^2 = 8`. This row is only a coordinate comparison inside
standard pure two-qubit quantum mechanics. It is not a derivation of settings,
outcomes, locality, no-signalling, a Bell experiment, or a TWIST-J event
measure. It does not strengthen or reinterpret `BELL-MAGIC-BOUNDARY`.

#### D1. PURE-QUBIT-RELATIONAL-READING, ceiling D

Once the following structures have been supplied externally:

```text
an orthonormal C^2 tensor C^2 factorization;
a normalized pure vector in that factorization;
the complex Hilbert norm;
the standard reduced state, concurrence and CHSH definitions;
```

the norm of the public determinant-line component may be read as the pure
two-qubit relational area and as one half of the standard concurrence. On
that scope the quantity belongs to the joint state: it is zero exactly when
the joint coefficient matrix factorizes, and it is not a third particle, a
force, a signal, or a separately transported substance. Schmidt rectangles
are a local-unitary gauge for the joint state, not a hidden spatial geometry.

This dictionary asserts no map from the integral QPAIR carrier, the rational
piston carrier, QDD, or any autonomous state to physical qubits. It asserts no
mixed-state convex-roof extension and no L2 manifold, L3 boundary, L4
apparatus, L5 event stream or L6 probability measure.

#### 1.2 Written proofs

Proof of R1. Direct multiplication gives

```text
det(rho_A) = det(A A^dagger)
           = det(A) conjugate(det(A))
           = |D|^2.
```

The public alternating projection gives `r=(D/2)kappa`; because
`||kappa||^2=4`, `||r||^2=|D|^2`. The pure concurrence convention gives
`C=2|D|`. The singular values of `A` are the Schmidt coefficients. Therefore
`D=0` exactly when `A` has rank at most one, which is exactly productness.
For normalized `A`, the eigenvalues of `rho_A` are `lambda` and `1-lambda`,
so `|D|^2=lambda(1-lambda)` lies in `[0,1/4]`, with equality at `lambda=1/2`.
Trace one and determinant determine the characteristic polynomial of a
`2 x 2` density matrix. Thus `|D|`, equivalently `||r||`, determines the
unordered Schmidt spectrum and therefore the local-unitary orbit. The
`2 x n` minors formula is the exact Cauchy-Binet identity for the two-row
matrix; expansion of the declared unhalved ambient tensor wedge gives the
additional factor two in its squared norm.

Proof of R2. The eigenvalues of `(I+b_vec dot sigma)/2` are
`(1+|b_vec|)/2` and `(1-|b_vec|)/2`, hence

```text
det(rho_A) = (1-|b_vec|^2)/4,
Tr(rho_A^2) = (1+|b_vec|^2)/2.
```

Substitute `C^2=4 det(rho_A)` from R1. The Schmidt-angle formulas follow by
putting `lambda=cos(theta)^2` and `1-lambda=sin(theta)^2`.

Proof of R3. Every Hermitian qubit observable with spectrum `{+1,-1}` is
`a dot sigma` for a real unit vector `a`. Let the two Bob directions be
`b_0,b_1`. There are orthonormal real vectors `u,v` and an angle
`0 <= eta <= pi/2` such that

```text
b_0+b_1 = 2 cos(eta) u,
b_0-b_1 = 2 sin(eta) v.
```

Orthogonality follows from
`(b_0+b_1) dot (b_0-b_1)=|b_0|^2-|b_1|^2=0`. For a state with real correlation
matrix `T`, independent optimization of Alice's two unit directions aligns
them with `T u` and `T v`, giving

```text
2 (cos(eta)||T u|| + sin(eta)||T v||).
```

Optimization over `eta` gives `2 sqrt(||T u||^2+||T v||^2)`. Rayleigh-Ritz
optimization over orthonormal `u,v` gives `2 sqrt(m_1+m_2)`, where `m_1,m_2`
are the two largest eigenvalues of `T^T T`. In Schmidt gauge the pure-state
correlation tensor is

```text
T = diag(C, -C, 1),
eigenvalues(T^T T) = (C^2, C^2, 1).
```

Since `0<=C<=1`, the two largest eigenvalues are `1,C^2`. Therefore
`B_max=2 sqrt(1+C^2)`. Substitute `C=2||r||`. This reproduces the named
Horodecki criterion on the frozen pure-state scope.

#### 1.3 Frozen scope breakers

`B1`, local phase. For the exact normalized coefficient matrix
`A=(1/2)((1,1),(1,-1))` and local unitaries `U=diag(i,1)`, `V=I`,

```text
Tr(A A^dagger) = 1,
det(A) = -1/2,
det(U A V^T) = i det(A) = -i/2,
|det(U A V^T)| = |det(A)|.
```

Thus the determinant phase and oriented `r` are not local-`U(2)` invariants;
the norm is.

`B2`, mixed state. Let

```text
rho_W = (1/2)|psi^-><psi^-| + (1/2) I/4.
```

Its partial transpose has eigenvalues `-1/8,3/8,3/8,3/8`, so it is entangled
in `2 x 2`. Its marginal is `I/2`, hence `|b_vec|=0`. The standard Wootters
concurrence is `1/4`, so `|b_vec|^2+C^2=1/16`, not 1. Its Horodecki quantity
is `M=2(1/2)^2=1/2<1`, so `B_max^2=4M=2` and it is CHSH-subcritical. The
pure-state R3 equation also fails: `B_max^2-4=-2`, whereas `4C^2=1/4`.
Therefore neither R2 nor the pure R3 relation is a mixed-state law.

`B3`, higher Schmidt rank. The normalized spectra

```text
(1/2,1/2,0) and (2/3,1/6,1/6)
```

are different but both have second elementary symmetric polynomial
`e2=sum_(i<j) lambda_i lambda_j=1/4`. Therefore one exterior scalar does not
classify local-unitary orbits once Schmidt rank three is available. This does
not contradict the `2 x n` statement, whose qubit side permits at most two
nonzero Schmidt coefficients.

### 2. Code

The accepted verifier is exactly `verify.py` in this directory. It uses only
the Python standard library, accepts no arguments, uses `Fraction`-backed
Gaussian rational arithmetic, imports no project module, reads no file and
writes only stdout. Written proofs carry the universal statements. Finite
grids audit the coordinate formulas and the frozen boundary witnesses.

No execution, import, bytecode compilation, doctest or helper evaluation is
allowed before the immutable pin. Syntax parsing is allowed. After the pin,
the only accepted command is

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-PURE-QUBIT-RELATIONAL-GEOMETRY-2/verify.py
```

Exit codes are `0 PASS`, `1 STOP` for integrity/environment failure, and
`2 FALSIFIED` for a scientific gate failure.

### 3. Carrier or data

There is no experimental data. The theorem carrier is the declared finite
Hilbert factorization `C^2 tensor C^2`, represented by exact Gaussian-rational
coordinate witnesses in the verifier. The Cauchy-Binet audit also uses
`C^2 tensor C^n` for `n=2,3,4`; it is algebraic support only. The fixed mixed
control and higher-rank spectra are displayed above. No cyclotomic field,
finite-field lift, piston, QDD state, decoder record or event stream is input.

### 4. Systematics

The following possible category errors are frozen as mandatory guards:

```text
S1  normalization and an orthonormal bipartite factorization are explicit;
S2  the invariant is ||r||, never the determinant phase;
S3  pure-state claims are not extended to mixed states;
S4  two-qubit concurrence and CHSH are not extended to 2 x n;
S5  the CHSH optimization is standard-QM mathematics, not a TWIST-J apparatus;
S6  BELL-MAGIC-BOUNDARY, QDD and piston claims remain unchanged;
S7  no L1 carrier is silently lifted to L2-L6;
S8  finite exact grids audit formulas but do not replace the written proofs.
```

### 5. Failure threshold

One exact counterexample to any universally quantified equality or
equivalence in R1-R3 is sufficient to falsify the corresponding candidate
row. Any failure of `B1`, `B2` or `B3` invalidates the frozen scope boundary
and is also scientific falsification. A mismatch of a declared exact count,
endpoint or eigenvalue is falsification.

An argument, environment or integrity defect, an exception, nonempty stderr,
an unexpected exit code, a verifier-byte mismatch, an stdout mismatch against
the one committed `EXPECTED.txt`, or disagreement between required
architectures is `STOP`, not scientific falsification. Thresholds and scope
may not move after the initial pin.

### 6. Action layer

The highest earned action layer can only be `L1`: exact geometry of a supplied
state in a supplied factorization. This probe contains no evolution, boundary
condition, apparatus support, realized event or sampling measure. It cannot
by itself support a claim about physical quantization, nonlocal influence,
communication, locality, no-signalling, or a Bell experiment.

## Frozen verifier exposure and outputs

The determinant, Pythagorean, Schmidt and CHSH formulas, the three boundary
witnesses, and the exact finite-grid sizes are exposed before the run. This is
a pinned confirmation and adversarial audit, not blind discovery.

The verifier must report:

```text
2401 exact Gaussian 2 x 2 matrices in the determinant grid;
69888 exact Gaussian row pairs in the 2 x n Cauchy-Binet grids;
all R1-R3 gates PASS;
all B1-B3 gates PASS;
17 gates and zero failures;
empty stderr;
exit code 0;
final line RESULT PASS.
```

The first formal local run creates `EXPECTED.txt`, `RUN.md` and `RESULT.md`.
The pull-request workflow must then reproduce the exact stdout byte for byte
on clean GitHub-hosted x86_64 and aarch64 Python 3.12 jobs. Until that succeeds,
the probe remains non-canonical and no candidate row is earned.

## Explicit non-claims

This preregistration does not say what quanta ontologically are. It proves a
conditional mathematical statement about a supplied standard-QM pure state.
It does not derive Planck quantization, particles, fields, a Hamiltonian,
space-time separation, measurement settings, outcomes, detector records,
Born frequencies, locality, no-signalling or causal influence from TWIST-J.
Those require separately named typed bridges and, where relevant, empirical
evidence.
