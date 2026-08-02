# Algebraic seed contract

Status: **NON-CANONICAL MANUAL LABORATORY ONLY**.

This contract is frozen against active Public Canon v32 at activation commit
`f8c4cc64ba4fc21723fc3e715b5a40036ef7b404`.  It changes no Canon, registry,
frontier, dependency ledger, evidence ledger, release metadata, claim status,
or claim scope.

Lean's `def J` constructs a term.  It does not formalize or prove the Canon's
ontological adoption of that term as the generator of reality.  A successful
build or `#print axioms` result is a manual review aid only.  It is not a
probe, reproduction, primary evidence, or `A-LEAN-*` audit and creates no
public status.

## Purpose of this cut

This branch formalizes the algebraic seed in parallel with, and independently
of, the counter/no-return laboratory.  The two branches have no import edge.
In particular, this work does not derive the Public Canon v32 architecture
from `J`; v32 explicitly declares that architecture separately.

The first concrete carrier is integer-native.  It has four named integer
coordinates in the ordered basis

```text
1, j, j^2, j^3
```

and multiplication reduces

```text
j^4 = -(1 + j + j^2 + j^3).
```

The explicit construction keeps the first cut below Mathlib's number-field,
Galois, and archimedean machinery.  Two different identification obligations
must not be conflated:

1. The mathematical presentation is mandatory now.  The carrier is freely
   represented by four integer coordinates; this cut checks that `1`, `j`,
   `j^2`, and `j^3` are the four coordinate vectors, then proves both
   `j^5 = 1` and `1 + j + j^2 + j^3 + j^4 = 0` from the multiplication table.
   Those theorems are falsifiers for a mistyped table, not deferred promises.
2. The formal identification and transport theorem is deferred: an explicit
   `RingEquiv` with `AdjoinRoot (Polynomial.cyclotomic 5 ℤ)`, preservation of
   `j`, `J`, `phi`, and the ordered basis under that equivalence, followed if
   needed by fraction-field/scalar extension to a concrete number field.  The
   transported regular norm and trace must then be proved equal to the field
   norm and trace.  Those theorems must exist before code using Mathlib's
   cyclotomic or field APIs can identify the types or invariants by rewriting.

## Two layers

### General root data

```lean
structure FifthRootData (K : Type*) [CommRing K] where
  ζ : K
  primitive : IsPrimitiveRoot ζ 5

def FifthRootData.J (A : FifthRootData K) : K :=
  1 + A.ζ ^ 2
```

At this layer the present cut proves only definitional consequences that use
the fifth-power law, notably

```text
(J - 1)^3 = ζ.
```

It does not attach a trace, norm, conjugation, positive real embedding, or
number-field structure to an arbitrary commutative ring.  In particular,
exact order five alone does not allow cancellation of
`(ζ - 1) * Φ₅(ζ) = 0` in a ring with zero divisors.

### Concrete integer home

`CyclotomicFiveInt` is a structure with four `ℤ` fields.  Addition, negation,
zero, one, multiplication, natural and integer scalar multiplication, and
natural and integer casts are explicit.  The additive group and `CommRing`
laws are proved from the coordinate formulas.  No project axiom or theorem
field is used to manufacture the ring laws.

The concrete definitions are

```text
j   = (0, 1,  0,  0)
J   = (1, 0,  1,  0) = 1 + j^2
phi = (0, 0, -1, -1) = -(j^2 + j^3).
```

The present target theorems are:

```text
1 + j + j^2 + j^3 + j^4 = 0
j^5 = 1, with j primitive of exact order five
(J - 1)^3 = j
phi^2 = phi + 1
J * phi = j
J^5 * phi^5 = 1
J^5 = (-8, 0, -5, -5), hence J^5 != 1
M_J^5 != I
J * (a,b,c,d) = (a-c+d, b-c, a, b-c+d)
det(M_J) = 1
trace(M_J) = 3.
```

The code names the determinant and trace of the regular multiplication matrix
`regularNorm` and `regularTrace`.  These names have Lean scope only in the
explicit four-component cyclotomic presentation defined here.  The first cut
does not identify them with Mathlib's field norm and field trace on a
constructed `Q(zeta_5)`.  Writing the proved result as an unqualified field
statement `N(J) = 1` or `Tr(J) = 3` would therefore exceed the formal scope.

## Matrix convention

Images of the ordered basis vectors are columns, so

```text
      [ 1  0 -1  1 ]
M_J = [ 0  1 -1  0 ]
      [ 1  0  0  0 ]
      [ 0  1 -1  1 ].
```

Thus matrix-vector multiplication agrees with the displayed Canon action.
The theorem checks this convention for an arbitrary four-coordinate input,
not only for a finite list of examples.

## Dependency firewall

The only project import chain is

```text
FifthRootData
      ↓
IntegralCarrier
      ↓
JArithmetic
      ↓
Audit
```

The Lake target admits only `TwistJ.AlgebraicSeed.+`.  This project must not
import any of:

```text
TwistJ.Foundation.*
TwistJ.Architecture.*
TwistJ.Models.*
TwistJ.Observation.*
TwistJ.Decoder.*
TwistJ.Dictionary.*
```

It also has no path dependency, symlink, shared sibling package directory, or
ambient `LEAN_PATH` dependency.  The toolchain and all Lake package revisions
are committed locally to this notes directory.

## Public-scope translation

The exact arithmetic is intended as a status-neutral formal precursor for the
already published v32 rows `J-GOLDEN-BRIDGE [T]` and `J-STEP [T]`, and only as
a partial algebraic precursor for the norm/trace clauses of `J-UNIT [T]`.  It
is not an audit of the complete `J-UNIT` statement.  The Lean theorem scope in
this cut is exactly "in the explicit four-component cyclotomic presentation as
defined."  The proved cyclotomic relation, fifth-power law, and free
coordinates supply the mathematical presentation check.  Before any later
public audit can cite the code at the Canon's literal `Z[zeta_5]` or
`Q(zeta_5)` scope, an independent review must also approve the translation and
the formal `AdjoinRoot`, fraction-field, and invariant-transport equivalences.
This notes branch does not perform that governance step.

The following distinctions are mandatory:

- `M_J` is multiplication by `J`; it is not the public autonomous update `U`.
- The exact order-five element is `j`, not `J`.
- `J^5 * phi^5 = 1` is proved in the ring; inverse notation belongs only after
  an appropriate unit or field layer is supplied.
- `regularNorm J = 1` is not the complex relative identity
  `J * conjugate(J) = phi^-2`.
- The algebraic element `phi` is not yet a proof of positivity or the selected
  principal archimedean embedding.
- Matrix iteration is not a time variable, a clock, or a derivation of the
  counter-checkpoint architecture.

## Excluded from this cut

- `Li_1`, `Li_2`, principal logarithms, or any polylogarithmic bridge;
- archimedean modulus and argument;
- the formal `AdjoinRoot Φ₅` ring equivalence, Mathlib
  `IsCyclotomicExtension`, a concrete number field, or Galois theory;
- conjugation and the golden fixed subring as structured objects;
- units, inverses, and a proof of `J^5 = phi^-5` in inverse notation;
- commutators, the public selector update, decoder, dictionary, observer, or
  physical-space reading;
- Canon, registry, policy, workflow, or evidence changes.

These omissions are scope boundaries, not failed theorems.
