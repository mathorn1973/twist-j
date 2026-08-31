# P-FCC-WEIGHTED-SHELL-REMAINDER-1 preregistration

Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / PROOF-FIRST / L2 ONLY

Owner: A. M. Thorn
Public claim: [issue #710](https://github.com/mathorn1973/twist-j/issues/710)
Branch: `probe/P-FCC-WEIGHTED-SHELL-REMAINDER-1`
Directory: `probes/P-FCC-WEIGHTED-SHELL-REMAINDER-1/`
Date: 2026-08-30

This preregistration freezes the complete written proof and accepted exact
certificate audit before the first formal execution. All theorem clauses,
constants and proof were derived before this pin: this is disclosed
result-exposed proof checking, not a blind prediction. Neither the draft nor
the accepted verifier has been executed or imported before this freeze.
Static reading and review are not formal gate executions.

The proposed status is candidate-T by the independent written proof, with
the verifier auditing finite certificates. No public claim promotion occurs
without a separate sealed Canon fold.

## 1. Public authority and inherited boundary

The read-back public authority for this draft is:

```text
STATE:                 ACTIVE
CANON:                 Public Canon v72
MAIN AT READBACK:       cff4c896cbbaf63ebeeec5cf4f50c6fb57b64414
TAG:                   canon-v72
TAG TARGET:            0bc7a623627c4453cc94515ae92880ec75ae7d94
CONTENT_COMMIT:        aac8a3a4aff027beb2b08edbde1ae8e59224914c
CANON_SHA256:          39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70
CANON_BYTES:           374406
READBACK DATE:         2026-08-30
```

The public source is `FCC-WEIGHTED-SHELL-SYMBOL [T]`, at L2 in section 9 of
`canon/CANON.md`, with evidence `probes/P-FCC-WEIGHTED-SHELL-SYMBOL-1/`.
That sealed probe is not resumed, renamed, amended, or reused. The new
candidate consumes only its displayed shells, positive weights, and exact
moments. It does not inherit a spatial carrier selection, temporal rule,
flux, physical normalization, or continuum interpretation.

The v72 statement explicitly claims no global remainder bound. This draft
addresses that previously unproved boundary only as a new candidate result;
the published statement and its scope remain unchanged until a separate
reviewed and sealed public fold. A stronger candidate does not retroactively
enlarge the evidence of the older theorem.

`PHOTON-CONE-CONVERGENCE [O]` remains `ROOT / STOP / FORMAL`.
`PHOTON-MASSLESS-PHASE [O]` is untouched. The terminal
`PHOTON-KAPPA-LEMMA [F]` and `PHOTON-WINDOW-PROOF [F]` are not reopened.

## 2. Fresh identity and claim lock

Before issue #710 was created, exact-ID scans found no collision among all
102 live remote heads, 1612 tracked public-main paths, public-main contents,
286 open/closed issues and 422 open/closed PRs (including head names). The
fuzzy hit #691 reserves the different, sealed predecessor SYMBOL-1 only.

The dedicated issue #710 claims exactly this new remainder scope. The
predecessor is neither resumed nor reinterpreted. This branch has no other
probe. No object, claim, equation or layer ownership is inherited silently.

## 3. Exact datum and equality

For `k=(k_x,k_y,k_z) in R^3`, use ordinary Euclidean dot product and put

```text
N = {2,4,8,10,16},
S_n = {v in Z^3 : v_1^2+v_2^2+v_3^2=n},
(w2,w4,w8,w10,w16) = (6,1,15,1,1),

L(k) = sum_(n in N) w_n sum_(v in S_n) (1-cos(<k,v>)),
s(k) = L(k)/324,
r = |k|,
M_d(k) = sum_(n in N) w_n sum_(v in S_n) <k,v>^d.
```

The function `L` is exactly the negative of the displayed canonical scalar
symbol `S`. Equality is pointwise equality of real functions on all of `R^3`;
polynomial certificate equality is exact coefficient equality over `Q`.
The factor `324=M_2/(2|k|^2)` is an algebraic normalization of this displayed
symbol, not an adopted physical speed, time step, action scale, or SI unit.

The inherited exact finite identities are:

```text
(|S_2|,|S_4|,|S_8|,|S_10|,|S_16|) = (12,6,12,24,6),
M_2 = 648 r^2,
M_4 = 3168 r^4,
M_6 = 21888 sum_i k_i^6 + 63360 sum_(i != j) k_i^4 k_j^2.
```

The pair sum is ordered and contains six monomials. The coefficient of
`k_x^2 k_y^2 k_z^2` in `M_6` is zero. The accepted finite audit recomputes
these moments rather than merely accepting their numbers as assertions.

This is an abstract mathematical examination of one already displayed L2
symbol. It makes no assertion that the complete TWIST-J architecture selects
its ambient `Z^3`, its effective parity sublattice, its weights, its scale,
or any flux.

## 4. Candidate theorem

For every `k in R^3`, the following global inequalities hold:

```text
0 <= r^2-s(k) <= (11/27) r^4,                         (R2)

0 <= s(k)-r^2+(11/27) r^4 <= (38/405) r^6,            (R4)

0 <= s(k) <= 16/9.                                  (B)
```

The complete zero locus is

```text
{k in R^3 : s(k)=0}
  = 2 pi Z^3 union (pi(1,1,1)+2 pi Z^3).              (Z)
```

For every real `epsilon>0`, define the mathematical rescaling

```text
s_epsilon(k) = s(epsilon k)/epsilon^2.
```

Then, for all `k in R^3`,

```text
0 <= r^2-s_epsilon(k) <= (11/27) epsilon^2 r^4,       (S2)

0 <= s_epsilon(k)-r^2+(11/27) epsilon^2 r^4
  <= (38/405) epsilon^4 r^6.                         (S4)
```

In particular, for every `R>=0`,

```text
sup_(|k|<=R) |s_epsilon(k)-|k|^2|
  <= (11/27) epsilon^2 R^4.                          (U)
```

Thus `s_epsilon` converges to the squared Euclidean norm uniformly on every
bounded `k`-ball as `epsilon` tends to zero through positive real values.
This statement concerns only scalar spatial symbols. It is not convergence
of a physical state, measure, spacetime theory, field propagator, or apparatus
readout. No sharpness claim for the displayed constants or bound (B) is
included.

## 5. Self-contained proof

### 5.1 Global scalar certificate

Define the following even smooth real functions:

```text
P2(x) = x^2/2 - 1 + cos(x),
P4(x) = 1 - cos(x) - x^2/2 + x^4/24,
P6(x) = x^6/720 - P4(x).
```

Direct exact differentiation gives

```text
P2''(x) = 1-cos(x) >= 0,
P4''(x) = P2(x),
P6''(x) = P4(x).
```

Each `Pj(0)` and `Pj'(0)` is zero. If a twice continuously differentiable
function `f` on `[0,infinity)` has `f(0)=f'(0)=0` and `f''>=0`, then

```text
f(x) = integral_(t=0)^x (x-t) f''(t) dt >= 0
```

for every `x>=0`. Apply this identity first to `P2`, then to `P4`, then to
`P6`. Evenness extends their nonnegativity to every real `x`.

The identities

```text
P2(x)+P4(x) = x^4/24,
P4(x)+P6(x) = x^6/720
```

therefore imply, globally on `R`,

```text
0 <= P2(x) <= x^4/24,
0 <= P4(x) <= x^6/720.                              (C)
```

This uses the exact real inequality `1-cos(x)>=0` and elementary integration.
It is not a power-series truncation with an unnamed or local remainder.

### 5.2 Sum the certificates with positive weights

Substitute `x=<k,v>` in (C) and sum over all weighted shells. The inherited
moments give

```text
sum_(n,v) w_n P2(<k,v>) = 324 r^2-L(k),

0 <= 324 r^2-L(k) <= M_4(k)/24 = 132 r^4.            (P2-SUM)
```

Similarly,

```text
sum_(n,v) w_n P4(<k,v>) = L(k)-324 r^2+132 r^4,

0 <= L(k)-324 r^2+132 r^4 <= M_6(k)/720.             (P4-SUM)
```

For the last bound define

```text
A = sum_i k_i^6,
B = sum_(i != j) k_i^4 k_j^2,
C = k_x^2 k_y^2 k_z^2.
```

Then `r^6=A+3B+6C`, while `M_6=21888A+63360B`. Hence

```text
21888 r^6-M_6 = 2304 B+131328 C >= 0.               (M6-CERT)
```

The right side is nonnegative because each monomial has only even powers and
both coefficients are positive. Combining (P2-SUM), (P4-SUM), and (M6-CERT),
then dividing by 324, proves (R2) and (R4), with exact constants

```text
132/324 = 11/27,
21888/(720*324) = 38/405.
```

### 5.3 Global boundedness

Every summand `1-cos(<k,v>)` lies in `[0,2]`, and the weighted cardinality is

```text
6*12 + 1*6 + 15*12 + 1*24 + 1*6 = 288.
```

Therefore `0<=L(k)<=576` for every `k`. Division by 324 gives (B).

### 5.4 The support lattice and complete zero locus

Every summand of `L` is nonnegative and every weight is strictly positive.
Consequently `L(k)=0` if and only if

```text
<k,v> in 2 pi Z for every vector v in every shell.   (DUAL)
```

For any shell vector, reduction modulo two gives

```text
v_1+v_2+v_3 = v_1^2+v_2^2+v_3^2 = n = 0 mod 2.
```

Thus the integer span of the support is contained in

```text
D3 = {x in Z^3 : x_1+x_2+x_3 is even}.
```

The shell `S_2` contains

```text
b1=(1,1,0), b2=(1,-1,0), b3=(1,0,1).
```

Their column matrix `B0` has determinant `-2`. More explicitly, for every
`x in D3`,

```text
x = ((x_1+x_2-x_3)/2) b1
  + ((x_1-x_2-x_3)/2) b2
  + x_3 b3.                                         (SPAN)
```

The two half expressions are integers precisely because the coordinate sum
is even. Equation (SPAN) proves that the support spans all of `D3`, without
assuming that `D3` is the physically selected carrier.

The three basis vectors in (DUAL) impose

```text
k_1+k_2 in 2 pi Z,
k_1-k_2 in 2 pi Z,
k_1+k_3 in 2 pi Z.
```

The first two conditions imply that `k_1,k_2` are integer multiples of `pi`
with the same parity. The third makes `k_3` an integer multiple of `pi` with
that same parity. This is precisely the union in (Z). Conversely, either
displayed parity class pairs into `2 pi Z` with every vector whose coordinate
sum is even, so both classes satisfy (DUAL). This proves both inclusions and
the completeness of the zero locus.

For a rational dual-basis audit, the exact matrix

```text
D = [[ 1/2,  1/2, 0],
     [ 1/2, -1/2, 0],
     [-1/2, -1/2, 1]]
```

obeys `B0^T D=I`. Its first two columns have common half-integer residue
modulo `Z^3`; the third is integral. Thus the dual modulo `Z^3` has precisely
the zero class and the class `(1/2,1/2,1/2)`.

There are exactly two zeros on the displayed `Z^3` Fourier torus
`R^3/(2 pi Z^3)`. This is a statement about the symbol's support lattice, not
a photon multiplicity, polarization count, or physical degree of freedom.
Quotienting instead by the reciprocal lattice `2 pi D3*` would identify the two
representatives, but adopting that different carrier is outside this theorem.

### 5.5 Exact scaling bound

In (R2) and (R4), replace `k` by `epsilon k`, then divide by
`epsilon^2>0`. This proves (S2) and (S4) for every positive `epsilon`, not
only sufficiently small values. The absolute error in (S2) is bounded by
`(11/27) epsilon^2 R^4` whenever `|k|<=R`. Taking the supremum proves (U)
and its compact-uniform convergence consequence.

## 6. Frozen six fields

### Field 1: equation

Exactly the datum and pointwise real equality in section 3, and assertions
(R2), (R4), (B), (Z), (S2), (S4), (U) in section 4, with the complete proof
in section 5. There is no temporal recurrence, characteristic cone,
physical carrier selection, phase or apparatus interpretation in this claim.

### Field 2: accepted code

```text
file:           probes/P-FCC-WEIGHTED-SHELL-REMAINDER-1/verify.py
sha256:         9cf242aeecdd5ae1d1fef3bf80b3a12dd37b01648988f4eaf4fae62eb80452b6
bytes:          15691
dependencies:   Python standard library only
arithmetic:     integer and fractions.Fraction; no floating point
input:          none
command:        python3 probes/P-FCC-WEIGHTED-SHELL-REMAINDER-1/verify.py
```

The complete code was independently read and accepted before the pin.
It enumerates complete shells and computes exact polynomial, derivative,
basis, parity and scaling certificates. It does not numerically sample
momenta or epsilons. Section 5, not the code, owns real nonnegativity by
integration, the real cosine zero criterion and taking uniform suprema.

The sixteen gates are frozen:

```text
G01 complete-shell-census-and-positive-weights
G02 weighted-cardinality-288
G03 complete-quadratic-moment
G04 complete-quartic-moment
G05 complete-sextic-moment-including-mixed-zero
G06 scalar-second-derivative-chain
G07 scalar-evenness-initial-values-additive-identities
G08 nonnegative-even-monomial-M6-gap
G09 exact-normalization-and-global-bound-constants
G10 complete-support-lattice-D3-certificate
G11 exact-dual-basis-and-two-cosets
G12 scaling-degrees-two-four-six
G13 negative-weight-and-missing-vector-controls-rejected
G14 negative-scalar-sign-and-bound-constant-controls-rejected
G15 negative-dual-control-rejected-despite-same-residues
G16 negative-scaling-exponent-control-rejected
```

Successful scientific stdout is buffered until all sixteen gates and ASCII
validation pass. Success requires exit 0 and empty stderr. Extra arguments
produce fixed STOP stderr and exit 2; a caught audit exception produces
fixed STOP stderr and exit 1. No files, network, environment, random source
or external dataset are read by the verifier; it writes only its transcript.

### Field 3: carrier and data

`k in R^3`, the Euclidean dot product, the five complete integer shells,
the fixed positive weights and normalization `s=L/324`. All shell
vectors lie in `[-4,4]^3` by squared norm at most 16. Coefficient equality
is over Q. The parameter epsilon is positive real and purely mathematical.
No numerical tolerance, measurement or imported source bytes enter.

The effective support span D3 and its reciprocal lattice are derived
mathematical facts about this fixed symbol, not selected physical carriers.

### Field 4: systematics and controls

Freeze positivity; complete shell enumeration; all polynomial coefficients
including zeros; the six ordered-pair sextic monomials; signs and exact
constants of both remainders; both real inclusions in (Z); distinction
between R^3, the displayed Z^3 Fourier torus and the D3 reciprocal quotient;
and positive-epsilon scaling of every term.

Negative controls change weight 6 to 7, omit vector (1,1,0), reverse the
quartic scalar sign, change 38/405 to 37/405, reverse 11/27, corrupt the
dual matrix while preserving its residue classes, and use an incorrect
epsilon exponent. The same certificate predicates must reject these
mutations. They never change the frozen positive datum.

Finite momentum grids cannot prove the global assertions, parity grids
alone cannot prove the real zero locus, and finitely many epsilon values
cannot prove uniform convergence. The written arguments supply completeness.
Prior analytical exposure is explicit. No new physical interpretation or
threshold may be selected after seeing the formal output.

### Field 5: failure threshold and dispositions

The success condition is the conjunction of every frozen theorem clause,
its complete proof, all sixteen exact gates and formal reproducibility
requirements. No approximate tolerance is admitted.

```text
REMAINDER-PROVED
  All clauses are proved, all exact certificates pass and required formal
  evidence gates pass. Candidate-T only until a separate public fold.

REMAINDER-REFUTED
  An independently checked exact counterexample or mathematical negation
  breaks a frozen inequality, coefficient, support-span identity, zero-locus
  inclusion/completeness assertion or scaling bound. Preserve the claim
  and witness; never move the threshold.

STOP
  Missing authority, claim ownership, typing, accepted code, usable Linux
  route, immutable public pin/readback, exact transcript, architecture
  agreement or security review. An execution or transcript defect without
  an exact mathematical negation is STOP, not REMAINDER-REFUTED.
```

If a pinned gate never completes, the policy's ABANDONED disposition is
mandatory: unchanged pinned files plus RESULT, no invented EXPECTED or RUN,
and the identifier is consumed. A completed scientific falsifier is
preserved, not relabelled or hidden. No pinned probe is resumed, renamed,
amended, rebased, squashed or force-pushed.

Neither outcome decides either photon successor root. Failure of a
provisional unselected interpretation is outside this falsifier.

### Field 6: action layer

```text
L2 ONLY: one unselected abstract spatial symbol and exact real bounds.
```

The map k -> epsilon k stays in the same L2 function domain. It is not an
architecture-to-physical-continuum lift. No L2-to-L5 or L4-to-L5 gate is
executed or closed, and no L6 measure is constructed.

## 7. Pinned execution and evidence route

An isolated Linux/aarch64 checkout with CPython 3.12.3 was verified available
before this freeze. It receives the accepted files through public Git,
not by copying an unattached verifier. No unrelated checkout is used.

1. Commit and push exactly this PREREG and accepted verify.py.
2. Record commit, single parent, blobs, file hashes and byte counts, and
   read both files back at that exact public commit before execution.
3. Fetch and check out that pin in the isolated Linux checkout. Require a
   clean tree, unchanged file hashes and the declared authority ancestry.
4. Execute the command in Field 2 from the repository root with
   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
   Capture raw stdout and stderr separately and preserve the exit code.
5. Only after a completed run, add exact stdout as EXPECTED.txt and neutral
   RUN.md fields (pin, command, environment, platform, architecture, Python,
   exit code, hashes, bytes and line count). Add RESULT.md without changing
   the pinned files.
6. Open one-probe PR; require its exact head to pass the x86_64 and aarch64
   jobs and aggregate check, with byte identity to that one EXPECTED.
7. Review security, exact scope and pin ancestry, merge with a merge commit,
   then publicly read back the merged result. Canon promotion requires a
   separate declared fold.

EXPECTED is actual post-pin stdout, never manufactured from this text.
The local lane is aarch64; the independent proof is the theorem basis.
Architecture agreement audits reproducibility, not universal calculus.

## 8. Scope firewall

No carrier, quotient, weights, physical scale or flux is selected; no
temporal transfer, time step, temporal characteristic, Herm2 cone, Lorentz
invariance or physical continuum is obtained; no Gibbs measure, massless
phase, propagator, polarization count, photon multiplicity, decoder,
apparatus readout or SI quantity is proved.

PHOTON-CONE-CONVERGENCE and PHOTON-MASSLESS-PHASE remain [O].
PHOTON-KAPPA-LEMMA and PHOTON-WINDOW-PROOF remain terminal [F].
Canon, registry, evidence, dependency and gate files are unchanged.

The exact new contribution is global signed remainder control, the complete
support-derived zero locus, and compact-uniform mathematical scaling for
the one displayed spatial L2 scalar symbol.
