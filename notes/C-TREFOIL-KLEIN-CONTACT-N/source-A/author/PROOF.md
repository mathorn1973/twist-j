# Exact marked Klein coordinates and their ramified boundary

Status: NON-CANONICAL, candidate-T analytic result. Native realization, topological stability in physical space, the baryon interpretation, and mass prediction remain OPEN.

Public basis: Canon v103 ACTIVE at `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`. The owned results used here are COLOR-CORE-2I, COLOR-SPECTRAL-INVARIANTS, COLOR-KLEIN-REDUCTION, COLOR-INTEGRAL-LIFT, and the invariant-Hermitian-form existence in COLOR-CM-2I-SEMILINEAR-PAIR. The old color-ladder reproduction already constructs marked invariants by averaging. The new statement supplies an explicit coordinate map and fully specified normalizations.

The frozen auxiliary checks are in PREREG.md, SHA-256 `d64ab46179bfe2acfaae3f61cbfdc9adc3c3c6a9e1048a92987d0e5bf7218053`. This proof is independent of a finite enumeration: the checks support the displayed identities but do not replace the arguments below.

## 1. Coefficient ring and action convention

Let

\[
K=\mathbb Q(j),\quad O=\mathbb Z[j],\quad
j^4+j^3+j^2+j+1=0,
\]

with principal embedding \(j=e^{2\pi i/5}\). Conjugation is \(c(j)=j^4\). Put

\[
\lambda=1-j,\quad a=j+j^4=\varphi^{-1},\quad
s=j^2-j^3=j^2\lambda,\quad r=j-j^4.
\]

Reduction modulo \(\lambda\) has residue field \(\mathbb F_5\). Its valuation is normalized by \(v_\lambda(\lambda)=1\), so \(v_\lambda(s)=1\), \(v_\lambda(5)=4\). The valuation of a polynomial means the minimum valuation of its nonzero coefficients.

Direct cyclotomic identities give

\[
a^2+a=1,\qquad s^2=a-2,\qquad s^4=5a^2,
\qquad r=s/a,
\]

\[
c(a)=a,\quad c(s)=-s,\quad a^2+s^2=-1,
\quad J=1+j^2=aj.
\]

All matrix actions below are on columns. Invariance means \(p(gv)=p(v)\). The old rung-11 substitution uses the transposed convention. This does not change the invariant ring of the entire marked group: for determinant-one matrices,

\[
g^T=Sg^{-1}S^{-1},\qquad
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]

and \(S\) belongs to the group. Nevertheless, a generator or a point must always be transported using the stated convention.

## 2. An explicit coordinate change

Keep the public marked generators

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T=\begin{pmatrix}j&1\\0&j^4\end{pmatrix}.
\]

Define

\[
P=\begin{pmatrix}1&-a\\0&s\end{pmatrix},\qquad
B=sP^{-1}=\begin{pmatrix}s&a\\0&1\end{pmatrix}.
\]

Both determinants are \(s\), so both matrices are invertible over \(K\), and over \(O[1/\lambda]\). Direct multiplication, using the identities in Section 1, gives

\[
P^{-1}TP=D=\begin{pmatrix}j&0\\0&j^4\end{pmatrix},
\]

\[
P^{-1}SP=E=
\begin{pmatrix}1/r&1/s\\1/s&-1/r\end{pmatrix}.
\]

Equivalently, \(BT=DB\) and \(BS=EB\). The key off-diagonal simplification is

\[
-s-a^2/s=1/s.
\]

The matrices \(D,E\) have determinant one. Moreover \(E^2=-I\), \(E^\dagger=-E\), hence \(E^\dagger E=I\), and \(D^\dagger D=I\).

This is an explicit conjugacy of marked representations, not an inference from a common group order.

## 3. Why these are the standard Klein coordinates

Write the standard forms as in PREREG.md:

\[
f_0(x,y)=xy(x^{10}+11x^5y^5-y^{10}),
\]

\[
H_0=-x^{20}-y^{20}+228x^{15}y^5
-228x^5y^{15}-494x^{10}y^{10},
\]

