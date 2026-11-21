# A path-funded Hamiltonian contact completion

**NON-CANONICAL / L1 / conditional analytical candidate-T.**

This is a new declared real completion of the specified integral contact.
It is not the original funding/reflection rule of PR #1894. Its real clock,
sector tags, mixed symplectic form and safe funding guard are explicit added
data. Integral contact states and an integer bank are recovered on the
declared stroboscopic sections. No physical action quantum, native-U
compilation, electrical charge or alpha closure is asserted.

The public reservation is #1909. The inherited mathematical inputs are the
contact law in Public Canon v109 and the real-coordinate symplectic
construction in PR #1894 at commit
`248ce7d7d2af016cb1e96a033014462972425993`. This proof does not consume that
PR's scientific executable or its finite observed output.

## 1. Integral data and real carrier

Let K=Q(j), O=Z[j], j^4+j^3+j^2+j+1=0, rho=j^2 and u=1-j.
The selected two complex embeddings are

    sigma_1(j)=exp(2 pi i/5),  sigma_2(j)=exp(4 pi i/5).

For a in K, write a_i=sigma_i(a). The positive half-trace account is

    Q(a)=Tr_(K/Q)(a conjugate(a))/2=|a_1|^2+|a_2|^2.

The same expression defines Q on K tensor_Q R, identified with C^2.
For z=(x,y,z_3,...,z_N), N>=3, put

    R(z)=sum_sites Q(z_site),
    I(z)=Q(y-z_3),
    E_lambda(z)=R(z)+lambda I(z),        lambda>=0.

For the integral stroboscopic carrier take lambda in Z_(>=0). A bank
coordinate b is initially nonnegative. Its reading is the literal coordinate
b, not a quotient that identifies different bank values.

On x-y in 2O the admitted pair map is

    F(x,y)=(s+rho d,s-rho d),  s=(x+y)/2, d=(x-y)/2.

On the refused complement the total contact C is identity. At admitted
integral inputs s,d belong to O. The admitted map preserves the pair sum,
both embedding norms, Q(x)+Q(y), and parity admission. The refused map also
preserves these data. C^5=identity on both branches.

## 2. One fixed real interpolation of the admitted branch

The primitive integral form on each O site is

    Omega_0(a,c)=Tr_(K/Q)(gamma a conjugate(c)),
    gamma=(j-j^(-1))/5.

Its matrix in (1,j,j^2,j^3) is

    [[ 0, 1, 0, 0],
     [-1, 0, 1, 0],
     [ 0,-1, 0, 1],
     [ 0, 0,-1, 0]].

Indeed its (k,l) entry is
[Tr(j^(k-l+1))-Tr(j^(k-l-1))]/5. The trace is 4 at exponents divisible
by five and -1 otherwise. The displayed matrix has Pfaffian 1 and
determinant 1.

Define the positive real constants

    g_1=2 sin(2 pi/5)/5,  g_2=2 sin(pi/5)/5.

If a_i=q_i+i r_i, the real form is

    Omega_0=2 g_1 dq_1 wedge dr_1+2 g_2 dq_2 wedge dr_2.

Use the same per-site form at every site:

    omega=sum_sites Omega_0.

Fix tau>0 and the positive branch representatives

    theta_1=6 pi/5,  theta_2=2 pi/5.

These representatives are a declared choice. A five-step return does not
select them uniquely. In the pair sum/difference variables, the inherited
per-site form is 2 Omega_0(s)+2 Omega_0(d). Define

    h(z)=sum_(i=1,2) [2 g_i theta_i/tau] |d_i|^2.

The spectator sites and s have zero h-generator. Adopt the convention

    i_(X_h) omega=dh.

The relative-sector equations are exactly

    dot d_i=-i(theta_i/tau)d_i.

For example its form is 4 g_i dq_(d,i) wedge dr_(d,i), while the
derivative of the corresponding h term is
4 g_i theta_i(q_(d,i)dq_(d,i)+r_(d,i)dr_(d,i))/tau. Thus

    d_i(a)=exp(-i theta_i a/tau)d_i(0),  s(a)=s(0).

Write this complete real symplectic flow as phi_h^a. At duration tau,
exp(-i theta_i)=sigma_i(rho), so phi_h^tau is the admitted map F.
At duration tau/2 the multiplier is -j in both embeddings:

    exp(-3 pi i/5)=sigma_1(-j),
    exp(-pi i/5)=sigma_2(-j).

R and h are invariant throughout the flow, not only at the endpoint.
The flow has period 5 tau. In particular it exists for all real a.

The intermediate real trajectory is added structure. Although full- and
half-step snapshots of admitted integral data are integral, multiplication
by -j has order ten and is not an isolated-pair power of multiplication
by j^2. This is not a compilation of smaller ticks into the contact alphabet.

## 3. Complete path-safe HOLD law

