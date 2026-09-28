# Result: native-cover metric class and the Hodge member

Status: PUBLIC NON-CANONICAL.
Owner: #1251. Author: A. M. Thorn <thorn@twistj.com>.
Ceiling: candidate-T classification, candidate-D selected Hodge seam,
candidate-C exact reproduction.

## Exact classification

The N2 tagged cube completion splits linearly into the native hexagonal
difference plane and the tagged diagonal direction d=(1,1,1).

After granting the full abstract symmetry of the selected regular hexagonal
cover and normalizing every cover unit step to squared length one, every
positive quadratic metric is exactly

    Q_rho=(3/2)I_3+(rho/9-1/2)11^T,    rho>0.

Thus one and only one positive dimensionless ratio survives:

    rho=Q_rho(d).

All members have cubic large-scale metric-ball growth and are compatible with
the same immutable prefix geometry.

## Hodge value

The accepted fixed-J Hodge spatial metric gives exactly

    q_H(unit)=2sqrt5/15,
    q_H(d)=3sqrt5/2,
    rho_H=45/4.

After cover-unit normalization,

    Q_H,norm=(3/2)I_3+(3/4)11^T=Q_(45/4).

A distinct admissible control is

    Q_E=(3/2)I_3=Q_(9/2).

Therefore the current native cover, its symmetry, positivity, cubic growth and
prefix consistency do NOT derive the Hodge metric.

## Selected flat seam

If the fixed-J Hodge target is independently adopted as a candidate-D
dictionary choice, the seam becomes parameter-free after unit normalization.
The complete normalized flat Lorentz form is

    g_norm =
      Q_(45/4) direct-sum [-(15+6sqrt5)/16],

with signature (3,1). Positive overall rescaling leaves its null cone
unchanged.

This is an exact selected flat-spacetime metric, not a native derivation of
rho=45/4.

## Remaining debt

A derivation claim now has one sharply identified missing datum: an independent
metric-sensitive native law that fixes rho=45/4. Larger archives, additional
prefixes, cubic counting and symmetry alone cannot do it.

Event resolution, generation time versus event time, METRO-TICK calibration,
SI units, physical Galois selection, curvature and the photon global/measure
obligations remain unchanged.

## Exact audit

The unchanged prospective pin
e0118a96f999e51ad623bb3cbc7954c38bd634a0 passed on arm64 and x86_64 with
identical 545-byte stdout, SHA256
5013c405ddca328076df12203ff65c0c69f4dbd2eb3866c29d1ebbcb4382b70f,
exit 0 and empty stderr.

The audit solved the exact invariant-form constraints, checked 512 tagged
diagonal increments, reproduced rho_H=45/4 and the distinct rho=9/2 control,
and reproduced the normalized time coefficient. Universal classification
rests on PROOF.md. The two executions are same-code reproduction, not
independent-agent confirmation.
