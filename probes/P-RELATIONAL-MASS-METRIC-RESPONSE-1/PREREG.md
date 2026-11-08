# Relational mass and metric response

Status: PROSPECTIVE
Scope: NON-CANONICAL, NEW_DECLARED L1, exact five-direction count carrier
Owner: A. M. Thorn, session relational-mass-metric-response-2026-10-20
Ownership: https://github.com/mathorn1973/twist-j/issues/1684
Base: 5f20429944b409d912202d141e158fdfec145c41

## 1. Question, custody and action layer

Extend the supplied C-RELATIONAL-MASS-1 algebra to a declared active inverse
metric variation, holding covectors and integer counts fixed. Distinguish
the derivative of energy from the derivative of mass squared. Determine
their ranks, the complete first response in cyclotomic data, concavity and
its equality cases, and the obstruction to reusing the old quadratic
scalar-lapse completion. PROOF.md supplies universal arguments; this audit
checks finite exact formulas and controls, not physical admission.

Publish and read back PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py
and FROZEN.sha256 before any new scientific execution, import or fixture
evaluation. Only analytical derivation, source review, AST parsing and byte
checks precede that receipt. No frozen file is repaired. A completed FAIL
is retained; an unexpected incomplete runtime follows POLICY's abandoned
pin route. The outcome-exposed reference package is a source of definitions,
not a public pin or an independent physical measurement. Its programs are
neither read by the new code authors nor imported or executed here.

This is one NEW_DECLARED L1 mathematical carrier. The inverse metric,
fixed-covector convention and energy functional below are explicit new
choices. No native U realization, physical metric, local source projector,
volume convention, h-to-G map, common nonlinear action, physical clock,
Lorentz closure, localized particle, SI calibration or cross-layer lift is
claimed. No existing Canon, registry, workflow or predecessor file changes.

## 2. Definitions and universal claims

K=Q(j), j^5=1, Phi5(j)=0, conjugation c(j)=j^4, sigma(j)=j^2.
F=Q(phi), phi=-j^2-j^3, phi^2=phi+1, with real place phi>1.
tau(phi)=1-phi and Re(z)=(z+c(z))/2. Counts n_k are nonnegative integers.
N=sum n_k, Z=sum n_k j^k, W=sum n_k j^(2k)=sigma(Z),
D=N^2-Z c(Z), Q=N W-Z^2. The equality W=sigma(Z) uses rational counts;
it is not an asserted operation on arbitrary real weights or noisy data.

For exact planar coordinates use basis (1,j), t=phi-1, columns

    u0=(1,0), u1=(0,1), u2=(-1,t), u3=(-t,-t), u4=(t,-1),
    G0=[[1,t/2],[t/2,1]], det G0=(2+phi)/4.

Then u_k^T G0 u_k=1. In this basis a real positive definite symmetric
inverse metric G acts on these fixed covector components. Set

    eps_k=sqrt(u_k^T G u_k)>0,
    E=sum n_k eps_k, P=sum n_k u_k,
    D_G=E^2-P^T G P,
    T_G=sum (n_k/eps_k) u_k u_k^T,
    R_G=E T_G-P P^T.

For a symmetric strain H, the Frobenius convention is

    dE[H]=tr(T_G H)/2, dD_G[H]=tr(R_G H).

Thus off-diagonal entries contribute twice to the trace pairing.
T_G/2 is the chosen energy derivative; R_G is a different derivative.
With w_k=n_k eps_k and v_k=u_k/eps_k,

    R_G=sum_(r<s) w_r w_s (v_r-v_s)(v_r-v_s)^T >=0,
    tr(G R_G)=D_G, tr(G T_G)=E.

For occupied support size s, rank T_G is 0,1,2 for s=0,s=1,s>=2;
rank R_G is 0,1,2 for s<=1,s=2,s>=3. D_G is concave and homogeneous
of degree one on the positive metric cone. For beta_k=u_k^T H u_k/eps_k^2,

    d^2 D_G[H,H]=-sum_(r<s)n_r n_s eps_r eps_s
                                (beta_r-beta_s)^2/2.

For s<=1 this vanishes for every H; for s=2 exactly when the two betas
agree; for s>=3 exactly when H=cG. These are real-metric theorems; the
finite audit below is at G0 with exact formal perturbations.

At G0 write T=sum n u u^T and R=N T-P P^T. For alpha in F, beta in K
define the symmetric strain H_(alpha,beta) by

    z^T H z = alpha |z|^2 + Re(beta z^2), z=x+yj,
    H00=alpha+Re(beta), H11=alpha+Re(beta j^2),
    H01=H10=alpha*t/2+Re(beta j).

Here the left expression denotes the coordinate quadratic form in (x,y).
The exact responses and determinants are

    dE[H]=(alpha N+Re(beta W))/2,
    dD[H]=alpha D+Re(beta Q),
    4 det(G0) det(T)=tau(D),
    4 det(G0) det(R)=D^2-Q c(Q).

