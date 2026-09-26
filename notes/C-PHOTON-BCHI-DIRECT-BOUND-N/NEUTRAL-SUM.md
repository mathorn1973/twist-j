# Neutral connection sums and a full-measure transverse lower bound

**PUBLIC, NON-CANONICAL; candidate-T analytical derivations.**
Working item C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Date: 24 September 2026. Apache-2.0.
Public basis: Canon v91, main
`b5b0792971b6841c8b7e61f95afaaabcec4ce082`, after PR #1159.

**P1 is not closed. No Canon promotion follows from these results.**
The original measure is retained on every even periodic four-torus L>=4:

    mu_L(n)=Z_L^-1 2^(-|supp n|) 1{partial n=0 mod5},
    n in {-1,0,1}^P, j=partial n/5, V=L^4.

There are three new evaluated results. First, summing the complete one-copy
field space of the explicit neutral bridge restores exponential suppression
of its current moment. Second, the cap transfer pays enough to sum a defined
family of generated comb connections over all lengths and admissible shapes:
for fixed endpoint edges and length threshold R>=3, its full-measure absolute
contribution is at most `(1/553728)(3375/4096)^R`. This includes the geometry of the aligned
obstruction; it does not cover all neutral backgrounds. Third, conditional
variance without an empty halo gives `b >=25/(36*2^41)` in every admitted
profile. The same proof gives `chi >=1/(36*2^41)`, so this certified lower
floor cannot establish the required strict difference.

The exact original joint thermodynamic-first, infrared-second profiles,
Fourier centers and Ward identity are unchanged. A finite geometry audit
is specified in [NEUTRAL-PREREG-20260924.md](NEUTRAL-PREREG-20260924.md).
The all-volume statements below rest on the written proofs, not on an
extrapolation from the finite audit.

## A. Complete one-copy sum on the aligned bridge

Use the odd-D geometry of [FULL-MEASURE.md](FULL-MEASURE.md), sections 7–9, D=2h+1>=5, L=2D+4.
Write C_0,...,C_(D+1), caps q_1,...,q_(D+1), S, and connected closed
background B exactly as there. The noncap background has

    M=|supp(B)\Q|=11D-13,
    beta_r=B(q_r)=(-1)^(r+1), 2<=r<=D.

Let R=S union Q union supp(B). Define E_R to be the event that the
restriction eta=n|R, extended by zero, is itself closed modulo five.
There is no empty halo condition. For every such deterministic eta,

    mu(n|R=eta)=2^(-|supp eta|) mu(n|R=0).                    (D)

Indeed subtracting eta bijects the exterior completions with those for
zero on R, preserves every exterior coefficient and weight, and preserves
closure modulo five. Write p0(R)=mu(n|R=0). If Z_R is the complete
standalone partition on R, then mu(E_R)=p0(R)Z_R. All exterior charged
sectors are summed in p0(R); the exterior is not forced to be empty or
integer-closed. A zero-halo version is also valid but weaker.

### A.1. The endpoint has five coefficients, not one

Removing its chosen cap leaves an endpoint cup defect with components of
sizes 1,4,5,5,5 under the neutral degree-two equality edges. They are the
central face, the open cup wall, and the other three cup walls. Write the
coefficients, relative to the original defect orientation, as
(z,a,b,c,d) in {-1,0,1}^5, where a is the open-cup coefficient.
The three charged-square edges not touching the removed cap impose

    z+a+b+c+d=0 (mod 5).

All five coefficients equal +1 or -1 are the only cases of nonzero
endpoint current. Every other admitted choice has integer sum zero.
The cap restored with coefficient a makes the boundary exactly
-(z+a+b+c+d) partial p_01. Thus this is also a sufficient condition.

This distinction is essential: gluing five incidences as if every
ternary field were monochromatic would omit neutral endpoint states.
The binary fixed-sum proof in #1159 did not have this issue.

Let eps=2^-20, t=1/16 and v=1/32. Summing the endpoint's noncap weights
at fixed a gives the even vector e=(e_1,e_0,e_1), in states (-1,0,1):

    e_0=1+3v+6v^2+3v^3=36035/32768,
    e_1=t[1/2+3v+(9/2)v^2+(7/2)v^3]=39207/1048576.

