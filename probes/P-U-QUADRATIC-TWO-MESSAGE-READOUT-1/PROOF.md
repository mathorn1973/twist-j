# A quadratic two-coordinate readout with an arbitrary decoder

**NON-CANONICAL / L1 / candidate-T.** This note is a separate mathematical
result. It neither changes the native evolution `U` nor modifies Canon v101.
The closed construction and audit in #1533/#1534, and the family and affine
obstruction in #1536, are used as established inputs; their audits are not
repeated here.

All arithmetic below takes place in `F5`. A semantic output is an element of
`L = {BLANK} union {PRESENT(k): k in F5}`. In particular, `PRESENT(0)` and
`BLANK` are different outputs.

## 1. Exact necessary and sufficient conditions

Let `S` be the established set of 550 required checkpoints, and let
`ell: S -> L` be the required semantic label. For any polynomials
`P,Q in F5[a,b,c,d,q,r]` of total degree at most two, put
`F(x)=(P(x),Q(x))` and `S_l={x in S: ell(x)=l}`.

There exists a single decoder `delta: F5^2 -> L` satisfying

```text
delta(P(x),Q(x)) = ell(x)   for every x in S
```

**if and only if** the six image sets `F(S_l)` are pairwise disjoint.
Equivalently,

```text
ell(x) != ell(y)  implies  (P(x),Q(x)) != (P(y),Q(y))
```

for every pair of required points `x,y`. Necessity follows because a
function cannot assign two different labels to one input. Conversely, assign
to every attained pair its uniquely determined label and extend the decoder
arbitrarily to unattained pairs. There is no requirement that every state
with the same label have the same pair of polynomial values.

For a coefficient formulation, let `m(x)` be the vector consisting of the
constant monomial, the six degree-one monomials, and the 21 degree-two
monomials, in any declared fixed order. Thus `m(x)` has 28 coordinates.
Write `F(x)=M m(x)` with `M in F5^(2 x 28)`, and define

```text
Delta = {m(x)-m(y): x,y in S and ell(x) != ell(y)}.
```

The complete condition is `M d != (0,0)` for every `d in Delta`, or
equivalently `ker(M) intersection Delta` is empty. Constant coefficients
do not affect these differences. This is the unrestricted quadratic-pair
problem; prescribing the numerical message coordinate would impose an
additional condition not assumed here.

## 2. Established trajectory facts and the additional linear form B

Use the native checkpoint coordinates `x=(a,b,c,d,q,r)` and write

```text
A = a+c,
B = b+d,
C = a-c-2,
D = b-d-1,
z = a+b+c+d+q+r.
```

The already established common preparation is

```text
x0(lambda,mu) = (3(lambda+3), 3(mu+1),
                 3(-lambda-1), 3(-mu-1), 0, 1).
```

The established prefix has `x2=x0` and

```text
x1 = (3lambda, 3mu, 2lambda+3, 2mu+2, 1, 4),
x3 = (2lambda+3, 2mu+3, 3lambda+1, 3mu+2, 2, 0).
```

Direct substitution in these formulas gives

| Checkpoint | A | B | z | Other needed facts | Required label |
| --- | --- | --- | --- | --- | --- |
| `x0=x2` | 1 | 0 | 2 | `D=mu` | `BLANK` |
| `x1` | 3 | 2 | 0 | `C=lambda` | `PRESENT(lambda)` |
| `x3` | 4 | 0 | 1 | `D=4mu` | `PRESENT(mu)` |

For every tail time `n>=3`, the established sector theorem gives

```text
z in {1,4}, A in {1,4}, and zD/A = mu.
```

The only extra trajectory observation needed here is `B=0` on the whole
tail. The selected generators there are the native `b,d,e`; their formulas
send `(b,d)` respectively to `(-d,-b)`, `(1-b,4-d)`, and `(1-b,4-d)`.
Every one therefore sends `B` to `-B`. Since `B(x3)=0`, induction proves
`B=0` for every subsequent step, including every permitted continuation
word. No change of the native evolution or new operation is involved.

Because `A^2=1` on the tail, its required message can also be written

```text
mu = AzD.
```

## 3. Explicit quadratic construction

Define one fixed pair on the entire checkpoint space `F5^6` by

```text
P = A + 2z,
Q = (1+2B)D + 3BC.
```

The first component is linear, and the second has total degree at most two.
An expanded certificate in the original coordinates is

```text
P = 3a+2b+3c+2d+2q+2r,
Q = 2b^2+3d^2+3ab+3ad+2bc+2cd+3b+d+4.
```

