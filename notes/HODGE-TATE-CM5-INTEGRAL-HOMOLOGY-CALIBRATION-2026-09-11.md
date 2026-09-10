# Hodge–Tate CM5: explicit integral homology calibration

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v83 and
`notes/HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md`.

**Date:** 2026-09-11.

This companion note attacks the next open calibration gate left by the parent
Hodge–Tate note. It does not change `canon/`, register a public claim, or start
a formal public probe.

## 1. Result

For

\[
C:\quad y^2=x^5-1,
\qquad
A=\operatorname{Jac}(C),
\qquad
T:(x,y)\mapsto(jx,y),
\]

there is an explicit integral basis of `H_1(C,Z) = H_1(A,Z)` in which

1. `T_*` is exactly the public multiplication-by-`j` companion matrix;
2. the topological intersection form is exactly the public `Omega_1`;
3. the change from the natural double-pentagon edge basis to this basis is
   multiplication by the TWIST-J unit `J^{-1}`.

Thus the external CM realization can be written exactly as

\[
\boxed{
 (\mathcal O_K,m_j,\Omega_1)
 \cong
 (H_1(A,\mathbf Z),T_*,E_A)
}
\]

up to the one global sign convention relating the oriented topological
intersection form to the chosen Riemann-form convention.

This closes the parent note's **Gate A** and supplies an explicit representative
for **Gate B** at note level. No Canon status is earned by this derivation.

## 2. Double-pentagon cell model

A standard translation-surface model of `C` is obtained by gluing two regular
pentagons along corresponding parallel sides. Let

\[
c_0,c_1,c_2,c_3,c_4
\]

be the five oriented side classes on the resulting surface, indexed
cyclically so that the order-five rotation satisfies

\[
T_*c_k=c_{k+1}
\]

with indices modulo five.

All ten polygon vertices are identified to one vertex. One way to see this is
to orient the first pentagon edges from `v_k` to `v_(k+1)`. Translation gluing
to the oppositely oriented corresponding edge of the second pentagon identifies
successive endpoints in such a way that

\[
v_{k+1}\sim v_{k-1}.
\]

Since `2` generates `Z/5Z`, all five first-pentagon vertices, and therefore all
ten polygon vertices, lie in one equivalence class.

The resulting CW decomposition has one zero-cell, five one-cells and two
two-cells. The two face boundaries are opposite and give one homology relation,

\[
\boxed{c_0+c_1+c_2+c_3+c_4=0}.
\]

Hence

\[
H_1(C,\mathbf Z)
 \cong
 \mathbf Z^5/\mathbf Z(1,1,1,1,1),
\]

and

\[
(c_0,c_1,c_2,c_3)
\]

is an integral basis.

This agrees with the standard module description

\[
H_1(C,\mathbf Z)
\cong
\mathbf Z[T]/(1+T+T^2+T^3+T^4).
\]

## 3. The order-five action is already the public `j` matrix

Because

\[
T_*c_0=c_1,
\quad
T_*c_1=c_2,
\quad
T_*c_2=c_3,
\quad
T_*c_3=c_4=-c_0-c_1-c_2-c_3,
\]

the matrix of `T_*` in the edge basis is

\[
M=
\begin{pmatrix}
0&0&0&-1\\
1&0&0&-1\\
0&1&0&-1\\
0&0&1&-1
\end{pmatrix}.
\]

This is exactly the companion matrix of multiplication by `j` in the public
basis

\[
(1,j,j^2,j^3)
\]

of `O_K = Z[j]`. Therefore

\[
\iota_c:\mathcal O_K\longrightarrow H_1(C,\mathbf Z),
\qquad
\iota_c(j^k)=c_k,
\]

is already an explicit integral `O_K`-module isomorphism, with

\[
\iota_c(jx)=T_*\iota_c(x).
\]

No rationalization or finite-index correction is required.

## 4. Intersection form in the natural edge basis

The five edge loops meet only at the single identified polygon vertex before
a local perturbation. Remove a small oriented disk around that point. Each
`c_k` becomes an arc with two boundary endpoints, denoted `c_k^+` and
`c_k^-` according to the outgoing and incoming orientation.