For example, the three closed cups have coefficient polynomial
(1+v(z+z^-1))^3, whose coefficients at 0,1,2 are respectively
1+6v^2, 3v+3v^3, and 3v^2. This yields the displayed expressions, with
the all-positive charged configuration supplying the additional v^3/2
inside e_1. The signed endpoint-current vector, with a common minus sign
removed from each of the two endpoints, is simply

    u=eps*(-1,0,1).

Thus integrating every neutral endpoint configuration changes the
partition, but leaves the charged source exactly as in the monochromatic
calculation.

### A.2. Complete remaining classification

Each of the D interior four-face noncap pieces has one coefficient
a_i in {-1,0,1}, as does B\Q, with coefficient y. This follows from
degree-two equality edges only. No degree-five edge is used to force
these equalities. The two open endpoint coefficients are a_0,a_(D+1).
The cap equations then force

    n(q_r)=a_(r-1)-a_r+beta_r*y,

with beta_1=beta_(D+1)=0. The right side must lie in {-1,0,1}.
At each interior cap the direction-two seam has at most four permitted
faces, hence the mod-five equation is an integer zero equation. Endcaps
also have neutral seam edges fixing the displayed difference. Their
other seam can be a charged-square edge of degree six; do not call
all endcap edges neutral. Its remaining equation is exactly the already
imposed five-coefficient endpoint congruence.

Conversely assemble the five endpoint pieces, the D tube pieces, and
yB with these cap values. The endpoint congruences and displayed cap
equations give closure modulo five everywhere. This proves completeness,
including all new neutral endpoint configurations.

Put g(0)=1, g(1)=g(-1)=1/2 and g(k)=0 otherwise. The exact local weight,
after the endpoint sums, is

    e(a_0)e(a_(D+1)) * t^(sum_(i=1)^D |a_i|)
    * 2^(-M|y|) * product_(r=1)^(D+1)
      g(a_(r-1)-a_r+beta_r*y).

For the signed endpoint numerator replace both e factors by u. This
is the original one-copy measure summed over all fields on R, not a
fixed sum of two copies and not an artificial resampling chain.

### A.3. Exact finite-dimensional neutral sum

In state order (-1,0,1), define W=diag(t,1,t),

    K0 = [[1,1/2,0], [1/2,1,1/2], [0,1/2,1]],
    K+ = [[1/2,1,1/2], [0,1/2,1], [0,0,1/2]],
    K- = transpose(K+),
    T0=sqrt(W) K0 sqrt(W), T+=sqrt(W) K+ sqrt(W), T-=transpose(T+).

The endpoint vectors are z=sqrt(W)K0 e and v_source=sqrt(W)K0 u
=eps/4*(-1,0,1). The y=0 partition and signed numerator are

    Z0=z^T T0^(D-1) z,
    N0=v_source^T T0^(D-1) v_source=2 eps^2 t^D.

The last equality uses the odd eigenvector of T0 with eigenvalue t.
It also has an exact cancellation proof: in any current-tagged term,
if an interior a_i is zero, independently reverse every coefficient on
one side of that zero. The cap weights are unchanged and one endpoint
current reverses. All these terms cancel. If every a_i is nonzero,
ternarity forbids adjacent opposite signs, so only the two globally
aligned fields remain. Consequently N0 equals their bare total weight,
although the partition includes all neutral fields.

For y=+1, the internal cap product alternates K-,K+ for D-1=2h steps.
Write

    A=32 T+=[[1,8,1],[0,16,8],[0,0,1]],
    G=A^T A=[[1,8,1],[8,320,136],[1,136,66]],
    P=G/1024=T- T+.

Then

    Z1=2^-M z^T P^h z,
    N1=2^-M (eps^2/16) w^T P^h w,  w=(-1,0,1).

Reversing the state order proves that y=-1 contributes the same Z1,N1.
Hence the complete exact sums are

    Z_R=Z0+2Z1,  N_R=2 eps^2 16^-D+2N1.

P is positive definite, so N1>=0. Global sign reversal makes both
endpoint current means zero in the local measure and in E_R. The
conditional current covariance is N_R/Z_R; it is not N_R alone.

### A.4. Evaluated all-D bounds and full-measure normalization

A simple preliminary bound, summing absolute endpoint weights through
K0 and dropping cap weights, is

    0<=N1<=eps^2 2^-M (9/8)^D.

There is a stronger uniform transfer estimate. Put r=(2,1,2) and q=5/8.
Direct rational inequalities give

    (K+ W r)_i/r_i=(9/16,5/8,1/32)_i,
    K- W r<=q r.

