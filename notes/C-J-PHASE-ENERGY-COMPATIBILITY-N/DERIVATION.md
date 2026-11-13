# Independent analytical derivation

PUBLIC / NON-CANONICAL / L1. Candidate C-J-PHASE-ENERGY-COMPATIBILITY-N.
Author identity for repository custody: A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.

This derivation follows ATTACK.md at
f398cbe9e72b9dae2744feaeff0832100a30bd00 and the equations in PREREG.md at
81b10ebb36a7b80482d500ce96e9e51c92a1ec55. It was written before this reviewer
read the author's PROOF.md, audit.py or source verifier. No scientific code
was executed. A second model context independently checked part B using
only its exposed equations; its agreement and cautions were incorporated.
These are assistant model contexts, not external peer review.

The coordinator supplied author-file commit
 e690cda29eda557ddde8b3f7f486a42cd15858e4 while this document was being
written, with a short summary already implied by the preregistration.
The independent analytical work below, including the 124-step hand trace,
had already reached the same conclusions before that message. No author
file at that commit has yet been opened.

## A. Complete cycles

Let S be a finite set, T a permutation, E a conserved integer-valued
function, and a:S->F5. Integers in the following equation are reduced
modulo five. Write f(s)=a(s)-kappa E(s)-beta. If f=chi o T-chi, summation
around a cycle C telescopes, giving sum_C f=0. Conversely, choose s_0 on
each cycle of length L and define

    chi(T^j s_0) = sum_(i=0)^(j-1) f(T^i s_0),  0<=j<L.

The cycle sum being zero makes the last edge consistent. Thus the exact
necessary and sufficient condition is

    sum_C a = L (kappa E(C)+beta) in F5 for every cycle C.

There is no division by L. If L=0 modulo five and sum_C a=0, that cycle
places no restriction on kappa,beta. The potential is unique up to one
additive constant per cycle. The statement requires complete cycles of the
specified state, not a projected return, and by itself has no physical
phase interpretation.

For the funded source, fix eta,c momentarily and let G_h be its requested
Q_h or P_h, with h=epsilon sigma. Both integer gates satisfy
G_h^(-1)=G_(-h). At total energy E the admissible integer states are
H(x)<=E and their bank is uniquely b=E-H(x). The gate attempts G_h x;
it accepts exactly when H(G_h x)<=E, otherwise leaves x fixed and flips
sigma. Let R flip only sigma. For the same fixed gate the inverse is RFR:
its attempted integer move is the opposite of the final direction. If
that predecessor is admissible, take it and preserve the final sigma;
if not, retain the integers and reverse the final sigma. In the first
case a forward accepted step is recovered; in the second case the same
inadmissible attempt certifies the forward rejection. This also proves
both inverse compositions. For the complete T, first replace c by c-1
modulo four, select that gate, and apply its inverse. Eta is unchanged.
Therefore T is a permutation preserving E on the whole carrier. Each
fixed-E shell is finite, so every complete state is on a finite cycle.

For an accepted Q step, Delta p=Delta u=Delta v=0. For an accepted P step,
q stays fixed and Delta p=h while Delta u=Delta v=hq. A rejected step
changes none of those integers. On every branch, exactly over Z,

    a_integer(s) = q Delta p = Delta u = Delta v.

Consequently every complete orbit has zero integer area sum. The proposed
residue phase is the coboundary of chi(s)=u modulo five on the whole
carrier. In particular, (kappa,beta)=(0,0) works universally.

For necessity, start at (q,p,u,v,b,sigma,eta,c)=(0,0,0,0,0,+,+,0).
Every requested gate costs one energy unit, so all steps reject. Only
sigma and c change; after four steps both return, and no earlier c return
is possible. This E=0 length-four cycle forces 4 beta=0, hence beta=0.
The state (0,0,1,0,0,+,+,0) has E=1. Each proposed Q step adds one to H;
each proposed P step also adds one because q=0. It likewise has period
four and forces 4(kappa+beta)=0. Thus kappa=0. These two actual cycles
prove the universal result without any finite-inventory extrapolation.

