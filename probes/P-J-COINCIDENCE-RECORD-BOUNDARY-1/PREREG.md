# P-J-COINCIDENCE-RECORD-BOUNDARY-1 preregistration

Status: **FROZEN TARGET / RESULT-EXPOSED / PROOF-FIRST / L1 ONLY / ONE
PHYSICAL ROW UNTESTED AT STOP / PUBLIC STATUS NONE / NO FORMAL RUN.**

Date: **2026-09-04.**

Author of record: **A. M. Thorn.**

This probe is the exact combinatorial boundary package
`C-J-COINCIDENCE-RECORD-1`. It proves what follows after reduced integer
fibres and complete Cartesian incidence are defined. It does not prove that
Nature realizes that incidence, that its pairs are records, or that their
cardinality ratio is an observed frequency.

The sole physical row is printed by the verifier as `UNTESTED STOP`. It is not
a computational gate and cannot be confirmed by a successful run.

```text
probe:           P-J-COINCIDENCE-RECORD-BOUNDARY-1
package:         C-J-COINCIDENCE-RECORD-1
branch:          probe/P-J-COINCIDENCE-RECORD-BOUNDARY-1
path:            probes/P-J-COINCIDENCE-RECORD-BOUNDARY-1/
claim lock:      https://github.com/mathorn1973/twist-j/issues/809
owner:           A. M. Thorn / delegated session 2026-09-04
mode:            RESULT-EXPOSED / PROOF-FIRST
action layer:    L1 exact finite-set and integer combinatorics
public basis:    Public Canon v75
base main:       50d7c0fd230efc80a6ca7604ec1266aed8a5ff56
tag:             canon-v75
tag target:      c4f00e1d9c89f503d913224dc3c09dc760dcec9d
content commit:  e32e85ed7297d4320df5b345e4488d78323d550c
canon sha256:    44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
canon bytes:     399513
formal runs:     0 before the atomic pin
public status:   NONE
```

## 1. Authority, collision, and novelty lock

The base is the merge of PR #808. It leaves the v75 activation tuple and
every Canon object unchanged. The content commit and activation tag are
ancestors of the base and the Canon hash and byte count agree with
`STATUS.md`.

Before issue #809 was opened, public repository search, the local worktree,
all fetched refs, branches, paths, commit text, issue and pull-request search,
Registry, and Frontier were checked for the exact probe, package, and claim
names. No prior public lock, probe, result, branch, path, or Registry row owns
them.

The physical row `COINCIDENCE-RECORD-FREQUENCY` already occurs in the
NON-CANONICAL candidate definition merged by PR #808. It is intentionally an
input boundary, not a newly claimed theorem. This probe owns only the two
mathematical claims below and the exact separation which leaves that row
untested.

The immediate inputs and novelty boundaries are:

1. PR #805, which confirms the exact integral-mixer/raw-step orbit separation
   used by the scaling gates, while its separate combined polar claim remains
   fired under its frozen verifier;
2. PR #807, which confirms the full-cell controlled copy, diagonal Gram
   contraction, and simplex compression boundary;
3. PR #808, which freezes the reduced residual unit as a NON-CANONICAL
   candidate definition and rejects historical survivor identity;
4. the registered `QDD-INSTRUMENT-NONSELECTION [T]` and
   `QDD-J-AFFINE-APPARATUS-NONSELECTION [T]`, which forbid an algebraic
   dilation from silently selecting a physical instrument;
5. `QDD-INSTRUMENT-APPARATUS [O]`, which remains the missing typed apparatus
   and occurrence source.

No previous result is reclaimed. The new content is the complete finite-set
normal-form proof, its Cartesian cardinality and Gram seam, the explicit
relation nonselection control, and the joint scaling ledger in one frozen
package.

## 2. Frozen claims and decision rule

