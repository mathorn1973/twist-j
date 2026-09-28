# RESULT - C-HODGE-WINDOW-FIELD-OPERATOR-N

Status: PUBLIC NON-CANONICAL.
Ceiling: candidate-T theorem package, candidate-D selected field dictionary,
candidate-C exact audit/reproduction. Canon v92 unchanged.

## Main positive result

A scalar field operator using only values at actual windowed events exists.

The inherited six source directions cannot be weighted independently to
produce the Lorentz principal tensor. The complete diagonal class is ZERO.

The source wedge form instead gives the exact identity

    C beta^-1 C^T = g^-1,

so the forced mixed continuum operator is

    Box_g=2(d_0 d_5-d_1 d_4+d_2 d_3).

The literal unit source stencil is not total on M. The total replacement uses
M_(n^4), physical stencil scale 1/n and the already frozen event rounding
map. Every requested corner is reprojected to an actual event with position
error <=R/n^4.

For C^4 fields,

    Box_n f = Box_g f + O(n^-2)

uniformly on compact event sets.

For an event plane wave exp(i xi x),

    |Box_n psi/psi + g^-1(xi,xi)|
       <= [2 A_xi^4+6R X_xi]/n^2.

## Local photon-mode bridge

With the independently frozen coframe and the actual principal D3 roots,
each lifted D3 scalar mode is sampled directly on M_(n^4). On every bounded
lifted momentum set its event-field residual obeys

    sup_x |Box_n psi_(n,k)(x)| = O(n^-2).

Thus the selected event field and the selected D3 characteristic now share
the same Hodge null cone through an explicit local scalar-mode construction,
not merely through a comparison of two quadratic formulas.

## Exact negative boundaries

1. A fixed unit source stencil is not total on the selected event set.
2. The deterministic rounding-neighbor rule is not exactly C5-equivariant.
3. The same rule is not exactly J-equivariant.

The finite-scale symmetry failures do not change exact covariance of the
continuum principal operator. No claim is made that Box_n violates every
weaker, averaged or differently rounded covariance notion.

## What is still missing

This does not yet give a finite-n propagation theorem. Self-adjointness,
Cauchy well-posedness, positive energy, a retarded Green function, exact
finite-scale covariance, global D3 action/measure transfer, vector gauge
structure, polarization and the physical massless phase remain open.

The operator, scaling path and coframe are explicit selected dictionary data.
They are not derived from native Omega,U or from experiment.
