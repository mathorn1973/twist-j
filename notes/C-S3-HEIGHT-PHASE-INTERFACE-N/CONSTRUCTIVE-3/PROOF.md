# A 95-contact finite-height compiler with returned common stock

NON-CANONICAL / L1 / analytical candidate. This is a new, expanded-stock
construction, distinct from the eight-slot searches. Its constants and word
were derived before the new executable's first run. Same-session review is
part of authorship, not independent scientific acceptance. The prospective
finite replay and its actual outcome are recorded separately.

## 1. Exact problem, law and stock

Use O=Z[j], rho=j^2, u=1-j, B=1-rho, J=1+rho and X=1+j-2j^3.
The five original inputs are

    I_t=(u+tB,u-tB,0,0,X,2,J,-J), t=-2,-1,0,1,2.

Addresses are zero based; products act chronologically from left to right.
The required output clock at slots 6,7 is
(rho^(t+2)J,-rho^(t+2)J). The complete six-slot G_t input is retained.

The only operation is the unchanged total contact C: it refuses unless
its two entries differ by an element of 2O, and otherwise fixes their mean
and multiplies their half-difference by rho. Every C is a total bijection,
C^5=id and C^-1=C^4. Sum, full Hermitian account and Q are preserved, and
each labelled residue modulo 1-j is preserved at every primitive.

J is an integral unit: J^-1=-rho-rho^3. Multiplication verifies this using
1+rho+rho^2+rho^3+rho^4=0. Modulo 2O the carrier is F16. Indeed Phi_5 has
no root over F2 and is not divisible by its only irreducible quadratic
T^2+T+1. The image of rho has order five. In particular B and J are units
modulo two. Parities below are F16 values; actual states remain integral.

The construction uses seven additional slots, all with common initial
values independent of the actual height. Set

    a_1=u, a_2=u-JB, a_3=u-B,
    x_-2=u-JB, x_-1=u-B, x_0=u,
    x_1=u+rho B, x_2=u+rho JB,
    d_s=-B*x_s/J, s=-1,0,1,2.

These are explicit integral O-valued constants, not lookup results chosen
by the runtime input. The full slot layout is

    0..7:   original I_t;
    8..10:  a_1,a_2,a_3;
    11..14: d_-1,d_0,d_1,d_2.

Call this seven-slot common stock Z. The gate g is original slot 5, whose
initial value is 2. The active height register x is original slot 0.
No bank of five input-dependent target clocks is supplied.

## 2. Three contacts separate the five heights by parity

Apply the fixed preprocessing word

    P=C(0,8) C(0,9) C(0,10).

Initially the even heights have parity u=1+j and the odd heights have
parity u+B=j+j^2. These classes are distinct and nonzero.

The first contact has reference a_1=u. Exactly the even heights admit,
giving x=u+(t/2)JB for t=-2,0,2. Odd heights retain x=u+tB.
The second contact has reference a_2=u-JB. Exactly t=-2,2 admit. The
negative value equals its reference and stays fixed; the positive value
becomes u-JB+J^2B=u+rho JB. All other x values stay unchanged.
The third contact has reference a_3=u-B. Exactly t=-1,1 admit. The
negative value stays fixed; the positive becomes u-B+JB=u+rho B.

Thus the final x value is precisely the displayed x_t in section 1.
For a direct guard check, their five parities in increasing t order are

    1+j^2+j^3,  j+j^2,  1+j,  j^3,  1+j^2.

These are five distinct nonzero elements in the degree-four field.
Before the second contact the +/-2 parity is 1+j^2+j^3, distinct from
both the zero-height and odd-height classes. Before the third contact
the two remaining odd heights share j+j^2, distinct from each of the
three completed even-height classes. This establishes every admission
and refusal used above, with no enumeration or search assumption.

The three reference slots may depend on t after P. Their complete actual
values are retained; no reset is made. The later literal inverse P^-1
returns those actual states to their common preparation.

