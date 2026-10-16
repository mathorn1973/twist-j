# Fixed receivers: a late two-write construction and the origin-zero boundary

Status: PUBLIC-content, NON-CANONICAL, candidate-T, L1.
Author: A. M. Thorn. Original text and code: Apache-2.0.
No scientific authority, physical subsystem selection or Canon change.
All calculations below are in F5 unless stated otherwise.

## 1. Source, notation and exact dynamics

The authoritative basis is public main
8b91a935c426036e00ecb300019fd94734addeec, Public Canon v101.
The original generator definitions are in
probes/P-U-NATIVE-MEMORY-EVENT-1/verify.py. That probe's MEMORY-PROOF.md
and CLOCK-PROOF.md supply the recurrent-support theorem used only where
explicitly named below. No prior verifier is imported or executed here.

Write x=(a,u,c,v,q,r)=(p1,p4,p1p,p4p,q,r), z=sum(x),
theta_n=popcount(n) mod 2 and T_t(x)=g_(z+2t)(x). The generators are

    g0(x)=(u,a,v,c,q,r),
    g1(x)=(-c,-v,-a,-u,-q,-r),
    g2(x)=(2-c,1-v+r,2-a,1-u-r,1-q,-r),
    g3(x)=(2-a,1-u,3-c,4-v,1-q,1-r),
    g4(x)=(2-a,1-u,3-c,4-v,2-q,1-r).

All six coordinates are retained. Define

    A=a+c, B=u+v, C=a-c-2, D=u-v-1,
    Sigma=q+r, w=q-r, H=Sigma+3(A-B).

The two fixed coordinate decompositions are

    Rbar=(u,v,Sigma), Sbar=(a,c,w),
    Rtilde=(D,H),     Stilde=(a,c,B,w).

The first has inverse q=3(Sigma+w), r=3(Sigma-w).
For the second recover

    u=3(B+D+1), v=3(B-D-1),
    Sigma=H-3(A-B), q=3(Sigma+w), r=3(Sigma-w).

These are global affine bijections of F5^6. They declare different
subsystem classes. H uses the original source sum A; replacing Rbar by
Rtilde is not permission to access that sum through an already frozen
physical Rbar-only interface. Neither split is claimed spatially local.

## 2. The complete exposed late-start construction

Prepare the following 25 states once, at absolute native time n=5:

    x5(lambda,mu)=(lambda,0,2-lambda,0,-1-mu,mu-1).

The original Rbar is (0,0,3) and Rtilde is (4,4), independently of BOTH
messages. No input-dependent receiver preparation is hidden in the chart.
The actual bits at n=5,6,7,8 are 0,0,1,1. The actual generators are
respectively g0,g0,g2,g4. Direct substitution yields

    x6=(0,lambda,0,2-lambda,-1-mu,mu-1),
    x7=x5,
    x8=(lambda,mu,2-lambda,2-mu,mu+2,1-mu),
    x9=(2-lambda,1-mu,1+lambda,2+mu,-mu,mu).

The corresponding Rtilde values are

    n=5: (4,4),
    n=6: (2lambda+2,2),
    n=7: (4,4),
    n=8: (2mu+2,3),
    n=9: (3-2mu,0).

Define one total fixed reader G:F5^2 -> {BLANK} disjoint-union PRESENT(F5):

    H=0       -> PRESENT(4-3D),
    H=2 or 3  -> PRESENT(4-2D),
    H=1 or 4  -> BLANK.

Its five displayed outputs are BLANK, PRESENT(lambda), BLANK,
PRESENT(mu), PRESENT(mu). This includes lambda=0 and mu=0.
At n=7 the ENTIRE receiver, not merely its output label, equals its
initial state. Indeed the entire original cell x7=x5 at this boundary;
the autonomous state (n,x) has not returned because the counter changed.

For comparison the user's total Rbar-only reader uses Z=2B+Sigma:

    B=2 and Sigma=3                  -> PRESENT(u),
    B in {2,3} and Z in {1,4}         -> PRESENT(4-BZD),
    otherwise                        -> BLANK.

The first two branches are disjoint: the first forces Z=2.
At n=5,...,9 it gives the same labels. This remains a different fixed
interface, not a silent switch from the pair to a larger receiver.

## 3. An exact closed tail, not a long-run conjecture

At n=9, A=B=3, z=1 and

    A z C=2-lambda, B z D=4-mu.

