# Induced quadratic energy partition and QDD processing boundary

**NON-CANONICAL / PROOF-FIRST / CONDITIONAL L1 CLAIMS ONLY.**

This is the argument to be audited by the new probe
`P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1`. Its public basis is
`4e794a01aec719a4536f2028ecbfd2f876a19e2b`, ACTIVE Public Canon v76.
The completed transport and coupling results are inputs at their own
conditional mathematical scopes. The analytical map in
`notes/DECODER-PHYSICAL-BORN-MAP.md` motivates this new probe; it is not an
execution record or additional evidence. This source text assigns no public
status and remains unchanged after the pin.

## 1. Fixed carrier, source and inherited energy

Let `V=C_c(D3,Q)`, `D3={x in Z^3:sum_i x_i even}`. For the complete shells
of squared norms `(2,4,8,10,16)`, set weights `(6,1,15,1,1)/324` and

```text
(Lv)_x=sum_(d in N) c_d(v_x-v_(x+d)),
H=2I-L,                  sum_d c_d=8/9.
```

The pair convention is `(u,v)=(previous,current)`. The completed
`P-DECODER-RETARDED-ENERGY-TRANSPORT-1` establishes

```text
E(u,v)=||v-u||^2/2+<u,Lv>/2,
e_x(u,v)=5(v_x-u_x)^2/18
         +sum_y c_xy[(v_y-u_x)^2+(u_y-v_x)^2]/8,
sum_x e_x=E,             e_x>=0,
E(u,v)=0 iff (u,v)=(0,0) on this finite-support carrier.
```

This is not an assertion about an arbitrary periodic box or a complex field.
The sums are finite on the active support and its one-stencil halo.

For `z in Q^4`, `s=sum_i z_i`, and `e=(1,1,1,1)^T`, use exactly the preceding
source injection

```text
S z=(z_0-s/5,z_1-s/5,z_2-s/5,z_3-s/5,-s/5)
    at (000),(110),(101),(011),(200), respectively;
B z=(0,S z);
G=I_4-e e^T/5,           m(z)=z^T G z,
2E(Bz)=m(z).
```

`G` has eigenvalue `1/5` on `span(e)` and eigenvalue `1` on `e^perp`, so it
is positive definite and `m=0` exactly at zero. The source kick is completed
before coupling is enabled. This norm-matched rational source is a disclosed
choice, not a physical source or target-independence certificate. The signed
source is not reconstructed from the sign-quotiented five QDD fields.

## 2. Cold linear port map

Fix a finite positive rational field `Gamma` on `R`, extended by zero
elsewhere; the empty field is allowed. A coupling context also carries a
positive rational threshold `q`, which is not consumed by the wave map.
Every step supplies a fresh zero incoming port, preserving the outgoing
signed tape and zero-initialized heat account. The completed
`P-DECODER-RESERVOIR-COUPLING-1` gives

```text
w_x=[(Hv)_x-(1-gamma_x/2)u_x]/(1+gamma_x/2),
T_Gamma(u,v)=(v,w),
b_x=-(w_x-u_x)/2=[2u_x-(Hv)_x]/(2+gamma_x),       x in R,
E(T_Gamma(u,v))+sum_(x in R) gamma_x b_x^2=E(u,v).   (1)
```

All denominators are positive; the successor retains finite support. Thus
`T_Gamma` and each port functional are rational linear maps on this carrier.
No claim of invertibility of the reduced cold wave map is needed. The full
wave/port map with arbitrary incoming ports has its separate inherited
reversibility theorem.

For fixed horizon `n>=0`, set `P_t(z)=T_Gamma^t Bz`. There is a unique
rational row `ell_(t,x)` for every `0<=t<n,x in R` such that
`b_(t,x)(z)=ell_(t,x) z`. The port address `(t,x)` refers to the transition
`P_t -> P_(t+1)`, starting at tick zero after preparation. It is not a physical
event ID, an independent trial or an A/U5 incidence token.

## 3. Claim A: positive partition of the source metric

Define the symmetric rational matrices

