# P-J-PLENUM-POLAR-GAUSS-1 preregistration

Status: **FROZEN TARGET / RESULT-EXPOSED / PROOF-FIRST / L1 ONLY / PUBLIC
STATUS NONE / NO FORMAL RUN.**

Date: 2026-09-04

Author of record: A. M. Thorn

This probe owns one exact algebraic question. It reconstructs the integral
five-cell plenum carrier, its centered relational lattice, and the polar and
orbit algebra of the raw step `J=1+g^2`. It does not own a probability law,
path ontology, apparatus, outcome, record, or frequency interpretation.

The theorem statements and successful transcript are exposed before
execution. This is a proof-first probe. The accepted verifier is an exact
audit of the finite premises used by the proofs below, not a search for a
surprising pattern.

```text
probe:           P-J-PLENUM-POLAR-GAUSS-1
branch:          probe/P-J-PLENUM-POLAR-GAUSS-1
path:            probes/P-J-PLENUM-POLAR-GAUSS-1/
claim lock:      https://github.com/mathorn1973/twist-j/issues/804
owner:           A. M. Thorn / delegated session 2026-09-04
mode:            RESULT-EXPOSED / PROOF-FIRST
action layer:    L1 exact algebra
public basis:    Public Canon v75
base main:       36293614bbf4c961c4a027155293352a8abad55e
tag:             canon-v75
tag target:      c4f00e1d9c89f503d913224dc3c09dc760dcec9d
content commit:  e32e85ed7297d4320df5b345e4488d78323d550c
canon sha256:    44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
canon bytes:     399513
formal runs:     0 before the atomic pin
public status:   NONE
```

## 1. Authority, collision, and novelty lock

Before issue #804 was opened, `STATUS.md`, `POLICY.md`, `AGENTS.md`,
`canon/CORE.md`, and `canon/FRONTIER.md` were read from the stated public
base. The v75 content commit and activation tag are ancestors of that base,
and the Canon hash and byte count match `STATUS.md`. The aggregate check and
both public architecture jobs on the base passed.

The public issue and pull-request indexes, repository tree, Registry, probe
paths, local refs, and every remote head were searched for the exact probe
and claim names. No formal collision was found. Issue #804 was opened before
the probe directory was created.

The divergent branch `notes/c-j-plenum-born-chain-1-n` and PR #803 expose the
formulas and proposed names. They are NON-CANONICAL design inputs and provide
no authority, claim status, pin, or execution. This probe is therefore
RESULT-EXPOSED. Adjacent PRs #798 and #802 concern different circular-quotient
and QDD dual-simplex carriers. Their results are not reclaimed.

The live frontier row `QDD-INSTRUMENT-APPARATUS [O]` expressly lacks realized
outcomes, event semantics, an occurrence law, and the L5-to-L6 gate. This L1
probe leaves that frontier unchanged.

## 2. Frozen claims and decision rule

```text
claim A: J-PLENUM-POLAR-GAUSS
claim B: J-PLENUM-POLAR-ORBIT-SEPARATION
```

Claim A is confirmed at candidate-T/L1 exactly when gates G01 through G10
pass and the written proof remains valid. Claim B is confirmed at
candidate-T/L1 exactly when gates G01, G03 through G09, and G11 through G16
pass and its written proof remains valid.

Any exact mismatch fires the affected claim. There is no numerical tolerance
and no result-dependent repair. Authority drift, collision, pre-pin execution,
post-pin mutation, custody failure, forbidden dependency, incomplete capture,
nonzero exit, nonempty stderr, transcript mismatch, or architecture mismatch
is `STOP`, not a scientific result.

A successful probe changes no Canon, Registry, Frontier, gate, or status.
Registration, if ever desired, requires a separate sealed Canon fold.

## 3. Frozen carrier and notation

Let

```text
R_Z = Z[C_5] = Z[g]/(g^5-1),
N   = 1+g+g^2+g^3+g^4,
g e_k = e_(k+1 mod 5).
```

