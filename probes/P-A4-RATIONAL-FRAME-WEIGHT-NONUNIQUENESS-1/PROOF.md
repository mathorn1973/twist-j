# A global positive nonquadratic frame weight on rational A4

Status target: **T**, conditional only on the definitions in this file.
Public probe: `P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1`.
Scope: **L4 rational rays, complete rational orthogonal frames, scalar weights**.

This proof decides one mathematical implication only. It does not assert a
physical realization of the nonquadratic weights and does not falsify the
owner-adopted quadratic decoder.

## 1. Carrier and frame weights

Let

\[
L=A_4=\{v\in\mathbb Z^5:\sum_i v_i=0\},\qquad
V=L\otimes_{\mathbb Z}\mathbb Q,\qquad
q(v)=\sum_i v_i^2.
\]

A ray is a one-dimensional rational subspace `[v]`, `v != 0`. A complete frame
is any four mutually orthogonal nonzero rational rays in V. No rational unit
representative is required.

For a ray write

\[
P_v=\frac{vv^{\mathsf T}}{q(v)}.
\]

A normalized positive frame weight is a function on rational rays with values
in `[0,1]` whose values on every complete frame sum to one.

## 2. The ternary residue function

For nonzero rational `a`, write

\[
a=3^k u,\qquad k=\nu_3(a),
\]

where numerator and denominator of `u` are prime to 3. Let `u_bar` be the
nonzero residue of `u` modulo 3. Define

\[
h(a)=
\begin{cases}
0,&k\text{ even},\\
-1,&k\text{ odd and }\bar u=1,\\
+1,&k\text{ odd and }\bar u=2.
\end{cases}
\tag{1}
\]

### Lemma 1. Projective square invariance

For every nonzero rational `s`,

\[
h(as^2)=h(a).\tag{2}
\]

The valuation changes by the even integer `2 nu_3(s)`. The leading unit is
multiplied by a nonzero square, and every nonzero square modulo 3 is 1.
Therefore

\[
H([v])=h(q(v))\tag{3}
\]

is a well-defined function of rational rays. Also `h(-a)=-h(a)`.

### Lemma 2. Binary diagonal-change identity

For nonzero rational `a,b,a+b`,

\[
h(a)+h(b)\equiv h(a+b)+h\!\left(\frac{ab}{a+b}\right)\pmod4.\tag{4}
\]

**Proof.** Write `a=3^alpha u`, `b=3^beta v` with `u,v` units at 3.

If `alpha<beta`, then `a+b` has valuation `alpha` and leading unit `u`, while
`ab/(a+b)` has valuation `beta` and leading unit `v`. The two contributions
are unchanged. The case `beta<alpha` is symmetric.

Now let `alpha=beta=k`. If `u+v` is a unit, the two input residues are equal,
while both output residues are their negatives. For even `k`, every h-value is
zero. For odd `k`, both signs reverse and the integer sum changes by four.

If `u+v` is divisible by 3, the input residues are opposite and cancel. Write
`u+v=3^s z`, `s>0`, with z a unit. The output valuations are `k+s` and `k-s`,
so they have the same parity. Their leading residues are `z` and `uv/z`.
Since `uv=-1 mod 3` and `z^2=1 mod 3`, the output residues are opposite and
cancel. QED.

## 3. Orthogonal-basis invariant modulo four

Let `(e_1,...,e_d)` be a rational orthogonal basis of a positive rational
quadratic space. Then

\[
\sum_i h(q(e_i))\pmod4\tag{5}
\]

is independent of the rational orthogonal basis.

Rescaling and permutation preserve (5) by Lemma 1. For an orthogonal pair
`e,f` of positive norms `a,b`, the rational change

\[
(e,f)\mapsto\left(e+f,\frac{be-af}{a+b}\right)\tag{6}
\]

produces another orthogonal pair with norms `a+b` and `ab/(a+b)`. Lemma 2
proves invariance under this elementary change.

These changes relate any two rational orthogonal bases. Given a prescribed
nonzero vector `x=sum c_i e_i`, rescale participating basis vectors by `c_i`
and combine them successively with (6). At the end the first vector is x and
the remaining vectors span `x^perp`. Induct on dimension inside `x^perp`.
Thus (5) is a basis invariant.

## 4. Exact frame-null identity on A4

### Theorem 1

For every rational complete orthogonal frame `(v_1,v_2,v_3,v_4)` of V,

\[
\boxed{\sum_{i=1}^4 H([v_i])=0}\tag{7}
\]

as an integer identity.

**Proof.** First use the explicit rational orthogonal basis