Following the corners of the two glued pentagons gives, up to cyclic shift,
the positive cyclic order

```text
c0+  c4-  c3+  c2-  c1+  c0-  c4+  c3-  c2+  c1-
```

on the boundary of the removed disk. Closing each arc inside the disk, two
classes intersect once exactly when their endpoint pairs alternate. The sign
is the oriented crossing sign. In the basis `(c0,c1,c2,c3)` this gives

\[
W_c=
\begin{pmatrix}
 0& 1&-1& 1\\
-1& 0& 1&-1\\
 1&-1& 0& 1\\
-1& 1&-1& 0
\end{pmatrix}.
\]

With the public forms

\[
\Omega_1=
\begin{pmatrix}
0&1&0&0\\
-1&0&1&0\\
0&-1&0&1\\
0&0&-1&0
\end{pmatrix},
\]

\[
\Omega_2=
\begin{pmatrix}
0&0&1&-1\\
0&0&0&1\\
-1&0&0&0\\
1&-1&0&0
\end{pmatrix},
\]

we obtain the exact identity

\[
\boxed{W_c=\Omega_1-\Omega_2=\Omega_{(1,-1)}}.
\]

Its Pfaffian is `-1`, so it is unimodular as required for the intersection
pairing of a compact oriented genus-two surface. Reversing the global
intersection-form convention negates the entire displayed matrix and changes
none of the structural conclusions below.

## 5. The required normalization is exactly `J^{-1}`

The natural edge basis therefore has the correct `j` action immediately but
displays the intersection form as `Omega_1-Omega_2`, not as the positive CM
representative `Omega_1` selected in the parent note.

The correction is not an arbitrary element of `GL_4(Z)`. It is multiplication
by the TWIST-J unit `J^{-1}`.

Since

\[
J=1+j^2,
\]

one has exactly

\[
\boxed{J^{-1}=-(j+j^2)},
\]

because

\[
(1+j^2)(-j-j^2)
 =-(j+j^2+j^3+j^4)=1.
\]

Define

\[
d_0=J^{-1}c_0=-c_1-c_2,
\qquad
d_k=T_*^k d_0.
\]

Using `c_4=-c_0-c_1-c_2-c_3`, the first four vectors are

\[
\begin{aligned}
d_0&=-c_1-c_2,\\
d_1&=-c_2-c_3,\\
d_2&= c_0+c_1+c_2,\\
d_3&= c_1+c_2+c_3.
\end{aligned}
\]

Thus the change-of-basis matrix whose columns are `d_0,...,d_3` in the
`c` basis is

\[
\boxed{
P=
\begin{pmatrix}
 0& 0&1&0\\
-1& 0&1&1\\
-1&-1&1&1\\
 0&-1&0&1
\end{pmatrix}
}
\]

and direct integer elimination gives

\[
\boxed{\det P=1}.
\]

So `(d0,d1,d2,d3)` is an integral basis, not merely a rational basis or a
finite-index sublattice.

Matrix-wise,

\[
\boxed{P=-(M+M^2)}
\]

and therefore

\[
MP=PM.
\]

Moreover, if

\[
M_J=I+M^2,
\]

then

\[
\boxed{M_JP=PM_J=I}.
\]

Thus `P` is literally multiplication by `J^{-1}` on the public cyclotomic
lattice.

## 6. Exact simultaneous match

Because `P` commutes with `M`, the order-five action in the `d` basis is still

\[
\boxed{P^{-1}MP=M}.
\]

For the intersection form, exact integer multiplication gives

\[
\boxed{P^T W_c P=\Omega_1}.
\]

Consequently the map

\[
\iota:\mathcal O_K\longrightarrow H_1(C,\mathbf Z),
\qquad
\iota(1)=d_0,
\qquad
\iota(j^k)=d_k,
\]

simultaneously satisfies

\[
\boxed{\iota\circ m_j=T_*\circ\iota}
\]

and

\[
\boxed{E_C(\iota(x),\iota(y))=\Omega_1(x,y)}
\]

for the displayed orientation convention.