```text
claim A: J-RESIDUAL-UNIT-NORMAL-FORM
claim B: J-COINCIDENCE-CARTESIAN-GRAM-SEAM

physical row: COINCIDENCE-RECORD-FREQUENCY
fixed status: UNTESTED STOP
```

Claim A is confirmed at candidate-T/L1 exactly when G01 through G04 and G16
pass and the written proof remains valid. Claim B is confirmed at
candidate-T/L1 exactly when G05 through G16 pass and the written proof remains
valid.

Any exact mismatch fires every owning claim. A scientific FIRED result exits
zero, remains public, and is not repaired under this identifier. Authority
drift, collision, pre-pin execution of the accepted verifier, post-pin
mutation, custody loss, incomplete capture, forbidden dependency, nonzero
exit, nonempty stderr, or transcript mismatch is `STOP`, not a scientific
outcome.

G16 audits only that the physical row remains named `UNTESTED STOP` and that
the scope line denies physical records and a frequency law. It does not test
the physical content. The H row has the same STOP status whether either
mathematical claim confirms or fires.

Completion changes no Canon, Registry, Frontier, gate, dependency,
dictionary, or `STATUS.md`. Any registration, definition adoption, H move, or
layer lift requires a separate sealed Canon fold.

## 3. Frozen carrier and reduced normal form

Let

```text
E_Z=Z^5,
V_Z={d in Z^5:sum_k d_k=0},
[n]={1,...,n},
[0]=empty set.
```

The cell basis and cycle follow the current convention

```text
g e_k=e_(k+1 mod 5).
```

For `d in E_Z`, define

```text
d_k^+=max(d_k,0),
d_k^-=max(-d_k,0),

U_k^+(d)={(k,+,m):m in [d_k^+]},
U_k^-(d)={(k,-,m):m in [d_k^-]},
U_k(d)=U_k^+(d) disjoint-union U_k^-(d),
U(d)=disjoint-union_k U_k(d).
```

An element of `U_k(d)` is called a reduced residual integer unit only inside
this candidate package. It is a fresh signed ordinal token at the selected
cut, not a persistent path or particle.

### 3.1 Reconstruction

Directly,

```text
|U_k^+(d)|=d_k^+,
|U_k^-(d)|=d_k^-,
d_k=|U_k^+(d)|-|U_k^-(d)|,
|U_k(d)|=|d_k|.
```

Hence the signed fibre reconstructs `d` exactly and

```text
|U(d)|=L(d)=sum_k |d_k|.
```

### 3.2 Uniqueness among reduced signed pairs

Suppose `a,b` are nonnegative integers satisfying

```text
ab=0,       a-b=c.
```

If `c>0`, then `b>0` would force `a=0` and make `a-b<0`; therefore `b=0`
and `a=c`. If `c<0`, the symmetric argument gives `a=0` and `b=-c`. If
`c=0`, reducedness gives `a=b=0`. Thus the unique reduced pair is

```text
(a,b)=(max(c,0),max(-c,0)).
```

The ordinal fibres are therefore the unique fixed normal-form
representatives once the cell order, signs, and standard ordinals `[n]` are
frozen.

### 3.3 Cell covariance

The cycle transports a token by

```text
(k,sign,m) -> (k+1 mod 5,sign,m).
```

Because `(gd)_(k+1)=d_k`, this gives a bijection from `U(d)` to `U(gd)`.
No such claim is made for a general linear update at the level of individual
token identity. For an integral map `T`, only the output normal form `U(Td)`
is fixed after summation and reduction.

These statements prove claim A once its gates pass.

## 4. Cancellation does not select a historical survivor

Let a coefficient be presented by labelled positive and negative word sets

```text
d_k=|W^+|-|W^-|.
```

With

```text
W^+={a,b},       W^-={c},
```

cancelling `c` against `a` leaves `b`, while cancelling it against `b` leaves
`a`. Both reductions have net coefficient `+1`. Integer addition supplies no
matching, order, priority, or ancestry rule which distinguishes the two.

