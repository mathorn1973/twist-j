# P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1 preregistration

Status: **FROZEN TARGET / RESULT-EXPOSED / PROOF-FIRST / L1 ONLY / PUBLIC
STATUS NONE / NO FORMAL RUN.**

Date: 2026-09-04

Author of record: A. M. Thorn

This probe owns one exact algebraic conjunction. It asks where a reversible
copying map exists on the marked five-cell register, where that map fails to
factor through the nonorthogonal augmentation simplex, and what follows
conditionally inside the positive-semidefinite quadratic response class.

The word `dilation` names only an algebraic embedding boundary. It does not
name a physical apparatus, instrument, outcome process, or Born reading.

```text
probe:           P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1
branch:          probe/P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1
path:            probes/P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1/
claim lock:      https://github.com/mathorn1973/twist-j/issues/806
owner:           A. M. Thorn / delegated session 2026-09-04
mode:            RESULT-EXPOSED / PROOF-FIRST
action layer:    L1 exact algebra
public basis:    Public Canon v75
base main:       ba728ffb6eea65c3c652ab4ec3a853889e6e590b
tag:             canon-v75
tag target:      c4f00e1d9c89f503d913224dc3c09dc760dcec9d
content commit:  e32e85ed7297d4320df5b345e4488d78323d550c
canon sha256:    44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
canon bytes:     399513
formal runs:     0 before the atomic pin
public status:   NONE
```

## 1. Authority, collision, and novelty lock

The stated base is the merge of PR #805. It leaves the v75 activation tuple
unchanged. The content commit and activation tag are ancestors of the base,
the Canon hash and byte count match `STATUS.md`, and the preceding policy,
x86_64, and aarch64 gates passed.

Before issue #806 was opened, the public issue and pull-request indexes,
repository paths, Registry, commit text, local refs, and every remote head
were searched for the exact probe and claim names. No formal issue, PR,
branch, path, lock, result, or Registry row owned them.

The only exact-name occurrence is section 9.2 of the divergent NON-CANONICAL
branch `notes/c-j-plenum-born-chain-1-n`, also exposed in PR #803. That note
declares the names provisional and authorizes no pin or run. It is a design
input, not authority.

PR #802 already exposed the rational QDD simplex, its tight-frame/projector
facts, and a distinct circular dual-lattice bridge. Those facts are guarded
here but not reclaimed. The divergent branch
`notes/c-qdd-instrument-dilation-1-n` is a v48-era NON-CANONICAL closeout. It
constructs a rational two-outcome controlled dilation and proves that
unrestricted orthogonal-dilation existence does not select a physical
instrument. That analysis is a novelty boundary and supplies no authority.

The registered rows `QDD-INSTRUMENT-NONSELECTION [T]` and
`QDD-J-AFFINE-APPARATUS-NONSELECTION [T]` also remain boundaries. The new
owned content is exactly:

1. the marked five-cell controlled-addition copy on the orthogonal full
   register;
2. the proof that its compressed simplex images cannot arise from a linear
   copy map on the four-dimensional quotient;
3. the exact diagonal algebraic contraction profile before compression;
4. the conditional PSD quadratic support-rigidity implication.

No apparatus or occurrence claim is new or consumed.

## 2. Frozen claims and decision

```text
claim A: J-SIMPLEX-TIGHT-FRAME-DILATION
claim B: J-SIMPLEX-QUADRATIC-SUPPORT-RIGIDITY
```

Claim A is confirmed at candidate-T/L1 exactly when gates G01 through G10 and
G15 pass and the written proof remains valid. Claim B is confirmed at
candidate-T/L1 exactly when gates G01 through G04 and G11 through G15 pass
and the written proof remains valid.

Any exact mismatch fires the affected claim. There is no tolerance or
result-dependent repair. Authority drift, collision, pre-pin execution,
post-pin mutation, custody loss, incomplete capture, forbidden dependency,
nonzero exit, nonempty stderr, transcript mismatch, or architecture mismatch
is `STOP`, not a scientific outcome.

Completion changes no Canon, Registry, Frontier, dependency, dictionary,
gate, or status. Any registration requires a separate sealed Canon fold.

