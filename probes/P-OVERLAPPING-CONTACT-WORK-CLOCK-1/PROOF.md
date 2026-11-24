# Smooth Hamiltonian composition of two overlapping contacts

**NON-CANONICAL / L1 / conditional analytical candidate.**

Public reservation: #1914. This is an explicitly added real architecture.
One fixed extended symplectic form and one autonomous Hamiltonian implement
C12 followed by C23 on the funded integral/ready family defined below.
A canonical controller computes the actual current pair parity and returns
to its ready state after each contact. No initially supplied parity history
or discrete retagging rule is used.

The controller, coefficientwise cosine selectors, phase representatives,
pulse profile, real clock, energy reading and mixed full form are declared
choices. They are not derived from native U or from a physical action law.
The continuous path is generally not integral. The construction supplies
no physical charge, action quantum, electromagnetic coupling or alpha.

## 1. Integral contact and base form

Let K=Q(j), O=Z[j], Phi_5(j)=j^4+j^3+j^2+j+1=0, rho=j^2 and u=1-j.
Use the power basis (1,j,j^2,j^3). The selected embeddings are

    sigma_1(j)=exp(2 pi i/5), sigma_2(j)=exp(4 pi i/5).

Identify K tensor_Q R with C^2. The positive half-trace account extends to
this real carrier as

    Q(a)=Tr_(K/Q)(a conjugate(a))/2
        =|sigma_1(a)|^2+|sigma_2(a)|^2.

For an integral power vector a=(a0,a1,a2,a3),

    2Q(a)=5 sum a_c^2-(sum a_c)^2.

On a pair of integral slots, the total contact C is identity unless
x-y belongs to 2O. On the admitted branch it is

    F(x,y)=(s+rho d,s-rho d), s=(x+y)/2, d=(x-y)/2.

Here s,d are integral. The new difference is rho(x-y), so parity admission
is preserved. The pair sum and both embedding norm sums are preserved.
Consequently C preserves Q(x)+Q(y), and C^5=identity on both branches.
Its inverse is C^4. These are properties of the supplied contact law.

Use the primitive per-site alternating form

    Omega_0(a,c)=Tr_(K/Q)(gamma a conjugate(c)),
    gamma=(j-j^(-1))/5.

Its power-basis matrix is

    [[ 0, 1, 0, 0],
     [-1, 0, 1, 0],
     [ 0,-1, 0, 1],
     [ 0, 0,-1, 0]].

The entries follow from Tr(j^k)=4 when 5 divides k and -1 otherwise.
The Pfaffian and determinant are one. Writing a_i=Q_i+i P_i, define

    g_1=2 sin(2 pi/5)/5, g_2=2 sin(pi/5)/5.

Both are positive, and

    Omega_0=2g_1 dQ_1 wedge dP_1+2g_2 dQ_2 wedge dP_2.

The three data slots z=(x,y,z3) carry omega=sum_sites Omega_0. We use

    i_(X_f) omega=df.

This form, its embedding description and the phase construction below are
mathematical inputs exposed in #1910 at
`afbafb9c84f93d4a7ea544ef08ec6c05c8467db0`; they are not physical selectors.

## 2. Unit-time pair Hamiltonians

For e=(i,j), set d_e=(z_i-z_j)/2 and select the positive representatives

    theta_1=6 pi/5, theta_2=2 pi/5.

Define the unit-time Hamiltonian

    h_e(z)=sum_(a=1,2) 2 g_a theta_a |sigma_a(d_e)|^2.

These phase representatives are choices, not a uniqueness consequence of
C^5=identity. On the pair sum/difference coordinates the form is
2 Omega_0(s_e)+2 Omega_0(d_e). Therefore

    dot d_(e,a)=-i theta_a d_(e,a), dot s_e=0.

Every spectator is fixed. At Hamiltonian time one the multiplier is
sigma_a(rho), so the endpoint is F_e. At time one half it is sigma_a(-j).
The full and half snapshots of an admitted integral pair are integral;
(-j)^2=rho, but -j has order ten and is not a power of rho. The continuous
interpolation is not a finer integer contact compilation.

