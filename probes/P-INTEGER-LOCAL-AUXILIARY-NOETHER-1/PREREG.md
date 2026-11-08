# P-INTEGER-LOCAL-AUXILIARY-NOETHER-1

Status: PROSPECTIVE
Scope: NON-CANONICAL, NEW_DECLARED L1, context a=0 only
Owner: A. M. Thorn, session integer-local-auxiliary-2026-10-20
Ownership: https://github.com/mathorn1973/twist-j/issues/1663

## 1. Question and custody

Construct a horizon-uniform temporally local second-order completion of the
inherited Noether system by transforming its existing constrained auxiliary
fields. Keep delta0 and delta1 and the carrier unchanged. Separately test
the raw commutator and a local skew correction which preserves the Ward
identity and is predicted to cancel that commutator through second order.

Authority is Public Canon v103. Base main is
8e1f6538a09c8ef012a0a9971d501119f13d52ee, which adds only unrelated notes
to the canon-v103 tag dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.
Both programs check all five normative hashes/sizes frozen in SOURCE.md.
The direct predecessor is #1662 at cb8d6e894b909cd1c7ab3a1a0338431f8d453226;
its field-only obstruction is preserved. The separately owned prospective
local-parent #1659 is not taken over or presumed to have completed a run.

This is analytically exposed, proof-first work. All formulas and witnesses
are fixed before either program is executed or imported. Only source reads,
AST parsing and byte hashing precede the public six-file pin and readback.
No numerical tolerance, floating-point arithmetic, observational fit or
post-run fixture change is admitted. Only Q and Z arithmetic is used.

## 2. Complete inherited definitions

T>=3; x_n=(h_n,chi_n) in Q^6, n=0,...,T. Every rational endpoint pair is
admitted; endpoints are held fixed during variations. There are five
vertices r=0,...,4, with e=(1,1,1,1,1), ell=(1,-1,0,0,0),
sigma=(1/2,1/2,0,0,0), and g=1/324. Edges e=r point r->r+1 mod5 with
weight29/324; edges e=5+r point r->r+2 mod5 with weight65/324.
B is head minus tail incidence, W is diagonal edge weight, L=B^T W B:

    (324Lh)_r=188h_r-29(h_(r-1)+h_(r+1))-65(h_(r-2)+h_(r+2)).

Pi0 v=v-mean(v)e. Define Lplus=(L+ee^T/5)^-1-ee^T/5, so
L Lplus=Lplus L=Pi0 and Lplus e=0. The finite five-site spatial inverse is
explicitly allowed. No large-spatial-lattice locality claim is made.

For b=1,...,T, alpha_b is scalar and lambda_b,tau_b lie in e^perp.
For n=1,...,T-1, N_n is a ten-vector and p_n lies in ker B^T.
M=(alpha,lambda,N). Every coordinate is rational. Put

    V=[[L,-g ell],[-g ell^T,1]], C=I_6-V/2,
    A=1/2 sum_b ||x_b-x_(b-1)||^2-1/2 sum_(n=1)^(T-1) x_n^T V x_n,
    f_n=DA_n=2C x_n-x_(n-1)-x_(n+1), R_n=-f_n.

In expressions acting only on interior coordinates set f_0=f_T=0. These
are endpoint tangent conventions, not endpoint Euler-Lagrange equations.

Define q_n=x_(n+1)-x_(n-1). Bond vertex density and edge current are

    e_b(r)=(h_b(r)-h_(b-1)(r))^2/2
      +1/4 sum_(edge incident r) w_edge (Bh_b)_edge(Bh_(b-1))_edge
      +sigma_r[(chi_b-chi_(b-1))^2/2+chi_b chi_(b-1)/2]
      -(g/2)ell_r[chi_(b-1)h_b(r)+chi_b h_(b-1)(r)],
    H_b=sum_r e_b(r)
       =1/2(||x_b||^2+||x_(b-1)||^2)-x_(b-1)^T C x_b,
    j_n(edge)=w_edge(Bh_n)_edge[q_h,n(tail)+q_h,n(head)]/4
       -(g/4)q_chi,n[h_n(0)+h_n(1)]delta_(edge,0),
    Baux=2 sum_b lambda_b^T L tau_b
       +2 sum_n N_n^T[WB(tau_(n+1)-tau_n)+p_n],
    S0=A+Baux,
    I=-sum_b alpha_b H_b-sum_b lambda_b^T e_b+sum_n N_n^T j_n.

