# Finite-precision seam readout and an exact mixture obstruction

**NON-CANONICAL, L1. C-JM-SEAM-READOUT-COST-N.**
Analytical implications: candidate-T. Finite audit: candidate-C only if RUN.json
records exit zero and empty stderr. This is provisional continuation of
C-JM-ORIENTED-QUADRATIC-READING-N, not dependent on its promotion or an
independent review. No Born occurrence or physical apparatus is derived.

## 1. The complete source class and the declared reference

Keep S=O5 x Z[M] and its index-41 suborder R from the predecessor. Use the
ambient integral cyclotomic coordinates (a0,...,a3,b0,...,b3), not the power
basis. This is a coordinate description, NOT enlargement of the source to
O5 x O8: membership in S still requires b1-b2-b3=0 modulo 3. Indeed the
silver power-basis matrix is

    BM = [[1,1,0,-5],[0,1,2,0],[0,1,3,5],[0,0,2,7]],

with determinant -3, and the displayed congruence kills all its columns.
The seam is the additional congruence ell z=0 modulo41, where

    ell=(1,10,18,16,-1,-27,-32,-3).

The selected trace form in these coordinates is

    G=diag(5I4-ones4,4I4),
    q(z)=5 sum(a_i^2)-(sum a_i)^2+4 sum(b_i^2).

Since (sum a_i)^2<=4 sum a_i^2, one has G>=I8; also G<=5I8.
For each integer Q>=8 freeze the entire finite preparation class

    B_Q={z in S:0<q(z)<=Q}.

Both seam labels occur already at Q=8. There are at most
(2 floor(sqrt(Q))+1)^8 candidates before filtering. No favorable finite
sample substitutes for this complete class.

Supply one explicit reference coordinate y_z=(1,z) and
Ghat=diag(1,G). Put A_z=1+q(z) and

    rho_z=y_z y_z^T Ghat/A_z.

This is a positive Ghat-self-adjoint rank-one projector with trace one.
The reference and the trace form are premises. q is not declared physical
energy, and the source is not the original native U carrier.

## 2. Forty-five fixed binary contexts with small rational coefficients

Before inspecting any seam label choose

    V={e_i:0<=i<9} union {e_i+e_j:0<=i<j<9}.

There are 45 vectors. For each v use the binary context (P_v,I-P_v),

    P_v=v v^T Ghat/(v^T Ghat v),
    p_v(z)=tr(rho_z P_v)
          =(v^T Ghat y_z)^2/[(v^T Ghat v) A_z].

The unnormalized denominators v^T Ghat v are exactly from
{1,4,5,6,8}. Numerator matrix entries are integers of absolute value at
most 4. Thus coefficients are fixed and uniformly small; their precision
is not allowed to hide a Q-dependent classifier.

All P_v are positive self-adjoint idempotents, and their complements are
positive. These are mathematical measurement effects in an explicitly
adopted Born comparison model, not constructed physical devices.

Exact reconstruction is possible even using the 17 contexts e_i and e0+e_i.
Write p0=p_e0 and d_i=Ghat_ii. For 1<=i<9,

    t_i=[(1+d_i)p_(e0+ei)-p0-d_i p_ei]/(2p0)
       =(Gz)_i.

Then z=G^-1 t and q=1/p0-1. No actual source coordinates or actual q are
supplied to the reader. They are recoverable from the assumed exact means.
The theorem below uses all 45 contexts for a uniform stability bound; it
claims no minimum setting count.

## 3. A complete lower bound for pure preparations

For two different integer vectors z,w in B_Q put y=(1,z),u=(1,w),
A=1+q(z), B=1+q(w), and c=1+b(z,w). Their pure-projector trace distance D
obeys

    D^2=1-c^2/(AB).

This identity follows from the two nonzero eigenvalues of their difference,
which are +D and -D after transforming to an orthonormal real chart.
This proof chart does not add square roots to the arithmetic implementation.

There is an exact lower bound:

    AB-c^2=q(z-w)+q(z)q(w)-b(z,w)^2
           >=q(z-w)>=sum_i(z_i-w_i)^2>=1.

Consequently D>=1/(Q+1). The integer separation is indispensable here.

Let delta=max_v |p_v(z)-p_v(w)|, and set

    Y=y y^T/A-u u^T/B,
    Bmat=Ghat Y Ghat.

From the e_i contexts, |Bmat_ii|<=Ghat_ii delta<=4delta. From e_i+e_j,

    |2Bmat_ij| <=[(e_i+e_j)^T Ghat(e_i+e_j)
                  +Ghat_ii+Ghat_jj]delta<=16delta.

Thus every entry has absolute value at most8delta and
||Bmat||_F<=72delta. Since Ghat>=I,

    sqrt(2)D=||Ghat^(1/2)Y Ghat^(1/2)||_F
             <=||Bmat||_F<=72delta.

In particular the convenient rational bound is

    delta >= 1/[72(Q+1)].

It holds for EVERY distinct pair in the full preparation class, hence also
for the minimum Delta_Q between the two seam classes. No finite enumeration
is the source of this universal conclusion.

## 4. No bounded effect family can improve the asymptotic precision rate

Let v=(1,0,0,0,-1,0,0,0), so q(v)=8 and tv belongs to R iff41 divides t.
For n>=1 set a=41n, b=a+1, r=av, s=bv, and Q_n=8b^2. Both are admissible,
with r in the seam and s outside it. Their anchored projectors satisfy

    D_n^2=8/[(1+8a^2)(1+8b^2)] < 9/Q_n^2.

For any effect 0<=E<=I, |tr E(rho_r-rho_s)|<=D_n: in the two-dimensional
support of the difference its eigenvalues are +/-D_n. This upper bound
applies even to an unlimited family of effects, not just the selected45.

