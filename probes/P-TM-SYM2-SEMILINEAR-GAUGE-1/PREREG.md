# PREREG. P-TM-SYM2-SEMILINEAR-GAUGE-1

Status: ACCEPTED FOR IMMUTABLE PIN; FORMAL GATE NOT RUN.

This preregistration belongs to public formal-lock issue #134. Definition
issue #132 and PR #133 supplied the theorem-grade, non-canonical
predefinition; neither is reused as the formal lock. The completed public
antecedent `P-TM-SYM2-MEASURE-1` is consumed only through its pinned public
transcript and is never imported or executed.

No exponent-one incidence system has been enumerated. No exponent-one
existence value, accepted permutation, matrix, candidate group order, coset
character, residual invariant, semilinear orbit partition, scientific route,
or formal-output hash is known to this preregistration.

## 1. Public authority and probe identity

```text
probe:                  P-TM-SYM2-SEMILINEAR-GAUGE-1
branch:                 probe/P-TM-SYM2-SEMILINEAR-GAUGE-1
path:                   probes/P-TM-SYM2-SEMILINEAR-GAUGE-1/
owner:                  A. M. Thorn / this owner session
public formal lock:     issue #134
branch parent:          87c1a0a42a23ad68612cabcddd1c91fd784c9150
Public Canon:           v16 ACTIVE
annotated tag target:   ffed1ff536972113cbc3d8f74830172206b3a489
content commit:         a96f6c7a8ed63c2234977cb1c7a3432fd315bd7a
Canon SHA-256:          836b8d642f5209d46a5b833a3a1e7a1acc14a249e83066af1adb21845242d4a9
Canon bytes:            89364
owner row:              TM-SYM2-MEASURE [H]
scientific layer:       L5 structural candidate equivalence only
excluded layer:         L6 physical measure
```

The collision audit recorded in issue #134 preceded the branch and probe
path. The definition parent and the active Canon are authority inputs, not
outputs of this probe.

## 2. Frozen public source snapshots

The immutable initial pin carries two byte-for-byte public snapshots:

```text
SOURCE-PREDEFINITION.md
  public source:
    notes/canon/P-TM-SYM2-SEMILINEAR-GAUGE-1-PREDEFINITION.md
  public commit:  87c1a0a42a23ad68612cabcddd1c91fd784c9150
  git blob:       f8ac57bc5d85505615fd03edaf341446dd2ba976
  bytes:          25896
  LF / CR:        776 / 0
  SHA-256:        9f5dfe902bb0ff9fc19c4bdc4fb1095301a55bd00201f770ab81a36899c2273f

SOURCE-MEASURE1-EXPECTED.txt
  public source:
    probes/P-TM-SYM2-MEASURE-1/EXPECTED.txt
  public merge:   284b3e28cba9daa80ec757592656e2ecbbfddfe0
  git blob:       b2b3250550dd78af0479db114499392c86812b13
  bytes:          9879
  LF / CR:        79 / 0
  SHA-256:        395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f
```

The second snapshot is inherited evidence for the already sealed facts

```text
|Sel_class| = 48,
|G| = 12,
the G action is free,
the old selector partition has four blocks of size 12.
```

It is not the expected output of this probe. The old
`P-TM-SYM2-MEASURE-1/verify.py` is not copied, imported, invoked, or
replayed.

The accepted new verifier identity at the immutable pin is:

```text
file:             verify.py
verify.py SHA-256: f526af796e0fd2951d5b136b17f786045a932214744040dfd0b86e47c50b3590
command:          python3 probes/P-TM-SYM2-SEMILINEAR-GAUGE-1/verify.py
arguments:        none
implementation:   Python standard library only
```

The placeholder on the preceding identity line must be replaced by the exact
lowercase 64-hex SHA-256 before `check_pin.py` can pass and before the pin is
committed. Replacing it is a pre-pin identity completion, not a scientific
evaluation.

## 3. Frozen equation and exact carriers

The coefficient field and involution are

```text
K = Q(sqrt(5)),
phi = (1 + sqrt(5))/2,
tau(a + b sqrt(5)) = a - b sqrt(5).
```

All arithmetic is exact normalized rational-pair arithmetic. Floating point,
numeric tolerance, randomized search, heuristic candidate generation, and
external algebra systems are forbidden.

The ordered vectors and projective lines are