## 3. Frozen carrier

Let `E=Q^5` have its standard orthonormal basis `e_0,...,e_4`. Put

```text
N   = 1 1^T,
P_0 = N/5,
P_V = I-P_0,
V   = ker(1^T),
g e_k=e_(k+1 mod 5).
```

All vectors are columns and the form is Euclidean. Define the five centered
vertices and frame operators

```text
u_k=P_V e_k=e_k-(1/5)1,
E_k=u_k u_k^T,
Pi_k=(5/4)E_k.
```

On `E tensor E`, use lexicographic system-record order

```text
(i,j) -> 5i+j.
```

The controlled-addition permutation is

```text
C_add(e_i tensor e_j)=e_i tensor e_(j+i mod 5).
```

The first tensor factor is named `system` and the second `record` solely to
distinguish the two algebraic factors. Those labels carry no physical
semantics in this probe.

## 4. Inherited simplex and tight-frame guard

Direct projection gives

```text
sum_k u_k=0,
<u_i,u_j>=delta_ij-1/5.
```

The five-by-five Gram matrix is `P_V`, of rank four. Its kernel is exactly the
line spanned by `1`, so the displayed sum is the unique linear relation among
the five vertices.

For the rank-one operators,

```text
sum_k E_k=P_V,
E_k^2=(4/5)E_k,
g E_k g^-1=E_(k+1).
```

If `d in V`, then

```text
<u_k,d>=d_k,
<d,E_k d>=d_k^2.
```

Thus `(u_k)` is a tight frame for `V` and the `E_k` resolve its identity. The
rescaled `Pi_k` are rank-one projectors, but

```text
sum_k Pi_k=(5/4)P_V,
tr(Pi_i Pi_j)=1/16 for i!=j.
```

They are not mutually orthogonal and do not form a PVM. These simplex and
projector facts are an inherited guard against convention drift, not the
novelty claim of this probe.

## 5. Claim A: copy before compression

### 5.1 Full-cell reversible copy

The matrix `C_add` is an integral permutation, has determinant one and exact
order five. With the ready label `e_0`,

```text
C_add(e_k tensor e_0)=e_k tensor e_k.
```

Therefore the induced full-cell embedding

```text
K:E -> E tensor E,
K e_k=e_k tensor e_k
```

is an isometry. For every `d=sum_k d_k e_k`,

```text
C_add(d tensor e_0)=K d=Psi_d=sum_k d_k e_k tensor e_k.
```

This is a reversible algebraic construction on the complete 25-dimensional
carrier. No deletion, collapse, random choice, or external stochastic input
occurs.

### 5.2 Exact algebraic contractions

Write a joint vector as a five-by-five coefficient matrix `M`, with the row
index in the first factor. Define the two algebraic contractions

```text
Gram_system=M M^T,
Gram_record=M^T M.
```

These are ordinary matrix contractions. They are not assigned the physical
meaning of a partial trace.

For `Psi_d`, `M=diag(d_0,...,d_4)`, hence identically

```text
Gram_system(Psi_d)=Gram_record(Psi_d)
                  =diag(d_0^2,...,d_4^2).
```

The accepted verifier proves the quadratic identity by polarization: it
checks every pair of the five columns of `K`, including all cross terms. It
then audits the two exposed lists

```text
d_0=(4,-1,-1,-1,-1):       (16,1,1,1,1), total 20,
h_0=(5,0,5,-5,-5):         (25,0,25,25,25), total 100.
```

These are diagonal Gram entries and quadratic totals, not record counts or
frequencies.

### 5.3 Compression obstruction

Compress both tensor factors after full-cell copying. The five marked images
are

```text
(P_V tensor P_V)K e_k=u_k tensor u_k.
```

Their Gram matrix is the entrywise square of the simplex Gram:

```text
<u_i tensor u_i,u_j tensor u_j>
=<u_i,u_j>^2
=16/25 if i=j, and 1/25 otherwise.
```

This matrix has eigenvalues `3/5` with multiplicity four and `4/5` with
multiplicity one, so it has rank five. Thus the five tensors
`u_k tensor u_k` are linearly independent.

