# C-DISCRETE-BOUNDARY-RECONSTRUCTION-N

Status: NON-CANONICAL / NO AUTHORITY. Action layer: L1.
Owner: A. M. Thorn, session discrete-boundary-reconstruction-20261008.
Reservation: https://github.com/mathorn1973/twist-j/issues/1421.
This is a notes-only proof and finite exact audit, not a public probe.

## 1. Authority and exposure

The public basis is main 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc,
Public Canon v100, content a4cc9666662967527abe711441833ff600c00337,
tag canon-v100 at 807dae3fe97dd6a872d5d1305a0133e8e8d856ea.
Canon SHA-256 is
5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4,
980212 bytes. Five normative hashes, ancestry and existing required
architecture/aggregate and publication checks were verified.

Analytical expectations are RESULT-EXPOSED. The prior conversation supplied
the mixed-difference reconstruction formula, the injectivity criterion and
a Gauss cycle witness. The public Maxwell reproduction already records its
whole-torus cycle dimension 17. None is new computational evidence.
No scientific computation for this candidate preceded this preregistration.

The new claims concern literal finite configurations, not physical entropy,
quantum states, spacetime dimension or a geometry derived from original U.
The chosen growing boxes and update below are additional definitions. The
existing Maxwell torus is used with its exact original edge multiplicities.

## 2. General question and equality

Let A=F5, represented by 0,1,2,3,4. Equality is literal coordinate equality.
For a finite set V, B subset V, and nonempty X subset A^V, let R be literal
restriction to B. Test the equivalence between a left inverse D on R(X)
and injectivity of R. For an affine class X={x:H x=b}, test the equivalent
criterion ker(H) intersect ker(R)={0}. No gauge quotient is adopted.

Also test the precise consequence: every map P:X->X with R P=R is the
identity when R is injective. This is a conditional statement about
boundary-fixing operations, not a prohibition of all local dynamics.
For U:X->X and injective R, define U_B=R U D. Prove R U=U_B R and transfer
of bijectivity when U is a bijection. Boundary locality is not asserted.

## 3. Mixed-cube comparison class

For every integer N>=2, V_N={0,...,N-1}^3, in lexicographic (i,j,k) order.
Let B_N be the union i=0 or j=0 or k=0. X_N consists of scalar fields
f:V_N->F5 satisfying, on EVERY unit cube,

    f111-f110-f101-f011+f100+f010+f001-f000=0.

The subscripts are offsets from that unit cube's lower vertex, not global
coordinates. This is H_N f=0; each coefficient is +1 or -1 modulo five.
No periodic identification is made in this class.

The anticipated formula, to prove or refute, is

    f(i,j,k)=f(i,j,0)+f(i,0,k)+f(0,j,k)
             -f(i,0,0)-f(0,j,0)-f(0,0,k)+f(0,0,0).

Test existence and uniqueness for every assignment on the UNION B_N,
including the intersections counted once. The anticipated dimension is
3*N*N-3*N+1, constraint rank (N-1)^3, and common-kernel dimension zero.
The claim is universal in N and must have a written proof; finite checks
do not establish its quantifier. Identify explicitly any dependence on five.

Define the comparison update U_2(f)=2*f, pointwise modulo five, with proposed
inverse U_3(f)=3*f. Test preservation, intertwining and exact reconstruction.
This update is neither original U nor a claimed derivation from J.

## 4. Gauss-only growing-box class

Use the same V_N, but a separate edge-field carrier. The directed edge set
E_N consists of (v,a), a=0,1,2, with v[a]<N-1 and head v+e_a. All edge
labels are independent. Incidence d has -1 at tail and +1 at head.

The outer vertex boundary O_N consists of vertices with ANY coordinate 0
or N-1. The reader Q_N returns EVERY edge value whose edge has at least
one endpoint in O_N, individually, in inherited lexicographic order.
This is stronger than a total boundary flux or the tangential surface
edge data alone. The unobserved edges have both endpoints in
I_N={1,...,N-2}^3. They form the induced nonperiodic interior grid.

For any rho and q with a nonempty fibre

    F(rho,q)={E:d E=rho, Q_N E=q},

classify the whole affine fibre. The anticipated kernel dimension is zero
for N=2, and, for m=N-2>=1,

    k_N=3*m*m*(m-1)-m^3+1=2*m^3-3*m*m+1.

Prove or refute that each nonempty fibre has exactly 5^k_N members. This is
the complete stated Gauss-only class, with no curl, energy, topology-sector,
preparation or native-admission restriction silently added afterwards.

Freeze a concrete N=4 witness: the oriented square through
(1,1,1),(2,1,1),(2,2,1),(1,2,1),(1,1,1). On forward-labelled edges traversed
backwards use -1. Set other edges to zero. Check nonzero support, d c=0,
Q_4 c=0. Compare the complete zero field and c with the same rho=0.

On the zero-charge class use the separately chosen U_2(E)=2*E. Check that
all four phases of this witness remain boundary-invisible and that its
least period is four. This is a specified all-time invisible family under
an explicitly chosen update, not the actual native U or Maxwell time law.

## 5. Public Maxwell torus comparison

Pin the original source at
7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/reproduce/maxwell/verify.py.
For the candidate's fresh audit restate the complete objects here:

    T={0,1}^3;
    E_T={(v,a):v in T,a=0,1,2};
    head(v,a)=v+e_a modulo 2;
    d_T[tail,e]=-1, d_T[head,e]=+1.