Column vectors and left multiplication are used throughout. Put

```text
epsilon(c) = sum_k c_k,
V_Z        = ker(epsilon),
V_R        = V_Z tensor R,
P_0        = N/5,
P_V        = I-P_0.
```

The second occurrences of `N`, `P_0`, and `P_V` denote their five-by-five
circulant matrices. Thus the matrix of `N` is the all-ones matrix. The scalar
product is the ordinary Euclidean product and `g*=g^-1`.

Freeze

```text
J     = 1+g^2,
Gamma = g+g^4-g^2-g^3,
A     = g Gamma = 1+g^2-g^3-g^4,
H     = Gamma/sqrt(5),
U_5   = gH = A/sqrt(5),
B     = (5-Gamma)/(2 sqrt(5)).
```

The Galois marking is

```text
S e_k = e_(3k mod 5),
S g S^-1 = g^3.
```

The multiplier `3` is frozen. The inverse convention `2` may not be silently
substituted. For the exact group calculation the ordered integral basis of
`V_Z` is

```text
f_0=e_0-e_4, f_1=e_1-e_4, f_2=e_2-e_4, f_3=e_3-e_4.
```

All `sqrt(5)` calculations take place in the exact ordered basis `(1,s)` of
`Q(s)`, with `s^2=5` and the distinguished positive embedding `2<s<3`.

## 4. Claim A: centered lattice and exact polar algebra

### 4.1 Centering

For `c in R_Z`, define

```text
D(c)=5c-epsilon(c)N.
```

Since `JN=2N` and `epsilon(Jc)=2 epsilon(c)`, direct expansion gives

```text
D(Jc)=J D(c).
```

If `D(c)=0`, then every coordinate satisfies `5c_i=epsilon(c)`, so all
coordinates of `c` agree. Therefore `ker D=Z N`. Also every pair of
coordinates of `D(c)` is congruent modulo five.

Conversely, let `d in V_Z` have all coordinates congruent modulo five. Choose
an integer `t` with `t=-d_i mod 5` and put `c_i=(d_i+t)/5`. Then
`epsilon(c)=t` because `epsilon(d)=0`, and `D(c)=d`. Hence

```text
im D = {d in V_Z : d_i=d_j mod 5 for all i,j}.
```

The first four columns `D(e_0),...,D(e_3)` generate the image because their
sum with `D(e_4)` is zero. In the frozen `f` basis their determinant is 125.
Thus the supported centered states form a proper full-rank sublattice of
`V_Z` of index `5^3=125`.

The exact five-by-five and restricted determinants are

```text
det(J|R_Z)=2,
det(J|V_Z)=1.
```

### 4.2 Integral Gauss identities and sector qualification

Multiplication in `Z[C_5]` gives

```text
Gamma N=0,
Gamma^2=5-N,
2J-g(Gamma-1)=N.
```

The last identity is the safe full integral statement. Dividing
`Gamma-1` by two without a rational extension or a divisibility proof is not
permitted.

Since `Gamma` is self-adjoint, its normalization obeys on the full real
register

```text
H*=H,
H^2=P_V.
```

It is therefore a self-adjoint involution only after restriction to `V_R`.
The two exact sector projectors are

```text
P_+=(P_V+H)/2,
P_-=(P_V-H)/2.
```

They are self-adjoint orthogonal idempotents with sum `P_V`.

### 4.3 Normalized mixer and positive boost

Because `g` commutes with `Gamma`, direct multiplication gives

```text
U_5* U_5=P_V,
U_5^2=g^2 P_V,
U_5^5=H,
U_5^10=P_V.
```

Restriction to `V_R` turns `P_V` into the identity. None of the first nine
powers is the identity there, so `U_5` has exact order ten and is orthogonal.

Let `phi=(1+sqrt(5))/2` and `phi^-1=(sqrt(5)-1)/2`. On `V_R`,

