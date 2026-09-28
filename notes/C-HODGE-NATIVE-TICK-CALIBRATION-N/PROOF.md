# Ideal METRO tick calibration and rounded-event boundary

Status: PUBLIC NON-CANONICAL.
Owner: #1257. Author: A. M. Thorn <thorn@twistj.com>.
Prospective pin: a98e1e17fc7fd52cbb414bd4a35d6fc0ea7c9aec.

The exact algebra below is conditional on the selected Hodge event frame and on the candidate-D identification of one native update with one ideal event-grid time step. It does not create an SI clock.

## 1. Frozen frame and tick

In the correctly typed event frame,

    g_frame=diag(a1,a2,a3,-ct),

where

    a1=2sqrt5/5,
    a2=6sqrt5/5,
    a3=3sqrt5/2,
    ct=(2+sqrt5)/8.                                  (1)

The selected ideal event grid at integer resolution h>=3 is

    y_h(m,z)=h^-1(m t+sum_i z_i s_i).                 (2)

A same-z ideal time edge is t/h, so its inherited squared interval is

    g(t/h,t/h)=-ct/h^2.                               (3)

METRO-TICK [T] gives the dimensionless proper-time tick

    T=2pi/5.                                          (4)

TIME-CUT-READING [D] permits, but does not uniquely force, reading one native update as one such tick.

## 2. Selected ideal calibration

As a candidate-D dictionary, identify one native update with one ideal step

    n -> n+1  corresponding to  m -> m+1

at fixed z, and require its proper time after a positive global conformal rescaling lambda_h g to equal T.

Equations (3)-(4) give

    lambda_h ct/h^2=T^2,

hence uniquely

    lambda_h=T^2 h^2/ct.                              (5)

Uniqueness here is only inside the frozen class of positive global conformal rescalings of the selected ideal Hodge metric.

## 3. Resolution cancels on integer label coordinates

For an integer label increment

    (dm,dz1,dz2,dz3),

the ideal geometric displacement is h^-1(dm t+sum dz_i s_i). Pulling lambda_h g back to label coordinates and using (5) gives

    g_tick =
      T^2 diag(a1/ct,a2/ct,a3/ct,-1).                 (6)

The resolution h cancels exactly.

The three exact ratios are

    a1/ct=16(5-2sqrt5)/5,                             (7)
    a2/ct=48(5-2sqrt5)/5,                             (8)
    a3/ct=12(5-2sqrt5).                               (9)

They are positive because sqrt5<5/2. The last coefficient in (6) is negative, so the signature is (3,1).

Equivalently, because the selected scalar stencil satisfies alpha_i=ct/a_i,

    g_tick =
      T^2 diag(1/alpha1,1/alpha2,1/alpha3,-1).        (10)

With T=2pi/5 the time coefficient is exactly -4pi^2/25. No SI unit has entered.

Equation (6) is the useful closure: once the Hodge frame and the ideal n=m tick dictionary are selected, the dimensionless metric on integer labels is independent of the arbitrary event resolution h.

Conversely METRO-TICK does not select h. For every h>=3, equation (5) supplies a different conformal factor producing the same label metric (6). Resolution and conformal factor are underdetermined separately.

## 4. Actual rounded events are not the ideal grid

The actual event construction rounds in the ambient integer carrier and then projects. The inherited theorem gives, uniformly in m,z,

    ||e_h(m,z)-y_h(m,z)||_* <= R0/h^4,                (11)

where

    R0=10-9sqrt5/5.

For a same-z actual edge put

    Delta=e_h(m+1,z)-e_h(m,z)
         =t/h+eta.

The two endpoint errors imply

    ||eta||_* <= epsilon_h=2R0/h^4.                   (12)

By the definition of the inherited star norm, decompose

    eta=tau t+s,

with s spatial and

    |tau|<=epsilon_h,
    g(s,s)<=ct epsilon_h^2.                           (13)

The frame is orthogonal, so

    g(Delta,Delta)
      =-ct(1/h+tau)^2+g(s,s).

Subtracting the ideal value -ct/h^2 and using (13),

    |g(Delta,Delta)+ct/h^2|
      <=ct(2 epsilon_h/h+2 epsilon_h^2)
      =ct(4R0/h^5+8R0^2/h^8).                        (14)

This is uniform over every same-site edge of the selected actual event mesh.

Multiplying by the ideal calibration factor (5),

    |lambda_h g(Delta,Delta)+T^2|
      <=T^2(4R0/h^3+8R0^2/h^6).                      (15)

Thus the CALIBRATED SQUARED intervals of actual rounded same-site edges converge uniformly to -T^2 with error O(h^-3).

This does not assert that every finite-h actual edge has equal proper time.

## 5. Exact finite-resolution obstruction

At h=3, the exact implementation gives for the edge from (m,z)=(0,(0,0,0))

    I0=-398/6561.                                     (16)

For the edge from (m,z)=(1,(1,0,0))

    I1=(-1861+sqrt5)/32805.                           (17)

These values are distinct. If one positive global conformal factor lambda made both actual edges have the same prescribed nonzero squared proper time -T^2, then lambda I0=lambda I1 and hence I0=I1, contradiction.

Therefore the actual h=3 rounded event mesh cannot be made exactly equitick by one global conformal scale.

This is a finite-resolution witness only. No all-h impossibility theorem is claimed.

## 6. Three clocks remain different objects

This construction contains three integer parameters that must not be conflated:

1. n, the native update counter in Omega;
2. m, the geometric event-time label in the selected Hodge mesh;
3. N, the append/serialization counter in C-OMEGA-GENERATIVE-GEOMETRY-N2.

The candidate-D clock dictionary identifies n=m for the ideal clock seam. It does not identify N with either. Generation order is not event time.

TIME-CUT-READING remains a selected dictionary and is not promoted to a unique physical clock theorem.

## 7. Status boundary

The selected ideal flat spacetime now has an exact dimensionless METRO-tick calibration. Its pulled-back integer-label metric is (6), independent of h.

Actual integer-rounded events approximate that calibrated timing uniformly by (15), but exact finite-resolution equitick behavior is already false at h=3.

Nothing here closes METRO-EDGE-SCALE, supplies SI units, derives physical clock realization, changes the microscopic spacelike-support result, or establishes curvature, photon-cone equality, occurrence, Galois physical selection or an L6 measure.
