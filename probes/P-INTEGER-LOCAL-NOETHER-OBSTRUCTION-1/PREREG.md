# P-INTEGER-LOCAL-NOETHER-OBSTRUCTION-1

Status: PROSPECTIVE
Scope: NON-CANONICAL, NEW_DECLARED L1
Owner: A. M. Thorn, session integer-local-noether-obstruction-2026-10-20
Ownership: https://github.com/mathorn1973/twist-j/issues/1661

## 1. Question, authority and fixed scope

This probe asks whether the inherited first-order Noether system admits a
second-order completion whose multiplier interactions have a fixed finite
temporal range, uniformly in the horizon. It does not propose a new gravity
law. It is distinct from the exact selected completion and local parent in
the separately owned #1659. That work is still prospective at the inspected
pin; its execution outcome is not an input.

Authority: Public Canon v103, main and peeled canon-v103
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. The five normative byte strings
must match their hashes in SOURCE.md. The scientific source is the frozen
specification of #1658, pin 56437c4ef2c2e3a5aee679bb87b693395213f644,
result 96b100322f5301293cefb382ac47b4ed5c484ad3. No earlier probe program is
imported or executed by either new verifier.

All arithmetic is exact over integers and rational numbers. No tolerance,
decimal approximation, fitted parameter, numerical derivative, physical
clock, native-U implementation or layer lift is admitted.

## 2. Inherited carrier and equations

Let T>=5. The five vertices are r=0,...,4. Edges e=r (0<=r<5) point
r -> r+1 mod 5 and have weight 29/324. Edges e=5+r point
r -> r+2 mod 5 and have weight 65/324. B maps a vertex vector to
head minus tail, W is the diagonal weight matrix, and L=B^T W B.

    (324 L h)_r = 188 h_r -29(h_(r-1)+h_(r+1))
                          -65(h_(r-2)+h_(r+2)).
    g=1/324, ell=(1,-1,0,0,0), sigma=(1/2,1/2,0,0,0), e=(1,1,1,1,1).

Fields x_n=(h_n,chi_n) are in Q^5 x Q at n=0,...,T. The identity is required
for every rational endpoint pair; endpoint values are held fixed during
variations, and completion coefficients may depend on them. This probe uses
the admitted force context a=0, sufficient
to obstruct a completion required on the full inherited domain. Auxiliary
tau_b and lambda_b lie in e^perp for b=1,...,T; p_n lies in ker B^T and
N_n in Q^10 for n=1,...,T-1. Alpha_b is a scalar. Thus M=(alpha,lambda,N).

The action and residuals at a=0 are

    A(x)=1/2 sum_(b=1)^T (||h_b-h_(b-1)||^2+(chi_b-chi_(b-1))^2)
       -1/2 sum_(n=1)^(T-1) (h_n^T L h_n+chi_n^2)
       +g sum_(n=1)^(T-1) chi_n ell^T h_n,
    R_h,n=h_(n+1)-2h_n+h_(n-1)+Lh_n-g chi_n ell,
    R_chi,n=chi_(n+1)-chi_n+chi_(n-1)-g ell^T h_n.

Its interior gradient is (-R_h,-R_chi). Define q_h,n=h_(n+1)-h_(n-1)
and q_chi,n=chi_(n+1)-chi_(n-1). The vertex bond density is

    e_b(r)=1/2(h_b(r)-h_(b-1)(r))^2
      +1/4 sum_(edge incident at r) w_edge (B h_b)_edge(B h_(b-1))_edge
      +sigma_r [(chi_b-chi_(b-1))^2/2+chi_b chi_(b-1)/2]
      -(g/2)ell_r[chi_(b-1)h_b(r)+chi_b h_(b-1)(r)].

H_b=sum_r e_b(r). The source/field current is

    j_h,n(edge)=w_edge(Bh_n)_edge
                         [q_h,n(tail)+q_h,n(head)]/4,
    j_int,n(edge)=-(g/4)q_chi,n[h_n(0)+h_n(1)] delta_(edge,0),
    j_n=j_h,n+j_int,n.

