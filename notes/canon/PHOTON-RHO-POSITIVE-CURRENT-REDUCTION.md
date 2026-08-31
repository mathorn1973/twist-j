# Full score defect as a positive integer current with exact noise subtraction

Status: NON-CANONICAL / RESULT-EXPOSED / CONDITIONAL MODEL / NO FORMAL RUN.

Date: 2026-08-31.
Shared notes identity: `P-PHOTON-GEOMETRIC-CURRENT-REDUCTION-1`.
Notes claim: [issue #727](https://github.com/mathorn1973/twist-j/issues/727).

Public reference: main `1c5f7832a9dec807d1f9830be3cdbdd092ff4f99`,
Public Canon v72 unchanged. This publication contains notes-only original
conditional mathematics, not a preregistration, verifier, new formal probe,
Canon adoption, or physical phase claim.

The selected finite-product model and its existing observable identities
are those of the [Born-current observable note](PHOTON-BORN-CURRENT-OBSERVABLE-LEMMA.md),
the [defect-screening criterion](PHOTON-DEFECT-SCREENING-CRITERION.md), and
the [unsigned-current bound](PHOTON-UNSIGNED-CURRENT-SUPPRESSION.md).
The companion [low-conflict path note](PHOTON-LOW-CONFLICT-CURRENT-PATHS.md)
addresses a restricted geometric family in the original character law.
Neither note establishes the full infrared estimate or closes a photon
successor root. No scientific verifier or census was executed for this note.

## 1. Selected model and a notes-only auxiliary-law gate

Let K be a finite free rectangular cubical box in Z^4, with all cells and
positive coordinate orientations. Let d be cellular coboundary. Every
edge variable A is summed in Z5 with weight product_p W(q_p), where
q=dA and W(q)=2+2cos(2pi q/5). Put s=sqrt(5), kappa=tan(pi/5), and

    kappa^2=5-2s,
    F=pr(q) in {0,+1,+2,-2,-1},
    H(q)=(0,0,1,-1,0),
    G=F+sH,
    X=kappa G,
    m=dF/5,
    rho=dX=kappa(5m+s dH).

These observables and the positive character law nu on ternary n,
partial n=0 modulo5, are the earlier conditional definitions. Its current
is j=partial n/5. The measures of n and q are paired, not identified.

For the new auxiliary construction the name below is only a local
notes-level description, not an adopted registry gate:

    NOTE-GATE-L4-L6-PHOTON-FULL-RHO-INTEGER-LIFT
    from: L4 finite incidence and explicit W,F,H,G and lift-kernel data
    to:   L6 auxiliary joint law of the selected q and the integer lift L
    map:  independent Bernoulli marks conditional on q, defined below
    identities: conditional mean, total covariance, exact noise subtraction
    scope: finite free boxes and the stated paired averaged local limits

The selected q measure is the finite-product law already constructed in
Section1 of the earlier screening note; it is not itself relabelled L4.
This does not change the selected source, replace rho by m, or discard
the branch term dH. It introduces an additional positive probability
space, not a physical identification of its auxiliary variables.

## 2. A local no-cancellation theorem for the full rho

Fix an oriented elementary three-cube. It has six boundary plaquettes.
Absorb their incidence signs into their principal residues. Let u be
the signed net count of residues +1 versus -1, and let v be the signed
net count of +2 versus -2. Consequently

    |u|+|v|<=6,
    (dF)_c=u+2v=5m_c,
    (dH)_c=v.

Suppose m_c>0 and v<0. Since these are integers, u=5m_c-2v>=7,
contradicting |u|+|v|<=6. The reversed signs give the same contradiction.
Thus, pointwise on every cube,

    m_c (dH)_c >= 0,
    |rho_c|=kappa[5|m_c|+s|(dH)_c|].                    (LOCAL)

In particular rho_c=0 exactly when both m_c and (dH)_c vanish. Every
nonzero rho_c has |rho_c|>=kappa s: if m_c=0 this follows from the
nonzero integer dH; if m_c!=0 the lower bound5kappa is larger.

The lower threshold is attained. On the full unit four-box choose
A_1=A_4=0,A_2=x_1 x_3,A_3=2x_1 x_2 modulo5, independently of x_4.
Then F_12=x_3,F_13=2x_2,F_23=x_1,F_i4=0. Hence dF=0, but
(dH)_123=-1 and rho_123=-kappa s. This edge configuration has positive
W weight. Thus the branch correction can be the entire score defect.

Equation(LOCAL) excludes cancellation between the two contributions at
ONE cube. It does not impose a sign on m_c(dH)_(c') at distinct cubes,
on cross covariances, or on a sum paired with a sign-changing test form.
It therefore supplies no infrared covariance estimate by itself.

## 3. An explicit rare-branch-noise lift

Conditional on the complete curvature field q, choose independent marks
xi_p in {0,1}, with the fixed probability

    P(xi_p=1 | q)=1/s=s/5.

They can equivalently be chosen independently of q. Define

    L_p=F_p+5 xi_p H_p,
    J=dL/5=m+d(xi H).

The finite alphabet of L is {0,+1,-1,+2,-2,+7,-7}. More explicitly,

    q=0:   L=0;
    q=+1:  L=1;
    q=-1:  L=-1;
    q=+2:  L=2 with probability1-1/s, L=7 with probability1/s;
    q=-2:  the sign-reflected pair of values and probabilities.

All probabilities are strictly between zero and one where a choice
occurs, and belong to Q(s). Always L=F modulo5, so dL is divisible by5.
Thus J is an integer three-cochain and dJ=0 exactly. On one cube
|J_c|<=8, since |(dL)_c|<=42 and it is an integer multiple of5.
Neither J nor m is identified with the separate character current j.

Conditional expectation preserves the FULL score:

    E[L_p | q]=F_p+sH_p=G_p,
    E[J | q]=dG/5=rho/(5kappa).                         (MEAN)

Let eta=L-G. Then E[eta|q]=0. Conditional independence gives

    E[eta_p eta_r | q]
       =delta_pr V_p(q),
    V_p(q)=25(1/s)(1-1/s)H_p^2
          =5(s-1)H_p^2.                               (NOISE)

The lifts are independent GIVEN q, not independent after q is summed.
All q correlations and hard curvature constraints remain present.

## 4. Equivalent positive constrained integer law; free-box exactness

The marginal law of L can be stated without conditional marks. Define
positive weights on its seven-element alphabet by

    w_0=4,
    w_(+1)=w_(-1)=phi^2,                   phi=(1+s)/2,
    w_(+2)=w_(-2)=phi^-2(1-1/s),
    w_(+7)=w_(-7)=phi^-2/s.

All other weights are zero. The residue sums are exactly W(q): for
example w_2+w_7=phi^-2. Then the auxiliary law is

    P(L) proportional to product_p w_(L_p)
        times1{dL=0 modulo5}.                           (POSITIVE)

Here the modulo5 constraint is a three-cell constraint, not the edge
constraint on the earlier n field. Its proof must retain the boundary
and topology. A free rectangular cubical box is contractible. The
cellular contraction obtained by successively contracting its interval
coordinates proves H^2(K;Z5)=0. Therefore every closed modulo5 face
cochain q is exact: ker d_2=im d_1. The linear map A->dA has the same
number |ker d_1| of preimages for every q in its image. Summing the
original edge law consequently gives

    P(q) proportional to product_p W(q_p) times1{d_2 q=0}.

For each q, splitting W(q_p) into the displayed positive residue weights
is exactly the independent lift kernel of Section3. Multiplying and
then summing over q yields(POSITIVE), with no discarded sector or fixed
outside current. Conversely reducing(POSITIVE) modulo5 returns the
original curvature law.

This argument uses free-box exactness and constant fibers. It is not
asserted for a torus without extra cohomology-sector data. It is not a
claim of face independence in the constrained marginal law.

## 5. Exact finite covariance reduction, with its nonoptional contact

Charge conjugation and the sign-equivariant mark construction give
zero means for G,L,rho,J. Write

    V=diag_p E_mu[V_p(q)]
     =5(s-1)diag_p P_mu(|F_p|=2).

By total covariance, for finite face indices,

    C_L=C_G+V=kappa^-2 C_X+V.

Applying d_2 and its real transpose gives exactly

    25 C_J=kappa^-2 C_rho+d_2 V d_2^T,
    C_rho=25 kappa^2 C_J-kappa^2 d_2 V d_2^T.            (CURL)

The second term is positive semidefinite and has finite spatial range:
two cube boundaries must share a face to contribute. It is SUBTRACTED.
For every finite real three-form test f this says

    Var_mu(<f,rho>)
      =25 kappa^2 Var_aux(<f,J>)
       -kappa^2 sum_p V_pp[(d_2^T f)_p]^2.

Thus the elementary consequence C_rho<=25kappa^2 C_J is valid, but
dropping the contact as an equality is not. Outside its finite overlap
range, the two covariance kernels are exactly proportional. No decay
or summability of either long-distance kernel follows from(CURL) alone.

## 6. Minimal local noise for an unbiased residue-preserving lift

The noise in(NOISE) is not an arbitrary inefficiency at the fixed
normalization E[L|q]=G. Consider ANY integer lift L' congruent to q
modulo5 with this conditional mean and finite conditional second moment.
At q=0 or +/-1 its variance is nonnegative, and our deterministic choices
attain zero. At q=+2 its permitted values lie in2+5Z and its mean is2+s.
For every such value,

    (L'-2)(L'-7)>=0.

Taking expectation proves

    Var(L' | q=2)>=(s)(5-s)=5(s-1).

Equality requires L' to lie in{2,7}, with probabilities forced by its
mean. Sign reflection handles q=-2. Therefore our construction minimizes
the conditional one-face variance among all integer residue-preserving
lifts unbiased for G, without restricting their allowed integer range.

This is a local variance-minimality statement. It does not optimize
spatially correlated lift noise, auxiliary-current spectra, or another
normalization of the target score.

## 7. Explicit noise bounds and stationary paired limits

The previous contact theorem gives E X_p^2<=1. Since

    X_p^2=(5+2s) when |F_p|=2,

we obtain the exact local bound

    V_pp <= [5(s-1)/(5+2s)] E X_p^2
           =(7s-15)E X_p^2.

For the fully hypercubic stationary paired limit constructed in the
screening note, E X_p^2=2d-1 and d in[1/2,1]. Extend that construction
by the same independent Bernoulli kernel on faces. The joint finite
alphabet is compact in the cylinder sense, and the kernel is compatible
with translations, signed coordinate permutations, and charge conjugation.
The same common averages and diagonal limits therefore give a stationary
auxiliary law preserving all finite local mean/covariance identities.

Hypercubic symmetry makes V=vI on face indices, with

    v=5(s-1)P_mu(|F_p|=2),
    0<=v<=(7s-15)(2d-1),
    0<=kappa^2 v<=(65s-145)(2d-1).                       (V-BOUND)

The coefficients are positive: 7s>15 and13s>29 follow by squaring
positive sides. These are bounds on a LOCAL noise coefficient, not on
the long-range auxiliary-current covariance.

The stationary covariance of L has bounded density

    S_L=kappa^-2 S_X+vI,

because the earlier S_X is bounded and positive. Thus the density S_J
exists without an additional summability assumption. With the screening
note's E_2(q)=wedge(exp(iq)-1) and lambda=sum_i|exp(iq_i)-1|^2,

    25 S_J=kappa^-2 S_rho+v E_2 E_2^*                  (a.e.).

For nonzero momentum E_2 E_2^* has rank3 and its three nonzero eigenvalues
are lambda. Consequently

    25 tr S_J/lambda
      =kappa^-2 tr S_rho/lambda+3v.                    (BASELINE)

In particular the auxiliary-current quantity includes a noise baseline;
positivity of S_J alone is not a smallness estimate above that baseline.

## 8. Exact screening rewrite, not an infrared estimate

The previous complete defect expression is

    R=[25 tr S_j+tr S_rho]/lambda.

Here S_j acts on one-forms in the original character law, while S_J acts
on three-forms in the new auxiliary law. Their scalar traces are added;
no Hodge identification of those distinct carriers is assumed. The new
auxiliary law is coupled to q, not to the original n or j. No cross
covariance or joint identification of j and J is needed.
Equation(BASELINE) gives the exact rewrite

    R=25[tr S_j+kappa^2 tr S_J]/lambda-3kappa^2 v.       (REWRITE)

Thus the earlier lower strict screening condition is equivalent to

    ess-limsup_(q->0,q!=0)
      25[tr S_j(q)+kappa^2 tr S_J(q)]/lambda(q)
        <3(d+kappa^2 v).                               (TARGET)

The upper strict-gap alternative similarly becomes an essential liminf
strictly larger than the same threshold. These are exact substitutions,
not new estimates. In particular using an UPPER bound for v to enlarge
the right side of(TARGET) would give a weaker test that is NOT sufficient
for the original screening claim. Keep the actual v, or use a justified
lower bound on it in a sufficient test. The(V-BOUND) inequalities do not
by themselves prove(TARGET).

This reduces the full rho channel to an actual positive integer-current
law with a known finite-range subtraction. A useful next theorem would
bound its low-momentum excess above3v together with the original j
contribution. Marker-count suppression or local variance alone does not
provide such a distance-sensitive estimate.

## 9. Lossless diagonal tails and the contact second moment

If two three-cubes have no common boundary face, the noise-contact entry
in C_rho=25kappa^2 C_J-kappa^2 d_2 V d_2^T vanishes. Therefore

    C_rho(c,c')=25kappa^2 C_J(c,c')

holds for such pairs already in finite volume.

In the stationary state V=vI. For one three-form orientation I, the
same-orientation diagonal kernel of d_2 d_2^T has Fourier symbol

    sum_(i in I)|exp(iq_i)-1|^2.

Its origin coefficient is6, its coefficient at each displacement +/-e_i
for i in I is-1, and all other coefficients vanish. Hence for every
Euclidean radius R>=1 the diagonal weighted absolute tails agree exactly:

    sum_(|x|>R)|x|^2 sum_(|I|=3)|C_rho(II;x)|
      =25kappa^2 sum_(|x|>R)|x|^2 sum_(|I|=3)|C_J(II;x)|.

The equality remains valid for divergent nonnegative sums. Thus weighted
absolute diagonal second-moment finiteness for rho is equivalent to that
for J. No extra long-range error is introduced by the lift. This exact
transfer is not a bound on either tail.

When the existing weighted absolute second-moment hypotheses hold,
define M_j and M_J as the sums of |x|^2 times the respective diagonal
covariance traces. Each of the four three-form contact components has
weighted moment-6, giving

    sum_x |x|^2 tr(d_2 d_2^T)(x)=-24.

Equivalently its trace Fourier symbol is3lambda. The covariance identity
therefore yields

    M_rho=25kappa^2 M_J+24kappa^2 v,
    M_total=25M_j+M_rho
           =25(M_j+kappa^2 M_J)+24kappa^2 v.

The earlier sufficient second-moment inequality -M_total<24d consequently
rewrites exactly as

    -25(M_j+kappa^2 M_J)<24(d+kappa^2 v).

The PLUS sign on the contact contribution to M_total comes from subtracting
a kernel whose weighted moment is-24. These M identities require the stated
absolute moment hypotheses, whereas the finite contact identities require
no tail assumption. The actual v must be retained, or a justified lower
bound used in a sufficient test; substituting an upper bound on the right
would not be sufficient.

## 10. Why the auxiliary positivity is not a continuous-action shortcut

The coefficients w_k are nonnegative. That fact makes(POSITIVE) a
probability law, but does NOT make their continuous Fourier sum
nonnegative. For this exact minimal-noise lift that sum is

    A(theta)=4+2phi^2 cos(theta)
      +2phi^-2[(1-1/s)cos(2theta)+(1/s)cos(7theta)].

On the five roots it equals5h, h=(2,1,0,0,1). At theta_2=4pi/5 one has
A(theta_2)=0 and A'(theta_2)=0, but direct differentiation gives

    A''(theta_2)=15s-35<0.

Indeed phi^2 cos(theta_2)=-1-s/2 and
phi^-2 cos(2theta_2)=(s-2)/2, while4(1-1/s)+49/s=4+9s.
Substitution gives the stated derivative. The sign follows from
5*15^2<35^2. Thus A is negative in a punctured neighborhood of this
sampled zero. Its coefficients cannot be substituted into a positive
U(1) angle-measure argument without a different construction and proof.

This obstruction is specific to that continuous-action shortcut, not to
the positive integer law already proved above or to every other lift.

## 11. Endpoint

The new finite results are the local no-cancellation identity, an explicit
positive residue-preserving integer lift retaining all of rho, its
conditional variance-minimality at fixed mean G, and the exact covariance
and noise-baseline formulas. The stationary rewriting retains all contact
terms and the unchanged infrared threshold.

No screening gap, connected-correlation decay, massless phase, physical
photon, source adoption, or Canon gate closure is proved. This publication changes notes only; it changes no Canon file, sealed
probe, accepted verifier, registered gate, or release.