### The two cold preparations: independent hand trace

For (0,0,1,-1,B,+,+,0), put r=(u+v)/2. Then u=r+1, v=r-1,

    E=B+2,  b=B-q^2-p^2-2r^2.

The exact reduced attempted gates are Q_h:q->q+h and
P_h:(p,r)->(p+h,r+hq), accepted if q^2+p^2+2r^2<=B after the attempt.
For B=0 every move rejects and the complete period is four, E=2.
For B=4 the following table is a hand calculation of the state at every
fourth step. Each row has c=0, eta=+1 and b=4-q^2-p^2-2r^2.
The four-letter word records acceptance (A) or rejection (R) for the
four transitions to the next row. No program produced this table.

| t | q | p | r | sigma | next four |
|---:|---:|---:|---:|:---:|:---:|
| 0 | 0 | 0 | 0 | + | AAAA |
| 4 | 0 | 0 | 1 | + | ARRA |
| 8 | 1 | -1 | 0 | + | RRAA |
| 12 | 0 | -2 | 0 | + | RRRA |
| 16 | 0 | -1 | 0 | - | ARRA |
| 20 | -1 | 0 | -1 | - | RRAA |
| 24 | 0 | 1 | -1 | - | AAAA |
| 28 | 0 | 1 | 0 | - | AAAA |
| 32 | 0 | 1 | 1 | - | ARRR |
| 36 | -1 | 1 | 1 | + | ARAR |
| 40 | 1 | 1 | 1 | + | RAAR |
| 44 | 2 | 0 | 0 | + | RRAA |
| 48 | 1 | -1 | -1 | + | RRAR |
| 52 | 0 | -1 | -1 | - | ARRR |
| 56 | -1 | -1 | -1 | + | AAAA |
| 60 | -1 | -1 | 0 | + | AAAA |
| 64 | -1 | -1 | 1 | + | AAAR |
| 68 | -1 | 0 | 1 | - | RARR |
| 72 | -1 | 1 | 0 | + | AARR |
| 76 | 0 | 2 | 0 | + | RAAR |
| 80 | 1 | 1 | 0 | + | RARR |
| 84 | 1 | 0 | -1 | - | AAAA |
| 88 | 1 | 0 | 0 | - | AAAA |
| 92 | 1 | 0 | 1 | - | AAAR |
| 96 | 1 | -1 | 1 | + | RRAR |
| 100 | 0 | -1 | 1 | - | ARRA |
| 104 | -1 | 0 | 0 | - | ARRR |
| 108 | -2 | 0 | 0 | + | AARR |
| 112 | -1 | 1 | -1 | + | ARAR |
| 116 | 1 | 1 | -1 | + | RRAA |
| 120 | 0 | 0 | -1 | + | AAAA |
| 124 | 0 | 0 | 0 | + | return |

The 31 states preceding the return are distinct. A complete return must
have t divisible by four, so the least period is 124. Its energy is six
and its area sum is zero by the exact coboundary. Thus the two cold-orbit
constraints are

    4(2 kappa+beta)=0,  124(6 kappa+beta)=0 in F5.

Their coefficients reduce to two independent equations
2 kappa+beta=0 and kappa+beta=0. Hence their allowed pair is again only
(0,0). This handwritten calculation is analytically checkable evidence,
not a completed execution of the preregistered exhaustive inventory.

## B. The normalized Fourier comparison

Let R=sqrt(1+m^2) and X be the Pauli exchange matrix. Since
(I-imX)(I+imX)=(1+m^2)I, the declared W is unitary. Its determinant is
one and its trace is 2 cos(k)/R. Its characteristic polynomial therefore
has roots exp(+i omega), exp(-i omega), where

    omega(k)=arccos(cos(k)/R) in (0,pi).

