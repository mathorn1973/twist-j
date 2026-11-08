# P-RELATIONAL-MASS-BOOST-COMPLETION-1

Status: PROSPECTIVE, NON-CANONICAL, NEW_DECLARED L1
Owner: A. M. Thorn / ChatGPT-boost-completion-20261020
Ownership: https://github.com/mathorn1973/twist-j/issues/1692
Base: 0f26395b17597af882014b99639d1fb6ee6d3d36

## Equation, question and action layer

The original #1689 action has a stronger transport obstruction than the
absence of a fixed-charge moving minimum: its finite-energy internal
dilation charge bounds the center's total displacement along P. Prove
that obstruction, then explicitly declare and analyze a different L1
collective-center action which retains the accepted internal binding.

    theta=tr(Pi dG)+rho^T dr+P^T dX,
    h=tr(G Pi G Pi)/2+sqrt(rho^T G rho)+kappa r^T G^-1 r,
    j=2G Pi+r rho^T,
    q=P^T gamma P,
    H_new=F(h,q), F(h,0)=h.

Here gamma is a new fixed SPD reference inverse metric, not the old
dynamical G. Classify the freedom in F before additional boost premises;
prove exactly which premises force F=sqrt(h^2+c^2q). Realize the complete
planar Poincare Poisson algebra, including the actual internal rotation
charge S, and construct the stable moving family with inherited h*=10.
Compare energy curvature with an explicitly declared external center-force
coupling W=-f.X. This is an operational model comparison, not an empirical
force measurement or a native-U derivation.

PROOF.md additionally gives an analytical reference lift with a canonical
SPD gamma and symmetric Gamma. It restores the diagonal GL charge by an
unbounded, zero-energy reference momentum. That cost is part of the result;
the reference lift is not advertised as a finite-resource physical closure.
The finite verifier does not test this optional 20-dimensional extension.

## Carrier and sources

The main model has fourteen real canonical coordinates: symmetric SPD G,
symmetric Pi, and X,P,r,rho in R^2, with rho!=0. Frobenius matrix pairing
fixes the off-diagonal factor two. kappa>0 in the proof; kappa=3 and
gamma=I in the finite audit. c is a declared positive conversion constant.
The inherited h-flow's completeness and fixed-j* minimum/stability theorem
are accepted inputs from #1689, not a repeated audit.

The original-action comparison uses its own smooth domain rho+P!=0 and
rho-P!=0, its unchanged stream energy and full charge j+XP^T. No assertion
equates its nonzero-P dynamics with H_new. Draft #1691 remains separate.
No empirical, private, fitted or target-selected data enter this probe.

## Frozen analytical claims

1. Original action: P.Xdot=E Xdot^T G^-1 Xdot>=0 and
   |tr j|<=4sqrt(H_old)+H_old sqrt(H_old/kappa). Consequently a complete
   smooth finite-energy solution cannot have positive asymptotic mean
   drift along P. This is a no-go for ordinary longitudinal inertia in the
   original center/time convention, not a blanket no-bound-motion claim.
2. Within H_new=F(h,q), all internal trajectories are constant rescalings
   of the old h-flow. Stable translating families exist, but F_q and hence
   their inertia remain arbitrary without an added selection law.
3. Positive H_new, F(h,0)=h and boost brackets
   {Ki,pj}=delta_ij H_new/c^2, {Ki,H_new}=pi, {Ki,h}=0
   force H_new^2=h^2+c^2p^2. Uniqueness is restricted to this declared class.
4. K=H_new x/c^2-SRp/(H_new+h), L=x wedge p+S give the complete canonical
   planar algebra. The spin term is necessary for its rotation bracket.
5. The exact translating h*=10 family has energy sqrt(100+c^2q),
   internal clock factor 10/H_new, and model mass 10/c^2. Stability fixes
   internal j and P and quotients internal symmetries and center translations.
6. The test force gives rest acceleration (c^2/h)gamma f, agreeing with
   the energy Hessian. The original full GL charge is replaced unless the
   explicitly costed reference extension is included.
7. A prescribed smooth center-force pulse prepares the moving minimum
   at any specified finite impulse without internal excitation. Its final
   energy and velocity are independent of pulse shape and internal phase;
   the work identity agrees with the selected dispersion. This preparation
   protocol is proved analytically, not simulated by the finite audit.

## Code, systematics and failure threshold

Standalone standard-library verify.py uses Fraction and exact degree-two
Taylor arithmetic. FIXTURES.md freezes 36 full canonical algebra cases,
36 force cases, 18 rest Hessian directions, one exact moving witness,
four old-action transport cases and five negative controls. Every tested
root has a positive rational constant coefficient. No floating point,
integration, fitting, random selection, files or network enter execution.

Every asserted equality is exact. Any mismatch fires its named FALSIFIER
and RESULT=FAIL; unexpected exceptions are failures. Failure exits nonzero.
The first outcome is retained. No fixture, threshold, source or proof edit
and rerun is allowed under this pin. The finite audit does not prove
universal stability, completeness, all-state algebra or long-time limits;
those claims rest on the analytical proof and its explicit inherited input.

All work is NON-CANONICAL, L1. No Canon, registry, frontier, old probe,
workflow, policy or native-U change. Analytical claims have candidate-T
scope with same-session independent review; finite checks have candidate-C
scope pending required replay. This is one implementation with automatic
derivative and explicit-formula routes, not two independent programs or
an outside physical experiment. Established relativistic center/internal
constructions are attributed in SOURCE.md; no general framework novelty
is claimed.

## Prospective custody

Freeze PREREG.md, PROOF.md, SOURCE.md, FIXTURES.md, verify.py and
FROZEN.sha256 in a public commit. Read all six back by exact commit and
compare complete bytes and Git blob identities before execution. Hashes,
AST parsing and static review are allowed beforehand; scientific imports
and executions are not. FROZEN.sha256 binds the other five files.

From a clean exact-pin worktree, under a 60-second bound and LC_ALL=C,
LANG=C, TZ=UTC, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, run exactly:

    python3 probes/P-RELATIONAL-MASS-BOOST-COMPLETION-1/verify.py

Capture stdout/stderr, exit code, duration, platform and Python version.
Then add the actual EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md and README.md.
The six frozen files stay unchanged. Required PR jobs replay the same
verifier/output on x86_64 and aarch64. No merge or Canon promotion is part
of this task.