For arbitrary fixed E_hom,

    B_aux(M;tau,p)=2 sum_b <lambda_b,L tau_b>
             +2 sum_n <N_n,W B(tau_(n+1)-tau_n)+p_n>,
    S0=A(x)+B_aux(M;tau,p),
    I(x,M)=-sum_b alpha_b(H_b-E_hom)-sum_b <lambda_b,e_b>
                                    +sum_n <N_n,j_n>.

E_hom is set to zero in the audit: its field derivative is zero and it
cannot affect this obstruction. For endpoint-zero parameters psi_n in Q^5,

    Gamma(psi)_alpha,b=mean(psi_b-psi_(b-1)),
    Gamma(psi)_lambda,b=Pi0(psi_b-psi_(b-1)),
    Gamma(psi)_N,n=B psi_n,
    (G_psi h)_n=psi_n*q_h,n/2,
    (G_psi chi)_n=<sigma,psi_n>q_chi,n/2,
    (G_psi x)_0=(G_psi x)_T=0.

Here * is componentwise multiplication. The inherited transformations are
delta0 M=Gamma(psi), zero elsewhere; delta1 x=G_psi x, zero elsewhere.
The desired second-order identity is

    delta0 S2 + delta1 I + delta2 S0 = 0.                 (W)

## 3. Complete tested class and analytic claims

S2 is any homogeneous quadratic function of the independent multiplier
coordinates, with differentiable coefficients depending arbitrarily on
the other coordinates and on T. Spatial mixing is unrestricted. The time
label of alpha_b or lambda_b is b; that of N_n is n. Range <=R means every
mixed multiplier Hessian coefficient is zero whenever its two labels
differ by more than R, for all admitted values of the other coordinates.
R is one nonnegative integer independent of T. This is a necessary
condition for the usual bounded-stencil local quadratic multiplier action,
and even permits nonlocal field-dependent coefficients.

delta2 may be an arbitrary endpoint-zero physical-field variation depending
on the complete state and parameter, defined and finite at every admitted
state including the on-shell histories. It acts only on x, not on tau,p,M.
No regularity or locality restriction on delta2 is needed for the theorem.
Identity (W) is required on the entire inherited domain, not only a prepared
family, and for every T. This exact class, not every local gauge theory,
is the subject of the claimed negative conclusion.

For each T and 2<=k<=T-2, define an exact autonomous history by

    h_(k-1)=u=(1,0,-1,0,0), h_k=0,
    chi_(k-1)=chi_k=0,

and use R=0 to extend it both forwards and backwards to 0,...,T.
Both recurrences solve uniquely for the missing adjacent slice over Q.
All h_n have zero spatial mean. Put tau=p=0 and let the only nonzero
multiplier be N_(k,0)=1. For uniform spatial psi_n=t_n e with t_0=t_T=0,
the predictions are

    delta1 I=-(29/648)t_k,       delta2 S0=0.             (A)

Let C_b be the mixed alpha_b/N_(k,0) Hessian coefficient of an arbitrary
S2 on this fixed field/auxiliary history. Homogeneous quadratic dependence
implies its alpha derivative at M=N_(k,0) equals C_b. Since Gamma(t e)
changes only alpha_b by t_b-t_(b-1), (W) forces

    C_b-C_(b+1)=(29/648)delta_(b,k), b=1,...,T-1.        (B)

The entire solution set is

    C_b=c+29/648 for b<=k, and C_b=c for b>k.            (C)

Here c is arbitrary in the coefficient field, in Q for rational-valued
completions. The same obstruction holds for real coefficients; the finite
audit remains entirely over Q and Z.

At least one complete tail is nonzero. The minimum radius |b-k| needed by
this necessary mixed-coefficient system is exactly min(k-1,T-k): c=0
uses the left tail, c=-29/648 uses the right tail, and both are nonzero
for every other c. Sharpness is ONLY for equations (B), not a sufficiency
claim for a full second-order action. Taking k away from both endpoints
excludes every fixed horizon-independent R.

The inherited prefix correction supplies C_b=(29/648)1_(b<=k). Its full
definition, used in the audit at lambda=0, is

    theta_0=theta_T=0, theta_n=sum_(b=1)^n (alpha_b e+lambda_b),
    rho=M-Gamma(theta), v=G_theta x,
    S2_prefix(x,M)=-D_x I(x,rho)[v]+1/2 Hess_A(v,v).      (D)

