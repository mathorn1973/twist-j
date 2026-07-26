# P-GYRON-DISCREPANCY-LOG-3 predefinition

Date: 2026-07-26.

**NON-CANONICAL PREDEFINITION.** This note records an exact proof surface for
possible Public Canon v23 work. It changes no public claim, status, scope,
evidence row, Canon text, or release identity. It authorizes no issue, probe,
preregistration, formal execution, promotion, or fold.

## 0. Disposition

The proposed successor is `P-GYRON-DISCREPANCY-LOG-3`. It must be freshly
preregistered if the owner decides to open it. No unattached verifier or
transcript is public evidence.

Two earlier incubation candidates remain outside the repository:

- `C-GYRON-DISCREPANCY-LOG-1` recorded a 15/16 result with its frozen
  `|d(L)| <= k + 2` gate fired. The threshold is not moved.
- `C-GYRON-DISCREPANCY-LOG-2` produced 16/16 against its implemented
  predicates, but its prose is not eligible for promotion. With the declared
  domain `N >= 1`, the least counterexample to `d(4N) = d(N)` is `N = 1`,
  not `N = 3`; its minimality gate checked only the values at `N = 3`.
  Its global sector conclusion was also inferred from a finite horizon.

The successor below replaces neither record. It starts from an exact
six-state signed-affine transducer and an all-`k` induction.

## 1. Currency

This note was prepared from the repository at:

```text
STATE             ACTIVE
Public Canon      v22
authority         mathorn1973/twist-j public main
tag               canon-v22
activation commit 91854391ee8529702a5776f028db86dd7fb0bef2
content commit    dd455edf7e10050bad6722f9bafc27fe6359e411
Canon SHA-256     67b1286845434ae6d20edb1d09b7d5c892470be3439c3331b07d8d598a780d21
Canon bytes       113066
registry SHA-256  3c8d46f08fe45ae4d6362d79e0dd423f06f179412d5c7223fd28aa919c21d58b
registry lines    206 including the header, 205 claim rows
```

The tag and content commit are ancestors of public `main`; the recorded Canon
and registry hashes match; the active push, tag, and release checks passed.

## 2. Objects and boundary convention

Let

```text
t_n = s_2(n) mod 2
```

be Thue-Morse. For every prefix length `L >= 1`, let `c_ab(L)` count adjacent
pairs `(t_i,t_(i+1)) = (a,b)` for `0 <= i <= L - 2`, let `n_a(L)` count
letters, and put

```text
S(L) = n_0(L) - n_1(L),
d(L) = 6 c_00(L) - L.
```

The empty pair census at `L = 1` is part of the declared domain:

```text
c_00(1) = 0,  d(1) = -1.
```

Consequently

```text
d(4) = -4 != -1 = d(1).
```

Thus `N = 1` is the least positive counterexample to the unqualified
four-step invariant. If a future probe instead intends `N >= 2`, it must say
so before pinning; only on that different domain is `N = 3` the least odd
counterexample.

## 3. Exact seam and balance identities

Use the Thue-Morse substitution

```text
mu(0) = 01,  mu(1) = 10.
```

The prefix of length `2L` is `mu(t_0 ... t_(L-1))`. Its internal pairs and
seams give, for every `L >= 1`,

```text
c_00(2L) = c_10(L),
c_01(2L) = n_0(L) + c_11(L),
c_10(2L) = n_1(L) + c_00(L),
c_11(2L) = c_01(L).
```

The balance is

```text
S(L) in {-1,0,1},
S(2m) = 0,
S(2m+1) = (-1)^(t_m).
```

Since the word begins in zero,

```text
c_10(L) = n_0(L) - c_00(L) - 1.
```

Substitution in the first seam identity proves the primitive law

```text
d(2L) = -d(L) + 3 S(L) - 6.                    (1)
```

Applying (1) twice and using `S(2L) = 0` proves

```text
d(4L) = d(L) - 3 S(L).                         (2)
```

Therefore, for every positive integer `N`,

```text
d(4N) = d(N)     iff N is even,
d(4N) != d(N)    iff N is odd.
```

This is an L1 integer statement. It supplies no physical density, mass,
measure, decoder, or cross-layer conclusion.

## 4. Six-state signed-affine transducer

For `L >= 1`, define the boundary state

```text
q(L) = (S(L), t_(L-1), t_L).
```

Write `q = (s,a,b)`. Appending one binary digit to the integer `L` means
passing to `2L` or `2L+1`. Equation (1), the appended boundary pair, and the
Thue-Morse recurrences give the exact transitions

```text
q(2L)   = (0, 1-a, b),
d(2L)   = -d(L) + 3s - 6,                      (T0)

q(2L+1) = (1-2b, b, 1-b),
d(2L+1) = -d(L) + 3s - 7
           + 6 [ (a,b) = (1,0) ].              (T1)
```

The initial pair is

```text
q(1) = (1,0,1),  d(1) = -1.
```

Closure under `T0,T1` gives exactly six reachable states:

```text
A = (-1,1,0)
B = ( 0,0,0)
C = ( 0,0,1)
D = ( 0,1,0)
E = ( 0,1,1)
F = ( 1,0,1).
```

No scan of a Thue-Morse word is needed after these transitions are proved.

## 5. All-k extremal certificate

For a binary length `n` and a reachable state `q`, let

```text
I_n(q) = [min d(L), max d(L)]
```

over all `L` with binary length `n` and `q(L) = q`. Exact propagation by
`T0,T1` gives the four base residue classes:

