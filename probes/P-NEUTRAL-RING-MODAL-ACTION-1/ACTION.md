# A discrete contact action and the trace-energy boundary

NON-CANONICAL L1 analytical candidate. This document supplies exact
derivations for the declared carrier. It does not identify a physical
action quantum, assign a Canon status, or establish a variational rule
for the complete parity-gated contact. No scientific program or imported
verifier was executed while writing it.

## 1. Carrier and a primitive integral symplectic form

Let K=Q(j), O=Z[j], Phi_5(j)=0, p=j^2 and

    Q(x)=Tr_(K/Q)(x conjugate(x))/2.

In the ordered power basis (1,j,j^2,j^3), write

    Omega0 = [[ 0, 1, 0, 0],
              [-1, 0, 1, 0],
              [ 0,-1, 0, 1],
              [ 0, 0,-1, 0]].

This is the trace form

    Omega0(x,y)=Tr_(K/Q)(gamma x conjugate(y)),
    gamma=(j-j^(-1))/5.

Indeed its entry (k,l), for k,l=0,...,3, is

    [Tr(j^(k-l+1))-Tr(j^(k-l-1))]/5.

Using Tr(j^r)=4 when 5 divides r and -1 otherwise gives the displayed
matrix. Its Pfaffian is 1 and determinant is 1. It is therefore
alternating, nondegenerate and unimodular over O's integer lattice.

Multiplication by p preserves Omega0 because p conjugate(p)=1. It also
preserves Q. The choice of this particular primitive form is explicit;
uniqueness or physical selection is not asserted.

## 2. Integral Darboux coordinates and the exact step

The columns of

    B = [[1,1,0,0],
         [0,0,1,0],
         [0,1,0,0],
         [0,0,0,1]]

are the integral basis (1,1+j^2,j,j^3). Its determinant is -1, and

    B^T Omega0 B = [[0,I2],[-I2,0]].

Write coordinates in this basis as (q1,q2,pi1,pi2), so

    x=q1+q2(1+j^2)+pi1*j+pi2*j^3.

Multiplication by p has matrix

    M = [[-1,-1,0,1],
         [ 1, 0,0,0],
         [ 0,-1,0,0],
         [ 0,-1,1,0]].

For example, p*1=(1+j^2)-1, p*(1+j^2)=-1-j-j^3,
p*j=j^3 and p*j^3=1. These four identities give every column of M.
Consequently M is an integral symplectic map and M^5=I.

## 3. An explicit discrete generating action

Define the global rational quadratic function

    G(pi,q') =
        -pi1*q2' + pi2*(q1'+q2')
        -pi2^2/2 - (q1'+q2')^2/2.

Use the generating-function convention

    q=-partial_pi G,       pi'=-partial_q' G.

Differentiation gives

    q1=q2',
    q2=pi2-q1'-q2',
    pi1'=q1'+q2'-pi2,
    pi2'=pi1+q1'+q2'-pi2.

Solving the first two equations and substituting into the last two gives

    q'=(-q1-q2+pi2, q1),
    pi'=(-q2, pi1-q2),

which is exactly M. There is no chart singularity: the displayed equations
solve globally. G is half-integral on integer arguments.

Thus the multiplication step has a concrete rational discrete generating
action and a primitive integral symplectic structure. Existence of this
action is stronger than merely naming a logarithm, but it does not make
Q the Hamiltonian generating a continuous interpolation.

## 4. Relation to the admitted contact

For an admitted pair x-y in 2O, set

    s=(x+y)/2,       d=(x-y)/2.

Both s,d belong to O, and the registered contact is

    (s,d) -> (s,pd).

The result above therefore supplies its difference-sector action. First
select the product normalization Omega0_s direct-sum Omega0_d. In that
normalization an explicit generating function for the admitted operation is

    G_pair = -pi_s dot q_s' + G(pi_d,q_d').

The first term generates identity on s; the second generates p on d.
This product normalization must be distinguished from the inherited
per-site form. Under x=s+d, y=s-d, the native per-site direct sum pulls back as

    Omega0_x direct-sum Omega0_y
        -> 2 Omega0_s direct-sum 2 Omega0_d.

Cross terms cancel by bilinearity. Consequently the generating action
with that inherited convention is 2G_pair, with the corresponding
factor two in the canonical boundary one-form. The unchanged map alone
does not distinguish these common normalizations.

The account satisfies

    Q(x)+Q(y)=2Q(s)+2Q(d).

These statements apply to the admitted sublattice and its displayed
real extension. They do not supply a global variational principle that
chooses between this branch and the identity on the refused complement.
The parity predicate, identity-refusal convention and any physical
implementation of that decision remain additional parts of the complete
contact law.

## 5. Complete constant-rational-form classification

Consider any constant rational alternating form Omega on K preserved by
p. The trace pairing Tr(x conjugate(y)) is nondegenerate, so a unique
Q-linear operator T represents it as

    Omega(x,y)=Tr(Tx conjugate(y)).