```text
v1 = (0,1,phi),       v2 = (0,1,-phi),
v3 = (1,phi,0),       v4 = (1,-phi,0),
v5 = (phi,0,1),       v6 = (phi,0,-1),
Lines = ([v1],[v2],[v3],[v4],[v5],[v6]),
sigma_line = (v1 v2)(v3 v4)(v5 v6).
```

The frozen oriented domain and target pairs are

```text
D0 = (001,110),       E0 = (v1,v2),
D1 = (010,101),       E1 = (v3,v4),
D2 = (011,100),       E2 = (v5,v6).
```

For `b in F2`, write their members as `D_(i,b)` and `E_(j,b)`. The complete
centralizer carrier is

```text
W = Cent_Sym(Lines)(sigma_line)
  = {(pi,delta): pi in S3, delta in F2^3},
a(E_(j,b)) = E_(pi_a(j), b + delta_a,j),
|W| = 48.
```

The selector carrier is the complete 48-element torsor

```text
Sel_class = {s_(pi,epsilon):
             s(D_(i,b)) = E_(pi(i), b + epsilon_i),
             pi in S3, epsilon in F2^3}.
```

The two frozen characters are

```text
chi_Q(a) = sgn(pi_a),
chi_F(a) = (-1)^(delta_a,0 + delta_a,1 + delta_a,2),
G = ker(chi_Q) intersect ker(chi_F),
|G| = 12.
```

The equality with the old projective-linear gauge is an inherited theorem
and must also be reconstructed as an integrity certificate.

The realization group and candidate effective permutation image are

```text
tilde_Gamma_sl = {
  ([B],e): e in F2, B in GL_3(K),
  [v] |-> [B tau^e(v)] permutes Lines and commutes with sigma_line
},
Gamma_sl = image(tilde_Gamma_sl -> W).
```

For fixed `e`, `(B,e) ~ (cB,e)` for `c in K^*`; no scalar equivalence is
allowed between distinct exponents. Composition and inverse are frozen as

```text
([B],e)([C],f) = ([B tau^e(C)], e+f),
([B],e)^(-1) = ([tau^e(B^(-1))], e).
```

For every exponent and every centralizer permutation, the sole
information-bearing equation is the exact homogeneous system

```text
B tau^e(v_i) = lambda_i v_(p(i)),       i=1,...,6,
e in {0,1},                              p in W,
```

in the nine entries of `B` and the six scalars `lambda_i`.

## 4. Frozen systematics and complete 96-case scan

The verifier performs one self-contained calculation in the following
fixed order.

1. Hash and byte-check both source snapshots before any scientific work.
2. Reconstruct `K`, `tau`, `phi`, the six vectors, exact projective
   proportionality, `sigma_line`, the three oriented pairs, all 48 elements
   of `W`, all 48 selectors, both characters, character covariance, and the
   12-element common kernel.
3. Reconstruct the exponent-zero projective group independently and require
   exact equality with `G=ker(chi_Q) intersect ker(chi_F)` and the sealed
   order-12 antecedent. This is an inherited-support integrity check, not a
   second execution of the old probe.
4. Visit every pair `(e,p)` in the deterministic order `e=0,1`, followed by
   lexicographic `(pi,delta)` order on all 48 members of `W`.
   Exactly `2*48=96` incidence cases must be built and decided. No filtering or
   candidate preselection is allowed.
5. For each case, independently construct the unique projective-frame
   candidate from the first four ordered source/target lines when their
   exact frame conditions hold, then decide that candidate by direct checks
   on all six lines. This frame path must return an explicit accept/reject
   record for every one of the same 96 keys.
6. Independently build the full coefficient matrix over `K`, compute a
   deterministic reduced row echelon form, publish/check the rank and
   nullity certificate, and derive the canonical nullspace basis.
7. Form the determinant polynomial of the nine matrix coordinates on the
   complete nullspace. Accept a case exactly when this polynomial is not
   identically zero. The frozen completeness witness tests the
   lexicographically ordered grid `{0,1,2,3}^d` for nullspace dimension
   `d`; degree at most three in each parameter proves that a nonzero
   polynomial cannot vanish on the whole grid.
8. For every accepted case, choose the first invertible grid witness and
   normalize the complete solution vector—`B` and all six `lambda_i`—by
   the first nonzero matrix entry in row-major flattening order. Directly
   recheck all six vector equalities, all six nonzero `lambda_i`, nonzero
   determinant, the induced `p`, and commutation with `sigma_line`.