## 3. A singleton marker with a complete inverse

For a fixed sample label s in {-1,0,1,2}, use its prepared reference

    d_s=-B*x_s/J.

Modulo 2O, B=J, so d_s has parity x_s, which is nonzero. Consider

    M_s=C(x,d_s) C(d_s,g),

where x is the preprocessed register and g initially equals 2.

If t differs from s, the first contact refuses because x_t and d_s have
different parities. The second also refuses because d_s has nonzero parity
and g=2 has parity zero. Thus the entire state is unchanged.

If t=s, the first contact admits and its second output is exactly

    (B*x_s+J*d_s)/2=0.

Its first output is x_s+d_s, the complete actual changed input register.
The second contact sends (d_s,g)=(0,2) to (B,J). Thus the gate is J only
on the selected sample, and is 2 on all other samples. The changed x and
reference are retained throughout; the program does not discard them.

If an intervening writer restores g and leaves x and d_s untouched,
then M_s^-1=C(d_s,g)^4 C(x,d_s)^4 restores all three entries exactly.
This inverse has eight contacts. The following writer has the required
restoration property.

## 4. A ten-contact controlled clock rotation

Let the target clock slots 6,7 be (rho^r J,-rho^r J). Put

    E=C(5,7), T=C(6,7),
    W_p=E T^(5-p) E^4 T^p, p in {1,2,3,4}.

This fixed word has 1+(5-p)+4+p=10 contacts. It touches only g and the
clock pair.

ACTIVE CASE: g=J and the clock is initially (J,-J), at phase zero.
E acts on (g,clock_minus)=(J,-J), giving (rho J,-rho J).
The clock's positive entry remains J. The clock contact T now refuses:
its difference is J+rho J=J^2, nonzero modulo 2O. Every one of the
5-p repeated T contacts therefore refuses. E^4 exactly reverses E,
restoring g=J and the phase-zero clock. Finally T^p rotates the opposite
clock pair to (rho^p J,-rho^p J). The gate has returned to J.

INACTIVE CASE: g=2 and the clock has ANY phase r modulo five.
E refuses because 2 is even and -rho^r J is nonzero modulo 2O.
T^(5-p) rotates the opposite clock pair to phase r+5-p. E^4 again
refuses at every contact for the same parity reason. T^p completes five
rotations in total, returning the exact clock pair to phase r. The gate
stays 2. Thus every inactive block fixes an already written phase, not
only the initial clock seed.

The active case deliberately assumes phase zero. The next section proves
that this hypothesis is satisfied whenever a marker is active. No active
arbitrary-occupied-clock extension is assumed.

## 5. The literal common word and full endpoint

Let the reference address for s be 12+s, so that -1,0,1,2 map to 11..14.
With M_s acting on slots (0,12+s,5), define

    A=P [product_(s=-1,0,1,2) M_s W_(s+2) M_s^-1] P^-1.

The product order is increasing s. All powers mean literal repetition;
each inverse contact is represented by four contacts. Every edge and every
repetition count is fixed independently of the actual height t.

At the start of each sample block, x equals its preprocessed x_t, the gate
is 2 and every reference d_s is in its common prepared state. If t differs
from s, the marker is inactive, W fixes every possible current clock phase,
and the inverse marker restores the unchanged complete state. If t=s,
all earlier sample blocks were inactive; therefore the clock still has
phase zero. The active marker produces g=J, W_(s+2) writes phase s+2
and restores g, and the inverse marker restores x,d_s,g. Every later
sample block is inactive and preserves this recorded clock phase.
Height -2 is never selected, and keeps phase zero, its required t+2.

The gate and all four marker references are restored at every block
boundary. These blocks never touch the three preprocessing references.
Consequently P^-1 receives exactly the complete state produced by P on
its four addressed slots and restores G_t and those three references.
It never touches either clock coordinate.

The exact endpoint is therefore

    A(I_t,Z)=(G_t,rho^(t+2)J,-rho^(t+2)J,Z)

