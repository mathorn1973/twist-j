# P-INTEGER-SCALAR-LAPSE-RIGIDITY-1

Status: PROSPECTIVE
Scope: NON-CANONICAL, NEW_DECLARED L1, scalar normal-form sector, force a=0
Owner: A. M. Thorn, session integer-scalar-lapse-rigidity-2026-10-20
Ownership: https://github.com/mathorn1973/twist-j/issues/1665

## 1. Question, class and custody

Determine the exact local completion of the scalar normal-form action from
#1664, its rigidity under an exact Ward identity, the boundary of rational
finite-parameter formulas, and its stationary physical content. The scalar
normal form is studied in its own right. This is not an all-order solution
for every original auxiliary coordinate or a nonlinear gravity theory.

Public Canon v103 is active. Base main is
8e1f6538a09c8ef012a0a9971d501119f13d52ee; peeled canon-v103 is
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d and declared content is
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. Normative and administrative
hashes are frozen in SOURCE.md. The direct completed predecessor is
#1664 at d902c2161ae4fa664eb2e57fc905b9aaa8d9f720. The separately owned
#1659 remains prospective and is not resumed or used as completed evidence.

This is analytically exposed, proof-first work. All formulas, examples,
fixtures, controls and output grammar below are fixed before either new
program is executed or imported. Source inspection, AST parsing and byte
hashing alone precede the public six-file pin and readback. No tolerance,
floating point, measured input or post-run fixture repair is admitted.

The rigidity class consists of one common real-analytic, homogeneous
quadratic nearest-bond generating family F_s(q,Q), regular in a connected
neighborhood of s=0, with nonsingular mixed q,Q Hessian, the F_0 and
partial_s F_0 below, independent bond parameters and arbitrary endpoints.
Require an exact all-state Ward identity with delta s_b=t_b-t_(b-1),
t_0=t_T=0, for every T>=3. The accompanying field variation may be
arbitrary but must be finite on every field-stationary history; it fixes
endpoints. There are no further auxiliary variations in this class.
Homogeneity excludes parameter-only additive action terms. A separately
declared +E sum s_b variant is treated explicitly, not silently inserted.
The analytic theorem admits all real field and endpoint coordinates on
its regular charts. The formal theorem and finite arithmetic audit use
rational coefficients and rational fields. Identity on rational samples
alone is not used to infer the analytic all-state premise.
The corresponding regular formal identity is allowed coefficientwise;
in that version the field variation is a regular formal expression for
which the stationary substitutions below are defined. Pointwise finite
but noncomposable field functions are not an admitted formal variation.
Formal stationary histories and endpoints may be substituted because the
identity is algebraic in the unrestricted field coordinates.

## 2. Exact spatial and phase definitions

Fields x_n=(h_n,chi_n) in Q^6, n=0,...,T, T>=3. All rational endpoint
pairs are admitted and held fixed in variations. Vertices r=0,...,4;
e=(1,1,1,1,1), ell=(1,-1,0,0,0), g=1/324. Edges r->r+1 mod5 have
weight29/324 and r->r+2 mod5 weight65/324, with five of each.
With head-minus-tail incidence B_sp and diagonal weights W, set

    L=B_sp^T W B_sp,
    (324Lh)_r=188h_r-29(h_(r-1)+h_(r+1))-65(h_(r-2)+h_(r+2)),
    V=[[L,-g ell],[-g ell^T,1]], C=I_6-V/2, D=I_6-C^2,
    K=[[0,I_6],[-D,0]], M0=[[C,I_6],[-D,C]],
    J=[[0,I_6],[-I_6,0]], G=diag(D,I_6),
    H(q,p)=(p dot p+q^T D q)/2.

K is the phase generator; it is not the predecessor's scalar bond K_b.
The six-vector v=(1,1,1,1,1,0) spans ker D. Its orthogonal complement is
the sector mean(h)=0 with chi unrestricted. Exact proof targets include
positive definiteness of D on this sector and

    trace(D)=163223/52488,
    trace(K^2)=-163223/26244.

The original autonomous action is

    A(x)=1/2 sum_(b=1)^T ||x_b-x_(b-1)||^2
         -1/2 sum_(n=1)^(T-1) x_n^T V x_n.

