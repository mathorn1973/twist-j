# Response coefficients and common-mode interface boundaries

NON-CANONICAL / L1 / conditional analytical candidate.
Public reservation: [#1918](https://github.com/mathorn1973/twist-j/issues/1918). This note supplies hand proofs within explicitly
specified linear interfaces. Same-session checks are authoring QA, not
independent scientific acceptance. No scientific executable or empirical
identification is part of this note, and no Canon status changes here.

## 1. Notation and the question being tested

Let O=Z[j], Phi_5(j)=0 and rho=j^2. In the selected complex embedding,
use the ordinary Hermitian inner product on the five labelled slots. Set

    e = (1,1,1,1,1)^T/sqrt(5),  P = e e*,  Q = Id-P,
    B = e_5 e_5*,  beta = e* B e = 1/5,
    w = Q B e,  ||w||^2 = 4/25.

Here P is the common-mode projection, Q is its orthogonal complement,
and B is the literal fifth-slot load. These are specified interface data.
Use M for a contact-word matrix, rather than overloading B. The symbol x
is a dimensionless load parameter whose microscopic definition must be
fixed independently of the desired answer. The literal load amplitude is

    t(x) = 1/(1+x),  L(x) = (Id+x B)^(-1) = Id-d(x)B,
    d(x) = x/(1+x).

The candidate comparison is f(x)=(1+x/5)^(-5). In particular,

    f(x) = 1-x+(3/5)x^2-(7/25)x^3+O(x^4).

The number 3/5 is a Taylor coefficient, not an output amplitude, an
individual contact-matrix entry, or a probability unless another contract
independently gives it that meaning. Formal series below are about x=0;
real positive-load statements may be restricted to x>=0.

As a declared comparison matrix, define D(a)=((1+a,1-a),(1-a,1+a))/2 and
T=diag(D(rho^4),D(rho^3),1). Its fixed space is spanned by
(1,1,0,0,0), (0,0,1,1,0), and (0,0,0,0,1). Thus Te=e and T^5=Id,
but T alone does not select the one-dimensional span of e. Also TB=BT.
This definition does not certify any particular integral contact word.

## 2. Four different scalar mechanisms

All readouts in this table start in e. The second row is a load-only
product over orthogonal directions, not an unspecified interleaving with T.

| Mechanism | Five-step scalar | Coefficient of x^2 |
|---|---|---:|
| Fixed fifth-slot load, passive final readout | (4+t^5)/5 | 3 |
| Five orthogonal load directions, each used once | t | 1 |
| Projection to span(e) after each load | ((4+t)/5)^5 | 7/5 |
| Common-mode constraint imposed before inversion | (1+x/5)^(-5) | 3/5 |

For the first row, (TL)^5=L^5 since T and L commute, so the readout is
(4+t^5)/5 exactly. For the second, let P_1,...,P_5 be mutually orthogonal
rank-one projections with sum Id. Then

    product_k (Id-d P_k) = Id-d sum_k P_k = t Id.

For the third, PLP=(e*Le)P and e*Le=(4+t)/5. Each additional projection
removes the other four components, giving the displayed fifth power.
Such a projection is an actual extra operation; a passive final reading
does not perform it. A reversible implementation would have to account
for any discarded information in the complete carrier.

The one-step projected amplitude is

    a_post(x) = (4+t)/5 = (1+4x/5)/(1+x),

whereas the constrained inverse gives a_pre(x)=1/(1+x/5). In particular,

    a_post-a_pre = 4x^2/[5(1+x)(5+x)],
    a_post^5 = 1-x+(7/5)x^2-(47/25)x^3+O(x^4).

Compression and inversion do not commute. These four formulas agree to
first order but describe different apparatus operations. Rotating a role
or adding mixing is not a specification of which formula applies.

## 3. An exact quadratic bound for fixed unitary mixing

Here is a broader class in which an exact obstruction can be proved.
Let v be a prescribed unit vector, V_0,...,V_m fixed unitaries independent
of x, and B_k fixed orthogonal projections. Rank one is allowed but not
needed for the proof. Use the chronological physical product

    W(x)=V_m(Id-d B_m)V_(m-1)...V_1(Id-d B_1)V_0.

Let U=V_m...V_0 be its unloaded unitary. Fix the output vector to Uv,
so the readout is matched to the unloaded evolution before inspecting x.
Set R_k=V_(k-1)...V_0 and Pi_k=R_k* B_k R_k. Then exactly

    a(x)=v* U* W(x)v
        =v* (Id-d Pi_m)...(Id-d Pi_1)v.

All Pi_k are fixed orthogonal projections. This reduction permits any
fixed unitary mixing and any fixed finite dimension. It does not permit
x-dependent mixers, fitted readouts, uncounted resets or a changed load law.
Define

    alpha_k=||Pi_k v||^2,  A=sum_k alpha_k,  s=sum_k Pi_k v,
    C=sum_(j>i) v* Pi_j Pi_i v.

Expanding the finite product and d=x-x^2+O(x^3) gives

    a(x)=1-Ax+(A+C)x^2+O(x^3).

This is an exact statement about its first two Taylor coefficients.
Because each Pi_k is self-adjoint and idempotent,

    2 Re C = ||s||^2-A,  v*s=A,
    Re [x^2]a = (A+||s||^2)/2
              = (A+A^2+||(Id-vv*)s||^2)/2.

Consequently

    A(A+1)/2 <= Re [x^2]a <= (m+1)A/2.

The lower bound uses the displayed orthogonal decomposition of s. The
upper bound uses ||sum Pi_k v||^2<=m sum ||Pi_k v||^2=mA.
If the independently fixed x and apparatus give A=1, then

    1 <= Re [x^2]a <= (m+1)/2.

Thus 3/5 is impossible in this precise family for every finite m when
A=1. The repeated fifth-slot load at m=5 attains the upper value 3;
five orthogonal load directions attain the lower value 1. Equality in
the lower bound means s=Av, not necessarily pairwise orthogonal loads.

For a fixed multiset of Pi_k, changing its order can change the imaginary
quadratic term, but not the real term above:

    Im C = (1/(2i)) sum_(j>i) v*(Pi_j Pi_i-Pi_i Pi_j)v.

Changing the physical interleaving may also change the Pi_k themselves,
so this is not general order independence. Since the first coefficient
-A is real, for real x the coefficient of x^2 in |a(x)| is also Re[x^2]a.
A coherent real target additionally requires its imaginary coefficients
to vanish. An intensity readout has different coefficients again.

The condition A=1 is essential. Rescaling an independently defined
parameter changes Taylor coefficients and must be carried through the
bound. This theorem excludes neither constraints, a different primitive
load, nonunitary interfaces nor other separately specified preparations.

## 4. Constraint reactions and finite stiffness

Write A_x=Id+xB. Requiring both source and output to lie in span(e) does
not solve the full unconstrained equation A_x y=v for nonzero x and
nonzero common input. Instead impose a declared holonomic constraint with
reaction r: A_x y+r=v, y in span(e), r orthogonal to e. Compression yields

    e*A_x e=1+x/5,  a_pre(x)=1/(1+x/5).

In unnormalized physical slot values, put y=a(1,1,1,1,1) and
v=b(1,1,1,1,1). Then b=a(1+x/5) and the reaction is

    r=(ax/5)(1,1,1,1,-4).

Each of the pairs (1,2) and (3,4) receives reaction 2ax/5 in this sign
convention. Moving the reaction to the other side reverses all signs.
The reaction is additional dynamics or a constraint law, not a passive
readout convention. One way to specify it independently is to fix K with
ker K=span(e) and use A_x y+K*mu=v, Ky=0 before deriving any response.

The Schur complement shows what a finite positive stiffness does instead.
Consider A_kappa=Id+xB+kappa Q, with kappa>=0 and a=1+kappa. Let
xi=Qe_5, so ||xi||^2=4/5 and w=xi/sqrt(5). Its Q-block is
D_kappa=a Id_Q+x xi xi*. Since w is parallel to xi,

    s_kappa=1+x/5-x^2 w*D_kappa^(-1)w
           =1+x/5-(4x^2/25)/(a+4x/5),
    g_kappa=e*A_kappa^(-1)e
           =(a+4x/5)/(a+(a+4)x/5).

If every step is compressed back to the common mode, this gives

    g_kappa^5=1-x+[3/5+4/(5(1+kappa))]x^2+O(x^3).

Every finite kappa>=0 gives a coefficient strictly greater than 3/5.
The limit kappa->infinity gives the constrained inverse. This is a
statement about this positive stiffness family, not a theorem that every
realization needs an infinite physical parameter. An exact holonomic
constraint directly defines a reduced carrier with a reaction law.

Passive iteration is different from compression at every step. With
r_0=1/(1+kappa), the coefficient of x^2 in e*A_kappa^(-5)e is

    3/5+(4/25)(5r_0+4r_0^2+3r_0^3+2r_0^4+r_0^5).

To see this, expand A_kappa^(-1)=D_0-xD_0BD_0+
 x^2D_0BD_0BD_0+O(x^3), where D_0=P+r_0 Q. A single quadratic insertion
contributes 5(beta^2+r_0||w||^2). Two linear insertions separated by l
unloaded factors contribute (4-l)(beta^2+r_0^(l+2)||w||^2), l=0,...,3.
Their sum is the displayed expression. It equals 3 at kappa=0, whereas
the compressed expression equals 7/5. Both limits are 3/5.

More generally, retain the common-mode block 1+x/5 and adjoint
couplings xw and xw*, with a positive-definite finite Q-block D(0).
Then the compressed five-step coefficient is 3/5+5w*D(0)^(-1)w.
The correction is strictly positive when w is nonzero.
This probes only the direction w, not every perpendicular degree of freedom.
Three directions orthogonal to w may have finite invisible admittance.

Positivity matters. For example take a perpendicular orthonormal pair
v_1,v_2 with w=(2/5)v_1 and an inverse stiffness Y whose block is
((0,1),(1,0)). For D(x)=Y^(-1)+(4x/5)v_1v_1*, its inverse block is
((0,1),(1,-4x/5)). Then w*D(x)^(-1)w=0 although D(x)^(-1)w is nonzero.
The scalar Schur correction vanishes with finite auxiliary motion. This
example is indefinite and lies outside the positive theorem. Nonreciprocal
channels or independently supplied direct terms likewise need their own
contracts; one cannot silently exclude them in a universal conclusion.

## 5. A coefficient is not a raw matrix entry

A finite fixed contact branch has entries in O[1/2]. Its rational entries
lie in Z[1/2]: if a rational number becomes an algebraic integer after
multiplication by a power of two, that rational number is a dyadic integer
fraction. Thus a literal rational entry 3/5 is unavailable in that ring.

This does not establish an obstruction to the coefficient [x^2]f after
an independently selected parameterization and readout. For example

    1-5s+15s^2,  x=5s

becomes 1-x+(3/5)x^2. This is a legitimate change only if x=5s is justified
independently; choosing it to fit the desired coefficient proves nothing.
Also B has entries 0 and 1 but e*Be=1/5, because the normalized interface
itself contains division by five. Such a readout is not automatically a
primitive contact operation, but an entry-ring argument cannot ignore it.

The bare formal inverse (Id+xM)^(-1)=sum_n(-xM)^n retains coefficients
in the same ring if M, the readout and parameter conventions do. A more
general boundary inverse can add denominators through its constant inverse;
so can normalization or compression. The actual interface, not the word
"resolvent", decides which coefficient ring is relevant. If x is defined
only on a discrete input set, an analytic or formal continuation must also
be specified before a Taylor coefficient is an intrinsic question.

## 6. What licenses a fifth power

A scalar one-step reading does not establish a scalar compositional channel.
For instance M=((a,b),(c,d)) has first-coordinate reading a on input(1,0),
but the reading after two steps is a^2+bc. The omitted coordinate matters.
The fixed-load and repeated-projection rows above give the same distinction
inside the present five-slot example.

Freeze a complete carrier, logical injection iota, readout R_out, update
M_x, ready state and continuation rule before comparing coefficients.
Require R_out composed with iota to be the identity on logical inputs.
Full-state closure M_x iota(s)=iota(a(x)s) licenses a(x)^5 by induction.
If auxiliary state changes, instead prove the stated finite-horizon
transfer R_out M_x^n iota(s)=a(x)^n s on the actual occupied continuation,
while accounting for that auxiliary state. A supplied reset or fresh bank
is an additional resource, not an inference from one successful readout.

These boundaries identify precise mathematical decisions for a future
interface. They neither select a physical load parameter nor establish
an empirical coupling. Missing programs, counted clock results or long
series reports are not evidence for any claim made in this note.