\[
W_0=x^{30}+y^{30}+522x^{25}y^5
-522x^5y^{25}-10005x^{20}y^{10}-10005x^{10}y^{20}.
\]

The public standard identity is

\[
W_0^2+H_0^3=1728f_0^5.
\tag{1}
\]

For completeness, the exact covariant normalizations are

\[
H_0=\frac{\det\operatorname{Hess}(f_0)}{121},\qquad
W_0=\frac{\operatorname{Jac}(f_0,H_0)}{20},
\tag{2}
\]

where \(\operatorname{Jac}(p,q)=p_xq_y-p_yq_x\).

To identify the coordinates, factor

\[
f_0(x,y)=xy\prod_{k=0}^4(x-aj^k y)
\prod_{k=0}^4(x+\varphi j^k y).
\tag{3}
\]

Indeed \(\varphi^5-a^5=11\) and \(\varphi^5a^5=1\). Its twelve distinct projective roots are

\[
0,\ \infty,\ aj^k,\ -\varphi j^k\quad(0\le k<5).
\]

The matrix \(D\) preserves them, and preserves the polynomial itself. On \(t=x/y\), the matrix \(E\) acts by

\[
h(t)=\frac{at+1}{t-a}.
\]

It permutes the roots in the six pairs

\[
(0,-\varphi),\quad(\infty,a),\quad
(aj,-\varphi j),\quad(aj^4,-\varphi j^4),
\]

\[
(aj^2,aj^3),\quad(-\varphi j^2,-\varphi j^3).
\]

Thus \(f_0\) spans an invariant line under \(\langle D,E\rangle\). Its scalar action is a group character. This group is conjugate to the already proved perfect group \(\langle S,T\rangle=2I\), so that character is trivial. Therefore \(f_0\) is invariant. Formula (2), together with determinant-one covariance of the Hessian and Jacobian, proves that \(H_0,W_0\) are invariant as well.

Consequently the substitutions

\[
\widehat f=f_0(su+av,v),\quad
\widehat H=H_0(su+av,v),\quad
\widehat W=W_0(su+av,v)
\]

are invariant under the exact public marked matrices \(S,T\). They have coefficients in \(O\) and satisfy (1) after substitution.

## 4. Exact primitive normalization at the ramified place

Define

\[
F=\widehat f/s^{10},\qquad
H=\widehat H/s^{20},\qquad
W=\widehat W/s^{25}.
\tag{4}
\]

We prove that these are integral and primitive, with the claimed reductions.

### 4.1 The degree-12 form

Substitute \(x=su+av\) into (3). Each of the ten factors in its two products is divisible by \(s\) over \(O\). For the first product this follows from \(1-j^k\) being divisible by \(1-j\). For the second use

\[
a+\varphi j^k=\sqrt5+\varphi(j^k-1),
\qquad v_\lambda(\sqrt5)=2.
\]

Since \(s=j^2\lambda\), division by \(s\) introduces no other prime denominator. Therefore \(F\in O[u,v]\).

Modulo \(\lambda\), both products divided by \(s^5\) become

\[
\prod_{k=0}^4(u+2kv)=u^5-uv^4.
\]

The remaining factor \((su+av)v\) becomes \(2v^2\). Thus

\[
\overline F=2v^2(u^5-uv^4)^2=2E_6^2,
\qquad E_6=u^5v-uv^5.
\tag{5}
\]

It is nonzero. Hence \(v_\lambda(\widehat f)=10\) exactly, and \(F\) is primitive.

### 4.2 The degree-20 form

Put \(b=a^5\). It satisfies \(b^2+11b-1=0\). Define

\[
q(u,v)=\frac{(su+av)^5-bv^5}{s^5}.
\]

The binomial expansion and \(5/s^4=a^{-2}\) show that \(q\in O[u,v]\) and

\[
\overline q=u^5-uv^4.
\tag{6}
\]

Let

\[
h(y)=-y^4+228y^3-494y^2-228y-1.
\]

Then \(H_0(x,v)=v^{20}h(x^5/v^5)\), interpreted homogeneously. Exact reduction by \(b^2+11b-1\) gives

