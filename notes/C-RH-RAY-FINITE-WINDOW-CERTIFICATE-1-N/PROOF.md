# Proof. Ray finite-window certificate

```text
STATUS: NON-CANONICAL candidate-T proof under issue #466
SCOPE:  conditional analytic theorem only
INPUT:  PREREG.md at Git blob fc4ffa8f49c633180ceebb2c39b6e14d34b0770e
BREAKER: break.py at Git blob a6493c43b9d89161883252bb80261cc52dfc8392
RH:     unchanged and open
```

This proof uses the objects and conventions frozen in `PREREG.md`. It proves
the conditional finite-window theorem. It does not provide a complete zeta
zero window, an off-critical zero, or an Euler-side tail certificate.

## Theorem

Let `c>1/2`. Let `W` be a finite `tau`-invariant set of distinct nontrivial
zero locations of `X(z)=xi(1/2+z)`, with multiplicities, and let

```text
O={alpha,tau alpha} subset W
```

be a nontrivial orbit of common multiplicity `m_O`. Define `t_beta`, `H_W`,
`L_r`, and `P_r` as in the preregistration. If

```text
q_W = sup_(beta notin W) |t_beta|/tau_0 < 1,
```

then for every integer `r_0>=1` and every `r>=r_0`,

```text
Tail_r <= A_W(c) q_W^(2(r-r_0)),
A_W(c) = B_W^2 C_W^2 M(c)/((c-1/2)tau_0^2).
```

Consequently the least integer

```text
r_* = min{r>=r_0 : A_W(c)q_W^(2(r-r_0))<2m_O}
```

exists. The one-point mixed-derivative matrix of `K_ray` through order

```text
N_* = r_*+|W|-1
```

is not positive semidefinite. At least one leading principal minor through
order `N_*` is nonpositive.

If `alpha=x+iy` and `W` contains every zero location with imaginary part of
absolute value at most `T`, the sufficient geometric condition

```text
T > sqrt(y^2+(c+|x|)^2)
```

implies `q_W<1`.

## 1. Derivative identity

The Cauchy vector is

```text
v_a(beta)=sqrt(m_beta)(a-conj(beta))^-1.
```

For `j>=1`, ordinary differentiation in the real parameter gives

```text
partial_a^(j-1)v_a|_(a=c)
 = (-1)^(j-1)(j-1)! w_j.
```

The involution `J_ref` is bounded and independent of `a,b`. Differentiation
may therefore be taken inside the Hilbert inner product:

```text
partial_a^(j-1)partial_b^(k-1)K_ray(a,b)|_(c,c)
 = <J_ref partial_a^(j-1)v_a,partial_b^(k-1)v_b>|_(c,c)
 = (-1)^(j+k-2)(j-1)!(k-1)!<J_ref w_j,w_k>.
```

This proves G1. The diagonal scaling factors are nonzero, so the raw derivative
matrix and the scaled Hermitian matrix `G_N=(<J_ref w_j,w_k>)` are congruent
and have the same inertia.

For `P(t)=sum_(k=1)^N p_k t^k`,

```text
sum_k p_k w_k(beta)=sqrt(m_beta)P(t_beta).
```

Thus its Ray quadratic value is exactly `p^*G_Np`.

## 2. Finite interpolation

The map

```text
beta -> t_beta=(c-conj(beta))^-1
```

is a composition of conjugation, translation, and inversion, each injective on
the declared domain. Hence it is injective. A nontrivial target orbit has two
distinct locations and therefore two distinct Cauchy coordinates.

Every factor of `H_W(t_alpha)` corresponds to a location in `W` outside the
target orbit. Injectivity makes each factor nonzero. The same holds at
`t_(tau alpha)`. Therefore `A_1(r)` and `A_2(r)` are nonzero.

There is a unique affine polynomial taking prescribed values at two distinct
points. The frozen Lagrange formula is that polynomial. Direct substitution
gives

```text
P_r(t_alpha)=1,
P_r(t_(tau alpha))=-1.
```

Every other point of `W` is a root of `H_W`, so `P_r` vanishes there. The
factor `t^r` makes every power below `r` zero. Since `deg H_W=|W|-2` and
`deg L_r<=1`, the degree is at most `r+|W|-1`. This proves G2.

## 3. Invariant split

Let

```text
u_O=sqrt(m_O)(e_alpha-e_(tau alpha)).
```

Interpolation gives `f_r|W=u_O`. Since `W` is `tau` invariant, both coordinate
subspaces `ell^2(W)` and `ell^2(W^c)` reduce `J_ref`. They are orthogonal, so
there are no cross terms:

