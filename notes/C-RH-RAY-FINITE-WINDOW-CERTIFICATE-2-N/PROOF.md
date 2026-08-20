# Proof. Ray finite-window certificate on the v57 basis

```text
STATUS:       NON-CANONICAL candidate-T
SCOPE:        conditional analytic theorem only
ISSUE:        #468
PREREG BLOB:  eb6375d2de08eda6152579e8aa49b9bf951a8b2a
BREAKER BLOB: 5d31fecb5a417b8463deea8797a4d6a4334f5b38
RH:           unchanged and open
```

This is a fresh written proof on Public Canon v57. Its conclusion is
conditional on a complete finite zero window containing a nontrivial tau
orbit. It does not provide such a window or orbit.

## Theorem

Fix `c>1/2`. Let `W` be a finite tau-invariant set of distinct nontrivial zero
locations of `X(z)=xi(1/2+z)`, with multiplicities. Let

```text
O={alpha,tau alpha} subset W,        tau alpha=-conj(alpha),
```

be a nontrivial orbit with common multiplicity `m_O`. Define `t_beta`, `H_W`,
`L_r`, and `P_r` as in `PREREG.md`. Put

```text
tau_0=min(|t_alpha|,|t_(tau alpha)|),
q_W=sup_(beta notin W)|t_beta|/tau_0.
```

If `q_W<1`, then for every integer `r_0>=1` and every `r>=r_0`,

```text
Tail_r<=A_W(c)q_W^(2(r-r_0)),
A_W(c)=B_W^2C_W^2M(c)/((c-1/2)tau_0^2).
```

Consequently the least integer

```text
r_*=min{r>=r_0:A_W(c)q_W^(2(r-r_0))<2m_O}
```

exists. The one-point mixed-derivative Ray-Pick matrix through order

```text
N_*=r_*+|W|-1
```

is indefinite, and at least one leading principal minor through order `N_*`
is nonpositive.

If `alpha=x+iy` and `W` contains every zero location with
`|Im beta|<=T`, then

```text
T>sqrt(y^2+(c+|x|)^2)
```

implies `q_W<1`.

## 1. The derivative matrix

The Cauchy vector is

```text
v_a(beta)=sqrt(m_beta)(a-conj(beta))^-1.
```

For every integer `j>=1`,

```text
partial_a^(j-1)v_a|_(a=c)
 =(-1)^(j-1)(j-1)!w_j.
```

`J_ref` is bounded and independent of `a` and `b`. Therefore differentiation
inside the Hilbert inner product gives

```text
partial_a^(j-1)partial_b^(k-1)K_ray(a,b)|_(c,c)
 =(-1)^(j+k-2)(j-1)!(k-1)!<J_ref w_j,w_k>.
```

Define

```text
G_N(j,k)=<J_ref w_j,w_k>,       1<=j,k<=N.
```

The raw derivative matrix is obtained from `G_N` by congruence with a diagonal
matrix whose entries are the nonzero real numbers
`(-1)^(j-1)(j-1)!`. The two matrices have the same inertia.

For a polynomial with no constant term,

```text
P(t)=sum_(k=1)^N p_k t^k,
```

we have

```text
sum_k p_k w_k(beta)=sqrt(m_beta)P(t_beta),
p^*G_Np=<J_ref f_P,f_P>.
```

This proves V1.

## 2. Exact interpolation on a finite window

The map

```text
beta -> t_beta=(c-conj(beta))^-1
```

is injective because conjugation, translation, and inversion are injective on
the declared domain. A nontrivial tau orbit therefore gives two distinct
Cauchy coordinates.

Every root used in `H_W` corresponds to a location outside the target orbit.
Injectivity gives

```text
H_W(t_alpha) != 0,
H_W(t_(tau alpha)) != 0.
```

The two target normalization factors are nonzero. There is exactly one affine
polynomial taking the two required values. The frozen Lagrange formula is that
polynomial. Substitution yields

```text
P_r(t_alpha)=+1,
P_r(t_(tau alpha))=-1.
```

Every other point of `W` is a root of `H_W`, so `P_r` vanishes there. Since
`deg H_W=|W|-2`, `deg L_r<=1`, and `P_r` contains the factor `t^r`,

```text
powers(P_r) subset {r,...,r+|W|-1}.
```

This proves V2.

## 3. Isolation of the negative orbit

Let

```text
u_O=sqrt(m_O)(e_alpha-e_(tau alpha)).
```

Exact interpolation gives `f_r|W=u_O`. Tau invariance implies that both
`ell^2(W)` and `ell^2(W^c)` reduce `J_ref`. They are orthogonal, so the cross
terms vanish exactly:

