# P-RELATIONAL-MASS-INERTIAL-RESPONSE-1

Status: PROSPECTIVE, NON-CANONICAL, L1
Owner: A. M. Thorn / ChatGPT-inertial-response-20261020
Ownership: https://github.com/mathorn1973/twist-j/issues/1690
Base: 0f26395b17597af882014b99639d1fb6ee6d3d36

## Equation and question

Keep exactly the complete two-unit-group Hamiltonian of #1689:

    theta=tr(Pi dG)+P^T dX+rho^T dr,
    H=tr(G Pi G Pi)/2
       +(sqrt((rho+P)^T G(rho+P))+sqrt((rho-P)^T G(rho-P)))/2
       +kappa r^T G^(-1)r.

The problem is whether its P=0 stable minimum at kappa=3, J=J* has a
well-defined moving continuation and an inertial energy curvature. The
unreduced vector field is already fixed; no alternative Hamiltonian is
introduced. The inherited interaction and coefficient remain premises.

## Carrier and data

Real 14-dimensional canonical carrier: G SPD symmetric, Pi symmetric,
X,P,r,rho in R^2, rho+P and rho-P nonzero. Canonical matrix pairing is
Frobenius, with the off-diagonal factor two. The full charge is
J=2G Pi+r rho^T+XP^T. Time is the original fixed Hamiltonian time.
The accepted P=0 source witness is

    kappa=3, G=I, Pi=[[0,-1],[-1,0]], X=0, P=0,
    r=e1, rho=6e2, J*=[[0,4],[-2,0]], H=10.

The old minimum/stability theorem is an input; its audit is not rerun.
No empirical measurements, private sources or physical calibration enter.

## Code and frozen analytical scope

PROOF.md contains analytical proofs, disclosed before execution:

1. Unique local all-P action flow, full charge conservation and the
   obstruction to constant elliptic internal j=2G Pi+r rho^T at P!=0.
2. Instantaneous Hessian A=G/E-G rho rho^T G/E^3, rank one, and
   A*=diag(1/6,0). Exact parallel and transverse energy witnesses.
3. Same-action, same-J*, same-rest-point preparation sections with any
   quadratic energy coefficient 2c+1/12.
4. Full-charge infimum F(0)=10, F(P)=0 unattained for every P!=0;
   no affine relative equilibrium and no constrained local energy
   critical point when the full J is elliptic and P!=0.
5. For explicitly fixed rest initial data, the derivative of mean center
   displacement over the fixed old period T=sqrt(2)pi is
   diag(1/12,1/24). Its optional averaged-metric ratio is 18; it is not
   declared a physical mass or an energy-dispersion curvature.

The standalone standard-library verify.py uses Fraction and exact degree-two
Taylor arithmetic. FIXTURES.md freezes the complete finite inventory:
24 full-action field cases, 54 Hessian directions, six charge/energy
witnesses, three preparation sections, four mean/phase algebra checks,
12 low-energy states and seven negative controls. Formal roots have
strictly positive rational constant coefficients. No floating point,
integration, fitting, external input or adaptive case selection is used.

## Systematics and failure threshold

Every asserted equality is exact. Any mismatch fires its named FALSIFIER
and RESULT=FAIL. Unexpected exceptions produce an explicit failure, not
PASS. No tolerance or threshold can move. The first completed run is
retained, including a failure; no edit-and-rerun is allowed under this pin.
Seven negative controls challenge frozen internal charge, scalar/positive
definite Hessian, inherited old minimum, omission of XP^T, reuse of the old
invertible generator and unique preparation curvature.

Finite checks audit algebraic identities; universal results, existence and
nonexistence statements rest on the written proof. The mean-tensor check
uses analytically proved trigonometric moments, not computed perturbed
trajectories. The low-energy points and preparation sections are not
asserted to be stable moving bound states. No full all-P completeness,
long-time approximation or blanket no-moving-bound-object claim is made.

## Action layer and status ceiling

All new work is L1, NON-CANONICAL. No Canon, registry, frontier, workflow,
policy, old probe, native U, physical reading or layer gate changes.
Analytical claims have candidate-T scope with same-session independent
derivation/review; exact finite checks have candidate-C scope pending
required replay. The code is one implementation with automatic-derivative
and explicit-equation routes, not two independent programs. No blind
prediction, independent outside review or physical mass identification.

## Prospective custody and execution

Freeze PREREG.md, PROOF.md, SOURCE.md, FIXTURES.md, verify.py and
FROZEN.sha256 in a public commit. Read every public file back and compare
bytes and Git blobs before the first execution. Hashing, AST parsing and
static review are permitted before the pin; scientific imports and runs
are not. The FROZEN.sha256 manifest binds the other five files.

Run from a clean exact-pin worktree under a 60-second bound, with
LC_ALL=C, LANG=C, TZ=UTC, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0:

    python3 -I probes/P-RELATIONAL-MASS-INERTIAL-RESPONSE-1/verify.py

Capture exact stdout/stderr, exit code, duration, platform and Python
version. Then add EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md and README.md.
The six frozen files remain byte-identical. Required PR jobs replay the
same verifier/output on x86_64 and aarch64. No merge is part of this run.