```text
B      = phi^-1 P_+ + phi P_-,
B^-1   = phi P_+ + phi^-1 P_-.
```

The frozen embedding `2<sqrt(5)<3` makes both coefficients strictly positive.
For nonzero `d in V_R`, orthogonality of the projectors therefore gives

```text
<d,Bd> = phi^-1 ||P_+d||^2 + phi ||P_-d||^2 > 0.
```

Thus `B=B*>0` on the augmentation-zero sector. Exact multiplication then
gives the polar identities

```text
B^2=J*J,
J=U_5B=BU_5                   on V_R.
```

The full-register correction is load-bearing:

```text
U_5B=BU_5=J-(2/5)N.
```

No unqualified full-register identity `J=U_5B` is claimed.

### 4.4 Galois transport and the marked finite group

The frozen permutation gives

```text
S H S^-1=-H,
S B S^-1=B^-1,
S U_5 S^-1=-U_5^3             on V_R.
```

Let

```text
G_mark=<U_5,S> <= GL(V_Q(sqrt(5))).
```

The conjugation relation rewrites every word into one of

```text
(-I)^epsilon U_5^a S^b,
epsilon in {0,1}, 0<=a<10, 0<=b<4.
```

The exact word

```text
U_5^3 S^3 U_5 S=-I
```

places the central sign inside the generated group. The accepted finite
enumeration checks that all 80 displayed matrices are distinct, that they are
the complete generated group, and that its only scalar matrices are `I` and
`-I`. Consequently

```text
|G_mark|=80,
G_mark intersect {alpha I}={I,-I},
|G_mark/{+/-I}|=40.
```

In the projective quotient, `[U_5]` and `[S]` have exact orders ten and four,
and

```text
[S][U_5][S]^-1=[U_5]^3.
```

The 40 distinct projective normal forms prove the marked presentation type
`C_10 semidirect_3 C_4`. These counts belong to the present augmentation
sector. They do not replace the 40/20 census on the different circular
quotient carrier in PRs #798 and #802.

This proves claim A once G01 through G10 audit the displayed finite premises.

## 5. Claim B: integer mixer and orbit separation

### 5.1 Universal integer-mixer norm law

The integral numerator obeys on the full register

```text
A^2=5g^2-N,
A* A=5-N.
```

For `d in V_R`, `Nd=0`; hence

```text
||Ad||^2=5||d||^2,
||A^n d||^2=5^n||d||^2.
```

This is a quadratic-norm multiplier. It is not a count of paths. The four
nonzero signed monomials of `A` give `4^n` labelled terms before collection.
At `n=2` there are 16 such formal words, while the collected coefficient
vector of `A^2` is a shift of `(-1,-1,4,-1,-1)` and has coefficient L1 norm
eight. Coincident endpoints and opposite signs have already combined.

### 5.2 Supported vertex orbit

Take the supported centered vertex

```text
d_0=D(e_0)=5e_0-N=(4,-1,-1,-1,-1).
```

Direct multiplication gives

```text
A d_0=(5,0,5,-5,-5).
```

The identity `A^2=5g^2` on `V` proves by induction

```text
A^(2m)d_0   =5^m g^(2m)d_0,
A^(2m+1)d_0 =5^m g^(2m)(5,0,5,-5,-5).
```

The two algebraic square profiles are therefore shifts of

```text
(16,1,1,1,1) / 20,
(25,0,25,25,25) / 100.
```

Equivalently, the normalized algebraic mixer `U_5=A/sqrt(5)` alternates the
vertex and one-zero profiles and has period ten. The word `profile` here
means only a normalized list of coordinate squares.

### 5.3 Raw step, exact recurrence, and absence of zero cells

Since `d_0=5e_0-N` and `JN=2N`, for every `n>=0`,

```text
J^n d_0=5(1+g^2)^n e_0-2^nN.
```

Every coordinate is congruent to `-2^n mod 5`, which is nonzero. Thus the raw
`J` orbit of this vertex has no zero coordinate at any finite step.