It equals sum F_0(x_(b-1),x_b) plus the fixed endpoint term
Ebdry=(x_0^T V x_0+x_T^T V x_T)/4, where
F_0(q,Q)=(q^T Cq+Q^T CQ)/2-q dot Q.

## 3. Formal local completion and exact Ward identity

Define the relative flow R(s)=exp(sK) and one-link transfer

    M(s)=M0 R(s)=[[U(s),B(s)],[-D B(s),U(s)]],
    E(s)=B(s)^-1, Acoef(s)=E(s)U(s),
    F_s(q,Q)=(q^T Acoef(s)q+Q^T Acoef(s)Q)/2-q^T E(s)Q.

R(0)=I; M(0)=M0 is not I. Additive composition concerns R, not M.
All formal coefficients are rational; B(0)=I makes its formal inverse
well-defined. The real analytic configuration chart requires det B(s)!=0.
No finite nonzero s value of exp(sK) is computed numerically in this audit.

Let s_b=epsilon alpha_b. Define S(epsilon)=sum_b F_(epsilon alpha_b)
plus Ebdry. Its first four coefficients are A, I, S2, S3:

    H_b=(||q||^2+||Q||^2)/2-q^T C Q,
    K_b=(C Q-q) dot (Q-C q),
    T_b=-q^T(I+2C^2)q-Q^T(I+2C^2)Q+q^T(5C+C^3)Q,
    I=-sum_b alpha_b H_b,
    S2=sum_b alpha_b^2 K_b/2,
    S3=sum_b alpha_b^3 T_b/6.                         (1)

The action is nearest-bond at every formal order. Its multiplier
coefficients are bond-separable, so every mixed derivative between two
distinct alpha coordinates vanishes. This scalar locality claim is not a
claim about the full original auxiliary system.

At interior n, abbreviate E_b=E(s_b), A_b=Acoef(s_b), and put

    pL_n=A_n x_n-E_n x_(n-1),
    pR_n=E_(n+1)x_(n+1)-A_(n+1)x_n,
    f_n=pL_n-pR_n, vmean_n=(pL_n+pR_n)/2.

Set f_0=f_T=0 solely as tangent conventions. For scalar parameters t with
t_0=t_T=0, the raw generator is

    delta alpha_b=t_b-t_(b-1), delta x_n=epsilon t_n vmean_n.

The exact formal/regular analytic identity is delta S=0. It follows from
partial_s F_s=-H of either endpoint phase state and the difference of
the two quadratic momentum energies at an interior vertex.

Define the skew time matrix A_t(alpha), acting identically on six field
coordinates, by upper neighbor entry alpha_(n+1)(t_n+t_(n+1))/8 and its
negative transpose below the diagonal. The adjusted generator adds

    delta x += epsilon^2 A_t(alpha) f(epsilon alpha). (2)

Its action work is exactly zero. It agrees with #1664's adjusted scalar
jet through order two, and its third coefficient is X3nat+A_t f1, where
f1=gradient I and

    X3nat_n=t_n/4 * {
      alpha_n^2[2C x_n-(I+C^2)x_(n-1)]
      +alpha_(n+1)^2[(I+C^2)x_(n+1)-2C x_n]}.

This is an exact Ward extension, not an assertion of exact commutation.

## 4. Commutator and fixed third-order witness

Use [delta_t,delta_s]=delta_t delta_s-delta_s delta_t on coordinates.
For the raw generator the exact field bracket is

    -epsilon^2/4 * {
      (s_n t_(n-1)-t_n s_(n-1)) E_n f_(n-1)
      +(s_n t_(n+1)-t_n s_(n+1)) E_(n+1) f_(n+1)}.   (3)

All lapse brackets vanish. The field bracket is skew times the field
gradient, vanishes on shell, and need not vanish off shell.

Fixed witness: T=4; x_3=u=(1,0,-1,0,0,0), all other x=0;
alpha_3=1, all other alpha=0; t_1=1, s_2=1, other parameters zero.
Actual derivatives of the generators, not the prediction (3) alone, must
give the following entire field arrays:

    raw degree2:      slice1=-u/4, every other slice zero;
    adjusted degree2: every slice zero;
    raw degree3:      slice1=C u/4, every other slice zero;
    adjusted degree3: slice1=-C u/8, every other slice zero.             (4)

The adjusted degree3 slice is exactly
(-395/5184,0,395/5184,-1/144,1/144,-1/5184).
This falsifies commutation for extension (2), not for all possible further
corrections. The predecessor's degree2 commutation result is preserved.