By contrast, the source simplex has rank four and satisfies

```text
sum_k u_k=0.
```

Its proposed copied images satisfy

```text
||sum_k u_k tensor u_k||^2=4,
```

so their sum is nonzero. Any linear map preserves every source relation.
Therefore no linear map

```text
L:V -> V tensor V
```

can obey `L u_k=u_k tensor u_k` for all five labels. In full-register form,
the compressed-copy matrix cannot factor as `L P_V`, since `P_V 1=0` but the
compressed-copy matrix does not annihilate `1`.

This is stronger than a no-isometry statement. No linear simplex-copy map
exists at all. Orthogonal full labels may be copied and then compressed;
compression first removes the relation-free label carrier required by that
copy. The two operations do not commute through a quotient factorization.

This proves claim A once G01 through G10 and G15 pass.

## 6. Claim B: conditional quadratic support rigidity

### 6.1 Frozen hypothesis class

For each cell let

```text
W_k=W_k^T >= 0 on V,
w_k(d)=<d,W_k d>.
```

Each operator is represented by its unique symmetric five-by-five extension
that annihilates the augmentation line. Freeze the three hypotheses

```text
darkness:      d_k=0 implies w_k(d)=0 for every d in V,
covariance:    g W_k g^-1=W_(k+1),
normalization: sum_k W_k=I_V=P_V.
```

Quadraticity and positive semidefiniteness are assumptions of this theorem.
They are not derived from darkness, covariance, or normalization.

### 6.2 Support proof

For `d in V`, `<u_k,d>=d_k`. Hence the dark hyperplane is

```text
H_k={d in V:d_k=0}=u_k^perp,
dim H_k=3.
```

For a positive-semidefinite `W_k`, the bilinear Cauchy-Schwarz inequality
gives

```text
|<x,W_k y>|^2 <= <x,W_k x><y,W_k y>.
```

If `y in H_k`, darkness makes the right side zero, so `W_k y=0`. Thus
`H_k` lies in the kernel. Self-adjointness then places the image in
`H_k^perp=span(u_k)`. Consequently

```text
W_k=c_k E_k,
c_k>=0.
```

The verifier independently checks this one-dimensional kernel statement. In
the 15-dimensional space of symmetric five-by-five matrices it imposes

```text
W_k 1=0,
W_k H_k=0.
```

The exact constraint rank is 14 for every cell, and `E_k` is a nonzero
solution. Therefore the solution line is exactly `Q E_k`.

Covariance and transitivity of `g` make all `c_k` equal. Since
`sum_k E_k=P_V`, normalization gives the common coefficient `c=1`. Therefore

```text
W_k=E_k,
w_k(d)=d_k^2.
```

This is a conditional rigidity theorem inside the frozen PSD quadratic class.
It does not assert that the physical world adopts any hypothesis.

### 6.3 Necessity controls

Darkness is load-bearing. For `0<=t<=1`, put

```text
F_k^(t)=tE_k+((1-t)/5)P_V.
```

Every such family is PSD, cyclically covariant, and normalized:

```text
sum_k F_k^(t)=P_V.
```

For nonzero `d in H_k`,

```text
<d,F_k^(t)d>=((1-t)/5)||d||^2,
```

so exact darkness selects `t=1` within this family.

Positive semidefiniteness is also load-bearing. Choose nonzero `h in H_k` and
define

```text
X=u_k h^T+h u_k^T.
```

Then `X=X^T`, `X1=0`, and `<d,Xd>=0` for every `d in H_k`, but `X` is not a
multiple of `E_k`. Moreover the quadratic form has opposite signs on
`u_k+h` and `u_k-h`, so `X` is indefinite. Darkness alone cannot promote
quadratic vanishing on the hyperplane to operator-kernel vanishing.

The accepted verifier audits `t=0,1/2,1`, the general matrix identities, the
dark witness, the cross-term restriction, and the two opposite signs. The
written formulas carry the full interval and universal implications.

This proves claim B once its frozen gates pass.

## 7. Six preregistration fields

