# Uncle-memory polymer grammar

**PUBLIC, NON-CANONICAL.**
**Status:** candidate-C exact context census; frozen supersolution ansatz closed negative.
Owner: #1170.
Author: A. M. Thorn.
Date: 26 September 2026.
License: Apache-2.0.

This continuation keeps the first nonlocal geometric exclusion omitted by
#1168: a prospective child cube may not share a plaquette with any of the
other children of its parent.

The exact context census succeeds. The particular geometric-vector ansatz
`q_u=q r^u` does not.

## Exact worst-case child polynomials

Type `u` is the number of uncles of the current cube. The exact
coefficientwise worst polynomials are

`
B0 = 1 +15x +74x^2 +154x^3 +143x^4 +49x^5,
B1 = 1 +15x +74x^2 +154x^3 +143x^4 +49x^5,
B2 = 1 +14x +65x^2 +129x^3 +115x^4 +38x^5,
B3 = 1 +13x +57x^2 +110x^3 + 97x^4 +32x^5,
B4 = 1 +12x +50x^2 + 94x^3 + 82x^4 +27x^5.
`

All six choices of the parent's entry face give the same table.

For the special six-child root context, where a root child has five uncles,

`
B_root5 = 1 +11x +44x^2 +82x^3 +72x^4 +24x^5,
`

which is coefficientwise bounded by `B4`. Thus the preregistered root
convention is valid.

## What the negative certificate means

The frozen search required

`
q_u=q r^u
`

with one common `q` and one decreasing ratio `r<1`.

No such vector in the preregistered grid is a supersolution, even at `y=1`.

This is **not** evidence that the five-type polynomial system diverges.
The reason is visible directly in the exact table:

`
B0 = B1.
`

The worst context with one uncle is just as rich, coefficientwise, as the
worst context with no uncles. But the frozen ansatz forces

`
q1 = r q0 < q0.
`

It therefore imposes a monotonic decrease that the worst-case grammar does not
justify.

The next test should not guess a shape for `q`. It should construct an exact
supersolution directly by monotone iteration on a fixed rational grid.

Public Canon v92 is unchanged. No `Xi` or P1 conclusion follows.