Since |u|<=eps*r/2 and |u|^T W r=4 eps t, any sequence of D-1
nonzero-sign cap shifts satisfies

    |N_y| <= 2 eps^2 t * 2^-M q^(D-1).

For the alternating geometry the two terms are nonnegative, so

    2 eps^2 16^-D <= N_R
      <= 2 eps^2 16^-D + (eps^2/4) 2^-(11D-13) (5/8)^(D-1)
      = 2 eps^2 16^-D + (2^14/5)eps^2 (5/16384)^D.             (A)

Both bases are explicit and below one. This sums all occupancy and
orientation states of the connected neutral background, including those
responsible for the nondecaying fixed-sum correlation in #1159.

Choose the same positive orientation-zero end edges e,f as #1159. Each
has at least five of its six incident faces in R. On E_R the exterior
restriction is separately closed modulo five; its at most one remaining
incidence at either end must therefore be zero. Thus the full current
equals the local current there. Applying (D) gives the genuine
original-ensemble, event-weighted identity

    E_mu[j_e j_f 1_(E_R)]=p0(R) N_R,

and therefore 0<=E_mu[j_e j_f 1_(E_R)]<=the right side of (A), since p0<=1.
Also E_mu[j_e|E_R]=E_mu[j_f|E_R]=0 and Cov_mu(j_e,j_f|E_R)=N_R/Z_R.
The same statements with B absent use just N0 and Z0.

### A.5. Exactly what was and was not summed

The sum includes the entire standalone one-copy measure on R,
every endpoint charge sector, all neutral
endpoint fluctuations, all cap occupancies, both orientations and absence
of B, and every separately mod-five-closed exterior charge sector. On this standalone one-copy event, the current moment decays after
the background occupancy is summed. This event is not the earlier
conditional two-copy event.

It does not cover configurations whose restriction to R fails to be
closed modulo five; arbitrary exterior faces may touch the patch but
must satisfy that separate closure.
Events for many overlapping corridors also cannot be combined by a
union bound on their signed moments: signs and overlaps require an
actual disjoint allocation or a pointwise cancellation mechanism.
In particular (A) is not a bound on full C_j(e,f).

There is also a bound suitable for an honest union sum. Let E_R^B be
the subevent E_R with the local background coefficient y nonzero. Replace
both current sources by their absolute values. Now K0|u|=eps*(1,1,1),
and 1<=r, while 1^T W r=5/4. Thus for either background orientation

    A_y=sum_local |j_e j_f| weight
       <=(5/4)eps^2 2^-M (5/8)^(D-1).

Consequently the original full measure satisfies

    E_mu[|j_e j_f| 1_(E_R^B)]
       <=2^15 eps^2 (5/16384)^D.                            (B)

This absolute bound can be summed over overlapping deterministic patch
events by an ordinary union bound. It does not use a union bound on a
signed moment. The y=0 contribution still requires its signed cancellation
and does not have the same absolute-distance estimate.

Part B proves the weighted geometric sum for a defined generated family.
It uses the absolute background estimate, never a union bound on the
signed y=0 cancellation.

## B. Summing actual neutral connection geometries

The exact deletion identity in Part A applies here to every stated closed
pattern, with the full exterior summed. In particular a nonzero integer-closed
ternary pattern on A faces has total probability at most `2^(1-A)` for its
two global orientations.

### B.1. Complete face-simple cube boundaries

A face-simple D-cube chain consists of distinct elementary 3-cubes
C_1,...,C_D such that consecutive cubes share one plaquette, these
D-1 interfaces are distinct, and nonconsecutive cubes share no
plaquette. Edge and vertex contacts are allowed. Choose orientations
successively so the shared faces cancel. The boundary is integer-closed,
ternary, with exactly

    A=6D-2(D-1)=4D+2

occupied faces. Fix C_1. For D>=2 the number of geometric descriptions is
at most 18*15^(D-2): six choices of first exit face times three other
incident 3-cubes; at subsequent cubes, the entry face is excluded, giving
five times three. Counting descriptions rather than distinct boundaries
only enlarges the union bound. The two global orientations therefore give

    mu(exists such complete boundary with D>=R, fixed C_1)
      <= min(1, (9/16)(15/16)^(R-2)),  R>=2.

For a fixed face p on the boundary of the first cube, the corresponding
count is at most 4*15^(D-1), and the tail is at most

    min(1, 2(15/16)^(R-1)), R>=1.