1. **Equation.** Sections 3 through 6 freeze every carrier, map, contraction,
   rank obstruction, hypothesis, implication, and negative control.
2. **Code.** The only accepted verifier is
   `probes/P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1/verify.py`.
3. **Carrier or data.** The complete exact carriers are `Q^5`, its
   augmentation subspace, and `Q^5 tensor Q^5`. There is no dataset.
4. **Systematics.** Basis order, tensor order, cycle direction, contraction
   convention, full-register-before-compression order, PSD quadratic class,
   canonical augmentation extension, and cyclic covariance are fixed.
5. **Failure threshold.** Tolerance is zero. A failed exact condition fires
   every owning claim; custody failure is STOP.
6. **Action layer.** L1 only. L3/L4 are names of a future semantic boundary,
   not earned lifts. L5/L6 are absent.

## 8. Accepted program

The accepted verifier has pre-pin SHA-256

```text
f964e45237315095221dd26f3e331c1e2f01b41920daf2b35e0399e4dbc4dc64
```

It uses only the Python standard library and exact integer/`Fraction`
arithmetic. It has no float, builtin complex arithmetic, NumPy, SymPy,
mpmath, file input, external dataset, network, subprocess, shell, randomness,
clock, dynamic import, `eval`, `exec`, environment input, or unbounded search.
Every carrier and loop bound is explicit.

## 9. Frozen systematics

- `g e_k=e_(k+1 mod 5)` and left action;
- lexicographic tensor order `(i,j)->5i+j`;
- first factor called system, second called record, without physical import;
- algebraic contractions `MM^T` and `M^TM`;
- full orthogonal labels copied before projection;
- both factors compressed by `P_V` in the obstruction;
- Euclidean adjoint on the embedded augmentation sector;
- symmetric operators represented by extensions annihilating `1`;
- positive-semidefinite quadratic response class;
- darkness quantified over the complete real augmentation hyperplane;
- covariance under the transitive five-cycle;
- normalization to `P_V`, the identity on `V`.

Changing any systematic requires a new identifier and pin.

## 10. Gates and falsifiers

The accepted verifier has exactly fifteen gates.

```text
G01  five-cell augmentation carrier and cycle
G02  simplex Gram, rank, and unique relation
G03  tight-frame resolution and coordinate quadratic response
G04  inherited normalized-projector guard
G05  integral controlled-addition permutation
G06  ready-state embedding and full-cell copy isometry
G07  universal diagonal contraction identity by polarization
G08  exposed vertex and one-zero Gram lists
G09  copy-after-compression rank and relation obstruction
G10  entrywise-square Gram and no-simplex-copy conclusion
G11  exact dark hyperplanes
G12  one-dimensional symmetric sector-kernel space
G13  canonical covariant normalized dark family
G14  darkness and PSD necessity controls
G15  copy/compression distinction and action-layer firewall
```

`SCIENTIFIC-FIRED-A` records an exact failure of the full-cell copy,
contraction, or compression-obstruction theorem. `SCIENTIFIC-FIRED-B` records
an exact failure of the conditional PSD support-rigidity theorem. A completed
FIRED result exits zero, remains public, and is never relabeled as abandonment.

## 11. Frozen successful transcript