\[
h(b)=-3125b^2,
\]

\[
h'(b)=500-9000b,
\]

\[
h''(b)/2=750b-500,
\]

\[
h'''(b)/6=228-4b,\qquad h''''(b)/24=-1.
\]

Their respective lambda valuations are

\[
(20,18,12,6,0).
\tag{7}
\]

For the middle entries one may use

\[
1-18b=5\sqrt5(4\sqrt5-9),
\]

\[
57-b=\frac{5\sqrt5}{2}(5\sqrt5-1),
\]

and \(3b-2\) being a lambda-unit. The denominator 2 is a unit at the ramified place.

Substitute \(x^5=bv^5+s^5q\). The five terms in the Taylor expansion of \(H_0\) have valuations at least

\[
(20,23,22,21,20).
\]

Thus \(\widehat H/s^{20}\) is integral. There are no hidden denominators at any other prime, since the original form was integral and only powers of \(s\) were divided out. Finally

\[
\frac{h(b)}{s^{20}}
=-\frac{5^5a^{10}}{(5a^2)^5}=-1.
\]

Only the constant term and the fourth power of \(q\) survive reduction. Hence

\[
\overline H=-v^{20}-(u^5-uv^4)^4=-D_{20},
\tag{8}
\]

where \(D_{20}=(u^5-uv^4)^4+v^{20}\). This proves the exact valuation 20 and primitive residue scalar 4.

### 4.3 The degree-30 form

Use the substituted identity (1):

\[
\widehat W^2=1728s^{50}F^5-s^{60}H^3.
\]

Its right side has coefficient valuation exactly 50. The first term has a nonzero reduction after division by \(s^{50}\), while the second has strictly larger valuation. The coefficient valuation is multiplicative for polynomials over a discretely valued field. Therefore

\[
v_\lambda(\widehat W)=25.
\]

Division by \(s^{25}\) yields \(W\in O[u,v]\), primitive, and

\[
W^2+s^{10}H^3=1728F^5.
\tag{9}
\]

The sign of its reduction follows from the Jacobian rather than a square-root choice. Covariance under \(B\), whose determinant is \(s\), gives

\[
\operatorname{Jac}(\widehat f,\widehat H)=20s\widehat W.
\]

After (4),

\[
W=\frac{s^4}{20}\operatorname{Jac}(F,H)
=\frac{a^2}{4}\operatorname{Jac}(F,H).
\tag{10}
\]

Using (5) and (8) in characteristic five,

\[
\operatorname{Jac}(2E_6^2,-D_{20})=-E_6^5.
\]

Moreover \(a^2/4\equiv1\pmod\lambda\). Hence

\[
\overline W=-E_6^5.
\tag{11}
\]

Equations (5), (8), (11) give the exact frozen residue triple \((2,4,4)\), including its sign, and \(\overline W^2=3\overline F^5\).

## 5. Geometric transport and the integral model are different normalizations

The direct pullback by \(P^{-1}=B/s\) is

\[
f_K=f_0\circ P^{-1}=F/s^2,\qquad
H_K=H_0\circ P^{-1}=H,\qquad
W_K=W_0\circ P^{-1}=W/s^5.
\]

It satisfies precisely

\[
W_K^2+H_K^3=1728f_K^5
\tag{12}
\]

over \(K\), with coefficient valuations \((-2,0,-5)\). In contrast, the integral primitive forms satisfy (9), with the nonunit coefficient \(s^{10}\). Both are exact statements. They are not the same integral normalization.

The singularity of the coordinate change at \(\lambda\) is unavoidable for this diagonalization. Reducing the two marked matrices gives

\[
\overline D=I,\qquad
\overline T=\begin{pmatrix}1&1\\0&1\end{pmatrix}\ne I.
\]

If a diagonalizing change of coordinates belonged to \(\mathrm{GL}_2(O_{(\lambda)})\), its reduction would conjugate these two matrices. No invertible matrix can conjugate the identity to a nonidentity matrix. Thus no such integral diagonalization exists.