Put H=E_lambda(z)+b. Add two explicit discrete sector tags epsilon,delta.
At each integral stroboscopic section require

    epsilon=1 iff x-y belongs to 2O,
    delta=1 iff H >= (1+2lambda)R.

Equality belongs to the funded sector. The tags are counted as added
resources. Between sections they are retained labels of a chosen smooth
sector; parity is not evaluated on arbitrary real points.

The funding condition is equivalently

    b >= lambda(2R-I).

Define the stroboscopic law, with clock c in Z/5, as follows:

    if epsilon*delta=1:
        z'=Fz,
        b'=b+E_lambda(z)-E_lambda(z');
    otherwise:
        z'=z, b'=b;
    c'=c+1 modulo 5.

Both tags are retained; recomputing them from the new integral state gives
the same values. This new HOLD convention is an explicit part of this
construction. It neither changes nor claims to implement the exhausted-bank
direction reflection in the predecessor.

For every real z,

    I=Q(y-z_3) <= 2[Q(y)+Q(z_3)] <= 2R.

This follows by applying |a-b|^2<=2(|a|^2+|b|^2) in each embedding.
Hence E_lambda<= (1+2lambda)R. If the step is funded, H remains fixed
under the displayed bank update and R remains fixed under F, so

    b'=H-E_lambda(z')>=0.

Both the inequality defining delta and parity admission are invariant.
On a held state everything except the clock is fixed. Therefore all
branches preserve nonnegative bank values and exact total H.

The inverse is explicit. Decrement c; on an active sector set

    z=F^(-1)z'=F^4 z',
    b=b'+E_lambda(z')-E_lambda(z),

and on a held sector retain z,b. Guard invariance makes this the inverse
on the complete declared integer carrier, including underfunded states.
The same funding bound proves b>=0 in the inverse. If lambda,b and the
slots are integral, all stroboscopic outputs are integral. The complete
stroboscopic law has fifth power identity.

At fixed integer H its stroboscopic energy shells are finite: E_lambda>=R
and b>=0 bound R and b; the positive definite Q bounds every integer slot
coordinate. The clock and sector tags have finite alphabets. This statement
does not say the full intervening real phase space is a finite set.

## 4. A single Hamiltonian for bank work, contact motion and clock

On each smooth sector (epsilon,delta), set

    h_eff=epsilon*delta*h,
    B=b+E_lambda(z)-h_eff(z),
    Omega_ext=omega+dt wedge dB,
    H=E_lambda(z)+b=B+h_eff(z).

The clock t is a circle R/(5 tau Z). Its one-form dt is globally defined.
The stroboscopic clock positions are t=c tau for c in Z/5.

The change of variables (z,b,t)->(z,B,t) is a global real diffeomorphism
on every sector, since its coefficient of b is one. In these coordinates
Omega_ext is the product symplectic form. Thus the stated mixed form is
closed and nondegenerate. It has the explicit global primitive

    Theta=sum_(sites,i) 2g_i q_(site,i)dr_(site,i)-B dt,
    dTheta=Omega_ext.

The Hamiltonian convention i_(X_H)Omega_ext=dH gives

    dot z=X_(h_eff),  dot t=1,  dot B=0.

It follows that

    b(a)=b(0)+E_lambda(z(0))-E_lambda(z(a)).

This proves the whole-path energy law H=E_lambda+b, not just an endpoint
balance. It also proves the stated time-tau map. For inactive sectors the
base and bank are fixed while the actual clock coordinate still advances.
For active sectors the real contact flow is produced and bank work is its
exact compensating energy change. The invariant safe guard gives

    b(a)=H-E_lambda(z(a))>=H-(1+2lambda)R>=0

for every real a, including negative time. Thus the nonnegative-bank
subset is flow-invariant on funded sectors; held sectors are trivially
invariant. The smooth sector flows and the discrete interface together
realize all branches of the declared HOLD law.

The functional

    S[path]=integral [Theta(dot path)+H(path)] da

has the above Hamilton equations under fixed-endpoint variations. The plus
sign is consistent with dTheta=Omega_ext and i_X Omega_ext=dH. This supplies
one explicit variational action for the declared real completion. It does
not select a quantum phase exp(iS/A), a Born rule or a physical A.

The parity/funding tags and their interface are supplied. The action does
not derive the parity predicate or a physical interpretation of the bank.

## 5. Why the naive product completion fails

Consider the active endpoint map

    T(z,b,t)=(Fz,b-Delta E(z),t+tau),
    Delta E=E_lambda(Fz)-E_lambda(z),

but retain the unmodified product form

    Omega_product=omega+dt wedge db.

Since F preserves omega,

    T^*Omega_product-Omega_product=-dt wedge d(Delta E).

