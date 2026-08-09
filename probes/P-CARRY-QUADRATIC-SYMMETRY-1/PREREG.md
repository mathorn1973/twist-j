# PREREG. P-CARRY-QUADRATIC-SYMMETRY-1

Public lock: issue #316. Base: Public Canon v39, public `main` commit
`4d8558356f2f945b34e9f7fece323771d266585a`; Canon content commit
`ab17b10412d03bf1cd69791fe22c66252502b2d4`.

```text
LAYER:  L1 finite/binary arithmetic only.
TARGET: new CARRY-QUADRATIC-SYMMETRY theorem candidate.
MODE:   proof-first exact theorem; verify.py is audit only.
```

## Collision declaration

This target does not claim the numerical identity `2^2+1=5` as new.

- Registered `CARRY-PENTAD [T]` already proves, with order five fixed, that
  four is the least binary linear width admitting an order-five element,
  equivalently `ord_5(2)=4`.
- Historical project work `verify_and_xor_p5.py` recorded the equivalent
  quarter-turn arithmetic `2^2=-1 mod p => p=5`. It is provenance only here,
  not public evidence or a dependency.
- Closed predecessor #314 / PR #315 proved a correct all-n circuit lemma but
  was invalidated for promotion after pin because its selector predicate was
  not independently distinguished and this collision was not declared.
  Nothing from #314 is evidence here; its verifier is not reused.

The new content is the reverse prime-free carry statement: the unique pure
quadratic carry layer has exact period four, first develops non-atomic
singular geometry at arity four, and at that birth its full automorphism group
acts as the complete symmetric group on its singular locus.

## Frozen definitions

For every integer `n >= 2`, define

```text
V_n = F_2^n,
w(x) = popcount(x),
e_r(x) = sum_(i_1<...<i_r) x_(i_1)...x_(i_r),
q_n(x) = e_2(x) = binom(w(x),2) mod 2,
P_n = {x in V_n \ {0} : q_n(x)=0},
E_n = {e_1,...,e_n},
A_n = {g in GL(n,2) : q_n(gx)=q_n(x) for every x}.
```

`S_n` acts by coordinate permutations.

A **pure quadratic Boolean form** here means a squarefree homogeneous
multilinear polynomial of degree exactly two, with zero constant and zero
linear part:

```text
f(x) = sum_(i<j) c_(ij) x_i x_j,   c_(ij) in F_2.
```

This restriction is load-bearing. If arbitrary linear terms are allowed,
`q_n+e_1` is another invariant quadratic refinement. No broader uniqueness is
claimed.

Let `rho_n:A_n -> Sym(P_n)` be the natural permutation action.

## Frozen theorem target

### Q1. Unique pure quadratic carry layer

The `S_n`-invariant subspace of pure quadratic Boolean forms is
one-dimensional, spanned by

```text
q_n = e_2 = sum_(i<j) x_i x_j.
```

Therefore `q_n` is the unique nonzero permutation-invariant pure quadratic
carry layer.

Lucas gives the binary carry hierarchy

```text
bit_r(w) = binom(w,2^r) mod 2 = e_(2^r)(x).
```

Thus the carry layers after `e_2` have degrees `4,8,...`; no higher carry bit
is quadratic.

**Proof.** `S_n` acts transitively on two-element subsets `{i,j}`. Invariance
therefore forces all coefficients `c_(ij)` to be equal. Over `F_2` the
invariant subspace is `{0,e_2}`. The carry hierarchy identity is Lucas'
theorem applied to `w=sum_i x_i`, since `e_m(x)=binom(w,m) mod 2` on Boolean
inputs.

### Q2. Exact period and first non-atomic singular arity

For every integer weight `w >= 0`,

```text
binom(w,2) mod 2 = 0  iff  w mod 4 is in {0,1}.
```

The sequence in `w` therefore has least positive period exactly `4=2^2`:
its period block is `0,0,1,1`, so periods one and two fail.

Consequently every coordinate atom is singular and the first possible
non-atomic singular weight is four. Hence

```text
P_n \ E_n = empty  for n=2,3,
P_4 \ E_4 = {1_4}.
```

Thus `n=4` is the unique minimal arity at which this pure quadratic carry
layer develops any non-atomic singular vector. At that arity

```text
P_4 = {e_1,e_2,e_3,e_4,1_4},
|P_4| = 5 = 2^2+1,
sum_(x in P_4) x = 0.
```

The five is an output cardinality, not an input prime or order condition.

### Q3. Exceptional full-symmetry birth

For all `n >= 2`,

```text
(P_n \ E_n != empty) AND (im rho_n = Sym(P_n))
    iff n=4.
```

At `n=4`, the registered `CARRY-PENTAD [T]` supplies the exact fixed-frame
statement

