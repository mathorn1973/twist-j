# PROOF - C-HEXAGON-HODGE-PHOTON-SEAM-N

**Status:** candidate-T, PUBLIC NON-CANONICAL.  
**Owner:** issue #1219.  
**Author:** A. M. Thorn <thorn@twistj.com>.  
**Date:** 2026-09-27.  
**Frozen public readback basis:** branch head `2a8b368ece347a6b291d727415211de41cb51c4c`, with preregistration and both standard-library audit sources read back before execution.

No Canon status is asserted here.

## 1. Boundary inherited from Public Canon v92

The proof uses only the registered L1 theorems named in `PREREG.md`.
In particular, write

\[
F=\mathbb Q(\sqrt5),\qquad W_F=(\Lambda^2A_4)\otimes F,
\]

and let `L` be the marked exterior J-step. The accepted fixed-J predictive
carrier `E_+` is four-dimensional and `A=L|E_+` has

\[
p_E(X)=(X^2-3X+1)(X^2-\varphi X+1),
\qquad \varphi=(1+\sqrt5)/2.
\]

Set

\[
B=\Lambda^2 A:\Lambda^2E_+\to\Lambda^2E_+.
\]

Both source and target therefore have F-dimension six. Equality of dimensions
is the only fact being tested here. It is not assumed to imply an
identification.

## 2. The planar hexagon is a mnemonic, not a forced integer split

For `(r0,...,r5)` consider the frozen display coordinates

\[
\begin{aligned}
x_0&=r_0-r_3,&x_1&=r_1-r_4,&x_2&=r_2-r_5,\\
\tau&=\sum_{i=0}^5r_i,\\
g_1&=r_0+r_3-r_1-r_4,\\
g_2&=r_0+r_3+r_1+r_4-2r_2-2r_5.
\end{aligned}
\]

The corresponding integer matrix has

\[
|\det H|=48.
\]

Hence it is invertible over Q and modulo five, but it is not unimodular over
Z. Its integer outputs occupy an index-48 sublattice. They are not six free
integer coordinates.

The antipodal-odd subspace contains

\[
v=(1,-1,1,-1,1,-1).
\]

One vertex rotation sends `v` to `-v`. Thus this three-dimensional odd
subspace already contains an invariant line and is reducible under the planar
cycle. The drawing does not symmetry-force an irreducible spatial triple.

This is a correction of the conversational `3+1+2` picture, not a rejection
of using a hexagon as a label diagram.

## 3. The two six-dimensional J modules have different spectra

### 3.1 Source exterior carrier

In the marked A4 basis `e0-e4,...,e3-e4`, the five-cycle is

\[
C=\begin{pmatrix}
-1&-1&-1&-1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
\]

Put `M=I+C^2` and `L=Lambda^2 M`. Exact characteristic-polynomial
calculation gives

\[
\boxed{
p_W(X)=(X^2-3X+1)(X^4-X^3+X^2-X+1).
}
\]

Write `zeta=zeta_10`. Over C its eigenvalues are

\[
\boxed{
\varphi^2,\ \varphi^{-2},\ \zeta,\ \zeta^3,\ \zeta^7,\ \zeta^9.
}
\]

The first pair is hyperbolic and the last four are primitive tenth-root
phases.

### 3.2 Two-forms of the fixed-J four-chart

The roots of `p_E` are

\[
\varphi^2,\quad \varphi^{-2},\quad \zeta,\quad \zeta^{-1}.
\]

Therefore `B=Lambda^2 A` has eigenvalues

\[
\boxed{
1,\ 1,\
\varphi^2\zeta,\ \varphi^2\zeta^{-1},\
\varphi^{-2}\zeta,\ \varphi^{-2}\zeta^{-1}.
}
\]

Its exact characteristic polynomial is

\[
\boxed{
p_B(X)=(X-1)^2
\left[X^4-3\varphi X^3+(8+\varphi)X^2-3\varphi X+1\right].
}
\]

The standard-library audit reconstructs both polynomials independently and
finds

\[
\gcd_F(p_W,p_B)=1.
\]

## 4. Same-step theorem: the only intertwiner is zero

Freeze an F-linear map

\[
S:W_F\to\Lambda^2E_+
\]

satisfying

\[
SL=BS.
\]

Then for every polynomial `f`,

\[
S f(L)=f(B)S.
\]

By Cayley-Hamilton `p_W(L)=0`, hence

\[
p_W(B)S=0.
\]

Since `gcd(p_W,p_B)=1`, choose `u,v in F[X]` such that

\[
u p_W+v p_B=1.
\]

Again by Cayley-Hamilton, `p_B(B)=0`, so

\[
u(B)p_W(B)=I.
\]

Therefore `S=0`.

Thus

\[
\boxed{
\operatorname{Hom}_{F[L]}(W_F,\Lambda^2E_+)=0.
}
\]

This is `SAME-STEP-ZERO`.

## 5. Complete positive-integer blocking theorem

The direct failure raises the natural repair attempt: sample the source every
`m` J-steps and the target every `n` induced two-form steps.

For positive integers `m,n`, define

\[
\mathcal H_{m,n}
=
\{S:S L^m=B^nS\}.
\]

Both operators are semisimple in characteristic zero. Extending scalars does
not change the dimension of the solution space of this F-linear matrix
system. Therefore its dimension is obtained by matching eigenspace
multiplicities over C.