If p can occur at any of the D positions, an extra D gives the valid
tail min(1, 2(R+15)(15/16)^(R-1)). This is a bound for coherent complete
boundary patterns, not for all connected occupied neutral surfaces.


### B.2. Alternating comb geometry and its complete-boundary sum

Write h=D-1. A comb has an ordered spine of 2h-1 cubes

    U_2,W_2,U_3,...,W_(D-1),U_D

and one leaf L_r at each U_r, r=2,...,D. Its full cube face-intersection
graph must be exactly this tree; all shared interface faces are distinct.
Orientations cancel every tree interface. There are 3h-1=3D-4 cubes and
the complete boundary B has 12h-2=12D-14 occupied faces.

Fix the first upper cube U_2. For h>=2:

* Its leaf has at most 6*3=18 choices, then its spine exit at most 5*3=15.
* Each of h-1 unleafed spine cubes has at most 15 continuations.
* Each of h-2 internal upper cubes has at most 15 leaf choices and then
  12 outgoing choices, excluding both incoming and leaf interfaces.
* The final upper cube has at most 15 leaf choices.

Consequently

    K_h <= 18*15^2*15^(h-1)*180^(h-2)
         =60750*2700^(h-2)
         =60750*2700^(D-3).

All collisions or additional shared faces are discarded. This is an
upper count, so rejecting them introduces no missing entropy factor.
Combining with the exact closed-pattern price gives the complete-boundary
tail, for H>=2,

    mu(exists full signed comb boundary, fixed U_2, h>=H)
      <= min(1, [30375/357376]*(675/1024)^(H-2)).

This does not yet control the #1159 fiber. At each leaf, that fiber can
cancel one cap of B against a tube piece. Only 11h-2 boundary faces remain
unconditionally assigned to the common background color. A bound using
only those faces has ratio 2700/2^11=675/512>1. The missing cap cost must
be recovered from the actual local sum, rather than claimed for free.

### B.3. Explicit generated events on decorated corridors

The following restricted class includes the geometry of the aligned #1159
neutral obstruction and its translations and lattice symmetries. The definition
does not assert that arbitrary neutral connections belong to the class.

Start with the comb just described. On leaf L_r let q_r be its face
opposite the interface with U_r. This opposite-face requirement fixes
q_r without an additional choice. Require consecutive caps q_r,q_(r+1)
to be faces of an elementary tube 3-cube. Add one further tube cube at
each end and a 21-face four-cup endpoint defect at each end; the tube
attaches to a noncentral wall face of each defect. Designate the two
charged endpoint edges e and f. The whole face patch is R. Require the
two endpoint current loops to be disjoint. Require that every overlap
between these generator supports is exactly one of the designated caps:
q_r belongs to C_(r-1) and C_r, r=1,...,D+1, and additionally to B for
2<=r<=D. All designated caps are distinct, belong to exactly these stated
generators, and every other face belongs to exactly one generator.
There are no other generator face overlaps. Thus the noncap
supports of C_0,C_1,...,C_D,C_(D+1),B are pairwise disjoint, of sizes
20,4,...,4,20,11D-13. All proposed embeddings violating these finite
geometric conditions are discarded. Extra edge or vertex contacts do
not invalidate the argument.

Choose orientations successively so adjacent C pieces cancel on their
common cap. Reorient the cap coordinates, if needed, so the resulting
coefficient equation has the form

    eta(q_r)=a_(r-1)-a_r+beta_r*y,

where beta_1=beta_(D+1)=0 and beta_r is +1 or -1 at interior caps.

Define Omega_Gamma to be the full-measure event that

    n|R=eta=sum_(i=0)^(D+1) a_i C_i+yB,
    a_0,a_(D+1) in {-1,+1},
    a_1,...,a_D in {-1,0,1},  y in {-1,+1},

and every cap coefficient is ternary. Every such eta is closed modulo
five because each C_i is and B is integer-closed. Noncap disjointness
makes the representation injective and gives the exact product weight.
No converse classification of all closed restrictions on a bent patch
is needed. On the aligned patch, the complete classification in
Part A does identify Omega_Gamma with the occupied-background
states whose two endpoint currents are both nonzero.

Two distinct plaquettes determine at most one elementary 3-cube containing
both (L>=4). For opposite parallel faces their displacement determines
the third direction; for nonparallel faces their union of tangent
directions and positions determines the cube. Thus the intermediate tube
cubes, when they exist, are forced by consecutive q_r. There is no extra
per-D factor for choosing that tube.