## 5. Rigidity, rational comparison and stationary content

The universal proof target is that the class in Section1 forces
M'(s)=K M(s), hence M(s)=exp(sK)M0 and F_s as above. On arbitrary
field-stationary histories, the exact Ward identity forces adjacent link
parameter derivatives to agree at every common phase point. Setting one
parameter to zero fixes the generating Hamiltonian to H. The two-jet
alone does not force this conclusion.

A rational-function matrix solution to M'=KM has no finite poles and is
therefore polynomial. Its Taylor coefficients would force K nilpotent;
the nonzero trace(K^2) excludes that. Thus no rational-function F_s in
this regular nearest-bond class satisfies the exact fixed-lapse Ward
identity. This does not exclude rational formal series, discrete integer
clocks, nonadditive parameterizations, additional parameters or auxiliaries,
nonquadratic actions, other Ward laws, or general relativity.

For comparison define the exact rational Cayley family

    Rc(s)=(I-sK/2)^-1(I+sK/2), Mc(s)=M0 Rc(s),
    Ecden=I+s^2 D/4, Nc=I+s C-s^2 D/4,
    Bc=Nc Ecden^-1,
    Uc=(C-sD-s^2 C D/4) Ecden^-1,
    Ecoef=Ecden Nc^-1,
    Acoef_c=(C-sD-s^2 C D/4) Nc^-1.                  (5)

Its generating action uses Acoef_c,Ecoef in the same quadratic formula.
It is symplectic, preserves H, commutes with M0, and agrees with the
exponential action through order two. It does not give an additive scalar
flow. The free uniform mode forces a putative composition of Rc(1) with
Rc(1) to have parameter2, while Rc(1)^2 != Rc(2). The infinitesimal
generator is K diag((I+s^2D/4)^-1,(I+s^2D/4)^-1), not K.

Frozen stationary Cayley Ward counterexample: T=3; bond parameters
(1,0,0). At vertex1 choose phase z1=(q=0,p=e_chi), where e_chi is the
sixth coordinate unit. Set z0=Mc(1)^-1 z1, z2=M0 z1, z3=M0 z2, and use
their q components as the fields. All interior field gradients must vanish.
For t1=1 and other t=0, compute the actual parameter derivative of the
Cayley action. It must equal

    [1-e_chi^T (I+D/4)^-1 e_chi]/2 > 0.             (6)

This is a concrete failure of the fixed scalar-lapse Ward premise despite
exact energy preservation, not merely failure of one guessed field variation.

On the exponential regular charts, stationarity of internal fields matches
momenta and yields z_T=M0^T exp((sum_b s_b)K)z0. Distribution of lapses
does not alter this endpoint transfer at fixed total lapse. M0 is not
asserted to equal exp(tau K) for a single scalar tau. Variation of lapses
in S gives H=0; in the explicitly different action S+E sum s_b it gives
H=E. Since D is positive away from the uniform mode, E=0 leaves only
static uniform h and chi=p=0; in the mean-zero sector it leaves the zero
state. This statement is about this stationary scalar completion, not
the predecessor's unrestricted off-shell identities or all gravity models.
The positivity conclusion concerns real or rational states, not complex
states. Arbitrary endpoint pairs remain allowed off shell; most pairs
have no zero-energy stationary history.

Both exp and Cayley have a configuration-chart singularity at s=-1:
B(-1)v=Bc(-1)v=0 on the uniform mode. The phase transfers remain
invertible. A global type-1 configuration chart is not claimed.

## 6. Frozen exact finite audit

Both new programs independently derive all matrices and coefficients from
the definitions above; neither imports or reads another scientific program.
Primary uses matrix-power series and rational matrix calculus. Breaker uses
independently assembled phase matrices, coefficient recurrences and dual
derivatives. Finite audit order is N=6 throughout. No exponential is
evaluated at a finite nonzero parameter.

1. Check all five normative files against SOURCE.md. Derive L from the
   ten edges and compare with its explicit circulant. Check symmetry,
   M0^T J M0=J, M0^T G M0=G, [M0,K]=0, the two frozen traces, and
   Dv=0. Prove positivity computationally by exact positive LDL pivots
   of Hbasis^T D Hbasis, with columns e_r-e_4 for r=0..3 followed by
   e_chi; require all five pivots positive. This complements the universal
   elementary bound in PROOF.md.