Define one fixed decoder on all 25 possible pairs by

```text
delta(p,t) = BLANK              if p=0,
             PRESENT(-p^2 t)    if p!=0.
```

This decoder uses no time, preparation label, previous output, or external
state. Its finite table is equivalently

| First coordinate p | Decoded label |
| --- | --- |
| 0 | `BLANK`, for every `t` |
| 1 or 4 | `PRESENT(-t)` |
| 2 or 3 | `PRESENT(t)` |

### Blank checkpoints

At `n=0,2`, the table above gives `A=1,z=2,B=0`, hence

```text
P = 1+2*2 = 0,    Q = D = mu.
```

The decoder therefore returns `BLANK` for every preparation.

### First-message checkpoint

At `n=1`, one has `A=3,z=0,B=2,C=lambda`. Consequently

```text
P = 3,
Q = (1+2*2)D + 3*2*C = C = lambda,
-P^2 Q = -9lambda = lambda.
```

The decoder returns `PRESENT(lambda)`, including when `lambda=0`.

### Every tail checkpoint

At every `n>=3`, one has `B=0` and `A^2=z^2=1`, so `Q=D` and

```text
P^2 = (A+2z)^2 = A^2+4Az+4z^2 = 4Az = -Az.
```

In particular, `P^2` is nonzero, so the blank branch cannot occur. Also

```text
-P^2 Q = AzD = mu.
```

The decoder therefore returns `PRESENT(mu)` at every tail time. This is
an all-time proof by the established sector invariant and the induction
for `B`; it is not an inference from a finite sampling of times.

Thus the fixed quadratic pair realizes exactly

```text
BLANK, PRESENT(lambda), BLANK,
PRESENT(mu), PRESENT(mu), ...
```

for all 25 common preparations on unchanged native `U`.

## 4. Exact label-image separation

The label-image condition from section 1 can also be read off directly.
The blank image is contained in `{(0,t): t in F5}`. For each `k in F5`,
every present point with label `PRESENT(k)` has an image in

```text
E_k = {(p,t): p!=0 and -p^2 t=k}.
```

These six sets are pairwise disjoint, regardless of whether their points
are all attained. Here they are in fact attained in full.

To see the latter without a new orbit enumeration, the established tail
set has exactly 500 points and is contained in

```text
B=0, A in {1,4}, z in {1,4}, C,D,r arbitrary,
q=z-A-r.
```

These are invertible linear/affine coordinates, so the displayed set also
has exactly `2*2*5*5*5=500` points. Containment and equal cardinality imply
equality. The four pairs `(A,z)` give distinct values

| A | z | P=A+2z |
| --- | --- | --- |
| 1 | 1 | 3 |
| 1 | 4 | 4 |
| 4 | 1 | 1 |
| 4 | 4 | 2 |

and `D` ranges over `F5` for each. Hence the tail image is exactly the
20 pairs with `p!=0`; each `E_k` has four elements. The blank image is
exactly the five pairs with `p=0`, since `Q=mu` there. The entire required
set therefore maps onto all 25 values of `F5^2`.

## 5. Sharp minimum and the precise scope

The inherited affine impossibility result in #1536 excludes every pair
of polynomials of total degree at most one even with an arbitrary decoder.
The construction above has degree at most two. Therefore, for this precise
preparation family, required label history, and unrestricted fixed decoder,
the minimum possible maximum degree of a two-coordinate polynomial
readout is **exactly two**.

This does not contradict the two established quadratic impossibility
results for prescribed exact codes. The raw value `Q` on a tail point is
`D`, not necessarily its semantic message `mu`; the decoder uses `P` to
choose its sign. The numerical encoding has changed, as the unrestricted
problem explicitly allows.

It is also essential that the contract asks for a common **blank semantic
output**, not a common raw polynomial receiver value over all preparations.
At the initial and reset checkpoints this construction gives

```text
(P,Q)(x0(lambda,mu)) = (P,Q)(x2(lambda,mu)) = (0,mu).
```

For a fixed preparation there is an exact raw reset because `x2=x0`, but
the raw blank pair varies with `mu` across the preparation family. A demand
for one identical raw initial receiver pair for all preparations is a
different, stricter problem and is not settled by this construction.

Finally, the result is mathematical existence of a global checkpoint
readout. It provides neither a physical detector realization, a transfer
between disjoint sectors, a later insertion of information, source
depletion, nor a new native law. Both messages remain jointly prepared
initial data. No Canon claim follows.
