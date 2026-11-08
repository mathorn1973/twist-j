# Analytical adversarial review of the nonzero-momentum continuation

Status: NON-CANONICAL, L1. Independent analytical review in the same session.
The reviewer saw the proposed claims and their proofs. This is not a blind
prediction, an external review, or a fresh audit of #1689. No scientific code
was imported or executed. The accepted predecessor minimum H=10 at P=0 and
J=J* is used as an input.

## Verdict

No mathematical blocker found in the displayed global and local continuation
claims. The strong negative conclusion concerns fixed affine momentum levels
and the attempted energy-minimum/relative-equilibrium continuation. It does
not exclude every possible nonzero-P bound trajectory.

## Checks and scope

1. The original unreduced Hamiltonian already specifies the nonzero-P vector
   field. On G SPD and rho+P,rho-P nonzero it is smooth; ordinary local
   uniqueness and finite-time dependence follow. A claim of complete flow for
   arbitrary nonzero-P initial data would be unsupported and is not made.

2. The full charge is J=2G Pi+r rho^T+X P^T. Consequently
   jdot_internal=-Xdot P^T. At P!=0, constant internal j forces Xdot=0,
   hence rho=cP with |c|>1. Preservation of this line under rhodot then
   forces r parallel to G rho. Whitening makes j symmetric, contrary to
   ellipticity. This proves the precise old-internal-charge obstruction.

3. The origin shift formula J->J+aP^T is essential. For J* and
   P=epsilon e1, a=(0,b) yields delta=8-4b epsilon. A claim that the full
   elliptic discriminant is an intrinsic moving binding invariant would be
   false; the draft explicitly avoids it.

4. In the low-energy family, G=diag(s^2,s^6), r=s^2 e1,
   rho=(4/s^2)e2, Pi=0, X=-(2/epsilon)e2, the two terms of J are
   [[0,4],[0,0]] and [[0,0],[-2,0]]. Both covectors remain nonzero.
   E=s sqrt(epsilon^2+16), V=3s^2 and K=0. Therefore the energy infimum
   is zero and unattained for any nonzero epsilon. The centralizer argument
   correctly extends this to all nonzero covectors P: solving L^T P=e1
   with L=aI+bJ* ensures that L^(-T)e1=P. This family is not a family of
   demonstrated bound trajectories and is not local to the rest state as
   P tends to zero. The proof states these restrictions.

5. The instantaneous Hessian is
   A=G/E-G rho rho^T G/E^3. Its whitened middle matrix is an orthogonal
   rank-one projection, so rank A=1 and ker A=span(rho). At the witness
   A=diag(1/6,0). Both the exact parallel plateau H=10 and the transverse
   expansion H=10+epsilon^2/12+O(epsilon^4) are correct.

6. The locally charge-exact family with X=c epsilon e2,
   rho=(6+c epsilon^2)e2, Pi12=-1-c epsilon^2/2 has precisely J*.
   Its kinetic term contributes c epsilon^2 and its stream term contributes
   (c+1/12)epsilon^2. The coefficient 2c+1/12 is therefore correct and
   ranges over all real numbers. These are different preparation sections,
   not different Hamiltonians and not proved stable moving branches.

7. For affine relative equilibria the necessary equations are
   B^T P=0 and [B,J]+bP^T=0. In coordinates P=e1 and
   J=[[a,c],[d,e]], ellipticity implies c!=0. Writing
   B=[[0,0],[u,v]], the second commutator column is (-cv,cu).
   Hence B=0, and then b=0. The resulting equilibrium is impossible
   because each occupied body's velocity is nonzero in the smooth domain.
   Thus the no-affine-relative-equilibrium theorem is valid.

8. The finite-time drift result uses a different observable from energy
   curvature. Evenness of the internal field in P gives an internal change
   of order epsilon^2 on the fixed unperturbed interval [0,T]. Integration
   of the rotated rank-one tensor yields diag(1/12,1/24). The derivative
   is mathematically well defined and need not coincide with the initial
   energy Hessian. No all-time drift or physical mass follows from it.
   The normalization Abar=Gbar/18 is correct but conditional on electing
   the averaged metric as the momentum comparison.

