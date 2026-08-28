# P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1 preregistration

Date: 2026-08-28

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count: zero. No
scientific result is earned by this file. The accepted `verify.py` may be read,
parsed, compiled, and inspected statically before the immutable public pin, but
it has not been imported or executed.

Public claim lock: issue #630, opened before this file was committed.

```text
branch:  probe/P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1
path:    probes/P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1/
owner:   A. M. Thorn
mode:    RESULT-EXPOSED, proof-first; verifier is an exact audit
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
BASE_COMMIT:    920ff60a8b4d92ec0eebc49832a38adca692eb00
ACTION_LAYER:   L1 exact unit-circle and cyclotomic algebra only
```

Immediately before issue lock and branch creation, public `main`, all matching
issues, pull requests and public branches, `STATUS.md`, `POLICY.md`,
`AGENTS.md`, `canon/CORE.md`, `canon/FRONTIER.md`, `canon/REGISTRY.tsv`, the
Canon, the source seam probe, its promotion package, and the abandoned
predecessor were read from GitHub. The annotated v68 tag, activation commit,
content commit, Canon SHA-256, and Canon byte count agree with `STATUS.md`.
The current public base is the merge commit displayed above.

This probe changes exactly its own directory. It changes no Canon, Registry,
Frontier, dependency, evidence, gate, workflow, release, decoder, Note, or
existing probe file.

## Consumed predecessor

`P-THORN-TRIANGLE-ROOT-CIRCLE-RIGIDITY-1`, issue #628 and merged PR #629,
is closed with exactly

```text
Status: ABANDONED.
```

Its formal gate never ran. Its accepted verifier required the whole
353145-byte Canon blob as a local runtime fixture that the owning session could
not materialize without changing the pin or using an unattached snapshot. It
created no `EXPECTED.txt`, no `RUN.md`, no scientific result, and no evidence.
Its identifier is consumed and must not be reused or resumed.

This successor keeps the already exposed equation and falsifiers, but uses a
fresh issue, fresh identifier, fresh verifier, and fresh immutable pin. The new
verifier is self-contained and does not read, import, amend, or execute the
abandoned verifier.

## Collision and adjacent ownership

No issue other than the fresh lock, pull request, public branch, probe path,
Registry row, Frontier row, or Note owns either

```text
P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1
THORN-TRIANGLE-PENTAGON-RIGIDITY
```

at lock time. The collision scan also covered `THORN-TRIANGLE`,
`PENTAGON-RIGIDITY`, `DOUBLE-RIGHT-TRIANGLE`, `ROOT-CIRCLE-CLOSURE`, and the
formulas below.

Existing public objects retain their exact ownership.

1. `J-PROJECTIONS [T]` owns the principal modulus and argument of the public
   axiom object.
2. `J-MODULUS-CHORD [T]`, `J-RAMIFIED-CHORD [T]`, and `PLENUM-POINT [T]` own
   the public principal chord identities.
3. `CM-ALTERNATING-PENCIL [T]` owns its alternating pencil, Pfaffian law, and
   the matrix with characteristic polynomial `x^2-3x+1`.
4. `P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1` and
   `PROMO-CM-ALTERNATING-PRIMARY-LATTICE-SEAM` own only their exact
   candidate-T source package. This probe does not strengthen, promote, or
   re-earn its primary split, index, quotient, projector, or retraction result.
5. `BRIDGE-DEFECT [T]` owns its existing scalar definitions. It is not a
   mechanism input to this proof.
6. `WALL-CIRCLE-LEMMA [T]` concerns logarithm and dilogarithm values on a
   different root-circle construction and does not own the closure below.

This probe is `RESULT-EXPOSED`: its target reduction was derived in public
conversation before the pin. That discussion is provenance only. The written
proof below carries the universal theorem. The accepted verifier is a fresh
exact audit and has execution count zero before the pin.

## Field 1: carrier

Let `z` be any complex unit-circle point:

```text
z conjugate(z) = 1.
```

Define

```text
J_z = 1 + z^2,
N_z = J_z conjugate(J_z),
S_z = (1-z)(1-conjugate(z)) = |1-z|^2,
t_z = z + conjugate(z).
```

`S_z` is the squared chord. No square root, root-of-unity assumption, order,
orientation, fifth root, field, embedding label, minimum, or Hurwitz premise
is admitted. The standard complex unit circle is the declared L1 comparison
carrier; no continuum-as-state or physical continuum claim is made.

## Frozen theorem

The maximum later claim is

```text
THORN-TRIANGLE-PENTAGON-RIGIDITY [T ceiling; L1]
```

with exactly the following four parts.

### T1. Full closure forces the pentagon

For every unit-circle `z`, the following are equivalent:

```text
S_z = 1 + N_z,
Phi_5(z) = z^4+z^3+z^2+z+1 = 0,
z has exact order five.
```

The first equality is the full Thorn closure. It forces the fifth-root locus
without assuming any root of unity and without an extremal selector.

### T2. Scale polynomial and branch census

On the equivalent closure locus,

```text
N_z^2-3N_z+1 = 0,
N_z in {phi^-2, phi^2}.
```

The contracting conjugate pair has `N_z=phi^-2`; the expanding conjugate pair
has `N_z=phi^2`. The theorem selects neither orientation within either pair.

