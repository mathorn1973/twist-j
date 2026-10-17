# Exact comparison of five selected field cells

NON-CANONICAL. Mathematical candidate at L1, submitted under
`P-FIELD-CELL-SHEAR-CENSUS-1`. The formulas below are analytic proofs on
the displayed carriers. The accompanying finite exact verifier audits these
formulas; it is not the source of their universal quantifiers. The five
orders were disclosed targets before this work. No physical interpretation,
native-U/J selection, or classification of all cell complexes is asserted.

## 1. Exact cells, coordinates, and incidence

Use the graph boundary convention `+1` at the tail and `-1` at the head.
Every edge in a listed tuple is a distinct edge, even when its endpoints
coincide with those of another edge. Digons are legitimate attached
two-dimensional CW cells bounded by two parallel edges. They are not
triangles in a simple graph. In each case the columns of `C` are the
oriented attaching cycles of the listed faces. Thus `D C=0` is an actual
boundary identity, not just an assigned Gram matrix.

The frozen five representatives are as follows. Indices of edges start at
zero, and rows of `D` follow the vertex order shown by their integer labels.

```text
G2: one digon
edges = ((0,1),(0,1)); faces = (e0-e1)
D = [[ 1, 1],
     [-1,-1]]
C = [[ 1],
     [-1]]
G = C^t C = [[2]]

G3: one triangle
edges = ((0,1),(1,2),(2,0)); faces = (e0+e1+e2)
D = [[ 1, 0,-1],
     [-1, 1, 0],
     [ 0,-1, 1]]
C = [[1],[1],[1]]
G = [[3]]

G22: two digons sharing one edge
edges = ((0,1),(0,1),(0,1)); faces = (e0-e1,e0-e2)
D = [[ 1, 1, 1],
     [-1,-1,-1]]
C = [[ 1, 1],
     [-1, 0],
     [ 0,-1]]
G = [[2,1],[1,2]]

G23: one digon and one triangle sharing one edge
edges = ((0,1),(0,1),(0,2),(2,1)); faces = (e0-e1,e0-e2-e3)
D = [[ 1, 1, 1, 0],
     [-1,-1, 0,-1],
     [ 0, 0,-1, 1]]
C = [[ 1, 1],
     [-1, 0],
     [ 0,-1],
     [ 0,-1]]
G = [[2,1],[1,3]]

G33: two triangles sharing one edge
edges = ((0,1),(1,2),(2,0),(1,3),(3,0));
faces = (e0+e1+e2,e0+e3+e4)
D = [[ 1, 0,-1, 0,-1],
     [-1, 1, 0, 1, 0],
     [ 0,-1, 1, 0, 0],
     [ 0, 0, 0,-1, 1]]
C = [[1,1],
     [1,0],
     [1,0],
     [0,1],
     [0,1]]
G = [[3,1],[1,3]]
```

The boundary of each face telescopes along its closed edge path. Counting
the squared entries gives the diagonal Gram entries; the only common
nonzero row of the two columns is `e0`, with product `1`. This proves all
five displayed Gram identities directly. The Gram determinants are
`2,3,3,5,8`, respectively; the columns are independent.

For `m` edges and `n` faces, the raw carrier is
`(E,M) in Z^m x Z^n`. Its electric-first update is

```text
T_C(E,M) = (E+CM, M-C^t(E+CM)),
T_C = [[I_m,C],[-C^t,I_n-G]].
```

The active carrier is the embedded lattice `E=Cz`, with `(z,M) in Z^(2n)`.
In the ordered coordinates `(z1,...,zn,M1,...,Mn)`, its matrix is

```text
A_G = [[I_n,I_n],[-G,I_n-G]].
```

Indeed `E'=C(z+M)` and `M'=M-G(z+M)`. With the injective map
`P_C=diag(C,I_n)`, this is the identity `T_C P_C=P_C A_G`. Dimensions are:

