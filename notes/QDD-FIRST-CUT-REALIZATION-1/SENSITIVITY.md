# From transfer calibration to an explicit residual allowance

NON-CANONICAL / EXACT DESIGN DERIVATION / NO MEASURED ERROR BUDGET.
This supplements the proposed first-cut test. Its exploratory calculation
was run before any formal preregistration; it is not a new formal probe.

Let the source coordinates be z, the input-energy metric M=G/2, and
q=z*Mz. Under the declared optical normalization, q is input pulse energy
divided by E_star. The ideal signed output rows are b_j=-v_j/4860, with
j=0 the origin and j=1,...,7 the ordered calibration ports. A normalized
four-mode source coordinate s=M^(1/2)z has squared norm q; the physical
transfer target in these coordinates is C_j=b_j M^(-1/2).

This is a coordinate convention to be independently realized and calibrated.
It is not an identification of arbitrary optical channels with native heads.
All source coordinates and energies are typed by the preceding test design.

## 1. A sufficient bound supplied by independently measured transfer errors

Suppose independent apparatus calibration establishes the row-norm bounds

    ||C_actual,j-C_j||_2 <= eta_j,
    ||s||^2 <= q_max

on the declared operating domain. For complex amplitudes, the norm and
inner products are Hermitian. Source leakage outside these four prepared
modes, nonlinearities, uncontrolled incoming light and detector processing
are not contained in this assumption; each must be excluded or separately
bounded before applying it.

Write alpha_j=||C_j||_2. Cauchy-Schwarz gives

    |C_j s| <= alpha_j sqrt(q_max),
    |(C_actual,j-C_j)s| <= eta_j sqrt(q_max).

Expanding the squared amplitude therefore gives the rigorous sufficient bound

    |D_actual,j-D_ideal,j|
      <= q_max (2 alpha_j eta_j + eta_j^2).

This is a bound for the actual transfer on a common prepared input, before
energy-readout errors. It neither assumes independent random errors nor
assigns a probability to a deterministic interval.

For the fixed omitted-origin residual and deposit coefficients d_j in the
quadratic-calibration proof, define w_0=1 and w_j=|d_j|. Then

    S_transfer <= q_max sum_(j=0)^7 w_j(2 alpha_j eta_j+eta_j^2).

The seventh calibration coefficient vanishes, so that channel contributes
zero to this particular residual even though it is needed for the universal
quadratic-calibration objective. This sufficient bound is not claimed sharp
under a jointly passive apparatus or correlated calibration constraints.

## 2. Exact constants in the declared source metric

Since G^(-1)=I+u u^T, M^(-1)=2(I+u u^T). Thus

    alpha_j^2=2(||v_j||^2+(sum_i v_ji)^2)/4860^2.

In origin-then-calibration order the exact squared norms are

    63113/295245, 6962/32805, 6962/32805, 2341/10935,
    127309/590490, 413/1180980, 413/1180980, 29/393660.

Upward rational square-root bounds with denominator 10^6 are respectively

    0.462348, 0.460678, 0.460678, 0.462692,
    0.464327, 0.018701, 0.018701, 0.008583.

These terminating decimals denote exact rationals, not measured values.
Integer-square comparisons establish that each is an upper bound. With a
common eta_j<=eta, substitution gives

    S_transfer <= q_max (K1 eta + K2 eta^2),
    K1=320403677788237/69393956250000,
    K2=936962003/185050550.

K1 is an upward rational bound obtained from the displayed square-root
enclosures; K2 is exactly 1+sum_j |d_j|. No physical tolerance is chosen by
these constants. The exploratory script independently retains every exact
intermediate squared norm and verifies the direction of each enclosure.

## 3. What this removes from the prospective protocol

The earlier residual condition had an unexpanded transfer-systematics term.
An independent complex-transfer calibration can now provide eta_j and an
independent energy-range certificate can provide q_max. In their presence,
this part of the allowance becomes explicit:

    |R_observed| <= epsilon_origin
        + A epsilon_atom + B epsilon_deposit
        + S_transfer + S_other.

The existing exact A and B govern readout errors only. S_other must retain
uncertainty not covered by the calibrated linear map and readout bounds,
including source leakage, window/integration mismatch and normalization
errors where applicable. Each contribution needs one owner; shared errors
must not be silently counted twice or set to zero. A calibration derived
by imposing R=0 would be circular.

The prediction is checked on validation inputs excluded from context fitting.
Violation rejects the specified apparatus/dictionary claim within its stated
assumptions. Compatibility supports that tested analogue, not an autonomous
native U realization, an occurrence law, or a multi-time physical evolution.
