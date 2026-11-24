# Bilinear coefficients and the affine contribution

**NON-CANONICAL. Authority none.** The identities, transfer bounds and sector
estimates are **candidate-D**. The positive whole-window estimate is **O**.
Action layer `NOT_APPLICABLE`. This is a paper derivation using the frozen
coefficients of [PRIME-CANCELLATION.md](PRIME-CANCELLATION.md).

## Projection error on the original slabs

Let \(X\) be dyadic and \(X\le N<2X\). Keep \(A,D,D_1,H,J\) as in the
prime note. Write \(w_X(N)=1/[N(N+1)]\) on the slab, and write
\(\|\cdot\|_X\) for its weighted norm. Put
\[
 L_X(N)=N+1/2+J(H-1)/2,\qquad B_X=2X+J(H-1).
\]
Thus \(B_X-1\) is the largest integer in any of the averages on the slab.
In particular \(B_X<A^2\) for all sufficiently large \(X\).
For a real coefficient sequence \(z\) supported on \(d\le4A^2\), put
\[
 V_X(z)=U_H^J\sum_d z_d\psi_d,\qquad
 P_X(z)=\operatorname{Proj}_{0<\|\theta\|<1/H,\ q(\theta)>D_1}
         U_H^J\sum_{d>D}z_d\psi_d,\qquad
 E_X(z)=V_X(z)-P_X(z),
\]
where \(q(\theta)\) is the reduced denominator. The original
\(T_{\mathrm{low}}=P_X(c*c)-L_Xh^2\).

For any such \(z\) with \(|z_d|\le C\tau(d)\), uniformly in \(z\),
\[
 \|E_X(z)\|_X\ll_C (1+\log X)^{3/2}.                         \tag{1}
\]
Indeed, the estimates of Sections 3 and 4 of the prime note use only
the divisor majorant. The raw short-denominator squared coefficient
mass is \(O_C(D(1+\log X)^3)\). On each translate of the slab, spacing
at least \(D^{-2}\) converts this to an unweighted squared norm
\(O_C((X+D^2)D(1+\log X)^3)\). Averaging preserves the bound by
convexity. For raw \(d>D\), frequencies at distance at least \(1/H\)
cost \(O_C((1+\log X)^2)\) pointwise by the multiplier \(2^{-J}=1/X\).
The remaining frequencies with \(q\le D_1\) have squared coefficient
mass \(O_C(D_1(1+\log X)^7)\) and spacing at least \(D_1^{-2}\).
Division by \(X^2\) in each squared slab norm proves (1). The result
also applies to any mask on the **raw** denominators of \(z\).

## The padding transfers an affine term

Write \(u_a=\mu(a)\mathbf 1_{a\le A}\), \(v=c-u\), \(m=M(A)\),
\(h_u=\sum_a u_a/a\), and \(b^u=u*u\). For any \(z\), the identity
\[
 V_X(z)=L_X\sum_d \frac{z_d}{d}-\frac12\sum_d z_d
              -U_H^J\sum_d z_d\lfloor N/d\rfloor             \tag{2}
\]
follows from the definition of \(\psi_d\). Every averaged argument
\(n\) satisfies \(2A\le n<A^2\) on sufficiently late slabs. For each \(a\)
in the support of \(v\), one has \(1\le n/a<A\). Therefore
\[
 \sum_{j\le A}\mu(j)\lfloor n/(aj)\rfloor=1.
\]
This is the sum of \(\mu*\mathbf 1=\delta\) through \(n/a\).
All the \(v*v\) floors vanish since their raw denominators exceed \(A^2\).
For \(e=c*c-b^u=2u*v+v*v\) the floor sum is exactly \(-2m\).
Also \(\sum e_d=-m^2\) and \(\sum e_d/d=h^2-h_u^2\). Equation (2) gives
\[
 T_{\mathrm{low}}
 = P_X(b^u)-L_Xh_u^2+\frac{m^2}{2}+2m-E_X(e).               \tag{3}
\]
Since \(|m|\le A\), the weighted slab norm of \(2m\) is \(O(1)\).
The divisor majorant holds for \(e\) with \(C=2\). Thus replacing
\(T_{\mathrm{low}}\) by
\[
 W_X=P_X(b^u)-L_Xh_u^2+\frac{m^2}{2}                         \tag{4}
\]
costs \(O((1+\log X)^{3/2})\) in slab norm. The positive constant
\(m^2/2\) is part of the main expression. Formula (3) accounts for the
entire change in the displayed square, including any cross term of
\(h_u\) with \(\sum_a v_a/a\). The argument holds for bounded padding
of the same support type and total \(-m\), with the divisor-majorant
constant changed as needed.

