# P-FIELD-ZERO-NONZERO-CUT-1 preregistration

Date: 2026-08-18

Author of record: A. M. Thorn

```text
PREREGISTERED CANDIDATE / RESULT-EXPOSED / PROOF-FIRST /
ZERO FORMAL RUNS / REMOTE PIN AND READBACK REQUIRED BEFORE EXECUTION
```

This file and the accepted verifier are a zero-run pin. They earn no
scientific status. No formal execution may occur until both files are
committed, pushed, and read back byte for byte from the public remote.
`EXPECTED.txt`, `RUN.md`, and `RESULT.md` do not exist at this pin.

Public claim lock: issue
[#412](https://github.com/mathorn1973/twist-j/issues/412), created before this
branch content, prospective pin, accepted verifier, or formal execution. The
issue freezes this probe identifier, branch, path, owner, base, L1 layer,
theorem, audit family, boundary control, and status ceiling.

## 0. Authority, base, and chronology

```text
STATE:          ACTIVE
CANON:          Public Canon v50
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v50
CONTENT_COMMIT: b68c60c57cfd0b1e655b6fc4d5496a333a249fdf
CANON_SHA256:   f99f5eeb42db3e9d40bc6a46f716aa98d7af1925b66989406e0b3671ab43a9fe
CANON_BYTES:    240724
BASE_COMMIT:    8359889ebac9ef85e05d4abe4d676c731b880167
BRANCH:         probe/P-FIELD-ZERO-NONZERO-CUT-1
PATH:           probes/P-FIELD-ZERO-NONZERO-CUT-1/
LAYER:          L1 field and Boolean algebra only
```

The theorem and its proof were exposed before the prospective pin. This is a
confirmatory, proof-first probe, not blind discovery. The proposed status
rests on the field-independent written proof below. The finite-field program
is an exact audit of the statement and its zero-boundary systematics; it is not
the logical source of the universal quantifier.

Before the pin, `verify.py` has been reviewed only as source and checked with
Python's syntax-only bytecode compiler. It has not been executed or imported,
and no scientific stdout has been produced from it. Any earlier informal
enumeration or discussion is discovery context only and is excluded from
formal evidence.

## 1. Six frozen preregistration fields

### 1.1 Equation

Let `F` be a field, let

```text
empty != A proper-subset F,
d_A = 1_A : F -> {0,1},
B : {0,1} x {0,1} -> {0,1}.
```

The frozen equation is

```text
d_A(xy) = B(d_A(x), d_A(y))             for every x,y in F.       (E)
```

`B` is one total Boolean table with four entries. It is not allowed to depend
on `x`, `y`, an element representative, or any datum other than the two input
bits.

### 1.2 Code

The accepted verifier is exactly `verify.py` in this directory. It uses only
integer arithmetic, tuples, lists, and `itertools.product` from the Python
standard library. It contains no floating point, randomness, external data,
network access, clock access, environment-dependent ordering, or fitted
threshold.

### 1.3 Carrier and audit data

The theorem carrier is an arbitrary field, finite or infinite, of arbitrary
characteristic. The exact finite audit uses these eight fields:

```text
F_2, F_3, F_4, F_5, F_7, F_8, F_9, F_11.
```

Prime fields use arithmetic modulo `p`. The extension fields use low-first
polynomial coordinates and the following monic moduli:

```text
F_4 = F_2[t]/(t^2 + t + 1),
F_8 = F_2[t]/(t^3 + t + 1),
F_9 = F_3[t]/(t^2 + 1).
```

The verifier exhaustively checks the field axioms on every displayed finite
carrier before using it. For every field it then tests all `2^|F|-2`
nonempty proper subsets and all sixteen Boolean tables against every ordered
pair `(x,y)`.

The separate boundary carrier is `F_5^x={1,2,3,4}` with zero removed. It is a
control only and is not an instance of the theorem's total carrier.

### 1.4 Systematics and exclusions

1. `d_A` is the indicator of the oriented subset `A`. Replacing `A` by its
   complement changes both the orientation and the Boolean table.
2. Zero belongs to the quantified carrier and both variables range over the
   whole field. Restriction to `F^x` is a different problem.
3. `A` is nonempty and proper, so both bit values are attained.
4. The field hypothesis is essential: multiplication by a nonzero element is
   bijective. Rings with zero divisors, partial multiplication, semigroups,
   and tagged exceptional values are outside the theorem.
5. Equation (E) is pointwise and total. Almost-everywhere equality, sampled
   equality, finite windows, probabilities, and measures are excluded.
6. The theorem classifies two-cell multiplicative quotients only. It does not
   select a field, a cut, a physical interpretation, or a decoder.
7. The finite audit is deliberately redundant across prime and nonprime
   fields. Agreement of those examples does not replace the universal proof.
8. The `F_5^x` control changes the domain by deleting zero. Its additional
   quadratic-character cuts do not contradict the theorem.

### 1.5 Failure threshold

There is no numerical tolerance. One exact counterexample to the universal
statement fires the theorem. In the audit, one failed field axiom, one missing
or extra accepted `(A,B)` pair, one incorrect Boolean table, or one failed
`F_5^x` boundary count fires the corresponding finite certificate.

### 1.6 Action layer

The action is entirely at L1: field multiplication and a Boolean quotient.
There is no map to L2 geometry, L3 boundary data, L4 support dynamics, an L5
stream, or an L6 measure.

## 2. Frozen theorem candidate

Proposed public row: `FIELD-ZERO-NONZERO-MULTIPLICATIVE-CUT [T]`.

**Theorem.** Let `F` be any field and let `empty != A proper-subset F`. A
Boolean operation `B` satisfies (E) if and only if exactly one of the following
oriented cases holds:

```text
A = {0},    B = OR;
A = F^x,    B = AND.
```

In particular, `B` is unique once `A` is fixed.

### Complete field-independent proof

Put

```text
epsilon = d_A(0).
```

Because `A` is nonempty and proper, `d_A` attains both zero and one. For each
attained bit `b`, choose `y` with `d_A(y)=b`. Since `0y=0`, equation (E) gives

```text
B(epsilon,b)=epsilon                         for b=0,1.     (1)
```

Suppose that a nonzero `u` had `d_A(u)=epsilon`. Then for every `y`, (1) gives

```text
d_A(uy)=B(epsilon,d_A(y))=epsilon.                         (2)
```

Multiplication by nonzero `u` is a bijection of the field. As `y` ranges over
`F`, so does `uy`; equation (2) would therefore make `d_A` constant. This
contradicts the assumption that `A` is nonempty and proper. Hence

```text
d_A(u)=1-epsilon for every u != 0.                         (3)
```

If `epsilon=1`, equations (3) and the definition of `epsilon` give `A={0}`.
The four input-bit pairs are all realized by choosing zero or nonzero factors,
and the product is zero exactly when at least one factor is zero. Thus the
entire table is uniquely `OR`.

If `epsilon=0`, equation (3) gives `A=F^x`. Again all four input-bit pairs are
realized, and a product is nonzero exactly when both factors are nonzero. Thus
the entire table is uniquely `AND`.

Conversely, a field has no zero divisors, so

```text
1_{ {0} }(xy) = OR(1_{ {0} }(x),1_{ {0} }(y)),
1_{ F^x }(xy) = AND(1_{ F^x }(x),1_{ F^x }(y)).
```

Both displayed cases satisfy (E). This proves both directions and uniqueness.

## 3. Frozen exact finite audit

For a field of order `q`, the verifier must find exactly the following two
solutions among `(2^q-2)*16` candidate pairs:

```text
mask(A={0}),       table OR  = 1110_2;
mask(A=F^x),       table AND = 1000_2.
```

Table bits are ordered by inputs `00,01,10,11`, with the output for `00` the
least significant bit. The exhaustive subset counts are frozen as

```text
F_2:     2       F_3:     6       F_4:    14       F_5:    30
F_7:   126       F_8:   254       F_9:   510       F_11: 2046.
```

Before the cut audit, the verifier checks addition, multiplication,
associativity, commutativity, distributivity, identities, additive inverses,
and unique multiplicative inverses for every displayed finite carrier.

## 4. Frozen zero-boundary control

On the changed carrier `F_5^x`, let

```text
QR  = {1,4},
NQR = {2,3}.
```

Exhausting all fourteen nonempty proper subsets and all sixteen Boolean tables
must give exactly

```text
A=QR,   B=XNOR;
A=NQR,  B=XOR.
```

This is the oriented quadratic-character quotient of the multiplicative group.
It shows exactly why totality at zero is material: after zero is deleted, a
nontrivial unit-group character survives. It makes no five-selection claim;
other multiplicative groups may have their own quotients.

## 5. QDD cross-reference firewall

Public Canon v50 already has the tagged matter-record branch
`ZERO_SUPPORT | SUPPORTED` in `DEF-QDD-MATTER-RECORD` and keeps
`QUADRATIC-DECODER-DATA [O]` at `ROOT / STOP / FORMAL`.

The proposed theorem is field-independent L1 algebra. Its agreement in shape
with a zero/nonzero support branch is a cross-reference only. This probe:

- does not assert that the QDD record map obeys equation (E);
- does not define a QDD composition law or add a dependency edge;
- does not define the QDD coefficient carrier, quadratic pair, factor map,
  effect pair, Born pairing, density, normalized weight, or write map;
- does not prove an L5 event stream or L6 measure;
- does not alter `QDD-ALGEBRAIC-FACTORIZATION [T]`,
  `QDD-QCARRIER-DIAGONAL-BOUNDARY [T]`, or any apparatus row; and
- does not move, narrow, or close `QUADRATIC-DECODER-DATA [O]`.

The `F_5^x` boundary control is not a replacement QDD domain. Deleting zero
would remove the very totality boundary classified by this theorem.

## 6. Frozen falsifiers

`X1 UNIVERSAL-COUNTEREXAMPLE`
: A field `F`, nonempty proper `A`, and total Boolean `B` satisfy (E), while
  `(A,B)` is neither `({0},OR)` nor `(F^x,AND)`.

`X2 MISSING-ORIENTED-CUT`
: Either displayed oriented cut fails equation (E) in a field.

`X3 NONUNIQUE-TABLE`
: One of the two displayed subsets admits a second total Boolean table.

`X4 ZERO-STEP`
: Equation `0y=0` fails to force `B(epsilon,b)=epsilon` for both attained
  colors under the frozen hypotheses.

`X5 BIJECTION-STEP`
: A nonzero field element fails to act bijectively by multiplication.

`X6 FINITE-FIELD-CARRIER`
: Any advertised finite carrier fails one checked field axiom or has an order
  different from its label.

`X7 FINITE-AUDIT-COUNT`
: Any of `F_2,F_3,F_4,F_5,F_7,F_8,F_9,F_11` returns other than exactly the two
  frozen oriented solutions.

`X8 F5-UNIT-BOUNDARY`
: The `F_5^x` control returns anything other than the two oriented
  `QR/XNOR` and `NQR/XOR` solutions.

Changing the carrier, deleting zero, admitting a partial Boolean table, or
moving to a ring is a scope change, not a falsifier of the frozen theorem.

## 7. Status ceiling and next permitted action

The complete proof may support exactly
`FIELD-ZERO-NONZERO-MULTIPLICATIVE-CUT [T]` after the zero-run pin, public
readback, formal audit, reviewed result, and separate Canon fold. The verifier
is then an audit of a proof-first theorem.

This probe cannot earn a stronger status, a field-selection theorem, a
five-specific theorem, a physical support law, a decoder-completion result, a
composition law for any existing record class, or an L2-L6 lift. It causes no
QDD or frontier status move.

The only next permitted action after this zero-run construction is static
review, then a named commit and public remote readback of these two files.
Formal execution remains forbidden until that readback succeeds.
