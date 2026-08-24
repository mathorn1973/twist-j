# HARDY COMPRESSION: EXACT BOUNDARY

```text
STATUS: candidate-T bounded-operator algebra; trace application conditional
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
**difference of projections**, not a single defect norm. In one relevant
orientation one writes, up to the source's sign convention and only when the
displayed product is trace class,

```text
W(f) = -(1/2) Tr(M_f u*[H,u])
     = Tr(M_f [P-u*Pu]).
```

Therefore the mere fact that the Toeplitz/Hardy compression of a unitary
multiplier is a contraction cannot prove the sign of the Weil form. The target
contains the relative position of two projections.

## 2. The orientation of the order must be frozen

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

Conjugating this inequality by `M_theta*` gives

```text
P <= M_theta* P M_theta.
```

Thus ordinary innerness gives the **opposite** sign for `P-u*Pu`. In the
displayed trace convention, the desired order is

```text
u*Pu <= P,
```

which corresponds to the co-inner orientation `u*H2 subset H2`. A future gate
must freeze the boundary half-plane, projection, multiplier orientation,
trace-class domain, and sign before importing an inner/co-inner theorem.

A general unimodular boundary function does **not** supply this inclusion.

## 3. Semilocal comparison

Connes--Consani prove that for a finite set of places containing infinity, the
product

```text
u_F = product_(v in F) rho_v
```

is quasi-inner: the off-diagonal Hardy block is compact. They also prove that
the corresponding semilocal kernels form an inductive system when the finite
set of places grows; the comparison maps are multipliers by the added local
denominators, not plain inclusions.

Quasi-inner is weaker than the exact inner/co-inner inclusion needed above.
Therefore their theorem supplies a candidate comparison category but does not
by itself close the contraction/positivity gate or identify these kernels with
the #357 feature carriers.

## 4. Sharpened construction target

After the frozen G3-G5 order permits G6, its search can be split into an exact
comparison problem:

```text
A. identify the #357 signed feature form with the appropriate semilocal
   projection-difference / quantized-differential form;

B. identify the graph map R_+ -> R_- with a subspace-angle / projection
   comparison in the semilocal Hardy/Sonin space;

C. freeze the trace-class and orientation hypotheses, then prove the required
   projection order or contractive graph inclusion by a structural theorem
   stronger than quasi-innerness, without assuming Weil positivity.
```

Failure of A is a clean mismatch of carriers. Success of A+B would still leave
C as a precise open subspace-inclusion problem; no equivalence with RH is
claimed before all typing and density implications are proved.

## 5. Falsified shortcut

```text
unimodular scattering phase
 -> Toeplitz compression is contractive
 -> Weil form positive
```

is invalid. The middle statement is automatic, but the Weil form is a signed
relative-projection quantity. Any future argument using this shortcut is
circular or incomplete.