| Cell | Vertices | Edges m | Faces n | Active dimension 2n | Raw dimension m+n |
| --- | ---: | ---: | ---: | ---: | ---: |
| G2 | 2 | 2 | 1 | 2 | 3 |
| G3 | 3 | 3 | 1 | 2 | 4 |
| G22 | 2 | 3 | 2 | 4 | 5 |
| G23 | 3 | 4 | 2 | 4 | 6 |
| G33 | 4 | 5 | 2 | 4 | 7 |

The five active matrices, in exactly that ordering, are

```text
A2 = [[1,1],[-2,-1]],
A3 = [[1,1],[-3,-2]],
A22 = [[ 1, 0, 1, 0],
       [ 0, 1, 0, 1],
       [-2,-1,-1,-1],
       [-1,-2,-1,-1]],
A23 = [[ 1, 0, 1, 0],
       [ 0, 1, 0, 1],
       [-2,-1,-1,-1],
       [-1,-3,-1,-2]],
A33 = [[ 1, 0, 1, 0],
       [ 0, 1, 0, 1],
       [-3,-1,-2,-1],
       [-1,-3,-1,-2]].
```

Every raw electric space splits over the rationals as
`im(C) + ker(C^t)`, by `z=G^-1 C^t E` and `E_perp=E-Cz`.
The perpendicular electric component is fixed by `T_C`, while the other
coordinates evolve by `A_G`. Consequently the raw matrix is rationally
similar to `A_G` plus an identity block of size `m-n`; its order equals
that of `A_G`. This does not assert that this splitting is unimodular or
that every raw integer state has integral `z` and `E_perp` coordinates.

## 2. Orientation equivalences and the exact canonical convention

Let `R` be any `m`-by-`m` diagonal matrix with entries `+1` or `-1`, and
let `S` be any such `n`-by-`n` matrix. Reversing edges and whole faces gives

```text
D_new = D R, C_new = R C S, G_new = S G S,
E_new = R E, M_new = S M, z_new = S z.
```

Since `R^2=I` and `S^2=I`, `D_new C_new=0`, and

```text
T_(C_new) = diag(R,S) T_C diag(R,S),
A_(G_new) = diag(S,S) A_G diag(S,S).
```

These are integer unimodular conjugacies, preserving determinant,
characteristic polynomial, matrix order, and the corresponding energy.
Reversing an edge changes an entire row of `C` and the same column of
`D`, so it leaves `G` unchanged. In particular, reversing the shared edge
alone cannot change the off-diagonal Gram sign. Reversing one entire face
does change the relative sign of its shared-edge coefficient and gives
`G_-=S G_+ S`, where `S=diag(1,-1)`. This is the meaning of the two
off-diagonal sign representatives here. Arbitrarily flipping one entry of
`C` while keeping the rest of its cycle fixed is not an orientation change
and generally violates `DC=0`.

For G23 the minus representative is exactly the v102 canonical cell:

```text
C_f = C23 diag(1,-1) = [[1,-1],[-1,0],[0,1],[0,1]],
G_f = [[2,-1],[-1,3]],
A_f = [[ 1, 0, 1, 0],
       [ 0, 1, 0, 1],
       [-2, 1,-1, 1],
       [ 1,-3, 1,-2]]
    = A_(G_f).
```

The Canon's active map
`P(a,b,c,d)=(a-b,-a,b,b,c,d)` is exactly `(C_f(a,b),(c,d))`.
Thus the identification uses its actual `(a,b,c,d)` order, and the positive
off-diagonal representative is conjugate through `diag(1,-1,1,-1)`.
No replacement of the canonical matrix, metric, physical law, or reading
is proposed.

## 3. Characteristic polynomial, determinant, and inverse

For any `n`-by-`n` matrix `G`, not necessarily one of the five, block
elimination at a scalar `t != 1` gives

```text
det(t I_(2n)-A_G)
 = det([[ (t-1)I,-I],[G,(t-1)I+G]])
 = det((t-1)^2 I+t G).                                      (1)
```

For completeness, the Schur complement of the first block is
`(t-1)I+G+G/(t-1)`, which, after multiplying its `n` rows by `t-1`,
gives the final matrix. Both sides are polynomials in `t` and agree at
every real `t != 1`; hence the identity also holds at `t=1`.

