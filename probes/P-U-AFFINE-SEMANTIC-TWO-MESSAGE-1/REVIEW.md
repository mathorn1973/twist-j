# Independent analytic review: an affine origin-zero readout

**NON-CANONICAL / L1 / candidate-T.** Review is analytic only; no scientific
code or previous audit was executed. The contract allows arbitrary common
preparation and requires a common blank *label*, not a common raw receiver
state across preparations.

This is a separate collaborating agent's formula-exposed review within the
authoring session, not an external audit. A. M. Thorn, Apache-2.0.

## Reviewed proposal

Work in `F5`, with

```text
A=a+c, B=b+d, C=a-c-2, D=b-d-1, z=a+b+c+d+q+r.
X=A+D, H=C+z,
r0=3(1+mu-lambda),
E(lambda,mu)=(3mu,3,3mu,2,2-mu-r0,r0).
```

The observation `(X,H)` is affine. The fixed total decoder is

```text
H=0 -> BLANK,
H!=0 -> PRESENT(H^2 X).
```

The preparation itself is affine as well. In expanded coordinates it is

```text
E(lambda,mu)=(3mu,3,3mu,2,4+mu+3lambda,3+3mu+2lambda).
```

## Prefix checked directly from the native generators

At the initial state,

```text
A=mu, B=D=0, C=3, z=2,
(X,H)=(mu,0).
```

Since the actual first three bits are `0,1,1`, the native prefix selects
`c,c,e`. Substitution into the native `c` formula gives

```text
x1=(2-3mu, r0-1, 2-3mu, -2-r0, mu+r0-1, -r0).
```

Consequently

```text
A1=4-mu, B1=2, C1=3, D1=2r0, z1=0,
X1=4-mu+2r0=-lambda, H1=3.
```

Thus the decoder returns `3^2*(-lambda)=lambda`. Applying `c` a second
time restores the full state: `x2=x0`, and the decoder returns blank again.
Applying the selected native `e` gives

```text
x3=(2-3mu,3,3-3mu,2,mu+r0,1-r0).
```

Here

```text
A3=-mu, B3=D3=0, C3=2, z3=1,
(X3,H3)=(-mu,3),
2*A3*C3*z3=mu.
```

The second message is therefore already read correctly at `n=3`.

## All-time tail and the zero-message case

The synchronized tail uses only native `b,d,e`. Their actions on
`(A,B,C,D,z)` are

```text
b:   (-A,-B, C, D,-z),
d/e: (-A,-B,-C,-D, z)   on their selected tail sheets.
```

They preserve

```text
B=D=0, C in {2,3}, z in {1,4}, 2ACz=mu.
```

Since `C^2=4` and `z^2=1`,

```text
H^2=(C+z)^2=2Cz != 0.
```

Thus no tail point is decoded as blank. Since `X=A` there,

```text
H^2 X=2ACz=mu.
```

The proof never divides by `A`. When `mu=0`, one has `A=X=0` on the
tail but `H!=0`; the output is therefore `PRESENT(0)`, distinct from
the initial raw value `(0,0)` and its blank label. There is no degeneracy
or exception at zero.

## Exact finite parameterization

For each fixed second message `mu`, define the following 20-point closed
set by independently choosing `C in {2,3}`, `z in {1,4}`, and `r in F5`:

```text
A=2Cz*mu,
a=3(A+C+2), c=3(A-C-2),
b=3, d=2,
q=z-A-r.
```

The formula for `A` follows from `2ACz=mu` because `(2Cz)^2=1`; it
also applies to zero. Every listed point has the claimed coordinates and
invariant, and the native tail transitions preserve this set. The union
over the five values of `mu` contains exactly 100 distinct tail points.

For the union over all 25 preparations, this is the exact actual tail
support; no assumption about arbitrary-word visitation is necessary.
At any common time the dependence on the initial `r0` has coefficient
`+1` or `-1`, so varying `lambda` at fixed `mu` supplies all five `r`
values. The actual bits give the four `(C,z)` cases already at times

| Time | C | z | Transition from preceding listed path |
| --- | --- | --- | --- |
| 3 | 2 | 1 | Initial tail point |
| 4 | 2 | 4 | `b` at time 3 |
| 7 | 3 | 4 | `b,b,e` at times 4,5,6 |
| 8 | 3 | 1 | `b` at time 7 |

The 25 blank states at `n=0,2` have `z=2`, and the 25 first-message
states at `n=1` have `z=0`, so they are mutually disjoint and disjoint
from the tail. This new family therefore has exactly **150 required
checkpoints**, not the old family's 550.

## Cross-label image separation

The raw blank image is exactly `{(mu,0): mu in F5}`. On the tail, `H`
assumes all four nonzero values, and a point with semantic label `mu`
has precisely the code

```text
(X,H)=(mu/H^2,H).
```

Hence different semantic labels cannot collide. The first-message code
`(-lambda,3)` is already one of the tail codes for semantic label
`lambda`, since `3^2=4`. All 25 raw observation values are used and are
assigned one unambiguous semantic label each.

For an independent finite verifier, the exact raw-fiber counts on the
150-point required set are: five points above every blank code; ten
points above every `H=3` code (five tail plus five first-message points);
five points above every remaining nonzero-`H` code.

## Scope and verdict

The formula passes the analytic review. It realizes the required origin
history for all 25 message pairs, including zero, on unchanged native `U`.
The observation is affine and two-dimensional; the decoder is fixed and
total. A single `F5` coordinate cannot produce six distinct semantic
outputs, so two coordinates are minimal in this contract.

The raw initial/reset value is `(mu,0)`, not one value common to all
preparations. The second message is already represented in that raw
receiver value while the decoder reports blank. This is explicitly
permitted by the current semantic-reset contract and is the essential
reason the older common-raw-reset obstruction does not apply. The older
550-state family's affine obstruction is also untouched because the
preparation family has changed.

No detector implementation, physically selected subsystem, newly inserted
information, source depletion, or Canon change follows from this result.
