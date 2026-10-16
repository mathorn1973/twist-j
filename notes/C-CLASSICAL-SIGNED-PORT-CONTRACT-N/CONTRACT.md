# Frozen classical signed-port response and energy contract

**NON-CANONICAL / L1 mathematical design contract / 2026-10-13.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1484](https://github.com/mathorn1973/twist-j/issues/1484).
Identifier: C-CLASSICAL-SIGNED-PORT-CONTRACT-N.
Authority basis: Public Canon v101, public main
5f54015ed8361e3a64cb10894397020ddfadd104.

This is one selected classical decoder leg, with a frozen complete mathematical
interface and a prospective physical qualification gate. It supplies no device,
calibration certificate or independently admitted physical source. Four successor
lanes must preserve these definitions. The mathematical and engineering choices
are disclosed choices, not a derivation of a unique physical dictionary.

## 1. Types, equality and fixed horizon

The source is z=(z0,z1,z2,z3) in Q^4, with operational preparations
Z_op={z: max_i|z_i|<=1}. Zero is allowed. Structural identities use all Q^4.
Equality is literal signed coordinate equality, without normalization,
global-sign quotient, phase fit or target-dependent rescaling.

Use D3={x in Z^3: sum(x) is even}. The complete symmetric stencil is
B={d in D3: |d|^2 in {2,4,8,10,16}}, with respective weights
(6,1,15,1,1) and c_d=weight(|d|^2)/324.
Its full diagonal is sum c_d=8/9. Let B_zero=B union {0}. Mark, in this order,

    y0=(0,0,0), y1=(1,1,0), y2=(1,0,1), y3=(0,1,1), y4=(2,0,0),
    Y={y0,y1,y2,y3,y4}, R=(y0,y1,y2,y3), H_run=2,
    D=Y+B_zero+B_zero.

The finite wave carrier is Q^D x Q^D, in previous/current order (u,v).
D is ordered lexicographically. P:Q^4->Q^D inserts the four marked port
values in the displayed R order. All fields are extended by zero outside D.
Use the principal Dirichlet operator

    L_D=P_D L P_D^T,  (Lf)(x)=sum_(d in B)c_d[f(x)-f(x+d)].

Its diagonal remains 8/9 at every boundary site. An induced-subgraph Laplacian,
periodic wrapping and dropping boundary edge energy are different contracts.
The chosen D supplies the two-cut causal buffer for the initial support Y
and forcing on R. Exact agreement with the infinite model is asserted only
through this frozen operational horizon, to be proved by the successor.

## 2. Preparation, admissible controls and cold operation

Let s=sum_i z_i and

    S(z)=sum_(i=0)^3(z_i-s/5)delta_yi -(s/5)delta_y4,
    (u0,v0)=(0,S(z)),  G_source=I-11^T/5,
    E_D(u0,v0)=z^T G_source z/2.

S is the existing selected five-site rational source, not an encoding from a
native F5 checkpoint or an asserted physical preparation. Source independence
of the ready context is part of the preparation contract.

Fix all four conductances to g_j=2; Gamma=2 on R and 0 elsewhere.
They do not depend on z, observed output, desired gain or a Born target.
The operational incoming tape has two entries a0=a1=0 in Q^4, prepared once.
Do not refresh, reconstruct, normalize or reset the wave or any tape between
the two cuts. Both signed outgoing vectors are retained.

The complete coupling domain also permits arbitrary incoming a in Q^4,
arbitrary wave pairs and occupied outgoing-tape values. A warm incoming field
is an explicit mathematical control case, not silently part of the cold test.
No extra source-sensitive gate or contact is admitted by this contract.

## 3. Exact transition and signed observable

Write C=P diag(g)P^T, D_g=I+C/2, H_D=2I-L_D. For one cut,

    w=D_g^-1[H_D v-(I-C/2)u+2P diag(g)a],
    p=P^T(w-u)/2,
    b=a-p,
    Couple((u,v),a)=((v,w),b).

D_g is diagonal and positive. These equations define the entire state,
including the residual wave and all four output signs. The observable at
cut t is y_t=b_t, in the marked R order. The delivered record is
Y_2=(b0,b1); the full post-state is retained separately. Squared deposits
alone are not this observation. Neither a click, exactly one outcome nor
a probability is selected.

The inverse obligation is the displayed complete-coupler inverse:

    u=D_g^-1[H_D v-(I-C/2)w+2P diag(g)b],
    a=b+P^T(w-u)/2.

The observation family must prove this inverse and the prepared-prefix
claim on their stated domains, not infer them from a few test trajectories.

## 4. Energy and complete occupied-tape carrier

Use the inherited positive pair energy of the finite zero extension,

    E_D(u,v)=(||v-u||^2 + u^T L_D v)/2.

The exact per-cut ledger is

    E_D(v,w)+sum_j g_j b_j^2
      =E_D(u,v)+sum_j g_j a_j^2.

All four ports belong in this sum. Cold operation gives nonnegative
outgoing deposit g_j b_j^2, but its sign has to remain in the stored b_j.

For a concrete complete finite-horizon memory target, let
A=(A0,A1), B_tape=(B0,B1) be arbitrary Q^4-valued two-slot tapes and let
k in Z/2Z be the control pointer. One total transition is specified by

    ((u,v),A0) -> ((v,w),b) through Couple,
    A'=(A1,B1),
    B_tape'=(b,B0),
    k'=k+1 mod2.

The full inverse and the complete energy invariant are proof obligations
of lane R. The declared invariant is

    E_full=E_D(u,v)+sum_(h=0,1)sum_j g_j(Ah_j^2+Bh_j^2).

Operational readiness is A=(0,0), B_tape=(0,0), k=0. The occupied-memory
continuation analysis must also cover arbitrary B_tape at readiness and
all A/B values on the full carrier. Cold behavior is promised only for
the first two controlled steps from the ready A. The returning tape after
two steps is not a fresh cold reservoir, and k wrapping is not renewal.

No tape item, sign, old record or driver is discarded. Physical realization
of the pointer/memory, their preparation and their energy remain independent
obligations; assigning a mathematical pointer zero energy is not a physical
zero-cost statement. A new trial requires an explicit preparation/reset
operation with its own boundary account.

## 5. Clock and other interfaces are typed separately

The classical port requires a cut index t=0,1 and external stop at H_run=2.
Its rational law does not require a Thue-Morse bit. The finite pointer above
does not establish an autonomous physical clock or SI duration.

Lane P additionally studies the existing prescribed native evaluator as a
separate time-only sidecar: native x in F5^6, time n in N0 and the five labels
kappa(n) from the immutable five-context proof. Freeze this sidecar input as
the supplied forward-window interface:

    W_n=(theta_n,theta_(n+1),theta_(n+2),theta_(n+3)),
    beta_n=theta_(n+4),  theta_m=popcount(m) mod2.

The provider initializes W_n at the declared starting n and supplies beta_n.
The source z and native payload x are inaccessible to this provider. A
four-bit driven buffer can update W by shifting; neither the provider nor
its physical acquisition is constructed by declaring the interface.
The checkpoint evaluator receives only its time label, not hidden n.
Any T1 raw-(q,r) reader remains a different, explicitly current-bit interface.

There is no admitted Enc_native:F5^6->Q^4, common timing equation between
n and t, or contact realizing the missing native T. These are open bridge
fields, not implicit consequences of the same word "port" or the number five.

Lane B's seven-mode DP5 endpoints are another separate type. They certify
the old compensated sine-versus-linear model only. Their energy, Hilbert
state, clock and ion parameters are not identified with E_D, z or this
classical port. The numerical data are result-exposed and preserved.

## 6. Prospective physical dictionary and full boundary

Choose positive conversion parameters A0_length,tau_step,E_star, with units
m,s,J, respectively. They are independently calibrated apparatus settings,
not new universal constants or values extracted from the tested law.

    V0=A0_length/tau_step, F0=E_star/A0_length,
    Z0=E_star*tau_step/A0_length^2, Z_j=g_j Z0,
    V_j=V0 p_j, F_j=F0 g_j(a_j+b_j),
    v_plus_j=V0 a_j, v_minus_j=V0 b_j.

One common marked positive direction fixes all signs. The selected map gives
tau_step sum_j F_j V_j=E_star sum_j g_j(a_j^2-b_j^2).
This is a dimensional identity under the map. Equality to an independently
measured continuous work integral requires a declared sample/bin/transfer
rule and its uncertainty. No force-motion instrument is supplied.

The physical instance boundary must include wave, both tapes/reservoirs,
source preparation, clock/control, sensors and loading, retained records,
loss ports and reset. Its measured ledger has the form

    Delta E_wave + Delta E_tapes + Delta E_control
      +Delta E_sensors +Delta E_records/reset
       = W_external + Q_external.

Specify the observation interval and signs of every term before validation.
Preparation/reset outside the two-cut window are separately accounted.
Unmeasured loss, control or memory terms cannot be replaced by zero.
Do not count a retained outgoing tape's energy again as an external flux.
No Shannon distribution, entropy or Landauer price is supplied.

## 7. Fixed calibration split and acceptance rule

Stage S owns independent sensor/reference polarity, gain, bandwidth, loading,
joint uncertainty, source preparation, clock/bin assignment and all conversion
parameters. Stage I may identify the chosen apparatus on the fixed source set

    Z_I={0} union{+e_i,-e_i:0<=i<4}  (9 preparations).

Stage V is held out and fixed now:

    Z_V={sigma e_i+rho e_j:0<=i<j<4, sigma,rho in{-1,+1}}
    (24 preparations, both cuts, all four signed outputs).

No source from V is used to choose or fit the carrier, conductance, sign,
phase, delay or interpretation. S/I may not derive a reference from the same
equation that V is testing. Freeze preprocessing and joint error bounds
before opening any V output. Existing archives are not qualified by default.

Mathematical identities have tolerance 0. For a later qualified physical
instance, select the engineering allowances eps_y=eps_E=1/10000 in the
normalized amplitude and E_star energy units. These are new declared design
targets, unrelated to DP5's 1/1000 and not physical constants. Measured response
residuals and the full energy residual must have sound joint intervals:

- PASS only if every required residual interval is contained in [-eps,+eps].
- FAIL if at least one required interval is disjoint from [-eps,+eps].
- Otherwise UNRESOLVED.
- Missing source/sensor/clock/boundary qualification gives NOT_READY before V;
  it is not a physical falsification.

Exact signed model predictions, identification, full energy accounting and
the physical uncertainty gate are separate deliverables. This contract
does not assert that an actual instance can reach these allowances.
A qualified physical PASS covers exactly the 24 preparations in Z_V and
the two declared cuts. It does not establish a uniform physical bound on
all Z_op; that requires a separate transfer certificate.

## 8. Four successors, permitted work and falsifiers

| Lane | Deliverable after this contract's immutable public pin |
|---|---|
| P | Total supplied-window update/readout, five-label decoder interface, readiness/latency and source-independence proof; explicit acquisition and composition gaps |
| O | Signed two-cut response maps, source identifiability, negative sign/square controls and complete S/I/V qualification/uncertainty protocol |
| R | Total occupied-tape inverse, conserved E_full, ready two-cut prefix and exact finite-horizon/reset limitations |
| B | Independently specified endpoint-restoration certifier for the closed DP5 output, its bounds, serialized-input custody, finite resource limits and pre-execution obligations |

For this dispatch, work is analytical proof/design and source review only.
No mathematical script, numerical propagator, scientific verifier, data
acquisition or hardware experiment is run under this note. Repository
policy/unit/Canon/ledger checks are permitted. A later computational gate
requires its own identifier, complete accepted code, preregistration and
public pre-execution pin/readback.

A mathematical counterexample is any admitted input violating a required
identity, inverse, causal-prefix equality, signed decoder or energy balance.
A physical result is judged only after qualification under Section 7.
Changing a map, source domain, cutoff, phase convention, threshold or boundary
after results is a new contract. None of the predecessor source pins changes.

Physical source/contact admission, occurrence, sampling, SI ownership and
L2-L6 bridges stay open. No Canon, owner status, registry, workflow, sealed
probe or release changes. No ion experiment or new long simulation.
