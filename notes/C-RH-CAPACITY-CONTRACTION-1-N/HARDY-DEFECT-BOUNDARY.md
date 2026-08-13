# HARDY COMPRESSION: EXACT BOUNDARY

```text
STATUS: candidate-T operator algebra; NON-CANONICAL
ISSUE:  #357
```

## 1. Why a unitary multiplier does not prove positivity

Let `P` be an orthogonal Hardy projection on a boundary `L2` space and set

```text
H=2P-I.
```

Let `u` be multiplication by a unimodular scattering function. Then `u` is
unitary on the boundary space and

```text
u* [H,u]
 = u*Hu-H
 = 2(u*Pu-P).
```

Thus the local trace formula written with the quantized differential is a
**difference of projections**, not a single defect norm. In the orientation
used by Connes--Consani one has, up to their stated sign convention,

```text
W(f) = -(1/2) Tr(M_f u*[H,u])
     = Tr(M_f [P-u*Pu]).
```

Therefore the mere fact that the Toeplitz/Hardy compression of a unitary
multiplier is a contraction cannot prove the sign of the Weil form. The target
contains the relative position of two projections.

## 2. Innerness is the missing order statement

For an inner analytic function `theta`, multiplication maps `H2` isometrically
into itself,

```text
M_theta H2 subset H2.
```

Consequently the associated range projection is ordered:

```text
M_theta P M_theta* <= P,
P-M_theta P M_theta* >=0.
```

For the opposite orientation the same statement uses the conjugate/co-inner
function. Thus exact innerness supplies the projection inclusion which turns a
signed projection difference into a positive operator.

A general unimodular boundary function does **not** supply this inclusion.

## 3. Semilocal comparison

Connes--Consani prove that for a finite set of places containing infinity, the
product

```text
u_F = product_(v in F) rho_v
```

is quasi-inner: the off-diagonal Hardy block is compact. They also prove that
the corresponding semilocal Sonin kernels form an inductive system when the
finite set of places grows.

Quasi-inner is weaker than the exact inner/co-inner inclusion needed above.
Therefore their theorem supplies the correct nested carrier category but does
not by itself close the contraction/positivity gate.

## 4. Sharpened construction target

The G6 search can now be split into an exact comparison problem:

```text
A. identify the #357 signed feature form with the appropriate semilocal
   projection-difference / quantized-differential form;

B. identify the graph map R_+ -> R_- with a subspace-angle / projection
   comparison in the semilocal Hardy/Sonin space;

C. prove the required projection order or contractive graph inclusion by a
   structural theorem stronger than quasi-innerness, without assuming Weil
   positivity.
```

Failure of A is a clean mismatch of carriers. Success of A+B but failure of C
localizes the RH wall to an exact subspace-inclusion problem.

## 5. Falsified shortcut

```text
unimodular scattering phase
 -> Toeplitz compression is contractive
 -> Weil form positive
```

is invalid. The middle statement is automatic, but the Weil form is a signed
relative-projection quantity. Any future argument using this shortcut is
circular or incomplete.
