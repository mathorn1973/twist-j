# PREREG. P-CARRY-ARITY-CIRCUIT-1

Public lock: issue #314. Base: Public Canon v39, public `main` commit
`4d8558356f2f945b34e9f7fece323771d266585a`; Canon content commit
`ab17b10412d03bf1cd69791fe22c66252502b2d4`.

```text
LAYER:  L1 finite/binary arithmetic only.
TARGET: new CARRY-ARITY-CIRCUIT theorem candidate.
MODE:   proof-first exact theorem; verify.py is audit only.
```

## Frozen definitions

For every integer `n >= 1`, define

```text
V_n = F_2^n,
w(x) = popcount(x),
q_n(x) = binom(w(x),2) mod 2,
P_n = {x in V_n \ {0} : q_n(x)=0},
E_n = {e_1,...,e_n}.
```

Addition in `V_n` is XOR.

A finite subset `P` of an `n`-dimensional F_2-vector space is a **spanning
circuit** when it spans, is dependent, and every proper subset is independent.
A spanning circuit has exactly `n+1` elements and one nonzero linear relation.

## Frozen theorem target

### A1. Weight law

For every integer weight `w >= 0`,

```text
binom(w,2) mod 2 = 0  iff  w mod 4 is in {0,1}.
```

Therefore every coordinate atom is in `P_n`, and the first possible
non-atomic singular layer has weight four.

### A2. Carry arity circuit theorem

```text
P_n is a spanning circuit  iff  n = 4.
```

Equivalently,

```text
|P_n| = n+1  iff  n = 4.
```

The cases are exact:

```text
n < 4:   P_n = E_n, hence independent.
n = 4:   P_4 = {e_1,e_2,e_3,e_4,1_4}; its unique relation is
           e_1+e_2+e_3+e_4+1_4=0, and every four are independent.
n >= 5:  P_n contains E_n and every weight-four vector, hence
           |P_n| >= n + binom(n,4) > n+1.
```

### A3. Bounded pentad consequence

At the selected arity `n=4`, `|P_4|=5`. The existing registered
`CARRY-PENTAD [T]` supplies, at its own fixed-frame scope, the minus-type
quadratic geometry, `O(q_4) ~= S_5`, and the A4/cyclotomic bridge. This probe
does not re-prove, enlarge, or reinterpret that theorem and selects no
particular five-cycle, orientation, exponent, prime-place reading, decoder,
or physics.

## Frozen proof

1. `binom(w,2)=w(w-1)/2`. Checking the four residue classes modulo four gives
   A1 for every integer `w`.
2. If `n<4`, the only nonzero weights available are `1,2,3`. A1 leaves only
   weight one, so `P_n=E_n` and there is no dependence.
3. If `n=4`, A1 leaves weights one and four. Thus
   `P_4=E_4 union {1_4}` and `1_4=sum_i e_i`. This gives one dependence.
   If a four-element subset contains `1_4` and omits `e_j`, then in any
   relation the `e_j` coordinate forces the coefficient of `1_4` to vanish;
   the remaining basis coefficients then vanish. Hence every four-element
   subset is independent and the five-term relation is unique.
4. If `n>=5`, all `n` atoms and all `binom(n,4)` weight-four words lie in
   `P_n`. Since `binom(n,4)>=binom(5,4)=5`, `|P_n|>n+1`. A circuit in an
   n-dimensional vector space has at most `n+1` elements. Hence `P_n` is not
   a circuit.

The proof is the theorem basis. No finite sweep carries the universal claim.

## Frozen fields

```text
EQUATION
  A1-A3 exactly as stated above.

CODE
  probes/P-CARRY-ARITY-CIRCUIT-1/verify.py
  Python standard library only; integers only; deterministic; no floats,
  random, files, network, subprocesses, or environment-dependent output.

CARRIER
  theorem: all n >= 1 by the displayed proof.
  audit: exact enumeration for 1 <= n <= 12, all vectors in F_2^n;
  exact circuit/rank tests for the enumerated carriers; residue audit for
  weights 0 <= w <= 255; exact n=4 pentad and relation checks.

SYSTEMATICS
  no approximation and no dataset. The computation is an audit, not the
  all-n proof. A verifier defect invalidates the formal probe and requires a
  fresh named probe; the theorem may still survive independently.

THRESHOLD
  NEGATIVE on one exact counterexample to A1 or A2, failure of the n=4
  circuit, or a proof gap. STOP on authority/collision/pin/type failure, on
  presenting finite enumeration as the universal proof, or on any attempted
  zeta, adelic, Hilbert-symbol, Redei, Weil, positivity, RH, physical, or
  L2-L6 promotion. Audit PASS requires exit 0, empty stderr, the frozen PASS
  transcript, and byte identity across required architectures.

LAYER
  L1 finite/binary arithmetic only. No lift.
```

## Dependencies and fences

The only public scientific dependency used for A3 is `CARRY-PENTAD [T]` at
its registered scope. A1-A2 are proved from the definitions here and do not
use `p=5`, `J`, `RAMIFIED-TM-LIFT`, a cyclotomic field, a zeta function, or a
physical dictionary.

The criterion "the complete nonzero singular locus is one spanning circuit"
is a frozen arithmetic selection predicate. This probe proves its unique
arity inside the family `q_n`; it does **not** prove that this predicate is the
unique possible notion of carry minimality or is physically forced.

`C-J-DEDEKIND-WEIL-ROAD-N` remains a separate NON-CANONICAL roadmap. All
J-LI/lambda-adic claims retain their scopes unchanged.
