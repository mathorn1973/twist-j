# Modal accounts, funded work and a common-action boundary

NON-CANONICAL L1 analytical candidate. These are exact derivations and a
new, explicitly declared work-account extension. They establish neither a
physical energy reading nor a Planck constant. No scientific program was
executed in preparing this document.

## 1. What the native contact conserves

Let O=Z[j], Phi_5(j)=0, p=j^2, a=1-j and u=a*p^g. Define

    Q(x)=Tr(x conjugate(x))/2,
    B(x,y)=Tr(x conjugate(y))/2,
    Q(x+y)=Q(x)+Q(y)+2B(x,y).

B is real and symmetric. Q(u)=5 and B(u,pu)=0. The total contact C is
identity when x-y is not in 2O; otherwise

    C(x,y)=((x+y+p(x-y))/2, (x+y-p(x-y))/2).

It preserves the sum and Q(x)+Q(y), and C^5=I. More precisely, the accounts

    I_plus=Q(x+y)/2,       I_minus=Q(x-y)/2

are separately invariant and sum to Q(x)+Q(y). Their exact budgets are:

| Input | I_plus | I_minus | Input port Q | Output port Q |
|---|---:|---:|---|---|
| (u,3u) | 40 | 10 | (5,45) | (25,25) |
| (u,-3u) | 10 | 40 | (5,45) | (25,25) |
| (u,-u) | 0 | 10 | (5,5) | (5,5) |

These output pairs are the summed two-embedding Q accounts. They do not
assert equality of the individual embedding powers. Writing s=x+y,d=x-y,

    Q(x)=(I_plus+I_minus)/2+B(s,d)/2,
    Q(y)=(I_plus+I_minus)/2-B(s,d)/2.

The contact replaces B(s,d) by B(s,pd). Thus the transferred 20 in either
c=3 or c=-3 preparation is port interference; neither modal account changes.
The c=-1 control has no transfer. Equal-amplitude symmetric and
antisymmetric states (u,u) and (u,-u) both cost 10 in native Q. Their
native-Q gap is zero. Their sums differ, so C alone cannot interchange
them; a work comparison requires another declared operation.

## 2. The complete two-site Hermitian family

At one complex embedding use normalized sum/difference coordinates and
projectors P_plus,P_minus. The admitted linear map is

    U=P_plus+p_sigma P_minus,       p_sigma != 1.

A Hermitian quadratic cost z^*Kz is invariant exactly when K commutes with
U. Its full family is

    K=k_plus P_plus+k_minus P_minus,       k_plus,k_minus real.

Positivity requires both coefficients nonnegative. For equally weighted
trace costs this reads

    E=A[Q(x)+Q(y)]+2D B(x,y),       A >= |D|.

The symmetric/antisymmetric weights are A+D and A-D. Their costs at
(u,+/-u) are 2(A+/-D)Q(u); the antisymmetric-minus-symmetric gap is
-4D Q(u). Native Q chooses A=1,D=0. An assigned D can create a gap, but
invariance does not select it or provide its work source. In particular,
Delta Q(x-y)/2 assigns a difference-mode cost using a new coefficient.

## 3. Overlapping contacts constrain a common quadratic cost

Take a connected graph of N>=2 sites at a fixed embedding. For each edge
ij put w_ij=e_i-e_j and P_ij=w_ij w_ij^*/2. Its admitted map is

    U_ij=I+(p_sigma-1)P_ij.

A common Hermitian cost is conserved by every edge precisely when
[K,P_ij]=0 for every edge. Each w_ij is then an eigenvector of K.
Edges sharing a vertex have nonzero inner product; Hermitian eigenvectors
with different eigenvalues are orthogonal. Connectivity therefore gives
one eigenvalue on the span of all edge differences, which is 1-perp.
The complete family is

    K=A I+D 11^*,       A,D real.

Conversely every such K commutes with all edges. Positivity is A>=0 and
A+ND>=0. Strict onsite additivity forces D=0. A fixed finite interaction
range also forces D=0 on paths containing sites farther apart than that
range: every off-diagonal entry of D11^* equals D. This argument does not
exclude a global sum account or apply a large-path premise to a tiny graph.

This classification also applies to invariance under the actual gated
integral contact. Every point of 2O^N admits every edge. For each edge the
real homogeneous quadratic difference E(U_ij z)-E(z) therefore vanishes
there. In the full Minkowski space 2O^N is a full-rank lattice. Values on
basis vectors and their pairwise sums force every quadratic coefficient
to vanish. At one embedding the subset 2(Z+Zj)^N supplies the same
real-basis argument. Thus gated invariance implies linear-branch
invariance throughout the relevant real space; refused points impose
nothing further. A finite five-phase alphabet alone would not justify
this extension.

For completeness, on both complex embeddings the full Hermitian family is

    E=A1||z1||^2+A2||z2||^2+D1|S1|^2+D2|S2|^2
      +2 Re(T conjugate(S1) S2),       Sr=sum_i z_ri.

The diagonal blocks follow the preceding proof. For an off-diagonal block
X, invariance gives (p1-1)P_ij X=(p2-1)X P_ij. Since p1!=p2 and neither
is 1, projection onto its four blocks gives P_ij X=X P_ij=0.
Connectivity yields X=T11^*. Locality removes the sum terms; equal
embedding weights then leave total Q up to scale.

For N>=3, a single such invariant K cannot also generate each individual
edge contact by exp(-itK/A_action) with the standard complex symplectic
structure. K acts as a scalar on 1-perp, whereas an edge U_ij has both
p_sigma and 1 there. This is a common-fixed-generator obstruction. It
excludes neither a Hamiltonian for a complete scheduled word, a changed
symplectic structure, time-dependent controls nor an enlarged carrier.

