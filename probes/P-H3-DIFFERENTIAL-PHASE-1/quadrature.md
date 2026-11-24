# Exact phase encoding and signed-reference controls

Write `pi=1-rho`, `J=1+rho`, and
`phi=-(rho+rho^-1)`. Use native C then B, starting at matching
color zero. At a legal B contact the material half-gap d selects
a branch with the radiation half-gap f through their Hermitian
norms. Holding d and either center fixed or varying the centers
without changing parity legality does not impart sensitivity
to the sign of f. In particular replacing an admitted f by -f
preserves the branch and the entire material output. This can be
different from flipping only one incident contribution before C:
C can combine it with a fixed reference before B measures its norm.

## Global affine sign and phase symmetry

For any common constant c in the ring and common integral unit eta
with `eta conjugate(eta)=1`, transform every CLK and every CORR word
by `w -> eta w+c` and leave all matter words fixed. At C a radiation
difference is multiplied by eta, so divisibility by two is preserved
in both directions, and the admitted pair rule commutes with the
transform because its coefficients sum to one. At B the radiation
difference gains eta, its center gains the same affine transform, and
the Hermitian norms in both branch guards are unchanged. The selected
center/difference map commutes with the transform. Induction gives
identical material trajectories and B tags for every cut, for the
entire admissible state class. It gives a negative result for a
globally sign-flipped signal with the radiation reference also
flipped, including affine reflection about a constant background.
A spatially varying offset or a sign flip only on one source is
outside this symmetry. The transformed state need not have the same
ledger as the original. The checker compares both separately and
checks each complete inverse.

## A local reference makes the signed source observable with zero scalar work

Use the 8 by 8 torus. At (0,0) give matter zero center and half-gap
`d=pi`. Launch radiation there with zero center and half-gap
`2 s u`, where `s=+1,-1` and `u=pi(1+pi)`. Give the vertical
neighbor (0,1) the same fixed CLK bias `-4 J pi` in both arms and
zero CORR. Other words vanish except the undriven material reference
at (4,0), with initial half-gap pi. The odd matter words refuse a
vacuum match. Both initial states have the same complete M,U,H,Q
because the changed source has zero center and its two words'
norms are sign-blind. In the first C, both relevant radiation
contacts are even and admitted. Using `A=(1+rho)/2` and
`B=(1-rho)/2`, their combined target half-gap and center are

    f = s J u - pi J pi
    center = -pi J pi.

Consequently `f_+=J pi` and `f_-=-J pi(1+2pi)`. The plus arm
gives B1. In the other arm the multiplicative norm
`h(1+2pi)=13+6phi` makes its norm `33-phi`; neither active
threshold `h(J pi)=3-phi` nor `h(J^-1 pi)=3+4phi` is met.
The reference stays fixed. After B the target/reference word ratios
are J and 1 and the phase-only coordinate `R/conjugate(R)` is
rho and 1. In both arms the material scalar Q at the target is 10
before and after B. The plus arm changes the full local Hermitian
material account by `2-4phi`, which the radiation account exactly
compensates. The minus arm has zero change in both. This isolates a
material phase contrast at zero scalar work. It leaves a nonzero
Hermitian work difference.

## Exact equal-H phase encoding and native material readout

Separately use zero radiation and four matter sites at consecutive rows
0, 1, 2, 3 in column 0 with zero centers and half-gaps
`(2s,2,2,2)`, s=+1 or -1. These preparations share the complete
ledger and the same per-site Hermitian material weights. At the first
C, y=1 is paired with y=0. Its word stays 2 in the plus arm and becomes
`2rho` in the minus arm. The row-2 reference stays 2 in both.
The post-B ratios are respectively 1 and rho, with every per-site
Hermitian weight unchanged by the encoding in both arms. B is
inactive throughout. There is no radiation.

At the second C, the changed matching joins rows 1 and 2. The plus
arm stays `(2,2)`; the minus arm gives
`(1+rho^2,1+2rho-rho^2)`. Its exact site material Q weights are
`(6,26)`, compared with `(16,16)` in the plus arm. The pair has
the same complete material Q and Hermitian budget before and after
readout. This is a phase-sensitive native conversion at a different
cut from encoding. It changes some local readout weights. The
encoding is a cold material circuit, not a zero-H optical B
actuation.

## Scoring

The code checks the listed full native cuts and exact comparisons,
and runs six native steps on each global symmetry control, with
whole accounts and inverse checks. Any wrong ratio, branch, work
quantity, readout weight or affine equivariance relation is reported
as a scientific failure. An ill-typed native preparation or failed
native complete inverse or ledger is an integrity failure. The
controls do not assign physical work, charge, optical polarization,
clock calibration, Born sampling or a physical meaning to these
native phase coordinates.