Therefore `sign(d_k)` and `|d_k|` are invariant, but the identity of a path
said to survive is not. `U_k(d)` is regenerated from those invariant data. It
is not a selected subset of a word expansion.

This negative control is load-bearing. Without it, the candidate definition
would silently add a microscopic trajectory structure absent from the
algebra.

## 5. Tagged copies and complete Cartesian incidence

Make two disjoint tagged copies of the same state-local fibre:

```text
U_k^S(d)={S} x U_k(d),
U_k^R(d)={R} x U_k(d).
```

The tags distinguish the factors and carry no physical semantics in the two
mathematical claims. Their cardinalities are

```text
|U_k^S(d)|=|U_k^R(d)|=|d_k|.
```

Define the complete within-cell relation

```text
C_k^x(d)=U_k^S(d) x U_k^R(d),
C^x(d)=disjoint-union_k C_k^x(d).
```

The product rule for finite sets gives

```text
|C_k^x(d)|=|d_k| |d_k|=d_k^2,
|C^x(d)|=sum_k d_k^2=q(d).
```

When `d_k` is nonzero, both members of a pair inherit the same coefficient
sign, so their sign product is positive. When `d_k=0`, both fibres and their
product are empty.

The exponent two is therefore a combinatorial theorem conditional on the
definition of complete Cartesian incidence. It is not a theorem that the
complete relation is physically realized.

## 6. Exact seam with the full-cell Gram contraction

Let `E=Q^5` have orthonormal basis `e_0,...,e_4`. Import the full-cell copy
from PR #807:

```text
K e_k=e_k tensor e_k,
K d=sum_k d_k e_k tensor e_k.
```

In system-record order, the coefficient matrix of `Kd` is

```text
M_d=diag(d_0,...,d_4).
```

The two algebraic contractions are

```text
M_d M_d^T=M_d^T M_d=diag(d_0^2,...,d_4^2).
```

Combining this identity with section 5 gives the exact seam

```text
(|C_0^x(d)|,...,|C_4^x(d)|)
=diag(M_d^T M_d).
```

The left side is a finite-set cardinality only because `C^x` was explicitly
defined. The right side is an algebraic Gram diagonal. Their equality does not
make the Gram contraction a physical record population.

For the supported vertex and its integral mixer image,

```text
d_0=(4,-1,-1,-1,-1),
Ad_0=(5,0,5,-5,-5),
```

the pair counts are

```text
(16,1,1,1,1),       total 20,
(25,0,25,25,25),    total 100.
```

These are the exposed exact witnesses. The second list contains one empty
cell.

## 7. Darkness and finite ratios inside the construction

Because a Cartesian product is empty exactly when at least one factor is
empty, and the two factors have equal size,

```text
C_k^x(d)=empty set  iff  d_k=0.
```

This is **combinatorial darkness**. It says where the defined complete
relation has no elements. It does not say that a detector never reports that
cell.

For `d!=0`, finite cardinality normalization gives

```text
r_k(d)=|C_k^x(d)|/|C^x(d)|=d_k^2/q(d),
sum_k r_k(d)=1.
```

The symbol `r_k` is a normalized ratio inside a finite constructed set. It is
not called an empirical frequency or probability by either mathematical
claim.

## 8. Relation nonselection: equal marginals do not force the square

A relation between the two tagged fibres may be any subset

```text
C_k subseteq U_k^S(d) x U_k^R(d).
```

If `n=|d_k|`, the complete product has `n^2` elements. The ordinal diagonal

```text
C_k^diag={((S,u_m),(R,u_m)):m in [n]}
```

has `n` elements. The empty relation has none. After lexicographically
ordering the complete product, taking its first `r` elements gives a relation
of every cardinality

```text
r in {0,1,...,n^2}.
```

