# Permanent proper binding and a stable periodic relative equilibrium

Status: PASS
Scope: NON-CANONICAL, NEW_DECLARED L1, interacting two-group P=0 sector
Theorem status: conditional candidate-T; no Canon promotion
Fired audit falsifiers: none
Ownership: https://github.com/mathorn1973/twist-j/issues/1688
Preregistration pin: 79d2247fd8e6937347e367b922de1c6e24a54cb4

## What changes relative to the unbound common action

The predecessor #1687 has complete flow but its source energy tends to
zero at both time infinities. This probe adds an explicit positive
translation- and GL(2)-covariant pair interaction. The harmonic form and
its coefficient kappa>0 are new declarations, not derived mechanisms.
For two unit-multiplicity groups at total momentum P=0, put
r=(x1-x2)/2 and rho=2p1=-2p2. The reduced common action is

    S=integral [tr(Pi Gdot)+rho^T rdot-H]dt,
    H=K+E+V,
    K=tr(G Pi G Pi)/2,
    E=sqrt(rho^T G rho), V=kappa r^T G^-1 r.

G is SPD, Pi symmetric and rho nonzero. E is the sum of both individual
stream energies. D_stream=E^2 is the old P=0 stream diagnostic; it is
not identified with the square of total interacting energy H.

Variation changes both the matter and metric forces. The three energies
exchange exactly while H and the full linear-coordinate charge

    J=2G Pi+r rho^T,
    delta=det J-(tr J)^2/4

remain constant. The corrected virial derivative Cdot=-E/2+V permits a
balance that the predecessor's strictly decreasing C could not have.

## Robust all-time binding

PROOF.md proves universally on the declared real carrier

    E^2 V >= 4kappa delta.

For delta>0 and conserved energy H=h0 this gives

    E >= 2sqrt(kappa delta/h0)>0,
    16delta/h0^2 <= d^2 <= 4h0/kappa,
    d^2=4r^T G^-1 r.

The two groups therefore cannot collide or escape in the instantaneous
proper distance, and their stream energy cannot disappear. The metric
kinetic bound controls G on every finite interval; the positive energy
floor keeps rho away from its nonsmooth zero boundary. Together they
prove unique smooth flow for every real time.

The positive-delta sector is open within the fixed two-group P=0 carrier.
The bounds remain uniform in neighborhoods with delta bounded below and
H bounded above. This is robust permanent binding. It is not a theorem
for arbitrary nonzero total momentum, fixed-coordinate boundedness or
uniformly bounded metric entries at infinite time. Delta>0 is sufficient,
not asserted necessary. At Pi=0 it is impossible, so the metric momentum
must participate already in the initial preparation.

For kappa=0 the predecessor and the charge-area inequality instead give
proper escape as E tends to zero. For kappa>0 the upper proper-distance
bound holds even when delta<=0, but the nonzero-momentum protection need
not: a collinear branch may reach rho=0 in finite time. Neither comparison
is used to claim an unstated necessity theorem.

## An exact energy-minimizing periodic state

For the declared simple witness

    kappa=3, G=I, Pi=[[0,-1],[-1,0]], r=(1,0), rho=(0,6),
    J*= [[0,4],[-2,0]], delta=8,

the exact values are:

| Quantity | Value |
|---|---:|
| Metric kinetic energy K | 1 |
| Total stream energy E | 6 |
| Binding potential V | 3 |
| Total energy H | 10 |
| Stream diagnostic D_stream | 36 |
| Proper pair separation d | 2 |

With Omega=-J*/2 and A(t)=exp(t Omega), the full solution is
G=A A^T, Pi=A^-T Pi0 A^-1, r=Ar0 and rho=A^-T rho0. Its full labeled
period is sqrt(2)pi, with all the displayed scalar values constant.
The metric-only half-period does not return the labeled pair.

On any traceless elliptic charge level the proof obtains the sharp bound

    H >= 3kappa^(1/3)a^(2/3)+(a-sqrt(a^2-delta))^2/4,
    a=|G^-1/2 r wedge G^1/2 rho|/2 >= sqrt(delta).

Its one-variable minimum is unique. The selected witness attains it at
a=3 and H=10. For the specific kappa=3 and exact J=J*, the complete
minimum set is one orbit of the centralizer Z(J*). Energy sublevels have
compact representatives after quotienting its scale. Conserved energy
then proves nonlinear Lyapunov stability modulo that group on the exact
fixed-charge level. This statement is stronger than bounded separation
and narrower than arbitrary-charge or ordinary coordinate-orbit stability.
The group includes dilation; free overall scale is not an attracting mode.

## Completed exact finite audit

The first formal run completed after public six-file pin/readback and
receipt readback. Independently authored Fraction/Taylor and integer-pair/
Picard implementations produced byte-identical certificates. No scientific
dry run or shared scientific module was used.

| Check | Completed coverage |
|---|---:|
| Main trajectory cases | 210 |
| Positive / zero / negative delta | 51 / 21 / 138 |
| Formal order | 4 |
| Main coefficient rows | 1050 |
| Covariance cases | 6 |
| Periodic cases | 1 |
| Detected negative controls | 8 |
| In-memory payload records | 1329 |

Both programs calculate all state and invariant coefficients, Hamiltonian
directional derivatives, exact exchange, charge conservation, the gap
identity and the stated bounds. They compare the periodic trajectory with
the group exponential and check the minimum conditions. The displaced
state r=(2,0),rho=(0,3) retains J* but has H=16, showing that ellipticity
alone does not select the energy-minimizing orbit.

The controls detect omitted matter/metric reactions, pair-energy
misnormalization, coordinate/proper-distance confusion, missing metric
momentum, determinant/discriminant confusion, separate source-energy
conservation, and minimum-orbit overclaim. The two genuine false-force
controls evaluate actual nonzero H derivatives, not just labels.

Payload SHA-256:
5f981356b844fe332740ab1ba3d90de15479e71ccb32d96913dcfecfcca56d15.
Exact stdout is 455 bytes in 20 LF-terminated lines, SHA-256
cefaf22c7a6112835ccf1e4b4114e3b8ac0393445c7df7d6fa6c9582efef33ec.
The local run used Python 3.12.14 on Ubuntu 24.04.3 LTS, x86_64, and
completed in 52.288 seconds with exit zero and empty stderr. RUN.md binds
the unchanged verifier and immutable pin. Required public replay on both
architectures remains the merge gate at this record's preparation.

Finite Taylor audits support the analytical proof; they do not establish
infinite-time binding or nonlinear stability by numerical extrapolation.
The interaction, physical units, native realization, composite inertial
response, Lorentz interpretation and equality of inertial/gravitational
mass remain unresolved. No physical particle or Canon promotion follows.
