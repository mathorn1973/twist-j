# Result: ideal tick calibration and finite rounded-event boundary

Status: PUBLIC NON-CANONICAL.
Owner: #1257. Author: A. M. Thorn <thorn@twistj.com>.
Ceiling: candidate-T conditional mathematics, candidate-D selected ideal clock seam, candidate-C same-code audit.

## Exact selected ideal result

With T=2pi/5 from METRO-TICK and the correctly typed Hodge frame, select one native update to equal one IDEAL event-grid step m->m+1.

For resolution h>=3 the unique positive global conformal factor in this class is

    lambda_h=T^2 h^2/ct,
    ct=(2+sqrt5)/8.

After pulling the calibrated metric back to integer event labels, h cancels exactly:

    g_tick =
      T^2 diag(
        16(5-2sqrt5)/5,
        48(5-2sqrt5)/5,
        12(5-2sqrt5),
        -1).

It has signature (3,1).

Thus the selected ideal dimensionless label metric is independent of event resolution. METRO-TICK does not select h because every h can be compensated by its corresponding lambda_h.

## Rounded actual events

For every actual same-site rounded edge,

    |lambda_h g(Delta,Delta)+T^2|
      <=T^2(4R0/h^3+8R0^2/h^6),

with R0=10-9sqrt5/5.

Therefore squared tick intervals converge uniformly to -T^2 as h grows.

They are not exactly equal at finite resolution in general. At h=3 two exact timelike edges have intervals

    -398/6561

and

    (-1861+sqrt5)/32805,

which are unequal. No single positive global scale can make both equal to one prescribed nonzero squared tick.

This is an exact h=3 obstruction, not an all-h no-go.

## Clock boundary

The candidate-D seam identifies native counter n with ideal event index m only. The N2 generative archive counter N remains a different object.

No SI scale, METRO-EDGE-SCALE closure, unique physical clock, curvature, photon-cone equality, occurrence, Galois physical selection or L6 measure is supplied.

## Exact audit

The unchanged prospective pin a98e1e17fc7fd52cbb414bd4a35d6fc0ea7c9aec passed on arm64 and x86_64 with identical 485-byte stdout, SHA256 82346022a7ef46fdb008a1a215a41c0cf67cd5f9f61fc1a55d0cc8ed70ac163b, exit 0 and empty stderr.

Universal interval and calibration statements rest on PROOF.md. Same-code execution is reproduction, not independent-agent confirmation.