## A large retained family and its signed deletion

For sequences supported on \(d\ge B_X\), every floor in (2) vanishes.
In particular let \(z=b^u\mathbf 1_{d\ge B_X}\) and
\(b^{<}=b^u-z\). Since \(h_u^2=\sum b_d^u/d\) and
\(m^2=\sum b_d^u\), their coupled contribution to (4) is
\[
 P_X(z)-L_X\sum_d z_d/d+\tfrac12\sum_d z_d=-E_X(z).          \tag{5}
\]
Consequently one may use the expression
\[
 W_X^{<}=P_X(b^{<})-L_X\sum_{d<B_X}b_d^u/d
                         +\tfrac12\sum_{d<B_X}b_d^u         \tag{6}
\]
with the error (1). In (6), the affine slope uses a truncated signed
sum. The square sign from the untruncated expression cannot be
assigned to this truncated sum by the square identity.

There is a power-scale example in the deleted family itself.
Let \(\mathcal P_X=\{p\text{ prime}:9A/10<p\le A\}\), and let
\(z'_d=2\) when \(d=p\ell\), \(p<\ell\) in \(\mathcal P_X\), and zero
otherwise. Both primes exceed \(A/2\), so the only \(u\)-support
ordered pairs with \(p\ell\mid ab\) are \((p,\ell)\) and \((\ell,p)\).
Thus the divisor-multiple coefficient in the unpadded expression
is \(2/q\) for every such \(q=p\ell\); the primitive modes of these
denominators have their actual coefficients in \(P_X(z')\).
All raw denominators here exceed \(243X/100\), and thus exceed
\(B_X\) for large \(X\).

For \(N\le11X/10\), the average argument \(L_X(N)\) is at most
\(6X/5\) for large \(X\). Then \(L_X(N)/d-1/2\le-1/162\).
For \(17X/10\le N<2X\), \(d\le A^2\le31X/10\) for large \(X\),
so \(L_X(N)/d-1/2\ge3/62\). By (2),
\(V_X(z')\) has the corresponding strict signs with magnitude at
least a fixed constant times \(\binom{|\mathcal P_X|}{2}\) on these
two intervals. Each interval has weight of order \(1/X\).
The prime number theorem gives
\(|\mathcal P_X|\sim A/(10\log A)\), so the weighted squared negative
and positive energies on the respective intervals are both
\(\gg X/(\log X)^4\). The difference between \(V_X(z')\) and
\(P_X(z')\) is bounded by (1). The Lipschitz inequality for positive and
negative parts transfers each lower bound to the projected family.
[Hadamard, prime number theorem](https://www.numdam.org/item/BSMF_1896__24__199_1/).

This isolates a retained family whose positive energy in isolation
is too large for the requested scale. Its exact allocated affine
term cancels it throughout the slab up to (1), by (5) with \(z'\).
The sector gives no lower bound for the complete signed sum. In
particular, the offsets needed for this family are already present
in (4).

## The remaining divisor-multiple coefficients

In (6), the arithmetic coefficient at primitive \(a/q\) is
\[
 S_X(q)=\sum_{\substack{D<d<B_X\\q\mid d}}\frac{b_d^u}{d}.
\]
The coefficient of the exponential is \(-S_X(q)/(1-e(-a/q))\)
times the frozen averaging multiplier. Let \(g=(a',q)\) for a first
factor \(a'\) of \(d\), set \(j=q/g\), and write \(a'=gx\),
\(b'=jy\) for the second factor \(b'\). The latter substitution is
forced by \(q\mid a'b'\). The gcd condition is \((x,j)=1\).
Since \(\mu(gx)\mu(jy)\ne0\) requires both \(g,j\) squarefree
and \((x,g)=(y,j)=1\), this gives the exact coefficient
\[
 q S_X(q)=
 \sum_{\substack{g j=q\\g,j\ \mathrm{squarefree}}}
 \mu(g)\mu(j)
 \sum_{\substack{x\le A/g,\ y\le A/j\\
                   D/q<xy<B_X/q\\ (x,q)=1,\ (y,j)=1}}
       \frac{\mu(x)\mu(y)}{xy}.                              \tag{7}
\]
All sums are over positive integers. If \(p^3\mid q\) the coefficient
vanishes. Otherwise \(q=r s^2\), with \(r,s\) coprime squarefree,
and \(g=s t\), \(j=s r/t\) run over \(t\mid r\). The prefactor
\(\mu(g)\mu(j)=\mu(r)\) is constant. The inner sum still depends on
the split and has a signed hyperbolic product restriction. Even for
\(q=s^2>D\), the square of a single harmonic sum would require an
inactive upper product restriction. That identity holds for the
untruncated \(b^u\), where the coefficient is
\[
 \frac1{s^2}
   \left(\sum_{x\le A/s,\ (x,s)=1}\frac{\mu(x)}x\right)^2.
\]
Before the coupled deletion, these square denominators \(q>D\)
can be removed with pointwise allowance \(O(A(1+\log X))\):
the absolute primitive numerator multipliers sum to
\(O(q(1+\log q))\) before smoothing, and
\(\sum_{s\le A}(1+\log(A/s))^2\ll A\) by dividing into dyadic bands.
This is an optional removal in (4), with whole-window norm price
\(O((1+\log Y)^{3/2})\). It is separate from the coupled deletion
leading to (6).

For a precise remaining estimate in (6), define
\(A_X=\sum_{d<B_X}b_d^u/d\) and \(C_X=\sum_{d<B_X}b_d^u\).
On the complete integer window \(I(Y)=[Y,Y^{3/2})\cap\mathbb Z\),
let \(f_N\ge0\) have weighted squared norm at most one, with weights
\(w(N)=1/[N(N+1)]\). For a slab \(X\), define
\[
 F_X(\theta)=\sum_{N\in I(Y)\cap[X,2X)}w(N)f_N e(N\theta),
 \qquad
 G_X=\sum_{N\in I(Y)\cap[X,2X)}w(N)f_N L_X(N),
\]
where \(e(t)=\exp(2\pi i t)\). Write
\(K_X(\theta)=(H^{-1}\sum_{j=0}^{H-1}e(j\theta))^J\).
Finite summation and one-sided norm duality identify the required
norm for (6) with the supremum over these \(f_N\) of
\[
 \sum_X\left[
 -\Re\!\sum_{\substack{\theta=a/q\ \mathrm{reduced}\ \bmod 1\\
                    0<\|\theta\|<1/H,\ q>D_1}}
     \frac{K_X(\theta)F_X(\theta)S_X(q)}{1-e(-\theta)}
 -A_X G_X+\tfrac12 C_X F_X(0)\right].                        \tag{8}
\]
The maximizer is the normalized positive part of (6), or zero if
that part vanishes. Thus (7) specifies the short signed sums whose
contribution in (8) remains to be bounded jointly with the actual
two affine boundary terms. The shared prime factor sign in (7)
and the deletion (5) supply no bound on that supremum.

For (3) and (5), intersect each dyadic slab with the same window
\(I(Y)\); bounding each error on its full slab and summing the squared
bounds costs a single factor \(O(1+\log Y)\). Hence (6) has
\(|\sqrt{Q_{R_{1/36}}(Y)}-\sqrt{Q_{W^{<}}(Y)}|\ll(1+\log Y)^2\)
on every sufficiently late complete window. This preserves the target
quantifiers in both directions by using exponent \(2r\) in the source
inequality and absorbing the logarithmic norm error. A subpower
bound on (8) on arbitrarily late complete windows is **O**.
