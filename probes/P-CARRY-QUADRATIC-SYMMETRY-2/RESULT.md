# P-CARRY-QUADRATIC-SYMMETRY-2 result

Status: `THEOREM-CERTIFIED IN THE FROZEN CLASS / PUBLIC REPLAY PENDING /
CANON UNCHANGED`

## Decision

```text
RESULT 9/9 ALL PASS
```

One formal execution returned zero, wrote empty process stderr, and produced
the exact committed ten-line output with all nine gates passing. The accepted
verifier was not executed or imported before its public pin and was not rerun
afterward.

The result repairs only the predecessor's evidence-integrity gap. Closed
claim #316 / closed-unmerged PR #501 remains

```text
STOP / FROZEN CARRIER UNDER-IMPLEMENTED / NO PROMOTION.
```

No old pinned byte, transcript, or result is evidence here.

## 1. The pure quadratic carry layer is unique

For every `n>=2`, a pure quadratic Boolean form has one coefficient for each
two-element coordinate subset. Coordinate permutations are transitive on
those subsets, so invariance forces one common coefficient. Over `F_2`, the
invariant subspace is exactly

```text
{0,e_2}.
```

Thus `q_n=e_2` is the unique nonzero permutation-invariant pure quadratic
carry layer. Lucas' theorem gives

```text
bit_r(w)=binom(w,2^r) mod 2=e_(2^r)(x).
```

For fixed `V_n`, each nonzero layer with `2^r<=n` has ANF degree `2^r`, while
later layers vanish. Therefore every nonzero carry layer after `e_2` has
degree at least four.

## 2. Period four forces the first non-atomic birth at arity four

The exact weight law is

```text
q_n(x)=binom(w(x),2) mod 2=0
    iff w(x) mod 4 is in {0,1}.
```

Its block `0,0,1,1` has least positive period four. Weights two and three are
nonsingular, while weight four is singular. Hence `P_n=E_n` for `n=2,3`, and

```text
P_4={e_1,e_2,e_3,e_4,1_4},
|P_4|=5=2^2+1,
sum_(x in P_4) x=0.
```

Thus four is the unique minimal arity with a non-atomic singular vector. Five
is an output cardinality, not a selected input prime.

## 3. Non-atomic full singular symmetry occurs exactly at the birth

At `n=4`, the registered fixed-frame `CARRY-PENTAD [T]` theorem supplies

```text
A_4=O(q_4)~=S_5.
```

The exact audit independently enumerates every element of `GL(4,2)`, tests all
16 Boolean vectors for every invertible candidate, finds 120 automorphisms,
and compares the induced action set with all 120 permutations of `P_4`.

For `n>=5`, full symmetric action is excluded by order. The direct carrier
enumeration gives

```text
n:       5   6   7    8    9   10
|P_n|:  11  27  63  135  271  527
```

and verifies `|GL(n,2)|<|P_n|!` for each boundary width. For all `n>=8`, the
weight-four layer and the proved induction give

```text
|P_n| >= binom(n,4) >= n^2+2,
```

so

```text
|P_n|! >= 2^(|P_n|-1) > |GL(n,2)| >= |A_n|.
```

Therefore the frozen conjunction is exact:

```text
(P_n \ E_n != empty) AND (im rho_n = Sym(P_n)) iff n=4.
```

The full action alone also occurs in the atomic-only cases `n=2,3`; those
cases fail the first conjunct and are not exceptional non-atomic births.

## 4. The corrected direct carrier is complete

The successor verifier visits every vector in every frozen carrier:

```text
sum_(n=2)^10 |F_2^n| = 2044.
```

For each vector it computes `q_n` independently as the XOR of all pair
monomials and compares that value with both the binomial formula and the
modulo-four residue law. The directly constructed `P_n` objects feed the exact
count and order gate for every `n=5..10`; in particular, the `n=8..10`
carriers are not replaced by the large-`n` inequality.

This closes the sole review blocker from PR #501 without altering or resuming
the sealed predecessor.

## 5. Contextual circuit corollary

The old lemma `P_n is a spanning circuit iff n=4` follows from the same weight
law but is not an additional selector or audit gate. For `n=2,3`, `P_n=E_n`
is a basis. At `n=4`, `E_4 union {1_4}` is minimally dependent. For `n>=5`,
`P_n` contains the proper dependent subset
`{e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4}` while containing the spanning basis
`E_n`, so it is not a circuit.

## 6. Interpretation and evidence boundary

The certified prime-free chain is exactly

```text
unique pure quadratic carry layer e_2
  -> least weight period 2^2
  -> first non-atomic singular arity 4
  -> exceptional full S_5 action on 5=2^2+1 singular points.
```

The collision gate records `5=2^2+1` and `ord_5(2)=4` only after Q1-Q3; those
facts are not inputs to the theorem. No rational-prime selection, `C_5`
selection, cyclotomic choice, orientation, exponent, `J`, or step form follows.
No zeta, Hilbert-symbol, Redei, adelic, Weil, positivity, RH, decoder, measure,
spacetime, force, physical, or L2-L6 claim follows.

After byte-identical public x86_64 and aarch64 replay, a later separate Canon
fold may register at most

```text
CARRY-QUADRATIC-SYMMETRY [T]
```

with exactly the frozen L1 scope. This probe changes no Canon, Registry,
Frontier, Evidence, Gate, workflow, release, or existing theorem row.
