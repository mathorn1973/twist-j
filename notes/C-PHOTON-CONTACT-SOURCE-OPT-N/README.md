# Exact rational optimization of the reinforcing-contact source

**PUBLIC, NON-CANONICAL.**
**Status:** candidate-C frozen-grid arithmetic; candidate-T implication only.
Owner: #1182.
Author: A. M. Thorn.
Date: 26 September 2026.
License: Apache-2.0.

For the exact source family `h=log t`, `2<=t<=32`, the local constants are

`
a_t=(t^2+1)^6/(64t^11),
r_t=2(t^4+1)/(t^2+1)^2,
s_t=4t^2/(t^2+1)^2.
`

If a simple cycle obeys `O_+<=rho m` and the helpful `O_-` factor is
discarded, the existing path argument is subcritical whenever

`
a_t(1+6r_t)r_t^rho<1.
`

The preregistered exact grid tested `rho=k/24`, `0<=k<=24`, and
`2<=t<=32`.

## Result

The largest passing density on this grid is

`
boxed: rho=1/12.
`

The unique passing source at that density is

`
boxed: t=3, h=log 3.
`

The exact 24th-power certificate is

`
835739816357067857525108918387910177516446402401293918281369514577655588667752813007184864435572535512619651854038238525390625
/
912034456046446591670769941126967809732389880154759674362919253085466672523897586208912607420113148072606337611541329196453281
<1.
`

At `rho=1/2` no source in the frozen family passes.

Thus the earlier `h=log3` choice was not merely convenient on this exact
integer-source grid. It is already the best member for the first unresolved
reinforcing-contact density step.

This does not prove continuum optimality in `h`. It proves that trying a
different exact integer `t` in the declared range cannot enlarge the clean
`O_+/m` threshold.

The useful enlargement therefore has to come from sign compensation
(`O_-`), geometric entropy reduction, or a different analytic mechanism.

Full `Xi_L`, P1 and the phase remain open.