9. Require exact equality of the frame-path and full-RREF accept/reject
   decision for every key and of their normalized witnesses when accepted.
   Check projective-frame uniqueness and encode the predefinition's
   faithfulness lemma independently of the observed accepted count.
10. Prove both completeness directions: every accepted witness belongs to
    `tilde_Gamma_sl`, and every realization induces one of the 48 scanned
    permutations and hence appears in the accepted list.
11. Verify exact semilinear composition and inverses, injectivity of the
    realization action, the exponent-zero equality with `G`, and the
    conditional exact-sequence theorem that permits only group order 12 or
    24.
12. Enumerate postcomposition on all 48 selectors, prove the action free,
    compute the complete orbit partition, and verify the conditional
    `12/4` versus `24/2` action theorem.
13. Derive the scientific route only after all structural certificates are
    green. The transcript must carry a canonical hash of the complete
    96-case certificate table and enough deterministic witness data to
    audit every accepted case.

The verifier must check its certificates independently in the same process.
There is no second evaluator invocation in the formal run.

## 5. Frozen character and residual-invariant classification

Write the characters additively as

```text
q(a) = 0 for chi_Q(a)=+1 and 1 for chi_Q(a)=-1,
f(a) = 0 for chi_F(a)=+1 and 1 for chi_F(a)=-1.
```

If the exponent-one fiber is nonempty, it must be one 12-element coset
`hG`. Every member has the same nonzero character

```text
c = (q(h),f(h)) in {(1,0),(0,1),(1,1)}.
```

The residual two-orbit invariant is derived, not selected, by this complete
conditional table:

```text
c=(1,0)  -> residual invariant chi_F
c=(0,1)  -> residual invariant chi_Q
c=(1,1)  -> residual invariant chi_Q chi_F
```

The pin contains all three cases symmetrically. It contains no expected
value of `c` and no preferred residual invariant.

## 6. Frozen scientific routes

Integrity is evaluated before science. With every structural certificate
green, exactly one of these two result-neutral scientific routes is valid:

```text
LINEAR-ONLY
  exponent-one realization count = 0;
  Gamma_sl = G and |Gamma_sl| = 12;
  four free selector orbits, all of size 12;
  the four old (chi_Q,chi_F) fibers remain distinct.

SEMILINEAR-DOUBLE
  exponent-one realization count = 12;
  Gamma_sl = G disjoint-union hG and |Gamma_sl| = 24;
  two free selector orbits, both of size 24;
  emit the common nonzero c and its table-derived residual invariant.
```

Neither route is expected. Both are valid exit-zero scientific results. The
analytic exact-sequence ceiling excludes order 48 and therefore excludes a
one-orbit route before evaluation; that exclusion is not an observed result.

The deterministic transcript must separate structural certificate lines
from one final scientific block. That block has the fixed field grammar

```text
ROUTE: <LINEAR-ONLY | SEMILINEAR-DOUBLE>
GAMMA_SL_ORDER: <12 | 24>
EXPONENT_ONE_COUNT: <0 | 12>
COSET_CHARACTER: <NONE | (1,0) | (0,1) | (1,1)>
RESIDUAL_INVARIANT: <(chi_Q,chi_F) | chi_F | chi_Q | chi_Q chi_F>
SELECTOR_ORBIT_COUNT: <4 | 2>
SELECTOR_ORBIT_SIZES: <12,12,12,12 | 24,24>
RESULT: PASS
```

All angle-bracket values are computed fields with the route-consistency
relations above. They are not substituted into the immutable source.

## 7. Frozen failure threshold

Any one of the following is `STOP`, not a scientific route and not
permission to edit or rerun this probe id:

- missing, additional, renamed, nonregular, or changed initial-pin file;
- source snapshot byte, LF, CR, SHA-256, or required-marker mismatch;
- unresolved or mismatched verifier hash;
- forbidden import, external process, network, filesystem write, argument,
  randomness, clock dependence, floating point, or old-verifier access;
- embedded expected exponent-one witness, route, candidate order, `c`,
  residual invariant, orbit partition, representative, pairing case, or
  output hash;
- field, involution, vector, line, proportionality, pairing, character,
  selector, antecedent, or exponent-zero reconstruction failure;
