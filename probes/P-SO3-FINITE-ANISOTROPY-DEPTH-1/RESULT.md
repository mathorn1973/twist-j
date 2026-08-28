# P-SO3-FINITE-ANISOTROPY-DEPTH-1 result

Status: **candidate-T / L1 / SO3-FINITE-ANISOTROPY-MAXIMUM CONFIRMED / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable public verifier exited zero, wrote empty stderr, and produced the exact committed `EXPECTED.txt` bytes. All 11 frozen gates passed. No scientific falsifier fired and no threshold moved.

## Result

For every finite subgroup `G <= SO(3)`, define

```text
a(G) = min { l >= 1 : H_l(R^3)^G != 0 }.
```

The exact depth table is

```text
C_n    1       n >= 1
D_n    2       n >= 2
A_4    3
S_4    4
A_5    6
```

Hence

```text
a(G) <= 6
```

for every finite `G <= SO(3)`, and equality holds if and only if `G` is conjugate to the rotational icosahedral group `A_5`.

The universal quantifier is carried by the proof in `PREREG.md`: the complete finite-rotation classification has five types, with the cyclic and dihedral types remaining infinite families. The computation is not a finite substitute for that classification.

## Polyhedral exact audit

Direct character averaging gives

```text
A_4: first positive invariant harmonic degree = 3
S_4: first positive invariant harmonic degree = 4
A_5: invariant harmonic multiplicities at degrees 1..5 = 0,0,0,0,0
A_5: invariant harmonic multiplicity at degree 6 = 1
```

An independent Molien construction from conjugacy-class rotation angles cross-multiplies exactly to

```text
M_A4(t) = (1+t^6)  / ((1-t^2)(1-t^3)(1-t^4))
M_S4(t) = (1+t^9)  / ((1-t^2)(1-t^4)(1-t^6))
M_A5(t) = (1+t^15) / ((1-t^2)(1-t^6)(1-t^10)).
```

The character and Molien routes agree through degree 16 after removing the radial `r^2` factor. The `A_5` Molien coefficient row is exactly

```text
[1,0,1,0,1,0,2,0,2,0,3,0,4,0,4,1,5].
```

## Golden equality branch

The two order-five rotation classes of the winning three-dimensional `A_5` representation have exact traces

```text
phi     = (1 + sqrt(5))/2,
1 - phi = (1 - sqrt(5))/2.
```

Their difference is `sqrt(5)`. Therefore the character field of the equality branch is exactly `Q(sqrt(5))`.

This is the theorem-grade sense in which the unique maximal-depth finite rotation type is golden. It is a representation-theoretic statement, not a physical selector.

## What failed from the earlier interpretation

The Lorentz-density construction is not consumed by this probe. In particular, the following route is rejected as an inference:

```text
density of <A5,B_J>  =>  uniqueness of the golden boost.
```

Density may protect a chosen construction, but this probe establishes no classification of boost choices. The selection theorem here is instead the complete finite-rotation harmonic-depth classification.

## Status ceiling

The proof in `PREREG.md` establishes the universal result independently of machine computation. The exact verifier audits the polyhedral arithmetic and the golden trace field. This supports a later public row

```text
SO3-FINITE-ANISOTROPY-MAXIMUM [T], L1
```

after required pull-request integrity checks and a separate Canon fold.

Until that fold, Public Canon v67 is unchanged.

## Scope firewall

No Lorentz invariance, Lorentz necessity, boost uniqueness, J uniqueness, p=5 physical selection, decoder theorem, continuum theorem, measure, probability, or SI statement is assumed or concluded.

The theorem does not say that `A_5` removes anisotropy. It says that among finite rotation groups it uniquely postpones the first allowed invariant harmonic scalar to degree six.

No claim is made that a degree-six leading anisotropy is dynamically small, physically sufficient, or the source of observed Lorentz invariance. Any such bridge requires a separate named public object.

## Pin and local run

```text
public claim issue:       #615
preregistration pin:      4448ad11a8026740962d06585c06b8e7d11ad6b2
verifier sha256:          f9cb216c006aa98a83ff99619955d8221d53b00484eabbffafbcba651e39cd55
local architecture:       x86_64
local exit:               0
local stderr bytes:       0
local stdout bytes:       470
local stdout sha256:      c5f29046913ca024427be3fc1213fc15af672ca2e51917a260788e792606ccbc
```

The local run is one architecture lane only. The proposed theorem status is proof-first; the pull-request workflow remains the required repository integrity and independent architecture audit.
