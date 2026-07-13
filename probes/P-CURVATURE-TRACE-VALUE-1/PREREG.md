# P-CURVATURE-TRACE-VALUE-1 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete decision surface for the first public
attack on `CURVATURE-TRACE-VALUE`. It contains no gate output and earns no
scientific status. Formal execution is forbidden until this document and the
accepted verifier pass reciprocal byte review, are committed, are pushed as
one immutable preregistration pin, and that remote pin is read back.

## Public identity and action layer

- Claim: `CURVATURE-TRACE-VALUE` [O]
- Public lock: issue 17
- Owner: master C session
- Branch: `probe/P-CURVATURE-TRACE-VALUE-1`
- Path: `probes/P-CURVATURE-TRACE-VALUE-1/`
- Initial base: `f9aac76ac9b1355fe45b9d675de7a8ec40cc9588`
- Action layer: L2, discrete geometric operator on the full checkpoint
  manifold

Pinned owner ruling, the definitional source of every term below:

```text
ruling merge SHA:  f9aac76ac9b1355fe45b9d675de7a8ec40cc9588
ruling file:       notes/canon/P-CURVATURE-TRACE-RULING-1.md
ruling SHA-256:    cf15037f5cc2690a9633ca68ef13107920ce9ce81116963dc9d8490c088eeccb
ruling size:       15496 bytes, 497 lines
```

No boundary, representation, golden block, physical decoder, continuum
curvature, or canonical-operator selection is included. Each would require a
separately named lift or probe.

## Equation

Work over the state carrier

```text
X = F_5^6,
x = (p1,p4,p1p,p4p,q,r),
F = Q^X.
```

All state arithmetic is modulo 5. Freeze the five public affine involutions:

```text
a(p1,p4,p1p,p4p,q,r) = (p4,p1,p4p,p1p,q,r)

b(p1,p4,p1p,p4p,q,r) = (-p1p,-p4p,-p1,-p4,-q,-r)

c: piston -> b4(piston) + (2,1,2,1) + r(0,1,0,-1)
   q       -> 1-q
   r       -> -r

d(x) = (2,1,3,4,1,1) - x
e(x) = (2,1,3,4,2,1) - x.
```

For affine maps, `(g o h)(x) = g(h(x))`. The Koopman convention and product
law are

```text
(T_g f)(x) = f(g^-1 x),
T_g T_h = T_(g o h).
```

Define exactly

```text
C0  = T_a T_c - T_c T_a
    = T_(a o c) - T_(c o a),

H   = <b,d>,
R_H = (1/20) sum_{h in H} T_h,

Pi_1(f) = (1/|X|) (sum_{x in X} f(x)) 1_X,
P0      = I - Pi_1,
P       = P0 R_H = R_H P0,

V       = im(P) = F^H intersect 1_X^perp,
K       = (P C0 P)|_V : V -> V,
kappa   = Tr_V(K^2).
```

The trace is the ordinary operator trace induced by the counting inner
product on `F`. There is no division by dimension, rescaling, fitted scalar,
metric weight, or other normalization. Since `C0` kills constants on both
sides and is skew-adjoint,

```text
kappa = Tr_F((P C0 P)^2) = Tr_F(R_H C0 R_H C0).
```

The map `e` is an integrity-only public generator. It does not enter `H`,
`K`, `kappa`, or the scientific comparison; failure of its involution check
is `STOP`.

## Carrier and exact arithmetic

The complete finite carrier is all `5^6 = 15625` states, ordered
lexicographically. Define `x ~_H y` exactly when `y = h(x)` for some `h` in
`H`. The verifier derives rather than assumes

```text
|H| = 20,
X/H = 1 orbit of size 5, 74 orbits of size 10,
      and 744 orbits of size 20,
dim F^H = 819,
dim V = rank(P) = 818.
```

Every affine map is represented by a `6 x 6` integer matrix and a length-six
translation vector modulo 5. Every rational quantity uses
`fractions.Fraction`. Fixed-point counts use exact Gaussian elimination over
`F_5`. Floating point, tolerance, sampling, randomness, timestamps,
external data, and external packages are forbidden.

## Pinned restriction-failure witness

Let

```text
O0 = H . (0,0,0,0,0,0),
x  = (0,0,1,3,0,1),
y  = (2,1,2,1,1,0).
```

The verifier must reconstruct and check

```text
x ~_H y,
C0 1_O0(x) = 0,
C0 1_O0(y) = -1.
```

This proves that raw `C0` does not preserve `F^H` and that compression, not
restriction, is the typed operator. Any witness failure is `STOP`.

## Code and independent exact routes

The accepted code is `verify.py` in this directory. It performs two exact
trace computations whose principal algorithms are independent.

### Route A: orbit incidence

Enumerate every `H`-orbit in least-state lexicographic order. For orbit
`O_i` of size `s_i`, define

```text
m_ij = #{x in O_j : (a o c)x in O_i}
       - #{x in O_j : (c o a)x in O_i}.
```

The verifier checks `m_ji = -m_ij` entry by entry, checks both row and column
sums are zero so the constant direction is killed on both sides, and computes
directly

```text
kappa_A = - sum_{i,j} m_ij^2 / (s_i s_j)
```

as a `Fraction`. Normalized orbit indicators form a basis of `F^H`; its
constant direction is annihilated by `K`, so the same trace is the trace on
`V`. No square root enters the arithmetic.

### Route B: Reynolds group words

Independently expand

```text
kappa_B = (1/400) sum_{h,k in H} Tr(T_h C0 T_k C0).
```

