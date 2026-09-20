# Faithful moving chart and complete archive cycle

PUBLIC; candidate mathematical result at L1 under the stated ideal control
model; NON-CANONICAL. P-QDD-ION-SIDEBAND-WRITER-1, lock
[#1091](https://github.com/mathorn1973/twist-j/issues/1091).

This file proves the relation between a three-register engineering experiment
and the previously specified native record block. It does not identify ion
motion with native U. The physical control model and its pulse proof are
additional premises, not consequences of the chart below. All field labels
and additions in this file use F_5; energies and pulse times do not.

## 1. The complete twenty-state native domain

Write a native checkpoint as (p;q,r), with p=(a,b,c,d),
s(p)=a+b+c+d and z=s(p)+q+r. At native counter three, the four code points are

    Y_h(3)=(h,0,0,0;1-h,0),  h=1,2,3,4.

Their common initial port is (z,r)=(1,0). Let Y_h(n) be their actual free
native evolution for n>=3, using theta_n=popcount(n) mod 2. The four points
have one common port (z_n,r_n^0), where z_n is always 1 or 4. Define

    T_e(p;q,r)=(p;q-e,r+e),
    X_(h,e)(n)=T_e Y_h(n),    e in F_5.

The stable-domain identity proved in
[P-QDD-UNINTERRUPTED-RECORD-1](../P-QDD-UNINTERRUPTED-RECORD-1/)
is

    U_n T_e = T_(-e) U_n,

on z in {1,4}, where U_n denotes the checkpoint part of the step at counter n.
It holds for either controlling bit. The shift preserves z, and the selected
generators b,d,e have source parts independent of q,r. Consequently

    U_n X_(h,e)(n)=X_(h,-e)(n+1).                         (1)

The twenty points at each n are distinct. Distinct h remain distinct in the
source coordinates because each selected source map is invertible and common
to all four points. For fixed h, the value r=r_n^0+e distinguishes e.

Let H_n be the twenty-dimensional complex span of their orthonormal formal
point states. The restriction of the native linear pushforward to H_n is an
isometry onto H_(n+1). This makes no claim that the full native checkpoint
map is injective, unitary or a physical quantum channel.

## 2. Hardware labels, chart and inverse

Use three distinct five-level logical registers S, P and M. They stand for
the source label, the relative port label and the archive label. Their
physical realization is specified in [PULSE-PROOF.md](PULSE-PROOF.md).
The archive called M here is the register called A there. In each register
the logical basis is labelled 0,1,2,3,4.

The four admitted source states have hardware labels

    k=h-1 in {0,1,2,3}.

Thus LOW is hardware source level 0. Hardware level 4 is an explicit
outside-code extension, not a native h=0 code point. In particular the change
of labels is not a cyclic relabeling of the old five-value function f.

Define

    E_n |X_(h,e)(n)> = |h-1>_S |e>_P.                    (2)

This is an isometry from H_n onto the twenty-dimensional subspace

    H_code = span{|0>,|1>,|2>,|3>}_S tensor C^5_P

of the twenty-five-dimensional S,P register space. It is not a unitary onto
all twenty-five hardware states. On H_code its inverse is explicit:

    E_n^dagger |k,e> = |T_e Y_(k+1)(n)>.

The forward coordinates are equally explicit on H_n:

    h=(-1)^(n-3) s(p),
    k=h-1,
    e=r-r_n^0.                                         (3)

Equations (2)-(3) are defined on the declared point set. Applying these two
scalar expressions to an arbitrary checkpoint does not assert that it belongs
to this set, and does not give an injective chart of all F_5^6.

Let N be the logical negation N|e>=|-e>. From (1),

    E_(n+1) U_n = (I_S tensor N_P) E_n.                  (4)

After l consecutive native steps, with epsilon=(-1)^l,

    E_(n+l) N_(n,l) E_n^dagger = I_S tensor N_P^l        (5)

on H_code. The proof is induction, not a finite waiting-time test. Every
identity also holds after tensoring an untouched reference system.

The full admitted S,P,M domain has dimension 4*5*5=100. Three five-level
registers have dimension 125 and faithfully contain it. Three is the minimum
number of five-level registers that can faithfully contain this entire
100-dimensional domain. No minimum is asserted for experiments restricted to
ready inputs, for other carrier dimensions, or for apparatuses using a
different encoding.

## 3. Coarse writer with an explicit outside-code extension

Let X|e>=|e+1> and let

    f_bar(0)=1,
    f_bar(1)=f_bar(2)=f_bar(3)=f_bar(4)=2.

Define the full twenty-five-dimensional hardware writer

    D|k,e> = |k,e+f_bar(k)>.

With Pi_0=|0><0| on S,

    G_0 = Pi_0 tensor X^(-1) + (I-Pi_0) tensor I,
    D = (I tensor X^2) G_0.                             (6)

This definition deliberately gives response 2 to outside-code source level
4. It is a fully specified unitary extension. No assertion about a native
f(0) input follows from it.

On the native code, f(h)=1 for h=1 and f(h)=2 for h=2,3,4. The entrance
C_n=T_(f(h_n(p))) therefore obeys

    E_n C_n E_n^dagger = D                              (7)

on H_code, for arbitrary initial relative port label e. The construction
uses a source-controlled interaction. It is not a passive observation.

## 4. Waiting, signed exchange and information accounting

The archive M is held unchanged during the prescribed waiting interval.
This is an explicit ideal control assumption. Define the signed exchange

    S_epsilon |e,m> = |epsilon m, epsilon e>,
    S_epsilon = (N_P^l tensor N_M^l) SWAP_(P,M).

The complete hardware block, in chronological order, is D on S,P, l waiting
steps N on P, then S_epsilon on P,M. Its exact action is

    |k,e,m>
      -> |k,e+f_bar(k),m>
      -> |k,epsilon(e+f_bar(k)),m>
      -> |k,epsilon m,e+f_bar(k)>.                       (8)

For a ready relative port and blank archive,

    |k,0,0> -> |k,0,f_bar(k)>.                          (9)

For m!=0, the old archive content returns to the port with sign epsilon.
For e!=0, the archive receives e+f_bar(k), not f_bar(k). The block is a
permutation; no input information has been erased. A blank cell and a ready
port are distinct and necessary input conditions.

The native endpoint form follows from (2):

    |T_e Y_h(n)> |m>
      -> |T_(epsilon m) Y_h(n+l)> |e+f(h)>.             (10)

In raw native coordinates the final source p and z are their freely evolved
values, while

    r_out = r_(n+l)^0 + epsilon m,
    q_out = z_(n+l) - s(p_out) - r_out,
    m_out = e+f(h).

For e=m=0 the entire native checkpoint is its freely evolved endpoint.
For a coherent input |psi>=sum_(k=0)^3 alpha_k |k>, (9) gives

    Pi_LOW |psi> |0>_P |1>_M
      + Pi_HIGH |psi> |0>_P |2>_M,                      (11)

where Pi_LOW=|0><0| and Pi_HIGH=sum_(k=1)^3 |k><k| on the admitted source
subspace. Equation (11) preserves all HIGH coherences. It also specifies the
complete joint LOW--HIGH coherence; the reduced source alone is generally
not its original pure state. Correct basis outputs do not suffice to prove
this statement: relative phases and all source matrix units matter.

Repeating with fresh blank archive cells records the same coarse observable
in each cell. It produces correlated records, not independent draws or a
law selecting one realized outcome.

## 5. Explicit archive compiler and unoptimized pulse count

The [pulse construction](PULSE-PROOF.md) supplies G_c, the same controlled X^(-1) as in (6)
with any selected source level c, and its inverse. Each G_c or G_c^(-1)
uses fourteen blue-sideband pulses and two carrier pulses. Choosing c means
addressing the corresponding physical transition; it does not require
measuring the control register. Pulse phases and their action on unused
levels belong to the separate pulse proof.

For two generic five-level registers i,j, define

    SUM_g : |u,v> -> |u,v+g u>,   g in {+1,-1}.

For c=1,2,3,4 let b_c be the balanced integer representative of g c in
{-2,-1,1,2}. Then SUM_g is the product of G_c^(-b_c). These factors act
on orthogonal control sectors and commute. The c=0 sector is unchanged.
For either sign of g,

    sum_(c=1)^4 |b_c|=1+2+2+1=6.

Thus one SUM uses six controlled-shift blocks, or 84 blue-sideband and
12 carrier pulses. Negative exponents use the reverse pulse sequence with
the inverse phases, not a different assumed primitive.

The following chronological four operations exchange x,y exactly:

    y <- y+x,
    x <- x-y,
    y <- y+x,
    x <- -x.

Indeed (x,y) becomes (x,y+x), then (-y,y+x), then (-y,x), then (y,x).
There are three SUM operations and one local NEG. The separate carrier
construction implements a local NEG using eight carrier pulses with exact
relative phases. The unsigned archive exchange therefore uses

    18 G blocks + 1 NEG
      = 252 blue-sideband pulses + 44 carrier pulses.

For odd l, the sign correction adds a NEG on each output register, hence
sixteen more carrier pulses. Each physically executed waiting step uses
one NEG, hence eight carrier pulses. This convention implements each
declared step; cancellation of successive logical negations is not used
to replace the specified physical schedule.

The entrance writer is one G_0 plus the local X^2, whose phase-correct
carrier implementation uses twelve carrier pulses. It therefore uses
fourteen blue-sideband and fourteen carrier pulses. The complete block
has the following deliberately unsimplified count:

    blue-sideband pulses: 266,
    carrier pulses:       58 + 8 l + 16 (l mod 2).       (12)

These counts exclude initial cooling and preparation, frequency calibration,
state analysis, fluorescence detection, archival readout, and reset. They
are neither minimal counts nor fidelity or duration estimates. All the
controlled-shift blocks share the assumed motional mode and must restore
its vacuum with one common phase on every logical input. A failure of that
condition cannot be hidden by counting the pulses as logical gates.

## 6. What the moving frame does and does not establish

The hardware source register is fixed during the waiting steps. The native
source motion is carried by the time-dependent dictionary E_n. In
particular Y_h(n), z_n and r_n^0 depend on the known actual native history.
Equation (4) absorbs that history; it does not derive the ion Hamiltonian,
laser, oscillator, electronics, energy supply, pulse duration or timing
reference from n. Those are independent physical resources.

A laboratory clock can implement the NEG schedule. A declared relation
between its times and the native indices is then an additional engineering
dictionary. Decoding the observations using the same precomputed Y_h(n)
does not independently validate that dictionary as a law of nature. The
result is a faithful encoded comparison for the stated finite sector, not
a globally unitary physical realization of U.

The reference r_n^0 is essential. Replacing it by r_n^0+delta changes the
relative port coordinate to e-delta. Preparing the new label zero without
accounting for that change prepares a different native port. A reference
change is not a proof of readiness, and the elapsed-step parity used in the
final signed exchange must be physically controlled.

The pulse sequence changes the encoded checkpoint during the entrance.
Although (10) returns a ready input to its free endpoint, it does not make
the entire process a feeds_U=false decoder. The present construction is an
externally controlled intervention comparison. The read-only architecture
and required physical event/record contract remain as stated in
[#539](https://github.com/mathorn1973/twist-j/issues/539) and current
[CORE](../../canon/CORE.md) and [FRONTIER](../../canon/FRONTIER.md).

The stable-domain proof is inherited from
[P-QDD-UNINTERRUPTED-RECORD-1](../P-QDD-UNINTERRUPTED-RECORD-1/).
The separation between a transported reader and an actuator is also
explicit in [#998](https://github.com/mathorn1973/twist-j/issues/998).
The earlier affine construction and energy boundary remain unchanged in
[P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1](../P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1/)
and [P-QDD-AFFINE-ENERGY-CONTROL-1](../P-QDD-AFFINE-ENERGY-CONTROL-1/).

Independent carrier and pulse calibration, preservation of the quantum
state through the delay, a physically persistent archive, an event law and
the complete apparatus-family boundary are not supplied by this chart.
No L1-to-L5 gate or Canon status follows from it.
