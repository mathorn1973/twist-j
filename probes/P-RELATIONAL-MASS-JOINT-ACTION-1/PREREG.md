# P-RELATIONAL-MASS-JOINT-ACTION-1

Status: PROSPECTIVE, NON-CANONICAL, NEW_DECLARED L1
Owner: A. M. Thorn, session relational-mass-joint-action-2026-10-20
Claim: https://github.com/mathorn1973/twist-j/issues/1686
Base: 4d345bf1c73da73c1922fdba9893ee5644742275

## Question and declared action

Does the following new homogeneous planar carrier give a common variational
evolution of inverse metric and relational matter, and which of its balances
survive a separately declared algebraic energy-preserving step?

G is a real SPD symmetric 2 by 2 inverse metric, Pi its symmetric canonical
momentum. For each occupied group n_k>0, x_k is a real position and p_k a
nonzero real covector. The n_k are fixed integer labels; p_k is varied
continuously before solving the equations. Unoccupied groups are omitted
from the phase space. With Frobenius pairing, including both off-diagonal
entries, and an explicit kinetic normalization of one, declare

    K=tr(G Pi G Pi)/2, E=sum n_k sqrt(p_k^T G p_k), H=K+E,
    S=integral [tr(Pi Gdot)+sum n_k p_k^T xdot_k-H]dt.

The resulting equations and charge are

    Gdot=G Pi G, Pidot=-Pi G Pi-T/2,
    xdot_k=G p_k/epsilon_k, pdot_k=0,
    T=sum (n_k/epsilon_k)p_k p_k^T,
    J=2G Pi+sum n_k x_k p_k^T,
    C=tr(G Pi), P=sum n_k p_k, D=E^2-P^T G P.

PROOF.md proves energy exchange, conservation of H, P and J, global SPD
flow at every finite time, Cdot=-E/2, and E,D tending to zero at both time
infinities for nonempty matter. Full-span momenta imply G tends to zero
at infinite time. It proves no equilibrium or periodic full orbit for
nonempty matter, not a universal gravity or binding no-go. A clock pair
with constraint p_t+H=0 is a separate declaration. A lapse imposing H=0
alone excludes nonempty matter. Exact time-one Hamiltonian flow is analytic,
symplectic and integer-indexed, not a native integer or finite-field update.

The new metric kinetic carrier replaces the earlier scalar carrier. No h-map,
old M0, scalar Ward identity, physical metric, native clock, source density,
local propagation, stable particle, inertial/gravitational mass equality,
L2 realization or other layer lift is inherited. Existing Canon FRW joint
actions retain their different scope. Authority and source custody are in
SOURCE.md. Public Canon is unchanged.

## Separate divided-difference step

For SPD endpoints, fixed p and epsilon_+/-=sqrt(p^T G_+/- p), define

    A=[Pi_- (G_++G_-) Pi_-+Pi_+ (G_++G_-) Pi_+]/4,
    B=[G_- (Pi_++Pi_-) G_-+G_+ (Pi_++Pi_-) G_+]/4,
    Q=sum n_k p_k p_k^T/(epsilon_++epsilon_-),
    DeltaG=hB, DeltaPi=-h(A+Q),
    Deltax_k=h(G_++G_-)p_k/(epsilon_++epsilon_-), Deltap=0.

This DG relation is locally analytic near h=0, symmetric and second order.
It preserves H exactly. With M=(G_++G_-)/2, Nbar=(Pi_++Pi_-)/2,
d=DeltaG and e=DeltaPi, its actual charge defect is

    DeltaJ=(h/2)(d Nbar d Nbar-M e M e).

For initial Pi=0 its cubic coefficient is -G T G T/8. The exact finite
witness below is regular and nonsymplectic. No all-h existence, uniqueness,
connection of that finite witness to the h=0 branch, or discrete canonical
variational principle is asserted. A proved defect is an intended boundary
result, not a failed audit gate. A discrepancy in its claimed value fails.

## Exact arithmetic, geometry and finite carrier

All finite computational audits use F=Q(phi), phi^2=phi+1 with phi>1, represented
exactly over rational numbers. Put gamma=phi-1 and

    u0=(1,0), u1=(0,1), u2=(-1,gamma),
    u3=(-gamma,-gamma), u4=(gamma,-1),
    G0=[[1,gamma/2],[gamma/2,1]].