The h_e flow preserves R=sum_sites Q and is complete. The three-slot
interaction account used in this new construction is

    I(z)=Q(x-y)+Q(y-z3).

It is fixed for the entire two-contact program, rather than relabelled
between its contacts. The exact quadratic identity

    3R-I=Q(x+y+z3)+Q(x-z3) >= 0                         (1)

follows by expanding the associated real symmetric bilinear form. Thus
0<=I<=3R on the entire real data carrier. The upper constant is attained,
for example, on (a,-2a,a) with a nonzero.

## 3. A smooth reversible parity controller

Add one canonical pair (q,p) in R^2 with form dq wedge dp. Its ready state
is (0,0). The two states (0,0) and (1,0) encode a control Boolean at contact
windows; the full controller is a continuous canonical pair, not a free
abstract bit. Define

    C_ctrl(q,p)=4*((q-1/2)^2+p^2),
    K(q,p)=(pi/2)*((q-1/2)^2+p^2).

The ready account is C_ctrl=1. With i_X(dq wedge dp)=dK, the equations are

    dot q=pi p, dot p=-pi(q-1/2).

A unit-area K pulse is a half-turn about (1/2,0):
(q,p) maps to (1-q,-p). It interchanges the two Boolean states. Its
half-area midpoint from (0,0) is (1/2,1/2), and from (1,0) it is
(1/2,-1/2). The entire motion preserves C_ctrl=1 on these preparations.

For a pair e, let v_c=z_i,c-z_j,c be its four real power-coordinate
differences. Define the globally smooth functions

    f_e(z)=product_(c=0,...,3) (1+cos(pi v_c))/2,
    g(q)=(1-cos(pi q))/2.

For every integral data state,

    f_e(z)=[z_i-z_j in 2O], df_e(z)=0.                 (2)

Indeed each cosine is +1 or -1 and each sine in the derivative is zero.
Also g(0)=0, g(1)=1 and g'(0)=g'(1)=0. These critical-point properties are
essential: a scalar Boolean value alone would not prevent unwanted forces
on data or controller.

Write omega_c=omega+dq wedge dp. A unit-area pulse of

    A_e(z,q,p)=f_e(z) K(q,p)

has data field K X_(f_e) and controller field f_e X_K. At integral data,
(2) makes the data remain exactly fixed throughout the pulse. The controller
therefore holds at (0,0) when refused and moves to (1,0) when admitted.
This computes the current pair parity inside the declared Hamiltonian law.

A subsequent unit-area pulse of

    D_e(z,q,p)=g(q) h_e(z)

has data field g(q) X_(h_e), dot q=0 and dot p=-g'(q)h_e.
At either Boolean state the controller is exactly fixed. The data undergo
F_e if the bit is one and otherwise hold. For a prepared integral pair,
this is precisely the total contact C_e; its endpoint is integral.

Finally apply another unit-area A_e pulse. The actual pair parity has the
same value after its own contact. Hence the second half-turn resets the
controller to (0,0) on the admitted branch, while the refused branch holds
there throughout. No previous parity value is erased from an uncontrolled
memory: the complete controller/data motion is invertible, and the bit is
uncomputed from the current data. The second pulse is the same positive
half-turn; on the two Boolean endpoints it is its own inverse.

This establishes the exact three-pulse block

    (z,0,0) -> (C_e z,0,0).                            (3)

During its prepared trajectory R is constant and C_ctrl=1. These two
invariances are not asserted for arbitrary off-ready real trajectories.

## 4. One periodic pulse program

Fix tau>0. Choose once the symmetric normalized smooth bump

    eta(s)=exp(-1/(s(1-s))) for 0<s<1, and 0 otherwise,
    chi(s)=eta(s)/(integral_0^1 eta(r) dr).

