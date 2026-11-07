# A full-field polygon action, its mod-five obstruction, and a twenty-five-state lift

**NON-CANONICAL / L1. Proof-first conditional candidate-T. Independent acceptance pending.**

Candidate: C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N, additive full-field continuation.
The exact arguments below were derived by hand before execution of the new
full-field audit. Earlier reduced-audit evidence does not validate this extension.
No physical phase, coherent interference, action unit, alpha, Canon promotion,
or ordinary-contact compiler is inferred.

## 1. Sources, carrier and the question being tested

The scalar stencil is specified in the public
[fixed signed-port contract](https://github.com/mathorn1973/twist-j/blob/d4d363722f052141a4ce65e9da39f11a74b43b95/notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md).
The link field and its conserved energy are the exact premises in
[#1926](https://github.com/mathorn1973/twist-j/issues/1926#issuecomment-6696647447).
The matched loaded collision is the premise in
[#1927](https://github.com/mathorn1973/twist-j/issues/1927#issuecomment-6697335444).
The original ramified source carry is in
[#1924](https://github.com/mathorn1973/twist-j/issues/1924).
The five-contact phase reader is the declared construction in
[#1925](https://github.com/mathorn1973/twist-j/issues/1925).
The original #1926/#1927 implementation bundles were unavailable; the new
full-field implementation, if executed, is a reconstruction from these public
equations, not replay of their unavailable source.

Retain O=Z[j], rho=j^2, phi=-j^2-j^3, J=1+rho, and the forms Q, g and
Omega defined in PROOF.md. Work on the finite periodic quotient D3/3D3.
It identifies with (Z/3)^3 in physical coordinates: reduction modulo three
of D3 is onto, and its kernel is 3D3. Keep all thirty labelled direction
representatives, including any periodic aliases. Representatives have first
nonzero coordinate positive, squared lengths 2,4,8,10,16, and weights
6,1,15,1,1 divided by 324. Put M=diag(c_v), K=d1* M2 d1 and D=M^-1 K.
The adjoints use the ordinary counting measure. Thus MD=K=K* and
D=L-d0 d0* M. These are the inherited field identities, not new geometric
selection rules.

Fix z=1/27 and the source edge ell of direction (1,1,0), where c_ell=1/54.
Introduce the electric drift coordinate

    B=z M^-1 E.

B is a phase-space coordinate, not the next A value. With R=Z[1/6], use
A,B in (O tensor R)^(27*30), and integral source slots x,y,e. In these
coordinates the free map is

    B'=B-D A,       A'=A+B'.                              (F1)

All coefficients of D lie in R, by D=L-d0 d0* M. The matched injection is
B'=B+2 i delta_ell. Consequently this carrier is closed under free steps,
inverse free steps, and admitted or refused matched collisions.

This change of variables matters: raw M^-1 contains a denominator five on
one shell, but neither D nor the energy matrix below has such a denominator.
No modulo-five operation on an arbitrary rational number is being assumed.
Reduction R -> Z/m for m=5 or 25 is the homomorphism obtained by inverting
powers of two and three. Arbitrary rational fields outside this R-carrier
are not included in the new modular claim. The primary lattice condition
is on A and B, with E=M B/z derived from them. It does NOT admit every
raw E in O tensor R: on the weight-fifteen shell z/c=4/5, so a generic
such E would produce a forbidden denominator five in B. The specified
submodule is nevertheless closed under the matched-source/free dynamics.

The proposed action is a definite polygon expression constructed from the
already fixed energy metric and Omega. The test asks whether its ramified
carry can remain on the old mod-five phase fibre, then exhibits an explicit
larger lift. Choosing this action is a disclosed model premise, not physical
selection of a unique action.

## 2. One energy metric and its alternating form

For scalar-valued field arrays use g(A,KB)=sum_e g(A_e,(KB)_e), and use
Omega(A,KB) similarly. Let s=(x,y,e,A,B). Its conserved core energy is

    E_G(s)=Q(x)+Q(y)+Q(e)+Q(y-e)
       + [g(B,MB)+g(A,KA)-g(B,KA)]/(2z).                 (F2)

For t=(X,Y,e_t,A_t,B_t), define the alternating bilinear form

    Omega_G(s,t)=Omega(x,X)+Omega(y,Y)+Omega(e,e_t)
       +Omega(y-e,Y-e_t)
       +[Omega(B,M B_t)+Omega(A,K A_t)
          -(Omega(B,K A_t)+Omega(A,K B_t))/2]/(2z).      (F3)

Every coefficient is in R. The field metric is the symmetric block matrix

    G_field=(1/(2z))*[[K,-K/2],[-K/2,M]]                 (F4)

in (A,B) order. Direct block multiplication, using D* M=MD=K, proves
T_L* G_field T_L=G_field for T_L=[[I-D,I],[-D,I]]. The same multiplication
with Omega in place of g proves that L preserves Omega_G. Source slots
are fixed by L. Degenerate gauge/flat modes are retained; no inverse of G
is used and no nondegeneracy is claimed.

The collision also preserves this form on its admitted linear branch.
Let h u=(-u,u,0,0,2u delta_ell) and let

    ell(s)=2y-x-e+F_ell=4d,
    F=E-KA/(2z)=M B/z-KA/(2z).

Then ell(h u)=4u, and the polarized energy metric satisfies

    g_G(s,h u)=g(ell(s),u).

Hence P=h ell/4 is an orthogonal projection for the Hermitian energy
metric. The admitted collision is I+(rho-1)P. Since rho rhobar=1, it
preserves that Hermitian metric and (F3). Equivalently one may verify the
identity directly from (F3). The refused branch is identity. This is
branchwise preservation; no bilinear assertion between states undergoing
different branches is needed.

## 3. A fixed primitive-step action

For a primitive collision or free step T define

    Gamma_T(s)=Omega_G(s,T s)/4 in R.                    (F5)

The normalization matches the already marked source cycle. For an
admitted collision,

    Omega_G(s,Cs)=Omega(ell(s),i)=4 Omega(d,rho d)=4B(d),
    Gamma_C(s)=B(d).                                    (F6)

A refused collision has Gamma_C=0. The inverse step has the negative
increment at its corresponding endpoint, by alternation:
Gamma_(T^-1)(Ts)=-Gamma_T(s).

The primitive calendar is fixed: collision first, free step second. The
macrostep increment is Gamma_C(s)+Gamma_L(Cs). It is NOT silently
replaced by Omega_G(s,LCs)/4. Polygon expressions depend on the specified
cuts; grouping operations into a different primitive is a different
contract. The inverse traverses these same cuts in reverse order.

Expanding (F3) under (F1) gives

    Gamma_L(A,B)=Omega(A,K(4I-D)B)/(16z).                 (F7)

This is generally nonzero. Its derivation uses the symmetry of K and KD,
which kills the A-A and B-B alternating terms. It supplies a concrete
free-field contribution instead of stipulating zero phase at every free
step. This choice remains an action model, not an empirical conclusion.

## 4. An exact transverse D3 witness

For r in (Z/3)^3 set

    f(r)=2 if r1+r2+r3=0 modulo3, and f(r)=-1 otherwise.

There are nine values equal to two and eighteen equal to minus one, so
sum_r f(r)^2=54. Let v=(1,-1,0). This direction is one of the labelled
length-two representatives, with c_v=1/54, and shifting by v fixes f.
A field supported on component v with profile f therefore has zero
weighted divergence.

The scalar stencil acts on f with eigenvalue 3/4. Here is a direct count,
with no floating trigonometry. For a representative whose coordinate sum
is nonzero modulo three, the sum of its positive and negative shifted
profiles is -f; its pair contributes 3c_v f to Lf. A zero-sum
representative contributes zero. The active weight totals in the five
shells are respectively

    squared length:       2    4    8    10   16
    active weight total: 18    3   45    12    3.

For lengths two and eight exactly three of the six representatives are
active; all three axial representatives at lengths four and sixteen and
all twelve length-ten representatives are active. The total is 81, hence
Lf=3*81*f/324=(3/4)f. The transverse identity yields D=lambda with
lambda=3/4 on this one-component mode.

Choose x=y=e=0 and

    A_v(r)=f(r)*1,       B_v(r)=f(r)*j,

with other components zero. E_v=B_v/2. The field is rational, Gauss is
zero, and the source edge ell, of a different direction, has F_ell=0.
Thus every source collision remains the zero collision during this
free modal evolution. No incompatible charge background is required.

Write the mode amplitudes as (a,b). Free evolution is

    (a',b')=((1-lambda)a+b, b-lambda a),
    T=[[1/4,1],[-3/4,1]].                               (F8)

Because Omega(1,j)=1 and c_v sum f^2=1, (F7) gives exactly

    Gamma_L=lambda(4-lambda)/(16z)=1053/256.             (F9)

As a supplementary normalization check, the initial field energy is
[Q(j)+(3/4)Q(1)-(3/4)g(1,j)]/(2z)=837/16. This is a
prepared occupied-field example, not an emitted zero-field source.

The same Gamma occurs at every free tick: preservation of Omega_G gives
Omega_G(Ls,L^2s)=Omega_G(s,Ls). Thus four ticks have total 1053/64.

## 5. No mod-five state potential can remove this free action

Modulo five, lambda=2 and T has trace zero and determinant one. Its
characteristic identity gives T^2=-I and T^4=I. The FULL field state,
including E, therefore returns modulo five after four free ticks. The
source remains zero. This is a return of the quotient state, not an
exact return of the rational field and not a return modulo twenty-five.

But (F9) is 3 modulo five, so the four increments sum to 2 modulo five.
For any function Phi of the full source-field state modulo five,

    sum_(n=0)^3 [Phi(L^(n+1)s)-Phi(L^n s)]=0,

whereas sum Gamma_L=2. Therefore

    NO such Phi satisfies Delta Phi=Gamma_L modulo5
    on this declared carrier and free map.              (F10)

This excludes every state function on that quotient, not just a quadratic
ansatz. Equivalently, the proposed ramified carry
(Gamma_T-Delta Phihat)/5 cannot belong to R on every primitive step
for any Phi of that scope. One cannot assign it a well-defined residue
modulo five by dividing an element with nonzero residue by five.

For context, form the quadratic f_G by using the same symmetric energy
matrix G and the polarization of #1924's modular quadratic f. The scalar
free matrix preserves f_G exactly modulo five, while a matched collision
satisfies Delta(f_G/2)=B(d). It provides the expected collision primitive
but fails on (F9). The four-cycle proof shows that replacing it by a
nonquadratic function of the same quotient cannot repair the failure.

The scope excludes functions of extra clocks, finer residues or other
additional state, and excludes a different chosen action. It is not a
no-go for every phase law. In particular the previously declared
zero-free-phase lift remains a different mathematically valid model.

## 6. An explicit twenty-five-state action lift

Reduce every Gamma_T through R -> Z/25 and add it to a retained register
r in Z/25. Mark a character zeta25 with zeta25^5=j and read

    phase=zeta25^r,
    r'=r+Gamma_T(s) modulo25.                           (F11)

This is a triangular bijection on the complete source-field-plus-register
carrier. Inversion reverses the primitive core step and subtracts its
recovered forward increment. Refused collisions contribute zero. Free
steps contribute (F7), with no fitted parameter.

Five repetitions of one admitted collision have Gamma=B(d) at every
cut, hence

    r_after-r_before=5B(d),
    phase_after/phase_before=j^B(d).                    (F12)

The old static five-contact monodromy is retained. There are five faithful
characters with this restriction: replacing zeta25 by zeta25^(1+5t),
t in Z/5, leaves its fifth power j unchanged. They agree on the static
source-loop values and differ on the free witness, whose action is a unit
modulo five. The marked extension is therefore additional data; the old
source calibration alone does not select it. Intermediate open-path
coordinates are not generally the old five-valued pointer. On a centered
ordinary source orbit the gauges can be compared through
r=5 r_old+2 fhat(d), up to the fixed initial offset; (15) in PROOF.md gives
the corresponding increment identity. Only the closed-loop equality
(F12) is required here.

On the transverse free witness, 1053/256 reduces to 13 modulo twenty-five.
A blank pointer therefore advances 0,13,1,14,2 through four free ticks.
The core returns only modulo five at that point. This is not an exact
closed-path holonomy claim.

There is a limited minimum statement. In the class of additive action
readings in which a primitive unit action has a context-independent
translation u and five such increments must read j, u^5=j. Thus u has
order twenty-five, so a faithful cyclic target needs at least twenty-five
states. An actual unit collision action occurs for d=phi, B(d)=1.
This does not bound arbitrary devices with state-dependent gauges,
additional histories, different actions or different output contracts.
The quotient-potential obstruction (F10) is the separate reason that the
old mod-five compression cannot handle the selected full action.

## 7. Integral pointer implementation and explicit reading cost

A literal primitive twenty-fifth root is not an O coordinate. Instead use
two ordinary neutral pointer pairs

    (p0,q0)=(j^r0,-j^r0), (p1,q1)=(j^r1,-j^r1),
    r=r0+5r1 modulo25.

Each pair has Q-account four, so the complete pointer has account eight.
For an increment t in {0,...,24}, decode the current two marked digits,
compute (r+t) modulo twenty-five, and apply the ordinary pair contact to
powers 3 times the required digit changes, modulo five. Since rho^3=j,
this implements exactly (F11). The carry between digits is explicit.

For a complete occupied-pointer law, let P be the five prepared pairs
(j^a,-j^a). Apply this digit translation on P times P, and identity on its
complement in O^4. Both sets are invariant, the restriction is a
permutation, and the complement is fixed. The resulting map is a total
bijection preserving pointer sum and Q on all occupied pairs. The
phase-orbit membership test, digit decoding and state-controlled contact
powers are declared controls. No universal fixed ordinary-contact word
or native implementation is asserted.

Two copies of the existing #1925 reader use twenty references in total,
with account forty. They read r0 and r1 separately; the ordered pair
uniquely reads the twenty-five-state label. The pointer-plus-reader
subsystem therefore has account 48. This excludes the actual source and
field preparation energy and any separately funded work archives. It is
an explicit upper bound for this declared reader, not a minimum total
apparatus price. Reader inversion removes its newly written records.

The finite actual-work archive construction in PROOF.md can be attached
unchanged: the new pointer steps preserve their account, and actual work
still comes from Delta H of the same source-field transition. One must
keep the stated finite archive horizon and funding. This construction
provides a common mathematical current, work and phase path. It does not
select the action, character, controls, physical clock, quantum
coherence, physical occurrence or alpha.

## 8. Status and next tests

The new exact result is specific: the natural energy-metric polygon action
has a demonstrably nontrivial free-field contribution, admits no mod-five
state-potential compression on the declared quotient, and has a complete
explicit twenty-five-state extension retaining the old static monodromy.
The rational global field and gauge modes remain; no recurrence or
long-time emission theorem follows. The full-field audit is separately
preregistered and its actual execution status must be reported without
borrowing the earlier reduced audit's evidence.