Check G0 SPD, all u_k unit in G0, sum u_k=0 and
sum u_k u_k^T=(5/2)G0^-1. Field signs must be exact, with no floating-point
square roots, tolerances, numerical ODEs, fitted constants or outcome tables.
Formal square roots start at one and are computed in F[[h]] through degree
four. Finite witness roots are prescribed positive rational roots and must
be checked by squaring and sign. Finite audits support the universal proof;
they do not establish global claims by finite extrapolation.

The main count box contains all 32 tuples in {0,1}^5 in Python
itertools.product(range(2),repeat=5) order, n0 outermost. For each tuple
use initial G=G0, x_k=0, p_k=u_k and seven initial Pi values, in this order:

    0: zero, 1: G0^-1, 2: -G0^-1,
    3: [[1,0],[0,0]], 4: [[0,0],[0,1]],
    5: [[0,1],[1,0]], 6: [[0,-1],[-1,0]].

There are 224 main trajectory cases. Absent slots have x_k(h)=0 in the
fixed-width audit representation; no equation of motion is imposed on them.
All five p entries remain in the marked geometry, but only occupied slots
contribute to E,T,P,J and matter equations. The empty preparation is allowed.

For each case form independent FLOW and DG series for G,Pi and occupied x
through degree four. Compute actual K,E,D,C and all four entries of J at
every degree 0..4, including nonzero coefficients. Do not insert expected
zero coefficients or a symbolic predicted defect into the certificate.

Required main checks:

- Symmetry, initial data, exact root squares and inverse denominators.
- FLOW equations through vector-field degree three; H and J coefficients
  one through four vanish. Check Edot=tr(T Gdot)/2=-Kdot and Cdot=-E/2
  through degree three using computed series.
- DG endpoint equations through degree four, H coefficients one through
  four zero, and actual DeltaJ equal to the full defect formula through
  degree four. For initial Pi=0 check the cubic value -G0 T0 G0 T0/8.
- FLOW and DG state coefficients agree through degree two, without imposing
  higher-order equality. Each method has 1120 serialized coefficient rows.
- D0=(3-phi)A_count+(2+phi)B_count, where
  A_count=sum n_k n_(k+1) and B_count=sum n_k n_(k+2), indices modulo five.
  Every D coefficient must be computed as E^2-P^T G P.
- At each initial state check directional derivatives of K with respect
  to G and Pi and of E with respect to G, for S=E00,E11 and [[0,1],[1,0]].
  Obtain directional coefficients from the corresponding perturbed
  expressions and compare to tr(Pi G Pi S), tr(G Pi G S), tr(T S)/2.

## Covariance and exact finite witness

Use two base cases, in order: n=(1,0,1,0,0), Pi index 5; then
n=(1,1,1,1,1), Pi index 0. For each use, in order,

    A0=[[1,1],[0,1]], A1=[[0,1],[1,0]], A2=[[2,0],[0,1]].

This gives covariance cases c=0..5. Transform each computed coefficient
by G'=A G A^T, Pi'=A^-T Pi A^-1, x'=Ax, p'=A^-T p. Re-evaluate the
actual FLOW and DG equations on those transformed coefficients through
the same orders. Recompute invariants and check K,E,D,C unchanged and
J'=A J A^-1, with initial lengths one. Serialize the transformed actual
states and invariants, for both methods. No separate solver is required
for these transformed trajectories.

For the one finite exchange witness set n=(1,1,1,1,1), p=u,

    h=1100/1921,
    G_-=(36/25)G0, Pi_-=0, x_-=0, epsilon_-=6/5,
    G_+=G0, Pi_+=-G0^-1,
    x_(k,+)=(1220/1921)G0 u_k, epsilon_+=1.

Compute all DG quantities from the endpoints. Check both metrics SPD,
the roots, every endpoint equation and the general charge defect identity.
The required actual results are K:0->1, E:6->5, H:6->6, P=0,
D:36->25, C:0->-2, J:0->-(792/1921)I.

