# C-AFFINE-READING-CHARACTER-CENSUS-1 preregistration

Status: **CANDIDATE PREREGISTRATION. NO AUTHORITY. NO SCIENTIFIC RESULT YET.**

Candidate id: `C-AFFINE-READING-CHARACTER-CENSUS-1`.
Target line on promotion: PUBLIC (`mathorn1973/twist-j`).
Layer: **L1 exact arithmetic, finite representation theory, exact linear
algebra only.**
Owner session: one named session, this one. No other session may write this id.

```text
STATE:          ACTIVE
CANON:          Public Canon v60
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v60
CONTENT_COMMIT: 18b21bdaf2c2236c9444b120900277ccfb63e050
CANON_SHA256:   9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0
CANON_BYTES:    329876
HEAD_AT_FREEZE: f9b7438747e612eeebf63cb3ac95283fcb2a7085
```

Currency gate performed against a fresh clone of public `main`, not an
attachment and not a rendered page: `canon/SHA256SUMS` five of five OK, tag and
content commit both ancestors of `main`, recomputed `canon/CANON.md` hash and
byte count equal to the declared fields.

Collision check performed before this file was written: no registry claim, no
frontier row, no probe directory and no `notes/` candidate covers a graded or
character-graded reading census. The two adjacent public rows are
`AFFINE-READING-DEGREE-CENSUS` and `AFFINE-QUADRATIC-FORM-UNIQUENESS`, both
already `T`, and both are inputs here rather than targets.

## Motivation, stated as the claim to be attacked

The informal claim under attack is that only contraction is readable and that
the expansive or phase datum is unreadable in principle. The precise L1 shadow
of that claim is that no nonzero linear reading of the carrier exists. The
existing public row establishes this only in the invariant sector,
`(V*)^G = 0`. A reading that is not invariant but merely covariant with a phase
weight would still be a reading, so the invariant sector alone does not settle
the question. This candidate closes the question in every linear character
sector at once and then, deliberately, attacks the overclaim that follows it.

## The six preregistration fields

### 1. Equation

For `G = AGL_1(F_5)` of order 20 acting on the four dimensional rational
carrier `V` and for every linear character `lambda` of `G`:

```text
m_lambda(d) = dim { f in Sym^d(V*) : f(rho(g) x) = lambda(g) f(x) for all g, x }
```

and the Molien identity

```text
sum_{d >= 0} m_lambda(d) t^d = (1/|G|) sum_{g in G} conj(lambda(g)) / det(I - t rho(g)).
```

The multiplicity of `V` itself is

```text
m_V(d) = (1/|G|) sum_{g in G} conj(chi_V(g)) chi_{Sym^d V}(g),
chi_V(g) = #Fix_{F_5}(g) - 1.
```

### 2. Code

`verify_C-AFFINE-READING-CHARACTER-CENSUS-1.py`. Python standard library only.
Exact `Fraction` and exact integer arithmetic. No float in any assertion, no
randomness, no external data, no environment input, no network, no third party
library. Deterministic single run under
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`,
under 120 seconds, exit 0 and empty stderr required.

### 3. Carrier or data

The public integer step matrix

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0,0,0],
       [0,1,-1,1]],
```

`D = M_J - I`, `v_x = D^x e_0` for `x in F_5`, and `rho(a,b) v_x = v_(ax+b)`
for `a in F_5^*`, `b in F_5`. Frozen quadratic forms

```text
q_+ = (5/2) G,  G = I_4 - (1/5) 1 1^T,
q_- = [[0,1,-1,-1],[1,0,1,-1],[-1,1,0,1],[-1,-1,1,0]].
```

No alternative carrier, basis or normalization is admitted after this freeze.

### 4. Systematics

Two independent computation routes are required wherever a dimension is
gated, and their independence is the systematic being controlled.

```text
Method A  explicit averaging projector on the monomial basis of Sym^d(V*),
          dimension read as an exact matrix rank over Q or over Q(i).
Method B  Molien power series, obtained by exact power series inversion of
          the integer polynomial det(I - t rho(g)), summed against the
          character values.
```

