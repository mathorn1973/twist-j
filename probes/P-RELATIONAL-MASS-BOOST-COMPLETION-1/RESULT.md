# Result

Status: NON-CANONICAL, NEW_DECLARED L1.
First exact run: PASS. No scientific falsifier fired.
Analytical scope: candidate T; finite computation: candidate C with required
public architecture replay recorded by the PR checks. No Canon promotion.

## Original action: a global transport obstruction

For every complete smooth finite-energy solution of the unchanged #1689
action, the center's total longitudinal displacement is finite:

    P.Xdot=E_P Xdot^T G^-1 Xdot>=0,
    |tr j|<=4sqrt(H_old)+H_old sqrt(H_old/kappa),
    P.[X(t)-X(0)]=tr j(0)-tr j(t).

Its long-time mean drift cannot have a positive component along P. A
positive inertial dispersion for this center cannot be recovered by merely
changing preparation. This is stronger than the missing moving minimum,
but does not exclude transverse drift or every possible bound trajectory.

## A conditional, operational model of inertia

The new action explicitly separates the collective center from the retained
internal h-flow. Within H_new=F(h,P^T gamma P), the boost premises
{Ki,pj}=delta_ij H_new/c^2, {Ki,H_new}=pi and {Ki,h}=0 uniquely force

    H_new=sqrt(h^2+c^2P^T gamma P).

Actual canonical boosts, including the internal spin term, realize the
complete planar Poincare Poisson algebra. The accepted h*=10 minimum has
the exact stable internally bound moving continuation

    E_*(P)=sqrt(100+c^2P^T gamma P),
    z(t)=z_*((10/E_*)t),
    Xdot=c^2gamma P/E_*,
    m_model=10/c^2.

Stability fixes internal j,P and quotients the inherited internal symmetry
and center translations. It is not stability of absolute center position
against neighboring velocities. A smooth prescribed center-force pulse
prepares the family without internal excitation. At nonzero final impulse,
energy change and force response determine the same model mass; pulse shape
and internal phase do not change the final energy/velocity. The external
coupling and calibration remain new declarations.

Before the boost premises, F=h+q and F=h+2q already give different positive
inertial curvatures. Thus conservation and stable binding alone do not select
the coefficient. The full old diagonal GL charge is not conserved in the
fixed-reference model. An optional autonomous reference lift restores it by
unbounded zero-energy reference momentum. Making finite energy bound all
non-center dilation charge restores the transport obstruction.

## Finite audit and limits

The first pinned run passed 36 full canonical algebra cases including both
Casimirs, 36 force cases, 18 Hessian directions, the explicit moving witness,
four old-action transport cases and five negative controls. Its actual
stdout is EXPECTED.txt; RUN.md gives immutable pin and hashes. The universal
results, stable orbit, pulse protocol and reference extension are analytical
proofs, not inferred from those finite samples.

The work identifies a model mass under new center/reference/boost/force
premises. It does not identify a calibrated physical mass, derive those
premises from U, supply microscopic covariant worldlines, or equate inertial
and gravitational mass. The relational scalar, permanent binding and
physical inertial response remain distinct levels of claim. The original
harmonic interaction remains assumed. #1689 is used without repeating its
audit; draft #1691 stays independent and unchanged.
