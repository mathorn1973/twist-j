# P-INTEGER-CUBIC-NOETHER-CLOSURE-1

Status: PROSPECTIVE  
Scope: NON-CANONICAL, NEW_DECLARED L1  
Owner: A. M. Thorn, session integer-cubic-noether-2026-10-19  
Ownership: https://github.com/mathorn1973/twist-j/issues/1653

## 1. Question, authority, custody, and earned-scope boundary

This probe asks two separate exact questions about the ACTUAL cubic
constraint extension of P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1 (#1652):

1. Does the complete finite-horizon action admit the first-order off-shell
   Noether completion specified below, with every neighboring current term
   included and every auxiliary variation taken in its declared space?
2. Does the resulting nearest-time generator family close under its Lie
   commutator on the unrestricted off-shell field domain?

The prospective analytical predictions are an exact first-order identity,
a generally nonzero second-order remainder, and nonclosure of this specific
generator family. A PASS certificate means that these separately stated
mathematical claims and their negative controls agree with the frozen
specification. It does NOT mean that the generator family is closed, that
an all-order gauge symmetry has been established, or that an Einstein
constraint algebra has been recovered.

Public Canon v103 main and peeled canon-v103 are at
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d; content commit is
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. SOURCE.md gives the actual five
normative hashes, byte sizes, mathematical inputs, and companion pins.

Before any scientific execution or import of either implementation, commit
and publish PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py, and
FROZEN.sha256. Read all six files back from GitHub and post the prospective
pin receipt. AST parsing, textual review and hashes are allowed before the
pin; scientific dry runs are not. Preserve the first completed outcome.

All state/parameter extensions, the formal deformation parameter epsilon,
gauge-generator choice and finite fixtures are NEW_DECLARED L1. The probe
does not create a new trajectory of the physical law of #1650, does not
claim gauge equivalence of the prepared fixed-mean histories, and does not
identify this action with Einstein-Hilbert or its cubic expansion. It does
not modify the inherited bank, native U, canonical action layer, physical
clock, or continuum interpretation. The local-current compatibility from
#1652 is retained; its mismatching public Phi/Pi summary is not an input.

## 2. Complete finite-horizon action and constrained domains

Fix m=324, g=1/m, e=(1,1,1,1,1), ell=(1,-1,0,0,0),
sigma=(1/2,1/2,0,0,0), and a in {-1,0,1}; A=a/4.
Vertices are r=0,...,4 modulo 5. There are ten oriented edges in order:

    edge r:   tail r, head r+1 mod 5, weight 29/324, r=0,...,4;
    edge 5+r: tail r, head r+2 mod 5, weight 65/324, r=0,...,4.

B maps vertex values to head-minus-tail differences, B^T is its ordinary
Euclidean adjoint, W is the diagonal edge weight matrix, and

    L = B^T W B = [188I-29(S+S^-1)-65(S^2+S^-2)]/324,
    C = 648I-324L,
    Pi0 f = f - mean(f)e,
    L_adj = 188I-65(S+S^-1)-29(S^2+S^-2),
    L_int = 324 L,
    L_int L_adj = 53605 Pi0.

For a horizon T>=5 the physical fields are x_n=(h_n,chi_n) in Q^5 x Q,
n=0,...,T. Endpoints x_0,x_T are held fixed. No mean condition is imposed
on h for this OFF-SHELL symmetry test. Define interior residuals

    R_h,n = h_(n+1)-2h_n+h_(n-1)+Lh_n-g chi_n ell,
    R_chi,n = chi_(n+1)-chi_n+chi_(n-1)-A-g<ell,h_n>,
    q_h,n = h_(n+1)-h_(n-1),
    q_chi,n = chi_(n+1)-chi_(n-1),       n=1,...,T-1.

The global inherited quadratic/affine action is

    A_auto = sum_(b=1)^T [ ||h_b-h_(b-1)||^2/2 + (chi_b-chi_(b-1))^2/2 ]
             + sum_(n=1)^(T-1) [ -<h_n,Lh_n>/2-chi_n^2/2+A chi_n
                                  +g chi_n<ell,h_n> ].

Its interior gradients are -R_h,-R_chi. On every bond b=1,...,T set

    e_h,b(r) = (h_b(r)-h_(b-1)(r))^2/2
                + (1/4)sum_(edge k incident to r) w_k(Bh_b)_k(Bh_(b-1))_k,
    e_chi,b(r) = sigma_r[ (chi_b-chi_(b-1))^2/2+chi_b chi_(b-1)/2
                          -A(chi_b+chi_(b-1))/2 ],
    e_int,b(r) = -(g/2)ell_r[chi_(b-1)h_b(r)+chi_b h_(b-1)(r)],
    e_loc,b = e_h,b+e_chi,b+e_int,b,
    E_star = (4342005/8683757) A^2,
    e_tot,b = e_loc,b+(E_star/5)e,
    H_b = sum_r e_loc,b(r)+E_star.

At interior n=1,...,T-1 define all ten edge current components

    j_h,n(k) = (w_k/4)(Bh_n)_k[q_h,n(tail k)+q_h,n(head k)],
    j_int,n(k) = -(g/4)q_chi,n[h_n(0)+h_n(1)] delta_(k,0),
    j_n = j_h,n+j_int,n.

The exact pointwise identity is

    C_n = e_loc,n+1-e_loc,n+B^Tj_n
        = (q_h,n * R_h,n + sigma q_chi,n R_chi,n)/2,                (2.1)

where * denotes componentwise multiplication. E_star cancels from the
bond difference. Local energy is not assumed pointwise nonnegative.

The auxiliary fields on every bond are tau_b,lambda_b in e^perp and
alpha_b in Q. On every interior n, p_n belongs to K_E=ker B^T (dimension
6) and N_n belongs to Q^10. E_hom is one fixed rational number, independent
of b and held fixed under all variations. Define

    S_0 = A_auto + 2sum_b <lambda_b,Ltau_b>
                   +2sum_n <N_n, WB(tau_(n+1)-tau_n)+p_n>,
    S_int = -sum_b alpha_b(H_b-E_hom)
            -sum_b <lambda_b,e_loc,b> + sum_n <N_n,j_n>,
    S_epsilon = S_0 + epsilon S_int.                               (2.2)

Epsilon is a formal deformation parameter; its order is NOT asserted to
be the homogeneous polynomial degree in the physical fields. S_int has
degree at most three in fields and multipliers, with fixed source context.
At epsilon=1 this is the reduced-field global constraint action of #1652.

All sums in (2.2) are global over the stated horizon. In particular, a
variation of h_n or chi_n includes the current terms at n-1, n, and n+1
whenever they exist. No central-current-only local functional substitutes
for the global action in any derivative test here.

## 3. Global constrained variations and constraint compatibility

The six-dimensional p variation gives P_KE N_n=0, equivalently N_n=Bxi_n
for a mean-zero vertex xi_n. Taking N_0=N_T=0, the tau variation gives

    Llambda_b+B^T W(N_(b-1)-N_b)=0.

Thus N_n=Bxi_n implies lambda_b=xi_b-xi_(b-1), with xi_0=xi_T=0.
Neither equation forces all N or lambda to vanish. The alpha variation
at epsilon=1 gives H_b=E_hom and does not force alpha_b=0.

Define the auxiliary constraint residuals at epsilon=1 by

    Hcon_b = 2Ltau_b-Pi0 e_loc,b,
    Mcon_n = 2WB(tau_(n+1)-tau_n)+2p_n+j_n.

For arbitrary auxiliary values (including ambient p outside K_E for the
identity alone),

    Hcon_(n+1)-Hcon_n
      = B^T Mcon_n-2B^Tp_n-Pi0 C_n.                              (3.1)

Therefore p in K_E, Mcon=0 and R_h=R_chi=0 propagate Hcon=0 from an
initial bond. This is a statement about the declared auxiliary constraints;
it is not identification with the ADM constraints.

For global coordinate differentiation use the exact independent bases

    V_i = e_i-e_4, i=0,1,2,3,
    K_0 = (1,1,1,1,1,0,0,0,0,0),
    K_1 = (-1,-1,0,0,0,1,0,0,0,0),
    K_2 = (0,-1,-1,0,0,0,1,0,0,0),
    K_3 = (0,0,-1,-1,0,0,0,1,0,0),
    K_4 = (1,1,1,0,0,0,0,0,1,0),
    K_5 = (0,1,1,1,0,0,0,0,0,1).

The global independent coordinates, in order, are interior h (time,site),
interior chi, all tau (bond,V_i), all p (time,K_i), all alpha (bond), all
lambda (bond,V_i), and all N (time,edge). There are
6(T-1)+4T+6(T-1)+T+4T+10(T-1)=31T-22 coordinates; T=5 gives 133.
Each individual coordinate has action degree at most two, so its centered
unit difference is its exact derivative. Joint directions can have degree
three, and their centered unit difference need not be exact.

## 4. Exact first-order Noether completion and its remainder

Choose any vertex-valued parameter psi_n in Q^5, n=1,...,T-1, with
psi_0=psi_T=0. Its mean is unrestricted. Define two vector fields:

    delta_0 N_n = Bpsi_n,
    delta_0 lambda_b = Pi0(psi_b-psi_(b-1)),
    delta_0 alpha_b = mean(psi_b-psi_(b-1)),
    delta_0 h = delta_0 chi = delta_0 tau = delta_0 p = 0;

    delta_1 h_n = psi_n * q_h,n / 2,
    delta_1 chi_n = <sigma,psi_n> q_chi,n / 2,
    delta_1 h_0 = delta_1 h_T = delta_1 chi_0 = delta_1 chi_T = 0,
    delta_1 of every auxiliary variable = 0.                         (4.1)

Writing X_psi x=delta_1 x, summation by parts and p in K_E give

    delta_0 S_0 = 0,
    delta_0 S_int = sum_n <psi_n,C_n>
                 = sum_n [<R_h,n,delta_1 h_n>+R_chi,n delta_1 chi_n],
    delta_1 S_0 = delta_1 A_auto = -delta_0 S_int.                   (4.2)

Consequently the exact directional variation is

    (delta_0+epsilon delta_1)S_epsilon = epsilon^2 U_psi,
    U_psi := delta_1 S_int.                                        (4.3)

The right side is generally nonzero. Equation (4.2) establishes the
first-order off-shell deformation identity, not an exact symmetry at
epsilon=1. The completion may change the mean of h even when psi has
mean zero; it is not claimed to preserve the prepared fixed-mean family.

For a joint direction d in the cubic action, use the exact derivative

    D_d S = [-S(x+2d)+8S(x+d)-8S(x-d)+S(x-2d)]/12,               (4.4)

or exact polynomial differentiation. The naive centered unit difference
is not a substitute. The primary checks (4.4) against its analytic global
gradient; the independent breaker may use dual/polynomial arithmetic.

If the multipliers are the pure auxiliary gauge values delta_0 psi
(alpha,lambda,N as in (4.1)), their bilinear terms cancel, and

    S_int = sum_n [<R_h,n,X_psi h_n>+R_chi,n X_psi chi_n].

For fixed x, let u=X_psi x. The quadratic Hessian pairing is

    A_auto''[u,u] = sum_(b=1)^T [||u_h,b-u_h,b-1||^2+(u_chi,b-u_chi,b-1)^2]
       +sum_(n=1)^(T-1)[-<u_h,n,Lu_h,n>-u_chi,n^2
                         +2g u_chi,n<ell,u_h,n>].

The exact Taylor identity is

    S_epsilon|pure-gauge = A_auto(x-epsilon u)
                            -(epsilon^2/2) A_auto''[u,u].          (4.5)

Thus the added term is equation-proportional. Its first-order contribution
can be removed by a field redefinition; the exact substitution leaves the
quadratic remainder displayed in (4.5). No exact nonlinear physical
equivalence or new interaction is inferred from this identity.

## 5. Generator commutator and the frozen nonclosure test

For fixed parameters psi,eta the Lie derivative convention is

    [X_psi,X_eta]x = D(X_eta x)[X_psi x]-D(X_psi x)[X_eta x].

If G_psi is the linear map x -> X_psi x on the full finite time array
(with zero endpoint rows), this is (G_eta G_psi-G_psi G_eta)x. It is the
opposite order to the bare matrix commutator [G_psi,G_eta].

For an interior layer whose indicated neighbors exist, its field component is

    (1/4)(eta_n*psi_(n+1)-psi_n*eta_(n+1))*h_(n+2)
    +(1/4)(eta_n*psi_(n-1)-psi_n*eta_(n-1))*h_(n-2)
    -(1/4)[eta_n*(psi_(n+1)+psi_(n-1))
            -psi_n*(eta_(n+1)+eta_(n-1))]*h_n.

Here subscripts n+1 etc. mean whole time subscripts, not addition to the
vector. The source component is the same scalar formula with parameters
<sigma,psi_n>, <sigma,eta_n> and field chi_n. Boundary parameter values
are zero, and absent second-neighbor terms with zero coefficient are
omitted. The map acts on all Q^5 x Q off-shell arrays with fixed endpoints.

At T=5 freeze psi_2=ell, eta_3=ell, all other parameter layers zero;
h_n=e/5 for n=0,...,5 except h_4=e/5+ell; every chi_n=0. Then

    [X_psi,X_eta]h_2 = -ell/4 = (-1/4,1/4,0,0,0),              (5.1)
    X_zeta h_2=0 for EVERY zeta, since h_3-h_1=0.

This proves nonclosure in the frozen family, even if a proposed zeta is
allowed to depend on this field state. It is not a no-go theorem for
additional generators, altered temporal stencils, on-shell relations,
higher-order auxiliary-dependent transformations, or integer gravity.
On the same field array, sum_r (X_eta h_3)(r)=1, displaying failure of
fixed-mean preservation by this family.

## 6. Explicit common-denominator integer lift

The field and auxiliary arrays are stored as signed integer numerators
over one positive integer D. Their subspace conditions are exact integer
conditions: sum tau=sum lambda=0 and B^T p=0. E_hom is an independent
fixed rational context stored as a signed numerator and positive denominator.
Parameters psi are integer arrays V over Qp>=1. No primitive or minimal
denominator, conserved budget, or finite gauge-orbit claim is made.

For the physical arrays h_n=P_n/D, chi_n=Y_n/D, set

    Qh_n=P_(n+1)-P_(n-1), Qchi_n=Y_(n+1)-Y_(n-1),
    Ah_n=m(P_(n+1)-2P_n+P_(n-1))+L_int P_n-Y_n ell,
    Achi_n=m(Y_(n+1)-Y_n+Y_(n-1))-81 a D-<ell,P_n>.

Then R_h=Ah/(mD) and R_chi=Achi/(mD). With the same D at ALL layers,

    Eb(r)=2m(P_b(r)-P_(b-1)(r))^2
       +sum_(k incident r)(mw_k)(BP_b)_k(BP_(b-1))_k
       +(2sigma_r)[m(Y_b-Y_(b-1))^2+mY_bY_(b-1)-81aD(Y_b+Y_(b-1))]
       -2ell_r[Y_(b-1) P_b(r)+Y_b P_(b-1)(r)],
    Jn(k)=(mw_k)(BP_n)_k[Qh_n(tail k)+Qh_n(head k)]
            -Qchi_n[P_n(0)+P_n(1)]delta_(k,0).

Here Eb=4mD^2 e_loc,b and Jn=4mD^2 j_n. The current scale differs from
the advancing-denominator current scale in #1652 because this horizon
uses one common D. The integer off-shell identity is

    E_(n+1)-E_n+B^T Jn = 2Qh_n*Ah_n+(2sigma)Qchi_n Achi_n.       (6.1)

Multiplying delta_0 S_int+delta_1 S_0 by 4mD^2 Qp therefore gives an
exact zero integer, without evaluating any floating point quantities.

For integer epsilon, x+(delta_0+epsilon delta_1)x has a common denominator
Dnew=20D Qp. In addition to rescaling the original numerators by 20Qp,
the tangent increments at interior n and bond b are exactly

    h:       10 epsilon V_n*Qh_n,
    chi:     5 epsilon(V_n(0)+V_n(1))Qchi_n,
    alpha:   4D sum_r(V_b(r)-V_(b-1)(r)),
    lambda:  4D[5(V_b-V_(b-1))-sum_r(V_b(r)-V_(b-1)(r))e],
    N:       20D B V_n,
    tau,p:   0.                                                   (6.2)

V_0=V_T=0. This encodes a finite tangent displacement for checking the
polynomial; it is not claimed to be a finite symmetry transformation.

## 7. Frozen finite fixtures, order, witnesses, and falsifiers

### 7.1 Six off-shell action configurations

All have T=5, D=60, a in {-1,0,1}, seed s in {0,1}, ordered a then s.
Define the integer function

    f(t,i,c) = ((17t+11i+7s+5a+3c) mod 19)-9,

where mod gives residues 0,...,18. The common numerators are:

    P_t(r)=f(t,r,0), Y_t=f(t,0,1),                 t=0,...,5;
    tau_b=sum_(i=0)^3 f(b,i,2)V_i,                b=1,...,5;
    p_n=sum_(i=0)^5 f(n,i,3)K_i,                 n=1,...,4;
    alpha_b=f(b,0,4),
    lambda_b=sum_(i=0)^3 f(b,i,5)V_i,
    N_n(k)=f(n,k,6),
    E_hom=(s+1)/(7+a^2).

All arrays above except E_hom are divided by D=60. At epsilon=1 compare
all 133 independent global coordinate derivatives, giving 798 checks.
Check (2.1), (3.1) and (6.1) at all 4 interiors and 5 vertices of each
configuration, giving 120 vertex checks for each identity.

For each configuration use 21 parameter arrays: first the 20 time/site
unit arrays psi_n=e_r at n=1,...,4 and r=0,...,4 (time-major order), then
the rational array psi_n(r)=f(n,r,7)/7. Endpoints are zero. This gives
126 parameter/configuration pairs. For each pair check separately
delta_0 S_0=0, delta_0 S_int=sum psi C, delta_1 S_0=-sum psi C, their
cancellation, and the integer Noether lift. Then for epsilon in
{-1,0,1,2} check the COMPLETE global directional variation (4.3) using
(4.4), the Taylor/field-redefinition identity (4.5), and the integer
tangent lift (6.2). Each of these three families has 504 checks.

For each configuration and all 190 unordered pairs of its first 20
unit parameters, compare the commutator evaluated by composed vector
fields with the closed temporal formula in section 5, including scalar
and endpoint components. This gives 1140 complete-array comparisons.

### 7.2 Exact witnesses and ten negative controls

1. GLOBAL NEIGHBORS: T=5,a=0,E_hom=0, all fields zero except
   h_1=(6,11,11,6,6)/40; all auxiliary fields zero except N_1=edge unit0.
   Relative to N=0 the global gradients at time2 change by
   h: (29/10368,29/10368,0,0,0), chi: -17/51840. A central-current-only
   action at2 omits these. Freeze both values.
2. OFF-GAUGE REMAINDER: T=5,a=0,E_hom=0,h_3=vertex unit0, all other h
   and all chi zero; only alpha_3=1 among auxiliary variables. Set
   psi_2=psi_3=vertex unit0, all other psi zero. Then
   delta_0 S_int=1/2, delta_1 S_0=-1/2 and U_psi=115/324.
   At epsilon=1 the full variation is NONZERO: 115/324.
3. NAIVE CENTRAL DIFFERENCE: on the same witness, the unit centered
   difference along delta_0+delta_1 minus the exact derivative is -1/8.
   The exact derivative must use (4.4) or polynomial differentiation.
4. FIELD REDEFINITION: keep that physical field and psi, but replace
   all multipliers with their pure-gauge delta_0 psi values. At epsilon=1,
   S_epsilon-A_auto(x-X_psi x)=-115/648, not zero. Equation (4.5) holds.
5. WRONG COMPLETION SIGN: on witness2, delta_0 S_int-delta_1 S_0=1,
   whereas their correct sum is zero.
6. OMIT HOMOGENEOUS LAPSE CHANGE: on witness2, set delta_0 alpha=0,
   keeping its other changes and delta_1. The first-order defect is -1/10.
7. OMIT INTERACTION CURRENT: T=5,a=0,E_hom=0,h_2=vertex unit0,
   chi_3=1, all other physical/auxiliary values zero, psi_2=vertex unit0.
   Removing j_int from S_int while retaining the same physical action
   gives delta_0 S_int+delta_1 S_0=-1/1296, not zero.
8. DROP CO-CLOSURE: T=5,a=0,all fields zero except p_2=edge unit0
   (outside the admitted p domain), psi_2=vertex unit0. Then delta_0 S_0=-2.
9. GENERATOR NONCLOSURE: the data of (5.1) give -ell/4 at time2 while
   the entire proposed nearest-time generator family is zero there.
10. FIXED-MEAN ESCAPE: on that same data, sum_r X_eta h_3(r)=1 even
   though each h_n has sum1 and eta_n has mean0.

These controls test ten different erroneous extensions of the claimed
scope. Nonzero control witnesses are predicted successes of this audit,
not hidden or retuned failures of a claimed closed gauge theory.

### 7.3 Certificate grammar and independent implementation

Each implementation emits this exact 22-line ASCII/LF certificate on
success; the two digest fields are computed, not read from EXPECTED.txt:

    CERTIFICATE=P-INTEGER-CUBIC-NOETHER-CLOSURE-1
    AUTHORITY_FILES=5
    GLOBAL_CONFIGURATIONS=6
    GLOBAL_VARIATIONS=798
    CONTINUITY_VERTICES=120
    CONSTRAINT_PROPAGATION_VERTICES=120
    INTEGER_CONTINUITY_VERTICES=120
    NOETHER_IDENTITIES=126
    INTEGER_NOETHER_IDENTITIES=126
    DEFORMATION_CHECKS=504
    FIELD_REDEFINITION_CHECKS=504
    INTEGER_TANGENT_CHECKS=504
    COMMUTATOR_CHECKS=1140
    GLOBAL_GRADIENT_SHA256=<computed lowercase SHA-256>
    NOETHER_PAYLOAD_SHA256=<computed lowercase SHA-256>
    GLOBAL_NEIGHBOR_GRADIENT=29/10368,29/10368,0,0,0;-17/51840
    SECOND_ORDER_REMAINDER=115/324
    NAIVE_CENTRAL_DEFECT=-1/8
    FIELD_REDEFINITION_DEFECT=-115/648
    GENERATOR_NONCLOSURE=-1/4,1/4,0,0,0
    NEGATIVE_CONTROLS=10
    CERTIFICATE_RESULT=PASS

The gradient payload, one LF per record, is

    a|s|i|value\n

in configuration order, then global-coordinate order of section3, with
zero-based coordinate index i=0,...,132. The Noether payload is

    a|s|p|d0Sint|d1S0|U\n

in configuration order and parameter index p=0,...,20. Each rational is
printed as a signed decimal integer when its denominator is1, otherwise
as its reduced signed numerator, slash, and positive denominator. There
are no spaces in either payload. Hash their ASCII bytes with SHA-256.

The primary uses explicit incidence arrays, integer numerator formulas,
and analytic complete global gradients. The breaker is written from this
specification independently of the primary: it uses a distinct action
evaluation/differentiation strategy and independently evaluates the
integer, symmetry, commutator, and witness checks. No companion or primary
runtime import is allowed. No expected-output file is consumed as data.

verify.py launches breaker.py as a separate process using the same Python
executable and -I. Require child exit0, empty stderr and byte-identical
unmodified certificate stdout; append exactly these two final lines:

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

Successful primary output thus has24 LF-terminated lines. Assertions use
only exact integer/Fraction arithmetic and standard-library Python3.12.
Registered falsifiers are AUTHORITY, DOMAIN, INCIDENCE, GLOBAL_GRADIENT,
CONTINUITY, CONSTRAINT_PROPAGATION, INTEGER_CONTINUITY, AUXILIARY_GAUGE,
NOETHER, INTEGER_NOETHER, DEFORMATION, FIELD_REDEFINITION, INTEGER_TANGENT,
COMMUTATOR, NEIGHBOR_WITNESS, REMAINDER_WITNESS, CENTRAL_WITNESS,
CONTROL, NONCLOSURE, CERTIFICATE, BREAKER_BYTES. A caught scientific
falsifier emits FALSIFIER=<key> and RESULT=FAIL with exit0; unexpected
runtime failure consumes the pin under POLICY.md's abandonment route.