It is nonnegative, smooth and flat at both endpoints; its integral is one.
Let the actual clock t belong to R/(6 tau Z). For k=0,...,5 define chi_k
on its kth clock window by

    chi_k(t)=chi((t-k tau)/tau)/tau,

and set it to zero on the other windows, periodically. Its pulse area is
one. Nonzero supports do not overlap; all functions and their derivatives
vanish at seams. Symmetry makes a half-window also half pulse area.

The six generators, in chronological order, are

    A12, D12, A12, A23, D23, A23.

Their pulse sum defines one globally smooth periodic function

    h(z,q,p,t)=chi_0 A12+chi_1 D12+chi_2 A12
              +chi_3 A23+chi_4 D23+chi_5 A23.           (4)

The unit-time h_e and unit-area K conventions ensure that no additional
factor of tau is hidden in their endpoint maps. The pulse shapes, order
and clock scale are fixed independently of the input state.

By (3), the first triple finishes with integral data and a ready controller.
The second triple therefore computes the new parity of pair23, rather
than using its old value before C12. The complete base/controller map is

    (z,0,0) -> (C23(C12(z)),0,0).                       (5)

The clock returns after 6 tau. The data generally do not return. The next
block starts with exactly the readiness conditions needed to repeat (5).

## 5. A single fixed full form and autonomous Hamiltonian

For each chosen lambda>=0, define once

    E_lambda(z,q,p)=R(z)+lambda I(z)+C_ctrl(q,p),
    B=b+E_lambda-h(z,q,p,t),
    Omega_ext=omega_c+dt wedge dB,
    H=E_lambda+b=B+h.                                  (6)

The ambient real carrier has three four-real-dimensional data slots,
one canonical controller pair, one real bank coordinate b and one circle
clock: dimension sixteen. The differential in (6) is the full differential;
the dt part of dB disappears when wedged with dt.

Because the coefficient of b in B is one, the coordinate map
(z,q,p,b,t)->(z,q,p,B,t) is a global diffeomorphism. It is well defined on
the circle because h is periodic. In these coordinates Omega_ext is the
product symplectic form. Thus (6) is one fixed smooth closed nondegenerate
form on the entire carrier, not a switch between forms assigned separately
to the two contacts. Its coefficients depend on the internal clock
coordinate, not on an external evolution parameter.

With i_(X_H)Omega_ext=dH the product-coordinate equations are

    dot(z,q,p)=X_(h(.,t)) under omega_c,
    dot t=1,
    dot B=-partial_t h.                                (7)

The last term is necessary for the nonconstant pulse program. It cannot
be replaced by the dot B=0 equation of a time-independent isolated lift.
Differentiating b=B-E_lambda+h and using dh(X_h)=0 gives

    dot b=-dE_lambda(X_h),
    b(a)=b(0)+E_lambda(z(0),q(0),p(0))
                   -E_lambda(z(a),q(a),p(a)).           (8)

Hence H is conserved throughout the actual real trajectory. Equations
(4) and (7) implement the six pulses, including their parity computation,
under the same autonomous extended Hamiltonian law.

For embedding coordinates Q_(site,i),P_(site,i), a global primitive is

    Theta=sum_(sites,i) 2g_i Q_(site,i) dP_(site,i)
          +q dp-B dt,
    dTheta=Omega_ext.

The clock one-form dt is globally defined on the circle. The variational
functional

    S[path]=integral [Theta(dot path)+H(path)] da        (9)

has (7) as its equations under fixed-endpoint variations. The plus sign
matches the conventions dTheta=Omega_ext and i_X Omega_ext=dH.
This supplies a common action; it does not assign a quantum phase or a
physical action unit.

The ambient real flow is complete. During an A_e pulse, f_e and K are
separately constant, df_e is globally bounded in power coordinates, and
X_(f_e) is therefore bounded. The data have bounded velocity for each fixed
initial K, and the controller undergoes a bounded-frequency rotation.
During a D_e pulse, q and h_e are constant; the data follow a complete
linear rotation at fixed factor g(q), and p changes linearly in pulse area.
Every finite clock interval contains only finitely many such complete
pulses. Equation (8) then supplies a finite real bank value. Completeness
of the ambient flow permits negative banks outside the funded class below;
it is not a funding assertion for arbitrary real states.

