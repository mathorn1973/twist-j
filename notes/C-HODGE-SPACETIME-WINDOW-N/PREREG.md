# C-HODGE-SPACETIME-WINDOW-N: preregistration

Status: PUBLIC NON-CANONICAL incubation. No Canon authority.
Owner: A. M. Thorn / hodge-spacetime-window-20260927; issue #1229.
Date: 2026-09-27. Basis: Public Canon v92, main
5daf8df697dc480227d7db5fe2c678f48c14040d.
Scope: MULTI mathematical L1/L2/L5 construction with the explicit candidate
bridges below. No physical realization, native-U identification or L6 claim.

## 1. Inherited source and exact marking

Lambda=Lambda^2 A4 is Z^6 in the ordered wedge basis of
(e0-e4,...,e3-e4). W_F=Lambda tensor F, F=Q(sqrt5), sqrt5>0.
Retain the five-cycle C, L=Lambda^2(I+C^2), K^2=5I, wedge form beta,
and fixed-J predictive E=E_+ from J-HODGE-HERM2-LOXODROME [T].
J-HODGE-RATIONAL-CLOSURE and J-HODGE-SEMILINEAR-MEMORY are inherited
at their exact registered scope. E has dimension four and g=beta|E has
signature (3,1). Write i for its inclusion and

    Pi=i g^-1 i^T beta,     N=I-Pi,      A=L|E.

The predecessor notes/C-HODGE-RANK4-SEAM-CANONICITY-N/PROOF.md establishes
the direct projection relative to the chosen E, and is reproduced rather
than promoted. Its different rank-four images in Lambda^2 E are NOT reused.

Freeze the executable matrix anchor
probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py,
SHA-256 02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9.
Freeze the photon finite-certificate anchor
probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1/verify.py,
SHA-256 3eecf0a389d084db9bc986a792adde247b54f23b405f82e2cf97730ea9e0b23e.
Normative authority remains the registered current rows, not an old wording
inside their immutable evidence. No formal-verifier rerun changes a status.

## 2. Exact event selection: an added definition

E_R is the real scalar extension at the declared embedding, regarded as an
affine vector space with origin zero and difference form g. Let t be the
fourth column of the frozen E basis (the nonzero negative Hodge cross column).
Its sign is the declared future orientation, not forced by J. Put

    c_t=-beta(t,t)>0,
    tau(x)=beta(t,x)/beta(t,t),
    spatial(x)=x-tau(x)t,
    |spatial(x)|_t^2=beta(spatial(x),spatial(x))/c_t,
    ||x||_*=max(|tau(x)|, |spatial(x)|_t).

This positive auxiliary norm is for approximation and counting, not a second
spacetime metric. Literal equality in E_R is the equality of events.
For an integral w, all event membership and causal sign decisions reduce to
ordered F arithmetic, represented by pairs of rationals.

Freeze the internal window rule before computation:

    c0=max{-beta(N e,N e): e in {+1/2,-1/2}^6},
    Window={y in im N: -beta(y,y)<=c0},
    M={Pi w: w in Lambda and Nw in Window}.

The ball and this marking-dependent covering normalization are additional
selection data. They are not claimed unique, forced by J, physical apparatus,
Born selection, or a physical probability. A different admitted window is a
different construction, not a silently equivalent one.

G1: Prove Pi is injective on W_Q and hence Lambda, despite real rank four.
Consequently the unwindowed rank-six subgroup Pi Lambda is not locally finite
in E_R. Do not describe the projection as erasing two integer labels.

G2: Prove c0>0, Window compact, and the selected M uniformly discrete and
relatively dense. Derive a covering constant by coordinate rounding:

    R_t=(1/2)sum_j |tau(Pi e_j)|,
    R_s2=max{|spatial(Pi e)|_t^2: e in {+1/2,-1/2}^6},
    R=R_t+R_s2+1.

For every x in E_R and positive integer h, round h*x in the original six
coordinates (ties toward +infinity). The resulting w is admitted and
||Pi w/h-x||_*<=R/h. Prove separation by lattice compactness and rational
injectivity, not by sampled minimum spacing. Prove A M=M and Q M=M for
Q=Lambda^2 C restricted to E. No entire Lorentz-group invariance of M is
asserted. No normalized counting density is claimed.

## 3. Candidate bridge C-GATE-L1-L2-HODGE-EVENT-GEOMETRY

Source: (Lambda,beta,L,K,E,t,Window), exactly as above.
Target: (E_R,g,M_h,preceq_h) for all integers h>=1, with M_h=M/h.
Map: Pi and the window formula; event equality is literal E_R equality.
Define x preceq y iff tau(y-x)>=0 and g(y-x,y-x)<=0.

G3: Prove this is a partial order, every causal interval on M_h is finite,
and A preserves the order and the event set. Prove the stated R/h geometric
approximation, closed-limit preservation of causal pairs, eventual agreement
for fixed strictly timelike or spacelike pairs under convergent rounding,
and approximation of every null pair by causal pairs after O(R/h) timelike
padding. Freeze padding of the first endpoint by -3R t/h and the second by
+3R t/h, followed by rounding. The endpoints have ||.||_* error <=4R/h.
Prove order R^4 point-count growth in expanding auxiliary balls and in
homothetically expanding nonempty timelike diamonds, using packing/covering.
This is a geometric/order limit, not a limit of fields, states or measures.

