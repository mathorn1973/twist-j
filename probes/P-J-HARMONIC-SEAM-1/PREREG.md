# P-J-HARMONIC-SEAM-1 preregistration

Date: 2026-08-09

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. No formal gate may run before this file and the accepted verifier are
both present at the immutable pin and that pin is pushed and read back from the
public remote.

Public claim lock: issue 307.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v39
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v39
CONTENT_COMMIT: ab17b10412d03bf1cd69791fe22c66252502b2d4
CANON_SHA256:   698df2212f0bc782de2fb50ff04fb4026d1e276743d6fae7f10607cca770b556
CANON_BYTES:    187370
BASE_COMMIT:    2d4ee6956f2da6f8ab23b7471ad7fcd73f787fa1
```

The governing authority is `mathorn1973/twist-j` on `main`. This probe is L1
only. It opens no inter-layer gate.

## Mandatory result-exposure disclosure

A prior NON-CANONICAL conversational/incubation remark,
`REMARK-C-TWOLOGPHI-J-WORD-1_2026-08-09.md`, explored closely related formulas
and executed one-architecture verifiers before its own preregistration text
existed. Freeze-before-execution was not satisfied there.

Every prior run, transcript, hash, finite check, and observed positive or
negative result from that remark is provenance only and is excluded from public
evidence for this probe. The accepted verifier in this directory is separately
authored. Its formal execution count is zero at this preregistration.

## Field 1: equation

### Fixed carrier and notation

```text
K       = Q(z)
z       = zeta_5, z^5 = 1, 1 + z + z^2 + z^3 + z^4 = 0
O       = Z[z]
phi     = -z^2 - z^3 = (1 + sqrt(5))/2
psi     = 1 - phi = -phi^-1
J       = 1 + z^2
mu_10   = {+/- z^k : 0 <= k < 5}
F_0     = 0, F_1 = 1, F_(n+1) = F_n + F_(n-1)
u_n     = F_n phi - F_(n+1), n >= 1
A(x)    = 1 - psi x
H(x)    = SUM_(n>=1) u_n x^n / n, x in mu_10
```

Because `|psi| = phi^-1 < 1`, the power series is absolutely convergent for
every `x in mu_10` and

```text
H(x) = Log(A(x)) = Log(1 - psi x)
```

on the principal archimedean branch. Since `|psi| < 1`, every `A(x)` lies in
the open disk of radius `|psi|` centered at `1`, so the branch cut is not met.

### S1. Integral numerator ladder

For every `n >= 1`,

```text
u_n = -psi^n
    = -F_(n+1) - F_n z^2 - F_n z^3.
```

The proof is not a bounded Fibonacci test. The fixed induction certificate is

```text
u_1 = -psi,
psi phi = -1,
psi (-1) = phi - 1,
```

so multiplication by `psi` carries the coefficient state `(F_n,F_(n+1))` to
`(F_(n+1),F_(n+2))` exactly.

### S2. Distinguished scale and phase reads

```text
H(1)  = log phi,
H(-z) = Log(1 - J) = Log(-z^2) = -i pi/5,
-5 H(-z) = i pi.
```

The second line uses `psi(-z) = J` and the principal representative
`-z^2 = exp(-i pi/5)`.

### S3. Complete real-axis classification on mu_10

For every `x in mu_10`,

```text
H(x) in R  iff  x in {1,-1}.
```

The values are

```text
H(1)  = log phi,
H(-1) = -2 log phi.
```

Proof route: `psi` is nonzero and real, so `A(x)` is real iff `x = bar(x)`.
The only real elements of `mu_10` are `+1` and `-1`. Both landing values are
positive:

```text
A(1)  = phi,
A(-1) = phi^-2 = 2 - phi.
```

Thus principal `Log(A(x))` is real exactly at those two weights.

### S4. Complete imaginary-axis classification on mu_10

For every `x in mu_10`,

```text
Re H(x) = 0  iff  x in {-z,-z^-1}.
```

The values are

```text
H(-z)    = -i pi/5,
H(-z^-1) = +i pi/5.
```

The load-bearing algebra is

```text
A(x) bar(A(x))
  = 1 + psi^2 - psi (x + x^-1),
```

so `|A(x)| = 1` iff `x + x^-1 = psi`. The two displayed weights satisfy that
quadratic exactly. The accepted verifier also exhausts the complete ten-element
set `mu_10` in exact cyclotomic arithmetic. No floating trigonometry or
numerical tolerance is admissible.

### S5. Free-unit and torsion-unit landing

```text
A(1)      = phi,
A(-1)     = phi^-2,
A(-z)     = -z^2,
A(-z^-1)  = -z^3.
```

`-z^2` and `-z^3` have exact order `10`. The arithmetic unit-group statement
used for the reading is

```text
O^x = mu_10 x <phi>.
```

For completeness, the written proof uses only standard number-theory facts
stated here. The roots of unity of `Q(zeta_5)` are `mu_10`. Dirichlet gives unit
rank one. More explicitly, for a unit `e in O^x`, `q=e/bar(e)` is an algebraic
integer all of whose conjugates have modulus one, hence a root of unity by
Kronecker. Reduction modulo `lambda=1-z` gives `q=1 mod lambda`, so among
`mu_10` it lies in `mu_5`. Squaring is bijective on `mu_5`, so choose
`xi in mu_5` with `xi^2=q`. Then `e/xi` is real and is a unit of
`Z[phi]`. The elementary Pell-unit theorem for `Q(sqrt(5))` gives
`Z[phi]^x={+/- phi^m:m in Z}`. Absorb the sign into `mu_10`. Hence every unit
is uniquely torsion times a power of `phi`, up to the evident intersection
`mu_10 cap <phi>={1}`.

The checker audits the exact landing identities and torsion orders. The
unbounded unit-group classification is supplied by the written proof, not by a
finite search.

### S6. Reconstruction of Log J

On the principal branch,

```text
Log J = -H(1) - 2 H(-z)
      = -log phi + 2 pi i/5.
