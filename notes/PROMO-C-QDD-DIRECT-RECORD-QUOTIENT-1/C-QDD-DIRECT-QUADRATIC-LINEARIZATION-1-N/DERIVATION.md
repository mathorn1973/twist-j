# Derivation

Status: candidate-T, NON-CANONICAL incubation.

## 1. Direct trace form

In the basis `B0=(1,z,z^2,z^3)` of `K=Q(zeta_5)`,

```text
<x,y>_tr = (1/5) Tr(x sigma_4(y)).
```

Since `Tr(1)=4` and `Tr(z^k)=-1` for `k not congruent 0 mod 5`, its matrix is

```text
G = I_4 - (1/5) 1 1^T.
```

For `lambda_B=1+z+z^2+z^3`, with coordinate vector `1`,

```text
G 1 = (1/5)1,
<lambda_B,lambda_B>_tr = 4/5.
```

For `w=iota_B0(v)` and `s=1^T v`, the orthogonal LOW component is therefore

```text
pi_low(w) = (s/4) lambda_B.
```

Hence

```text
m(v)      = v^T G v = |v|^2 - s^2/5,
l(v)      = s^2/20,
h(v)      = |v|^2 - s^2/4,
N(v)      = MATRIX_B0(T_w) = v v^T G.
```

These formulas are derived from the direct cyclotomic write. No factor map or Born pairing is used.

## 2. The quadratic images span all symmetric matrices

Let `S=Sym_4(Q)` and `q(v)=vv^T`. The ten vectors

```text
e_i,                    0 <= i < 4,
e_i+e_j,                0 <= i < j < 4,
```

belong to `V_eff={-2,-1,0,1,2}^4`. Their quadratic images generate

```text
E_ii = q(e_i),
E_ij+E_ji = q(e_i+e_j)-q(e_i)-q(e_j).
```

Thus `q(V_eff)` spans `S`, whose dimension is 10.

## 3. Unique rational-linear factor data

The four raw direct fields are linear in `A=vv^T`:

```text
m_Q(A) = Tr(A G),
l_Q(A) = Tr(E_low A G),
h_Q(A) = Tr(E_high A G),
N_Q(A) = A G,
```

where

```text
E_low  = (1/4) 1 1^T,
E_high = I-E_low.
```

If two rational-linear maps on `S` agree on every `q(v)`, their difference vanishes on a spanning set and is zero. The displayed extension is therefore unique. Ten independent piston heads suffice, and ten is minimal for an unrestricted rational-linear map on a ten-dimensional domain.

## 4. Recovery of the metric and effects

The total-weight functional uniquely represents `G`. Let `H_low` represent the LOW functional:

```text
l_Q(A)=Tr(A H_low).
```

The direct formula gives

```text
H_low = G E_low = E_low G = (1/20)1 1^T.
```

Since `G` is invertible,

```text
E_low = G^-1 H_low = H_low G^-1,
E_high = I-E_low.
```

The recovered pair is ordered and satisfies

```text
E_a^2=E_a,
E_low E_high=0,
E_low+E_high=I,
E_a^T G=G E_a.
```

The LOW raw field is necessary. The metric alone admits other rational rank-one `G`-self-adjoint projectors, for example the projector onto `Q e_0`.

## 5. Normalized record and fibres

For nonzero `v`, `G` is positive definite, so `m_Q(q(v))>0`. The normalized fields are uniquely obtained by division:

```text
density = N_Q(A)/m_Q(A),
normalized_weights = (l_Q(A),h_Q(A))/m_Q(A).
```

If `vv^T=ww^T` over `Q`, then either both vanish or `w=+v` or `w=-v`. Thus the 625 pistons form one zero class and 312 sign pairs, giving 313 quadratic classes. The two ignored head coordinates contribute 25 orbit heads per piston, so the orbit fibres are one class of size 25 and 312 classes of size 50.

## 6. Scope boundary

Linearity is essential. The cubic

```text
p(A_00)=A_00(A_00-1)(A_00-4)
```

vanishes on every `q(V_eff)` because `A_00` is in `{0,1,4}`, but not at `A_00=2`. Adding it to one scalar output gives a distinct nonlinear extension with identical finite carrier values.

This result does not derive `V_eff`, `B0`, `lambda_B`, or the direct dictionary from `J`. It supplies no Born interpretation, physical effect, apparatus, event, decoder ownership, stream, measure, SI statement, or layer lift.