All these relations have the same available marginal fibres. Therefore the
two marginal counts and the Cayley copy do not select complete incidence.
The step from equal fibres to all ordered pairs is the precise missing choice.

The accepted verifier audits the complete, diagonal, and all-cardinality
controls for `n=1,...,5`. The proof above is the universal finite-set
argument.

## 9. Extensive ledger and the action fork

Freeze the current maps

```text
A=1+g^2-g^3-g^4,
U_5=A/sqrt(5),
J=1+g^2,
N=11^T.
```

Exact multiplication gives

```text
A^T A=5I-N.
```

For `d in V_Z`, `d^TNd=(sum_k d_k)^2=0`, hence

```text
q(Ad)=5q(d).
```

Inside the complete Cartesian construction this becomes the literal
cardinality law

```text
|C^x(Ad)|=5|C^x(d)|.
```

This is the state-independent extensive law for pairs under the **integral**
mixer `A`.

### 9.1 Single units fail the same test

For `L(d)=sum_k|d_k|`, use two supported states. The vertex gives

```text
L(d_0)=8,       L(Ad_0)=20,       ratio=5/2.
```

For

```text
h=(-1,1,0,0,0),
Ah=(-2,1,-1,2,0),
```

the supported scaled state `5h` gives

```text
L(5h)=10,       L(A(5h))=30,       ratio=3.
```

No state-independent multiplier governs the number of single residual units.
This pair of witnesses is enough for that exclusion. This probe does not claim
the stronger all-power functional theorem proposed elsewhere.

### 9.2 `A` and `U_5` have different counting roles

The normalized map satisfies

```text
q(U_5d)=q(d)
```

on the real augmentation sector. But `U_5d=Ad/sqrt(5)` is generally not an
integer vector. Since `sqrt(5)` is irrational and `Ad_0` is nonzero, `U_5d_0`
cannot be interpreted by the literal finite fibres of section 3 without an
additional unit-scale law.

Thus pair-count multiplication by five is an `A` statement. Quadratic-norm
preservation is a `U_5` statement. The verifier audits this naming boundary;
it does not choose a physical step.

### 9.3 Raw `J` has no universal pair-yield multiplier

For the raw orbit of `d_0`, direct exact iteration gives

```text
q(d_0), q(Jd_0), q(J^2d_0), q(J^3d_0)
=20, 30, 70, 180.
```

Already the previously exposed witness `5h` has a different one-step ratio
from `d_0`. Consequently raw `J` does not carry the state-independent
quadratic multiplier of `A`.

The result is a fork ledger only:

```text
A:    integral complete-pair count multiplies by 5;
U_5:  normalized q is preserved, literal integer fibres need a scale law;
J:    raw q yield is state-dependent.
```

Selecting a physical branch remains an owner decision after this probe.

## 10. Sole physical row, frozen but untested

The only physical proposal in this package is reproduced exactly:

```text
COINCIDENCE-RECORD-FREQUENCY [candidate-H / future L5-L6 / STOP]

At a frozen calibrated read cut for a supported nonzero integral preparation,
the physically realized record population is exactly

    C^x(d)=disjoint-union_k U_k^S(d) x U_k^R(d),

with every within-cell ordered pair realized once and no other record. The
ensemble is this simultaneous finite plenum itself, not repetition in time and
not a set of modal branches. Observed cell frequency is finite self-location
in this record population:

    f_k(d)=|C_k^x(d)|/|C^x(d)|=d_k^2/q(d).
```

This row selects complete incidence, gives its pairs physical record status,
and identifies a cardinality ratio with an observed frequency. None of those
three physical acts follows from sections 3 through 9. Keeping them in one row
makes the complete bridge visible instead of distributing hidden assumptions
through otherwise mathematical prose.

The verifier must print

```text
HYPOTHESIS COINCIDENCE-RECORD-FREQUENCY UNTESTED STOP
```

for every scientific outcome. The line cannot be promoted by passing G01
through G16.