```

This is a reconstruction identity. It does not assert any algebraic dependence
between `pi` and `log phi`; public `LOG-AXES-INDEPENDENCE [T]` is unchanged.

## Field 2: code

Accepted verifier:

```text
probes/P-J-HARMONIC-SEAM-1/verify.py
```

The verifier is Python standard library only. It uses integers, tuples, and
`Fraction`; it forms no `float`, `complex`, decimal approximation, numerical
logarithm, trigonometric value, or external dataset. It represents
`Z[zeta_5]` in the ordered basis `(1,z,z^2,z^3)` and enumerates exactly the ten
weights of `mu_10`.

The verifier is an audit of the written proof. In particular, S1 is certified
by a universal recurrence identity, not by checking finitely many `n`, and S3
and S4 are complete because `mu_10` has exactly ten explicitly enumerated
elements.

## Field 3: carrier or data

Carrier only. No external data.

```text
Z[zeta_5] = Z[X]/(X^4+X^3+X^2+X+1)
mu_10     = {+/- zeta_5^k : 0 <= k < 5}
```

All ring equalities use integer coordinates in the power basis. Principal
branch angles used by the checker are rational multiples of `pi` attached only
after an exact root-of-unity identity has been proved.

## Field 4: systematics and completeness

There is no measurement systematic.

Completeness obligations are frozen as follows:

```text
C1  The cyclotomic reduction rule is exact and z^5=1 is checked.
C2  The ten listed weights are distinct, so the mu_10 enumeration is complete.
C3  S1 is universal by its two basis/recurrence identities, not a finite range.
C4  S3 exhausts all ten weights and proves positivity at the only two real landings.
C5  S4 exhausts all ten weights and independently checks the norm formula.
C6  S5 checks the four landing identities and the two primitive order-10 claims;
    the full unit group is covered by the written theorem proof above.
C7  S6 is exact branch bookkeeping in the basis {log phi, i pi}; no numerical
    transcendental comparison is used.
```

Any hidden input, non-exhaustive replacement for `mu_10`, floating tolerance,
or import of the prior incubation transcript is a STOP condition.

## Field 5: failure threshold and scientific routing

No tolerance exists.

```text
SEAM-PASS
  Every frozen exact gate for S1 through S6 passes and the complete sets are
  exactly
    real-axis weights       {1,-1}
    imaginary-axis weights  {-z,-z^-1}.

MISMATCH
  One exact counterexample in the frozen carrier falsifies any S1 through S6
  statement. The exact witness is printed and preserved.

STOP
  Authority, branch, pin, verifier integrity, completeness, security,
  transcript, or layer discipline fails.
```

`SEAM-PASS` and `MISMATCH` are scientific outcomes and exit zero. `STOP` is an
integrity outcome and exits nonzero. The threshold and scope may not move after
the pin.

## Field 6: action layer

```text
L1 only: cyclotomic integer arithmetic and the principal archimedean evaluation
of algebraic landing points already named in the frozen equation.
```

No L1-to-L2/L3/L4/L5/L6 lift is attempted or owned.

## Scope firewall

This probe does not:

- derive why there are two abelian forces;
- promote `AXIOM-PROJECTION-DICTIONARY [D]`;
- prove `TWO-PLACE-PHYSICS [D]`;
- identify the order-two torsion sign inside `mu_10` with the distinct
  `zeta_8` read place;
- construct a decoder, measure, observer, force, spacetime, or SI bridge;
- strengthen `BOOST-COUNT-LADDER [D]`;
- add a new constant;
- reuse the prior one-architecture remark as evidence.

A later architectural interpretation, if attempted, requires a separately
named claim and layer gate.

## Formal sequence after the pin

1. Read back this file and `verify.py` from the public remote at the immutable
   pin; record commit, SHA-256, and byte counts on issue 307.
2. Only then execute the accepted verifier for the first formal run.
3. Commit exact `EXPECTED.txt`, neutral `RUN.md`, and `RESULT.md` without
   changing the pinned preregistration or verifier.
4. Open one pull request changing only `probes/P-J-HARMONIC-SEAM-1/`.
5. Require GitHub x86_64 and aarch64 jobs to reproduce the same committed
   `EXPECTED.txt` byte for byte before any computation-grade promotion.
6. Any Canon/registry/frontier fold is a later separate reviewed action.