Consequently this endpoint map is symplectic in that product form only
where d(Delta E)=0. On a connected F-invariant domain this makes Delta E constant.
If F^5=I, summing E(Fz)-E(z) around that five-cycle gives five times
this constant equal to zero; it must be zero. For lambda>0 the defect
is not identically zero. At zero data
Delta E=0; on (u,-u,u) the initial I is20 and the final I is10, so
Delta E=-10lambda. To see the final I exactly, note

    Tr[(u conjugate(u))rho]
      =Tr(2j^2-j-j^3)=0,
    Q((1+rho)u)=2Q(u)+Tr[(u conjugate(u))rho]=10.

Homogeneity also makes nonconstancy of Delta E immediate.
The safe funded domain has open real neighborhoods on which this defect
is nonzero when the bank is sufficiently large.

This is a specific obstruction to the unchanged product completion. It
excludes neither the displayed mixed form, another admitted full form,
another energy, enlarged control dynamics nor a different physical model.

## 6. Sharp midpoint funding witness

Take x=u, y=-u, z_3=-j u, with all other sites zero. Then R=15.
The identity

    (u conjugate(u))^2
      =6-4(j+j^(-1))+j^2+j^(-2)

has trace30. Therefore Q(u^2)=15, while Q(u)=Q(ju)=5.

At the beginning, midpoint and endpoint of the chosen admitted flow,

| Time | Pair (x,y) | y-z_3 | I=Q(y-z_3) |
|---|---|---|---:|
| 0 | (u,-u) | -u^2 | 15 |
| tau/2 | (-ju,ju) | 2ju | 20 |
| tau | (j^2u,-j^2u) | ju^2 | 15 |

Thus E_lambda is 15+15lambda, 15+20lambda, 15+15lambda at these snapshots.
An endpoint-only rule sees zero net cost and would permit b(0)=0.
In this real interpolation its midpoint bank would instead be -5lambda.
This disproves that endpoint affordability alone certifies funding of
this chosen whole path; it does not falsify the predecessor's discrete rule.

For this orbit Q(y(a))=Q(z_3)=5, so I(a)<=20 by Cauchy-Schwarz.
The midpoint attains20. Hence b(0)>=5lambda is necessary and sufficient
to fund this particular entire orbit with no rejection. This is the sharp
orbit-specific reserve, and is different from the conservative uniform
guard used in the complete HOLD law. In particular that uniform guard
requires15lambda on this preparation; a bank of5lambda funds the real
active path but is held by the deliberately stronger uniform policy.

## 7. One bank for any fixed finite preparation family

For an arbitrary finite family with R<=R_max, a single common initial bank

    b_*=2lambda R_max

meets the safe guard at every preparation, because I>=0. The sharper
state-specific sufficient bound is lambda(2R-I). These bounds fund the
entire real trajectory and all repeats of this same isolated-pair flow,
not only one endpoint; no error or debit accumulates from repetition.

For example the six-slot loader preparations
(tB,-tB,u,u,X,2), B=1-j^2, X=1+j-2j^3 and t=-2,...,2,
have R=10t^2+33<=73. For an independently specified C12 test of those
states, b_*=146lambda is a common sufficient bank. This does not compile
the 322-contact loader schedule into one shared full symplectic form.

## 8. Work remains nonselected

Fix tau and h as above and use the same declared bank reading b, with
initial data (u,-u,u) and common b=60. For lambda=1 and lambda=2 the
safe guard is satisfied, since it requires10lambda. In both cases the
data follow exactly the same phase trajectory, and dot t=1. At duration tau,
I changes20->10, so

    b'=60+10lambda,

which is70 and80 respectively. R remains15 in either completion.
The mixed symplectic form changes with lambda. Therefore this family
supplies action/work/clock completions for different relative work readings;
existence of such a completion does not independently select lambda.

The on-shell action is also the same on these two active trajectories.
Indeed dot t=1 gives

    Theta(dot path)+H
      =Theta_base(dot z)-(b+E_lambda-h_eff)+(b+E_lambda)
      =Theta_base(dot z)+h_eff.

Both the base trajectory and h_eff are the same, so lambda cancels from
this action while the literal bank-coordinate gain changes from10 to20.

This is not a theorem that the different completions are physically
inequivalent under every possible physical equality. The comparison fixes
the declared bank-coordinate reading. It also does not identify lambda
with electrical coupling. In particular the selected base flow keeps
z_3 fixed despite the appearance of Q(y-z_3) in E_lambda; mixed clock/bank
terms compensate that apparent interaction in the Hamilton equations.

## 9. What an independent action selector would decide

On a connected smooth domain, if one independently fixes both a
nondegenerate full form Omega and a full vector field X, any Hamiltonians
H1,H2 satisfying i_X Omega=dH1=dH2 obey

    d(H1-H2)=0.

They differ only by an additive constant on that connected component.
Different disconnected sectors may have different constants. This elementary
rigidity statement does not provide the missing physical Omega or X.

The construction above deliberately changes Omega with the chosen energy.
Thus it closes a precise conditional existence question and exhibits a
precise remaining selection debt. It supplies neither the physical charged
response nor a fixed ratio of that response to action and propagation.
No exact or measured value of alpha is an input to this construction.