Because m>0, |cos(k)/R|<1 for all real k: the branch is smooth and there
are no eigenvalue degeneracies. At k=0, tan(omega)=m and omega lies in
(0,pi/2), so omega(0)=arctan(m). Direct implicit differentiation gives

    omega'(k)=sin(k)/sqrt(m^2+sin^2(k)),
    omega''(k)=m^2 cos(k)/(m^2+sin^2(k))^(3/2).

Thus omega''(0)=1/m. At k=pi the curvature is instead -1/m; a claimed
global positive curvature would be false, but it is not preregistered.

For E_phase=A omega and p_phase=B k,

    E_phase(0)=A arctan(m),
    d^2 E_phase/dp_phase^2 at 0 = A/(B^2 m),
    M_curv=B^2 m/A.

The m=0 positive principal phase is |k| near zero, so its speed reference
is its one-sided slope, giving c=A/B. Therefore

    E_phase(0)/c^2 = B^2 arctan(m)/A,
    M_curv / (E_phase(0)/c^2) = m/arctan(m) > 1.

Strictness follows from m-arctan(m)=integral_0^m t^2/(1+t^2) dt>0.
No common positive linear A,B can remove the mismatch. This contradicts
exact relativistic dispersion in those declared variables, since such a
dispersion would force E''(0)=c^2/E(0). It does not identify M_curv with
measured force-response inertia. An offset changes rest energy without
changing curvature, so the exclusion of offsets is substantive.

For the alternative variables, positivity of sin(omega) gives

    Ehat=R sin(omega)=sqrt(m^2+sin^2(k)),  phat=sin(k),
    Ehat^2-phat^2=m^2,
    omega'(k)=phat/Ehat=d sqrt(m^2+phat^2)/dphat.

Where cos(k) is nonzero, phat is a smooth local coordinate and the last
derivative also equals (dEhat/dk)/(dphat/dk). At cos(k)=0 the latter
quotient is 0/0: the shell derivative still exists as a function of
phat, but phat is not a local coordinate on the original k carrier.

Globally, k and pi-k have the same phat and Ehat, while
omega(pi-k)=pi-omega(k). Their phases differ except when cos(k)=0.
For example k=0 and k=pi map to the same (phat,Ehat)=(0,m) but have
phases arctan(m) and pi-arctan(m), and opposite phase curvatures.
Moreover phat is restricted to [-1,1] and Ehat to [m,sqrt(1+m^2)].
This bounded shell segment is not invariant under arbitrary ordinary
Lorentz boosts. The identity supplies neither unrestricted Lorentz
symmetry nor global phase recovery, a canonical change of variables,
or a complete native or physical dynamical interpretation.

### Explicit weak-step rest scaling and bound

The substitution m=epsilon M alone does not specify an energy unit.
Choose explicitly E_epsilon=omega/epsilon and p_epsilon=k/epsilon;
then c=1 and the same calculation gives M_curv=M. The rest-energy defect
has the exact identity

    M-arctan(epsilon M)/epsilon
      = epsilon^2 integral_0^M s^2/(1+epsilon^2 s^2) ds.

For every epsilon,M>0 this implies

    epsilon^2 M^3/[3(1+epsilon^2 M^2)]
      <= M-E_epsilon(0) <= epsilon^2 M^3/3.

The defect is positive, and for fixed M tends to zero with leading term
epsilon^2 M^3/3. This is a controlled rest limit in an additional family,
not a uniform small error for unbounded M, a full dynamical continuum
limit, or a repair of any fixed positive rung such as m=2.

## Independent outcome before author-file exposure

No analytical counterexample was found to the scoped preregistered
claims. Necessary qualifications are explicit: complete-state cycles,
modulo-five coefficients, positive principal branch, local curvature,
a common linear calibration, a local nonlinear momentum chart, and an
explicit weak-step scaling. The finite exhaustive code audit remains
unexecuted and unreviewed at this point. A and B act on different declared
constructions; their juxtaposition creates no common native carrier.
