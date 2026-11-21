# Reversible elastic contact and the inelastic crossing boundary

Author: A. M. Thorn
Date: 2026-10-30
Candidate: C-PRIME-ELASTIC-CONTACT-N
Status: NON-CANONICAL / L1 / analytical candidate-T in a NEW_DECLARED model.
No authority, registered theorem promotion, public Git pin or independent review.

## 0. Inherited comparison

Use O=Z[phi], phi^2=phi+1, conjugation bar(phi)=1-phi. O_+ is the set
positive in BOTH real embeddings. The comparison reads
E(x)=Tr(x)/2, P(x)=(x-x')/2, and N(x)=E(x)^2-P(x)^2.
The predecessor PR #1837 at head 54631cb5128ff0b978a732b1367a8207c434e4f2
proves the complete two-body norm-shell criterion and
R_z(x)=(z/z')x', with z=x+y. It is a noncanonical mathematical input.
No contact law, position or time reading is inherited from native U.
The present claims do not close any public physical owner or layer gate.

## 1. Signed integer relative invariant [candidate-T]

For x=a+b phi, y=c+d phi define

    beta=bc-ad, z=x+y, T=N(z), r=N(x), s=N(y), D=T+r-s.

Direct multiplication gives

    xz'=(D+beta sqrt(5))/2,
    (x-y)z'=(r-s)+beta sqrt(5),
    (T+r-s)^2-4Tr=5 beta^2.                         (1)

Thus Tr((x-y)z')=2(r-s), and the reflection R_z on both inputs sends
beta to -beta, leaving r,s,z fixed. Its meaning is a signed relative
momentum numerator, not a velocity itself. At the center-of-momentum frame

    E_x^cm=D/(2sqrt(T)), E_y^cm=(2T-D)/(2sqrt(T)),
    p_x^cm=beta sqrt(5)/(2sqrt(T))=-p_y^cm.            (2)

The relative velocities are

    v_x-v_y=2sqrt(5) beta/[Tr(x)Tr(y)],
    v_x^cm-v_y^cm=2sqrt(5) T beta/[D(2T-D)].          (3)

Both denominators are positive. The second proportionality factor is
constant on a fixed ELASTIC (T,r,s) shell but not across arbitrary shells.
A streaming increment chosen proportional to beta therefore requires a
separate distance/time dictionary before it is a universal physical clock.

For clarity, N(z/z')=1 follows just by cancellation. Hilbert theorem 90
supplies the converse representation of all norm-one elements; it is not
needed for this elementary direction. The two split prime-ideal orientations
are arithmetic data, not an assertion of physical particle chirality.

## 2. Exact integer elastic gate [candidate-T]

Write z^2 x'=n0+n1 phi with n0,n1 integers and T=N(z)>0. Define

    chi(x,y)=1 iff n0=0 mod T and n1=0 mod T.

This is exactly R_z(x) in O, since R_z(x)=z^2 x'/T. If chi=1, set

    C(x,y)=(R_z(x),z-R_z(x));

otherwise C(x,y)=(x,y). Every output stays in O_+^2. The inherited
R_z^2=id proves C^2=id and chi(C(x,y))=chi(x,y). Conjugating both inputs
commutes with C and preserves chi. If chi=1, beta changes to -beta;
if chi=0 it is unchanged. At beta=0, C is the identity.

No factorization is required for this decision. Prime-ideal valuations
explain the obstruction, while remainders implement it. There is no fixed
modulus M>=1 that decides chi for all inputs merely from their coefficients
modulo M. Indeed (x,y)=(1,phi^2) and (1,(1+M)phi^2) have identical such
residues. By the predecessor's all-c family theorem the first is admitted
and the second is not. Thus parity or a single fixed finite residue alone
cannot replace the variable modulus T on the unbounded carrier.

An optional reversible scratch bit h can carry chi by XOR, never assignment.
For an actual contact gate, (s,h)->(C(s),h XOR e(s)) is involutive whenever
e(C(s))=e(s), for instance e=chi*1_[beta!=0]. This stores collision parity,
not a persistent fresh archive of arbitrarily many events. No auxiliary bit
is needed for the basic gate C or the spatial map below.

## 3. Total exact crossing model [definition and candidate-T]

Let Sigma=(2Z+1) x O_+^2. The odd signed register q samples a grid whose
origin is between sites. It avoids endpoints lying exactly at the contact;
this is an explicit chosen convention. q is not automatically a physical
separation or a coordinate of the native automaton.

Fix a law parameter kappa in {0,1}, and for s=(x,y) compute

    q_free=q+2 beta(s).

Define

    F_kappa(q,s)=(-q_free,C(s))
        if kappa*chi(s)=1 and q*q_free<0;
    F_kappa(q,s)=(q_free,s) otherwise.                (4)

When reflected, the part of the displacement remaining after the contact
must reverse along with the momentum. Because q and q_free are odd they
never equal zero. In the reflected case the exact event fraction is
lambda=-q/(2beta), 0<lambda<1, and the post-event displacement is

    (-2beta)(1-lambda)=-q-2beta=-q_free.              (5)

This proves that (4) is exactly the sampled broken-line motion with the
chosen stream velocity 2beta, not an arbitrary endpoint sign correction.
If reflection is unavailable or kappa=0, the path transmits.

The map preserves z,r,s, positivity and odd-grid membership. Define physical
momentum reversal on the comparison carrier by

    Theta(q,x,y)=(q,x',y').

It changes beta to -beta, preserves chi, and commutes with C. Then

    F_kappa^(-1)=Theta F_kappa Theta.                 (6)

Proof by the two cases. A transmitted path has reversed endpoints q_free,q,
with the same admission test; if they cross but reflection is disabled,
it stays disabled under Theta. It retraces the segment. For a reflected
path put Q=-q-2beta and beta_out=-beta. After Theta the trial point is
Q+2beta=-q. It lies across zero from Q, so the reverse path reflects again,
returning -Q-2beta=q and restoring the pair by C^2=id. These exhaust the
carrier, including beta=0. Hence both a left and a right inverse exist.

This holds for every state, not only a finite tested box. Kappa=0 and
kappa=1 give distinct reversible models with the same arithmetic and
conservation rules. Choosing kappa=1 is a hard-contact assumption, not a
consequence of the prime-ideal criterion or the addition of q.

For beta!=0 a trajectory crosses the contact at most once. Before crossing,
q beta<0. After either reflection or transmission q_out beta_out>0, and
its magnitude then grows without another encounter. Nonzero-beta bound
orbits do not occur. beta=0 gives stationary arbitrary separations, not a
restoring interaction or a derived bound-state spectrum.

## 4. Two traps avoided by the crossing construction [candidate-T]

Let s_plus=(phi^2,1), beta=+1, and s_minus=(1,phi^2), beta=-1. Both have
z=2+phi and chi=1. A naive rule that flips only momenta on a crossing and
keeps the free endpoint has

    (-1,s_plus) -> (1,s_minus),
    ( 3,s_minus)-> (1,s_minus).

The first crosses and the second does not. It is not injective. Equation
(4) instead maps the first input to (-1,s_minus), preserving invertibility.

A trigger that examines only q=0 also fails to detect general crossings:
q->q+2beta can pass from -1 to +1 without ever sampling zero. On the odd
grid it NEVER samples zero. On an arbitrary integer grid the congruence
class of q modulo the increment likewise prevents many visits to zero.
A contact phase or crossing test must address this; it cannot be omitted.

Equation (4) is contact-supported in the chosen relative coordinate but
NOT a uniformly finite-range cellular automaton on the entire carrier:
beta is unbounded, and so is the displacement 2beta. Serializing motion
into unit shifts requires explicit clock and resource accounting. No
physical-register locality, native-U compilation or universal speed scale
is claimed merely from arithmetic locality of the guard.

## 5. A genuine inelastic channel and a position-grid failure [candidate-T]

For z=3+2phi the complete ordered positive decomposition fibre is

    (1,2phi^2),       (r,s,beta)=(1,4,-2),
    (phi^2,2+phi),    (r,s,beta)=(1,5, 1),
    (2+phi,phi^2),    (r,s,beta)=(5,1,-1),
    (2phi^2,1),       (r,s,beta)=(4,1, 2).             (7)

Completeness follows by 0<a<3 and positivity of x and z-x in both
embeddings, or by the predecessor's exact criterion. The elastic alternative
to the first state is not integral, but the second state is integral and
has the same total. Thus an inelastic (1,4)->(1,5) output is arithmetically
available. No law selecting that transposition has been derived.

It cannot simply be substituted into (4) while keeping the same meaning
of the stream velocity 2beta on a COMMON unit tick. Start at q=1 with
beta_in=-2; choose beta_out=1 at the contact. The contact occurs at
lambda=1/4 and the remaining displacement is

    q_out=2beta_out(1-lambda)=3/2,                    (8)

outside 2Z+1 and even outside Z. The incoming q=3 gives q_out=1/2.
The general formula is

    q_out=(beta_out/beta_in)(q+2beta_in).             (9)

This is an exact failure of THAT common-tick streaming prescription,
not a theorem excluding all integer inelastic models. Enlarging the
position/phase carrier, introducing a reversible residual-time register,
or supplying a differently calibrated source-fixed stream rule are distinct
possible repairs. They require their own complete carrier and inverse.
A bit that only says 'collision occurred' does not represent an arbitrary
fractional residual. No universal minimal register size is asserted.

Furthermore (3) shows that the relationship between beta and actual
relative speed changes with r,s. For (7), with T=11, the coefficients are
11sqrt(5)/56 on the (1,4) shell and 22sqrt(5)/105 on the (1,5) shell.
In actual center-of-momentum units their relative-speed ratio is -8/15,
not the -1/2 from the selected beta-only stream. Thus physical inelastic
transport has a separate calibration problem as well as a carrier issue.
Neither is cured merely by an allowed norm-shell transition.

## 6. Reusable conclusions and remaining work

The derived integer guard is exact, the selected elastic crossing update
is a total time-reversal-symmetric bijection, and its naive competitor
has an explicit collision of preimages. The inelastic example is real
arithmetic admission, together with an exact obstruction to one proposed
position/time implementation. All remain NON-CANONICAL.

The next scoped physical question is to derive or independently admit a
contact law and a clock/distance dictionary on one complete state carrier.
No equation in this note is named original U, no bound object is created,
and no completeness of physical readings or L1-to-L6 lift is assumed.

The standard continuum elastic collision map has an established literature,
for example T. E. Kouloukas, Relativistic Collisions as Yang-Baxter maps,
arXiv:1706.06361 (2017). No claim of novelty for that continuum map is made;
its stronger properties are not imported for the guarded lattice map.