Also differentiate the isotropic endpoint equations in PROOF.md (35),
not a pre-entered determinant table. At x=36/25,y=0,X=1,Y=-1 and the
above h use the exact derivative formulas

    f1_X=1-h X(y+Y)/2, f1_Y=-h(x^2+X^2)/4,
    f2_X=h(y^2+Y^2)/4-5h/[4 sqrt(X)(sqrt(x)+sqrt(X))^2],
    f2_Y=1+hY(x+X)/2,
    f1_x=-1-h x(y+Y)/2, f1_y=f1_Y,
    f2_x=h(y^2+Y^2)/4-5h/[4 sqrt(x)(sqrt(x)+sqrt(X))^2],
    f2_y=-1+hy(x+X)/2.

Compute det(F_out)=1423025/1921^2, det(F_in)=6875/(6*1921) and
their ratio 528275/341526, different from one. Full regularity and the
pullback symplectic-form argument are analytical claims in PROOF.md.

## Eight negative controls

Each control must detect a nonzero exact discrepancy in the indicated
false alternative. The false assertion is never used as a solver input.

1. NC01: n=(1,0,0,0,0), G0, Pi=0. Replacing T/2 by R/2, with
   R=ET-PP^T, incorrectly makes the metric source zero.
2. NC02: empty counts, G0, Pi=G0^-1. Omitting -Pi G Pi from Pidot
   gives nonzero Hdot, computed by the actual directional derivatives.
3. NC03: control-only n=(2,0,0,0,0), G0, Pi=0. An unweighted p dx
   term gives twice the correct occupied velocity. This additional tuple
   is outside and does not change the 32-tuple main box.
4. NC04: empty counts, G0, Pi=[[0,1],[1,0]], deltaG=[[0,1],[1,0]].
   Counting just one shared off-diagonal entry gives half the true
   directional derivative of K: gamma/2 instead of gamma.
5. NC05: the finite witness falsifies separate conservation of E.
6. NC06: the finite witness falsifies preservation of J by DG and hence
   equality with an exact common-action flow segment.
7. NC07: the actual finite Jacobian ratio falsifies canonical symplecticity.
8. NC08: witness H=6 contradicts a free-lapse H=0 constraint; the separately
   declared p_t=-6 instead satisfies p_t+H=0.

## Independent implementations and byte protocol

verify.py and breaker.py are written by separate isolated authors who may
read this contract and PROOF.md but neither the companion implementation
nor predecessor scientific programs. Both are Python standard-library-only,
self-contained exact implementations. Primary uses rational-pair field
arithmetic and direct triangular coefficient recursion (FLOW coefficient
m is vector-field coefficient m-1 divided by m; DG uses endpoint coefficient
m-1). Breaker uses an independently written field implementation and four
formal Picard passes for each method. Distinct root algorithms are required:
primary binomial expansions, breaker root-square and inverse recurrences.
No common scientific module or imported scientific predecessor is allowed.

Each builds the following ASCII/LF payload in memory and hashes it, without
writing it. An F scalar a+b phi serializes as a,b, with each rational in
Python Fraction string form (integer or reduced numerator/positive
denominator). Flatten matrices row-major and vectors in index order, and
separate scalar rational components by commas. Thus an F matrix has eight
rational components; a vector has four; all five positions have twenty.
ntext is the five digits without commas. Each payload record ends in LF.

The eight state fields, in order, are:

    G (8), Pi (8), X (20), K (2), E (2), D (2), C (2), J (8).

Record order and literal prefixes:

    G|<G0>|<u0,...,u4>
    B|<index>|<initial Pi>                 # seven, index 0..6
    C|<ntext>|<index>|<sum n>|<P>|<D0>    # case header
    S|<ntext>|<index>|FLOW|<m>|<eight state fields>
    S|<ntext>|<index>|DG|<m>|<eight state fields>

For each main case emit its C header, all FLOW degrees m=0..4, then all
DG degrees m=0..4, before the next case. Main cases are count-outer and
momentum-index-inner. After all main cases emit each covariance case:

    A|<c>|<ntext>|<index>|<A>|<all transformed p>
    Y|<c>|FLOW|<m>|<eight state fields>
    Y|<c>|DG|<m>|<eight state fields>

Again emit all five FLOW rows then all five DG rows. Finally emit

    W|1100/1921
    F|0|<eight old endpoint state fields>
    F|1|<eight new endpoint state fields>
    R|DG_J_DEFECT|<DeltaJ>|<det F_out>|<det F_in>|<det ratio>
    N|NC01|DETECTED
    ... through N|NC08|DETECTED.

