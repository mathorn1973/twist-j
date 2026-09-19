# PREREG: P-J-HODGE-COUNTER-CARRY-FACTOR-1

FORMAL PUBLIC PROBE. Action layer L1. Issue #1067.
Base: Public Canon v89 main 20e6804ed1405672d9f8ceba68a30a0c875ffa50.

For n>=0 let s(n)=s_2(n) be binary popcount and define

    delta_n = s(n+1)-s(n),
    kappa_n = nu_2(n+1),
    C(n) = sum_(m=1)^n nu_2(m),  C(0)=0.

The public SQRT-PHI-DIGIT-LIFT chronological exponent is delta_n.

Frozen targets:

G1 Prove for every n>=0
    delta_n = 1-kappa_n,
hence delta_n+kappa_n=1.

G2 Prove
    C(n)=nu_2(n!)=n-s(n),
hence s(n)+C(n)=n.

G3 Uniqueness: if H(0)=0 is integer-valued and
    [s(n+1)-s(n)] + [H(n+1)-H(n)] = 1
for every n, then H(n)=C(n). Equivalently in the free infinite cyclic group
<r>, the unique normalized complement Z_n with r^s(n) Z_n=r^n is
Z_n=r^C(n).

G4 For either public finite root r_epsilon of r^2=phi in F_25, the formal
exponent specialization gives
    Y_n^epsilon r_epsilon^C(n)=r_epsilon^n.
This remains finite of order dividing eight. No finite/archimedean carrier
identification is made.

G5 In the characteristic-zero real quadratic extension with positive
rho^2=phi, define D_n=rho^s(n), K_n=rho^C(n). Then
    D_n K_n=rho^n,
    (D_n K_n)^4=phi^(2n),
    (D_n K_n)^(-4)=phi^(-2n).
The last pair matches the hyperbolic multiplier powers of the accepted
fixed-J Hodge loxodrome only as an exact comparison.

G6 Using the separately accepted algebraic identity
    a_H=phi^2 zeta_10,
record
    a_H^n=(D_n K_n)^4 zeta_10^n.
The torsion phase is a separate counter residue and is not derived from carry.

G7 The public finite digit branch has at most eight values and by the accepted
finite-reader obstruction cannot by itself supply a nonzero all-time
hyperbolic orbit. The carry-completed characteristic-zero exponent is n and
has infinite image. This classifies a missing mathematical resource, not a
physical read.

PROOF.md carries all universal quantifiers. verify.py is a deterministic exact
integer audit through a frozen finite range and audits exponent residues only;
it is not theorem evidence for all-n scope. No floating point, randomness,
external package, network input or tolerance.

Falsifiers are any exact failure of G1-G7 at the typed scope or any hidden
cross-place carrier identification. Runtime/integrity failure is STOP.

No physical clock/time arrow, gravity, checkpoint identity, decoder selection,
occurrence law, measure, SI scale, Canon promotion or L2-L6 lift.
SQRT-PHI-TIME-GRAVITY [O] remains open. The author explicitly authorized the
connected GitHub commit identity.
