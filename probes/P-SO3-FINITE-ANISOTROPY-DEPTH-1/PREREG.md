# P-SO3-FINITE-ANISOTROPY-DEPTH-1

Status: PREREGISTERED / UNRUN at this file state.

Public claim issue: #615  
Target claim: `SO3-FINITE-ANISOTROPY-MAXIMUM`  
Action layer: `L1` only  
Owner: A. M. Thorn / current ChatGPT owner session  
Proposed status: `T` by exact proof; verifier is an audit.

## 1. Equation and claim

Let `G <= SO(3)` be finite. Let `H_l(R^3)` be the real vector space of
homogeneous harmonic polynomials of degree `l` on `R^3`. Define the harmonic
anisotropy depth

```text
a(G) := min { l >= 1 : H_l(R^3)^G != 0 }.
```

The frozen target is

```text
a(C_n) = 1                  n >= 1
a(D_n) = 2                  n >= 2
a(A_4) = 3
a(S_4) = 4
a(A_5) = 6
```

and therefore

```text
a(G) <= 6
```

for every finite `G <= SO(3)`, with equality if and only if `G` is conjugate
to the rotational icosahedral group `A_5`.

The same three-dimensional `A_5` representation has two order-five rotation
classes with exact traces

```text
(1 + sqrt(5))/2
(1 - sqrt(5))/2
```

whose difference is `sqrt(5)`. Hence their character field is
`Q(sqrt(5))`.

No Lorentz, J-selection, decoder, measure, continuum or physical necessity
claim is included.

## 2. Proof

The theorem status is proof-first. The computation below audits the finite
polyhedral arithmetic but is not the logical source of the universal
classification.

### 2.1 Complete finite-rotation classification

A finite subgroup of `SO(3)` acts on `S^2`.

If the group has a common fixed axis, it is a finite subgroup of the circle
group of rotations about that axis, hence cyclic.

Otherwise the quotient spherical orbifold has three branch orders
`2 <= a <= b <= c` with

```text
1/a + 1/b + 1/c > 1.
```

The integer solutions are exactly

```text
(2,2,n)  n >= 2
(2,3,3)
(2,3,4)
(2,3,5).
```

Indeed `a >= 3` is impossible, and with `a = 2`, either `b = 2`, or `b = 3`
and then `c < 6`. The orientation-preserving spherical triangle groups have
orders

```text
2n, 12, 24, 60
```

and are respectively the rotational dihedral groups `D_n`, tetrahedral
`A_4`, octahedral `S_4`, and icosahedral `A_5`. Together with the cyclic
case, these are all finite subgroups of `SO(3)` up to conjugacy.

This is the standard finite-rotation classification written in the exact
form consumed by this probe. The phrase "there are finitely many finite
subgroups" is explicitly forbidden. There are infinitely many `C_n` and
`D_n`; there are five classification types.

### 2.2 The cyclic and dihedral families

For `C_n`, the coordinate along the rotation axis is a nonzero invariant
harmonic linear form, so `a(C_n)=1`.

For `D_n`, `n >= 2`, there is no nonzero invariant linear form. For `n > 2`,
the principal rotation forces a fixed vector onto the main axis and an
equatorial half-turn reverses it. For `n=2`, the three perpendicular
half-turns have no common nonzero fixed vector.

The quadratic polynomial

```text
2 z^2 - x^2 - y^2
```

is invariant under every rotational `D_n` and has Laplacian

```text
4 - 2 - 2 = 0.
```

Thus `a(D_n)=2`.

### 2.3 Polyhedral harmonic multiplicities

For the irreducible degree-`l` harmonic representation of `SO(3)`, a rotation
through angle `theta` has character

```text
chi_l(theta) = 1 + 2 sum_(k=1)^l cos(k theta).
```

For a finite group,

```text
dim H_l(R^3)^G = (1/|G|) sum_(g in G) chi_l(g).
```

The exact rotation-angle class tables consumed are

```text
A_4:  1 identity, 3 rotations pi, 8 rotations 2pi/3
S_4:  1 identity, 9 rotations pi, 8 rotations 2pi/3, 6 rotations pi/2
A_5:  1 identity, 15 rotations pi, 20 rotations 2pi/3,
      12 rotations 2pi/5, 12 rotations 4pi/5.
```

The verifier performs this average exactly in `Q(sqrt(5))`.

### 2.4 Independent Molien audit

For a three-dimensional rotation by `theta`, with `c = 2 cos(theta)`,

```text
det(I - t R_theta) = (1-t)(1-c t+t^2).
```

The verifier independently averages the corresponding rational functions and
cross-multiplies exactly against

```text
M_A4(t) = (1+t^6)  / ((1-t^2)(1-t^3)(1-t^4))
M_S4(t) = (1+t^9)  / ((1-t^2)(1-t^4)(1-t^6))
M_A5(t) = (1+t^15) / ((1-t^2)(1-t^6)(1-t^10)).
```