On the synchronized sector M=X1 union X4, the actual selected operations
have the following effects. g1 negates A,B,z and preserves C,D;
selected g3 or g4 negate A,B,C,D and preserve z. Thus

    A=B, B in {2,3}, z in {1,4},
    A z C=2-lambda, B z D=4-mu

are preserved under BOTH control choices. In particular H=Sigma=z-2B.
The four possibilities (B,z,H,Bz) are

    (2,1,2,2), (2,4,0,3), (3,1,0,3), (3,4,3,2).

Therefore G(D,H)=PRESENT(4-BzD)=PRESENT(mu) forever from n=9,
and together with n=8 forever from n=8. The Rbar reader agrees.

A complete closed set for each pair is parameterized by
B in {2,3}, z in {1,4}, r in F5, with

    A=B, C=(2-lambda)/(Az), D=(4-mu)/(Bz),
    a=3(A+C+2), c=3(A-C-2),
    u=3(B+D+1), v=3(B-D-1), q=z-A-B-r.

It contains 20 states per pair and 500 distinct states in all. The proof
requires closure, not an assumption that arbitrary control words are
actual Thue-Morse continuations.

The three-point Rtilde support for a fixed mu is

    {(3-2mu,0), (2mu+2,2), (2mu+2,3)}.

None is the ready point (4,4). Both references Sigma_n and H_n are
message-independent at every common time: initially this follows from
the prefix; in the tail their evolution is fixed by the common B,z.
This is no autonomous closed law for Rtilde through the writing phase.

The first message remains readable for every n>=9 by

    lambda=2-A(2A+Sigma)C=2-A(2A+H)C.

Both persistent readings use the common reference, not disjoint private
reference copies. The first source piston pair is exactly returned at
n=7 and is left unchanged by g2 at n=7. The second source is NOT depleted:
at n=8, r=1-mu and w=2mu+1; at n=9, r=mu. Later source differences in
r change sign but do not vanish at a fixed common time.

For the original bare pair (u,v), the recurrent projection has
B in {2,3} and D in {+(3-2mu),-(3-2mu)}. The identical-support classes
are exactly {0,3}, {1,2}, {4}; the last has two points, the others four.
Full recurrent visitation follows from the inherited actual-clock support
proof: x9 lies on the actual reachable sheet X1 at n=9 and so shares its
future with a synchronized origin-zero chart trajectory. Graph connectivity
alone is not used to infer this visitation.

## 4. The precise two-coordinate minimum

A single F5 coordinate has five states. A total fixed reader from it
cannot take all six different values BLANK and PRESENT(0),...,PRESENT(4).
Thus any coordinate receiver F5^k with this contract has k>=2.
Section 2 attains k=2 with an affine bijection of the complete cell.
This minimizes coordinate count in that declared class, not apparatus
size, energy, physical spatial dimension or cost of acquiring H.
There is no claim that the original Rbar-only interface can be reduced
to Rtilde without changing allowed access.

## 5. Launch windows, reachable states and missing predecessors

The trace actions of g0,...,g4 are z,-z,2-z,2-z,3-z. Hence

    z               0  1  2  3  4
    z after T0      0  4  0  4  4
    z after T1      2  1  1  3  1.

Each restriction to a trace sheet is an affine bijection onto the target
sheet. The origin-zero reachable checkpoint sets are consequently

    D0=F5^6,
    D1=X0 union X4,
    D2=X1 union X2,
    Dn=X_(4+2theta_(n-1)) for n>=3.

For n>=3 the complement has four sheets, including the opposite sheet
inside M, not just the three sheets outside M. That opposite sheet
remains inside M under future U and does not restore a g0 opportunity.

Using theta_(2m)=theta_m and theta_(2m+1)=1-theta_m,

    0011 starts at n
    iff n=2m+1 and (theta_m,theta_(m+1),theta_(m+2))=(1,0,1).

It cannot start at an even n because an aligned pair is complementary.
The first five starts are 5,23,29,39,53, not 5,13,21,29,37.
For every k>=4, n_k=3*2^k+5 is a start: for j=5,6,7,8 there is no binary
carry and theta_(3*2^k+j)=theta_3 xor theta_j=theta_j.

Every such start has theta_(n-1)=theta_(2m)=1. But T1's image omits X0.
Every x5(lambda,mu) has trace zero. Thus (n,x5(lambda,mu)), at ANY of these
launch times, has no immediate predecessor under U. In particular the
n=5 family is not merely missing from the origin-zero image; its inverse
image from n=4 is empty.