```text
A_4 = O(q_4) ~= S_5
```

acting as every permutation of the five singular points.

For every `n>=5`, full symmetric action is impossible by order. Since
`A_n <= GL(n,2)`,

```text
|A_n| <= |GL(n,2)| < 2^(n^2).
```

The exact small singular counts are

```text
|P_5|=11, |P_6|=27, |P_7|=63.
```

The order obstruction is

```text
|GL(5,2)| < 2^25 < 11!,
|GL(6,2)| < 2^36 < 27!,
|GL(7,2)| < 2^49 < 63!.
```

For `n>=8`, the weight-four layer gives

```text
|P_n| >= binom(n,4).
```

Prove by induction that

```text
binom(n,4) >= n^2+2  for all n>=8.
```

Base: `binom(8,4)=70 >= 66`. For the step,

```text
binom(n+1,4)-binom(n,4)=binom(n,3) >= 2n+1
```

for `n>=8`, so the bound advances from `n^2+2` to `(n+1)^2+2`.
Therefore

```text
|P_n|! >= 2^(|P_n|-1) >= 2^(n^2+1) > |GL(n,2)| >= |A_n|,
```

and `rho_n` cannot be surjective. This proves Q3 for all `n>=2`.

### Q4. Circuit lemma only as a corollary

The closed predecessor's identity

```text
P_n is a spanning circuit iff n=4
```

is true, but it is not the selector predicate of this probe. It follows from
the same weight law and carries no evidence or promotion authority from #314.

## Exact interpretation boundary

If Q1-Q3 survive, the theorem is exactly

```text
unique pure quadratic carry layer e_2
  -> least weight period 2^2
  -> first non-atomic singular arity 4
  -> exceptional full symmetric action S_5 on 5=2^2+1 singular points.
```

This is a prime-free direction inside the carry hierarchy. It does not make
`2^2+1=5` new and does not identify the output cardinality with a rational
prime selected by Nature.

## Frozen fields

```text
EQUATION
  Q1-Q4 exactly as stated above.

CODE
  probes/P-CARRY-QUADRATIC-SYMMETRY-1/verify.py
  Python standard library only; integers only; deterministic; no floats,
  random, files, network, subprocesses, or environment-dependent output.

CARRIER
  theorem: all n >= 2 by the written proof.
  audit: direct Boolean carriers for 2 <= n <= 10; exact coefficient-orbit
  checks for invariant pure quadratics; Lucas/carry checks for weights
  0 <= w <= 255 and carry bits through degree 8; full GL(4,2) enumeration for
  the n=4 automorphism action; exact singular counts for n=5,6,7; exact
  inequality-bound audit through n=64.

SYSTEMATICS
  no approximation and no dataset. The verifier is an audit only. The owner
  has seen the closed predecessor #314 outcome; that is exposed preparation,
  not evidence. This verifier is newly authored and must not import the
  predecessor verifier.

THRESHOLD
  NEGATIVE on one exact counterexample to Q1, the least-period-four claim,
  first-non-atomic arity, n=4 full symmetry, or all-n>=5 order obstruction.
  STOP on authority/collision/pin/type failure, misuse of the word quadratic,
  undeclared arithmetic collision, presenting finite enumeration as the
  universal proof, any accepted-verifier execution/import before pin, or any
  zeta/physical/inter-layer promotion. Audit PASS requires exit 0, empty
  stderr, the frozen PASS transcript, and byte identity across required
  architectures.

LAYER
  L1 finite/binary arithmetic only. No lift.
```

## Scope firewall

No claim that `q_n` is the only invariant quadratic refinement when linear
terms are allowed. No claim that the full-symmetry-birth criterion is
physically forced or the only conceivable selector. No selection of a C5
subgroup, cyclotomic field, cycle, orientation, exponent, `J`, or step form.
No zeta, Hilbert-symbol, Redei, adelic, Weil, positivity, RH, decoder, measure,
spacetime, force, or L2-L6 claim.

The only scientific dependency is `CARRY-PENTAD [T]` for the bounded n=4
full-symmetry clause. All other statements are proved here from the frozen
definitions.

## Procedure

At claim time no accepted verifier for this probe existed or had been executed
or imported. No `EXPECTED.txt`, `RUN.md`, or `RESULT.md` existed. The prior
notebook-wrapper event belongs only to closed #314 and occurred after that
probe's pin.

The prospective public pin must contain exactly this `PREREG.md` and the newly
authored accepted `verify.py` together. **No execution or import of accepted
`verify.py` before that pin.** After commit and push, remotely read back the
exact commit, blobs, SHA-256 hashes, byte counts, and line endings. After pin,
no amend, rebase, squash, force-push, scope movement, or threshold repair.

Proposed status is `T`, proof-first. The written all-n proof is the theorem
basis; computation remains an audit.