The field-constant E_hom is set to zero; no forcing a!=0 is included.
For endpoint-zero psi_n in Q^5, set

    Gamma(psi)_alpha,b=mean(psi_b-psi_(b-1)),
    Gamma(psi)_lambda,b=Pi0(psi_b-psi_(b-1)),
    Gamma(psi)_N,n=B psi_n,
    (G_psi x)_h,n=psi_n*q_h,n/2,
    (G_psi x)_chi,n=(sigma dot psi_n)q_chi,n/2.

G has zero endpoint values. delta0 changes only M by Gamma(psi);
delta1 changes only x by G_psi x. Products of vertex arrays are componentwise.
The known lower-order identities are delta0 S0=0 and
delta0 I+delta1 S0=0; both are rechecked here.

## 3. Proposed local second-order completion

Define, on interior slices, Z_n=Lplus B^T W N_n, Q_n=N_n-BZ_n;
set Z_0=Z_T=0. For each bond l_b=lambda_b-Z_b+Z_(b-1). Put

    P=I_10-WB Lplus B^T,
    Ires=I(x;(alpha,l,Q)), w=G_Z x,
    K_b=(C x_b-x_(b-1)) dot (x_b-C x_(b-1)),
    S2hom=1/2 sum_b alpha_b^2 K_b,
    S2=-D_x Ires[w]+1/2 Hess_A(w,w)+S2hom.             (1)

Q is in ker(B^T W), NOT in general ker B^T. P maps edges into ker B^T;
P^T Q=Q. The decomposition is exactly

    Baux=2 sum_b l_b^T L tau_b+2 sum_n Q_n^T p_n.

Under delta0, Z changes by Pi0 psi, while l,Q are invariant.

Let t_n=mean psi_n and U=G_(t e)x. Define the raw second-order variation

    Xhom_n=t_n/2[alpha_(n+1)(x_n-Cx_(n+1))
                         -alpha_n(x_n-Cx_(n-1))],
    Xraw=G_Z G_psi x-G_(t e)G_Z x+Xhom,
    F_b=1/2 Lplus Pi0 D_x e_b[U],
    J_n=-1/2 P D_x j_n[U].                            (2)

All field variations vanish at the endpoints. F is a mean-zero vertex
direction and B^T J=0. Raw delta2 changes x,tau,p by Xraw,F,J and leaves
every multiplier unchanged.

The adjusted variation adds a skew Euler-gradient term. On interior time
slices define the scalar skew matrix A_t(alpha) with only nearest entries

    (A_t)_(n,n+1)=alpha_(n+1)(t_n+t_(n+1))/8,
    (A_t)_(n+1,n)=-(A_t)_(n,n+1),
    Xadj=Xraw+A_t f.                                 (3)

The matrix acts identically on each of six field coordinates. Equivalent
row formula:

    (A_t f)_n=[alpha_(n+1)(t_n+t_(n+1))f_(n+1)
                  -alpha_n(t_(n-1)+t_n)f_(n-1)]/8.

Endpoint f values are zero as specified above. Adjusted delta2 changes
x,tau,p by Xadj,F,J and still has delta2 M=0.

Analytic predictions, on the FULL off-shell declared state space, are

    delta0 S2+delta1 I+delta2_raw S0=0,
    DA dot (A_t f)=0,
    delta0 S2+delta1 I+delta2_adj S0=0.                (4)

S2 is homogeneous quadratic in independent multipliers. Every mixed
multiplier Hessian entry with time-label separation greater than one is
zero identically. Labels are b for alpha_b,lambda_b and n for N_n.
Field and parameter stencils are bounded independently of T; field
dependencies reach at most two slices from a central current slice.
No temporal prefix or inverse of a horizon-sized matrix is used.

## 4. Commutator, adjustment and exact scope

Let D_psi=delta0_psi+epsilon delta1_psi+epsilon^2 delta2_psi.
Use the vector-field convention [D_psi,D_eta]=D_psi D_eta-D_eta D_psi,
so the field coefficient at epsilon^2 is

    G_eta G_psi x-G_psi G_eta x
      +D_M X2_eta[Gamma(psi)]-D_M X2_psi[Gamma(eta)].   (5)

For s_n=mean eta_n, the raw coefficient is predicted to be

    Craw_n=1/4[(s_n t_(n+1)-t_n s_(n+1))R_(n+1)
             +(s_n t_(n-1)-t_n s_(n-1))R_(n-1)].      (6)