## 6. Funded preparations, complete inverse and repeated blocks

Consider the prepared family at clock phase zero:

    z in O^3, (q,p)=(0,0),
    b >= lambda(3R-I).                                 (10)

For integral bank snapshots take lambda,b in Z_(>=0). The right side of
(10) is nonnegative by (1). This is a specified funded domain, not a HOLD
or reflection rule on underfunded initial states.

Throughout the prepared six-pulse trajectory, the argument in section3
preserves R and C_ctrl=1. Therefore (1) gives

    E_lambda(a)<= (1+3lambda)R+1.

Condition (10) is exactly H(0)>=(1+3lambda)R+1. Conservation of H in (8)
proves b(a)>=0 at every real time in the complete block. This bound uses
the entire real path, not only its integral endpoints or sampled midpoints.

At the block boundary write Pz=C23(C12(z)). Equation (8) becomes

    z'=Pz, (q',p')=(0,0), t'=0 modulo 6 tau,
    b'=b+lambda(I(z)-I(Pz)).                            (11)

R is unchanged, and the equivalent inequality H>=(1+3lambda)R+1 remains
true. Thus the output is again in (10), with integral b' when lambda,b
were integral. Induction proves the same assertion for arbitrarily many
repeated blocks, without reinitializing the controller or supplying a
fresh bank between them.

The inverse is the negative-time flow of the same fixed Hamiltonian.
At integral block boundaries it first applies C23^(-1)=C23^4 and then
C12^(-1)=C12^4, reversing the bank difference in (11). Reverse compute and
uncompute pulses run through the opposite controller semicircles; the
current contact parity still agrees at the two ends of its own contact.
The controller again returns to readiness. R and C_ctrl=1 are preserved
on these backward prepared paths, so the same bound funds them. This
proves nonnegative bank values for every positive or negative time from
(10), not merely for one forward block.

Only the controller and clock hand return after each block. No fifth-power
or other fixed global return period for C23 C12 is asserted. No arbitrary
off-ready or nonintegral data state is included in the funding guarantee.

For any finite initial family with R<=R_max, the common bank

    b_*=3lambda R_max

satisfies (10), since I>=0. In the frozen finite audit family each slot has
Q<=8, so R<=24 and b_*=72lambda suffices. The controller's common account
one is already included in E_lambda; it has not been omitted from H.

## 7. Why old parity and an old isolated form do not suffice

The need to recompute parity is visible on exact small inputs. Starting
from (2,0,0), C12 produces (1+rho,1-rho,0). Pair23 was admitted before the
first contact but is refused afterward, since B0=1-rho is not in 2O.
Using the stale admitted bit would apply F23 to (B0,0). Its first output
is (1+rho)B0/2=(1-rho^2)/2, with power coefficients (2,1,1,1)/2, which
are not integral.

Conversely, starting from (2,0,B0), pair23 is initially refused and becomes
the diagonal admitted pair (B0,B0) after C12. The stale refused bit is
again wrong. This second example witnesses a predicate error; because the
new pair is diagonal, holding it happens to give the same data endpoint.
It must not be described as a second endpoint counterexample.

There is also a restricted form obstruction. Fix the old isolated form

    Omega12=omega+dt wedge d(b+E_lambda-h12)

and try to use it unchanged for the compensated real endpoint

    T23(z,b,t)=(F23 z,b+E_lambda(z)-E_lambda(F23 z),t+tau).

Since F23 preserves omega, direct pullback gives

    T23^*Omega12-Omega12
      =-dt wedge d(h12(F23 z)-h12(z)).                 (12)

On z=(2,2,0), h12(z)=0, while F23 z=(2,1+rho,1-rho) has first-pair
half-difference (1-rho)/2, so h12(F23 z)>0. The difference is zero at
the zero state. It is a nonconstant quadratic form, and its differential
at this witness is nonzero by homogeneity. Thus the naive second endpoint
is not symplectic for that frozen first-contact form. The bank may be
chosen sufficiently large, so this is not an affordability issue.