Model-level falsifiers are:

1. realized record counts not equal to the diagonal of the joint Gram
   contraction;
2. a missing or multiply counted within-cell Cartesian pair;
3. an off-cell record or a record without a system-record coincidence;
4. a nonzero realized record in a cell with `d_k=0`.

Operational use of those falsifiers still needs the independently frozen
apparatus, gain, background, resolution, preparation, and read-cut ownership
missing from `QDD-INSTRUMENT-APPARATUS [O]`.

The H row gives no randomness law for one run. If adopted, every coincidence
is realized. The phrase `which result do I see?` would name finite
self-location within that realized population, not a random selection proved
by this package.

## 11. Six preregistration fields

1. **Equation.** Sections 3 through 10 freeze the carrier, normal form,
   complete relation, Gram seam, extensive laws, controls, and sole H row.
2. **Code.** The only accepted verifier is
   `probes/P-J-COINCIDENCE-RECORD-BOUNDARY-1/verify.py`.
3. **Carrier or data.** The mathematical carriers are finite signed ordinal
   sets over `Z^5`, exact five-by-five integer matrices, and exact rational
   ratios. There is no dataset.
4. **Systematics.** Cell order, cycle direction, reducedness, fresh ordinal
   labels, tagged factor order, ordered Cartesian pairs, within-cell relation,
   Gram convention, integral `A`, normalized `U_5`, and raw `J` are fixed.
5. **Failure threshold.** Tolerance is zero. A failed exact condition fires
   every owning mathematical claim; custody failure is STOP. The physical row
   is always UNTESTED STOP.
6. **Action layer.** Mathematical claims are L1 only. The H row names a future
   L5-L6 bridge but earns no layer.

## 12. Accepted program

The accepted verifier has pre-pin SHA-256

```text
b2cf94f68bc6d6a2d4963827a27ff733537209a18ea37fd07f35f660d47e4eb5
```

It uses only the Python standard library and exact integer/`Fraction`
arithmetic. It has no float, builtin complex arithmetic, NumPy, SymPy,
mpmath, file input, external dataset, network, subprocess, shell, randomness,
clock, dynamic import, `eval`, `exec`, environment input, or unbounded search.
Every carrier and loop bound is explicit.

The finite audit set is the complete collection

```text
{d in {-2,-1,0,1,2}^5:sum_k d_k=0},
```

which has 381 states. Universal conclusions come from the written proofs, not
from extrapolating that finite set.

## 13. Frozen systematics

- `g e_k=e_(k+1 mod 5)` and left action;
- cells ordered `0,1,2,3,4`;
- reduced sign pair means nonnegative multiplicities with product zero;
- standard ordinal fibre `[n]={1,...,n}` and `[0]=empty`;
- ordinal labels are fresh at each selected cut;
- no token ancestry or persistence under a general linear map;
- two disjoint tags `S` and `R`;
- coincidence pairs are ordered `(system,record)` pairs;
- complete incidence means the entire within-cell Cartesian product;
- cross-cell pairs are excluded from `C^x` by definition;
- Gram is the algebraic contraction `M_d^T M_d`;
- `q(d)=sum_kd_k^2` and `L(d)=sum_k|d_k|`;
- `A=1+g^2-g^3-g^4`, `U_5=A/sqrt(5)`, and `J=1+g^2`;
- no physical interpretation of `S`, `R`, pair, darkness, or ratio in the
  mathematical claims;
- the physical H row is printed but never tested.

Changing any systematic requires a new identifier and public lock.

## 14. Gates and falsifiers

The accepted verifier has exactly sixteen mathematical/meta gates.