The three determinants in R use F scalar encoding, including zero phi
component. The record count is 1+7+224*11+6*11+4+8=2550. All reported
counts are derived and checked, not merely printed constants. The common
15-line certificate is exactly

    CERTIFICATE=P-RELATIONAL-MASS-JOINT-ACTION-1
    AUTHORITY_FILES=5
    COUNT_PREPARATIONS=32
    MOMENTUM_CASES=7
    TRAJECTORY_CASES=224
    FORMAL_ORDER=4
    FLOW_COEFFICIENTS=1120
    DG_COEFFICIENTS=1120
    COVARIANCE_CASES=6
    COVARIANCE_METHODS=2
    FINITE_EXCHANGE_CASES=1
    NEGATIVE_CONTROLS=8
    PAYLOAD_RECORDS=2550
    PAYLOAD_SHA256=<computed lower-case SHA-256>
    CERTIFICATE_RESULT=PASS

breaker.py writes only this certificate on success. verify.py independently
computes it, then invokes breaker.py with the same interpreter, -I, no shell,
a 540-second subprocess timeout and deterministic environment. It requires
exit zero, empty stderr and raw certificate byte identity before writing
its own certificate followed by

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

The primary outer budget is 600 seconds. Neither implementation reads
EXPECTED.txt, RUN.md, result text, a frozen expected digest, network,
environment secrets or external scientific data. The only scientific
runtime file reads are the five authority files below; the primary also
launches its pinned breaker. Importing or reading the companion program
as a source of scientific values is forbidden.

## Authority checks, failures and systematics

Both programs verify the following exact byte counts and SHA-256 values
before producing scientific evidence:

    canon/CANON.md 1052518 d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b
    canon/CORE.md 30714 9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728
    canon/FRONTIER.md 27382 8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0
    canon/REGISTRY.tsv 532811 5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d
    canon/CHANGELOG.md 207770 79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078

Failure threshold is one exact discrepancy. Explicit audit failures are
handled with deterministic LF output and exit zero:

    FALSIFIER=<code>
    RESULT=FAIL

Codes: F01_AUTHORITY, F02_GEOMETRY, F03_FLOW, F04_EXCHANGE,
F05_DG, F06_CHARGE, F07_COVARIANCE, F08_WITNESS,
F09_NEGATIVE_CONTROL, F10_PAYLOAD, F11_BREAKER.
Use the first failing check in deterministic program order. A breaker
failure, nonzero exit, stderr, timeout or certificate mismatch is
F11_BREAKER in a completed primary run. No unexpected exception is
converted into a scientific result; an incomplete primary run is handled
as an abandoned pin under POLICY, without EXPECTED.txt or RUN.md.

Finite domain, field ordering, off-diagonal multiplicity, weighted canonical
pairs, absent groups, formal truncation, endpoint versus local branch,
FLOW versus DG, and inverse versus covariant metric are explicit systematics.
No observed outcome may change the fixture, equation, threshold, domain,
program, expected defect or physical scope after the pin.

## Pin, execution and disposition

Before any scientific execution, import or fixture evaluation, commit and
push exactly PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py and
FROZEN.sha256. The manifest contains the five other file hashes. Read back
all six complete public files at that immutable commit and post a public
receipt with commit, byte counts and hashes; read back that receipt before
the first run. Source inspection, AST parsing, analytical derivation and
byte/hash checks are permitted beforehand. No scientific dry run is allowed.

Run from the repository root:

    python3 probes/P-RELATIONAL-MASS-JOINT-ACTION-1/verify.py

Use LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0,
TZ=UTC. Record neutral platform/architecture/Python, exact command,
preregistration commit, start/end, exit, stdout/stderr byte counts and hashes.
After a completed run add EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md and
README.md. Retain completed FAIL unchanged. An incomplete pin consumes this
identifier and must be explicitly abandoned, not repaired or resumed.

The public result requires byte-identical replay on the required x86_64 and
aarch64 jobs of one PR head, passing policy/Canon/ledger/gate checks and
security review. Merge only with preserved pin ancestry. No probe outcome
promotes Canon; a later separately declared fold is required.
