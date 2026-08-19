# P-DQRC-INTRINSIC-SELECTION-1 preregistration

Status: `PREREGISTERED CANDIDATE / RESULT-EXPOSED / PROOF-FIRST / NO FORMAL RUN`

This probe retains the previously frozen umbrella identifier but narrows its
formal public scope to exactly one sub-target:

```text
R3. DQRC-INTERCEPT-PREPOST-FORK
    [HISTORICAL IDENTIFIER ONLY; NO PRE/POST SEMANTICS]
```

The historical sub-target label is retained for lineage only. The probe does
not identify either integer shift with a pre-update or post-update state. Its
entire target is an exact classification of two explicitly declared L1 word
normalizations.

The result is exposed before execution:

```text
BETA REPARAMETERIZED, NOT SELECTED /
TWO NAMED INTERCEPT NORMALIZATIONS RETURN (0,1)
```

This is the formal, scope-exact spelling of the audit shorthand `INTERCEPT
REDUCED TO ONE NAMED BIT`.

Here "one named bit" means only that the two frozen normalization rules return
the ordered pair `(j_absolute,j_fixed)=(0,1)`. It is not a claim that every
possible intercept convention has been classified, and it does not select
which rule is physical. The universal statements are carried by the written
proofs below. The verifier is a finite exact audit, not a discovery engine.

## Public identity, authority, and action layer

```text
probe:               P-DQRC-INTRINSIC-SELECTION-1
public claim lock:   issue #440
probe owner:         A. M. Thorn / delegated session
branch:              probe/P-DQRC-INTRINSIC-SELECTION-1
path:                probes/P-DQRC-INTRINSIC-SELECTION-1/
initial base:        18f1180b6128c05705ebaa23733a10457aea3d3f
Public Canon:        v54, tag canon-v54
content commit:      0bfd67b47f1f59b1ef232b40a9a7d8e8c7459b0f
Canon SHA-256:       c48254a3c73133244547231bb2cb63ca2f232de64a6f1c26d29a67d8684d88c2
Canon bytes:         281522
action layer:        L1 exact arithmetic and one-sided word combinatorics only
mode:                result-exposed, proof-first; verifier is an exact audit
formal runs:         none
static checks:       Python ast.parse and public text/hash readback only
```

Candidate object for a later, separate Canon fold:

```text
DQRC-SILVER-INTERCEPT-CLASSIFICATION    ceiling T at L1
finite-audit evidence ceiling           C
written-proof candidate ceiling         T only after public proof review
```

No status is earned by this preregistration. A one-architecture finite pass is
at most `C`. The displayed ceiling can be reached only if the all-prefix proof
survives public review; the finite verifier then remains an audit. There is no
physical-origin candidate object at any status.

Possible dependency edges for a later fold are frozen as:

```text
DQRC-SILVER-INTERCEPT-CLASSIFICATION
    REQUIRES DQRC-ORIGIN-NONSELECTION
DQRC-SILVER-INTERCEPT-CLASSIFICATION
    REQUIRES DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY
DQRC-SILVER-INTERCEPT-CLASSIFICATION
    REQUIRES DEF-ACTION-LAYERS
DQRC-SILVER-INTERCEPT-CLASSIFICATION
    BOUNDED_BY BELL-CAUSAL-ACCOUNTING
```

No dependency on `SILVER-RING-FACTS`, `SILVER-SIBLING`,
`BELL-MAGIC-BOUNDARY`, QPAIR, QDD, a Born measure, an apparatus, or a physical
clock is proposed.

## Audit boundary: beta is not a target

The beta audit is disclosed solely to prevent the old umbrella name from being
misread as a successful coefficient-selection probe.

For a separately declared DQRC determinant-line coordinate
`r=c D_DQRC`, invariance under a separately fixed planar rotation whose angle
is not congruent to `0` or `pi` fixes a positive quadratic form up to scale in
the declared `(Q,r)` coordinates. It does not fix the coordinate scale `c`.
Within the separate coordinate declaration `H=Q^2+r^2`, the original
coefficient is merely reparameterized as `beta=c^2`: choosing `beta=4` is
exactly choosing `|c|=2`. A quarter-turn, the symbol `i`, and an extension to
`Q(zeta_8)` are not required to obtain the isotropic shape, and none fixes
`c`.