```text
G01  reduced signed ordinal fibres and absolute cardinality
G02  reduced-pair uniqueness and coefficient reconstruction
G03  five-cycle covariance and no token-persistence claim
G04  historical cancellation-survivor ambiguity
G05  disjoint tagged copies with equal marginal sizes
G06  complete Cartesian cardinality d_k^2
G07  equal-sign pair product and empty zero fibre
G08  equality with the diagonal full-copy Gram contraction
G09  exposed vertex and one-zero pair-count lists
G10  combinatorial darkness inside the complete relation
G11  finite normalized ratio equals the square profile
G12  complete/diagonal/arbitrary relation nonselection
G13  integral-A pair-total multiplier five on V
G14  state-dependent single-unit yield witnesses
G15  raw-J totals and normalized-U5 integer-count boundary
G16  H row remains UNTESTED STOP and physical scope remains NONE
```

`SCIENTIFIC-FIRED-A` records an exact failure of the normal-form theorem or
its cancellation boundary. `SCIENTIFIC-FIRED-B` records an exact failure of
the Cartesian cardinality, Gram seam, darkness, finite ratio, relation
nonselection, or scaling ledger. Neither decision changes the H row.

## 15. Frozen successful transcript

```text
SPEC J_COINCIDENCE_RECORD_BOUNDARY_EXACT_V1
MODE RESULT-EXPOSED PROOF-FIRST
CHECK G01 RESIDUAL_FIBRES PASS states=381 signed_ordinal=yes cardinality=absolute_value
CHECK G02 NORMAL_FORM PASS reduced_pair_unique=yes reconstruction=exact
CHECK G03 CELL_COVARIANCE PASS five_cycle_transports_fibres=yes token_persistence=NONE
CHECK G04 CANCELLATION_AMBIGUITY PASS net=1 historical_survivor_choices=2 invariant=cardinality
CHECK G05 TAGGED_COPIES PASS system_record_disjoint=yes equal_marginal_size=absolute_value
CHECK G06 CARTESIAN_CARDINALITY PASS complete_within_cell_pairs=d_k_squared
CHECK G07 SIGN_SQUARE PASS nonzero_pair_sign=positive zero_fibre=empty
CHECK G08 GRAM_SEAM PASS cartesian_counts=diag_Kd_Gram cross_cells=zero
CHECK G09 EXPOSED_WITNESSES PASS vertex=16,1,1,1,1 hole=25,0,25,25,25 totals=20,100
CHECK G10 COMBINATORIAL_DARKNESS PASS complete_pair_cell_empty_iff_d_k_zero
CHECK G11 FINITE_RATIO PASS nonzero_complete_relation_normalizes_to_square_profile
CHECK G12 RELATION_NONSELECTION PASS same_marginals_allow_counts_0_through_n_squared diagonal=n
CHECK G13 A_PAIR_EXTENSIVITY PASS A_star_A=5I-N pair_total_multiplier=5_on_V
CHECK G14 SINGLE_UNIT_NONSELECTION PASS A_l1_ratios=5/2,3 no_state_independent_unit_yield
CHECK G15 SCALE_FORK PASS raw_J_totals=20,30,70,180 U5_normalization_not_integer_count_map
CHECK G16 HYPOTHESIS_FIREWALL PASS physical_row=UNTESTED_STOP computation_cannot_confirm_H
RESULT CLAIM_A J-RESIDUAL-UNIT-NORMAL-FORM CONFIRMED
RESULT CLAIM_B J-COINCIDENCE-CARTESIAN-GRAM-SEAM CONFIRMED
HYPOTHESIS COINCIDENCE-RECORD-FREQUENCY UNTESTED STOP
SCOPE L1_only physical_records=NONE frequency_law=NONE probability=NONE self_location_fact=NONE single_run_randomness=NONE L2-L6=NONE
RESULT OVERALL PASS gates=16 claims=2 hypothesis=1
```

Success requires exit zero, empty stderr, exact byte identity with the later
committed `EXPECTED.txt`, and byte-identical x86_64 and aarch64 replay.

## 16. Action-layer and semantics firewall