2. Compute R_j=K^j/j!, M_j=M0 R_j, U_j,B_j for j=0..6; invert B as a
   formal series and obtain E_j,Acoef_j. Check all seven coefficients
   of R^T J R=J and R^T G R=G. Check all 28 pairs i,j>=0,i+j<=6 in
   R_i R_j=binomial(i+j,i)R_(i+j). Check U^2+D B^2=I and the six
   derivative coefficients E'=-Acoef E, Acoef'=-E^2, using actual series.
3. For T=(3,4,5), each seed q=(1,2), ascending, define

       z(q,n,r)=(((q+2)(n+1)(r+3)+(n-r)^2) mod17-8)/(q+2),
       x_n[r]=z(q,n,r), r=0..5, n=0..T,
       alpha_b=z(q,b,6), b=1..T.

   There are six off-shell states and 24 bonds total. At each bond check
   the four unscaled action coefficients j=0..3 against (1), including
   F0. Also check the whole S0 equals A including Ebdry. For each state,
   use t equal to each interior coordinate unit (time ascending), then
   dense t_n=z(q+2,n,7), endpoints zero. This gives 24 parameter cases.
   Differentiate actual S coefficients with respect to alpha; compute raw
   and adjusted field work by coefficient convolution with the actual
   gradient and generator. Require both Ward sums zero at degrees0..6,
   and zero skew work. Check first three raw/adjusted generator coefficients
   against Section3 and #1664's Xhom and A_t f0. For each degree1..6
   clear the least common denominator of the three scalar terms
   (parameter work, raw field work, adjusted field work), require integral
   values and both Ward sums zero. Exactly144 integer coefficient cases.
4. At T=5,q=1, compute actual action series for alpha=0, the five unit
   alpha directions, and their pairwise sums. For all ten i<j and each
   degree2..6 require S_j(e_i+e_j)-S_j(e_i)-S_j(e_j)+S_j(0)=0:
   50 mixed coefficients. This does not replace the all-order locality proof.
5. For s=(-1/2,0,1/2,1,2), compute Rc and Mc by exact rational matrix
   inversion. Check symplecticity, H preservation, inverse Rc(-s), and
   commutation with M0. Compare their upper blocks with (5). Check the
   three formal Cayley generating coefficients j=0,1,2 equal those of
   the exponential. Require Rc(1)^2-Rc(2) nonzero, and that the free
   phase mode gives the forced candidate parameter2. Evaluate (6) from
   actual Cayley action derivatives on the stationary history, not only
   from the displayed prediction. Require both field gradients zero and
   the residual exactly the displayed positive rational value.
6. Start z0=(q=0,p=u), u=(1,0,-1,0,0,0), and compute z_n=M0^n z0,
   n=0..8. Check H=1 at all nine states. Check the uniform static phase
   (q=v,p=0) is fixed by M0 and annihilated by K. Check singularity
   Bc(-1)v=0 by its actual rational blocks; the exponential uniform
   block is exactly 1+s because K^2 annihilates the free phase plane.
7. Compute actual field commutators at degrees2 and3 for the fixed witness
   (4), differentiating the generators in alpha and x. Do not substitute
   only their predicted bracket formula. Require the entire four arrays
   in (4), including zero endpoints, exactly. This is one bracket witness.

## 7. Eight controls and failure handling

NC01: omit S2 while retaining generators; the degree2 Ward residual must
      be nonzero in at least one of the fixed 24 parameter cases.
NC02: omit S3 while retaining generators; the degree3 Ward residual must
      be nonzero in at least one fixed case.
NC03: reverse the lower-left sign of K, retaining the same G; the
      coefficient K_wrong^T G+G K_wrong must be a nonzero matrix.
NC04: pretend the Cayley clock is additive; Rc(1)^2-Rc(2) must be nonzero.
NC05: pretend the Cayley action satisfies the fixed-lapse Ward premise;
      the stationary residual (6) must be nonzero.
NC06: omit the skew correction; the degree2 raw witness must be nonzero.
NC07: extend degree2 commutation to degree3 for (2); its actual adjusted
      degree3 witness must be nonzero with exactly the value (4).
NC08: omit +E sum s from the E=1 prepared variant; its lapse constraint
      residual is -H=-1 on z0, while the correctly retained variant is zero.