No Klein formula is used as the construction route. It is the exact target of
an independently constructed class-angle average.

The harmonic decomposition

```text
P_l = H_l direct_sum r^2 P_(l-2)
```

implies

```text
dim H_l^G = dim P_l^G - dim P_(l-2)^G.
```

The verifier compares this route with the direct character route through
degree 16.

## 3. Code

Accepted verifier:

```text
probes/P-SO3-FINITE-ANISOTROPY-DEPTH-1/verify.py
sha256 f9cb216c006aa98a83ff99619955d8221d53b00484eabbffafbcba651e39cd55
bytes  9329
```

The verifier uses only the Python standard library, `Fraction`, and a
two-coordinate exact implementation of `Q(sqrt(5))`. It uses no floating
point, NumPy, SymPy, PSLQ, network access, external dataset, paper table, or
TWIST-J internal artifact.

Before the prospective pin, only syntax compilation of this accepted file is
permitted as a verifier action. A formal execution is forbidden until both
this preregistration and the accepted verifier are committed and pushed.

## 4. Carrier and data

Carrier:

```text
H_l(R^3), l >= 0
```

with the standard `SO(3)` action by substitution.

Exact finite class data are the conjugacy-angle multiplicities displayed in
section 2.3. The only quadratic extension is represented as
`a + b sqrt(5)` with `a,b in Q`.

No measured data are consumed.

## 5. Systematics and prior exposure

### 5.1 Prior exposure

Before the public pin, the owner supplied:

```text
candidate depth table: 1,2,3,4,6
candidate A5 Molien coefficients through degree 16:
[1,0,1,0,1,0,2,0,2,0,3,0,4,0,4,1,5]
a published density construction involving A5 and a golden boost
```

The builder also used non-formal scratch arithmetic while preparing the
accepted exact verifier. These exposed values are not evidence and earn no
status. The accepted verifier itself was not formally executed before the
prospective pin.

The Lorentz-density construction is excluded from every gate. In particular,
the probe must not conclude that density selects a golden rapidity.

### 5.2 Semantic predecessor

`P-A3-FCC-POINT-GROUP-1` is an ABANDONED public identifier. Its formal gate
never ran. Its files are not evidence and this probe does not resume, repair,
rename, or inherit it.

### 5.3 Classification boundary

The universal quantifier over all finite `G <= SO(3)` is owned by the proof in
section 2.1, not by finite computation. The verifier audits the three
polyhedral cases and the exact golden trace field. The infinite cyclic and
dihedral families are proved symbolically in section 2.2.

### 5.4 Meaning of anisotropy

"Anisotropy depth" in this probe is exactly the first positive degree carrying
a `G`-invariant harmonic scalar. It does not mean a dynamical error term,
dispersion relation, regulator artifact, Lorentz violation, or measured
anisotropy.

## 6. Frozen gates and thresholds

All gates are boolean exact-equality gates. Any single failure fires the probe.

```text
G01  direct character average gives a(A4)=3
G02  direct character average gives a(S4)=4
G03  A5 direct harmonic multiplicities vanish in degrees 1 through 5
G04  A5 direct harmonic multiplicity in degree 6 is exactly 1
G05  class-angle Molien average equals the frozen A4 rational function
G06  class-angle Molien average equals the frozen S4 rational function
G07  class-angle Molien average equals the frozen A5 rational function
G08  direct-character and Molien harmonic multiplicities agree through degree 16
G09  A5 Molien coefficients degree 0 through 16 equal the exposed candidate row
G10  the two A5 order-five traces equal phi and 1-phi exactly
G11  their difference is sqrt(5), so the character field is Q(sqrt(5))
```

No threshold, tolerance, search box, numerical precision, or post-run choice
exists.

## 7. Falsifier

The theorem fires if any of the following is exhibited:

```text
F1  finite G <= SO(3) with a(G) > 6
F2  finite G <= SO(3), not conjugate to A5, with a(G) = 6
F3  nonzero A5-invariant harmonic polynomial in degree 1,2,3,4 or 5
F4  H_6(R^3)^A5 = 0
F5  the order-five trace pair fails to generate Q(sqrt(5))
```

Any failed verifier gate also fires the audited finite arithmetic.

## 8. Action layer and scope firewall

Action layer: `L1`.

No lift to L2 through L6 occurs. No cross-layer gate is owned.

Excluded conclusions:

```text
Lorentz invariance or Lorentz necessity
uniqueness of a boost or rapidity
uniqueness or derivation of J
physical selection of p=5
decoder totality or uniqueness
continuum or coarse-graining claims
measure or probability claims
claim that A5 removes anisotropy
claim that degree-6 suppression is physically sufficient
claim that another discrete universe must resonate
```

A later physical bridge, if attempted, must be a separately named public
object with its own scope and falsifier.
