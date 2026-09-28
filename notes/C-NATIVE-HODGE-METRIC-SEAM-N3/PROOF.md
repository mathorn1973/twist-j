# Correctly typed native-cover / Hodge metric boundary

Status: PUBLIC NON-CANONICAL.
Owner: #1255. Author: A. M. Thorn <thorn@twistj.com>.
Prospective pin: d4847ca43c6b94e1095053cb2e4ad54505601e93.

This note supersedes C-NATIVE-HODGE-METRIC-SEAM-N for the actual C-OMEGA-GENERATIVE-GEOMETRY-N2 pipeline.

## 1. Coordinate type

The inherited Hodge carrier E+ is first described in a marked four-coordinate basis whose spatial 3x3 Gram is (sqrt5/10)(2I+11^T). C-HODGE-EVENT-CAUCHY-N then changes to the orthogonal frame

    t =(0,0,0,1),
    s1=(1,-1,0,0),
    s2=(1,1,-2,0),
    s3=(1,1,1,0).

C-OMEGA-GENERATIVE-GEOMETRY-N2 passes its integer site z=(z1,z2,z3) to the event constructor as the coefficient triple of s1,s2,s3:

    y_h(m,z)=h^-1(m t+z1 s1+z2 s2+z3 s3).             (1)

Therefore the Hodge spatial Gram on N2 site coordinates is

    Q_frame=diag(a1,a2,a3),                            (2)

with

    a1=2sqrt5/5,
    a2=6sqrt5/5,
    a3=3sqrt5/2.                                      (3)

This is the decisive type correction.

## 2. Cover directions in the actual N2 coefficient space

The N2 cube-shell coordinates retain the cover differences

    x=z1-z3,
    y=z2-z3.

The zero-sum coefficient representatives of the three positive cover directions are

    p10=( 2,-1,-1)/3,
    p01=(-1, 2,-1)/3,
    p11=( 1, 1,-2)/3.                                 (4)

Their negatives give the other three directions. Using (2)-(3),

    Q_frame(p10)=(4a1+a2+a3)/9=43sqrt5/90,            (5)
    Q_frame(p01)=(a1+4a2+a3)/9=67sqrt5/90,            (6)
    Q_frame(p11)=(a1+a2+4a3)/9=38sqrt5/45
                                      =76sqrt5/90.     (7)

The three values 43, 67 and 76 are pairwise distinct. Thus the six abstract cover directions split into three opposite pairs of different Hodge lengths. The regular-hexagon symmetry of the selected cover is not an isometry symmetry of the typed Hodge target.

## 3. Tagged diagonal

The N2 tagged increment at fixed cover coordinate is

    d=(1,1,1).

Its exact Hodge square is

    Q_frame(d)=a1+a2+a3=31sqrt5/10.                   (8)

No common scalar normalization can equalize (5)-(7), because scalar multiplication preserves their ratios.

## 4. What remained correct in N1

N1 applied the original first-three-coordinate block

    Q_orig=(sqrt5/10)(2I+11^T)

directly to the cube coefficient triples. In that different coordinate identification, the vectors in (4) have equal square 2sqrt5/15 and d has square 3sqrt5/2, hence

    (3sqrt5/2)/(2sqrt5/15)=45/4.                      (9)

Equation (9) is mathematically correct for that hypothetical mapping. It is not the N2 seam because N2 uses (1). Therefore the N1 statements that rho=45/4 is the current N2/Hodge seam and that it fixes the N2 scale-free flat metric are superseded.

## 5. Correctly typed selected flat frame

For the actual N2 event labels the inherited selected flat Lorentz form is

    g_frame =
      diag(2sqrt5/5,
           6sqrt5/5,
           3sqrt5/2,
          -(2+sqrt5)/8).                              (10)

Its signature is (3,1). Equation (10) is inherited Hodge data expressed in the coordinates actually consumed by the event and generative-geometry code. It is not a new native derivation.

## 6. Corrected selection debt

The selected native commutator cover has a regular six-step abstract word metric. The N2 Hodge target has the anisotropic quadratic metric (2). The current bridge preserves combinatorial difference labels, not cover metric lengths.

Therefore a future claim that native commutator geometry derives the Hodge metric must supply an independently justified metric-sensitive map or law explaining the anisotropic image. It is invalid to impose the abstract cover permutation symmetry as a target isometry and then infer the Hodge metric, because the actual typed target violates that premise by (5)-(7).

A different linear or nonlinear metric-sensitive embedding might exist. It is not classified here and would need its own scoped construction.

## 7. Scope

This correction leaves intact the N2 append-only exhaustive geometry, its exact Hodge-frame metric and cubic large-scale growth, dependency-closed scalar field prefixes, the native event-address bridge, and the earlier microscopic spacelike one-hop counterexample.

No time calibration, METRO-TICK bridge, SI scale, photon cone, Galois physical selection, occurrence, L6 measure or curvature statement follows.
