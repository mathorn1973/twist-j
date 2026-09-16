# P-TT-NATIVE-QUADRATIC-EMISSION-1

Status: FORMAL PUBLIC PROBE preregistration. No result is recorded here.
Owner: ChatGPT-TT-SOURCE-20260910-B. Object lock: issue #931.
Authority: Public Canon v83, main 51dee9705628e0c9f7bfc7082df46af46ed314b3.
Content commit: 528e868abaa368403ac3c7e81ebd326a3d81b588.
Canon SHA-256: aaaa9773390b3283f6ea72df1ef47fb5d29f80db2197b2b6419e32b65757bca6.
Action layer: L1 source descriptor -> L1 TT field. No L2-L6 lift is claimed.
Owner target: TT-SOURCE [O]. TT-VECTOR-STATE-NORMALIZATION [O] is not targeted.

## 1. Frozen question

Does the already declared K1/TM source packet admit a parameter-free, typed,
quadratic spin-2 emission map into an independently propagated TT field that
satisfies the registered flat TT propagation type and the registered planar
source conservation constraints?

This probe tests the positive mathematical core needed by TT-SOURCE. It does
not itself edit Canon, Registry, Frontier or gates. A later reviewed fold owns
any status move.

## 2. Public inputs and source packet

Use the public Thue-Morse bit

    theta_n = s_2(n) mod 2.

For a legal trailing four-bit packet w=(w0,w1,w2,w3), define

    u0 = w2-w0,
    u1 = w3-w1.

The probe freezes the theorem target that the complete length-four Thue-Morse
factor language is exactly

    W = {0010,0011,0100,0101,0110,1001,1010,1011,1100,1101},

and that its stationary factor masses are

    mu(0110)=mu(1001)=1/6,
    mu(w)=1/12 for the other eight words.

This must be derived from the substitution 0->01, 1->10 and its exact factor
frequency equations, not inferred from the optional K1 law. The frequency
statement is a native-source consistency theorem only. It is not a physical
occurrence law or an L6 measure claim.

The public orientation-source function is

    omega(a,b,c)=c-a.

The probe must verify

    u0=omega(w0,w1,w2),
    u1=omega(w1,w2,w3)

for every legal w.

Use the public K1 source amplitudes, in the selected plus frame,

    b_t(r)=[delta_(r,u_t)+delta_(r,u_t+1)]/sqrt(2),
    H_t(r)=b_t(r)^2=[delta_(r,u_t)+delta_(r,u_t+1)]/2,
    t=0,1, r in Z/5.

The typed source object is the ordered packet

    Src(w)=(w,(u0,u1),(b0,b1),(H0,H1)).

The source doublet b_src is an emitter descriptor. It is not the outgoing
square-root field of the radiated h.

## 3. Frozen emission map and admissible local class

Let V be the real spin-1 O(2) doublet and W_2 the real traceless spin-2
doublet. Freeze the local homogeneous quadratic class A of maps

    Q : V x V -> W_2

with all of the following conditions:

A1. O(2)-equivariance, including reflection. Rotations act with weight 1 on
    each input and weight 2 on the output; reflection is complex conjugation.
A2. Ordered-slice antisymmetry: Q(y,x)=-Q(x,y).
A3. Locality: no neighbouring site, counter, hidden state or external carrier
    enters Q.
A4. Homogeneous degree two with real coefficients and the public spin-square
    normalization on one-slice terms.

The theorem target is

    A = { kappa [y^2-x^2] : kappa in R },

where complex notation identifies V with C and W_2 with C at the representation
level. No uniqueness is claimed outside this frozen class.

Freeze source-work normalization A5: with zero initial TT field, the radiation
energy deposited by an isolated packet equals the inherited K1 kinetic source
channel

    epsilon_K1(r)=(H1(r)-H0(r))^2/2.

A5 must force kappa^2=1 on every nonstatic packet. Forward source order fixes
kappa=+1. Therefore the candidate emission map is

    Phi(Src)=b1^2-b0^2=H1-H0.

No dimensionless coefficient may be tuned or inserted after the pin.

## 4. Independent TT field and source stress

The emitted field h is independent of b_src. There is no pullback of an action
through h=v^2 and no outgoing-vector evolution is assumed.

On the selected planar Z/5 carrier use exactly the public rational stencil

    L=[188 I-29(S+S^-1)-65(S^2+S^-2)]/324.

For one isolated source packet use local emission time m>=0 and freeze

    h_0=h_1=0,
    R_L h_1=Phi,
    R_L h_m=0 for m>=2,
    R_L z_m=z_(m+1)-2z_m+z_(m-1)+L z_m.

Equivalently the force sequence is f_1=Phi and f_m=0 otherwise. The recurrence
coefficient of h_(m+1) is one, so the intended solution is total, unique and
prefix compatible.

Write Phi=Phi_+ + i Phi_x. In the public planar constrained source notation,
freeze

    rho=0,
    J_1=J_2=J_3=0,
    S_13=S_23=S_33=0,
    S_11= Phi_+/(2 lambda),
    S_22=-Phi_+/(2 lambda),
    S_12=S_21=Phi_x/(2 lambda),
    lambda=216 pi inherited from the public action.