There are 24 directed labels, not twelve simple-cube edges. Oppositely
wrapping labels are distinct. Audit the already known rank 7 and kernel
dimension 17 without claiming a new proof of the registered Maxwell result.

Mark R={v:v[0]=0}. Let E_R contain edges with both endpoints in R; let
cut(R) contain edges with exactly one endpoint in R. Define

    Z_R={E:d_T E=0, E vanishes outside E_R}.

Determine its exact dimension and construct its complete basis. Every
member fixes the entire complement and every individual crossing edge.
Also determine the kernel of the full reader (d_T, restriction to cut(R))
on ALL F5^E_T, without the support restriction. These are distinct classes.

A marked nonzero witness is the forward-labelled cycle through
(0,0,0),(0,1,0),(0,1,1),(0,0,1),(0,0,0), using the appropriate wrapping
edges and coefficient +1 at each. Check its divergence, cut data, support
and all four phases under the same comparison U_2.

## 6. Finite audit, independence and frozen output

Use Python standard library and exact integers modulo five only. No random
sampling, floating point, external data, source-verifier imports or hidden
expected-output input. A Python program is not imported or executed before
its pin; syntax compilation and static review are permitted.

Primary verify.py and independent break.py are frozen as separate Git
commits with SHA-256 before EITHER first scientific execution. The breaker
receives only this frozen preregistration and repository operating rules,
not verify.py, PROOF.md, output or an existing scientific implementation.
Its author may choose an independent exact method. Freeze break.py before
implementation comparison. Written proof review is separately identified.

Required finite coverage:

- Mixed-cube N=2,3,4,5,6: actual constraint rank; full rank of stacked
  constraints and face readout; check the reconstruction on EVERY face
  unit basis vector, including cube constraints, boundary readback and
  U_2/U_3. A proved equivalent full linear-map audit is admissible.
- Gauss-box N=2,3,4,5,6,7: explicit graph and reader partitions; actual
  interior incidence rank and COMPLETE kernel basis, independently check
  every basis vector's full divergence and complete observed edge values.
  Check basis independence. Matrix elimination or a proved equivalent
  constructive spanning-tree cycle basis is admissible.
- Both frozen four-edge witnesses, including their complete four-phase
  histories and least period, and the torus complete, restricted-region
  and full-cut kernel dimensions and bases.

Stdout is UTF-8 ASCII, one space between tokens, LF line endings and one
final LF. Both programs use exactly the following order and line formats;
angle-bracket slots are computed integers, not literal text:

    C-DISCRETE-BOUNDARY-RECONSTRUCTION-N exact audit
    STATUS NON-CANONICAL L1
    CUBE N=<N> vertices=<v> face=<b> rank=<r> hidden=<h> basis=<b> update=PASS
    [one CUBE line for each N=2,...,6]
    GAUSS N=<N> vertices=<v> edges=<e> observed=<o> interior=<i> interior_edges=<ie> rank=<r> hidden=<h>
    [one GAUSS line for each N=2,...,7]
    TORUS vertices=8 edges=24 rank=<r> hidden=<h>
    TORUS_REGION vertices=<v> internal_edges=<e> cut_edges=<c> rank=<r> hidden=<h> full_cut_hidden=<f>
    WITNESS BOX_N4 support=<s> divergence=ZERO boundary=ZERO period=<p>
    WITNESS TORUS_REGION support=<s> divergence=ZERO boundary=ZERO period=<p>
    NATIVE_BRIDGE NOT_PROVIDED
    AUDIT PASS

Bracketed explanatory lines are not emitted. A PASS requires actual checks
of every finite obligation, not merely printing the anticipated formulas.
Universal statements, general inverse criterion and physical-scope limits
are proof/review obligations, not established by the AUDIT PASS line.

First runs are sequential from one clean pinned checkout. Freeze a timeout
of 180 seconds per program, with LC_ALL=C, LANG=C, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1, TZ=UTC and Python -I. Record OS, architecture,
Python, code pins/hashes, commands, start times, duration, return code,
stdout/stderr byte counts and hashes. Preserve every first result; never
overwrite a failed transcript. Only matching successful exact outputs may
be copied to EXPECTED.txt. One local architecture remains candidate-C.

## 7. Failure and scope rules

An exact mathematical counterexample fires the corresponding anticipated
claim and is retained. The class, equality, boundary, coefficient field,
size quantifiers and thresholds do not change. Runtime, stale basis,
custody, incomplete output or integrity failure is STOP, not falsification.
Implementation defects require preserved first evidence and a new code pin;
they do not permit changing scientific membership to recover success.

No growth law, quantum recovery, Bekenstein-Hawking coefficient, local
physical operation, entropy measure or SI scale is adopted. The original
Omega=N_0 times F5^6, its counter and state equality are not modified. A
native scalable carrier, region selection, complete reader and actual-U
intertwining are NOT_PROVIDED for this candidate. Missing admission is not
an impossibility theorem about every native reading.

Existing #1288 / PR #1289 owns the prior non-canonical fixed-source capacity
and uniform-radius support statements. This note does not re-earn them and
does not depend on their unmerged proof. The D3 spectrum/transport/energy
lanes #1402, #1404, #1406 and #1410 remain separate. No existing probe,
Canon, registry, frontier, gate, workflow or policy file is changed.

Final packaging is PROMO-C-DISCRETE-BOUNDARY-RECONSTRUCTION-N with explicit
candidate-T proof versus candidate-C finite audit. No public status is
earned or promoted by this notes-only publication.
