# P-CARRY-MOMENT-DEPTH-1

Status: **NON-CANONICAL, prepared preregistration; not executed**.
Action layer: **L1**, exact arithmetic on a declared carrier and supplied uniform
finite words. No physical source, energy account, time arrow, occurrence law,
Canon fold, registry entry or status promotion is asserted.

This document and the accepted `verify.py` must be committed, pushed and read
back at their exact Git identities before the first execution of this probe.
The coordinator records that commit and both SHA-256 values in the run record.
Compilation and static review are allowed before the pin. No scientific
execution, including a shortened discovery run, is allowed before it.

## Prior knowledge and purpose

This is a prospective audit of a written mathematical continuation. It is not a
new blind discovery test of values already seen in prior incubation material.
The review already knew the forward/inverse carry counts, the candidate mean
formula and the displayed 36/64 values. Those earlier source bytes and outputs
remain untouched. Their earlier execution is not retroactively preregistered
by this probe.

The new analytical work supplies the delayed-residue lemma for depths below
four, a finite moment formula whose initial cross moments are predicted without
DP feedback, a rational error bound and the corrected scope of the balanced
minimum. The exact finite checks below audit those statements. Infinite and
universal assertions rest on the separate proof, not on extrapolation from the
finite test inventory.

## Carrier, equation and input measure

Let `O = Z[zeta_5]`, `lambda = 1 - zeta_5`, `J = 1 + zeta_5^2` and
`Q(x) = Tr(x conjugate(x))`. Integral elements use the coefficient basis
`1,zeta,zeta^2,zeta^3`. The two fixed alphabets are

```text
counts:   0, 1, 2, 3, 4       mean mu = 2, variance = 2
balanced: -2, -1, 0, 1, 2     mean mu = 0, variance = 2
```

For a declared algebraic unit `u`, the input is uniform on all `5^N` ordered
words, with independent uniform letters in the chosen alphabet. The initial
carry is zero. With `rep_D` the representative in that alphabet, the update is

```text
a_i     = rep_D(res_lambda(C_i + u b_i))
C_{i+1} = (C_i + u b_i - a_i) / lambda
C_0     = 0.
```

Write `s = rep_D(res_lambda(u))` and `h = v_lambda(u-s)`. The moment theorem is
admitted only when `h` is 1, 2 or 3. Its independently predicted cross moment is

```text
M_D(s) = (1/5) sum_{b in D} b rep_D(s b)
m_i    = M_D(s) for i < h; mu^2 for i >= h.
```

The code never substitutes an observed DP value of `m_i` into its moment
prediction. DP and the closed formula are separate arithmetic calculations.

For `L = lambda conjugate(lambda)`, `S_N = sum_{k=1}^N lambda^-k`,
`G_N = sum_{k=1}^N L^-k`, and
`W_N,h = sum_{i=0}^{min(h,N)-1} L^{-(N-i)}`, the target is

```text
E Q(C_N) = mu^2 Tr((u-1)(conjugate(u)-1) S_N conjugate(S_N))
           + 2 Tr((u conjugate(u)+1) G_N)
           + (mu^2-M_D(s)) Tr((u+conjugate(u)) W_N,h).

Q_infinity(u) = mu^2 Q(u-1) + 2 Q(u/J) + 12.
```

For `N >= h`, the prescribed rational upper bound on the absolute difference
between the finite mean and its limit is, with `r = 40/47`,

```text
mu^2 Q(u-1) (2 r^N + r^(2N))
+ (2 Q(u/J) + 12) r^(2N)
+ abs(mu^2-M_D(s)) (Q(u)+4)
  sum_{i=0}^{h-1} r^(2(N-i)).
```

The proof justifies this choice by `min_sigma |sigma(lambda)| > 47/40`.
The verifier checks the corresponding squared rational inequality exactly.

## Accepted code and independence

The sole executable is the adjacent standalone `verify.py`, written for this
audit. It imports only the Python standard library and loads no earlier
verifier, carry table, private fixture, Canon file or network data.

Its field arithmetic uses polynomial convolution reduced by the fifth
cyclotomic polynomial. DP uses integral carry coordinates. The formula uses
exact `Fraction` arithmetic in the field. The small-word comparison multiplies
the complete input integer once and then extracts output digits, rather than
following the streaming DP.

All scientific predicates use integers or fractions. A false predicate raises
an exception and exits nonzero even under Python optimization. Decimal
rounding, printed `True`/`False` without an enforced failure, convergence judged
by a visual decimal match, and approximate numerical thresholds are excluded.
The only noninteger runtime quantity is the monotonic engineering timer; it is
not part of the scientific result or deterministic stdout.

## Fixed finite inventory

### F1. Ring operations and exact contraction bound

Check the defining cyclotomic relation, the stated unit inverses, the inverse
of lambda, `lambda conjugate(lambda) = 1 + J conjugate(J)`,
`J = zeta phi^-1` and `Q(J^-1) = 6`. Over all 625 coefficient tuples in
`{-2,-1,0,1,2}^4`, compare the trace definition of Q with its Gram formula,
check conjugation involution, and check integral lambda division where admitted.