```text
<J_ref f_r,f_r>
 = <J_ref u_O,u_O>+<J_ref e_r,e_r>.
```

The involution exchanges the two target basis vectors, hence

```text
J_ref u_O=-u_O,
<J_ref u_O,u_O>=-||u_O||^2=-2m_O.
```

Because `J_ref` is unitary,

```text
|<J_ref e_r,e_r>|<=||e_r||^2=Tail_r.
```

Therefore

```text
<J_ref f_r,f_r><0
```

whenever `Tail_r<2m_O`. This proves G3.

## 4. Finite matrix consequence

The polynomial `P_r` has no constant term and degree at most
`N=r+|W|-1`. Its coefficient vector is therefore a vector in the finite matrix
`G_N`. Under the sufficient tail inequality that vector has a negative
quadratic value. Hence `G_N` is not positive semidefinite. Congruence transfers
the same inertia to the raw mixed-derivative matrix.

If every leading principal minor of a Hermitian matrix were positive, the
matrix would be positive definite by Sylvester's criterion. Therefore at least
one leading principal minor through order `N` is nonpositive. This proves G4.

## 5. Uniform tail estimate

Write

```text
t_1=t_alpha,
t_2=t_(tau alpha),
h_i=H_W(t_i),
delta_t=|t_1-t_2|,
h_*=min(|h_1|,|h_2|).
```

The explicit affine formula and the triangle inequality give, for every
outside point `t`,

```text
|L_r(t)|
 <= |t-t_2|/(|t_1|^r|h_1|delta_t)
    + |t-t_1|/(|t_2|^r|h_2|delta_t).
```

Since `|t_i|>=tau_0` and `|t|<=q_Wtau_0`,

```text
|L_r(t)|
 <= tau_0^(-r)
    (2q_Wtau_0+|t_1|+|t_2|)/(delta_t h_*)
 = B_W tau_0^(-r).
```

For the finite root polynomial,

```text
|H_W(t)|
 <= product_(gamma in W minus O)(|t|+|t_gamma|)
 <= C_W.
```

Thus

```text
|P_r(t)|<=B_WC_W(|t|/tau_0)^r.
```

Summing outside the window gives

```text
Tail_r
 <= B_W^2C_W^2 sum_(beta notin W)m_beta
       (|t_beta|/tau_0)^(2r).
```

For `r>=r_0>=1` and every outside ratio at most `q_W<1`,

```text
(|t_beta|/tau_0)^(2r)
 <= q_W^(2(r-r_0))(|t_beta|/tau_0)^(2r_0)
 <= q_W^(2(r-r_0))|t_beta|^2/tau_0^2.
```

It remains to bound the ordinary Cauchy norm. For a zero location `beta`,

```text
Re(1/(c-beta))=(c-Re beta)/|c-beta|^2.
```

Since `|Re beta|<1/2` and `c>1/2`,

```text
1/|c-beta|^2
 <= Re(1/(c-beta))/(c-1/2).
```

All terms on the right are positive. The paired Hadamard expansion sums them
to `M(c)=X'(c)/X(c)`. Also `|c-beta|=|c-conj(beta)|`. Therefore

```text
sum_beta m_beta|t_beta|^2<=M(c)/(c-1/2).
```

Substitution proves

```text
Tail_r<=A_W(c)q_W^(2(r-r_0)).
```

The constant is finite and independent of `r`. Since `q_W<1`, the right side
tends to zero. The exact least integer `r_*` therefore exists, and G3 and G4
apply at `N_*`. This proves G5.

## 6. Complete height window

For `alpha=x+iy`,

```text
|t_alpha|       = 1/sqrt((c-x)^2+y^2),
|t_(tau alpha)| = 1/sqrt((c+x)^2+y^2).
```

The smaller is

```text
tau_0=1/sqrt((c+|x|)^2+y^2).
```

If `beta` lies outside a complete height window, then `|Im beta|>T` and

```text
|t_beta|=1/|c-conj(beta)|<1/T.
```

Consequently

```text
q_W<=sqrt((c+|x|)^2+y^2)/T.
```

The displayed strict height inequality makes this ratio less than one. This
proves G6.

## 7. Exact boundary

The proof is zero-side and conditional. To use it against zeta, one must first
exhibit an actual nontrivial `tau` orbit, prove a complete invariant zero
window with multiplicities without assuming RH, and certify every bound in the
threshold. Those tasks contain the unresolved arithmetic difficulty. The
present theorem only proves that such data would generate an explicit finite
Ray-Pick certificate rather than a merely existential one.