Thus the source is purely transverse TT stress. The probe does not alter
lambda or treat it as a new free coefficient.

The registered planar source conservation identities to be satisfied are

    (1-E) rho = D J_3,
    (E^-1-1) J_i = D S_i3,  i=1,2,3.

They must hold exactly without projecting away a failed source component.

## 5. Registered spin and propagation compatibility

The public square assigns weight 1 to the source doublet and weight 2 to its
quadratic TT image. The registered propagation coefficient is

    c(s)=1-s^2.

The probe freezes the compatibility requirements

    c(1)=0,
    c(2)=-3.

This checks the representation type of the source and output. It does not
rederive the Schwarzschild endpoint or claim a new curved-background theorem.

## 6. Local energy/current compatibility

Use exactly the public v83 planar specialization of the local TT energy and
current. For any h let

    e_(n+1/2)(x)= (h_(n+1)(x)-h_n(x))^2/2
       +(1/4) sum_(edges incident x) w_e (B h_(n+1))_e (B h_n)_e,

    j_n(e)= (w_e/4) (B h_n)_e
            [q_n(tail e)+q_n(head e)],
    q_n=h_(n+1)-h_(n-1).

The off-shell identity to be proved is

    Delta e + B^T j = q_n R_L h_n/2.

At onset this gives field gain Phi^2/2 pointwise because h_0=h_1=0 and
h_2=Phi. Freeze the source radiative channel as the inherited K1 kinetic
channel before the impulse and spent after it:

    e_src,1/2=Phi^2/2,
    e_src,n+1/2=0 for n>=1,
    j_src=0.

This is not asserted to be the complete physical source energy. It is the
specific radiative source channel being transferred. The total local ledger
must satisfy

    Delta(e+e_src)+B^T j=0

at onset and the ordinary source-off identity afterwards.

For the v83 auxiliary completion define

    2 L tau_(n+1/2)=Pi0(e+e_src),
    p_n=-j_n/2-WB(tau_(n+1/2)-tau_(n-1/2)).

The probe must verify B^T p_n=0 on the isolated packet histories. This is a
compatibility audit of the already selected v83 auxiliary recipe, not a new
FRW or GR claim.

## 7. Frozen falsifiers

F1. The exact length-four TM language differs from W, or its stationary factor
    masses differ from the printed K1 optional law.
F2. Either overlapping u_t differs from the public omega formula.
F3. The exact O(2)-equivariant antisymmetric local homogeneous quadratic class
    has dimension other than one, or its generator is not y^2-x^2.
F4. Source-work normalization fails to force kappa^2=1 on a nonstatic packet.
F5. Phi has nonzero spatial mean; a static packet emits; a nonstatic packet
    has Phi=0; or the zero-start recurrence is not total and prefix compatible.
F6. The frozen transverse source violates a registered planar source
    conservation identity.
F7. The local off-shell field identity, onset source-work transfer, source-off
    conservation or auxiliary co-closure B^T p=0 fails.
F8. The representation weights fail c(1)=0 or c(2)=-3.
F9. Any new unfrozen dimensionless source coefficient is required to make a
    preceding condition pass.

Zero tolerance. No word, frequency, source map, coefficient, action factor or
failure condition may move after this preregistration is pinned. A fired
falsifier is retained.

## 8. Proof and computation discipline

The verifier will use only the Python standard library, integers and Fraction.
It will independently:

1. solve the exact factor-frequency equations of the Thue-Morse substitution;
2. derive the ten legal length-four factors by even/odd start decomposition;
3. solve the complete coefficient linear system for class A using the
   infinitesimal O(2) generator, reflection and slice exchange;
4. audit all ten source packets exactly;
5. prove the local energy identity by sparse polynomial arithmetic;
6. evolve exact rational histories for finite audit fixtures and solve the
   mean-zero Poisson problem by independent Fraction Gaussian elimination;
7. check the source conservation and spin coefficients.

The finite history audit is not an all-time theorem. Totality and prefix
compatibility follow from the displayed recurrence, and the off-shell balance
follows from the symbolic polynomial identity. The class-A statement follows
from the exact coefficient system, not from sampling rotations.

Commit and push this PREREG.md and the accepted verify.py before the first
formal execution. Compilation and static inspection are allowed before the pin.
After the pin, execute the exact verifier from repository root, preserve exact
stdout in EXPECTED.txt and record the run in RUN.md. The PR changes exactly one
probe directory. GitHub's required x86_64 and aarch64 jobs must reproduce the
same pinned bytes before a computation-only T can be earned. An independent
proof review may separately establish theorem status.

## 9. Explicit nonclaims

No outgoing vector state dynamics, fourth-moment normalization, scalar
comparison, numerical r_T(k), occurrence law, detector, apparatus, SI value,
irreversible radiation flux, overlapping-source superposition law, full FRW
reaction, full inhomogeneous GR, Stage-B pullback or global decoder uniqueness
is claimed. TT-VECTOR-STATE-NORMALIZATION remains a separate owner.