Furthermore Q_(n+1)<4Q_n. Therefore, for arbitrary Q>=Q_1=14112, choose
the largest n with Q_n<=Q. The same pair yields

    Delta_Q(any effect family) <=D_n<12/Q.

For the declared45-context family we therefore have

    1/[72(Q+1)] <= Delta_Q < 12/Q,       Q>=14112.

The order Q^-1 is sharp in this explicitly referenced pure-state comparison
class. Constants, number of settings, and decoding complexity are NOT claimed
optimal. In particular there is no fixed nonzero absolute tolerance valid
for all unbounded preparation norms, even after adding the reference.

## 5. Finite-precision decision and computation resources

The reader is given Q and the fixed45 contexts, not the actual z or q(z).
It may enumerate B_Q by the finite integer coefficient bound, calculate all
exact rational response profiles, and label them by the frozen congruence.
Given observations within sup-norm error epsilon of the true profile, retain
all profiles within epsilon. If

    epsilon <1/[144(Q+1)],

the retained list cannot contain both seam labels. The true profile remains
in the list. For example epsilon=1/[288(Q+1)] is a valid declared tolerance.
This is a constructive finite algorithm; its table can be large. The crude
candidate-count upper bound is O(Q^4), so constant measurement count must not
be confused with constant classical memory or computation.
Mean precision has logarithmic bit cost in Q, but obtaining those means from
samples can have a much larger cost. Calibration and state-preparation errors
must be charged to the same response-error contract; none is supplied here.

## 6. Conditional sample complexity, with the assumptions made explicit

This section additionally assumes identical fresh preparations and independent
Bernoulli outcomes with the adopted mean p_v at every use of a binary context.
Those assumptions are NOT consequences of the integer record.

For N samples of one binary context, the elementary exponential-moment bound
E exp[t(X-EX)]<=exp(t^2/8) gives

    Pr(|p_hat-p|>=epsilon)<=2 exp(-2N epsilon^2).

For completeness, the second derivative of the centered log moment generating
function is the variance of a tilted Bernoulli variable, at most1/4. Its value
and first derivative at zero vanish, giving t^2/8 by two integrations. Markov's
inequality and optimization give the displayed tail bound.

The union bound across45 settings gives error probability at most
90 exp(-2N epsilon^2). At epsilon=1/[288(Q+1)], sufficient samples PER SETTING are

    N >= ceil(41472 (Q+1)^2 log(90/eta)).

There are45N individual preparations. The constants are deliberately loose,
not a proposed laboratory design. For fixed confidence this is O(Q^2).

This quadratic worst-case rate cannot be improved merely by permitting
arbitrary collective measurements on independent identical pure copies.
For the pair in section4 let F=1-D_n^2. N copies have squared overlap F^N.
The optimum equal-prior binary error is

    e_N=(1-sqrt(1-F^N))/2,

again by diagonalizing the rank-two difference of the pure projectors.
To obtain e_N<=eta<1/2 requires F^N<=4eta(1-eta). Since -log(1-d)<=2d
for0<d<=1/2, the large-Q bounds in section4 give the necessary estimate

    N > (Q^2/288) log(1/[4eta(1-eta)]),   Q>=14112.

Thus O(Q^2) and Omega(Q^2) hold for fixed error in the declared model.
This is not a proof of physical Born occurrence, independent settings,
repeatability, finite-capacity renewal, or the cost of preparing the reference.

## 7. An exact failure for unrestricted mixtures

Pure-state distinguishability cannot be promoted to classifying arbitrary
mixture preparations. Define

    sigma_t=(rho_(tv)+rho_(-tv))/2,
    v=(1,0,0,0,-1,0,0,0), q(v)=8.

The off-diagonal reference/source blocks cancel, leaving

    sigma_t = [1/(1+8t^2)] P_ref
              +[8t^2/(1+8t^2)] P_v.

Here P_v denotes the rank-one projector onto the source line in the augmented
space, orthogonal to the reference. Put

    lambda=354161/735212,
    1-lambda=381051/735212.

Then exactly

    sigma_41 = lambda sigma_40+(1-lambda)sigma_42.

Every pure member of the left preparation is in R. Every pure member on the
right is in S minus R. All satisfy q<=14112. The two averaged density matrices
are identical; hence every effect has identical mean, regardless of the
number or precision of settings. In the adopted state-only quantum model
no measurement distinguishes these preparations. Independently resampling
these mixtures gives identical tensor-power states for any sample count.

This is NOT a claim about retaining one hidden pure label across all trials,
about access to a classical norm/label register, or about additional source
records: those are different complete preparation contracts. The mixture
counterexample excludes precisely a universal decision from the averaged
reference-augmented density alone. Extra precision cannot fix it.

## 8. What has and has not been established

A fixed modest-rational45-setting family reads the seam on each complete
bounded PURE preparation class, under an explicit fixed reference and adopted
Born means. Worst-case mean precision scales as Q^-1; conditional sample cost
has sharp order Q^2 at fixed confidence. Arbitrary mixtures instead admit an
exact opposite-label collision already at Q=14112.

These are mathematical existence, cost, and obstruction results. The 20/820
modular periods of the predecessor are not used as physical signal periods.
No native contact, actual event, conserved energy, reference availability,
metric selection, universal apparatus class, or L1-to-L6 bridge is supplied.

## 9. Evidence

PREREG.md predates the finite verifier execution. Analytical predictions were
already known when that contract was written. verify.py uses only integers
and Fraction from the standard library. Its finite controls audit projector
identities, reconstruction, inequalities, adjacent-multiple witnesses and the
exact mixture equality. RUN.json and ACTUAL.txt report the actual run; none of
the universal statements rests on counting a sample. One local architecture,
no blind independent agent, no earned public theorem status.
