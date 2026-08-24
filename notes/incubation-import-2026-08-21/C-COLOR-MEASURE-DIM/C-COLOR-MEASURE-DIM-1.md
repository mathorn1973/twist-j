# C-COLOR-MEASURE-DIM-1

In-project incubation-lane candidate. Status: candidate-C (computed, exact) plus
candidate-F (a scoped fired falsifier). No authority. Promotes nothing by living
here. One named session per candidate; this is that session.

Target line on promotion: Public Canon (v5, mathorn1973/twist-j main).
Action layer: L6 (measure) over the L4 support (the 24 recurrent carrier orbits).
Session date: 2026-07-15. Roadmap consumed: PROGRAMROADMAPV4.md, Lane 3.

## Step 0 currency (confirmed this session)

Public head is Public Canon v5, STATE ACTIVE, AUTHORITY mathorn1973/twist-j main,
tag canon-v5, CONTENT_COMMIT 1a4097727029b8b27ac89453c64d075cab6607e2,
CANON_SHA256 fb797ad4b65f516526189af860b4fd1180347290fac7a7e685c2c7d571a1854c,
59640 bytes; canon/SHA256SUMS lists 5 files and canon/CANON.md matches. The
uploaded roadmap is a v4 planning surface and lags the live line by one integer
version. COLOR-MEASURE-SELECTION [O] is live and untouched in v5 (v5 added only
ENTROPY-MIRROR-LAW [C]). No collision: no public COLOR probe or branch, and no
prior in-project COLOR candidate doc.

## Claim and scope

The color measure over the 24 carrier orbits is a probability weight vector.
This candidate turns the roadmap Lane 3 task into an exact constraint problem and
tests one sub-hypothesis by falsification first:

H-DIM: the two named structural constraints available at this layer, invariance
under the AUT_col symmetry action and consistency with the 16-type observable,
select a UNIQUE color measure over the 24 orbits.

Explicit falsifier: the admissible family has dimension d >= 1 (two inequivalent
vectors survive every named constraint). This mirrors the public negative-closure
clause of COLOR-MEASURE-SELECTION.

Scope ceiling: this candidate evaluates exactly those two constraints. It does
NOT evaluate the three registered routes of O-A18-COLOR-MEASURE-SELECTION (their
exact definitions are internal or inline and out of local scope). It cannot close
the parent O; it quantifies the residual freedom and fires or fails H-DIM.

## Inputs and their provenance

Public (Public Canon v5, canon/REGISTRY.tsv, canon/FRONTIER.md):
  N_orbits = 24, N_types = 16, carrier SL_3(F_5), COLOR-MEASURE-SELECTION [O].
Sealed internal census (twistj-jam v184, D-A18-COMPONENT-TYPES, file sha256
cd92b8bb..., (N_sym, N_inv) = (24, 16)):
  (a) AUT_col fixes all 24 orbits, trivial action, unit cycles only;
  (b) observable shape 8 doubletons + 8 singletons (8 undistinguished pairs,
      24 - 16 = 8);
  (c) all component measures uniform 1/L (context; not used by the dimension).

Load-bearing: the counts (24, 16), public; and the AUT_col action shape,
internal and declared. The doubleton/singleton shape (b) is used only for a
concrete witness; the dimension is proved shape-independent for any surjection.

## Preregistration (frozen before compute)

Five frozen fields, action layer, and falsifier are in PREREG.md.
PREREG.md sha256 6fca2545264531fe23337b09bdb7552dcafb6f33c6dadd55a109736c45ac79d0
(5125 bytes), frozen and hashed before verify.py was written or run.

## Result (exact, no floats in any assertion)

```
d_obs  (16-type observable measurability alone)        = 15
d_sym  (AUT_col invariance alone, trivial action c=24) = 23
d_comb (observable AND symmetry, c=24)                 = 15
rank(observable difference system)                     = 8   ( = 24 - 16 )
equivalence classes of weight vectors                  = 16  (the observable types)
positivity                                             = full; uniform 1/24 interior
admissible set                                         = relative interior of a 15-simplex
```

Decision against the frozen threshold: H-DIM predicted d = 0; computed
d_comb = 15 >= 1, so H-DIM is FALSIFIED (candidate-F, scoped). Two explicit
inequivalent survivors were exhibited. The computation reproduces, from the
public counts plus the sealed AUT_col action, the internal v184 statement
"simplex dimension 23 by symmetry, 15 by observables".

Verifier pins:
```
verify.py     sha256 5f3954f883a0e2653038e7420659d8e764394801319795f71676f76de402daac (8211 bytes)
stdout        sha256 b0924ff000bbf157c39e450137d6afa39374cd96c87eeb986e1e1b29d4208693
platform      x86_64 CPython 3.11.15 (single platform; two-platform is public scope)
```

## Break-it record

1. Two independent dimension algorithms inside verify.py agree at d_comb = 15
   (rank-nullity by exact Gaussian elimination, and union-find join-block count).
2. Independent second reading break_check.py (augmented-rank / nullity) gives 15
   and confirms the normalization row is independent of the difference rows.
3. Shape independence: four distinct surjection shapes each give rank 8,
   d_obs = 15. The number depends only on the counts 24 and 16.
4. Symmetry dependence: only a transitive action (c = 1) would force uniqueness;
   the sealed c = 24 gives 15. The falsification hinges exactly on the sealed
   AUT_col-trivial-action fact, which is declared load-bearing.
None overturned d = 15 or the falsification.

## Output

The promotion proposal a public fold can consume is PROMO-C-COLOR-MEASURE-DIM-1.
It proposes a fully-public Tier 1 [C] (observable alone leaves 15 dimensions) and
a Tier 2 [C] gated on the public typing of the AUT_col action. It does NOT close
COLOR-MEASURE-SELECTION [O]. Validation is public, not here: two architectures,
byte-identical stdout, public checks, an owner-opened fold PR.