At tau=p=0 this depends only on x,M. Mixed coefficients are evaluated by
S2_prefix(alpha_b+N_(k,0))-S2_prefix(alpha_b)-S2_prefix(N_(k,0)).
The final coefficient is a temporal step, not compact support.

The restriction on auxiliary transformations is essential to the proof.
For the plateau t_n=1 at every interior slice, the single variation

    delta2 tau_k=ell/8, all other components zero         (E)

gives delta2 S0=29/648 on this witness, cancelling delta1 I locally.
This is a positive escape witness only. It is NOT an all-state local
completion and does not establish a closed algebra or gravitational law.

## 4. Frozen finite audit

Both programs independently implement all needed definitions. They use
only the Python standard library. No program execution, import, fixture
evaluation or scientific dry run occurs before the six-file public pin.
AST parsing, source inspection and hashing are permitted before the pin.

Horizons: T in (5,7,9,13), in this order. For each T, k=2,...,T-2 in
ascending order. This gives 22 histories, all with the fixed u above.

For every history:

1. Check all 6(T-1) interior residual components, zero mean at every slice,
   and the exact interior gradient using all coordinate directions.
   The primary uses exact central unit differences of the quadratic A;
   the breaker uses an independently assembled quadratic Hessian/linear
   action representation or exact dual arithmetic. Check 1200 components
   and 1200 action derivatives in total.
2. Check (A) for t equal to each interior unit vector in order, then the
   interior plateau 1, then t_n=(-1)^n(n+1)/7, endpoints zero. These are
   244 parameter cases. Current differentiation is exact algebraic
   differentiation or coefficient extraction; central differences are
   exact because j is quadratic. Confirm the interaction-current
   contribution vanishes on this witness.
3. Extract every prefix mixed coefficient in (D), for b=1,...,T, and
   compare it to (29/648)1_(b<=k). Total 222 coefficients. No runtime
   import from #1658 or #1659 is allowed.
4. Solve (B) with locality zeros C_b=0 for |b-k|>R, for every R=0,...,T-1.
   Compare feasibility with R>=min(k-1,T-k). The primary may propagate
   the one-parameter affine solution; the breaker must use independent
   exact row reduction of the full linear system. Total 222 systems.
5. Check the plateau obstruction and positive auxiliary escape (E), one
   of each per history. A finite support failure is not the proof for
   arbitrary R; the universal proof separately quantifies over T and k.
6. Let D be the least common denominator of the full history. Encode all
   fields by integer numerators H_n=D h_n, X_n=D chi_n and check
   324(H_(n+1)-2H_n+H_(n-1))+L_int H_n-X_n ell=0 and
   324(X_(n+1)-X_n+X_(n-1))-ell^T H_n=0, for 1200 components.
   For each t let Q be its least common denominator and check the exact
   integer equality 648Q(delta1 I)+29Q t_k=0, for 244 cases.

## 5. Negative controls and falsifiers

Every control must detect its stated defect, not merely run without error.
The fixed control history is T=5,k=2 and the interior plateau parameter.

- NC01 orientation: reverse only the tested edge-current sign. The witness
  derivative becomes +29/648 and must not satisfy (A).
- NC02 omitted current: remove the N*j interaction; its derivative is 0
  and must not satisfy (A).
- NC03 omitted reciprocal coupling: build the history with g=0 but
  evaluate the inherited g=1/324 residuals; at least one must be nonzero.
- NC04 undersized range: R=min(k-1,T-k)-1 makes (B) plus locality
  inconsistent. Require this for all 22 histories as well.
- NC05 both tails zero: add C_1=C_T=0 to (B); it must be inconsistent.
- NC06 reversed tail: C_b=-(29/648)1_(b<=k) must violate (B).
- NC07 absent correction: S2=0, field-only delta2 on an on-shell history,
  leaves the nonzero plateau residual -29/648.
- NC08 wrong auxiliary sign: delta2 tau_k=-ell/8 leaves -29/324,
  whereas the positive escape (E) cancels exactly.