Every launch defines a valid separately stipulated initial-value problem
on Omega. These launches are not internally reached reset opportunities
of one running system. The n=5 construction never derives its preparation.

## 6. Complete obstruction for the proposed origin-zero affine contract

Let E be ANY preparation family, without linearity or constant initial trace.
Let R(x)=Lx+h be ANY fixed affine observation, of any rank and any finite
number of F5 coordinates. Let G be ANY fixed total function on its image.
Assume all preparations have a common complete receiver state r_star at n=2.
No source factorization or condition at n=0 or n=1 is needed for this lemma.

From the actual origin-zero bits 0,1,1 and the trace table,

    z0=0 or 2       -> z1=0 -> z2=2 -> z3=1,
    z0=1,3 or 4     -> z1=4 -> z2=1 -> z3=1.

At n=2 the selected generator is g3 on X1 and g4 on X2. Write

    t_d=(2,1,3,4,1,1), t_e=(2,1,3,4,2,1).

Both generators have linear part -I. Therefore, for every preparation,

    R(x3)=-r_star+2h+L t_d, or
    R(x3)=-r_star+2h+L t_e.

There are AT MOST TWO receiver states at n=3, independent of receiver
rank, source encoding, number of preparations, or nonlinearity of G.
Five distinct PRESENT(mu) values at n=3 are impossible. This proves the
proposed 25-pair contract empty for ALL affine receivers, not just a
chosen pair, chosen raw coordinates or enumerated low-rank matrices.
The exact reset condition R(x2)=R(x0)=r_ready implies the common-r_star
hypothesis and hence the result. Retention or the first-message condition
cannot repair a contradiction already present at n=3.

### 6.1 Waiting cannot repair it under permanent nonblank retention

Suppose additionally G(R(x2))=BLANK for all preparations and each orbit
has an eventually constant nonblank output, with any finite onset.
The existing recurrent-support NOWRITE theorem applies to G composed
with R, an arbitrary fixed checkpoint function. If z2=1, x2 is already
synchronized, so eventual constancy would give that same nonblank label
at x2, a contradiction. Hence every admitted preparation has z2=2.

All remaining x2 use g4. Their R(x3) is the SAME value
-r_star+2h+L t_e. Since x3 is synchronized, NOWRITE also says that the
eventual label equals G(R(x3)). It is consequently the SAME label for
every preparation. There is at most ONE possible eventual nonblank message.
No assertion of attainability of that one-message upper bound is needed.
This excludes a nonconstant permanently retained second message even if
its onset is postponed. It remains a fixed-affine-common-reset theorem.

### 6.2 What the negative does and does not decide

The exact origin-zero question posed in PREREG is answered negatively.
Its scope is arbitrary affine R, arbitrary input codes, arbitrary total
reader G, exact common receiver reset at n=2 and unchanged U. The weaker
instantaneous bound uses no recurrent-support theorem. The eventual
strengthening explicitly depends on that already public theorem.

The claim does not cover nonlinear subsystem charts, a merely BLANK
output with different hidden receiver states, added context, new coupling,
external loading, or finite rather than permanent retention. A different
launch time changes the actual generator at the write edge. At n=7 in
the late construction it is g2, which mixes coordinates, whereas the
origin-zero reset at n=2 is followed only by g3 or g4 with linear part -I.
This explains the positive/negative contrast without changing U.

Arbitrary nonlinear coordinate freedom is not a physical solution by
itself; a subsequent class must justify its information access rather
than encode a desired history in a lookup table. This note makes no new
physical selection, energy law, apparatus realization or probability claim.

## 7. Evidence status and promotion boundary

The previous conversation exposed the late-start formulas and mentioned
computational checks. Their old raw run artifacts were not present in
this fresh worktree. This note does not use those statements as evidence.
The fresh audit is frozen and publicly read back before its first execution.
The new origin-zero proof in section 6 was obtained analytically in this
session before the audit, and is disclosed as such, not a blind prediction.

Finite direct-coordinate and same-author affine-matrix checks provide
candidate-C evidence only. All universal statements above have the written
proofs and the explicitly pinned public support premise. A separate agent
has not yet independently reviewed the note. Promotion requires a separate
public audit/fold under repository policy. Canon, old probes and the parallel
funded-device program are unchanged.