There is also an invariant-form normalization obstruction. The owned Molien series gives one-dimensional invariant spaces in degrees 12,20,30. Any alternative forms in those degrees are \((cF,dH,eW)\) for nonzero scalars in \(K\). Algebraic independence of \(F,H\) follows from their nonzero Jacobian (10). Requiring the standard relation forces

\[
e^2=c^5,\qquad d^3=e^2s^{10}.
\]

If the degree-12 and degree-30 forms were both lambda-primitive, then \(v_\lambda(c)=v_\lambda(e)=0\). The second equation would require

\[
3v_\lambda(d)=10,
\]

impossible for a scalar in \(K\). A further ramified field extension would be a different coefficient carrier.

Over \(K\), the displayed forms generate the full invariant ring: their quadratic relation defines an integral graded algebra because its right side is not a square in \(K(F,H)\) (it has odd degree three in \(H\)). Its Hilbert series is exactly the owned Molien series

\[
\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]

The inclusion in \(K[u,v]^G\) therefore has equal dimensions in every degree and is equality. This conclusion concerns the field-valued invariant ring. It does not assert that the three primitive forms generate \(O[u,v]^G\).

At the ramified place their polynomial image is

\[
\mathbb F_5[E_6^2,D_{20},E_6^5]
\subsetneq \mathbb F_5[E_6,D_{20}],
\]

where the right side is the owned Dickson invariant ring. The degree-6 generator is absent from the image. In its fraction field it can be recovered as

\[
E_6=\overline W/\overline F^2,
\]

and it is integral, since \(E_6^2=3\overline F\). The normalization of the special-fiber algebra adds precisely this missing parameter (and retains the free degree-20 parameter). Thus the characteristic-zero geometric picture cannot simply be identified with the reduced polynomial image.

## 6. A fixed J-bearing branch point on an invariant unit ellipsoid

Take

\[
v_0=\binom{-a}{j^2}.
\]

Its image under the already fixed matrix \(B\) is

\[
Bv_0=\binom{a(j^2-s)}{j^2}
=\binom{aj^3}{j^2}
=j^2\binom{J}{1}.
\]

Since \(J=aj\), it is one of the projective roots listed in (3). Consequently

\[
f_0(J,1)=0,\qquad F(v_0)=0.
\]

The unitary standard representation provides the explicit Hermitian form

\[
M=(P^{-1})^\dagger P^{-1}
=\begin{pmatrix}1&a/s\\-a/s&1\end{pmatrix}.
\]

It satisfies \(S^\dagger MS=M\), \(T^\dagger MT=M\),

\[
\operatorname{tr}M=2,\qquad \det M=-1/s^2.
\]

At each archimedean place, \(s\) is nonzero and purely imaginary. Thus \(-1/s^2>0\), and the Hermitian matrix with trace 2 and positive determinant is positive definite. This supplies one explicit normalization of the already owned invariant Hermitian line.

Finally

\[
v_0^\dagger Mv_0
=\|P^{-1}v_0\|^2
=\frac{1+a^2}{-s^2}=1.
\]

The normalized ellipsoid \(v^\dagger Mv=1\) is a mathematical coordinate choice. It supplies no physical length or energy scale.

## 7. What this pays and what it leaves open

The marked integral spin carrier, its characteristic-zero Klein invariant surface, a specified Hermitian sphere, and the fixed J-bearing point are now connected by explicit formulas. Scalar multiplication by \(j^3\) commutes with the coordinate change and has the same degree-dependent action on either invariant normalization: it fixes degrees 20 and 30 and multiplies degree 12 by \(j\).

After an archimedean embedding, the standard Klein surface can therefore be used for the separately established fivefold trefoil-branching construction with no unexplained change of matrix coordinates. At the ramified prime the proved coefficient and generator changes must be retained.

This supplies no map from the actual autonomous U to the spin carrier, no physical-space embedding, no topological protection under allowed microscopic moves, no energy functional, and no baryon or mass identification. Those are separate research obligations. The local exact computations were performed on one x86_64 environment and are not represented as a public two-architecture gate.