The exact deletion equality and the same charged-source transfer sum as
in Part A give, with epsilon=2^-20,

    mu(Omega_Gamma)=E_mu[|j_e j_f| 1_(Omega_Gamma)]
      <= 2^15 epsilon^2 (5/16384)^D
       = 2^-25 (5/16384)^D.                         (G1)

For clarity, its arithmetic uses M=11D-13 noncap background faces and
the cap transfer K_beta W, W=diag(1/16,1,1/16). With r=(2,1,2),
K_beta W r <= (5/8)r for beta=+1 or -1. Summing absolute endpoint sources
gives K_0|u|=epsilon*(1,1,1) and 1^T W r=5/4. Both background signs give

    2 epsilon^2 2^-M (5/4)(5/8)^(D-1)
      =2^-25(5/16384)^D.

The equality of full and local endpoint currents follows because at
least five incident faces at each designated edge lie in R. Separate
closure of both restrictions forces the possible sixth exterior face
to vanish. The chosen endpoint current loops are disjoint, so the local
currents there are respectively the endpoint coefficients, up to fixed
signs, and their absolute product is one. Equation (G1) includes all
separately closed exterior charged sectors. It is a probability bound
and an absolute moment bound, so can be summed over overlapping events.

### B.4. Count at fixed endpoint edges and evaluated union tail

For a fixed edge, there are six possible central plaquettes of an
endpoint defect. Its attachment cap has twenty noncentral wall choices.
There are therefore at most 120 endpoint templates per specified edge,
and at most 120^2 template pairs for fixed e,f. Their signs are summed
inside (G1), so no extra sign factor is needed.

Given the left attachment cap q_1, choose its adjacent tube cube (at most
four choices), the other cap q_2 of that cube (at most five), its lower
leaf cube L_2 (at most four), and the upper cube U_2 across the opposite
face of L_2 (at most three). Thus there are at most 240 possible roots
U_2. Subsequent comb choices are bounded by K_(D-1); intermediate tube
cubes are already forced, and the right endpoint template supplies its
terminal cap. This count deliberately repeats choices at the first leaf;
repetition only enlarges an upper count.

Let U_D(e,f) be the union of Omega_Gamma over all admissible D-corridors
joining the fixed edges. Nonnegativity and (G1) give

    mu(U_D(e,f))=E_mu[|j_e j_f| 1_(U_D(e,f))]
      <=120^2*240*60750*2700^(D-3)*2^-25*(5/16384)^D
       =[1/(3*2^20)]*(3375/4096)^D.                  (G2)

Here 120^2*240*60750/2700^3=32/3 exactly. Thus for every integer R>=3,
with absent or inadmissible D simply omitted,

    mu(union_(D>=R) U_D(e,f))
      <=[1/(3*2^8*721)]*(3375/4096)^R.              (G3)

The geometric count and generated-event estimate apply to every D>=3
for which an admissible embedding exists. The original aligned witness
with nondecaying conditional two-copy correlation uses odd D>=5.

Using the periodic minimum l1 distance between edge centers, each endpoint
edge is at distance at most 3/2 from its chosen noncentral wall cap.
The two caps of any tube cube are at l1 distance at most one. Therefore
any admissible D-corridor has dist_1(e,f)<=D+3. One may use
R=max(3,ceil(dist_1(e,f)-3)) in (G3).

### B.5. What this does not prove

Equation (G3) is a genuine full-measure geometric sum for the indicated
generated events, with all interior tube occupancies, both neutral
background orientations, both charged endpoint orientations, and every
allowed exterior charged sector retained. It resolves the failure of the
punctured-comb price for this explicit class by retaining the cap transfer.

It does not bound configurations whose restriction to every such patch
lies outside the displayed generated family, neutral backgrounds with
different branching or compact geometry, multiple overlapping background
coefficients, or the signed y=0 contribution after a geometric union.
The signed y=0 single-patch cancellation cannot be union-bounded as an
absolute moment.

In particular, there is no proved pointwise covering or non-overcounted
switching allocation of the whole current covariance to the controlled
events. Neither a full distance bound for C_j nor a uniform transverse
lower response follows. The desired positive numerical P1 margin is
still absent; no Canon status change is justified.

## C. Transverse lower bound without an empty halo