Neither route consumes the other's output. Method A never forms a character
value; Method B never forms a Sym^d matrix. Truncation is a declared
systematic: Method A runs for `d` in 0 to 5, Method B for `d` in 0 to 12. No
degree beyond those is claimed.

Order four characters take values in `{1, i, -1, -i}`. They are handled in
exact `Q(i)` as pairs of rationals, and rank over `Q(i)` is read as half the
rank of the faithful eight by eight rational embedding. No float, no complex
type.

### 5. Failure threshold

There is no numerical threshold. Every decision is an exact equality, an exact
rank, an exact integer, or an exact power series coefficient. The gates and
their falsifiers follow. One exact witness fires a gate.

**G1. Carrier integrity.** `D^5 = I`; the characteristic polynomial of `M_J` is
`x^4 - 3x^3 + 4x^2 - 2x + 1`; the sum of `v_x` over `F_5` is zero; `rho` is a
group homomorphism on all 400 ordered pairs; `rho(1,1) = D`.
Falsifier: any one of these fails.

**G2. Character list.** The abelianization of `G` is cyclic of order 4, so `G`
has exactly four linear characters. With `a = 2^m` in `F_5^*`, define
`lambda_r(a,b) = i^(r m)` for `r` in `{0,1,2,3}`, so `lambda_0 = 1`,
`lambda_2 = epsilon`. Each must be a homomorphism on all 400 ordered pairs, the
four must be pairwise distinct as functions, and `epsilon = lambda_1^2`.
Falsifier: a homomorphism failure, a coincidence, or `epsilon != lambda_1^2`.

**G3. Linear void in every character sector.** `m_lambda(1) = 0` for all four
`lambda`, by both methods. This is the exact form of the claim under attack.
Predicted forced: `V` is absolutely irreducible of dimension four
(`dim End_(Q[G])(V) = 1`, public row `AFFINE-READING-DEGREE-CENSUS`), so
`V tensor lambda` is irreducible of dimension four and carries no trivial
summand.
Falsifier: exhibit a nonzero linear form `f` on `V` and a linear character
`lambda` with `f(rho(g) x) = lambda(g) f(x)` for all `g` and `x`. One such `f`
falsifies the whole route.

**G4. Quadratic sector.** `m_1(2) = 1` and `m_epsilon(2) = 1` and
`m_lambda_1(2) = m_lambda_3(2) = 0`, by both methods; the invariant line is
spanned by `q_+` and the epsilon line by `q_-`, verified as
`rho^T q_+ rho = q_+` and `rho^T q_- rho = epsilon(g) q_-` for all 20 elements.
Predicted forced by the public decomposition `Sym^2 V = 1 + epsilon + 2V`.
Falsifier: any dimension differs, or either form fails its transformation law.

**G5. Graded census, two methods.** For every `d` in 0 to 5 and every linear
character, Method A and Method B must return the same integer.
Falsifier: one disagreement anywhere in the 24 cells.

**G6. Total dimension consistency.** For every `d` in 0 to 5,

```text
m_1(d) + m_epsilon(d) + m_lambda_1(d) + m_lambda_3(d) + 4 m_V(d) = C(d+3,3),
```

and `m_lambda_1(d) = m_lambda_3(d)` for every `d` in 0 to 12, since `V` is
realizable over `Q` and the decomposition is stable under the Galois action.
Falsifier: either identity fails at any degree.

**G7. Odd degree forcing and the smallest odd reading.** `chi_V(g)` lies in
`{-1, 0, 4}` for every `g`, so no element of `G` acts as `-I` on `V`; hence for
generic `x` the vectors `x` and `-x` lie in different `G` orbits. Over a field
of characteristic zero the invariant ring of a finite group separates orbits,
so some invariant of odd degree must exist. Record `d_odd`, the least odd `d`
with `m_1(d) > 0`.
Falsifier: `chi_V` takes the value `-4`; or `m_1(d) = 0` for every odd `d` up
to 12, which would contradict the separation theorem and falsify the route.
`d_odd >= 3` is already forced by G3 and G4.