No cases or thresholds may be added after the pin. F_AUTHORITY denotes
changed normative bytes; F_CARRIER a wrong matrix, trace, phase constraint
or positive pivot; F_SERIES a wrong formal identity; F_JET a wrong action
or generator coefficient; F_WARD a failed raw/adjusted identity; F_LOCALITY
a nonzero mixed coefficient; F_RATIONAL a wrong Cayley identity or expected
counterexample; F_STATIONARY a wrong stationary history, energy or chart
witness; F_BRACKET a wrong actual bracket array; F_INTEGER failed exact
denominator clearing; F_CONTROL a missed deliberate defect; F_COUNTS wrong
case counts; F_BYTES unequal raw certificates or failed breaker execution.

A completed scientific failure emits its F_* followed by RESULT=FAIL and
exits0; preserve it. An unexpected runtime error whose gate never completes
uses POLICY's abandoned-pin route. No frozen scientific file is repaired.

## 8. Canonical payload and certificate

ASCII, Fraction.__str__, comma-separated fractions, row-major matrices,
LF after every record, no normalization. For an array of field vectors
flatten n=0..T then coordinate0..5. Append records in this exact order:

    P|<five LDL pivots>
    R|j|<flatten R_j>                   j=0..6
    E|j|<flatten E_j>                   j=0..6
    A|j|<flatten Acoef_j>               j=0..6

For each (T,q), in the order of Section6, append

    S|T|q|<seven action coefficients j=0..6>

then for each parameter index i (zero based) append

    W|T|q|i|<seven parameter-work coefficients>|<seven raw field-work coefficients>|<seven adjusted field-work coefficients>

After all six states, append mixed coefficients by i<j (zero based unit
bond indices0..4), then degree k=2..6:

    L|i|j|k|mixed

Then append Cayley records in the five-parameter order above:

    C|s|<flatten Rc(s)>|<flatten Mc(s)>

Then

    CW|<Cayley stationary Ward residual>
    EN|n|<flatten phase (q then p)>|H    n=0..8
    B|RAW2|<entire field witness>
    B|ADJUSTED2|<entire field witness>
    B|RAW3|<entire field witness>
    B|ADJUSTED3|<entire field witness>
    N|NC01|DETECTED                    through NC08, ascending

PAYLOAD_SHA256 is the SHA-256 of the concatenated exact records. Both
programs emit exactly these certificate lines, with computed digest:

    CERTIFICATE=P-INTEGER-SCALAR-LAPSE-RIGIDITY-1
    AUTHORITY_FILES=5
    SERIES_ORDER=6
    SERIES_COEFFICIENTS=7
    COMPOSITION_PAIRS=28
    POSITIVE_PIVOTS=5
    OFF_SHELL_STATES=6
    BOND_JETS=24
    WARD_PARAMETER_CASES=24
    INTEGER_WARD_COEFFICIENTS=144
    MIXED_LAPSE_COEFFICIENTS=50
    CAYLEY_PARAMETERS=5
    POSITIVE_ENERGY_STATES=9
    COMMUTATOR_WITNESSES=1
    CUBIC_ADJUSTED_WITNESS=-395/5184,0,395/5184,-1/144,1/144,-1/5184
    PAYLOAD_SHA256=<computed lowercase digest>
    NEGATIVE_CONTROLS=8
    CERTIFICATE_RESULT=PASS

Primary runs breaker.py with the same interpreter and -I, timeout540s,
requires exit0, empty stderr and identical unmodified certificate bytes,
then appends BREAKER_RAW_BYTES=IDENTICAL and RESULT=PASS, each LF. The
enclosing repository limit is600s.

## 9. Publication and limits

Freeze PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py and FROZEN.sha256
in one public commit. The manifest lists the other five. Read back every
file and publish a receipt before scientific execution/import. After the
first run add EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md and README.md.
Required architecture replay uses the unchanged scientific files.

Universal conclusions rest on the proof; the finite audit checks formulas,
examples, controls and implementation agreement. Candidate-T is conditional
and NON-CANONICAL; no Canon promotion occurs. The rational-function
obstruction is not a ban on integer physics. The positive formal result
does not provide finite rational values, a global configuration chart,
all-order commuting adjusted generators, new gravitational bulk dynamics,
physical preparation, native-U implementation, metric selection or any
cross-layer lift.