The public coefficient `D_QPAIR/2`, on its own frozen QPAIR carrier and
determinant line, and its formal square coefficient `1/4`, are read-only audit
sentinels. QPAIR and DQRC retain distinct typed carriers and determinant
lines. No equality or carrier map between them is asserted, and the QPAIR
coefficient is forbidden as a DQRC premise, selector, threshold, dependency,
or evidence.

`DQRC-H-COEFFICIENT-NONSELECTION [T]` remains controlling and unchanged.
The silver word below is the same mechanical word already carried by the
maximal DQRC slope, so its frequency is not an independent beta check. This
probe does not test, reopen, narrow, supersede, amend, falsify, or promote
`F-DQRC-ANTIFIT`. It authorizes no `PROMO-*` package. The verifier contains no
beta gate.

## 1. Frozen carrier, indexing, and equations

All words are one-sided and zero-indexed. Let

```text
alpha = 1/sqrt(2),
M(K) = floor(K/sqrt(2))
     = max {m in N_0 : 2m^2 <= K^2},            K in N_0,
u(k) = M(k+1)-M(k),                             k in N_0.
```

The integer maximum is the accepted implementation. No floating-point square
root is evaluated. On the public DQRC maximal sector `4 Delta=Q^2`, both
registered comparator slopes are `alpha`, so their increment words coincide
and the redundant comparator subscript is dropped here.

For every integer shift `j>=0`, define

```text
M^[j](K) = M(K+j)-M(j),
u^[j](k) = u(k+j).
```

Freeze the substitution and its prolongable fixed word as

```text
tau(1)=110,
tau(0)=1,
w=tau^infinity(1).
```

The exact all-prefix target is

```text
u^[1]=w,
u^[0]=0w.
```

Consequently, for every `K>=0`,

```text
sum_(0<=k<K) u^[0](k) = floor(K/sqrt(2)),
sum_(0<=k<K) u^[1](k) = floor((K+1)/sqrt(2)).
```

## 2. Frozen two-selector class

This probe compares exactly two normalization rules.

### ABSOLUTE-LOWER

The rule accepts a shift precisely when its lower counts preserve the
unshifted absolute head:

```text
A_absolute = {j>=0 : M^[j](K)=M(K) for every K>=0}.
```

Every shift has `M^[j](0)=0`; the rule requires equality with the complete
unshifted prefix-count function for every `K`, not merely agreement at zero.

The target is

```text
A_absolute={0}.
```

### SILVER-FIXED

The rule accepts a shift precisely when its complete increment word is the
prolongable substitution fixed word:

```text
A_fixed = {j>=0 : u^[j]=w}.
```

The target is

```text
A_fixed={1}.
```

Thus a declared rule-label bit can be recorded as

```text
b=0  ABSOLUTE-LOWER, returning j=0,
b=1  SILVER-FIXED,   returning j=1.
```

The theorem is the conditional classification of these two rules. It does not
prove that they exhaust every admissible DQRC reading. Indeed, with
`rho_j={j/sqrt(2)}` one has

```text
M^[j](K)=floor(K/sqrt(2)+rho_j),
```

and, by the standard density theorem for an irrational circle rotation, the
phases `{rho_j:j>=0}` form a dense family modulo one. The raw shift space is
therefore not literally reduced to two phases.

## 3. Exact proof of the all-prefix word identity

Put `v=u^[1]`. The 1-positions of `u` are exactly

```text
floor(m sqrt(2)),    m>=1.
```

Indeed, the `m`-th crossed integer occurs at

```text
k=ceil(m/alpha)-1=floor(m sqrt(2)),
```

where the last equality uses the irrationality of `m sqrt(2)`. Therefore the
1-positions of `v` are

```text
p_m=floor(m sqrt(2))-1,    m>=1.
```

The Beatty sequences of `sqrt(2)` and `2+sqrt(2)` partition the positive
integers because

```text
1/sqrt(2)+1/(2+sqrt(2))=1.
```

For completeness, the needed complementarity follows directly. If
`r,s>1` are irrational and `1/r+1/s=1`, equality
`floor(mr)=floor(ns)=k` would imply