## 4. A constructive funded work account

Here is a reversible extension with an explicit work source. For
v=(x,y,z), choose an integer lambda>=0 and define

    E_lambda(v)=Q(x)+Q(y)+Q(z)+lambda Q(y-z),
    F=C_12,       F^(-1)=F^4,
    delta_d(v)=E_lambda(F^d v)-E_lambda(v),       d in {+1,-1}.

Add a nonnegative integer bank b and direction d. The step is

    if b >= delta_d(v):
        (v,b,d) -> (F^d v, b-delta_d(v), d)
    otherwise:
        (v,b,d) -> (v,b,-d).

Negative costs are always affordable. Both branches conserve E_lambda+b.
The inverse uses F^(-d) and its cost with the same rule, retaining d on
acceptance and flipping it on rejection. An accepted reverse costs the
negative of the forward cost and restores the original nonnegative bank.
For a rejected step, the reverse proposal is precisely the unaffordable
original proposal. Hence the inverse rejects and restores the direction.
Equivalently, T^(-1)=R T R with R(v,b,d)=(v,b,-d).

Each shell E_lambda+b=H is finite. In the power basis x=sum_(k=0)^3 a_k j^k,

    Q(x)=[5 sum a_k^2-(sum a_k)^2]/2 >= (sum a_k^2)/2.

Thus Q(x)+Q(y)+Q(z)<=H bounds all twelve integer coordinates, and b<=H.
The direction has two values. This proves finite reversible positive
account shells without assuming an infinite overdraft.

For the admitted preparation

    (u,-u,u) -> (pu,-pu,u),

all three native Q accounts remain 5, while

    Q(y-z): Q(-2u)=20 -> Q(-(1+p)u)=10.

The bank therefore gains exactly 10lambda. Lambda=0 gives no exchange.
Lambda is a new relative coefficient beside the fixed native coefficient
1; it is not merely an overall unit change. The bank, direction and
reflection rule are additional resources. This construction has not
compiled them into native auxiliary O slots. Nor does conservation of the
enlarged account prove that E_lambda generates F. It provides a funded
work reading whose extra choices are explicit.

## 5. A common action across the two embeddings

Use sigma1(j)=exp(2pi i/5), sigma2(j)=exp(4pi i/5) and the convention
exp(-i H tau/A_action). Relative to the unchanged symmetric mode, gaps
Delta1,Delta2 realizing the two difference phases must satisfy

    Delta1 tau/A_action=(2pi/5)(3+5n),
    Delta2 tau/A_action=(2pi/5)(1+5m),       n,m integers.

Consequently

    Delta1/Delta2=(3+5n)/(1+5m).

For positive gaps and positive tau,A_action, n,m>=0. The least positive
individual branch representatives give 3:1; this is not a minimum over
all possible ratios. Equal trace weights cannot satisfy the congruences.

Neither can a nonzero Galois-conjugate gap pair from Q(sqrt(5)). If its
ratio r were rational, applying conjugation would give r=1/r, hence
r=+1 or -1. The displayed phase ratio can equal neither: the required
integer equations would make 2 or 4 divisible by 5. This concerns
normalized modal energy gaps and a common duration/action, not an
arbitrary comparison of unnormalized field amplitudes.

A declared pair (Delta1,Delta2)=(3g,g), g>0, does work with
A_action=5g*tau/(2pi). It adds an embedding-dependent energy reading;
it does not select g, fund it natively, or establish a physical action
quantum. ACTION.md gives a separate arithmetic discrete-action
construction and its rational-symplectic boundary.

Finally, alpha=kappa*q_e^2/(A_action*v) still requires a charged response
kappa, charge identification q_e and propagation coefficient v on the
same carrier as the action. Here the Coulomb convention is
V(R)=kappa*q1*q2/R in dimensionless energy and length units; any 4pi
factor is included in kappa. A common energy rescaling can cancel in
alpha. The unresolved issue is therefore not a free overall scale alone:
it is the missing selected, funded action/energy relation and the
independent charged-response relation on one carrier.

## 6. The resulting conditional coupling equation

With the least positive branch representatives above, Delta2=g and
A_action=5g*tau/(2pi). If this same coefficient governs the charged
response, the operational candidate becomes

    alpha_op = 2pi*kappa*q_e^2 / (5g*tau*v).

This is a consistency equation, not a computed alpha value. Neither the
bank coefficient lambda nor an observed port transfer can be substituted
for g without proving the energy/action identification. In particular,
ENERGY's funded E_lambda and ACTION's G are separate constructions;
no common enlarged variational generator for them is claimed.

The standard physical comparison is alpha=e^2/(4pi epsilon0 hbar c),
with hbar=h/(2pi); see [NIST's SI definition discussion](https://www.nist.gov/pml/special-publication-330/sp-330-section-2).
Thus A_action must be identified with the reduced action coefficient,
not with h, if the phase convention exp(-iHt/A_action) is used.

An electron-mass unit anchor cannot change the dimensionless ratio.
Explicitly, for conversion units E0,L0,T0,

    Coulomb coefficient = E0*L0*(kappa*q_e^2),
    reduced action       = E0*T0*A_action,
    speed                = (L0/T0)*v.

All three conversion units cancel in alpha_op. After an electron state
and its rest-energy number are independently identified, anchoring its
mass can calibrate the chosen conversion scheme. It does not determine
the still missing ratio kappa*q_e^2/(g*tau*v). Predictive closure requires
that ratio from the same carrier, with a normalized charged preparation,
work/recoil reading and clock, before inserting the measured alpha.