Using the standard identification of the Jacobian period lattice with
`H_1(C,Z)`, the same gives

\[
\boxed{
(H_1(A,\mathbf Z),T_*,E_A)
\cong
(\mathcal O_K,m_j,\Omega_1).
}
\]

This is stronger than an abstract classification of principal polarizations:
it exhibits one exact integral basis realizing the public representative
`Omega_1` while keeping the public `j` matrix unchanged.

## 7. Relation to the public `J` pullback

The parent note observed that the public pullback matrix

\[
A_J=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix}
\]

sends the parameter vector of `Omega_1` to that of

\[
\Omega_1-\Omega_2.
\]

The double-pentagon computation now gives a geometric meaning to precisely
this already-public algebraic relation:

\[
\boxed{W_c=J^*\Omega_1}.
\]

Passing from the raw edge generator `c_0` to

\[
d_0=J^{-1}c_0
\]

therefore removes exactly that pullback and returns the intersection matrix to
`Omega_1`.

This is an external realization of the public `J` action. It is not a new
Canon theorem and it does not give a physical interpretation to the Jacobian.

## 8. Gate disposition

Against the work programme in the parent note:

**Gate A, integral CM identification: NOTE-LEVEL PASS.** The basis
`(d0,d1,d2,d3)` is explicit; `P` is integral unimodular; and
`P^{-1}MP=M` exactly.

**Gate B, principal polarization representative: NOTE-LEVEL PASS.** In the
same basis, the canonical surface/Jacobian intersection pairing is `Omega_1`,
which is the principal-polarization class selected algebraically in section 5A
of the parent note.

**Gate C, Hodge positivity:** the abstract positivity check was already done in
section 5A. The present basis supplies its missing topological representative.
A later formal probe may repeat it under a preregistered exact verifier if
promotion is desired.

**Gate D, existing `J` action:** reproduced structurally here by
`P=J^{-1}` and `W_c=J^*Omega_1`; this earns no new public status because the
`J` pullback itself is already a Canon theorem.

The next genuinely new calibration task is therefore **Gate E**, the exact
Hodge-tensor census on small powers `A^n`, checked against the known
nondegenerate-CM answer.

## 9. Exact audit identities

All algebra needed for the matrix part reduces to the following finite list of
integer identities:

```text
M^4 + M^3 + M^2 + M + I = 0
P = -(M + M^2)
det(P) = 1
(I + M^2) P = P (I + M^2) = I
M P = P M
W_c = Omega_1 - Omega_2
P^T W_c P = Omega_1
```

No floating-point arithmetic or numerical period integration enters this
calibration.

## 10. Boundary and nonclaims

This result does not overturn `CM-PERIOD-LATTICE-NONSELECTION [T]`. The bare
TWIST-J CM pencil still does not select a torus, homology carrier, or
polarization. The selection here uses additional external mathematical data:

```text
the algebraic curve y^2=x^5-1
+ its double-pentagon translation-surface model
+ its order-five automorphism
+ its complex orientation and principal Jacobian polarization.
```

Nor does the result advance the Hodge or Tate conjecture. It establishes an
exact polarized integral CM realization on a solved benchmark. The difficult
future step remains the classification, and eventually algebraicity, of
higher-codimension Hodge or Tate classes in genuinely nontrivial families.

The prime `5` also remains excluded from the good-reduction Tate calibration;
this topological calculation changes nothing about that restriction.

## References

- C. McMullen, *Riemann Surfaces* course notes, pentagon example and the
  `Z[T]/(1+T+T^2+T^3+T^4)` homology description:
  https://people.math.harvard.edu/~ctm/home/text/class/harvard/213b/19/html/home/course/course.pdf
- J. Boulanger, E. Lanneau, D. Massart, *Algebraic intersection for a family
  of Veech surfaces*, Annales Henri Lebesgue 7 (2024), 787-821, especially
  the double regular odd-gon side-intersection calculation:
  https://doi.org/10.5802/ahl.211
- Parent TWIST-J note:
  `notes/HODGE-AND-TATE-CM5-CALIBRATION-2026-09-11.md`
- Public Canon v83:
  `canon/CANON.md`