```text
k/r<m<(k+1)/r,
k/s<n<(k+1)/s,
```

and hence the impossible integer inequality `k<m+n<k+1`. The two sequences
are disjoint. The number of their terms not exceeding `N` is

```text
floor((N+1)/r)+floor((N+1)/s)=N,
```

because the two nonintegral summands add to `N+1`. They therefore partition
`{1,...,N}` for every `N`.

It follows that the 0-positions of `v` are exactly

```text
q_m=floor(m(2+sqrt(2)))-1,    m>=1.
```

Under `tau`, an input `0` contributes no zero and an input `1` contributes
exactly one zero, at the end of its image `110`. Through the `m`-th input 1 of
`v` there are `p_m+1=floor(m sqrt(2))` input letters, exactly `m` of which are
ones. The corresponding output zero is therefore at the zero-based position

```text
floor(m sqrt(2))+2m-1
  =floor(m(2+sqrt(2)))-1
  =q_m.
```

These are all the zeros of `tau(v)`, so `tau(v)=v`. The word starts with 1.
Since `tau(1)` begins with 1 and `|tau^n(1)|` tends to infinity, every fixed
word beginning with 1 has `tau^n(1)` as a prefix for every `n`; hence it is
uniquely `w=tau^infinity(1)`. Thus `v=w`. Finally `u(0)=0`, proving as whole
one-sided words

```text
u^[1]=w,
u^[0]=0w.
```

This is an all-prefix equality, not an asymptotic-frequency match.

## 4. Exact proof of the two selector outputs

For `j>=1`,

```text
u^[j]=shift^(j-1)(w).
```

The case `j=0` cannot equal `w` because `u^[0](0)=0` while `w(0)=1`. If a
shift `j>1` satisfied `u^[j]=w`, then `w` would be periodic with period
`j-1`. But its first-`K` number of ones is

```text
M(K+1)-M(1)=floor((K+1)/sqrt(2)),
```

so its limiting density is the irrational number `1/sqrt(2)`. A periodic
binary word has rational density. Therefore

```text
u^[j]=w  iff  j=1.
```

For the absolute lower counts, put `rho_j={j/sqrt(2)}`. Direct separation of
the integer and fractional parts gives

```text
M^[j](K)=floor(K/sqrt(2)+rho_j).
```

At `j=0`, `rho_0=0`, so the absolute counts agree for every prefix. If `j>0`,
irrationality gives `0<rho_j<1`. The following elementary irrational-rotation
argument supplies a `K` with `{K/sqrt(2)}>1-rho_j`. By pigeonhole, for any
`epsilon>0` there is `q>0` with

```text
0<||q/sqrt(2)||<epsilon.
```

Take `epsilon=rho_j` and call the distance `delta`. If
`{q/sqrt(2)}=1-delta`, take `K=q`. Otherwise
`{q/sqrt(2)}=delta`; with `r=floor(1/delta)`, irrationality gives

```text
1-delta<r delta<1,
```

so `K=rq` works. At that prefix,

```text
{K/sqrt(2)}=r delta.
```

Therefore

```text
M^[j](K)=M(K)+1.
```

Consequently

```text
M^[j](K)=M(K) for every K>=0  iff  j=0.
```

The two frozen selectors therefore return exactly `(0,1)`.

## 5. Accepted code and finite audit

The accepted verifier is the sibling `verify.py` frozen in the same public
pin. It uses the Python standard library and integer arithmetic only. It has
no RNG, external input, network access, third-party package, or floating-point
operation.

Frozen implementation constants:

```text
WORD_LENGTH=20000
MAX_SHIFT=32
ABSOLUTE_PREFIX_LIMIT=4000       # K=0,...,3999
AGREEMENT_PREFIX=40
COMPARATOR_MAX=20032             # every integer argument accessed by the audit
```

The finite audit checks:

```text
G1  exact integer comparator inequalities for every n in 0..20032;
G2  the frozen incidence matrix and tau(w)=w through 20000 letters;
G3  u^[0]=0w and u^[1]=w through 20000 letters, together with the two
    exact prefix-sum formulas;
G4  j=1 is the unique shift in 0..32 matching w through 20000 letters;
G5  j=0 is the unique shift in 0..32 preserving all absolute counts
    for K<4000;
G6  the unshifted first-40 agreement count is 16, not 12;
G7  the finite-box survivor-index pair is (0,1).
```

