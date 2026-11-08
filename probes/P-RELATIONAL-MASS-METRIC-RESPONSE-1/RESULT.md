# Relational mass has a complete declared metric response

Status: PASS
Scope: NON-CANONICAL, NEW_DECLARED L1, fixed five-direction count carrier
Theorem status: conditional candidate-T; no Canon promotion
Fired falsifiers: none
Ownership: https://github.com/mathorn1973/twist-j/issues/1684
Preregistration pin: b5c8466118e546f8d93ea2071cb42ef018b6b2b6

## Energy and mass-square responses

For fixed covectors u_k, nonnegative integer counts n_k and a declared
positive inverse planar metric G, set eps_k=sqrt(u_k^T G u_k),
E=sum n_k eps_k and P=sum n_k u_k. The two derivatives are distinct:

    T_G=sum (n_k/eps_k) u_k u_k^T,
    R_G=E T_G-P P^T,
    dE[H]=tr(T_G H)/2,
    d(E^2-P^T G P)[H]=tr(R_G H).

The exact covariance formula makes R_G positive semidefinite. T_G has
rank 0,1,2 for support 0,1,at least 2; R_G has rank 0,1,2 for support
at most 1,2,at least 3. In particular zero mass square does not imply
zero energy response. The contractions tr(G T_G)=E and tr(G R_G)=D_G
are homogeneity identities, not an inferred gravitational conservation law.

D_G is homogeneous of degree one, monotone under positive-semidefinite
metric increments and concave on the positive metric cone. Its second
variation is

    d^2 D_G[H,H]=-sum_(r<s) n_r n_s eps_r eps_s
                          (beta_r-beta_s)^2/2,
    beta_k=(u_k^T H u_k)/(u_k^T G u_k).

For support at most one every strain is in its Hessian kernel; for two
directions the two betas must agree; for at least three directions the
kernel consists exactly of H=cG. These universal statements follow from
PROOF.md; the finite audit does not substitute for those proofs.

## The other arithmetic place and complete source information

At G0, let N=sum n_k, Z=sum n_k j^k, W=sum n_k j^(2k),
D=N^2-Z*conj(Z) and Q=N W-Z^2. Rational counts give W=sigma_2(Z).
In the exact component basis (1,j), det G0=(2+phi)/4 and

    4 det(G0) det(T)=tau(D),
    4 det(G0) det(R)=D^2-Q*conj(Q).

Equivalently, in orthonormal coordinates tau(D)=4 det(T_o). Because the
actual energy gradient is T_o/2, its determinant obeys
tau(D)=16 det(T_o/2). The other arithmetic place therefore controls a
tensor invariant of the same preparation at the reference metric. It is
not a second physical frame, particle species or empirical mass scale.

The exact pair (N,Z) reconstructs every count. With
Z=z0+z1*j+z2*j^2+z3*j^3, set r=(N-sum z_i)/5; the admitted preparation
is (z0+r,z1+r,z2+r,z3+r,r) when all entries are nonnegative integers.
Thus it determines the entire declared E(G), not just its first response.
This is an exact algebraic admission criterion, without a finite-precision
physical decoder claim.

Z alone leaves a whole-pentagon ambiguity. Adding h to all counts keeps
Z,W fixed, but adds 5h to N and (5h/2)G0^-1 to T. Z=0 holds exactly
for equal counts. This marked class does not supply Lorentz closure.
Five rotations of a primitive two-direction preparation have the same
N,D,tau(D) but distinct Q and R in a fixed marking. A simultaneous
rotation of preparation and metric is covariant. Scalar mass alone is
therefore insufficient directional input; the missing data are present
in the full exact preparation.

## Consequence for the gravity continuation

For a metric line through any positive base G_star, write
b_k=u_k^T H u_k and eps_k_star=sqrt(u_k^T G_star u_k). Then

    [epsilon^4] E(G_star+epsilon H)
        =-5 sum n_k b_k^4/eps_k_star^7 /128.

This is strictly negative whenever the line changes an occupied length.
An affine map from the old variables to G whose image includes such a
direction therefore produces a nonquadratic energy term. Adding it to
the old quadratic scalar Hamiltonian cannot retain its fixed linear
phase equations merely by substitution. Old transfer, Ward and constraint
closure statements would require a new proof for a newly declared joint
action. The result is not a no-go for nonlinear gravity.

Likewise, if an independently varied lapse multiplies precisely H_g+E
with H_g nonnegative, the equation H_g+E=0 excludes nonempty counts.
This is a conditional statement about that coupling, not a universal
constraint. The previous fixed-total-lapse boundary problem remains a
different variational problem and has not been silently replaced.

## Exact finite audit and boundaries

Two separately authored standard-library programs produced identical raw
certificate bytes. The primary uses direct Q(phi) matrix moments and
binomial coefficients; the breaker uses normalized integer triples,
pair-derived mass coefficients and square-root recurrences.

| Audit per implementation | Count |
|---|---:|
| Normative authority files | 5 |
| Count preparations in {0,1,2,3,4}^5 | 3125 |
| Fixed strain directions | 4 |
| Energy/mass series through degree 4 | 12500 |
| Energy moment ranks 0,1,2 | 1,20,3104 |
| Mass-response ranks 0,1,2 | 21,160,2944 |
| Hessian ranks 0,1,2 | 21,160,2944 |
| Rest preparations, including empty | 5 |
| Fixed-J fibre cases | 8 |
| Marked rotations | 5 |
| Deliberate defects detected | 8 |

All coefficients through degree four were calculated; predicted zero
residuals were not substituted. The exact payload contains 15651 records,
SHA-256 89be1fbdf46f25bdeb1093ac3fae226bd0cc78802cafceee40ad53d337a4dc91.
EXPECTED.txt is the 466-byte, 18-line stdout. RUN.md records the first
completed run. Required architecture replays are pending at this record
and will be receipted on the exact-head pull request.

The positive metric, fixed-covector convention and energy dependence are
explicit new choices. No native realization, spacetime metric, local source
projector, volume convention, old-field-to-metric map, common action,
physical clock, stable particle, SI calibration, equality of inertial and
gravitational mass, continuum limit or unnamed layer lift is established.
Canon, registry, policy and workflows remain unchanged.