There is also a direct factorization and integer inverse:

```text
A_G = [[I,0],[-G,I]] [[I,I],[0,I]],  det(A_G)=1,
A_G^-1 = [[I-G,-I],[G,I]].                                  (2)
```

Thus integer `G` gives an automorphism of the entire active integer
lattice. For `n=2`, write `s=tr(G)` and `d=det(G)`. Expanding (1) gives

```text
chi_G(t) = t^4+(s-4)t^3+(d-2s+6)t^2+(s-4)t+1.              (3)
```

The exact specializations are

| Cell | Characteristic polynomial of A_G | Factorization |
| --- | --- | --- |
| G2 | `t^2+1` | `Phi4(t)` |
| G3 | `t^2+t+1` | `Phi3(t)` |
| G22 | `t^4+t^2+1` | `(t^2-t+1)(t^2+t+1)` |
| G23 | `t^4+t^3+t^2+t+1` | `Phi5(t)` |
| G33 | `t^4+2t^3+2t^2+2t+1` | `(t^2+1)(t+1)^2` |

Here `Phi_k` denotes the displayed cyclotomic polynomial. These are
identities from the fixed matrices, not a numerical fit of eigenvalues.

## 4. Conserved energy and its exact boundary

The general raw energy and its invariant are inherited from
`FIELD-SHEAR-ENERGY-BOUNDARY`:

```text
H_C(E,M)=E^t E+M^t M+E^t C M,
4H_C(E,M)=||2E+CM||^2+M^t(4I-G)M.                          (4)
```

To verify conservation directly, set `a=E+CM`. Substituting `E=a-CM`
in the old energy gives `a^t a+M^t M-a^t C M`. Substituting
`M_new=M-C^t a` in `H_C(a,M_new)` gives exactly the same expression.
The inverse first recovers `M=M_new+C^t E_new`, then
`E=E_new-CM`; `DC=0` gives `DE_new=DE`.

On the active carrier (4) becomes

```text
H_G(z,M)=z^t G z+M^t M+z^t G M = (z,M)^t B_G(z,M)/2,
B_G = [[2G,G],[G,2I]],
A_G^t B_G A_G=B_G,
4H_G(z,M)=(2z+M)^t G(2z+M)+M^t(4I-G)M.                   (5)
```

All five `G` are positive definite. For a positive definite `G`, equation
(5) says that `H_G` is positive definite exactly when `4I-G` is positive
definite, and positive semidefinite exactly when `4I-G` is positive
semidefinite. Sufficiency follows from the two nonnegative terms and their
common zero set. Necessity follows by taking `z=-M/2`; strict positivity
then requires `M^t(4I-G)M>0` for every nonzero real `M`.
The same criterion for the full raw energy follows from (4), by choosing
`E=-CM/2`. It concerns positivity over the whole real space, not only a
finite collection of integer test states.

| Cell | Eigenvalues of G | Energy classification |
| --- | --- | --- |
| G2 | `2` | positive definite |
| G3 | `3` | positive definite |
| G22 | `1,3` | positive definite |
| G23 | `(5-sqrt(5))/2,(5+sqrt(5))/2` | positive definite |
| G33 | `2,4` | positive semidefinite, not definite |

For G23 an entirely rational positivity certificate is also immediate:
`G23` has positive leading minor `2` and determinant `5`, while
`4I-G23=[[2,-1],[-1,1]]` has positive leading minor `2` and determinant
`1`. Thus no rounded comparison with the threshold `4` is used.

For G33 put `w=(1,1)` and `v=(w,-2w)`. Then `G33 w=4w`, and (5) gives
`H_G33(v)=0` despite `v != 0`. The entire zero set over the reals is the
line generated by `v`: vanishing in (5) forces `2z+M=0` and
`M in ker(4I-G33)=R w`. The canonical integer witness is the negative
of this active vector, `z=(-1,-1), M=(2,2)`, whose raw electric component
is `E=(-2,-1,-1,-1,-1)`. It has `DE=0`. It is precisely the existing
shared-triangle boundary witness, not a new resolution of it.