### T3. Double-right-triangle identities

On the same locus,

```text
N_z^-1 = 3-N_z,
S_z + N_z^-1 = 4,
S_z^2 = 5 N_z,
disc(x^2-3x+1) = 5.
```

Equivalently, writing `rho^2=N_z` and `s^2=S_z`, the two exact squared-leg
relations are

```text
1 + rho^2 = s^2,
s^2 + rho^-2 = 2^2.
```

The weaker second relation alone is not a selector; the primitive-third-root
control below satisfies it while failing the full first relation.

### T4. Principal public specialization

For the principal public branch `z=zeta_5`, inherited public identities give

```text
N_z = J Jbar = phi^-2,
S_z = s_J^2 = 3-phi,
s_J^4 = 5 phi^-2.
```

The last line is the literal golden ramified chord squared. The exact source
seam independently carries the same quadratic `x^2-3x+1` and an integral
index five; this agreement is a cross-reference only and supplies no extra
claim or evidence here.

The existing public scalar definitions permit the derived rewriting

```text
script-Q = 2 pi phi^-2 = s_J^4 (2 pi/5).
```

No physical mechanism, action carrier, vacuum theorem, phase law, `h`,
`hbar`, SI scale, decoder field, time orientation, continuum derivation, or
L2-L6 lift is asserted.

## Written proof

Unit modulus gives `conjugate(z)=z^-1`. Put `t=t_z`. Then

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
S_z=1+N_z
iff 2-t=1+t^2
iff t^2+t-1=0.
```

Multiplying by the nonzero element `z^2` gives exactly

```text
z^2(t^2+t-1)
 = z^4+z^3+z^2+z+1
 = Phi_5(z).
```

This proves the first equivalence in both directions. The roots of `Phi_5`
are exactly the primitive fifth roots, proving the order statement without a
root-of-unity premise.

On the closure locus, `N=t^2=1-t`, hence `t=1-N`. Substitution into `N=t^2`
gives

```text
N=(1-N)^2,
N^2-3N+1=0.
```

Its roots are `(3-sqrt5)/2=phi^-2` and `(3+sqrt5)/2=phi^2`. The signs of the
corresponding traces classify the two conjugate pairs as contracting and
expanding without selecting orientation.

The constant term of the quadratic is one, so

```text
N(3-N)=1,
N^-1=3-N.
```

Together with `S=1+N` this gives

```text
S+N^-1=1+N+3-N=4,
S^2=(1+N)^2=1+2N+N^2=5N,
disc(N^2-3N+1)=9-4=5.
```

The public specialization follows by substituting the already registered
principal values and creates no new physical reading.

## Falsifiers

One exact counterexample fires the corresponding part:

1. a unit-circle `z` satisfies `S_z=1+N_z` while `Phi_5(z)` is nonzero;
2. a primitive fifth root fails the closure or has order other than five;
3. the scale polynomial, branch census, inverse identity, weak triangle,
   quartic chord, discriminant, or principal specialization is false;
4. the proof silently assumes a root of unity, selects an orientation or
   `Omega_1`, imports minimality or Hurwitz approximation, strengthens the
   source seam, or attributes any physical, action, vacuum, SI, decoder,
   continuum-as-state, or L2-L6 conclusion to the row.

A stale authority basis, changed pin, nonzero verifier exit, nonempty stderr,
stdout mismatch, architecture disagreement, moved equation, or scope widening
is integrity STOP, not a scientific falsifier.

## Frozen controls

```text
B1  primitive third root: t=-1, N=1, S=3. The weaker identity
    S+N^-1=4 holds, but the full closure S=1+N fails.

B2  z=i: J_z=0, N=0, S=2. The closure fails.

B3  z=-1: N=4, S=4. The closure fails.

B4  z=(3+4i)/5: |z|=1 exactly, N=36/25, S=4/5, and
    S-(1+N)=-41/25; Phi_5(z) is nonzero.

B5  replacing J_z=1+z^2 by 1+z changes the equation and is outside scope.
```

## Verifier contract

The accepted `verify.py` is standard-library only. It uses integers,
`Fraction`, exact ordinary and Laurent polynomials, exact `Q(sqrt5)` pairs,
and exact Gaussian rationals. It performs no floating-point operation,
tolerance test, numerical root finding, random search, network access,
subprocess, clock read, or external source-file import.

The written proof carries the universal theorem. The verifier audits:

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
G11 principal_golden_chord_square
G12 scope_and_nonselection_guard
```

Success requires all gates to print `PASS`, followed exactly by

```text
DECISION THORN-TRIANGLE-PENTAGON-RIGIDITY-CONFIRMED
```

with exit zero and empty stderr. Any other outcome is STOP pending diagnosis;
no equation, threshold, or scope may move after the pin.

## Formal run protocol

1. Commit this file and `verify.py` together as the first branch commit.
2. Push and read both files byte-identically from GitHub.
3. Record the immutable commit and hashes.
4. Run the accepted verifier once in the local formal lane.
5. Commit `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing the pin.
6. Open one pull request changing exactly this probe directory.
7. Require byte-identical GitHub-hosted Python 3.12 x86_64 and native aarch64
   output plus aggregate `check` success.

No Canon fold, promotion package, action bridge, or physical interpretation is
part of this probe transaction.