Equation (12) only rejects that naive reuse. The single smooth form (6)
contains the complete fixed program from the start and is not subject to
that restricted objection. The canonical controller can be added as an
unchanged spectator to (12) without removing its defect.

## 8. Intermediate funding and a genuinely overlapping work witness

For the first pair contact on (u,-u,-ju), the first difference always has
Q(x-y)=20. The other difference has Q values 15,20,15 at the start,
half-area midpoint and endpoint of the selected contact flow. Consequently

    R=15, I=35,40,35.

For completeness Q(u)=Q(ju)=5 and Q(u^2)=15; the latter follows by tracing
(u conjugate(u))^2=6-4(j+j^(-1))+j^2+j^(-2), whose trace is30.
At the midpoint the pair is (-ju,ju), and its second difference is2ju.
The first-difference account20 is fixed, while Q(y-z3)<=20 throughout this orbit.
Thus the first contact's exact path reserve is5lambda despite its zero
net endpoint cost. Bank0 would become -5lambda at the midpoint when
lambda>0. The uniform guard (10) instead asks for10lambda here and funds
all future blocks as well. The sharp5lambda statement concerns this
first contact's chosen path, not a universal reserve for later blocks.

For a full block in which both overlapping contacts are active, take

    z0=(2u,-2u,2u).

It has R=60 and I(z0)=160. The first contact gives

    z1=(2rho u,-2rho u,2u), I(z1)=120.

Pair23 remains admitted: its difference is -2(1+rho)u. The second contact
gives

    z2=(2rho u,(1-2rho-rho^2)u,(1+rho^2)u).

In the j power basis these three slots are

    (0,0,2,-2), (3,0,-1,3), (-1,-2,-1,-1).

Their Q accounts are20,35,5. Their two adjacent differences have Q accounts
95 and40. Hence R(z2)=60 and I(z2)=135. These identities follow directly
from the coefficient formula for Q in section1.

The entire block's bank gain is therefore25lambda. Its safe initial
threshold is lambda(180-160)=20lambda. A common bank60 funds lambda=1
and lambda=2, giving final banks85 and110. Both contacts are active in
both cases, and their data, controller and clock trajectories coincide.
These are analytical pre-pin identities; the finite audit separately
tests their exact implementation.

## 9. Equal on-shell action does not select the work coefficient

The pulse function h and its data/controller trajectories do not depend
on lambda. For a common initial bank large enough for two chosen lambda
values, the complete prepared projected motion and clock agree, while
(8) gives different literal bank-coordinate gains whenever I changes.

On solutions dot t=1, so the integrand in (9) is

    Theta(dot path)+H
      =Theta_c(dot(z,q,p))-(b+E_lambda-h)+(b+E_lambda)
      =Theta_c(dot(z,q,p))+h.

The on-shell action in this selected primitive is therefore the same for
the two work witnesses above. This is not equality of the full action
functionals. For fixed phase-space paths and two parameters lambda,mu,

    L_lambda-L_mu=(lambda-mu) I(1-dot t),
    Omega_lambda-Omega_mu=(lambda-mu) dt wedge dI.

The full forms and bank dynamics differ. The construction supplies one
fixed full form for each selected lambda throughout all six pulses; it
does not supply one lambda-independent physical form selecting that value.
If both a full nondegenerate form and a full vector field are independently
fixed, their Hamiltonian is fixed up to a constant on each connected
component. No conflict with that elementary rigidity is claimed.

The bank reading is the declared coordinate b. No physical inequivalence
under every possible alternative reading is proved. Pulse order, primitive
form, controller, clock scale and real selectors remain supplied structure.
The construction resolves smooth composition within that enlarged L1
architecture; native-U implementation, physical work/action selection and
alpha remain separate obligations.

Original proof text: Apache-2.0 under the repository license.