**G8. Sign witness.** Scanning `{-1,0,1}^4` in lexicographic order, take the
first `x` with `q_-(x)` nonzero, and the first `g` with `epsilon(g) = -1`.
Require exactly `q_+(rho(g) x) = q_+(x)` and `q_-(rho(g) x) = -q_-(x)` with
`q_-(x)` nonzero. This is the concrete witness that the epsilon graded
quadratic channel carries no absolute reading, only a relative one.
Falsifier: no such `x` exists, or either equality fails.

**G9. Separation counterweight, two sided and declared before the run.** Over
the exhaustive test set `T = {-2,-1,0,1,2}^4` minus the zero vector, 624
vectors, build the complete invariant fingerprint from a basis of the invariant
spaces of degree at most 5 obtained from the Method A projector image, and test
whether equal fingerprint implies same `G` orbit, orbit membership being
decided exactly by trying all 20 elements.
This gate is recorded, not route deciding: the outcome `SEPARATING-AT-5` or
`NON-SEPARATING-AT-5` is reported either way and neither outcome falsifies G1
to G8. It is preregistered as two sided precisely so that a negative cannot be
reread afterwards as a positive. Its purpose is to bound the overclaim: if the
fingerprint separates, then the carrier state is recoverable from readings up
to the 20 element orbit, and the correct statement is that the state is
unreadable **linearly**, not unreadable.

### 6. Action layer

**L1 only.** Exact arithmetic, finite representation theory, exact linear
algebra. No lift is performed.

## Decision

```text
READING-CENSUS-CERTIFIED
  carrier integrity holds and every frozen G1 to G8 statement passes exactly.
  G9 is reported with its recorded label.

ROUTE-FALSIFIED
  carrier integrity holds but at least one frozen G1 to G8 statement fails.
  Preserve the failing witness. Do not modify this candidate.

STOP
  authority, collision, exactness, determinism, stderr, security or mutation
  requirement fails.
```

## Maximum scope and firewall

Maximum status a later public fold may propose from this candidate is **T at
L1 only**, and only after the public probe protocol supplies a pinned
preregistration, a two architecture byte identical run and a sealed fold. Being
a candidate promotes nothing.

No measurement, apparatus, instrument, observer, decoder, Born rule,
probability, effect, record, photon, light, matter, energy density, radiation
density, cosmology, expansion, contraction, dark sector, hidden fraction, SI
value, or L2 to L6 lift is assumed or concluded. In particular this candidate
does **not** establish that any physical apparatus is unable to record a linear
datum. It establishes a statement about invariant and semi-invariant
polynomials on a finite dimensional rational carrier, and nothing else.

## The lift, named here and not crossed

The passage from the L1 statement to any apparatus statement is an unnamed
layer lift and therefore a stop condition under the operating contract. This
candidate names it as an open obligation for a later and separate fold, and
does not attempt it:

```text
O-LINEAR-READING-APPARATUS-LIFT [O]
  scope: from the L1 character graded reading census to L4 support and L5
  stream. Required before any apparatus, record or measurement reading of the
  census: the support carrier, the instrument or write map, the record
  codomain, the exact equality, the normalization, and a complete acyclic
  dependency graph.
  falsifier: exhibit one registered L4 or L5 readout whose emitted record is a
  nonzero linear function of the L1 carrier state.
  decision: STOP until every typed field above is public and frozen.
```

## Formal order

1. Freeze this file and record its SHA-256 before writing the verifier.
2. Write the verifier. Do not open any gate value before the freeze above.
3. Execute once in the deterministic environment. Save exact stdout.
4. Attempt to break the result by an independent path and record what was
   tried, whether or not it succeeded.
5. Package `PROMO-C-AFFINE-READING-CHARACTER-CENSUS-1`.
6. Validation is public and is not performed here.