For each ordered pair `(h,k)`, expand all four signed affine words. The trace
of each Koopman permutation is the exact fixed-point count of its affine map.
Count those fixed points by solving `(A-I)x = -v` over `F_5`. This route must
not read the orbit labels, the incidence matrix, any Route A subtotal, or any
stored exploratory result.

Both routes may share only the public generator definitions, affine
composition, and exact construction of `H`. Exact equality
`kappa_A = kappa_B` is an integrity gate before either value is compared with
the historical proposal.

## Integrity and completeness certificates

The verifier must check and print the exact thirteen gates of the public
ruling, in the same order and with the same meaning:

1. `I1`: all 15625 states; exact public `a,b,c,d,e`; five involutions;
2. `I2`: affine composition and the Koopman product convention;
3. `I3`: `|H| = 20`, group closure, exact action, and complete orbit census;
4. `I4`: commuting Reynolds and traceless projectors, invariant dimension
   819, and `rank(P) = 818`;
5. `I5`: pinned witness W and raw-restriction failure;
6. `I6`: `C0* = -C0`, constant annihilation on both sides, and the
   compression identities;
7. `I7`: `K` is a total endomorphism of `V` and is skew-adjoint there;
8. `I8`: Route A has complete skew incidence and an exact `Fraction` trace;
9. `I9`: Route B has exactly `20^2 x 4 = 1600` exact fixed-point terms and
   an exact `Fraction` trace;
10. `I10`: exact Route A/Route B agreement before threshold comparison;
11. `I11`: separate historical checksum `-22` and degree-ten polynomial,
    without asserting that spectrum for `K`;
12. `I12`: integer/Fraction exactness and standard-library-only discipline;
13. `I13`: deterministic total ordering, fixed stdout, complete tally, and
    audit-before-decision precedence.

The orbit census, skew-incidence test, complete word expansion, fixed-point
rank consistency, witness, and route equality are completeness certificates.
They are not substitute predicates and must all precede decision routing.

## Prior knowledge disclosure

Before this preregistration, a non-canonical exact exploratory audit printed

```text
historical printed-spectrum checksum     -22
raw full-space commutator trace           -31250
<b,d> Reynolds compression                -881/8
<b,d,e> Reynolds compression              -181/8.
```

These are disclosed prior knowledge, not formal evidence, predictions, or
pass thresholds. In particular, the verifier must not contain an assertion
that `kappa` equals `-881/8` or any other exploratory trace. It computes both
routes independently, checks only their exact agreement and the structural
gates, and then applies the frozen scientific comparison.

## Failure threshold and scientific routing

The registered historical proposal is exactly

```text
kappa = -21/8.
```

After the complete integrity tally:

- `DECISION NEGATIVE` if every audit passes and `kappa != -21/8`;
- `DECISION TRACE-SURVIVES` if every audit passes and `kappa = -21/8`;
- `DECISION STOP` if any integrity, typing, exactness, completeness,
  determinism, stderr, or execution gate fails.

`NEGATIVE` is a valid first-class fired falsifier and exits zero.
`TRACE-SURVIVES` also exits zero, but does not close the claim positively:
the registry additionally requires the separately named exact spectrum gate.
`STOP` is not a scientific result, prints no `NEGATIVE` or `TRACE-SURVIVES`
line, and exits nonzero. The audit tally is computed and printed before the
decision line.

## Systematics frozen at the pin

- The carrier is the full ordered `F_5^6`, not a boundary or selected block.
- The affine maps and `(g o h)(x) = g(h(x))` word order are fixed exactly.
- The Koopman representation uses `g^-1`; no opposite convention is allowed.
- `H` is exactly `<b,d>` and no quotient or extension by `e` is allowed.
- `P = P0 R_H`; raw restriction, a non-orthogonal projection, or omitting
  `P0` from the typed carrier is not an alternative predicate.
- The observable is the ordinary trace of `K^2` on `V`, with no
  normalization and no inferred spectrum.
- Route A uses every orbit and Route B uses every ordered pair in `H x H`.
- The historical checksum is an audit of inherited wording, not the spectrum
  of `K`.
- A different operator, selected representation, golden block, physical
  decoder, or continuum interpretation requires a new probe.
- No exploratory stdout is copied into formal evidence or used as expected
  output.

## Deterministic output contract

The accepted verifier prints, in a fixed order:

```text
public base and ruling pin
carrier and public generator integrity
composition and Koopman convention
H order and sorted orbit census
invariant and traceless dimensions
restriction-failure witness
compression and skew-adjoint checks
Route A numerator/denominator and completeness counts
Route B numerator/denominator and complete word count
exact route agreement
historical checksum audit
AUDIT passed/total
DECISION NEGATIVE, TRACE-SURVIVES, or STOP
RESULT
```

Every printed sequence is sorted by a declared total order. No set or
dictionary iteration order reaches stdout. Formal evidence additionally
requires empty stderr and byte identity with `EXPECTED.txt`.

## Budget, run, and stop rule

- Python standard library only; single verifier file.
- Public CI budget: less than 15 minutes; intended verifier budget: less than
  60 seconds on a current general-purpose core.
- Formal local evidence: Linux or Linux-compatible `aarch64`, neutral public
  environment fields, exit code 0, empty stderr.
- Independent public check: GitHub `x86_64`, byte-identical stdout.
- `EXPECTED.txt`, `RUN.md`, and `RESULT.md` are forbidden before the first
  formal post-pin execution.
- Any change after the pin to the equation, code, carrier, systematics,
  witness, failure threshold, decision routing, or action layer invalidates
  all run evidence and requires a new probe name.
- The pinned branch must never be amended, rebased, squashed, or force-pushed.