## Strengthened local-extremum corollary

The full smooth carrier has dimension 14 and the affine symmetry group has
dimension six. At P!=0 its infinitesimal phase action is free. Indeed a
stabilizer (B,b) obeys

    BG+GB^T=0, B^T P=0.

Put C=G^(-1/2)B G^(1/2). The first equation makes C skew-symmetric and the
second makes it annihilate the nonzero vector G^(1/2)P. A 2-by-2 real
skew-symmetric matrix with nonzero kernel is zero. Thus B=0; the center
position component then forces b=0.

Nondegeneracy of the symplectic form identifies the differentials of the
six moment-map components with the six independent fundamental vectors.
Therefore dmu has rank six. Every fixed full (J,P) level is locally a smooth
regular level here. If H had a constrained critical point on it, the
Lagrange-multiplier condition would give dH=<xi,dmu>, equivalently
X_H=xi_M. Conservation of mu then puts xi in its coadjoint stabilizer.
For elliptic full J and P!=0 that stabilizer Lie algebra is zero by item 7.
It follows that X_H=0, again impossible in the admitted domain.

Consequently there are no constrained critical points and no local extrema
of H on a fixed full elliptic-J, nonzero-P level. This strengthens the
failure of a global minimum. It still does not exclude other sorts of bound
motion selected by a different invariant/observation prescription.

## Additional-data boundary

A unique mathematical response requires a selected initial-state section
(to second order if only an energy curvature is wanted), a momentum/frame
comparison, and a specified observable and elapsed time. Those data suffice
for finite-time response because the action already fixes the flow. Calling
the result a bound-state mass additionally requires an actual bound-family
selection/existence/stability result; the old fixed-affine-charge minimum
cannot provide one. Scalar isotropy and physical calibration are separate
requirements. Necessary declarations should not be called a construction
of a stable moving family that has not been proved to exist.

## Pre-pin static source review

Read the consolidated `probe/PROOF.md` and `probe/verify.py` without
execution or importing the verifier. The symmetric-coordinate canonical
factors are correct: the off-diagonal components of both Gdot and Pidot
divide the ordinary coordinate derivative by two. The explicit source
force has coefficient -1/4 in rho+P,rho-P coordinates, while Xdot uses
the difference of the two normalized vectors and rdot their sum.

All announced initial square roots are rational: stream lengths are
5,13; 5,5; 2,3; and 5,5 before the factor two in rho+/-P. Rest covector
lengths are 5,6,13. The transverse witness has root 15/2 and energy 23/2.
The collapse epsilon values +/-3 and +/-16/3 have roots 5 and 20/3.
All six GL matrices are invertible. The finite counts 24,54,6,3,4,12,7
match the corresponding loops, witnesses and stated negative controls.

The code uses only standard-library Fraction and isqrt, with no file,
network, subprocess, dynamic import or external-data access. No security
blocker was identified. No claim is made that reading code proves its
actual execution outcome. The public pin and first exact execution remain
separate steps.

Two prose corrections were reported before pinning: replace the accidental
`generator,+which` text, and distinguish Noether conservation along the
flow from GL covariance (P and J transform rather than staying numerically
fixed under general GL changes). Neither changes the mathematical result.

## Integration and security record

The reviewed conclusions were synthesized in PROOF.md before the public pin.
The minor phrase conflating conserved charges with invariant coordinates was
corrected before pinning; the final text explicitly states conservation along
the Hamiltonian flow. The typographical line break was also corrected.
The proof and all source files were then frozen unchanged through the run.
The review found no unresolved mathematical or source/security blocker.

The first exact run passed all declared cases and negative controls. This
review is an independent analytical check within the same agent session,
not an outside review or a blind independent experimental replication.
Two-architecture exact-head replay and final repository acceptance remain
separate merge gates. No merge or Canon promotion is performed here.
