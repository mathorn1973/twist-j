# P-AFFINE-READING-CHARACTER-CENSUS-1 preregistration

Status: **PREREGISTRATION. FROZEN BEFORE FIRST EXECUTION. NO RESULT YET.**

```text
CLAIM ISSUE     #534
BRANCH          probe/P-AFFINE-READING-CHARACTER-CENSUS-1
PATH            probes/P-AFFINE-READING-CHARACTER-CENSUS-1/
STATE           ACTIVE
CANON           Public Canon v60
AUTHORITY       mathorn1973/twist-j main
TAG             canon-v60
CONTENT_COMMIT  18b21bdaf2c2236c9444b120900277ccfb63e050
CANON_SHA256    9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0
CANON_BYTES     329876
PIN PARENT      f9b7438747e612eeebf63cb3ac95283fcb2a7085
LAYER           L1 exact arithmetic only
```

Currency gate performed against a fresh clone of public `main`:
`canon/SHA256SUMS` five of five OK, tag and content commit both ancestors of
`main`, recomputed `canon/CANON.md` hash and byte count equal to the declared
fields. Collision check performed before this file was written: no registry
claim, no frontier row, no probe directory and no other open issue covers a
graded or character graded reading census.

## Obligation

`AFFINE-READING-DEGREE-CENSUS` establishes `(V*)^G = 0`, closing the invariant
sector only. `G = AGL_1(F_5)` has four linear characters. A reading that is not
invariant but covariant with a phase weight is still a reading. This probe
closes every sector and computes the graded census above them.

The mathematics was developed as incubation candidate
`C-AFFINE-READING-CHARACTER-CENSUS-1`, published on branch
`notes/C-AFFINE-READING-CHARACTER-CENSUS-1`. That candidate carried a recorded
defect in invariant basis extraction. The verifier pinned here is a new
verifier that extracts correctly, gates the extraction itself, prints one line
per gate from that gate's own boolean, and contains no gate that is a constant
true by inspection.

## The six preregistration fields

### 1. Equation

For every linear character `lambda` of `G`,

```text
m_lambda(d) = dim { f in Sym^d(V*) : f(rho(g)x) = lambda(g) f(x) for all g, x }
```

with the Molien identity

```text
sum_d m_lambda(d) t^d = (1/|G|) sum_g conj(lambda(g)) / det(I - t rho(g))
```

and the multiplicity of `V` itself

```text
m_V(d) = (1/|G|) sum_g conj(chi_V(g)) chi_(Sym^d V)(g),
chi_V(g) = #Fix_(F_5)(g) - 1.
```

### 2. Code

`probes/P-AFFINE-READING-CHARACTER-CENSUS-1/verify.py`. Python standard library
only. Exact `Fraction` and exact integer arithmetic. No float in any assertion,
no randomness, no external data, no environment input, no network, no third
party library. Run from the repository root as

```text
python3 probes/P-AFFINE-READING-CHARACTER-CENSUS-1/verify.py
```

under `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`, in
under 120 seconds, with exit 0 and empty stderr required.

### 3. Carrier or data

```text
M_J = [[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]]
D   = M_J - I
v_x = D^x e_0 for x in F_5
rho(a,b) v_x = v_(a x + b) for a in F_5^*, b in F_5
q_+ = (5/2) G with G = I_4 - (1/5) 1 1^T
q_- = [[0,1,-1,-1],[1,0,1,-1],[-1,1,0,1],[-1,-1,1,0]]
T   = {-2,-1,0,1,2}^4 minus the zero vector, 624 vectors, in lexicographic
      order as produced by itertools.product over (-2,-1,0,1,2) repeated 4
```

No alternative carrier, basis, normalization or test set is admitted after this
freeze.

### 4. Systematics

Two independent routes are required wherever a dimension is gated.

```text
Method A  explicit averaging projector on the monomial basis of Sym^d(V*),
          dimension read as an exact matrix rank over Q or over Q(i)
Method B  Molien power series by exact power series inversion of the integer
          polynomial det(I - t rho(g)), summed against character values
```

Neither consumes the other's output. Method A never forms a character value.
Method B never forms a `Sym^d` matrix. Truncation is declared: Method A for `d`
in 0 to 5, Method B for `d` in 0 to 12. Nothing beyond is claimed.

Order four characters take values in `{1, i, -1, -i}` and are handled in exact
`Q(i)` as pairs of rationals. Rank over `Q(i)` is read as half the rank of the
faithful eight by eight rational embedding, and the parity of that rank is
itself gated. No float and no complex type appear anywhere.

The collision count in G14 is defined exactly as follows and is order
dependent by design: test vectors are grouped by fingerprint in first
appearance order, and the count is the number of vectors that share a
fingerprint with the first vector of their group but do not lie in its `G`
orbit, orbit membership being decided by trying all twenty group elements.

### 5. Failure threshold

No numerical threshold. Every decision is an exact equality, an exact rank, an
exact integer, or an exact power series coefficient. Fourteen gates follow,
each printed from its own boolean. Any single failing gate fires the route
falsifier and produces `ROUTE-FALSIFIED`.

**G1 carrier integrity.** `D^5 = I`; characteristic polynomial of `M_J` equals
`x^4 - 3x^3 + 4x^2 - 2x + 1`; the sum of `v_x` over `F_5` is zero; `rho` is a
group homomorphism on all 400 ordered pairs; `rho(1,1) = D`.

**G2 four linear characters.** With `a = 2^m` in `F_5^*`, `lambda_r(a,b) =
i^(r m)` for `r` in `{0,1,2,3}`. Each is a homomorphism on all 400 ordered
pairs, the four are pairwise distinct as functions, `lambda_1^2 = lambda_2`,
and `lambda_2` agrees with the sign of `a` being a square.

