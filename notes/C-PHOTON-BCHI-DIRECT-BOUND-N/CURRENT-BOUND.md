# P1 current analysis: a sharp four-edge Fourier block bound

**Working item:** C-PHOTON-BCHI-DIRECT-BOUND-N; owner [#1143](https://github.com/mathorn1973/twist-j/issues/1143).

**Author:** A. M. Thorn. **Date:** 22 September 2026.

**PUBLIC, NON-CANONICAL; candidate-T written proof. No authority or phase promotion.** This is a bound on the fixed model's dressed current-sector coefficients, not a bound on the complete normalized current covariance. Two separate agents reviewed the algebra and its use in the full measure; this is not a formal promotion or a two-architecture scientific gate.

Dependencies are the continuous U(1) current-sector representation [#1119](https://github.com/mathorn1973/twist-j/issues/1119), the one-edge estimate [#1120](https://github.com/mathorn1973/twist-j/issues/1120), and the eight-color packing [#1121](https://github.com/mathorn1973/twist-j/issues/1121), each at its existing candidate scope. The exact source normalization is derived again below.

## 1. Exact current geometry

Each edge of the four-dimensional cubic lattice has six incident plaquettes. Since their signed values are in {-1,0,1}, the condition `(∂n)_e=5j_e` implies `j_e∈{-1,0,1}`. A nonzero current requires exactly five incident signed plaquette values equal to its sign and one zero. Thus

`5 |supp j| <= 4 |supp n|`.

This incidence estimate is too weak to sum currents against path entropy at weight 1/2. It is not a current-covariance estimate.

## 2. The single-edge coefficient 1/2 is sharp

The #1120 single-edge integration uses a polynomial with six unit-circle roots. The allowed exterior phases can be chosen as the five equally spaced fifth roots plus one repeated root. Then

`P(z)=(1+z)(1+z^5)=1+z+z^5+z^6`.

For `h(z)=|P(z)|²`,

`hhat(0)=4, hhat(5)=2`.

Therefore a uniform one-edge coefficient estimate cannot improve 1/2. This saturation already occurs with exterior phases that are fifth roots of unity.

## 3. Four-edge plaquette block

Take an even torus with L>=4. For a plaquette p=(x;μν), μ<ν, its oriented boundary is e1=(x,μ), e2=(x+μ,ν), −e3=−(x+ν,μ), −e4=−(x,ν). Use θ=(A_e1,A_e2,−A_e3,−A_e4), z_i=exp(iθ_i). The Haar measure is unchanged. Then (dA)_p=θ_1+θ_2+θ_3+θ_4. Their incident stars contain one common central plaquette and five other plaquettes per edge, for 21 distinct plaquettes in total. No exterior plaquette in this star union uses two of the four selected edges.

Orient all four edge variables along ∂p. Fix every other U(1) link angle. Each outside five-plaquette factor is

`h_i(z_i)=|P_i(z_i)|²`,

where

`P_i(z)=∏_{a=1}^5(1+u_{ia} z)`, `|u_{ia}|=1`.

The full conditional block integrand, up to a common positive normalization, is

`H(z)=∏_{i=1}^4 h_i(z_i) [2+u z_1 z_2 z_3 z_4+conj(u)(z_1 z_2 z_3 z_4)^−1]`,

where physically u=1 in these coordinates; allowing an arbitrary |u|=1 only strengthens the bound. The Fourier convention is d_ik=∫h_i(exp(iθ))exp(−ikθ)dθ/(2π), and C_k=∫H(exp(iθ))exp(−i<k,θ>)∏dθ_i/(2π). This uses the same continuous U(1) Fourier representation of the fixed surface-sector weight as #1120, not a different action.

Write

`P_i=[1,s_i,t_i,v_i conj(t_i),v_i conj(s_i),v_i]`, `|v_i|=1`.

This coefficient identity follows directly from all five factors having unit-modulus parameters. Let `d_{ik}` denote the k-th Fourier coefficient of `|P_i|²`. Put `x_i=|s_i|`, `y_i=|t_i|`. Then

`d_{i0}=A_i=2(1+x_i²+y_i²)`,

`d_{i1}=2s_i+2t_i conj(s_i)+v_i conj(t_i)²`,

`|d_{i1}| <= B_i=2x_i+2x_i y_i+y_i²`,

`d_{i4}=2v_i conj(s_i)`, `d_{i5}=v_i`.

The zero-current block coefficient is

`C_0=2∏A_i+2 Re[u∏conj(d_{i1})]`.

The coefficient for current +1 on all four oriented edges is

`C_5=2∏v_i+u∏d_{i4}`.

Consequently

`C_0 >= 2(∏A_i−∏B_i)`,

`|C_5| <= 2+16∏x_i`.

## 4. Exact elementary inequality

For x,y>=0 define

`A=2(1+x²+y²)`, `B=2x+2xy+y²`.

The following polynomial identity is exact:

```
A²−B²−4−4x²
=8(y−x²/2−xy/4)²
 +(25/16)x⁴
 +(y−x/2)²(3y²−xy+(7/4)x²).
```

The last quadratic is positive semidefinite because

`3y²−xy+(7/4)x²=3(y−x/6)²+(5/3)x²`.

Thus `A²−B² >= 4(1+x²)`. Also, directly from the definitions,

`A²+B² >= 4[(1+x²)²+x²]=4(1+3x²+x⁴)`.

Multiplication gives

```
A⁴−B⁴
>=16(1+x²)(1+3x²+x⁴)
=16+128x⁴+16x²(x²−2)²
>=16+128x⁴.
```

In particular A>B>=0.

## 5. Hölder and the block constant

Hölder's inequality applied to the four two-component vectors gives

`∏A_i >= ∏B_i+∏(A_i⁴−B_i⁴)^(1/4)`.

Applying it again, now to `16+128x_i⁴`, gives

`∏A_i−∏B_i >= 16+128∏x_i`.

Therefore

`C_0 >= 32+256∏x_i >=16 |C_5|`,

or

**`|C_5| <= C_0/16`.**

The constant is sharp as a conditional block statement: choose every `P_i(z)=1+z^5`. These factors arise by giving each of the five exterior plaquettes at each chosen edge the complete set of fifth-root phases. They are realizable simultaneously: every exterior plaquette has an opposite edge parallel to its selected boundary edge, and this opposite edge belongs to no other plaquette of the 21-plaquette block. Assign those 20 independent exterior link angles and set all other exterior angles to zero. This realizes arbitrary values of the 20 exterior plaquette phases, including the required fifth roots. Then `A_i=2`, `d_{i1}=d_{i4}=0`, `d_{i5}=1`, and `(C_0,C_5)=(32,2)`.

For a mixed ±5 source pattern on these same four edges, the central shifted terms require a degree-six coefficient in at least one outside degree-five factor, so they vanish. Only `2∏d_{i,±5}` remains, with modulus 2. The same 1/16 bound then also holds. Hence every pattern with a nonzero ±1 current on all four boundary edges obeys this coefficient estimate.

## 6. Consequence for dressed current sectors

Let

`Q_j=2^(−|P|) ∫_[0,2π)^E e^(−5i<j,A>) ∏_p [2+e^(i(dA)_p)+e^(−i(dA)_p)] ∏_e dA_e/(2π)`

in the continuous U(1) Fourier representation. Expanding characters and applying normalized Haar orthogonality gives exactly `Q_j=Σ_(∂n=5j)2^(−|supp n|)`. The global factor 2^(−|P|) is the same in both numerator and denominator. The integrand without the current character is nonnegative, including at its possible zeros, and Q_0>=1 from n=0.

For the elementary current `j=∂p`, integrate first over the four edges of p. The unintegrated exterior factor is nonnegative, while the block ratio above holds pointwise in every exterior angle. It follows that

\[
\boxed{0\le\frac{Q_{\partial p}}{Q_0}\le\frac1{16}.}
\]

The same argument applies to any current j with all four edges of p charged: the remaining exterior character has modulus one and is removed by the absolute value, yielding again `Q_j <= Q_0/16`. No conditional completion-count or healing argument is used.

For k plaquette blocks whose 21-plaquette star unions are pairwise disjoint, and with all four edges in each block charged, the selected link sets are disjoint, no plaquette meets selected links from two different blocks, and all remaining factors are independent of every selected variable. Thus the conditional block integrations factor pointwise in the exterior angles. Then

`Q_j/Q_0 <= 16^(−k)`.

A mixed collection of k such square blocks and s single current edges also factorizes whenever their plaquette neighborhoods are pairwise disjoint. Applying this block estimate and the #1120 single-edge estimate yields

`Q_j/Q_0 <= 16^(−k) 2^(−s)=2^(−(4k+s))`.

Define κ(j) to be the maximum value of 4k+s over these compatible collections. Then

\[
\boxed{\frac{Q_j}{Q_0}\le 2^{-\kappa(j)},\qquad
\kappa(j)=\max(4k+s).}
\]

The eight-color independent single-edge construction of #1121 is an admissible collection, so κ(j)>=ceil(|supp j|/8). Thus this packing bound never weakens that theorem and strictly improves its guarantee on a current comprising a single elementary loop: κ>=4, instead of the earlier exponent 1. No assumption is made that arbitrary long currents contain elementary plaquette loops.

This is a coefficient statement in the full integer-closed dressing. It differs from the fixed binary completion classes in #1118, whose equal-count witnesses prohibit a strict local healing ratio.

## 7. The remaining P1 gap

This improves the known elementary-loop dressed-sector estimate `Q_{∂p}/Q_0 <=1/2` to `1/16`. It does not imply a bound on `Pr(j contains ∂p)` conditional on an arbitrary other current configuration. Nor does it show a connected interaction decays with the distance between loops.

In particular two separated elementary loops receive the bound 1/256, independent of their separation. Summing other current sectors is still needed to pass from these coefficients to the complete covariance `C_j(e,f)`. Therefore this estimate gives no certified numerical `χ_upper`, and P1 remains open.

No use is made of the withdrawn constant 243, no modification of the fixed weight W, and no order of thermodynamic/infrared limits is changed.

Original new text: Apache-2.0.