The polar factors commute, `U_5` is orthogonal, and `B` acts by `phi^-1` and
`phi` on the two Gauss sectors. Direct projection gives

```text
||P_+d_0||^2=||P_-d_0||^2=10.
```

Therefore

```text
q_n=||J^n d_0||^2
   =10(phi^(2n)+phi^(-2n)).
```

Since `phi^2+phi^-2=3`,

```text
q_0=20,
q_1=30,
q_(n+2)=3q_(n+1)-q_n.
```

The first nine values are

```text
20, 30, 70, 180, 470, 1230, 3220, 8430, 22070.
```

At the exposed cut `n=8`,

```text
J^8d_0=(29,29,-76,94,-76),
||J^8d_0||^2=22070.
```

More generally, whenever both denominators are nonzero,

```text
||P_-J^n d||^2 / ||P_+J^n d||^2
=phi^(4n) ||P_-d||^2 / ||P_+d||^2.
```

This follows by applying the two scalar actions of `B^n`; the commuting
orthogonal factor `U_5^n` does not change either sector norm.

### 5.4 The boost is visible to coordinate squares

At one step,

```text
B d_0=(2 sqrt(5),-sqrt(5),0,0,-sqrt(5)),
J d_0=(3,-2,3,-2,-2).
```

Their coordinate-square lists are respectively

```text
(20,5,0,0,5),
(9,4,9,4,4).
```

The normalized coordinate-square profiles are different. Therefore the boost
is not invisible to this algebraic readout. Any claim that it is invisible
requires an additional decoder law.

The raw step also lacks a state-independent quadratic-norm multiplier. For

```text
d_1=e_0-e_1,
```

the ratios are

```text
||Jd_0||^2/||d_0||^2=3/2,
||Jd_1||^2/||d_1||^2=2.
```

By contrast, `A` has the universal multiplier five and `U_5` the universal
multiplier one on `V`. This proves a strict algebraic separation among raw
`J`, integral `A`, normalized `U_5`, and positive `B`. It assigns none of
them a physical clock, path count, outcome, or frequency.

This proves claim B once its finite premises pass the frozen gates.

## 6. Accepted program and exact carrier

The accepted program is

```text
probes/P-J-PLENUM-POLAR-GAUSS-1/verify.py
```

Its pre-pin SHA-256 is frozen as

```text
7f7e0fddc72b8e282e77f56d11c6f1f28dff0ac2bac85c45d8beae2db06c8ebc
```

It uses only the Python standard library and exact integer, `Fraction`, and
pair arithmetic in `Q(sqrt(5))`. It has no float, builtin complex arithmetic,
NumPy, SymPy, mpmath, file input, dataset, network, subprocess, shell,
randomness, clock, dynamic import, `eval`, `exec`, environment input, or
unbounded search. The finite group traversal is explicitly stopped beyond
160 elements and such an overflow fires its gate.

There is no empirical dataset. The complete carrier is the displayed
five-cell group-ring matrices, the fixed augmentation basis, the exact
quadratic extension, the supported vector `d_0`, and the comparison vector
`d_1`.

## 7. Systematics

The following are frozen systematic choices:

- column-vector convention and left multiplication;
- `g e_k=e_(k+1 mod 5)`;
- Euclidean adjoint and coordinate squares;
- augmentation-zero restriction exactly where stated;
- the `f_0,...,f_3` basis for the group census;
- positive embedding `2<sqrt(5)<3`;
- Galois multiplier `3`, not `2`;
- linear group before quotienting by exactly `{I,-I}`;
- labelled signed words before coefficient collection;
- raw `J`, integer `A`, normalized `U_5`, and boost `B` kept distinct.

Changing any item requires a new probe identifier and a new public pin.

## 8. Gates and falsifiers

The accepted verifier has exactly sixteen gates.