- anything other than exactly 48 centralizer elements, 48 selectors, two
  exponents, and 96 completely decided incidence systems;
- incomplete or inexact RREF, nullspace, determinant-polynomial, grid,
  witness normalization, direct-incidence, uniqueness, faithfulness,
  composition, inverse, injectivity, or two-direction completeness
  certificate;
- accepted singular `B`, zero `lambda_i`, wrong induced permutation, or a
  permutation not commuting with `sigma_line`;
- exponent-zero image unequal to the exact 12-element `G`;
- exponent-one accepted set other than empty or one 12-element coset with a
  common nonzero character;
- candidate group/order/action/orbit data inconsistent with the frozen
  `12/4` versus `24/2` theorem;
- nondeterministic or malformed transcript, missing or multiple route,
  nonzero formal exit, nonempty formal stderr, timeout, or
  cross-architecture byte mismatch.

`STOP` carries no conclusion about semilinear realizability. A frozen-file
defect invalidates this probe id; thresholds, route grammar, equations, and
carriers never move after the public pin.

## 8. Action layer and debt firewall

This probe is confined to a candidate equivalence relation on the already
frozen L5 selector carrier. It asks whether the exact semilinear realization
image is the old 12-element linear gauge or a 24-element extension.

No outcome:

- edits or adopts `canon/CANON.md`, `canon/REGISTRY.tsv`,
  `canon/FRONTIER.md`, `canon/GATES.tsv`, `canon/DEPENDENCIES.tsv`,
  `STATUS.md`, or release metadata;
- changes `TM-SYM2-MEASURE [H]`, closes either registered action-layer gate,
  or supplies an L1-to-L5 or L5-to-L6 bridge;
- normatively adopts `Gamma_sl` as gauge;
- changes the old N2 result, selects a character fiber or selector, or
  claims microscopic canonicality;
- enlarges gauge to all of `W`, turns domain negation into gauge, chooses a
  sign branch, or adds a minority-coordinate dictionary;
- derives physical probability, a Born halving, or any L6 measure theorem.

Any later adoption or Canon/status treatment requires a separate owner
decision and separately reviewed fold after the result.

## 9. Static pin gate and formal execution budget

The immutable initial pin contains exactly

```text
PREREG.md
verify.py
check_pin.py
SOURCE-PREDEFINITION.md
SOURCE-MEASURE1-EXPECTED.txt
```

It contains no `EXPECTED.txt`, `RUN.md`, `RESULT.md`, output fixture, or
formal transcript. `check_pin.py` only reads bytes and parses source/AST. It
must not import, compile, execute, or solve through `verify.py`, enumerate
the exponent-one incidence systems, or emit a scientific result.

Before pin publication, static review covers file inventory, source hashes,
line endings, verifier SHA-256, syntax AST, imports, zero-argument entry,
required complete-scan structure, result neutrality, and security. The
static checker must exit zero with empty stderr and deterministic stdout.
The pin commit, all five file SHA-256 values and byte counts, Git blobs, and
public readback are published on issue #134 before formal execution.

Only after that readback is exactly one formal scientific execution
authorized:

```text
runner scheduling:      one owner-authorized JAS 2 or JAS 4 Linux runner
public platform field:  neutral Linux distribution/version only
public architecture:    aarch64
formal command:         python3 probes/P-TM-SYM2-SEMILINEAR-GAUGE-1/verify.py
arguments:              none
environment:            LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
                        PYTHONHASHSEED=0 TZ=UTC
external timeout:       600 seconds
deterministic runs:     exactly 1
```

No Studio execution belongs to this lane. `RUN.md` must not record a machine
nickname or private path. It records UTC start/finish, neutral platform,
architecture, Python version, detached commit, pre/post clean state, command,
environment, exit, exact stdout/stderr bytes and SHA-256, LF/CR/final-byte
metadata, verifier and support hashes, route, and
`deterministic_executions: 1`.

Only after the single aarch64 run may `EXPECTED.txt`, `RUN.md`, and
`RESULT.md` be added. The pull request changes only this probe directory.
The required clean GitHub Linux/x86_64 replay must use identical pinned
support and verifier hashes, exit zero, write empty stderr, and reproduce
stdout byte for byte.

After the pin there is no amend, rebase, squash, force-push, threshold
repair, or rerun. The probe may merge only by merge commit. Either valid
scientific route is preserved first-class.
