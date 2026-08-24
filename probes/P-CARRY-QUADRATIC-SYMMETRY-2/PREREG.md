# PREREG. P-CARRY-QUADRATIC-SYMMETRY-2

Public lock: issue #507. Base: Public Canon v59, public `main` commit
`5e077db1a33924bbaaeb8498046605a21e1b0a0d`; Canon content commit
`5da6b883defebd8edc470db1e2e7ebde095ef20a`.

```text
LAYER:  L1 finite/binary arithmetic only.
TARGET: CARRY-QUADRATIC-SYMMETRY theorem candidate.
MODE:   result-exposed, proof-first exact theorem; verify.py is audit only.
```

## Predecessor integrity disposition and collision declaration

Closed claim #316 / closed-unmerged PR #501 is the sealed predecessor
`P-CARRY-QUADRATIC-SYMMETRY-1`, pin
`6229acdeb8bce1afca61c8f4202821c1ebb2e5d0`. Its frozen `CARRIER`
promised direct Boolean carriers for every `2 <= n <= 10`, but its accepted
verifier directly enumerated the defining carrier only for `n=2..7`;
`n=8..10` received only the inequality audit. It is therefore

```text
STOP / FROZEN CARRIER UNDER-IMPLEMENTED / NO PROMOTION.
```

The old pin, branch, verifier, and `8/8 ALL PASS` transcript remain immutable
audit history. They are result-exposed preparation only, not evidence for this
successor. The `-1` probe is not edited, renamed, resumed, rerun, imported, or
reused. The defect is not a mathematical counterexample to Q1-Q3.

Closed predecessor #314 / PR #315 proved a correct circuit lemma but was
invalidated for promotion after pin because its selector predicate was not
independently distinguished and the adjacent arithmetic collision was not
declared. It is also non-evidence here.

This target does not claim the numerical identity `2^2+1=5` as new.

- Registered `CARRY-PENTAD [T]` already proves, with order five fixed, that
  four is the least binary linear width admitting an order-five element,
  equivalently `ord_5(2)=4`.
- Historical project work `verify_and_xor_p5.py` recorded the equivalent
  quarter-turn arithmetic `2^2=-1 mod p => p=5`. It is provenance only, not
  evidence or a dependency.

The new target is the reverse prime-free carry statement: the unique pure
quadratic carry layer has exact period four, first develops non-atomic
singular geometry at arity four, and at that birth its full automorphism group
acts as the complete symmetric group on its singular locus.

At claim time no issue, pull request, branch, Registry row, indexed path, or
candidate named `P-CARRY-QUADRATIC-SYMMETRY-2` existed.

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

`S_n` acts by coordinate permutations. A **pure quadratic Boolean form** here
means a squarefree homogeneous multilinear polynomial of degree exactly two,
with zero constant and zero linear part:

```text
f(x) = sum_(i<j) c_(ij) x_i x_j,   c_(ij) in F_2.
```

This restriction is load-bearing. If arbitrary linear terms are allowed,
`q_n+e_1` is another invariant quadratic refinement. No broader uniqueness is
claimed. Let `rho_n:A_n -> Sym(P_n)` be the natural permutation action.

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

For each `r` with `2^r <= n`, the nonzero layer `e_(2^r)` has algebraic
normal-form degree exactly `2^r`; layers with `2^r > n` vanish on `V_n`.
Thus every nonzero carry layer after `e_2` has degree `4,8,...`, and no higher
nonzero carry bit is quadratic.

**Proof.** `S_n` acts transitively on two-element subsets `{i,j}`. Invariance
therefore forces all coefficients `c_(ij)` to be equal. Over `F_2` the
invariant subspace is `{0,e_2}`. The carry hierarchy identity is Lucas'
theorem applied to `w=sum_i x_i`, since
`e_m(x)=binom(w,m) mod 2` on Boolean inputs.

### Q2. Exact period and first non-atomic singular arity

For every integer weight `w >= 0`,

```text
binom(w,2) mod 2 = 0  iff  w mod 4 is in {0,1}.
```

The sequence in `w` therefore has least positive period exactly `4=2^2`:
its period block is `0,0,1,1`, so periods one, two, and three fail.

Consequently every coordinate atom is singular and the first possible
non-atomic singular weight is four. Hence

```text
P_n \ E_n = empty  for n=2,3,
P_4 \ E_4 = {1_4}.
```

Thus `n=4` is the unique minimal arity at which this pure quadratic carry
layer develops a non-atomic singular vector. At that arity

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

At `n=4`, registered `CARRY-PENTAD [T]` supplies the exact fixed-frame
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

The exact directly audited singular counts are

```text
|P_5|=11, |P_6|=27, |P_7|=63,
|P_8|=135, |P_9|=271, |P_10|=527.
```

They give `|GL(n,2)| < |P_n|!` for `5 <= n <= 10`.

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

### Q4. Circuit lemma only as a contextual corollary

The closed predecessor's identity

```text
P_n is a spanning circuit iff n=4
```

is true, but it is not the selector predicate, an additional frozen equation,
or an audit gate of this probe. It carries no predecessor evidence or
promotion authority.