Endpoint residual terms are omitted. All other component coefficients
through epsilon^2 vanish. Craw is a skew matrix times the Euler gradient,
so it preserves A and vanishes on shell, but need not vanish off shell.
The skew adjustment (3) is predicted to cancel (6) identically: the adjusted
generators commute off shell through epsilon^2, for arbitrary psi,eta.

Fixed raw nonclosure witness: T=4, x_3=(1,0,-1,0,0,0), every other x=0;
M=tau=p=0; psi_1=e and eta_2=e, other parameters zero. The raw field
commutator is -x_3/4 at slice1 and zero elsewhere. The adjustment cancels it;
reversing the adjustment sign leaves twice that raw witness.

The construction proves only the displayed coefficients through order2.
It neither asserts exact finite-epsilon invariance nor solves orders3+.
It is formally related through order2 to scalar-lapse autonomous mechanics
plus algebraic auxiliary pairs; no new nonlinear gravitational bulk law is
inferred. No physical clock, native-U realization, metric selection or
cross-layer lift is claimed.

## 5. Frozen finite audit and rational fixtures

Horizons T=(3,4,5,7), ascending. For each use seeds q=(1,2,3), ascending:
12 dense off-shell states. Coordinates are zero-indexed. Define

    z(q,n,r)=(((q+2)(n+1)(r+3)+(n-r)^2) mod17-8)/(q+2).

For every n=0,...,T set x_n[r]=z(q,n,r), r=0,...,5. For b=1,...,T:
alpha_b=z(q,b,6), lambda_b=Pi0(z(q,b,7+r))_(r=0..4),
tau_b=Pi0(z(q+1,b,12+r))_(r=0..4).
For n=1,...,T-1 set N_n[e]=z(q,n,17+e), e=0,...,9;
p_n=Pcyc (z(q+1,n,27+e))_(e=0..9), where
Pcyc=I-B B^T/5. This last equality uses B^T B=5Pi0 for the complete
five-vertex graph. Padding coordinates outside these declared ranges are zero.

For each state, parameter list: the 5(T-1) interior coordinate unit psi,
ordered by time n then vertex r, followed by one dense parameter
psi_n[r]=z(q+2,n,37+r) at interior n, zero at endpoints.
This gives 237 state/parameter cases. For commutators pair every such psi
with eta_n[r]=z(q+3,n,42+r), with zero endpoints, giving 237 pairs.

Both programs independently implement the full definitions. Primary uses
exact central polynomial differences for action/interaction derivatives,
quadratic polarization and multiplier-direction differences. The breaker
uses exact dual arithmetic and an independently assembled quadratic action
Hessian. Neither imports or reads companion or earlier probe code.

For each state check authority, density-sum equality to matrix H, matrix
inverse/projection identities, decomposition and all carrier constraints.
For each parameter check both lower-order identities, raw and adjusted
second-order Ward identities, the scalar-only Ward identity, zero skew
work, admissibility of every generated tangent, and actual raw/adjusted
commutators against (6)/zero. Compute the commutator from (5) using the
actual transformations, not from its predicted residual formula alone.
Auxiliary order2 commutator components must be checked as well.

For every Ward case let D be the least common denominator of the eight
scalar terms in the W payload below. Multiply each by D, check integrality,
and check both second-order sums vanish as integer sums. Count one integer
Ward record per parameter case (237). This is exact denominator clearing,
not a claim of bounded precision or native integer dynamics.

Locality audit: T=5,q=1, x as above, tau=p=0, expand S2 at M=0 in the 65
independent multiplier basis directions. Order: all alpha_b (b ascending),
then all lambda_b=e_r-e_4 (b ascending, r=0..3), then all N_(n,e)
(n ascending, e=0..9). For every pair i<j with time-label separation>1,
evaluate S2(E_i+E_j)-S2(E_i)-S2(E_j), using the actual formula (1), and
require zero. Exactly 900 distant pairs. This audit supports, but does not
replace, the universal stencil proof. Cache single-basis evaluations freely.

## 6. Eight negative controls and falsifiers