```text
<J_ref f_r,f_r>
 =<J_ref u_O,u_O>+<J_ref e_r,e_r>.
```

`J_ref` exchanges the target basis vectors, hence

```text
J_ref u_O=-u_O,
<J_ref u_O,u_O>=-||u_O||^2=-2m_O.
```

Because `J_ref` is unitary,

```text
|<J_ref e_r,e_r>|<=||e_r||^2
 =sum_(beta notin W)m_beta|P_r(t_beta)|^2
 =Tail_r.
```

Thus

```text
<J_ref f_r,f_r>=-2m_O+E_r,
|E_r|<=Tail_r.
```

If `Tail_r<2m_O`, the form is negative. This proves V3.

## 4. Finite derivative consequence

`P_r` has no constant term and degree at most

```text
N=r+|W|-1.
```

Its coefficient vector therefore belongs to `G_N`. Under the sufficient tail
inequality it has a negative quadratic value, so `G_N` is indefinite. The raw
mixed-derivative matrix has the same inertia by the congruence in section 1.

If every leading principal minor of a Hermitian matrix were positive, the
matrix would be positive definite by Sylvester's criterion. Therefore an
indefinite matrix has at least one nonpositive leading principal minor. This
proves V4.

## 5. Uniform exponential tail estimate

Write

```text
t_1=t_alpha,
t_2=t_(tau alpha),
h_i=H_W(t_i),
delta_t=|t_1-t_2|,
h_*=min(|h_1|,|h_2|).
```

The explicit affine formula gives, for every outside coordinate `t`,

```text
|L_r(t)|
 <= |t-t_2|/(|t_1|^r|h_1|delta_t)
    +|t-t_1|/(|t_2|^r|h_2|delta_t).
```

Since `|t_i|>=tau_0` and `|t|<=q_Wtau_0`,

```text
|L_r(t)|<=B_Wtau_0^-r,
B_W=(2q_Wtau_0+|t_1|+|t_2|)/(delta_t h_*).
```

For the finite root polynomial,

```text
|H_W(t)|
 <=product_(gamma in W minus O)(|t|+|t_gamma|)
 <=C_W.
```

Therefore

```text
|P_r(t)|<=B_WC_W(|t|/tau_0)^r.
```

Summing outside the window,

```text
Tail_r
 <=B_W^2C_W^2 sum_(beta notin W)m_beta
      (|t_beta|/tau_0)^(2r).
```

For `r>=r_0>=1`,

```text
(|t_beta|/tau_0)^(2r)
 <=q_W^(2(r-r_0))(|t_beta|/tau_0)^(2r_0)
 <=q_W^(2(r-r_0))|t_beta|^2/tau_0^2.
```

It remains to control the ordinary Cauchy norm.

## 6. Ordinary Cauchy norm from the ray value

For every zero location `beta`,

```text
Re(1/(c-beta))=(c-Re beta)/|c-beta|^2.
```

All nontrivial zero locations satisfy `|Re beta|<1/2`, so

```text
1/|c-beta|^2
 <=Re(1/(c-beta))/(c-1/2).
```

Every term on the right is positive. The paired Hadamard expansion has no
extra affine term and sums these terms to

```text
M(c)=X'(c)/X(c)=sum_beta m_beta/(c-beta).
```

Conjugation invariance gives `|c-beta|=|c-conj(beta)|`. Hence

```text
sum_beta m_beta|t_beta|^2<=M(c)/(c-1/2).
```

Combining this with section 5 proves

```text
Tail_r<=A_W(c)q_W^(2(r-r_0)).
```

`A_W(c)` is finite and independent of `r`. Since `q_W<1`, the right side tends
to zero. The exact minimum `r_*` exists, and V3 and V4 apply at `N_*`. This
proves V5 and V6.

## 7. Complete-height corollary

For `alpha=x+iy`,

```text
|t_alpha|       =1/sqrt((c-x)^2+y^2),
|t_(tau alpha)| =1/sqrt((c+x)^2+y^2).
```

The smaller value is

```text
tau_0=1/sqrt((c+|x|)^2+y^2).
```

If `beta` lies outside a complete height window, then `|Im beta|>T`, so

```text
|t_beta|=1/|c-conj(beta)|<1/T.
```

Consequently

```text
q_W<=sqrt((c+|x|)^2+y^2)/T.
```

The displayed strict height condition makes this less than one. This proves
V7.

## 8. Exact boundary

This theorem is zero-side and conditional. Applying it to zeta would first
require an actual nontrivial tau orbit, a complete invariant zero window with
multiplicities proved without assuming RH, and rigorous enclosures of every
constant entering the threshold. These unresolved inputs carry the arithmetic
difficulty. The theorem only converts them into a finite explicit Ray-Pick
failure rather than an existential one.