The first determinant identifies the other arithmetic place with a tensor
invariant of this same preparation. It does not identify two particles or
two inertial frames. Marked rotations preserve N and both places of D but
can change directional responses; rotating source and metric together is
covariance, not a physical discrepancy.

If Z=z0+z1*j+z2*j^2+z3*j^3 in the integral basis, reconstruct
r=(N-z0-z1-z2-z3)/5 and n=(z0+r,z1+r,z2+r,z3+r,r).
Admission means r integral and every entry nonnegative. Thus (N,Z)
determines the full count preparation. Adding h whole pentagons at fixed Z
adds 5h to N and (5h/2)G0^-1 to T, leaving W unchanged. Z=0 holds exactly
for equal counts, so rest preparations inside this marked class are whole
pentagons. This does not provide Lorentz closure of the marked carrier.

Along G0+epsilon H let a_k=u_k^T H u_k. The formal energy coefficient

    [epsilon^4] E = -5 sum n_k a_k^4 /128

is negative iff some occupied a_k is nonzero; otherwise E is constant on
that line. Every nontrivial affine-metric energy coupling therefore leaves
the old homogeneous quadratic class. Its exact transfer and Ward closure
cannot be inherited merely by replacing the old scalar source variable.

## 3. Arithmetic, strains and fixed audit domain

Both programs use only standard-library exact arithmetic. Field elements
are serialized uniquely as a+b*phi with rational a,b; cyclotomic elements
as four rational coefficients in (1,j,j^2,j^3). Internally the primary
uses direct real-quadratic matrix moments and binomial series; the breaker
uses a separately implemented arithmetic path, pair forms and a square-root
coefficient recurrence. Neither author may read companion or predecessor
scientific source. No floats, finite nonzero exponential or finite nonzero
square-root evaluation. Exact signs use phi=(1+sqrt5)/2 algebraically.

Strains in order s=0,1,2,3 are H(alpha,beta) for

    (1,0), (0,1), (0,j), (1,2-j).

Thus H3=H0+2H1-H2. H0,H1,H2 form a basis of symmetric matrices over F.
Define a_(s,k)=u_k^T H_s u_k. Formal degree is 4, coefficients 0..4.
The primary derives sqrt(1+a epsilon) by exact binomial coefficients;
the breaker derives b0=1, b1=a/2 and
b_m=-sum_(i=1)^(m-1)b_i*b_(m-i)/2 for m=2..4.

Enumerate all 3125 tuples n in {0,1,2,3,4}^5 in Python product order,
n0 outermost and n4 innermost. For every tuple:

1. Derive N,Z,W,P,T,R,D from definitions. Check W=sigma(Z), the matrix
   and cyclotomic norms, reconstruction of all five counts, zero-momentum
   iff equal counts, R's pair-difference formula, trace pairings, both
   determinant identities and the rank laws. Check T and R are positive
   semidefinite by exact diagonal signs and determinant signs, not by a
   predicted rank alone. Count all three rank classes independently.
2. Compute the 3x3 Hessian B in basis H0,H1,H2 from actual weighted
   moments and compare to the pair form, for all i,j=0..2:

       B_ij=((sum n a_i)(sum n a_j)-N sum n a_i a_j)/2
           =-sum_(r<s)n_r n_s(a_(i,r)-a_(i,s))
                                  (a_(j,r)-a_(j,s))/2.

   Require the H0 row/column zero, negative semidefinite 2x2 remaining
   block by exact principal signs, and ranks 0,1,2 for support<=1,2,>=3.
3. For each of four strains calculate the actual E series and actual D
   series through degree4. Primary uses E^2-P^T(G0+epsilon H)P; breaker
   independently derives D by the unordered-pair formula

       sum_(r<q)2 n_r n_q [sqrt((1+a_r epsilon)(1+a_q epsilon))
                                 -u_r^T(G0+epsilon H)u_q].

   Both may cross-check the alternate formula but must calculate every
   coefficient, never substitute predicted zeros. Require E0=N,D0=D;
   E1 and D1 equal both matrix and cyclotomic response formulas. Require
   D2=direction^T B direction/2 (directions e0,e1,e2,(1,2,-1)), and the
   pair formula -sum n_r n_q(a_r-a_q)^2/4. Require D2<=0 and its stated
   equality criterion; for occupied>=3, equality iff all five a values
   equal (H proportional to G0). Require E4=-5 sum n a^4/128 and its
   strictness iff some occupied a is nonzero.

Expected rank counts: T=(1,20,3104); R=(21,160,2944);
B=(21,160,2944). Rest tuples:5 including the empty tuple.
These are audit counts, not assertions that the finite box proves a theorem.

Separately check eight fixed-J preparations h=0,...,7:
n=(1+h,h,1+h,h,h). Compute N,Z,W,D,T,R directly, require Z=1+j^2,
N=2+5h,D=2+phi+20h+25h^2, W unchanged and
T_h=T_0+(5h/2)G0^-1. Require R_h=N_h T_h-P_0 P_0^T.