NC01: omit S2, leaving delta1 I+delta2_adj S0.
NC02: omit the tau variation F from delta2.
NC03: omit the p variation J from delta2.
NC04: reverse the tau variation F.
NC05: reverse S2hom in S2, keeping all transformations.
NC06: replace the full S2 by S2hom, keeping all transformations.
Each of NC01-NC06 must produce a nonzero second-order residual in at least
one member of the complete fixed 237-case audit. Do not add cases afterward.
NC07: omit the skew adjustment, detecting the exact raw commutator witness
of Section4, rather than calling raw nonclosure a failure of the Ward identity.
NC08: reverse the skew adjustment, detecting exactly twice the raw witness.
Positive cancellation checks are not members of the negative-control set.

F_AUTHORITY: any normative byte length/hash differs.
F_CARRIER: any matrix, decomposition, density or tangent constraint fails.
F_LOWER: either lower-order Noether identity fails.
F_SCALAR: the scalar-lapse second-order identity fails.
F_WARD: either full raw or adjusted second-order identity fails.
F_SKEW: the skew correction does nonzero work on A.
F_BRACKET: raw commutator differs from (6), adjusted is nonzero, or an
           auxiliary/multiplier coefficient through order2 is nonzero.
F_LOCALITY: any distant multiplier coefficient is nonzero.
F_INTEGER: denominator-cleared terms are not integral or Ward sums nonzero.
F_CONTROL: any of the eight intended defects is undetected.
F_COUNTS: any case count differs from the contract.
F_BYTES: certificates differ as raw bytes, subprocess exit is nonzero,
         stderr is nonempty, or the fixed subprocess timeout is reached.

A completed scientific failure emits its F_* and RESULT=FAIL and is kept
unchanged. An unexpected execution error whose gate never completes is
disposed under POLICY's abandoned-pin procedure. No frozen repair is allowed.

## 7. Canonical payload and certificate bytes

All fractions use Fraction.__str__, integer when denominator1. ASCII and
LF only. Lists are comma-separated without whitespace. Each record ends LF.
For each (T,q) in the order above append:

    S|T|q|A|Baux|I|S2

For each parameter index i append in order:

    W|T|q|i|delta0S0|delta0I|delta1S0|delta0S2|delta1I|delta2rawS0|delta2adjS0|skewwork
    G|T|q|i|flattened adjusted (X,F,J)
    B|T|q|i|flattened raw field commutator

Flatten X and bracket by n=0,...,T then six coordinates h0,...,h4,chi;
then F by b=1,...,T and vertex0,...,4; then J by n=1,...,T-1 and edge0,...,9.
After all states append locality records in lexicographic basis-pair order:

    L|i|j|mixed-coefficient

Then append E|RAW|<flattened raw field witness> and
E|ADJUSTED|<flattened adjusted field witness>, then N|NC01|DETECTED through
N|NC08|DETECTED. SHA-256 covers concatenation of all records exactly.

Both implementations emit precisely this certificate with computed digest:

    CERTIFICATE=P-INTEGER-LOCAL-AUXILIARY-NOETHER-1
    AUTHORITY_FILES=5
    OFF_SHELL_STATES=12
    LOWER_ORDER_CASES=237
    SCALAR_WARD_CASES=237
    RAW_WARD_CASES=237
    ADJUSTED_WARD_CASES=237
    SKEW_WORK_CASES=237
    TANGENT_CASES=237
    COMMUTATOR_PAIRS=237
    DISTANT_MULTIPLIER_PAIRS=900
    INTEGER_WARD_CASES=237
    RAW_WITNESS=-1/4,0,1/4,0,0,0
    ADJUSTED_WITNESS=0,0,0,0,0,0
    PAYLOAD_SHA256=<lowercase computed digest>
    NEGATIVE_CONTROLS=8
    CERTIFICATE_RESULT=PASS

Primary executes breaker.py with the same interpreter and -I, timeout540s,
requires exit0, empty stderr and identical unmodified certificate bytes,
then appends BREAKER_RAW_BYTES=IDENTICAL and RESULT=PASS, each with LF.
The enclosing repository runner's 600-second limit remains authoritative.

## 8. Publication and boundaries

Freeze PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py and FROZEN.sha256
in one public commit; the manifest lists the other five. Read back every
file and post the pin receipt before any scientific execution/import.
After the first run add EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md, README.md.
Required two-architecture replay uses unchanged scientific bytes.

The positive theorem, if proved and audited, is conditional candidate-T at
NON-CANONICAL L1. Finite arithmetic is recorded at its actual scope. No
claim excludes other action classes; no new physical gravity law is inferred.
The old #1662 hypothesis was deliberately relaxed and its result is preserved.