1. Reduced units are finite normal-form tokens, not particles or paths.
2. A tagged copy is a finite-set construction, not a physically populated
   system or record register.
3. A complete Cartesian relation is a definition, not an occurrence law.
4. The Gram contraction is algebra, not a physical partial trace or count.
5. Combinatorial darkness is emptiness of the defined set, not a detector
   theorem.
6. A normalized finite ratio is not an empirical frequency or probability.
7. The state-independent factor five belongs to integral `A`, not raw `J` and
   not a literal finite-set action of normalized `U_5`.
8. The probe does not choose between raw `J` and `A/U_5` as the physical step.
9. The H row is not a theorem, definition, result, or registered hypothesis.
10. No apparatus, event stream, occurrence, measurement, observer fact,
    self-location fact, stochastic seed, temporal repetition, modal branch
    measure, collapse, continuous hidden trajectory, or single-run randomness
    is supplied.
11. `QDD-INSTRUMENT-APPARATUS [O]`, the typed L5 source, and the L5-to-L6
    Born reading gate remain open.
12. No physical time, space, gravity, action scale, or L2 through L6 lift is
    made.

The probe cannot be cited as a physical derivation of Born's rule. It isolates
the one row that would turn an exact finite construction into such a proposed
reading.

## 17. Formal order and custody

Before the first formal execution, this `PREREG.md` and the accepted
`verify.py` must be committed and pushed atomically. Their Git blobs,
SHA-256 hashes, byte counts, LF status, and final-newline status must be
recorded in issue #809 after byte-for-byte public remote readback. Static
source inspection and syntax compilation are permitted before the pin.
Importing or executing the accepted verifier is forbidden.

After the readback, invoke the immutable verifier exactly once locally from
repository root. The transport wrapper must make exactly one call equivalent
to

```text
subprocess.run(
    ["python3", "probes/P-J-COINCIDENCE-RECORD-BOUNDARY-1/verify.py"],
    cwd=repository_root,
    env=frozen_environment,
    stdin=subprocess.DEVNULL,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=False,
    check=False)
```

The wrapper must build `frozen_environment` from exactly these literals and
inherit nothing else:

```text
PATH=/usr/bin:/bin
LC_ALL=C
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
PYTHONNOUSERSITE=1
PYTHONSAFEPATH=1
TZ=UTC
```

Immediately before the child call it must compare the verifier hash with
`b2cf94f68bc6d6a2d4963827a27ff733537209a18ea37fd07f35f660d47e4eb5`.
A mismatch emits a preflight record with zero child invocations and is STOP.

After the one child returns, the same wrapper must hash the verifier again,
hex-encode both raw buffers, and emit one sorted compact JSON object directly
to the outer tool stdout. The object must include `capture_complete=true`,
`child_invocations=1`, argv, the seven-field environment, UTC start and end,
return code, pre/post verifier hashes and match flags, and stdout/stderr hex,
byte counts, and SHA-256 hashes. Before emission only lossless envelope
construction is allowed. No decode, validation, classification, presentation,
Base64, JavaScript decoder, temporary file, shell redirection, credential,
token, user path, secret, or ambient environment capture is permitted. A lost
or truncated envelope consumes the pin and may not be retried.

Only after the raw envelope is exposed may it be parsed. Preserve exact stdout
as `EXPECTED.txt`, record neutral metadata in `RUN.md`, and record the frozen
decision in `RESULT.md`. Do not alter either pinned file.

The pull request must change only this probe directory, pass exact x86_64 and
aarch64 replay and the aggregate policy gate, and receive a named manual
security review. Merge is permitted only by merge commit, never squash or
rebase. The probe may not be amended, force-pushed, renamed, resumed, or reused
after the pin.

If no scientific gate completes after the pin, the only abandonment route is
an unchanged pin plus `RESULT.md` with `Status: ABANDONED` and no run files.
That route is unavailable after any completed PASS or FIRED execution.