**Proof.** For `n=2,3`, the weight law gives `P_n=E_n`, which is a basis and
therefore not a circuit. At `n=4`, the five elements
`E_4 union {e_1+e_2+e_3+e_4}` sum to zero. Removing the all-ones vector leaves
the basis `E_4`; removing `e_i` leaves three other atoms plus a vector whose
`i`-th coordinate is one, so every four-element proper subset is independent.
Thus `P_4` is a spanning circuit. For `n>=5`, `P_n` contains `E_n` and the
proper dependent subset
`{e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4}`; it spans but is not a circuit.

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
  Q1-Q3 exactly as stated above. Q4 is a proved contextual corollary only,
  not an additional frozen decision target or audit gate.

CODE
  probes/P-CARRY-QUADRATIC-SYMMETRY-2/verify.py
  Python standard library only; integers only; deterministic; no floats,
  random, files, network, subprocesses, or environment-dependent output.

CARRIER
  theorem: Q1-Q3 for all n >= 2 by the written proof.
  audit: adjacent-transposition coefficient-pair orbits for n=2..10;
  Lucas/carry checks for weights 0..255 and carry bits through degree 8;
  direct complete enumeration of every x in F_2^n for every n=2..10,
  including independent pair-polynomial, binomial, and residue-law values;
  full GL(4,2) enumeration and exact comparison with all 5! permutations;
  directly enumerated singular counts and exact order obstruction n=5..10;
  complete inequality base, identity, induction-step, and bound audit n=8..64.

SYSTEMATICS
  no approximation and no dataset. The verifier is an audit only. The owner
  has seen the outcomes of #314 and #316/#501; those are exposed preparation,
  not evidence. This verifier is newly authored and does not import, execute,
  or otherwise depend on either predecessor verifier.

THRESHOLD
  NEGATIVE on one exact counterexample to Q1, the least-period-four claim,
  first-non-atomic arity, n=4 full symmetry, or all-n>=5 order obstruction.
  STOP on authority/collision/pin/type failure, misuse of the word quadratic,
  undeclared arithmetic collision, presenting finite enumeration as the
  universal proof, under-implementation of any n=2..10 direct carrier, any
  accepted-verifier execution/import before pin, or any zeta/physical/
  inter-layer promotion. Audit PASS requires exit 0, empty stderr, the frozen
  transcript below, and byte identity across required architectures.

LAYER
  L1 finite/binary arithmetic only. No lift.
```

## Frozen accepted transcript

```text
PASS Q1A coefficient-orbit uniqueness audited for n=2..10
PASS Q1B Lucas carry layers e_1,e_2,e_4,e_8 audited for w=0..255
PASS Q2A second carry bit has exact least weight period 4=2^2
PASS Q2B complete Boolean carriers audited for every x in F_2^n, n=2..10 (2044 vectors)
PASS Q2C first non-atomic singular arity is 4 and P_4 has 5 points
PASS Q3A Aut(q_4) has order 120 and induces every permutation of P_4
PASS Q3B exact carrier counts and order obstruction audited for n=5..10
PASS Q3C binom(n,4)>=n^2+2 and induction step audited for n=8..64
PASS C01 collision control only: 5=2^2+1 and ord_5(2)=4
RESULT 9/9 ALL PASS
```

Q1A computes coefficient-pair orbits under adjacent transpositions. Q2B
must visit all `sum_(n=2)^10 2^n = 2044` vectors, including zero vectors,
and construct every nonzero `P_n`. Q3B consumes those directly enumerated
carriers; direct carriers at `n=8..10` may not be replaced by inequalities.
Q3A compares the induced action set exactly with the set of all five-point
permutations. C01 runs last and is not an input to Q1-Q3. Every gate uses an
explicit non-optimizable requirement rather than Python `assert`.

## Scope firewall

No claim that `q_n` is the only invariant quadratic refinement when linear
terms are allowed. No claim that the full-symmetry-birth criterion is
physically forced or the only conceivable selector. No selection of a `C_5`
subgroup, cyclotomic field, cycle, orientation, exponent, `J`, or step form.
No zeta, Hilbert-symbol, Redei, adelic, Weil, positivity, RH, decoder,
measure, spacetime, force, physical, or L2-L6 claim.

The only scientific dependency is `CARRY-PENTAD [T]` for the bounded `n=4`
full-symmetry clause. All other statements are proved here from the frozen
definitions.

## Procedure

At claim time no accepted verifier for this successor existed or had been
executed or imported. No successor `EXPECTED.txt`, `RUN.md`, or `RESULT.md`
existed.

The prospective public pin must contain exactly this `PREREG.md` and the
newly authored accepted `verify.py` together. **No execution or import of the
accepted `verify.py` before that pin.** After commit and push, remotely read
back the exact commit, both blobs, SHA-256 hashes, byte counts, and LF line
endings. After pin, no amend, rebase, squash, force-push, scope movement,
threshold repair, or accepted-byte change.

Proposed status is `T`, proof-first. The written all-n proof is the theorem
basis; computation remains an audit.
