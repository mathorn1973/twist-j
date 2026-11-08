# P-RELATIONAL-MASS-CLOSED-RECOIL-1

Status: PROSPECTIVE, NON-CANONICAL, NEW_DECLARED L1
Owner: A. M. Thorn / ChatGPT-closed-recoil-20261020
Ownership: https://github.com/mathorn1973/twist-j/issues/1694
Base: 0f26395b17597af882014b99639d1fb6ee6d3d36

## Question, equations and action layer

Can two already stable composites compare their inertia in a closed
finite-energy preparation, using free center readings and their internal
clocks? Does that construction select physical mass from native U?
Keep the accepted internal binding and explicitly distinguish conditional
operational mass ratios from native law selection and physical occurrence.

    theta_i=tr(Pi_i dG_i)+rho_i^T dr_i+P_i^T dX_i,
    h_i=tr(G_i Pi_i G_i Pi_i)/2+sqrt(rho_i^T G_i rho_i)
          +kappa r_i^T G_i^(-1)r_i,
    j_i=2G_i Pi_i+r_i rho_i^T,
    epsilon_i=sqrt(h_i^2+c^2P_i^T gamma P_i),
    H_AB=epsilon_A+epsilon_B+W(X_A-X_B).

Here gamma is one common fixed SPD inverse metric, c>0 is declared,
and W is a newly declared smooth repulsive center-only interaction.
The inherited common boost law and rest-energy normalization are new
model premises, not consequences of U. W uses canonical X, not the
noncanonical free covariant center Y constructed in PROOF.md. No
interacting Lorentz locality is assumed or claimed.

## Carrier, data and inputs

Each object has fourteen canonical real coordinates (symmetric SPD G,
symmetric Pi, X,P,r,rho in R^2), with rho!=0 and Frobenius off-diagonal
factor two. The joint finite audit differentiates all 28 coordinates.
kappa=3 and gamma=I in the audit, c in {1,2}. The optional direct-sum
finite spectator C makes the reference outputs explicit analytically;
the 42-dimensional enlargement is not part of the finite audit.

#1689 supplies complete elliptic internal flow and the sharp fixed-charge
minimum bound. Its h=10 object is an accepted input, not a repeated audit.
Draft #1693 supplies the declared free dispersion and planar boost law.
It remains unmerged and noncanonical. A new h=45 minimum at the same
kappa is proved here. Native counter-reading classification and finite
reader boundaries are accepted at their published scope; full U includes
an unbounded counter. SOURCE.md gives exact pins and attribution.

All fixture values are analytic choices disclosed before execution. No
empirical dataset, fitted physical constant, private data or native
preparation experiment is used. Same-session reviewers saw the candidate
claims; this is not blind prediction or external physical validation.

## Frozen claims and falsifiers

1. The spin-corrected free center Y satisfies the displayed free worldline
   brackets, with {Y1,Y2}=c^2S/(h epsilon). Canonical X generally does not.
   Neither free result proves interacting locality or a detector coupling.
2. At exact j_B=[[0,42],[-6,0]], the known sharp bound attains h_B=45,
   yielding a second stable relative equilibrium with kappa=3.
3. The closed interaction preserves h_i,j_i,total momentum and energy,
   retains binding, and gives complete flow. A radial repulsive bump
   prepares an outgoing free channel in finite time from rest.
4. At h_A=10,h_B=45,w=22,c=1,gamma=I, outgoing energies are 26 and 51,
   opposite momenta have length 24, clock rates are 5/13 and 15/17, and
   free speeds are 12/13 and 8/17. Thus m_B/m_A=9/2; the checker prints
   the explicitly labeled reciprocal m_A/m_B=2/9. Raw speed and kinetic
   energy ratios are not the rest-mass ratio.
5. A finite spectator C and calibrated finite-window phase records make
   the relative readout explicit. AB separation alone does not give both
   velocities; an instantaneous periodic state is not an unbounded clock.
6. The cubic comparison law a(h)=1+(h-10)^3/12250 agrees with the selected
   free Hamiltonian and its full vector field at h=10 for every momentum,
   but predicts weak recoil ratio 1 instead of 9/2 for h=10 versus h=45.
   The common boost premise excludes it; conservation and binding do not.
   A further F_R/F_N comparison agrees at rest curvature but differs in
   the dimensionless fourth derivative (-1 versus 0).
7. Unrestricted native counter intertwining realizes any stipulated
   complete target flow and therefore cannot select this mass law. The
   fixed-origin initial menu has 3125 labels and cannot cover an open
   continuous preparation family exactly. Enlargements/limits need a
   separate contract.
8. If a closed reference extension retains a bounded nonposition dilation
   charge and conserved relative momentum, its transported frame/clock
   readings cannot yield finite positive-mass asymptotic coasting under
   the convergence premises in PROOF.md. This is a scoped obstruction,
   not a prohibition on all proper-distance growth.

Every failed equality or counterexample to the stated analytic premises
is a falsifier. Physical mass from U, empirical species identification,
absolute unit calibration and gravitational equality remain unproved.

## Finite audit and systematics

Standalone standard-library verify.py uses exact Fraction arithmetic and
degree-four Taylor coefficients. FIXTURES.md fixes 36 free-center cases,
6 fourth-order discriminators, 1 new B-state witness, 8 full-carrier
contact cases, 4 canonical-X rest acceleration ratios, 4 outgoing cases,
3 complete-reference-calibration cases and 5 negative-control categories.
The five controls reject canonical-X covariance, canonical-Y brackets,
the raw speed reading, omission of one clock factor, and the wrong boost
law. Controls are deliberate incorrect claims which must be rejected.

All roots at tested constants are positive rational numbers. The bump's
Taylor exponential has exactly zero constant exponent at contact; outside
its support it is exactly zero. No numerical integration, floating point,
random search, file input, network access or imported old verifier occurs.
The initial and outgoing phase-space fixtures test local identities and
conserved endpoint quantities; they are not a claim that arbitrary fixture
positions/phases are one integrated trajectory. The proof supplies the
existence and endpoint theorem.

Any mismatch gives its named FALSIFIER, RESULT=FAIL and nonzero exit;
unexpected exceptions are failures. There is no tolerance or statistical
threshold. Universal stability, completeness, all-state identities and
native classification rest on proofs, not the finite audit. One exact
implementation and same-session mathematical review are not two
independent implementations or an outside experiment.

## Prospective custody and disposition

Before the first scientific execution, publicly commit PREREG.md,
PROOF.md, SOURCE.md, FIXTURES.md, verify.py and FROZEN.sha256. The manifest
binds the other five. Read all six back at the exact commit, comparing
complete text and independently calculated Git blob identities. Only
writing, reading, hashing, AST parsing and static review precede the pin.

From a clean exact-pin worktree, with LC_ALL=C, LANG=C, TZ=UTC,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and a 60-second bound, run:

    python3 probes/P-RELATIONAL-MASS-CLOSED-RECOIL-1/verify.py

Preserve the first stdout/stderr, exit status, duration, platform and Python
version. No frozen-file edit or scientific rerun is allowed to repair that
outcome. Add actual EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md and README.md
afterward. Required PR jobs replay the frozen verifier/output on x86_64
and aarch64. Failure is retained and reported, not hidden by tuning.

This is one separate NON-CANONICAL L1 probe, with candidate-T analytical
claims and candidate-C finite checks pending required replay. No Canon,
registry, frontier, native U, workflow, policy or predecessor modification.
No merge or Canon promotion is part of this task.