**G3 linear void in every character sector.** `m_lambda(1) = 0` for all four
characters by both methods. This is the claim under attack.
Falsifier: a nonzero linear form `f` with `f(rho(g)x) = lambda(g) f(x)`.

**G4 quadratic sector.** `m(2)` equals `1, 1, 0, 0` for
`lambda_0, lambda_2, lambda_1, lambda_3`; the invariant line is spanned by
`q_+` and the epsilon line by `q_-`, verified as `rho^T q_+ rho = q_+` and
`rho^T q_- rho = lambda_2(g) q_-` for all twenty elements.

**G5 method agreement.** Method A equals Method B in all 24 cells,
`d` in 0 to 5 across the four characters.

**G6 frozen census table.** The multiplicities equal exactly

```text
d   dim   1   eps   i   ibar   V
0     1   1     0   0      0   0
1     4   0     0   0      0   1
2    10   1     1   0      0   2
3    20   1     1   1      1   4
4    35   3     2   1      1   7
5    56   3     3   3      3  11
```

**G7 total dimension and Galois pairing.** For `d` in 0 to 5,
`m_1 + m_eps + m_i + m_ibar + 4 m_V = C(d+3,3)`, and `m_i(d) = m_ibar(d)` for
`d` in 0 to 12 since `V` is realizable over `Q`. Every Method B value is a
nonnegative integer with vanishing imaginary part.

**G8 frozen Molien rows through degree twelve.**

```text
invariant sector   1 0 1 1 3 3 5 6 10 11 16 18 25
epsilon sector     0 0 1 1 2 3 5 6  9 11 16 18 24
each order four    0 0 0 1 1 3 3 6  7 11 13 18 21
```

**G9 character values and the absence of minus the identity.** The value set of
`chi_V` is exactly `{-1, 0, 4}` and no element of `G` acts as `-I` on `V`.

**G10 smallest odd invariant degree.** The least odd `d` with `m_1(d) > 0`
equals exactly 3. Its existence is forced: no element acts as `-I`, so `x` and
`-x` lie in different orbits for generic `x`, and over a field of
characteristic zero the invariant ring of a finite group separates orbits.

**G11 the cubic invariant and its closed form.** Define
`Kstar := (p_1^3 + 6 p_1 q_+ - 25 p_3)/3` with `p_1` the coordinate sum and
`p_3` the sum of cubes. Required exactly: all coefficients of `Kstar` are
integers; `Kstar` has exactly 20 monomials; the set of its coefficients is
exactly `{-4, 3}`; `Kstar` composed with `rho(g)` equals `Kstar` coefficientwise
for all twenty elements; and the degree three invariant projector fixes
`Kstar`, so `Kstar` spans the one dimensional degree three invariant space.

**G12 basis extraction integrity.** For every `d` in 0 to 5 the invariant
family extracted from the projector image has rank exactly `m_1(d)`, contains
no zero polynomial, and every extracted polynomial is fixed by the projector.
This gate exists because the incubation candidate failed it silently.

**G13 sign witness.** Scanning `{-1,0,1}^4` in lexicographic order take the
first `x` with `q_-(x)` nonzero, and the first `g` with `lambda_2(g) = -1`.
Required exactly: `q_-(x)` nonzero, `q_+(rho(g)x) = q_+(x)`, and
`q_-(rho(g)x) = -q_-(x)`.

**G14 orbit separation and the minimal separating degree.** Over `T` the
cumulative invariant fingerprint through degree `d` must produce exactly

```text
d          0     1     2     3    4    5
invariants 1     1     2     3    6    9
classes    1     1    18    45   84   86
collisions 619 619   474   264    8    0
```

and the exact number of `G` orbits on `T`, computed independently by canonical
orbit representatives and not from any fingerprint, must equal 86. Degree five
therefore separates and degree four does not, so five is the minimal separating
degree on this test set.

### 6. Action layer

**L1 only.** Exact arithmetic, finite representation theory, exact linear
algebra. No lift is performed.

## Decision

```text
READING-CENSUS-CERTIFIED
  carrier integrity holds and all of G1 to G14 pass exactly.

ROUTE-FALSIFIED
  carrier integrity holds and at least one of G2 to G14 fails.
  Preserve the failing witness. Do not modify this preregistration, do not move
  a threshold, do not resume this probe under another name.

STOP
  authority, collision, exactness, determinism, stderr, security or mutation
  requirement fails before or during the formal run.
```

## Scope and firewall

Maximum status this probe can earn is **T at L1 only**, and a later separate
sealed fold is required to move any Canon, Registry or Frontier row. The pull
request that carries this probe changes exactly one probe directory and moves
no normative file.

No measurement, apparatus, instrument, observer, decoder, Born rule,
probability, effect, record, photon, light, matter, energy density, radiation
density, cosmology, expansion, contraction, dark sector, hidden fraction, SI
value, or L2 to L6 lift is assumed or concluded. This probe does **not**
establish that any physical apparatus is unable to record a linear datum. It
establishes a statement about invariant and semi-invariant polynomials on a
finite dimensional rational carrier, and nothing else.

## The lift, named and not crossed

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

Proposing that row is the business of a later fold, not of this probe.

## What the result must not be read as

The central negative and the central positive travel together. The linear void
is complete across all four character sectors, and the informal reading that
only even or contractive quantities are observable is false, because an odd
cubic invariant exists at degree three and the invariants separate orbits up to
the twenty element orbit. Neither half may be quoted without the other.
