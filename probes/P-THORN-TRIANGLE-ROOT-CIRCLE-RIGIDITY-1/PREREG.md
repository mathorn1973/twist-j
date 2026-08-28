# P-THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-1 preregistration

Date: 2026-08-28

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count: zero. No
scientific result is earned by this file. The accepted `verify.py` may be read,
parsed, compiled, and inspected statically before the public pin, but it has
not been imported or executed.

Public claim lock: issue #628, opened before this file was committed.

```text
branch:  probe/P-THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-1
path:    probes/P-THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-1/
owner:   A. M. Thorn
mode:    RESULT-EXPOSED, proof-first; the verifier is an exact audit
```

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v68
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v68
TAG_TARGET:     b72505f55bcf2ef3d5985065ae52f3365966f32e
CONTENT_COMMIT: d755c5758406bfed13405dde0864c2ce81f5f581
CANON_SHA256:   63370401c2e25d94e7d8f94bdf142ba32fe3c2a5cdf81d1435114b669b0e5546
CANON_BYTES:    353145
BASE_COMMIT:    37a0fa95e8a49d2a554651545f33975c1c082bd8
ACTION_LAYER:   L1 exact unit-circle and cyclotomic algebra only
```

Immediately before issue lock and branch creation, public `main`, the v68
status, tag, policy, agent manual, Core, Frontier, Registry, Canon, source
probe, promotion package, issues, pull requests, and matching branches were
read from GitHub. The tag, activation commit, content commit, Canon SHA-256,
and byte count agree with `STATUS.md`. The source promotion merge is the
current public `main` displayed above.

This probe changes exactly its own directory. It changes no Canon, Registry,
Frontier, dependency, evidence, gate, workflow, release, decoder, Note, or
existing probe file.

## Collision and prior exposure

No issue, pull request, public branch, probe path, Registry row, Frontier row,
or Note owns either fresh identifier

```text
P-THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-1
THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY
```

at lock time. The collision scan also covered `THORN-TRIANGLE`,
`ROOT-CIRCLE-RIGIDITY`, `PENTAGON-PYTHAGOREAN-CLOSURE`,
`CHORD-SCALE-CLOSURE`, and the displayed polynomial identities.

This probe is `RESULT-EXPOSED`. The algebraic reduction was derived in public
discussion before the pin. That discussion is provenance only. The accepted
verifier is a fresh deterministic standard-library audit and has not been
imported or executed before this pin.

## Adjacent ownership and source pins

The following existing objects retain their exact ownership.

1. `J-PROJECTIONS [T]` owns the principal modulus and argument of the public
   axiom object.
2. `J-MODULUS-CHORD [T]`, `J-RAMIFIED-CHORD [T]`, and `PLENUM-POINT [T]`
   own the public principal chord identities.
3. `CM-ALTERNATING-PENCIL [T]` owns the public alternating pencil, its
   Pfaffian law, and the matrix with polynomial `x^2-3x+1`.
4. `P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1`, issue #625 and merged PR #626,
   owns candidate-T evidence that the same quadratic is the hyperbolic primary
   factor and that the integral primary seam has index five. Its result blob
   is pinned here as
   `60ad9beb89c0c708ca52c4327f865d759e8a96d5`.
5. `PROMO-CM-ALTERNATING-PRIMARY-LATTICE-SEAM`, merged by PR #627, freezes a
   later fold and no current public claim. Its blob is pinned here as
   `42b001e781b68178a29dd5bd5f8e56189d4057a9` and its scope SHA-256 is
   `4350d7f162389982e612565e05ab9e89c2ec772da28b0de56331b0ea1cdb8625`.
6. `BRIDGE-DEFECT [T]` owns its exact scalar identities. This probe does not
   re-earn or physically interpret `script-Q`.
7. `WALL-CIRCLE-LEMMA [T]` concerns logarithm and dilogarithm values on a
   different root-circle construction and does not own the closure below.

The source seam remains candidate-T pending a later Canon fold. This probe may
compare exact source formulas but does not promote or duplicate them.

## Field 1: frozen carrier

Let `z` be any complex number on the unit circle:

```text
z conjugate(z) = 1.
```

Define

```text
J_z = 1 + z^2,
N_z = J_z conjugate(J_z),
S_z = (1-z)(1-conjugate(z)),
t_z = z + conjugate(z).
```

`S_z` is the squared chord `|1-z|^2`. No square root, orientation, root of
unity, order, field, embedding label, or fifth root is assumed. The only
ambient continuum used is the standard complex unit circle already present in
the declared archimedean comparison scope. No statement that the continuum is
a state carrier is made.

## Frozen theorem

The maximum later claim is

```text
THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY [T ceiling; L1]
```

with exactly the following four parts.

### T1. Root-circle rigidity

For every unit-circle `z`, the following are equivalent:

```text
S_z = 1 + N_z,
Phi_5(z) = z^4+z^3+z^2+z+1 = 0,
z has exact order five.
```

The first equality is the full closure condition. It forces the fifth-root
locus and does not assume a root of unity or apply an extremal selector.

### T2. Scale polynomial and branch census

On the equivalent closure locus,

```text
q(N_z) = N_z^2-3N_z+1 = 0,
N_z in {phi^-2, phi^2}.
```

The two roots each occur on one complex-conjugate pair of primitive fifth
roots. The contracting pair is exactly the pair with `N_z=phi^-2`; the
expanding pair has `N_z=phi^2`. No member inside either conjugate pair is
selected.

### T3. Thorn identities

On the same locus,

```text
N_z^-1 = 3-N_z,
S_z + N_z^-1 = 4,
S_z^2 = 5 N_z,
disc(q) = 5.
```

For the principal public branch `z=zeta_5`, the inherited public identities
specialize this to

```text
N_z = J Jbar = phi^-2,
S_z = s_J^2 = 3-phi,
s_J^4 = 5 phi^-2.
```

### T4. Primary-seam agreement

The quadratic `q=x^2-3x+1` is exactly the hyperbolic primary polynomial in the
pinned source seam result. Its discriminant five agrees with that source's
independently computed integral index five. This is an exact cross-source
agreement, not new evidence for the source bases, quotient, projector,
retraction theorem, or physical interpretation.

The public exact rows then permit the derived scalar rewriting

```text
script-Q = 2 pi phi^-2 = s_J^4 (2 pi/5).
```

This line is a consequence of inherited exact definitions and the new
arithmetic identity only. No physical mechanism, action carrier, `h`, `hbar`,
continuum derivation, vacuum theorem, phase law, SI normalization, decoder
field, time orientation, or L2-L6 lift is asserted.

## Written proof

Because `z conjugate(z)=1`, one has `conjugate(z)=z^-1`. Put
`t=t_z`. Then

```text
N_z
 = (1+z^2)(1+z^-2)
 = 2+z^2+z^-2
 = (z+z^-1)^2
 = t^2,