```text
M_(t,x)=2 gamma_x ell_(t,x)^T ell_(t,x),
z^T R_n z=2E(P_n(z)).                                    (2)
```

The residual is defined from the actual final wave, not by subtraction of
deposits. It exists uniquely because the final pair is linear in `z` and the
energy is quadratic. Explicitly, with the bilinear wave-energy form

```text
Q_wave = [[I,-I+L/2],[-I+L/2,I]],
2E(P)=<P,Q_wave P>,
R_n=B^T (T_Gamma^n)^T Q_wave T_Gamma^n B.
```

These transpose expressions denote finite bilinear pairings on the relevant
finite supports; no infinite matrix truncation is performed.

Every `M_(t,x)` is a nonnegative rational multiple of a row square. To see
that `R_n` is positive semidefinite independently of any conservation
identity, substitute the four source-coordinate linear maps into every
square of the displayed `e_x` and sum the finite energy halo. This is a
positive rational sum-of-squares representation of `R_n`. It establishes
positivity on the real extension of the rational source space as well.

Telescope (1) from zero through `n-1` and multiply by two. For every `z`,

```text
z^T [sum_(t<n,x in R) M_(t,x)+R_n] z=z^T G z.
```

Equality on all rational vectors determines a symmetric matrix: diagonal
entries follow from basis vectors and off-diagonal entries from their pair
sums. Therefore

```text
sum_(t<n,x in R) M_(t,x)+R_n=G.                           (3)
```

At `n=0`, there are no port slots and `R_0=G`. With no ports, the wave evolves
freely and the same residual identity holds at every finite horizon.

For a longer horizon the earlier port rows/matrices are unchanged. In
particular

```text
R_n=R_(n+1)+sum_(x in R) M_(n,x).
```

This is a positive-order decrease, not a claim of a zero limit. No complete
absorption or finite detection time is inferred.

### Grouping, normalized shares and exact operator spelling

Partition all finite port slots into preselected disjoint groups and sum
their matrices. Keep `R_n` as one separately labelled residual group. Empty
groups are harmless zero matrices. The grouped forms `A_j`, including the
residual, remain positive semidefinite and sum to `G`.

For `z!=0`,

```text
w_j(z)=z^T A_j z/m(z),       w_j>=0,       sum_j w_j=1.     (4)
```

On a deposit group this is accumulated heat divided by initial wave energy;
on the residual it is remaining wave energy divided by initial wave energy.
The value is unchanged by a nonzero rational scaling of `z`. At zero source
there is no normalized share: an explicit zero-denominator disposition is
required. Zero wave and heat histories themselves remain well defined.

The inverse metric is rational, `G^(-1)=I_4+e e^T`. Put

```text
F_j=G^(-1)A_j,             rho_z=z z^T G/m(z).
```

Then `G F_j=A_j=F_j^T G`, positivity means
`v^T G F_j v=v^T A_j v>=0`, `sum_j F_j=I`, and

```text
tr(rho_z F_j)=tr(z z^T A_j)/m=z^T A_j z/m=w_j.
```

Similarly `rho_z` is self-adjoint and positive in the `G` metric and has
trace one. Ordinary Euclidean symmetry of these coordinate matrices is not
asserted. This is a real rational algebraic representation; it provides no
physical effect, instrument, outcome, complex phase or polarization carrier.

Dropping the residual and renormalizing is a different conditional statistic.
Changing Gamma, grouping or horizon as a function of the outcome is outside
the fixed-family claim. Warm external ports require a different source and
energy budget; (3) is not asserted unchanged for them.

## 4. Claim B: obstruction to sharp QDD postprocessing

The comparison targets in the same source coordinates are

```text
L_QDD=e e^T/20,             H_QDD=I_4-e e^T/4,
L_QDD+H_QDD=G.
```

Their `G`-operator representatives are complementary projectors onto
`span(e)` and `e^perp`. This probe compares already chosen dynamics with
these targets; it does not use them to design a coupling.

For a fixed context and finite horizon, admit exactly the complete
state-independent nonnegative two-output postprocessing family

