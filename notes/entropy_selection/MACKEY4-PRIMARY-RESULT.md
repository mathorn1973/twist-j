# C-ENTROPY-MACKEY-OBSTRUCTION-4-N primary result

```text
STATUS:          NON-CANONICAL PRIMARY RESULT
SCIENTIFIC GRADE: UNEARNED
PRIMARY:         13/13 PASS
INDEPENDENT BREAKER: MISSING BY DESIGN IN THIS SESSION
DECISION:        STOP PENDING INDEPENDENT BREAKER
PUBLIC BRIDGE:   ENTROPY-LAYER-BRIDGE remains O / STOP
```

## What the primary route established

### Source

The exact quotient model gives

```text
Q_5 = O/lambda^5,
Q_5 additive type = Z/25 + (Z/5)^3,
|Q_5| = 3125,
J cycle type = 1^1 4^1 20^156.
```

For the finite dyadic factor at substitution level `r`,

```text
c_src(r) = 1 + gcd(2^r,4) + 156 gcd(2^r,20),
          = 158 at r=0,
          = 315 at r=1,
          = 629 for every admitted r>=2.
```

The conclusion therefore retains the preregistered `r>=2` scope.

### Target and common cocycle

The full public generator reconstruction gives 312 size-20 components and one
size-10 component. Each generic half is separately a free regular `D_5`-set.
The singlet half is `D_5/C_2` with stabilizer `{id,ref2}`.

The first raw coordinate inspection showed a mixture of left and right
torsor translations. That was not a falsifier. A fixed basepoint change on the
second half of each generic component, by either `id` or `ref2`, removes the
right translation. The gauge census is

```text
id:   157 components,
ref2: 155 components.
```

After that fixed component coordinate choice, all 312 generic blocks and the
singlet carry the same four edge labels:

```text
(previous half,current bit)
(0,0) -> ref4,
(0,1) -> id,
(1,0) -> id,
(1,1) -> ref0.
```

The two reflections generate `D_5`. Thus the common-cocycle premise survives
the primary reconstruction rather than being assumed from blockwise cycle
types.

### Mackey menu

All eight subgroups were enumerated individually:

```text
D_5,
C_5,
five conjugate C_2 reflection subgroups,
{1}.
```

Their orbit counts on one regular block, the singlet, and the full target half
are

```text
M       regular   singlet   312*regular + singlet
D_5        1         1              313
C_5        2         1              625
C_2        5         3             1563
{1}       10         5             3125.
```

Hence

```text
629 not in {313,625,1563,3125}.
```

The mixed control was also reconstructed. Over the separate menus the equation

```text
312*a + b = 629
```

has the unique solution `(a,b)=(2,5)`. It requires `C_5` on the generic blocks
and the trivial subgroup on the singlet, so it is unavailable to one common
Mackey range. The control confirms that the common cocycle is load bearing.

### Conditional Route A embedding

Normalized additive Haar probability assigns equal mass to every coset of
`lambda^5`, because translations act transitively on the finite quotient and
preserve Haar probability. Therefore

```text
(pi_5)_* h_lambda({q}) = 1/3125.
```

Only together with an almost-everywhere fiberwise bijection and the
Thue-Morse one-letter mass `1/2` does this give

```text
P_*mu({psi}) = (1/2)(1/3125) = 1/6250.
```

The primary result does not claim that exact equivariance alone forces the
uniform pushforward.

## Primary implication, not yet a candidate conclusion

Modulo the written finite-extension Mackey theorem, the primary route excludes
measurable conjugacy in the fixed-depth-five, fiberwise-bijective Route A
subclass.

This does not exclude:

- maps using deeper or variable lambda depth;
- maps that are not fiberwise bijective;
- non-factorizing maps on the full lambda-adic source;
- `r>2` collar classes outside the fixed recon ansatz;
- any general element of `A_A` outside the declared subclass.

It therefore does not prove `A_A=empty` and does not close the public bridge.

## Required next gate

The preregistration requires an independently authored
`mackey4_break.py`. That breaker must:

1. be written by a separate named session without reading
   `mackey4_verify.py`;
2. reconstruct the source through a distinct exact presentation, preferably the
   integer multiplication matrix and Smith normal form;
3. reconstruct the target common cocycle and subgroup menu independently;
4. freeze before comparison;
5. preserve any disagreement as a first-class result.

Until that gate exists and agrees, the only permitted decision is

```text
STOP PENDING INDEPENDENT BREAKER.
```
