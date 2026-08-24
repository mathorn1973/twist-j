# Derivation

Status: candidate-T, NON-CANONICAL incubation.

Let

```text
X = K_QDD,
q = Q_QDD o beta_QDD : X -> QCarrier_QDD,
D = D_QDD_direct : X -> MatterData_QDD.
```

The proof uses the frozen direct cyclotomic dictionary. It does not use `F_QDD`, the effect pair, or the Born pairing as premises.

## 1. Equality of fibres

If `q(x)=q(y)`, write `v=beta(x)` and `w=beta(y)`. On the rational carrier the two typed slots both equal the rank-one matrix, so

```text
v v^T = w w^T.
```

Over `Q`, this implies either `v=w=0` or `w=+v` or `w=-v`. The direct write is even under `v -> -v`, because total weight and raw branch weights are quadratic and `T_(-w)=T_w`. Therefore `D(x)=D(y)`.

Conversely, assume `D(x)=D(y)`. The support tags first separate the zero branch. On the supported branch the complete record contains equal total weights `m` and equal density matrices `rho`. Direct field arithmetic gives

```text
rho = A G / m,        A=v v^T.
```

Since `G` is invertible,

```text
A = m rho G^-1.
```

Thus equal records give equal `A`, hence equal `q`. Therefore

```text
D(x)=D(y) iff q(x)=q(y).
```

## 2. Exact quotient and census

The 625 piston vectors give one zero quadratic class and 312 sign pairs. The two ignored head coordinates contribute 25 pointed heads per piston. Hence the common fibre partition has

```text
313 classes,
one class of size 25,
312 classes of size 50.
```

Define

```text
F_set(q(x))=D(x).
```

The equality theorem makes this well defined. It is injective and surjective onto `im(D)`, so

```text
X/Eq_D  ~=  QCarrier_QDD  ~=  im(D)
```

canonically as finite typed sets.

## 3. Universal factor property

A reduced exact factorization is a surjective `f:X->C` and a map `g:C->MatterData_QDD` with `D=g o f`.

If `f(x)=f(y)`, then `D(x)=D(y)`, hence `q(x)=q(y)`. Therefore

```text
h(f(x))=q(x)
```

defines a map `h:C->QCarrier_QDD`. It is unique because `f` is surjective. Moreover

```text
F_set(h(f(x)))=F_set(q(x))=D(x)=g(f(x)),
```

so `g=F_set o h`. Thus the public quadratic factor object is terminal among reduced exact factorizations of the frozen direct record.

The map `h` is surjective because `q=h o f` and `q` is surjective. Consequently every reduced exact factor carrier has at least 313 elements. If it has exactly 313, `h` is bijective and gives the unique factor isomorphism to `QCarrier_QDD`.

## 4. Scope boundary

The complete scale-bearing record is essential. Density alone identifies `v` and `2v`; the exact audit finds only 273 density classes. The theorem is conditional on the adopted direct Route A dictionary and its equality. It does not make that dictionary physical, close `D_matter`, or supply Born, apparatus, event, stream, measure, or higher-layer content.
