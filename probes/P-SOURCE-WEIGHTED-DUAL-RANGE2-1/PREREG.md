# P-SOURCE-WEIGHTED-DUAL-RANGE2-1 preregistration

**NON-CANONICAL. L1. Prospective finite weighted-dual certificate.**
A. M. Thorn. 2026-10-26. Apache-2.0.
Reservation: [#1790](https://github.com/mathorn1973/twist-j/issues/1790).
Branch: probe/P-SOURCE-WEIGHTED-DUAL-RANGE2-1.
Dossier: PROMO-P-SOURCE-WEIGHTED-DUAL-RANGE2-1.

## 1. Authority and exposed predecessors

The sole authority remains ACTIVE Public Canon v105, public main and
peeled canon-v105 `892a0b11089d34e241e1eb76d2c03247022d18e6`, with
content commit `b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`. STATUS was
read first; POLICY, AGENTS, CORE and FRONTIER were completely read in
this session and remain unchanged. Public main was fetched, ancestry,
all five normative hashes and required architecture/aggregate/publication
checks verified, and main rechecked unchanged before reservation. A fresh
explicit remote scan contained 315 branch heads. Open issues/PRs, branches,
probe/note directories and registry were checked for collision. Retired
internal attachments are not authority.

The immediately preceding [PR1789](https://github.com/mathorn1973/twist-j/pull/1789)
at `538341e03bd18fecdaf0eeaa6d88d154eb8e851f` records both original
parity/global-remainder tests INCONCLUSIVE. Its pin is
`55b6472d8b3081dd22f26439f09eb31d2e8dba69`; its output SHA-256 is
`49001f332e87d27caa8bc286c8804a8a998d663c3d18ef73a6ec434f1d6e74d2`.
Those outputs are exposed inputs to this successor, not blind evidence.
The earlier PR1787 at `165964849b2d8f3ca6278e88755c1a8e03d6d842`
and its stopping rule for a different filtered-carrier test are unchanged.
PR1785 at `19f1c74a27684a22bf038c1e6fc1133f638fb613` retains its
conditional diameter-one obstruction. No independent external acceptance
is inherited or asserted for these successors.

## 2. Unchanged source, energy and forbidden output

Use the source of PR1777 at `191ab035be823bd9d6fdc9effba81528fa026e49`
and logarithm of PR1772 at `3abf054e435e31c51e6e50528b09fe3cf7cffe13`:

    U=U_rec, Q=E0 f(U), E0>0,
    f(exp(-i theta))=theta for 0<=theta<2pi, f(1)=0,
    chi=|R=97,r=0,iB;c=97,token label0> tensor Xi,
    B=(e2-e3)/sqrt(2),
    psi_sigma=[I+sigma(U²-U^-²)]chi/sqrt(Z), sigma=+1,-1,
    Z=(39521+154sqrt(5))/15625.

All 26 old-memory labels and arbitrary passive references remain admitted.
The bare occupation isometry and its phases are unchanged. Comparators
are sums of Hermitian terms of physical diameter at most two, with source
action and matrix-element convergence as stated in PROOF.md. Extra ancillas
have fixed data-independent readiness, possibly internally entangled.
No positivity, charge or term-strength assumption is needed by the test.

The common projection F is exactly the predecessor's rule. Form the union
S0 of both actual nonzero source supports (R,r,c,kind), after collecting
equal-basis coefficients and only then omitting coin. A target alpha must
have even object positions R+r and R-r. For EVERY beta in S0 form

    D_obj={R_alpha+r_alpha,R_alpha-r_alpha,
           R_beta+r_beta,R_beta-r_beta},
    D_car={} when (c_alpha,kind_alpha)=(c_beta,kind_beta),
          {c_alpha,c_beta} otherwise.

F selects alpha iff the diameter of D_obj union D_car is greater than two
against every beta. Its omission of labels/memory is conservative and it
commutes with receiver calibration. The same F is used for both signs.
Changing mathematical dual vectors below does not change the source or
the physically admitted comparison class.

## 3. Entire fixed family and exact error envelope

Set A=(U-U*)/(2i), C=(U+U*)/2 and S=[f(U)-f(-U)]/pi, including
S(1)=-1 and S(-1)=+1. Keep the same polynomial

    p4(A)=(315A-420A³+378A⁵-180A⁷+35A⁹)/128,
    v_sigma=F p4(A)psi_sigma, L=F A² F,
    w_(sigma,m)=L^m v_sigma, m=0,1,2.

L is a positive contraction. For every sign and m compute

    N_(sigma,m)=||w_(sigma,m)||²,
    X_(sigma,m)=Re <w_(sigma,m),v_sigma>,
    B_(sigma,m,a)=||C^a w_(sigma,m)||², a=0,...,10.

Apply F after EACH A² in L. Apply NO additional F inside or after the
C^a chains defining B. The common unit phase i may be included in both
v and w for integer computation; it cancels from N, B and X.

For y=C² the absolute sign-polynomial error has the positive series

    e(y)=sum_(n>=5) e_n y^n,
    e_n=315*binom(2(n-5),n-5)/(256*n*4^(n-5)),
    q_n=sum_(j=5)^(n-5) e_j e_(n-j), n>=10.

Both coefficient sequences sum to one. Freeze for every a=0,...,10

    r_a(y)=sum_(n=10)^(a+9) q_n y^(n-a)
           +[1-sum_(n=10)^(a+9)q_n] y^10,
    R_(sigma,j)=||C^j psi_sigma||², j=0,...,10,
    T_(sigma,a)=<psi_sigma,r_a(C²)psi_sigma>.

Empty sums vanish. T is the displayed positive LINEAR combination of
the R values, not the squared norm of r_a(C²)psi. All coefficients through
q19 are exact rational numbers. The bound (S-p4)²/C^(2a)<=r_a(C²)
holds in the stated Borel sense, including C=0 and the spectral cuts.
No no-atom or fitted spectral-density premise is used.

PROOF.md gives, when N>0,

    error/E0 >= (pi/2)(X-sqrt(P))/sqrt(N),
    P=B*T, t=1/1800,
    D=X²-P-t²N, E=D²-4t²NP.

A case succeeds iff `N>0 AND X>0 AND D>0 AND E>0`. These guards are
exactly equivalent to the displayed normalized gap being greater than t.
By pi>3, success excludes energy-action error at most E0/1200.
Zero N is an inconclusive zero witness, never division by zero or an
integrity failure. The final output convention is fixed below.

All 2*3*11=66 sign/m/a cases MUST be evaluated and reported, including
every failed case, without early stopping. A per-sign disposition is
CERTIFIED_OBSTRUCTION iff at least one of its 33 cases succeeds; overall
disposition succeeds iff at least one sign succeeds. This is a declared
finite exact family, not a selected statistical trial. No source, degree,
projection, m/a range, threshold or method can change after the pin.

## 4. Exact implementation, checks and execution boundary

Accepted executable: [verify.py](verify.py), standard library only.
Verifier SHA-256:
`c637973a805bddbf38071d3e758416454ca7bd3821bd074d72d08640993c46ad`.

The inherited exact walk is evaluated in fixed arithmetic coin coordinates
G=diag(1,i,i,1), with integer U25=25 G*U_uncal G over Z[zeta5]. This
changes arithmetic coordinates only. The source and polynomial stage uses
seed powers -12 through 12 and denominator D0=65536*25^12, as before.
The integer witness update is

    2500 L w = F(1250 w - U25² w - (U25*)² w).

Each C step uses U25+U25* with denominator 50. The maximum propagation
radius from the original seed is 11+2m+a<=25. All intermediate paths are
retained; no finite-box truncation is introduced. R_j and T_a require
only seed horizon 12. Data and dual-vector radius bounds are distinct.

Squared norms, real overlaps, positive envelopes and all guards use exact
integer/rational arithmetic in Q(sqrt(5)). No numerical square root,
floating point, randomized search, selected precision or external input
is used. The previously published W_plus, W_minus and R10 are explicit
exposed baseline checks; m=0,a=0 must reproduce both prior inconclusive
comparisons. Source spectral equality gives R_j,plus=R_j,minus.
Positivity and contraction supply additional exact consistency checks,
including X0=N0, X2=N1, B_m0=N_m and nonincreasing C-power norms.

Static source review and syntax compilation are allowed before the pin.
This new verifier must not be imported or scientifically executed before
its exact code, PREREG.md and PROOF.md are committed, pushed and publicly
read back byte for byte. No exploratory timing or memory benchmark is
allowed. Expected cost is a static estimate only. The existing repository
600-second verifier timeout is retained, not raised for this probe.

Command from repository root:

    python3 probes/P-SOURCE-WEIGHTED-DUAL-RANGE2-1/verify.py

The verifier emits exactly 381 deterministic UTF-8 key=value lines.
The first fourteen keys, in order, are:

    probe
    arithmetic
    parameters
    radii
    projection
    source_Z
    dual_gap_threshold
    energy_action_target
    common_denominator
    exposed_baseline
    source_spatial_support
    positive_support_counts
    negative_support_counts
    integrity

Next come eleven `source_R00` through `source_R10` lines, then eleven
`sharp_R_a00` through `sharp_R_a10` lines. They report the common exact
source norms and common envelope expectations after independently checking
both source signs for equality.

Then report plus and minus in that order. For each setting, report m=0,1,2
in order: first `<sign>_m<m>_X` and `<sign>_m<m>_N`; then for every a=0,...,10
in order, with two-digit a, report these five keys:

    <sign>_m<m>_a<aa>_B
    <sign>_m<m>_a<aa>_d_sign
    <sign>_m<m>_a<aa>_e_sign
    <sign>_m<m>_a<aa>_comparison
    <sign>_m<m>_a<aa>_disposition

After each setting comes `<sign>_disposition`. The final line is
`overall_disposition`. The line count is
`14+11+11+2*(3*(2+11*5)+1)+1=381`.

Algebraic values use (u+(v)*sqrt(5))/d with a positive denominator and
a gcd-reduced integer triple. The exact X,N,B and sharp_R values determine
both guard expressions; their potentially much larger expanded numerators
are not duplicated. Guard signs are -1,0,1. Comparison is GT, EQ or LT for
the normalized gap versus t, or ZERO_DUAL when N or X vanishes. ZERO_DUAL
is INCONCLUSIVE. Because 0<=N<=X, X=0 also forces N=0 in this family.
The support line lexicographically sorts (R,r,c,kind), encodes each tuple
with colons and separates tuples with semicolons. Both seed-count lists
include powers 0 through 12. No timing or platform-dependent data is emitted.

## 5. Failure, custody and acceptance

All integrity checks must pass before stdout is emitted. Completed
INCONCLUSIVE comparisons exit zero with empty stderr, just like a completed
certificate. Any assertion, exception, nonzero exit, timeout, missing output
or inconsistent custody is an integrity failure, not a physical result.
The identifier cannot be repaired and rerun after the pin. An incomplete
gate is recorded under the abandoned-pin policy, and any successor must
have a new identifier and prospective pin.

Preserve the first completed stdout unchanged in EXPECTED.txt. RUN.md
records the full pin, code hash, canonical command, neutral platform,
architecture and Python version, exit code, stdout byte/line counts/hash
and empty-stderr counts/hash. Unchanged local and clean GitHub x86_64 and
aarch64 replays must require byte-identical stdout. RESULT.md reports both
signs and all cases, including any successful case's limited physical scope.

If all cases fail, diameter two remains open. A failed sufficient bound
does not construct a local Hamiltonian or bound the true energy tail above.
A passing bound excludes only original bare-occupation diameter-two energy
action on the stated source. It does not exclude a local discrete step,
accurate evolution alone, dressed encodings, another energy, larger diameter,
or the separate compact apparatus with its own Hamiltonian. Native physical
derivation, empirical units, thermal readiness, individual-event selection
and replenished indefinite operation remain outside this test.

Same-session authoring, adversarial checks and reproduction are not external
independent scientific acceptance. Public Canon v105 remains unchanged;
no registry, policy, workflow, predecessor, release or authority change.