| state | q | `I_5` | `I_6` | `I_7` | `I_8` |
|---|---|---:|---:|---:|---:|
| A | `(-1,1,0)` | `[-5,-3]` | `[-5,-1]` | `[-7,-3]` | `[-5,-1]` |
| B | `(0,0,0)` | `[-6,-6]` | `[-6,-4]` | `[-8,-4]` | `[-6,-2]` |
| C | `(0,0,1)` | `[-4,-4]` | `[-4,-2]` | `[-6,-4]` | `[-4,-2]` |
| D | `(0,1,0)` | `[-2,-2]` | `[0,0]` | `[-2,0]` | `[-2,2]` |
| E | `(0,1,1)` | `[-4,-2]` | `[-2,0]` | `[-4,-2]` | `[-4,0]` |
| F | `(1,0,1)` | `[-3,-1]` | `[-1,1]` | `[-3,1]` | `[-3,3]` |

Four successive transitions have positive sign on `d`: every four-bit path
has the form `d -> d + c`. Exhausting the `16` four-bit paths from each of the
six states gives, for `n = 5,6,7,8`,

```text
I_(n+4)(q) = I_n(q) + [-2,2]                   (3)
```

for every state `q`. The four-step extremum map is translation-equivariant:
uniformly shifting every input minimum or maximum shifts every output by the
same amount. Applying the same exact four-step map to both sides of (3)
therefore proves by induction that (3) holds for every `n >= 5`.

Let

```text
E_k = max_(1 <= L <= 2^k) |d(L)|.
```

The small endpoints are `E_1 = 2` and `E_2 = 4`. For `k >= 3`, the interval
table and (3) give

```text
E_k = 2 ( floor((k+1)/4) + 2 ).                (4)
```

The endpoint `L = 2^k` contributes only `|d(2^k)| = 2` for odd `k` and `4`
for even `k`, so it does not alter (4) for `k >= 3`.

Equation (4) is an all-`k` theorem, not a fit through `k = 24`. In particular,

```text
max_(L <= X) |d(L)| = (1/2) log_2(X) + O(1)
```

along dyadic horizons, and `d(L) = O(log L)` globally.

## 6. Precise sector consequence

The logarithmic bound implies

```text
d(L) / L^epsilon -> 0
```

for every fixed `epsilon > 0`. It therefore excludes any nonzero leading
term of either precise form

```text
L Phi(log_2 L),
L^alpha Psi(log_b L),  alpha > 0,
```

with bounded periodic `Phi` or `Psi` and nonzero amplitude.

This statement is deliberately narrower than "no Takagi-type modulator".
That broad phrase is undefined without specifying the normalization and
function class. The comparison targets are the classical scale types in:

- H. Delange, *Sur la fonction sommatoire de la fonction "somme des
  chiffres"*, L'Enseignement Mathematique 21 (1975),
  DOI `10.5169/seals-47328`;
- J. Coquet, *A Summation Formula Related to the Binary Digits*,
  Inventiones Mathematicae 73 (1983), 107-115,
  DOI `10.1007/BF01393827`.

Those papers concern different summatory functions. They are comparison
classes here, not imported theorems about the gyron pair census.

## 7. Possible public probe

If the owner opens a successor, the public objects should be:

```text
issue:  one named public issue
branch: probe/P-GYRON-DISCREPANCY-LOG-3
path:   probes/P-GYRON-DISCREPANCY-LOG-3/
layer:  L1
```

The preregistration should freeze:

1. equations (1) through (4);
2. the domain `L,N >= 1`, including the `N = 1` boundary;
3. the six reachable states and both signed-affine transitions;
4. the four base interval classes and the four-step translation induction;
5. a verifier that audits the finite certificate without treating a finite
   horizon as proof of the all-`k` statement;
6. two-architecture byte identity before any computation-backed public `T`.

Suggested falsifiers:

```text
DOUBLING:
  one L >= 1 violating a seam identity, the balance law, or equation (1);

FOUR-STEP SCOPE:
  one N >= 1 violating equation (2), its even/odd consequence, or the
  declared least positive counterexample N = 1;

ALL-K EXTREMA:
  one incorrect reachable state, transition, base interval, four-step shift,
  endpoint value, or value of E_k in equation (4);

SECTOR:
  one failure of the proved O(log L) implication, not a moved finite
  threshold or a newly selected sample ray.
```

## 8. Possible v23 disposition

A later owner-reviewed v23 fold may decide to:

1. register the primitive doubling and four-step laws as one exact L1 row;
2. register the all-`k` extremal theorem as a second exact L1 row;
3. keep the sector exclusion as a precise corollary rather than a broad
   "fractal modulator" claim;
4. reconcile the existing `GYRON-DENSITY` wording with equation (2) without
   changing its density `1/6`, stationary vector `(1,2,2,1)/6`, physical
   dictionary consumers, or status;
5. add only dependencies justified by the public probe and proof.

This note proposes no row text, status, evidence hash, history event, generated
artifact, release number, or commit set. Those belong to a fresh fold built
from the then-current public `main`.

## 9. Stop conditions

Stop if a future candidate:

- changes the domain without refreezing the `N = 1` boundary;
- mutates either earlier incubation record or moves its threshold;
- uses a finite scan as the proof of (3) or (4);
- calls a sampled ray an asymptotic limit;
- imports a Delange or Coquet theorem as if it applied directly to this pair
  census;
- promotes a physical density, mass, measure, decoder, or L2-L6 reading;
- treats this note or an unattached transcript as public evidence.