S_z
 = (1-z)(1-z^-1)
 = 2-z-z^-1
 = 2-t.
```

Therefore

```text
S_z = 1+N_z
iff 2-t = 1+t^2
iff t^2+t-1 = 0.
```

Multiplication by the nonzero element `z^2` gives

```text
z^2(t^2+t-1)
 = z^4+z^3+z^2+z+1
 = Phi_5(z).
```

This proves the first equivalence in both directions. The roots of `Phi_5`
are exactly the primitive fifth roots, proving the order statement without a
prior root-of-unity assumption.

On the closure locus, `N=t^2=1-t`, hence `t=1-N`. Substitution into `N=t^2`
gives

```text
N=(1-N)^2,
N^2-3N+1=0.
```

The roots are `(3-sqrt5)/2=phi^-2` and
`(3+sqrt5)/2=phi^2`. Their positive sizes classify the contracting and
expanding conjugate pairs.

The constant term of `q` is one, so

```text
N(3-N)=1,
N^-1=3-N.
```

Since `S=1+N`,

```text
S+N^-1 = 1+N+3-N = 4,
S^2 = (1+N)^2 = 1+2N+N^2 = 5N,
disc(q)=(-3)^2-4=5.
```

The source seam result prints the same `q` and an independently computed
index five. Equality of the displayed integers proves T4 and nothing beyond
its frozen scope.

## Falsifiers

One exact counterexample fires the corresponding part:

1. a unit-circle `z` satisfies `S_z=1+N_z` while `Phi_5(z)` is nonzero;
2. a primitive fifth root fails the closure or has order other than five;
3. `N_z` fails `N^2-3N+1=0`, the branch census is wrong, or one displayed
   inverse, triangle, quartic-chord, or discriminant identity fails;
4. the displayed quadratic differs from the pinned source hyperbolic factor or
   its discriminant differs from the pinned source index;
5. the proof silently assumes a root of unity, selects an orientation or
   `Omega_1`, imports minimality or Hurwitz approximation, strengthens the
   source seam, or attributes a physical, action, vacuum, SI, decoder, or
   L2-L6 conclusion to this row.

A stale authority basis, changed source blob, failed source firewall, altered
pin, nonzero verifier exit, nonempty stderr, stdout mismatch, architecture
disagreement, moved equation, or scope widening is integrity STOP, not a
scientific falsifier.

## Negative controls

The controls are frozen before execution.

```text
B1  primitive third root: t=-1, N=1, S=3. The weaker identity
    S+N^-1=4 holds, but the full closure S=1+N fails. Thus the weaker scalar
    triangle cannot replace T1.