The bounded gates audit the formulas; they do not establish the universal
quantifiers. The proofs in Sections 3 and 4 do that work.

Accepted command after the immutable public pin only:

```text
python3 -B probes/P-DQRC-INTRINSIC-SELECTION-1/verify.py
```

Accepted environment and process contract:

```text
implementation: CPython
version:        3.12.x
optimization:   0
arguments:      none
stdout:         deterministic UTF-8 scientific record
stderr:         empty on success
success exit:   0
integrity exit: 1
science exit:   2
```

`EXPECTED.txt`, `RUN.md`, and `RESULT.md` do not exist at preregistration.
They may be added only after formal execution of the publicly pinned verifier.

## 6. Frozen systematics

1. **Index convention.** Every word and position is one-sided and
   zero-indexed. Switching to one-based positions after pinning fires the
   scope rather than repairing it.
2. **Substitution direction.** The frozen morphism is exactly
   `tau(1)=110,tau(0)=1`; reversal, complement, conjugation, or a different
   prolongable letter is a different probe.
3. **Integer comparator.** The implementation uses
   `max{m:2m^2<=K^2}`. Floating-point agreement is not evidence.
4. **All-prefix versus density.** Equal density or a long common prefix does
   not replace the all-prefix proof.
5. **Finite versus universal evidence.** No finite search establishes either
   uniqueness theorem. The verifier is an audit of the written derivation.
6. **Selector completeness.** Only `ABSOLUTE-LOWER` and `SILVER-FIXED` are
   classified. No complete admissible decoder, clock, or apparatus class is
   asserted.
7. **Typed time firewall.** `j` shifts a DQRC block comparator. It is not a
   one-step pre/post convention for the autonomous map `U`. Any future address
   embedding, semiconjugacy, block stride such as `U^16`, clock zero, event
   onset, or apparatus time requires a separately named bridge gate.
8. **Origin nonselection.** `DQRC-ORIGIN-NONSELECTION [T]` remains valid. The
   existence of two exact but incompatible normalizations illustrates its
   boundary; it does not falsify it.
9. **Beta and anti-fit firewall.** No beta, CHSH, QPAIR, `2sqrt(2)`, or
   anti-fit acceptance condition may be added after the pin.
10. **Layer firewall.** No L2 manifold, L3 boundary, L4 apparatus, L5 event
    stream, L6 measure, physical Bell, locality, signalling, force, or causal
    conclusion is in scope.

## 7. Failure and disposition

The written candidate theorem fires if an exact counterexample invalidates an
all-prefix identity, either universal selector classification, or the
corrected `16/40` count. A bounded verifier mismatch at any frozen gate is a
scientific failure for this audit and exits 2. A wrong interpreter, command,
optimization mode, argument list, or internal verifier invariant is an
integrity STOP and exits 1; it is not a scientific falsification.

Allowed result vocabulary is:

```text
AUDIT-CONSISTENT
AUDIT-MISMATCH
REPARAMETERIZATION-ONLY
STOP
```

No result may say `BETA SELECTED`, `INTRINSIC PHYSICAL SELECTION`, `PROMO`,
`PHYSICAL ORIGIN`, `PRE-U`, or `POST-U`.

## 8. Pin and execution protocol

Before any formal execution:

1. commit exactly this `PREREG.md` and the accepted `verify.py`;
2. push the commit on `probe/P-DQRC-INTRINSIC-SELECTION-1`;
3. read back the public commit and both file bytes;
4. record the full commit SHA and both SHA-256 hashes publicly;
5. only then run the accepted command.

Compilation and static parsing are allowed before the pin. Importing or
executing the verifier, opening formal stdout, or moving a threshold before
the public readback is forbidden. A change to equations, code, word length,
shift range, prefix limit, agreement threshold, selector definitions,
failure conditions, or action layer after execution requires a fresh probe;
it may not be repaired in place.

This probe changes no Canon, registry, frontier, gate, workflow, or existing
probe file.