This is a mathematical candidate-D selection with candidate-T consequences.
It is NOT a registered public gate and does not close any public owner.

## 4. Time step versus Lorentz action

G4: Test the identification of x -> A x with causal time advancement.
Use the rational hyperbolic plane

    T=ker(L^2-3L+I).

Construct a future timelike primitive integral u in T by exact rational
basis selection and indefinite binary-form completion of the square.
Test g((A-I)u,(A-I)u)=-g(u,u)>0. This would refute that particular
identification while leaving the Lorentz action and event geometry intact.

Candidate bridge C-GATE-L1-L5-HODGE-CUMULATIVE-CLOCK:
source is an additional retained integral seed u in T, selected as above;
state consists of (n,w_n,v_n) with w_0=0,v_0=u and

    (n,w_n,v_n) -> (n+1,w_n+v_n,L v_n),
    X_n=Pi w_n.

Literal full-sequence equality; no quotient or implicit auxiliary state.
This is a different declared mathematical history, NOT native Omega,U.
G5: Prove all X_n belong to M, the increments are future timelike with
constant squared proper length ell^2=-beta(u,u), and accumulated polygonal
proper time is n*ell (counter n in units ell). The counter clock is a
normalization of this chosen path, not METRO-TICK or an SI realization.
Prove the endpoint squared interval is

    -g(X_n,X_n)=ell^2(a_n-2),
    a_0=2, a_1=3, a_(n+2)=3a_(n+1)-a_n.

This distinguishes accumulated proper length from the endpoint interval.

## 5. Candidate bridge C-GATE-L2-L5-HODGE-PHOTON-LOCAL

The source of the independent photon symbol is exactly the already selected
D3 model in PHOTON-SPATIAL-TEMPORAL-TRANSFER [D], with shells of squared
norms 2,4,8,10,16, weights 6,1,15,1,1 and scale 1/324. The inherited
PHOTON-TEMPORAL-CHARACTERISTIC [T] supplies its actual roots and bound

    0 <= r^2-s(epsilon*k)/epsilon^2 <= (11/27)epsilon^2 r^4,
    r=|k|.

Freeze the complete coframe class: all real linear isometries
F:E_R^* -> R x R^3 such that

    -g^-1(xi,xi)=Omega^2-|k|^2,   (Omega,k)=F xi.

Existence is a consequence of the fixed Lorentz signature, not a unique
physical dictionary. Fixing any one member defines a comparison. The
rational finite-event algorithm never needs this real coframe.
No coframe is selected by matching a target measurement.

G6: For epsilon*r<=1, define the principal positive frequency
Omega_epsilon(k)=(2/epsilon)asin(sqrt(s(epsilon*k))/2).
Prove directly from monotone roots, NOT from function convergence alone,

    -(11/27)epsilon^2*r^3 <= Omega_epsilon(k)-r
                                <= (1/12)epsilon^2*r^3.

Use asin(z)-z<=z^3/3 on 0<=z<=1/2 with its explicit derivative proof.
The lower sheet is its negative. Conclude graph convergence, with error
<= (11/27)epsilon^2 Rk^3 on r<=Rk, of these two principal lifted null sheets
to the dual Hodge null cone in any fixed admitted coframe.

This is a LOCAL comparison of the independently selected D3 propagation law.
It is not an exact global torus-vector map, full spectral/state convergence,
physical photon, polarization, phase, propagator or complete coframe class
for physical readings. GATE-L4-L5-PHOTON-GLOBAL-CARRIER and
PHOTON-MASSLESS-PHASE remain unchanged.

## 6. Prospective executable audit and scope limits

Commit this file and verify.py and publicly read back before execution.
The standard-library verifier checks the source hashes; reproduces the
accepted Hodge matrices; checks the projector, Q/L invariance and rational
rank; computes the complete 64-vertex window/cover constants; checks exact
rounding on 81 source points at h=1,2,5,10; constructs the integral timelike
seed and checks the first 40 cumulative steps; and independently reconstructs
the photon shell moments and checks selected rational principal-sheet brackets
using rigorous rational Taylor intervals for cosine. No floating point,
heuristic sign test or numerical asymptotic extrapolation is allowed.
Universal geometry, order, counting and limit statements rest on PROOF.md.

Known mathematical background: cut-and-project sets with compact internal
windows. No external theorem is required for the intended packing/covering
proof; any background citation will be marked as such, not as an imported
TWIST-J conclusion. No third-party code or dataset is imported.

A second execution is reproduction. A same-session alternative calculation
is not a blind second agent. Ordinary notes-only repository CI does not itself
execute this verifier. Actual architecture runs must be separately recorded.

Any exact failure fires its own scoped mathematical clause. Runtime or
integrity failure is STOP and must not be reported as mathematical success.
The time-advance test may close negative while the selected event geometry
closes positive. These are distinct predicates, not a moved threshold.
No prior sealed probe, public negative or input marking is altered.
Only this new notes directory may be added. No Canon/Registry/Frontier,
GATES.tsv, existing notes, tools, workflows, releases or physical status changes.