\[
\begin{aligned}
b_1&=(1,1,-1,-1,0),\\
b_2&=(1,-1,1,-1,0),\\
b_3&=(1,-1,-1,1,0),\\
b_4&=(1,1,1,1,-4).
\end{aligned}
\]

Its norms are `4,4,4,20`, hence every h-value is zero. By Section 3, every
rational frame has H-sum congruent to zero modulo four. Because four summands
lie in `{-1,0,1}`, the integer sum can only be `-4,0,4`.

Use the integer basis `(e_0-e_4,...,e_3-e_4)` of A4. Its Gram matrix is

\[
G=I_4+\mathbf1\mathbf1^{\mathsf T},\qquad \det G=5.
\]

Let C be the rational coordinate matrix of an arbitrary orthogonal frame.
Then

\[
\prod_{i=1}^4 q(v_i)=\det(C^{\mathsf T}GC)=5(\det C)^2.\tag{8}
\]

Remove all powers of 3 from the four norms. The product of the remaining
nonzero unit residues is 2 modulo 3: the factor 5 contributes 2 and a rational
square contributes 1.

If the H-sum were `+4`, every H-value would be `+1`, hence all four unit
residues would be 2 and their product would be 1 modulo 3. If the H-sum were
`-4`, all four unit residues would be 1 and their product would again be 1.
Both contradict (8). Therefore the sum is exactly zero. QED.

The discriminant step is essential. On standard determinant-one Q^4, the
columns of

\[
\begin{pmatrix}
1&-1&-1&0\\
1&1&0&1\\
1&0&1&-1\\
0&-1&1&1
\end{pmatrix}
\]

are orthogonal of norm 3 and have H-sum `-4`.

## 5. Global positive nonquadratic family

### Theorem 2

For every rational `t` with `|t|<=1/4`,

\[
\boxed{w_t([v])=\frac14+tH([v])}\tag{9}
\]

is a rational-valued nonnegative normalized frame weight on **all** rational
rays of V. For `|t|<1/4`, it is uniformly strictly positive.

Theorem 1 gives normalization on every frame. Its range is exactly contained in
`{1/4-t,1/4,1/4+t}`.

The 30 inner Cl(4) rays consist of ten A4 root rays of norm 2, fifteen primitive
rays of norm 4, and five simplex rays represented by permutations of
`(4,-1,-1,-1,-1)` of norm 20. Their 3-valuations are even, so H=0 and every
member of the family has value `1/4` on all thirty rays.

### Six-ray cover witness

Use

\[
\begin{aligned}
d_1&=(2,-1,-1,0,0),&r_1&=(0,1,-1,0,0),\\
d_2&=(-1,2,-1,0,0),&r_2&=(1,0,-1,0,0),\\
d_3&=(-1,-1,2,0,0),&r_3&=(1,-1,0,0,0).
\end{aligned}
\]

The d-rays have norm 6 and H=+1. The r-rays have norm 2 and H=0. Therefore

\[
\boxed{D(w_t):=\sum_mw_t(d_m)-\sum_mw_t(r_m)=3t.}\tag{10}
\]

Direct projector arithmetic gives

\[
\sum_mP_{d_m}=\sum_mP_{r_m}.\tag{11}
\]

Both are `(3/2)P_U` on the common plane `U=U_012`.

Any quadratic assignment `w([v])=tr(WP_v)` with one symmetric W would respect
(11), hence would have D=0. Thus every nonzero-t member of (9) is nonquadratic,
even if W is not required to be positive.

For `t=1/8`, all weights lie in `{1/8,1/4,3/8}` and are therefore strictly
positive while `D=3/8`.

## 6. Exact logical consequence

The implication

```text
rational A4 rays
+ all complete rational orthogonal records
+ noncontextual frame additivity
+ positivity, even uniform strict positivity
=> quadratic reading
```

is false.

This theorem closes a proposed **uniqueness derivation** only. It does not
select a physical decoder and does not show that the nonquadratic family is
physically realized.

In particular, the result is compatible with explicitly choosing the
quadratic reading as one declared decoder branch. Public reading-family
discipline does not require global decoder uniqueness; it requires that a
reading used for a physical claim be frozen before target inspection and that
inequivalent admitted readings on the same physical context be independently
resolved, proved equivalent at the claimed scope, or left open.

## 7. Layer boundary

Everything proved above is L4 mathematics. No physical apparatus, ready state,
pointer, occurrence law, sampling rule, post-state instrument or L6 probability
measure is supplied. No claim about J, real Gleason theorems, or quantum
mechanics is falsified by this result.