### C.1. The finite-volume model and observable

For an even periodic four-dimensional torus of side L>=4, V=L^4, let

    mu_L(n)=Z_L^-1 2^(-|supp n|) 1{partial n=0 mod5},
    n_p in {-1,0,1},  j=partial n/5.

Write F_I(n;q)=sum_x n_I(x) exp(-i q dot midpoint(p_I(x))). Global reversal gives E_mu F_I=0, so S_n,II(q)=V^-1 Var_mu F_I, using the Hermitian variance E|F-EF|^2. The established axial Ward identity is 25 chi_L(t)=S_n,01,01(t e_1) at every allowed nonzero t.

The already proved full-measure empty-face estimate is

    P_mu(n|B=0)>=2^(-|B|).

Its positive Z5 integral proof is in SIGNED-SLICES.md section 3: delete the B plaquette factors from the nonnegative integral of Q=1+cos, and use Q<=2. This is an unconditional probability; no positive lower bound for emptiness under every fixed exterior is asserted.

### C.2. A conditional-variance insertion lemma

Let S be a finite set of faces and let a be a ternary field supported exactly on S, with partial a=0 modulo 5. Write m=|S|. Fix every face outside S. In the resulting conditional law, if the zero filling on S is permitted, then +a and -a are also permitted, because each preserves every modulo-five edge constraint. Their conditional probabilities satisfy

    p_+=p_-=2^-m p_0,

where p_0 is the conditional probability of the zero filling. If p_0=0 the following lower bound is trivial.

Let A=sum_(p in S) a_p g_p for arbitrary complex deterministic g_p. The local linear observable X=sum_(p in S) n_p g_p takes values 0,+A,-A on these three fillings. For every complex z,

    p_0 |z|^2 + p_+ |A-z|^2 + p_- |-A-z|^2
      =(1+2^(1-m))p_0 |z|^2 + 2^(1-m)p_0 |A|^2
      >=2^(1-m)p_0 |A|^2.

Put z equal to the conditional mean of X and retain only these three nonnegative summands in its variance. Thus

    Var(X | outside S)>=2^(1-m) p_0 |A|^2.

This uses neither isolation of the inserted component nor a fixed-current-sector comparison. The exterior may carry arbitrary admissible currents.

### C.3. Several patches and the averaging step

Let S_1,...,S_k be face sets such that no edge belongs to the boundary of faces from two different S_i. Fix every face outside their union U. The product face weights factor across the S_i. Each modulo-five edge constraint involves at most one set of remaining variables. Therefore the entire conditional law on U factors over the k patches, even though their unconditional fields need not be independent.

For a full linear observable F, this gives

    Var(F | outside U)=sum_i Var(F|S_i | outside U).

Apply the preceding three-filling argument in each factor and average. The tower property identifies the average local zero probability with the original unconditional empty event on that patch:

    E p_(i,0)=P_mu(n|S_i=0)>=2^(-m_i).

Total variance now gives the full-measure bound

    Var_mu F >=sum_i 2^(1-2m_i) |F(a_i)|^2.             (CV)

There is no empty halo or shielding event. It is enough that each local insertion is modulo-five closed and the chosen patches share no incident edge. Their contributions add through conditional independence, not by assuming that they remain separate occupied or paired components.

### C.4. The actual 21-face insertion and its packing

Use the proved 21-face charged cup a_I from SIGNED-SLICES.md sections 2 and 4, rotated to central orientation I. Its coefficients are all +/-1 on its support, and its boundary is -5 times the boundary of its central plaquette. Thus it meets the insertion lemma with m=21.

For central orientation 02, its vertices lie in the box

    x_0 in [z_0,z_0+1],  x_2 in [z_2,z_2+1],
    x_1 in [z_1-1,z_1+1], x_3 in [z_3-1,z_3+1].

Choose centers z_0,z_2 from {0,2,...,L-2}, and z_1,z_3 from

    {1+3r: 0<=r<floor(L/3)}.

The corresponding vertex boxes are disjoint and remain inside coordinates 0,...,L-1. In particular their face supports share no incident edge, including across the periodic boundary. Their number is

    k_L=(L/2)^2 floor(L/3)^2.

Every translated insertion has the same absolute form factor. The established explicit cup formulas are

    |F_02(a_02;t e_1)|=|3+2 cos t|,
    |F_01(a_01;t e_1)|=5.