Invariance under p implies T p=p T. Since K=Q[p] and the minimal
polynomial of p has degree four, every such T is multiplication by an
element gamma of K. Alternation is equivalent to

    conjugate(gamma)=-gamma.

Conversely every such gamma gives an invariant alternating form;
nonzero gamma gives nondegeneracy. Thus the complete class is

    Omega_gamma(x,y)=Tr(gamma x conjugate(y)),
    gamma=A(j-j^(-1))+B(j^2-j^(-2)),       A,B in Q.

This includes every integral form. No positivity assumption has been
used.

## 6. Q cannot generate this step in that rational class

Identify K tensor R with C^2 through
sigma1(j)=exp(2pi i/5), sigma2(j)=exp(4pi i/5).
Write z_i=q_i+i r_i, phi=(1+sqrt(5))/2 and t=sin(pi/5).
For the preceding gamma,

    g1=Im sigma1(gamma)=2t(phi A+B),
    g2=Im sigma2(gamma)=2t(A-phi B),

and

    Omega_gamma=2g1 dq1 wedge dr1 + 2g2 dq2 wedge dr2,
    Q=|z1|^2+|z2|^2.

With convention i_(X_Q) Omega_gamma=dQ, Hamilton's equation is

    dz_i/dt_clock = -i z_i/g_i.

Hence the frequency ratio is

    omega2/omega1 = g1/g2 = (phi A+B)/(A-phi B).

Both denominator and numerator are nonzero for nonzero rational (A,B).
If the ratio were rational r, irrationality of phi would give

    A+rB=0,       B-rA=0.

These imply (1+r^2)A=0 and then B=0, contradicting nondegeneracy.
The ratio is therefore irrational.

An exact common-time map equal to multiplication by p would instead
require, for some nonzero duration tau,

    tau/g1 = 6pi/5 + 2pi n1,
    tau/g2 = 2pi/5 + 2pi n2,       n1,n2 in Z.

Their ratio is rational, giving a contradiction.

This proves the candidate obstruction for all constant rational
symplectic forms, even if p-invariance was not initially assumed:
a Hamiltonian time map must preserve its symplectic form, so that
invariance is necessary. Multiplying Q by a common nonzero constant,
including the difference-sector factor two above, does not alter the
frequency-ratio obstruction.

The result excludes this autonomous Q-flow identification. It does not
exclude discrete generating actions, real nonarithmetic forms, another
energy reading, time-dependent Hamiltonians or an enlarged carrier.

## 7. Positive real constructions

A real Q-flow realization exists. Choose tau>0 and positive branch angles

    theta1=6pi/5+2pi n1,
    theta2=2pi/5+2pi n2,

and set

    Omega=(2tau/theta1)dq1 wedge dr1
          +(2tau/theta2)dq2 wedge dr2.

It is compatible with the standard complex structure and gives

    z_i(t_clock)=exp(-i theta_i t_clock/tau) z_i(0).

Its time-tau map is exactly p. The simplest positive choice is

    Omega=(5tau/(3pi))dq1 wedge dr1
          +(5tau/pi)dq2 wedge dr2.

No choice of tau makes this form rational on K, by the proved
obstruction. Branches and common scale remain unselected.

Alternatively retain Omega0. Its positive embedding coefficients are

    g1=2sin(2pi/5)/5,       g2=2sin(pi/5)/5.

The real positive quadratic reading

    H_mod=3g1|z1|^2+g2|z2|^2

then generates mode frequencies 3 and 1. At duration 2pi/5 its map is
again p. This is a concrete alternative energy reading, not Q and not
an independently established physical energy or action quantum.

For Omega0, p also commutes with X_Q because it preserves both Omega0
and Q. Therefore p exp(s X_Q) is an available symplectic lapse family.
It retains a discrete step and a separate lapse parameter; it does not
turn p itself into a time-tau Q-flow or select one physical clock.

## 8. What remains to normalize

Multiplying the selected symplectic form and generating action by any
common nonzero real factor leaves the discrete map unchanged. Requiring
integer coefficients restricts admissible arithmetic scalings but does
not assign a joule-second unit. Primitivity of Omega0 fixes the lattice
gcd of this selected form, not a physical phase period.

Nor does the existence of G imply a phase law exp(iG/A_*), a Born rule,
or a preferred A_*. Such a law requires an additional carrier and
normalization contract. The contact's principal difference phase is
+4pi/5; the positive exp(-iH) representative is 6pi/5. A five-step return
does not choose an unwrapped frequency, and this step is distinct from
the Canon's fiber increment 2pi/5.

The constructive outcome is an exact arithmetic discrete action plus
explicit continuous realizations with their changed data exposed. A
physical closure must connect one chosen action, a funded energy
reading and an independently defined clock on the same carrier. It
must then retain that coefficient in momentum and recoil. No Planck
constant, electromagnetic coupling or electron identification follows
from the constructions in this document alone.