## 5. Minimal orders, including an explicit parabolic chain

On an eigendirection `Gw=mu w`, the two-dimensional invariant subspace
`(z,M)=(xw,yw)` has matrix

```text
B_mu = [[1,1],[-mu,1-mu]],
B_mu^2-(2-mu)B_mu+I=0.                                    (6)
```

This is an algebraic identity, obtained either by multiplication or from
its trace and determinant. The following deductions establish the
smallest positive powers equal to the identity.

* **G2 has order 4.** Equation (6) at `mu=2` gives `A2^2=-I`, hence
  `A2^4=I`. Neither `A2` nor `A2^2` is the identity. The order divides
  `4` and therefore is exactly `4`.
* **G3 has order 3.** Equation (6) gives `A3^2+A3+I=0`, so
  `A3^3=I`. Its nonzero upper-right entry excludes the identity;
  because `3` is prime, the order is exactly `3`.
* **G22 has order 6.** Its eigenvectors `(1,-1)` and `(1,1)` have
  eigenvalues `1` and `3`. The first block satisfies
  `B1^2=B1-I` and `B1^3=-I`, while the second has order `3` as above.
  Thus both blocks have sixth power identity. For `B1`, possible proper
  divisors `1,2,3` are excluded: `B1 != I`, `B1^2=B1-I != I`, and
  `B1^3=-I != I`. The full matrix consequently has exact order `6`.
  The rational eigenbasis is used only for this matrix identity; no
  unimodular decomposition of its integer lattice is assumed.
* **G23 has order 5.** By its characteristic polynomial and the
  Cayley-Hamilton theorem, `I+A23+A23^2+A23^3+A23^4=0`. Multiplication
  by `A23-I` gives `A23^5=I`. It is not the identity (its upper-right
  block is `I`); since `5` is prime, its order is exactly `5`. The
  conjugate canonical `A_f` has the same order, already established
  by the Canon's unimodular cyclic certificate.
* **G33 has infinite order.** The eigenvalue `mu=4` is the boundary
  block. There `N=B4+I=[[2,1],[-4,-2]]` is nonzero and `N^2=0`.
  To exhibit the parabolic part in the original four integer coordinates,
  set

  ```text
  w=(1,1), v=(w,-2w)=(1,1,-2,-2), u=(0,0,1,1).
  (A33+I)v=0, (A33+I)u=v != 0.
  ```

  The two vectors are independent, so their span is a genuine length-two
  Jordan chain. On it `A33=-I+N`, `N^2=0`, and the binomial identity gives
  for every integer `k>=0`

  ```text
  A33^k u=(-1)^k (u-k v).                                  (7)
  ```

  A positive even `k` cannot give `u`, because `kv != 0`. For odd `k`
  the equation would be `kv=2u`, impossible by their first two
  coordinates. Hence no positive power of `A33` is the identity.
  This is an all-time analytic witness, not inference from a repeated
  characteristic root or a bounded power search. It also shows why
  semidefinite energy does not bound this orbit: `H_G33(u)=2` is constant
  under (7), while `v` is its nonzero zero-energy drift direction.

All statements survive the signed orientation conjugacies in section 2.
The finite orders are the orders of the matrices on their whole declared
carriers, not a claim that every individual state has that least period.
In particular, the zero state is fixed in every case.

## 6. Scope of the comparison

The five-cell comparison is complete only for the frozen list in section
1 and its explicitly stated orientation equivalents. It does not enumerate
all two-face CW complexes, larger polygons, weighted incidences, multiple
shared edges, alternative update orders, or alternative energies. The
word `CENSUS` in the probe identifier does not enlarge this domain.

The order-five cell is one selected positive cell among these examples.
The positive order-four, order-three and order-six cells prohibit reading
this table as a uniqueness or physical selection of five. No field matrix
is derived from native U or J; no new layer lift, apparatus, occurrence
law, or existing H/O closure is asserted. Generic shear identities,
triangle order, canonical order-five dynamics, and the shared-triangle
zero mode remain inherited content, as detailed in `LINEAGE.md`.