The source labels are

\[
\varphi^{2m},\ \varphi^{-2m},\
\zeta^m,\ \zeta^{3m},\ \zeta^{7m},\ \zeta^{9m},
\]

and the target labels are

\[
1,1,
\varphi^{2n}\zeta^n,\ \varphi^{2n}\zeta^{-n},
\varphi^{-2n}\zeta^n,\ \varphi^{-2n}\zeta^{-n}.
\]

An equality

\[
\varphi^a\zeta^b=\varphi^{a'}\zeta^{b'}
\]

first forces `a=a'` by absolute values because `phi>1`, then
`b=b' mod 10` by phase. Hence the labels may be matched as ordered pairs
`(a,b mod 10)`.

### Case 1: `10` does not divide `m`

None of the four unit-modulus source eigenvalues is `1`, because
`1,3,7,9` are units modulo ten. The positive real source eigenvalues cannot
match a target hyperbolic-phase eigenvalue unless `m=n` and the target phase
is one, which would require `10|n= m`. Contradiction.

Therefore

\[
\boxed{\dim_F\mathcal H_{m,n}=0.}
\]

### Case 2: `10|m` and `m!=n`

All four phase eigenvalues of `L^m` collapse to `1`. The source `1`-eigenspace
has dimension four, while the target `1`-eigenspace has dimension two.
There is no hyperbolic match because equality of moduli would require `m=n`.
Thus

\[
\boxed{\dim_F\mathcal H_{m,n}=4\cdot2=8.}
\]

Every such map has rank at most two.

### Case 3: `10|m` and `m=n`

The fixed-space contribution again gives eight dimensions of Hom. In addition,
`phi^(2m)` occurs with multiplicities `1` in the source and `2` in the target,
and the same is true for `phi^(-2m)`. Therefore

\[
\boxed{
\dim_F\mathcal H_{m,m}=8+1\cdot2+1\cdot2=12.
}
\]

The maximum possible rank is

\[
\min(4,2)+\min(1,2)+\min(1,2)=4.
\]

It is attained over `F`: after scalar extension a nonzero four-by-four minor
exists, so the corresponding minor polynomial is not identically zero on the
F-vector space `H_(m,m)`; the infinite field `F` contains an F-point where it
is nonzero.

Hence synchronized ten-step blocking produces a genuine rank-four linear seam
between the two six-dimensional carriers.

It is nevertheless never invertible. On the common eigenvalue `1`, source
multiplicity is four and target multiplicity is two, so every intertwiner has
kernel dimension at least two. Equivalently, the complete multiplicity
profiles differ:

\[
(4,1,1)\ne(2,2,2).
\]

Combining the cases,

\[
\boxed{
\dim_F\mathcal H_{m,n}=
\begin{cases}
0,&10\nmid m,\\
8,&10\mid m,\ m\ne n,\\
12,&10\mid m=n,
\end{cases}
}
\]

and no positive pair `(m,n)` admits an invertible intertwiner.

Target time reversal replaces each `zeta^b` by `zeta^(-b)` and leaves its
spectral multiset unchanged. It does not repair the obstruction.

## 6. What the rank-four blocked seam means, and what it does not

The ten-step phase closure is not cosmetic. At `m=n=10k`, the tenth-root
phases close and the two six-dimensional modules acquire a four-dimensional
maximum common image.

This is an exact algebraic `6 -> rank 4` statement. It is **not** a theorem
that four-dimensional spacetime has emerged. In particular:

- the kernel of a maximum-rank intertwiner is a two-dimensional subspace of
  the four-dimensional source fixed space and is not selected by this theorem;
- the one-dimensional choices inside the two target hyperbolic eigenspaces are
  likewise not selected;
- no metric, null cone, orientation, field normalization or physical carrier
  has been imposed on the rank-four image;
- the result compares `W_F` with `Lambda^2 E_+`, not with the current photon
  carrier `T_D3`.

The result therefore supplies a sharply typed next question rather than a
physical closure: does the already existing Hodge, wedge and photon
characteristic structure select one of these rank-four blocked seams and make
its null geometry agree with the photon characteristic without putting that
answer into the definition?

## 7. Axial recurrence boundary

The accepted primary recurrence is

\[
(y,z)\mapsto(3y-z,y).
\]

The quadratic form

\[
I(y,z)=y^2-3yz+z^2
\]

obeys

\[
I(3y-z,y)=I(y,z).
\]

Its Gram matrix is

\[
\begin{pmatrix}1&-3/2\\-3/2&1\end{pmatrix},
\]

whose determinant is `-5/4`. Hence it has real signature `(1,1)`.

This is an invariant of the predictive recurrence. It is not by itself the
selected photon temporal characteristic and is not used to alter the photon
program.

## 8. Status

- planar-hexagon determinant/reducibility correction: **candidate-T**;
- same-step zero-Hom theorem: **candidate-T**;
- all-positive-integer blocked Hom dimension theorem: **candidate-T**;
- synchronized ten-step maximum rank four corollary: **candidate-T**;
- exact standard-library audits: **candidate-C corroboration**;
- physical dimension/time, photon carrier identification, cone equivalence,
  massless phase, continuum and apparatus: **unchanged / OPEN where already
  open**.
