# Independent full-word composition and pair-account review

**PUBLIC / NON-CANONICAL. Conditional L1 analytical review, 2026-10-12.**
Reservation: [#1473](https://github.com/mathorn1973/twist-j/issues/1473).
All line references below name the immutable reviewed
[source pin](https://github.com/mathorn1973/twist-j/tree/bca348445715c03f4cdc3af6079207024dd40332/probes/P-U-CA40-DP5-FULL-CLOSURE-1).
This is a disclosed same-assistant-session analytical derivation and source
comparison, not blind replication, external human review or a numerical run.

## A. Review result and dependencies

The full-word composition and weighted final-pair aggregation are consistent
under the stated unitary propagator and valid local-enclosure premises.
No defect in those mathematical formulas was found in this static review.
That conclusion does not certify the running campaign or establish every
inherited local bound. In particular, this note does not independently
rederive all of `kernel.cpp`'s norm-ball operation bounds (lines 217-336), its
analytic tail/continuum implementation (lines 357-383), or the 384-cell MPFR
model preparation in `validated_model.cpp` (lines 108-113). These are explicit
inherited dependencies. Syntax/custody validation is not a proof of them.

## B. Derivation from the actual carried curve

Assume R(t) has the declared unitary propagator on the harmonic Hilbert space.
On cell j let p_j be the actual finite-support dyadic polynomial, y_(j-1)
its incoming stored state, y_j the actual stored outgoing state, and

```text
p_j(t_(j-1)) = y_(j-1),
r_j(t) = i p'_j(t) - R(t)p_j(t),
d_j = integral_cell ||r_j(t)|| dt,
J_j = ||p_j(t_j) - y_j||.
```

Variation of constants bounds the exact evolution from y_(j-1) by d_j from
the polynomial endpoint. The final stored-state jump adds J_j. If the prior
error is E_(j-1), unitarity carries it unchanged in norm, so

```text
||y_j - psi(t_j)|| <= E_(j-1) + d_j + J_j,
||y_m - psi(t_m)|| <= sum_(j=1..m) (d_j + J_j) <= C_m,  C_0=0.
```

Here E_(j-1) denotes a valid preceding error bound and C_m is the outward
cumulative runtime certificate, which can exceed the exact sum through rounding.

No projected propagator is assumed unitary. No Gronwall multiplier is needed.
No normalization or fit is permitted. Bounds from independently reset windows
cannot substitute for defects of this actual carried curve. The stored final
jump is charged once: the next polynomial begins at y_j, not at p_j(t_j).
Snapshot copying introduces no mathematical jump.

Implementation comparison: `higher_order.hpp` lines 56-78 explicitly copies the
incoming state into poly[0] and constructs the quintic. `full.cpp` lines 183-209
initializes once, compares poly[0] with each actual incoming state, calls the
certifier and carries the state/certificate across all eighty segments.
`kernel.cpp` lines 382-383 charges the outgoing jump and upward cumulative sum.
`full_run.py` lines 257-330 can check only saved boundary consequences of those
runtime assertions; it cannot recover the missing per-cell polynomials.

## C. Switches and inactive segments

A bounded piecewise change of the coefficients changes the one-sided
Hamiltonian without a delta kick. The state remains continuous; the next
cell requires the right-side coefficients and a fresh initial derivative.
Its previous certificate remains in force. In the declared compensated
moving-frame parent, an inactive segment has R=0 and therefore carries the
entire state and accumulated certificate identically. This statement does
not discard the original physical linear history: that history is restored
at the common final time.

Comparison: `full.cpp` lines 136-147 checks active indicators in the prepared
stage and Gauss profiles, and lines 188-209 carries the actual state. Each
`higher_order_step` computes its initial derivative afresh; no cross-cell FSAL
reuse is present (`higher_order.hpp` lines 56-60). Inactive payload identity is
auditable from saved bytes (`full_run.py` lines 310-317). Active endpoint
agreement alone cannot rule out an internal reset between snapshots.

## D. Relative linear-frame restoration

Write U_L,z = exp(i phi_z) D(alpha_z). Weyl composition gives

```text
U_L,b^* U_L,a = exp(i theta_ab) D(alpha_a-alpha_b),
theta_ab = phi_a-phi_b + Im(sum_m conjugate(alpha_b,m)*alpha_a,m).
```

Thus a retained sine coherence uses the overlap of the carried b-vector with
the displaced carried a-vector and this relative phase, at the same final T.
Different branch onset times cannot be substituted for a common endpoint.
`validated_model.cpp` line 113 computes exactly this delta and phase; `full.cpp`
lines 243-245 applies them to the carried states. This review checks the sign
and operand order. It does not independently evaluate the MPFR intervals or
the full displacement implementation. The saved auditor accordingly checks
rectangle arithmetic but labels restoration recomputation unavailable.

The subtraction of the raw-parent unary sine term is an explicit model
choice, not a general permission to discard a branch-dependent phase.
This account concerns that compensated parent only.

## E. Weighted Gram error with nonunit stored vectors

Let q be retained thermal mass. Package each branch's exact and stored
retained vectors into weighted purifications X_z and Y_z. Then

```text
||X_z|| = sqrt(q),  ||Y_z|| = A_z,
||X_z-Y_z|| <= E_z,
E_z^2 >= sum_n p_n e_(z,n)^2,
A_z^2 >= sum_n p_n ||y_(z,n)||^2.
```

For unitary relative restoration V, insert either one mixed overlap:

```text
|<X_b,VX_a>-<Y_b,VY_a>|
 <= min(sqrt(q)*E_a + A_a*E_b, sqrt(q)*E_b + A_b*E_a).
```

The indices in these two equivalent bounds follow by expanding first one
error term and then the other. Replacing the bound by E_a+E_b is unsafe unless
the stored norms are controlled. There is no multiplier equal to thermal
rank. `full.cpp` lines 235-246 applies positive thermal weights, upward RMS
bounds and this minimum. `full_run.py` lines 444-466 checks saved aggregation
with exact squared comparisons and a required nonnegative affine difference.

Specific strengthening: `full_run.py` lines 447-449 takes each saved norm
interval as an enclosure of the actual endpoint without independently
recomputing the norm from those bytes. This is an audit gap, not evidence that
the C++ norm routine is wrong. `audit_saved.py` recomputes the terminal norm
exactly from IEEE significands and exponents. Synthetic understated-norm
fixtures must fail. Optional all-snapshot norms strengthen the same check.

## F. Thermal tail, center width and decisions

The exact retained weights are (20/21)^7(1/21)^N, N<=3. The full-linear
reference already includes its entire thermal distribution. The omitted sine
coherence has modulus at most p_tail by unitarity, so its Bell half-distance
radius is p_tail/2 once, where p_tail=680046581/794280046581.

If [c_lo,c_hi] encloses half the magnitude of the retained-sine minus
full-linear complex coherence, define r_num=B_ab/2, r_th=p_tail/2 and
r_arith >= (c_hi-c_lo)/2. Then

```text
r_total >= r_num+r_th+r_arith,
D_ab in [max(0,c_lo-r_num-r_th), min(1,c_hi+r_num+r_th)].
```

Adding r_arith again to an already interval-valued center would double-count
it. Omitting it from r_total would make the precision goal unsound.
`full.cpp` lines 245-247 and `full_run.py` lines 468-487 implement these separate
roles. The auditor checks squared extrema of the complex rectangle exactly.

Numerical precision passes only if all six total radii are <=1/1000.
Independently, each distance is above threshold iff its lower endpoint is
strictly greater than 1/1000, within iff its upper endpoint is <=1/1000, and
otherwise unresolved. One above-threshold pair per sign supports the limited
two-angle discrepancy statement. It neither covers all inputs nor measures
apparatus error. A valid wide interval can resolve discrepancy while failing
precision; a precision PASS can accompany a resolved undesirable discrepancy.

## G. Evidence limits and disposition

The copied manifest/summary/checkpoint receipts are mutually checked records,
not an independent execution attestation. Closed payloads plus markers do not
prove crash durability. C++ uses close then rename and writes the marker last
(`full.cpp` lines 75-98); markerless or partial files must remain uncommitted.
The auditor rejects holes, altered inactive carries, terminal disagreement,
understated norms, unsafe exact-threshold decisions and broken copied custody.

No actual campaign outcome is available to this preparatory review. Any
source repair, new pulse, longer deadline or renewed attempt needs a new
preregistration and pin. This note changes none of the original sources and
creates no physical, canonical or all-input admission.