for all five declared heights. All seven extra stock coordinates, every
original helper, the full two-slot height input and the gate return to
their initial values. Only the two clock coordinates change. This proves
the stronger nondemolition endpoint for this specific expanded-stock word.

The contact count is

    |P|+|P^-1|=3+12=15,
    |M_s W_(s+2) M_s^-1|=2+10+8=20,
    |A|=15+4*20=95.

Its unreduced literal inverse has 380 contacts. These are construction
counts, not shortest-word or stock-minimum claims. The map is globally
invertible because every primitive is a total bijection, independently
of this restricted five-input endpoint proof.

## 6. Resource and composition consequences

Every primitive preserves the complete sum, full Hermitian account, Q
and labelled residues. All seven stock coordinates are counted, including
references returned at the end. Write

    E_Z=sum Q(Z_l), H_Z=sum h(Z_l), Sigma_Z=sum Z_l.

The stock is explicit in the basis (1,j,j^2,j^3):

| Slot | Value | Hermitian square | Q |
| --- | --- | --- | ---: |
| 8 | (1,-1,0,0) | 3-phi | 5 |
| 9 | (-1,-2,-1,-1) | 2+phi | 5 |
| 10 | (0,-1,1,0) | 3-phi | 5 |
| 11 | (-2,-3,-3,-2) | 5+5phi | 15 |
| 12 | (1,1,0,-2) | 5+5phi | 15 |
| 13 | (-2,-2,0,-1) | 5 | 10 |
| 14 | (-1,-2,-3,-4) | 10+5phi | 25 |

For example, -B/J=1+2j+2j^2 gives each d_s by direct multiplication.
Also h(B/J)=3+4phi, while
h(x_-1)=h(x_0)=3-phi, h(x_1)=7-4phi and h(x_2)=10-5phi.
Here x_2=(1-j)^2 and phi^2=phi+1. Multiplying these four Hermitian
squares by 3+4phi gives the last four rows. The first three rows follow
from the corresponding fifth-root chord lengths.
Consequently

    E_Z=80, H_Z=33+14phi, Sigma_Z=(-4,-10,-6,-10).

These values are analytical predictions to be checked by the prospective
audit, not previously observed program output. The standalone 15-slot
preparation has Q=119+10t^2 and
H=52+15phi+(4+2phi)t^2. Stock restoration is not a reason to omit its
initial preparation from the account.

The established conditional assembly in ../PROOF.md section 5 now has the
explicit compiler premise, with h=7, c=95 and no translator SWAP. Using
the independently supplied source Y_n and the unchanged registered
read/copy/uncompute cycle gives, for every fixed finite k and all 10^k
prepared input sequences,

    N=39+25k,
    E_total=177+78k+10 sum_i t_i^2,
    H_total=70+37phi+k(30+18phi)+(4+2phi)sum_i t_i^2,
    Sigma_total=(1+4k,-9-2k,-6,-12),
    forward contacts=27345k,
    forward supplied reload swaps=5(k-1).

The common auxiliary preparation has 39+20k slots and account
177+60k. The unreduced complete inverse has 109380k contacts and the
same number of reload swaps. These are literal construction counts.

Each A U_i A^-1 retains the two permanent archives while restoring the
translator and actual read core. A returns its own G_t and stock but still
changes the clock; its inverse after U_i restores the common clock seed.
Every earlier input is parked and every archive remains in the state.
No operation infers the input phase n from the height t. The ten admitted
inputs are a Cartesian product of independently supplied mathematical
preparations, with no probability assumption.

The analytical all-finite-k composition is distinct from an executed full
apparatus replay. It gives no unlimited history on one finite carrier,
autonomous schedule, environment/bootstrap preparation, native-U
compilation, physical occurrence law, action calibration or Canon
promotion. The predecessor's all-integer impossibility remains intact:
these singleton markers are proved only for the five specified heights,
not for every integer t.