For the second formula use the coordinate-permuted packing, with step 2 in directions 0 and 1 and step 3 in directions 2 and 3. Its count is the same k_L. These are two separate variance estimates, not simultaneous packings that would need additional separation.

Combining with (CV), define

    c_L=2^-41 k_L/V
       =2^-41 floor(L/3)^2/(4 L^2).

Then, in the full original measure, at every allowed finite-volume axis momentum,

    S_n,02,02(t e_1)>=c_L (3+2 cos t)^2,
    S_n,01,01(t e_1)>=25 c_L,
    chi_L(t)>=c_L                       (t nonzero).    (FLOOR)

The transverse estimate is a Fourier variance statement, not a local variance substituted for a long-wave coefficient.

### C.5. Explicit limit errors and all admitted profiles

Put

    rho_new=1/(36*2^41).

Since floor(L/3)>=L/3-1 and L>=4,

    rho_new-2^-41/(6L) <= c_L <= rho_new.

Also (3+2cos t)^2>=25-10t^2. Hence a convenient explicit lower bound is

    S_n,02,02(t e_1)
       >=25 rho_new -25*2^-41/(6L) -10 rho_new t^2.

This is uniform in every even volume and allowed axis momentum. It passes first to each already-admitted thermodynamic profile and then to its infrared lower limit, without replacing that ordered process by q_min. Consequently

    b^omega >=25 rho_new,
    chi^omega >=rho_new,
    b_* >=25/(36*2^41)>0.                              (LIMIT)

No existence or uniqueness of those profiles is proved or needed beyond the original admitted nonempty family.

### C.6. Removing the proved dense-current class

FULL-MEASURE.md section 14 gives, for N=|supp j| and r_dense=13824/14641<1,

    P_mu(N>=V)<=8 r_dense^(V/8),
    V^-1 E_mu[|F_I|^2 1{N>=V}]<=8V r_dense^(V/8).

Therefore the unnormalized retained transverse contribution satisfies

    V^-1 E_mu[|F_02|^2 1{N<V}]
      >= c_L(3+2cos t)^2 -8V r_dense^(V/8).

The conditional normalized second moment under mu(.|N<V) is at least this retained contribution, since its normalizing probability is at most one. Thus the same positive limiting floor holds after the prescribed dense-current removal. The error is explicit and uniform in q.

The event N<V is reversal invariant, so the conditional mean still vanishes. This again compares the averaged measure with a high-density event removed; it does not assert a positive lower bound in each surviving complete current sector.

### C.7. Why this is still not a positive P1 gap

The previous isolated-insertion floor was b>=25*2^-173. The improvement here replaces the empty 153-face shield by conditional variance on the 21-face support, plus a packing of density 1/36.

Nevertheless, exactly the same proof yields chi>=rho_new. Every valid chi_upper over the admitted nonempty profile family must therefore satisfy chi_upper>=rho_new. Consequently this particular certified floor obeys

    25 rho_new -25 chi_upper <=0.

It cannot close b_lower>25 chi_upper. The stronger numerical floor is an actual full-measure result, but it remains the common charged local contribution. A neutral insertion confined to bounded size has a transverse axis form factor vanishing at t=0; the already proved bounded-component cancellation explains why replacing the charged insertion by finitely many bounded neutral moves cannot repair this limitation.

No successful reverse-covariance estimate for the macroscopic neutral contribution was obtained in this derivation. No additional unidentified constant or named assumption is introduced as a substitute for that missing result.

## D. Closure assessment

These estimates resolve the explicit common-background obstruction after
its real occupancy cost and the stated shape count are included. They do
not supply a covering or switching allocation of every contribution to
the signed current covariance. General branching, compact backgrounds and
multiple interacting neutral fields remain outside the summed family.

The improved transverse floor is uniform but is still the shared local
charged contribution. A separately evaluated positive macroscopic neutral
contribution, or another direct positive bound on the complete ordered
contrast, has not been obtained. Therefore no evaluated pair of constants
satisfies `b_lower >25 chi_upper` over all original admitted profiles.

Separate agents reviewed the written arguments with shared sources. That
review is not blind external evidence. The finite audit does not enumerate
the full ensemble and ordinary repository CI does not execute notes audits.
P1, P2, S7 and PHOTON-MASSLESS-PHASE remain open; Public Canon v91 remains
unchanged. A complete P1 theorem and its earned review are still required
before any corresponding canonical fold.