The following are fired falsifiers, with exact zero tolerance:

F_AUTHORITY: any normative hash/size differs.
F_HISTORY: any recurrence, mean, encoding, or action-gradient identity fails.
F_WITNESS: any current derivative or interaction cancellation differs from (A).
F_INTEGER: any scaled witness or residual is not integral or is nonzero.
F_PREFIX: any actual mixed coefficient of (D) differs from its predicted tail.
F_TAIL: affine classification or exact linear-system feasibility fails.
F_RADIUS: any minimum radius differs from min(k-1,T-k).
F_PLATEAU: any promised finite-range contradiction fails.
F_ESCAPE: the positive auxiliary witness fails or is misreported as a theorem
          of full completion.
F_CONTROL: any of the eight negative controls fails to detect its defect.
F_COUNTS: finite case counts differ from those fixed above.
F_BYTES: the two raw ASCII/LF certificates differ, either process exits
         nonzero, or either writes stderr.

A completed scientific failure is recorded unchanged. A pin whose first
gate does not complete is disposed under POLICY.md; it is never repaired,
renamed, reused or resumed. No post-run threshold or fixture change is allowed.

## 6. Exact certificate and data ordering

Fractions serialize as Python Fraction.__str__: integer when denominator=1,
otherwise numerator/positive-denominator. No whitespace occurs inside lists.
Each payload record ends with one LF; SHA-256 covers their concatenation.
For each (T,k), append in order:

    H|T|k|comma-separated x_0,...,x_T, each h_0,...,h_4,chi
    C|T|k|i|delta1I                     (i=0,...,T for the parameter list)
    P|T|k|b|mixed-coefficient           (b=1,...,T)
    R|T|k|R|feasible-as-0-or-1          (R=0,...,T-1)
    E|T|k|positive-auxiliary-variation

After all histories append N|NC01|DETECTED through N|NC08|DETECTED in order.

Both implementations emit exactly this certificate, with computed digest:

    CERTIFICATE=P-INTEGER-LOCAL-NOETHER-OBSTRUCTION-1
    AUTHORITY_FILES=5
    HISTORY_CASES=22
    ON_SHELL_COMPONENTS=1200
    ACTION_DERIVATIVES=1200
    CURRENT_PARAMETER_CHECKS=244
    PREFIX_MIXED_COEFFICIENTS=222
    TAIL_SYSTEMS=222
    PLATEAU_OBSTRUCTIONS=22
    AUXILIARY_ESCAPE_CHECKS=22
    INTEGER_RESIDUALS=1200
    INTEGER_WARD_WITNESSES=244
    WITNESS=-29/648
    TAIL_JUMP=29/648
    PAYLOAD_SHA256=<computed lowercase hex>
    NEGATIVE_CONTROLS=8
    CERTIFICATE_RESULT=PASS

The primary launches breaker.py through the same interpreter with -I and a
540-second timeout, requires exit 0, empty stderr and unmodified byte equality,
then appends BREAKER_RAW_BYTES=IDENTICAL and RESULT=PASS, each followed by LF.
No newline normalization or subprocess import is allowed. The repository's
600-second verifier limit remains authoritative. A failed scientific check
emits its frozen falsifier identifier and RESULT=FAIL; unexpected execution
errors are recorded under the abandoned-pin procedure if no gate completes.

## 7. Custody, interpretation and next admissible work

Freeze PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py and FROZEN.sha256
in one commit. FROZEN.sha256 lists the other five files. Push, fetch/read
back every file and post the pin receipt on #1661 before first execution.
Afterwards add EXPECTED.txt, RUN.md, RESULT.md, REVIEW.md and README.md.
Required x86_64/aarch64 replay must use the unchanged scientific bytes.

The universal conclusion, if proved and audited, is conditional candidate-T
at NON-CANONICAL L1. Finite computations are reported at their actual scope.
This is a statement about the inherited action and transformation class,
not a physical prohibition. It excludes neither a local parent in a new
carrier nor a local completion with transformed auxiliary fields. Those
alternatives require a separately frozen law and genuine dynamical-content
test; this probe does not select them or promote any Canon claim.