```text
G01  five-cell carrier, order of g, augmentation projector
G02  centered map, kernel/image premises, index 125
G03  raw-J augmentation multiplier and full/sector determinants
G04  integral Gauss identities and safe quotient equation
G05  normalized Gauss involution and orthogonal sector projectors
G06  normalized mixer, partial-isometry correction, exact order ten
G07  positive-boost spectral decomposition and sector inverse
G08  polar square, commutation, and full-register correction
G09  frozen Galois conjugations
G10  80/40 marked group census, scalar kernel, projective type
G11  integer-mixer square, norm law, signed-word distinction
G12  supported vertex/hole orbit and square lists
G13  raw orbit formula, residue obstruction, exposed n=8 vector
G14  raw norms, golden formula, and recurrence
G15  Gauss-plane scaling and ratio-law premises
G16  boost visibility and state-dependent raw norm ratios
```

`SCIENTIFIC-FIRED-A` means at least one exact premise of the frozen centered,
Gauss, polar, Galois, or group theorem failed. `SCIENTIFIC-FIRED-B` means at
least one exact premise of the frozen orbit-separation theorem failed. A
completed scientific failure exits zero, remains public, and is never
relabeled as abandonment.

## 9. Frozen successful transcript

The exact successful stdout is preregistered as follows:

```text
SPEC J_PLENUM_POLAR_GAUSS_EXACT_V1
MODE RESULT-EXPOSED PROOF-FIRST
CHECK G01 CARRIER PASS g_order=5 rank_V=4 projector=exact
CHECK G02 CENTERING PASS kernel=ZN image=equal_mod_5 index=125
CHECK G03 RAW_J PASS augmentation_multiplier=2 det_full=2 det_V=1
CHECK G04 INTEGRAL_GAUSS PASS GammaN=0 Gamma2=5I-N quotient_identity=safe
CHECK G05 GAUSS_SECTORS PASS H2=P_V projectors=orthogonal_complete
CHECK G06 NORMALIZED_MIXER PASS U5=A/sqrt5 unitary_on_V order=10
CHECK G07 POSITIVE_BOOST PASS eigenvalues=phi^-1,phi positive_on_V=yes
CHECK G08 POLAR PASS B2=JstarJ_on_V J=U5B=BU5 full_correction=2N/5
CHECK G09 GALOIS PASS g_to_g3 H_to_minusH B_to_Binv U5_to_minusU5cubed
CHECK G10 MARKED_GROUP PASS linear=80 scalar_kernel=2 projective=40 type=C10_semidirect_3_C4
CHECK G11 INTEGER_MIXER PASS A2=5g2-N norm_multiplier=5 signed_words=4^n
CHECK G12 SUPPORTED_ORBIT PASS vertex=16,1,1,1,1 hole=25,0,25,25,25 period=10
CHECK G13 RAW_ORBIT PASS formula=5(1+g2)^n_e0-2^nN zero_cells=none n8=29,29,-76,94,-76
CHECK G14 RAW_NORMS PASS q=20,30,70,180,470,1230,3220,8430,22070 recurrence=3q1-q0
CHECK G15 PLANE_SEPARATION PASS Pplus_scale=phi^-1 Pminus_scale=phi ratio_multiplier=phi^4
CHECK G16 ORBIT_SEPARATION PASS boost_profile=20,5,0,0,5 raw_profile=9,4,9,4,4 J_ratios=3/2,2
RESULT CLAIM_A J-PLENUM-POLAR-GAUSS CONFIRMED
RESULT CLAIM_B J-PLENUM-POLAR-ORBIT-SEPARATION CONFIRMED
SCOPE born=NONE probability=NONE outcomes=NONE records=NONE action_layer=L1
RESULT OVERALL PASS gates=16 claims=2
```

Success requires exit zero, empty stderr, byte equality with the later
committed `EXPECTED.txt`, and byte-identical x86_64 and aarch64 replays.

## 10. Action-layer firewall

This probe stops at L1 exact algebra.