### F2. Independent DP, prefix moments and finite formula

Audit the following **12** alphabet/unit pairs at every `N = 1,...,100`.

| Alphabet | Units | Declared limit values in the same order |
| --- | --- | --- |
| counts | zeta, phi, J, J^-1, phi^-1 | 64, 64, 36, 64, 76 |
| balanced | zeta, phi, J, J^-1, phi^-1, -phi, -phi^-1 | 24, 40, 20, 40, 20, 40, 20 |

This gives **1,200 exact finite-moment comparisons**. At every step also check
the total weight `5^N`, uniform output marginal, predicted diagonal cross
moment, predicted four-component mean carry, and the delayed residue law:
residue zero before depth h and uniform residue at and after depth h.

The exact tail inequality is checked for every admitted `N >= h`, giving
**1,194 tail checks**. No numerical estimate of a stationary distribution is
substituted for the finite calculation or the analytical limit proof.

### F3. Small complete words and inverse edges

For all 12 pairs, exhaust all words of every length 1 through 4, a total of
**9,360 words**. Check agreement of streaming multiplication with multiplication
of the complete integer word and subsequent digit extraction; full output-word
bijection; the complete carry histogram against DP; every off-diagonal mixed
letter moment; and every centered increment cross-covariance. These comprise
**240 off-diagonal mixed-moment checks** and **120 covariance checks**.

For every newly encountered DP carry, check each of its five exact local
equations and the inverse-edge identity under `C -> -u^-1 C`, with the input
and output digits exchanged. The reported finite edge count is the actual
number checked, not a presupposed coverage claim.

For the counts-alphabet J and J^-1 cases, check the known complete closures:
**1,649 states**, **8,245 edges**, maximum first-reach depth **28**, maximum Q
**274** and **706**, respectively. The test requires actual closure of the
enumerated graph, not merely stable support at the last sampled N.

### F4. Declared 70-unit family and the two minima

Examine the **70 distinct specified parameter triples**
`(sign,k,m)` with sign in `{+1,-1}`, `k = 0,...,4`, and `m = -3,...,3`, for
`u = sign zeta^k phi^m`. Check each displayed inverse and each mixing depth in
both alphabets. The 68 admitted triples split into 56 at depth one and 12 at
depth two. The two rational units are excluded.

On these admitted inputs, the counting formula has minimum 36 exactly at
`(sign,k,m) = (+1,1,-1)` and `(+1,4,-1)`. The balanced formula has minimum 20
at all ten triples with `m=-1`. The proof establishes the corresponding
universal conclusions on its declared class; this finite scan does not prove
the universal quantifier by itself.

### F5. Scope and negative controls

For both rational units `u=+1,-1` and every balanced input letter, verify that
zero carry is preserved and the output is exactly `u b`. This ten-transition
closure is the induction premise for zero carry at every word length. The
unadmitted algebraic functional instead equals 24; it must not be called the
actual mean for these units.

The prediction function must reject `+1`, `-1` and `phi^5` in both alphabets.
Check `phi^5 = 3 + 5 phi` and exact depth four for `phi^5` in each alphabet.
Depth four is an applicability boundary. This test does not assert that a
formula outside its scope necessarily fails at every finite N.

## Systematics and failure rules

The alphabet, measure, initial carry, unit list, maximum lengths, arithmetic,
scope tests and exact equalities above are fixed before execution. The two
alphabets are compared explicitly; no arbitrary-alphabet independence is
claimed. These are counts under a supplied uniform measure, not observed
physical frequencies. Q is an assigned trace quadratic form, not an inferred
Hamiltonian, dissipated energy or gate-work account.

Any failed scientific predicate fires this audit's falsifier, exits nonzero
and preserves the original source and outcome. No expectation or scope may be
changed after the pin to make that run pass. Unhandled program errors likewise
prevent a successful record; they are not silently converted into scientific
evidence. A code correction after execution requires a new probe identifier
and a new pin, with the earlier disposition retained according to POLICY.

The declared engineering ceiling is **540 seconds**, below the repository's
600-second verifier ceiling, with at most **50,000 occupied carry states** in
one DP case. Exceeding either limit exits with code 2 and `INCOMPLETE`, without
scientific success stdout. A complete success requires exit 0, empty stderr,
and the one deterministic JSON stdout. Timing and machine identity are recorded
only in `RUN.md`, not in that stdout.

## Execution and evidence record

After the public source pin has been read back, run from the repository root:

```bash
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-CARRY-MOMENT-DEPTH-1/verify.py
```

Preserve the first exact stdout as `EXPECTED.txt`, with command, source pins,
SHA-256 values, environment, exit code, byte counts and stderr disposition in
`RUN.md`. The result record distinguishes mathematical proof, the completed
finite audit and any physical interpretation. A one-architecture computation
is not two-architecture evidence. The required architecture jobs must use the
same immutable source and match the same committed stdout byte for byte.

At preparation time there is no `EXPECTED.txt`, `RUN.md`, successful execution
claim, second-architecture claim or newly earned public status.