```text
SPEC J_SIMPLEX_DILATION_BOUNDARY_EXACT_V1
MODE RESULT-EXPOSED PROOF-FIRST
CHECK G01 AUGMENTATION_CARRIER PASS g_order=5 P_V_rank=4 full_cells=5
CHECK G02 SIMPLEX PASS Gram_diag=4/5 offdiag=-1/5 rank=4 unique_relation=sum
CHECK G03 TIGHT_FRAME PASS sum_E=P_V E2=4E/5 response=d_k_squared
CHECK G04 PROJECTOR_GUARD PASS Pi=5E/4 sum=5P_V/4 cross_trace=1/16
CHECK G05 CONTROLLED_ADD PASS integral_permutation=yes order=5 determinant=1
CHECK G06 FULL_CELL_COPY PASS C_add(d_tensor_e0)=sum_dk_ek_tensor_ek isometry=yes
CHECK G07 JOINT_GRAM PASS both_contractions=diag(d_k_squared) universal=polarized
CHECK G08 GRAM_WITNESSES PASS vertex=16,1,1,1,1 hole=25,0,25,25,25 totals=20,100
CHECK G09 COPY_COMPRESSION PASS source_rank=4 target_rank=5 sum_source=0 sum_target_norm2=4
CHECK G10 NO_SIMPLEX_COPY PASS input_Gram_rank=4 output_Gram_rank=5 linear_factorization=impossible
CHECK G11 DARK_HYPERPLANES PASS d_k=0 iff d_in_u_k_perp dimension=3
CHECK G12 KERNEL_RIGIDITY PASS symmetric_sector_kernel_dim=1 generator=E_k
CHECK G13 RIGID_FAMILY PASS PSD_plus_darkness_plus_covariance_plus_sumI implies_Wk=E_k
CHECK G14 NECESSITY_CONTROLS PASS darkness_selects_t=1 PSD_excludes_indefinite_cross=yes
CHECK G15 BOUNDARY_FIREWALL PASS copy_before_compression=yes physical_semantics=NONE
RESULT CLAIM_A J-SIMPLEX-TIGHT-FRAME-DILATION CONFIRMED
RESULT CLAIM_B J-SIMPLEX-QUADRATIC-SUPPORT-RIGIDITY CONFIRMED
SCOPE L1_only Born=NONE probability=NONE apparatus=NONE outcomes=NONE records=NONE physical_partial_trace=NONE L2-L6=NONE
RESULT OVERALL PASS gates=15 claims=2
```

Success requires exit zero, empty stderr, exact byte identity with the later
committed `EXPECTED.txt`, and byte-identical x86_64 and aarch64 replay.

## 12. Action-layer and semantics firewall

1. `C_add` is an algebraic permutation, not a selected physical coupling.
2. The label `e_0` is an algebraic ready vector, not a prepared apparatus
   state.
3. `Gram_system` and `Gram_record` are matrix contractions, not physical
   partial traces, reduced states, observations, or record populations.
4. A diagonal entry `d_k^2` is not a probability, frequency, occurrence,
   count, current, or sampling rate.
5. The no-copy boundary is not a no-cloning claim about an assumed quantum
   theory. It is the displayed rank and relation obstruction for five fixed
   nonorthogonal simplex vectors.
6. The support theorem assumes quadraticity and PSD. It does not derive the
   exponent two among arbitrary response functionals.
7. Exact darkness is an antecedent of a conditional L1 theorem. The physical
   row `EXACT-OUTCOME-NULL-EXCLUSION` is not adopted or advanced.
8. No apparatus or instrument is selected. The registered nonselection rows
   and `QDD-INSTRUMENT-APPARATUS [O]` remain unchanged.
9. No Born rule, physical record, coincidence, event stream, single outcome,
   self-location, raw-yield law, probability, frequency, or decoder completion
   is supplied.
10. No physical time, space, gravity, action scale, or L2 through L6 lift is
    made.

This probe cannot be cited as a physical derivation of Born's rule. It only
prepares an exact algebraic boundary for a later separately locked unit and
coincidence construction.

## 13. Formal order and custody

Before the first formal execution, this `PREREG.md` and the accepted
`verify.py` must be committed and pushed atomically. Their Git blobs,
SHA-256 hashes, byte counts, LF status, and final-newline status must be
recorded in issue #806 after byte-for-byte public remote readback. Static
source inspection and syntax compilation are permitted before the pin.
Importing or executing the accepted verifier is forbidden.

After the readback, invoke the immutable verifier exactly once locally from
repository root. The transport wrapper must make exactly one call equivalent
to

```text
subprocess.run(
    ["python3", "probes/P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1/verify.py"],
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
`f964e45237315095221dd26f3e331c1e2f01b41920daf2b35e0399e4dbc4dc64`.
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
rebase. The probe may not be amended, force-pushed, renamed, resumed, or
reused after the pin.

If no scientific gate completes after the pin, the only abandonment route is
an unchanged pin plus `RESULT.md` with `Status: ABANDONED` and no run files.
That route is unavailable after any completed PASS or FIRED execution.