1. `4^n` is an unreduced signed-word count only. It is not a path count or a
   population of physical units.
2. `5^n` is a quadratic-norm multiplier only. It is not a frequency count.
3. Coordinate-square profiles are algebraic lists, not probabilities,
   chances, branch measures, event rates, or observed histograms.
4. The centered sublattice is a support condition, not a preparation theory.
5. `BORN-FACE-WEIGHTS [T]` and `MEASURE-BORN-VERB [D]` are neither consumed
   as a physical law nor strengthened.
6. `QDD-INSTRUMENT-APPARATUS [O]`, `QDD-INSTRUMENT-NONSELECTION [T]`, and
   `QDD-J-AFFINE-APPARATUS-NONSELECTION [T]` remain unchanged.
7. No apparatus, effect, event, realized outcome, occurrence law, sampling,
   record, coincidence, decoder completion, self-location, or single-run
   randomness is supplied.
8. No physical time, gravity, SI scale, continuum limit, or L2 through L6
   statement is made.

In particular, this probe cannot be cited as a Born derivation. A later
coincidence construction must independently freeze its unit ontology and
state its one physical frequency premise.

## 11. Formal execution and custody

Before the first formal execution, this `PREREG.md` and the accepted
`verify.py` must be committed and pushed atomically. Their Git blobs,
SHA-256 hashes, byte counts, LF status, and final-newline status must be
recorded in issue #804 after both files are read back byte for byte from the
public remote. Static source inspection and syntax compilation are permitted
before that pin. Importing or executing the accepted verifier is forbidden.

After the public readback, run the immutable verifier exactly once locally
from repository root in a clean deterministic environment. The transport
wrapper must make exactly one child call equivalent to

```text
subprocess.run(
    ["python3", "probes/P-J-PLENUM-POLAR-GAUSS-1/verify.py"],
    cwd=repository_root,
    env=frozen_environment,
    stdin=subprocess.DEVNULL,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=False,
    check=False)
```

The wrapper must construct `frozen_environment` from exactly these literals
and inherit nothing else:

```text
PATH=/usr/bin:/bin
LC_ALL=C
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
PYTHONNOUSERSITE=1
PYTHONSAFEPATH=1
TZ=UTC
```

Immediately before the child call, the wrapper must hash the verifier bytes
and compare them with
`7f7e0fddc72b8e282e77f56d11c6f1f28dff0ac2bac85c45d8beae2db06c8ebc`.
A mismatch emits a preflight record with `child_invocations=0` and is `STOP`.
It must not invoke the verifier.

After the one child returns, the same wrapper hashes the verifier again,
hex-encodes the two raw byte buffers, and emits one sorted compact JSON object
to the outer tool stdout. The envelope must contain
`capture_complete=true`, `child_invocations=1`, child argv, the seven-field
environment, UTC start and end, return code, verifier pre/post hashes and
match flags, and stdout/stderr hex, byte counts, and SHA-256 hashes. Before
emission it may perform only lossless envelope construction. It must not
decode, validate, classify, or present the child transcript. There is no
Base64 field, JavaScript decoder, temporary file, shell redirection, ambient
environment capture, credential, token, user path, or secret in the child or
envelope. A lost or truncated envelope consumes the pin and may not be
retried.

Only after the raw envelope has been exposed may it be parsed and classified.
Preserve exact child stdout as `EXPECTED.txt`, record neutral execution
metadata in `RUN.md`, and record the decision in `RESULT.md`. Do not alter
either pinned file.

The pull request must change only this probe directory, pass the public
x86_64 and aarch64 exact replay, pass the aggregate policy check, and receive
a named manual security review. It may be merged only with a merge commit.
It may not be amended, rebased, squashed, force-pushed, renamed, resumed, or
reused after the pin.

If no scientific gate completes after the public pin, the only abandonment
route is to leave both pinned files unchanged and add only a `RESULT.md` with
`Status: ABANDONED`. That route is unavailable after any completed PASS or
FIRED execution.