B2  z=i: t=0, J_z=0, N=0, S=2. The closure fails.

B3  z=-1: t=-2, N=4, S=4. The closure fails.

B4  z=(3+4i)/5: |z|=1 exactly, t=6/5, N=36/25, S=4/5, and the closure defect
    S-(1+N)=-41/25 is nonzero; Phi_5(z) is nonzero.

B5  replacing J_z=1+z^2 by 1+z changes the equation and is outside scope.
```

## Verifier contract

The accepted `verify.py` is standard-library only and uses integers,
`Fraction`, exact Laurent polynomials, exact polynomial division, exact
`Q(sqrt5)` pairs, and exact Gaussian rationals. It performs no numerical root
finding, floating point, tolerance test, random search, network access,
subprocess, clock read, or external import.

The written proof carries the universal quantifiers. The verifier audits:

```text
G01 source_scope_firewall
G02 unit_circle_laurent_reduction
G03 closure_equals_phi5
G04 primitive_fifth_order
G05 scale_polynomial
G06 thorn_inverse_and_quartic
G07 quadratic_branch_values
G08 contracting_expanding_census
G09 weaker_triangle_third_root_control
G10 gaussian_rational_controls
G11 primary_seam_agreement
G12 principal_scalar_and_scope_guard
```

Success requires all gates to print `PASS`, then exactly

```text
DECISION THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-CONFIRMED
```

with exit zero and empty stderr. Any other outcome is STOP pending diagnosis;
no equation or threshold may move after the pin.

## Formal run protocol

1. Commit this file and `verify.py` together as the first branch commit.
2. Push the branch and read both files back byte for byte from GitHub.
3. Record the immutable commit and file hashes.
4. Run the clean-interpreter source preflight.
5. Execute the accepted verifier exactly once for the local formal lane.
6. Commit `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing the pinned
   files.
7. Open one pull request changing exactly this probe directory.
8. Require byte-identical GitHub-hosted Python 3.12 x86_64 and native aarch64
   outputs and aggregate `check` success.

No Canon fold, promotion package, action bridge, or physical interpretation is
part of this probe transaction.