```text
0<=a_j<=1 for each fine slot and the residual,
A_LOW=sum_j a_j A_j,         A_HIGH=sum_j (1-a_j) A_j.     (5)
```

Coefficients may be real and depend on the fixed context/horizon, but not
on the source or output target. No outcome is omitted. Deterministic
coarse-graining is the subfamily with `a_j` zero or one. Pre-grouping fine
slots only restricts them to equal coefficients and is already covered.

### General positive-processing lemma

Suppose one fine positive form `A_k` has strictly positive values on a
vector `z_H` with `z_H^T L_QDD z_H=0` and on a vector `z_L` with
`z_L^T H_QDD z_L=0`. Exact agreement `A_LOW=L_QDD` would imply

```text
0=sum_j a_j z_H^T A_j z_H,
```

forcing `a_k=0` because every summand is nonnegative. Agreement with HIGH
on `z_L` forces `1-a_k=0`, a contradiction. The same proof only needs
agreement on these two sources; it need not assume equality throughout a
continuous source domain. Additional positive effects and the residual
cannot cancel a positive summand.

### First origin slot for every positive origin conductance

Assume the origin is a port, `gamma_0>0`, and `n>=1`. At the first step the
prepared previous slice is zero. Only the origin conductance enters its
successor. The source sites and stencil give

```text
(HSz)_0=(10/9)(z_0-s/5)
         +(1/54) sum_(i=1)^3(z_i-s/5)-s/1620
       =h z,             h=(1421,-349,-349,-349)/1620.
ell_(0,0)=-h/(2+gamma_0),
M_(0,0)=[2 gamma_0/(2+gamma_0)^2] h^T h.                  (6)
```

The coefficient is strictly positive for every admitted origin conductance.
For the two balanced source vectors

```text
z_H=(1,-1,0,0):          L_QDD[z_H]=0,       h z_H=59/54;
z_L=(1,1,1,1):           H_QDD[z_L]=0,       h z_L=187/810,
```

both slot values are positive. The lemma applies. Thus, for every such
context and every finite `n>=1`, **no member of (5) agrees with both sharp
QDD target weights on these sources, and hence none agrees on all `Q^4`**.
In the control `gamma_0=2`, `M_(0,0)=h^T h/4`.

The result is about this complete declared postprocessing family after this
chosen source and coupling. It is not a theorem excluding physical
apparatuses, nonlinear/source-dependent rules, coherent amplitude mixing,
altered interactions, discarded outcomes with renormalization, or differently
typed measurements. No physical Born falsifier or apparatus-family closure
follows. A zero-origin-conductance context and `n=0` are outside the claimed
origin-slot obstruction, not positive realizations by default.

## 5. Threshold boundary and status discipline

The inherited detector convention is `N_x=floor(H_x/q)` with remainder
`0<=H_x-qN_x<q`. Since `H_x=z^T(sum_t M_(t,x))z/2`, scaling the source by
lambda scales heat by `lambda^2` while (4) is invariant. Floors generally
change and are not the quadratic shares. This is an audit boundary, not
an additional occurrence claim. The code uses an exact nonzero deposit and
predeclared rational thresholds to witness the difference; no measured
frequency or fitted parameter is used.

All conclusions are conditional L1 mathematics. The finite audit checks
independent propagation, energy polarization, exact principal minors,
prefix/grouping, metric/trace identities, witness arithmetic and stated
zero/threshold boundaries. Its finite horizons do not replace the uniform
proof. Failed scientific gates are preserved under the frozen disposition.

Physical source/coupling/record identification, the #539 profile, QDD
terminality, whole physical apparatus-family completeness, ordered occurrence,
L1-to-L5 realization and L6 measure remain unresolved. The signed tape may
reconstruct a source mathematically; recomputing the QDD target from it is
not a physical LOW/HIGH effect identification. COINCIDENCE-RECORD-FREQUENCY
remains candidate-H / UNTESTED / STOP. The photon #744 and #756 boundaries
and production prohibition #742 are unchanged. Registration, if earned,
requires a separate Canon fold.