Check the five rotations r=0,...,4 of the unit pair with occupied indices
r and r+2 modulo5. Compute all records directly. Require N=2,D=2+phi,
tau(D)=3-phi, Z_r=j^r Z_0,W_r=j^(2r)W_0,Q_r=j^(2r)Q_0,
Q_0=(1-j^2)^2, and pairwise distinct Q and R. Multiplication by j has
coordinate matrix C=[[0,-1],[1,t]]; require C^T G0 C=G0 and verify
P_r=C^r P_0,T_r=C^r T_0(C^r)^T,R_r=C^r R_0(C^r)^T.

## 4. Eight actual negative controls

All controls use these fixed cases; no case is selected after inspection.

NC01: single ray n=(1,0,0,0,0), H0. False identification of energy and
      mass-square derivatives: actual E1=1/2, D1=0.
NC02: primitive pair n=(1,0,1,0,0), H1. Substitute W=Z in E1; require
      the false value differs from the actual energy derivative.
NC03: same primitive pair. Omit -PP^T from R; require the actual matrix
      residual is nonzero.
NC04: collapse all five rotated pairs to a source determined only by
      scalar (N,D,tau(D)); these scalars agree but actual R matrices differ.
NC05: identify the h=0 and h=1 fixed-J preparations; actual T differs
      by (5/2)G0^-1 although Z and W agree.
NC06: same primitive pair, explicitly Hcross=[[0,1],[1,0]]. Compute
      actual E1=sum n_k(u_k^T Hcross u_k)/2. A false off-diagonal
      pairing using T01/2 rather than T01 differs from actual E1.
NC07: same primitive pair, H1. Mistake the coefficient D2 for the
      second derivative: D2 differs from the actual B11=2*D2.
NC08: single ray, H0. Assume the responding energy is quadratic;
      its actual fourth coefficient -5/128 is nonzero.

## 5. Canonical payload and certificate

ASCII, LF after every record, no normalization. Rational values use
Fraction.__str__. An F scalar serializes as a,b; an F array flattens the
two coefficients of each element in row-major order with commas. A K
scalar serializes as its four rational coefficients with commas.

Payload records in order:

    G|<G0 as 8 rationals>|<u0,...,u4 as 20 rationals>
    B|s|<H_s as 8 rationals>|<a_s,0,...,a_s,4 as 10 rationals>  s=0..3

For each count tuple in product order, let ntext be its five comma-separated
integers. Emit one C followed by four S records:

    C|ntext|N|<Z as 4>|<W as 4>|<D as 2>|<T as 8>|<R as 8>|<B as 18>|rT,rR,rB
    S|ntext|s|<E coefficients0..4 as 10>|<D coefficients0..4 as 10> s=0..3

Then for h=0..7 and r=0..4 respectively:

    F|h|N|<Z as 4>|<W as 4>|<D as 2>|<T as 8>|<R as 8>
    O|r|<Z as 4>|<W as 4>|<D as 2>|<Q as 4>|<T as 8>|<R as 8>

Finally N|NC01|DETECTED through NC08 in order. Total records15651.
PAYLOAD_SHA256 hashes these exact concatenated records. Neither program
writes or reads a payload file. Certificate lines in this exact order:

    CERTIFICATE=P-RELATIONAL-MASS-METRIC-RESPONSE-1
    AUTHORITY_FILES=5
    COUNT_CASES=3125
    STRAIN_DIRECTIONS=4
    SERIES_ORDER=4
    SERIES_CASES=12500
    ENERGY_RANK_COUNTS=1,20,3104
    MASS_RESPONSE_RANK_COUNTS=21,160,2944
    HESSIAN_RANK_COUNTS=21,160,2944
    REST_CASES=5
    FIBER_CASES=8
    ROTATION_CASES=5
    NEGATIVE_CONTROLS=8
    PAYLOAD_RECORDS=15651
    PAYLOAD_SHA256=<computed lowercase SHA-256>
    CERTIFICATE_RESULT=PASS

Primary runs the frozen sibling breaker with the same interpreter and -I,
timeout540 seconds, no shell. Require exit0, empty stderr, and raw identical
certificate bytes; append BREAKER_RAW_BYTES=IDENTICAL and RESULT=PASS with
LF. Enclosing limit600 seconds. No companion or predecessor source reads,
no EXPECTED reads, no file writes, no network, no nondeterministic inputs.
The only authority reads are the five normative files frozen in SOURCE.md.

Completed scientific failures emit a declared code and RESULT=FAIL, exit0:
F_AUTHORITY (normative bytes), F_GEOMETRY (field, basis, strains), F_RESPONSE
(moments, derivatives, determinants), F_RANK (ranks/signs), F_HESSIAN
(moment/pair matrix, kernel, concavity), F_SERIES (actual coefficients),
F_FIBER (reconstruction/fixed-J/rest), F_ROTATION (covariance or ambiguity),
F_CONTROL (missed declared defect), F_COUNTS, or F_BYTES (breaker mismatch).
Unexpected incomplete execution uses the abandoned-pin route, never a
scientific PASS. No post-pin threshold, file, fixture or output repair.

After public readback and the first completed execution add exactly
EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md and README.md. Required x86_64
and aarch64 jobs replay unchanged programs against the same exact stdout.
