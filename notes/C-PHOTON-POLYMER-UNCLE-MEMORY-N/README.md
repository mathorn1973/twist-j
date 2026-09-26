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


## Post-audit analytic corollary: the whole five-type worst-case system is supercritical

This is a written consequence of the exact frozen census above. It is not an
additional computational claim.

Let the five-type coefficientwise-majorant map at physical activity be

`
F_u(q)=(1/16)[B_u(0)+sum_(b=1)^5 B_u(b) q_(b-1)^b].
`

Suppose any finite nonnegative vector `q=(q0,...,q4)` were a componentwise
supersolution:

`
F_u(q)<=q_u.
`

The exact census gives `B0=B1`, so

`
F0(q)=F1(q)=S.
`

Hence

`
S<=min(q0,q1).
`

Put `t=min(q0,q1)`. Since `q0>=t`, `q1>=t`, and every omitted term is
nonnegative,

`
S >= (1/16)(1+15 q0+74 q1^2)
  >= (1/16)(1+15 t+74 t^2).
`

But

`
(1/16)(1+15t+74t^2)-t
 = (1-t+74t^2)/16
 > 0
`

for every real `t`, because the quadratic has discriminant `-295`.

Thus `S>t`, contradicting `S<=t`.

Therefore **no finite componentwise supersolution exists for the
coefficientwise-worst five-type uncle-memory majorant at x=1/16**.

This is stronger than the preregistered negative result for vectors
`q_u=q r^u`. It still does not prove divergence of the real embedded tree
sum. The overestimate now has a precise source: replacing many geometrically
different uncle contexts by the coefficientwise maximum `B_u`.

The next absolute attack must retain context identity rather than uncle count
alone.
