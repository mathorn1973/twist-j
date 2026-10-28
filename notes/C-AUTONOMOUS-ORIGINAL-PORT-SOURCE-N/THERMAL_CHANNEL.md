# Thermal launch, two output windows and exact finite return

**NON-CANONICAL, L1. Conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.

This is a channel and readiness theorem for the complete local apparatus
specified by the companion geometry and energy accounts. Its exact gates,
finite ladder sites and couplings are conditional implementation inputs.
No scientific executable, expanded circuit or physical experiment has been
run. Review within this authoring session is not independent acceptance.

The source identities are those of the active-source supplement to
[#1775](https://github.com/mathorn1973/twist-j/issues/1775#issuecomment-6399173427).
The complete preparation word and its occupation realization are specified
in [SOURCE_CIRCUIT](../C-ORIGINAL-PORT-SOURCE-PREPARATION-N/SOURCE_CIRCUIT.md)
and [LOCAL_REALIZATION](../C-ORIGINAL-PORT-SOURCE-PREPARATION-N/LOCAL_REALIZATION.md).
This note supplies a different autonomous thermal implementation of those
conditional endpoint operations. It does not modify their frozen text.

## 1. Input information and the two target channels

Let C be a retained, zero-energy setting qubit. The information input is
an arbitrary joint state on C, the original receiver memory and a passive
reference R. The receiver is encoded by thirteen occupation coordinates
at the original physical position 100. Its code has dimension 26 and
constant occupation energy 2 epsilon. These thirteen coordinates are one
joint information block, not thirteen independent thermal ready states.

The preparation endpoint is valid on all 26 receiver states. The later
receiver-only indication and contrast require the admitted old-memory
subspace

```text
K_mem=span(d1,...,d25),       P_W=|d0><d0|.             (T1)
```

The source basis seed u2 has R=97, r=0 and token coordinate 97. In the
actual occupation representation its four nonzero coordinates, all at
97, are h2=-1, h3=-1, h5=+1 and h12=-1. Their total occupation energy is
8 epsilon. All other source occupation coordinates are zero. The phase
of the fixed intertwiner I_0=Emb Gamma^(-1) D_2* is included in the
preparation word; it is not removed separately from a controlled call.

Write the normalized source targets as

```text
chi_s=alpha_(97,0),    d_s=(U^2-U^(-2))chi_s,
<chi_s,d_s>=0,
Z=(39521+154 sqrt(5))/15625,
psi_+=(chi_s+d_s)/sqrt(Z),
psi_-=(chi_s-d_s)/sqrt(Z).                            (T2)
```

The ideal source-preparation isometry retains the setting and acts as

```text
|0>_C |xi>_(mem,R) -> |0>_C |psi_+>_S |xi>_(mem,R),
|1>_C |xi>_(mem,R) -> |1>_C |psi_->_S |xi>_(mem,R).    (T3)
```

It includes the counted setting phase correction, so (T3), including its
off-diagonal setting blocks, is the declared convention. Linearity gives
the channel P_src on every admitted mixed or reference-correlated input.
Endpoint restoration of the old memory does not assert absence of its
intermediate interactions. Let

```text
P_fin=Ad_(U_rec^3) o P_src,                           (T4)
```

with identities on C and R. The finite occupation implementation agrees
with the original law on all prefixes used for (T3)-(T4). This is an
admitted-input finite-propagation statement, not equality of the finite
and infinite operators on arbitrary raw inputs.

The first excursion cools the helpers, executes the source-preparation
word, returns the payload to its original physical row, then raises a
physical flag A. The second executes three complete original steps,
returns the payload to that same row, then raises a separate flag B_f.
The integer B below is a clock length parameter; B_f always denotes the
physical second flag. Future payload rows are transport space, not
additional supplied pure source copies.

## 2. A complete two-temperature input inventory

Fix epsilon>0 and an integer k>=8. Put

```text
n=2208,                 M=2209,
r=2(k+ceil(log2 M)+1),
G_cool=M(2r^2-r),        G_star=512 n^4 4^n,
P1=G_cool+G_star,        P2=3G_star,     P=P1+P2,
S=7726+2Mr.                                             (T5)
```

One payload row has 1102 four-level occupation sites, 2210 zero-energy
qubits, 4414 ladder sites, and 2Mr donor qubits. Thus its physical site
count is S. The 2210 zero-energy qubits are the M helpers and C. Each
occupation site has levels h=0,+1,-1,2 with energies
0,2 epsilon,2 epsilon,8 epsilon. Each ladder has levels 0,...,26468
with energy epsilon times the level. The initial active ladder will be
loaded to b0=17632 by the launch, rather than supplied in that state.

There are P+1 physical payload rows. Initially only the original row's
thirteen receiver coordinates and its C carry admitted information. The
M helpers start in I/2. All other zero-energy sites, including C copies
in future rows, start in their zero-energy Gibbs states I/2. The row
transport and return are exact SWAP circuits on arbitrary future-row
contents; the endpoint theorem does not require pure transport junk.

There are Mr hot donors in the original row, Mr cold donors there, and
2Mr cold donors in each future row. BOTH donor types have the same gap

```text
G=17643 epsilon.                                      (T6)
```

The launch fuel is one further hot qubit with this gap. All hot factors
are independent Gibbs states at the single temperature specified by

```text
beta_h G=ln 2,       p_h=1/3.                          (T7)
```

Every charged site outside the information block and hot factors starts
in its independent Gibbs state at beta_c. This includes the four source
seed coordinates, every ladder, every future-row donor and occupation
site, both flags and all physical clock sites. No outer pure clock, pure
source or sharp excited battery is supplied.

The colored-clock layout has r1+r2 qutrit sites and
K-2(r1+r2) qubit sites. Every nonvacuum color has gap at least epsilon;
there is exactly one vacuum per physical clock site. Hence

```text
sum_clock_sites (dimension-1)=K.                       (T8)
```

The physical number of clock sites is K-(r1+r2). A qutrit contributes
two possible thermal excitation colors to the estimate below, not two
independent qubits. The complete physical site count is
S(P+1)+K-(r1+r2)+3, where the final three are the fuel and two flags.
All donors and transport registers remain physical subsystems.

Let x=exp(-beta_c epsilon), and require x<=1/2. For one occupation site,
one ladder and one ordinary cold qubit respectively,

```text
Pr(h!=0)=(2x^2+x^8)/(1+2x^2+x^8)<=3x^2,
Pr(ladder!=0)<=x/(1-x)<=2x,
Pr(qubit excited)<=x.                                (T9)
```

For a clock site of dimension d, its total excitation probability is at
most (d-1)x. The counts entering the cold comparison are exactly

```text
N_h=1089+1102P,
N_l=4414(P+1),
N_cq=Mr(1+2P)+2,
C_eff=3N_h+2N_l+Mr(1+2P)+K+2.                        (T10)
```

N_cq counts cold donor qubits and flags. The clock colors contribute K
separately. The thirteen information coordinates are excluded from N_h.
Set the one common cold temperature by

```text
beta_c epsilon=(k+1+ceil(log2 C_eff)) ln 2.             (T11)
```

Let rho_th be the actual input and rho_0 the mathematical comparison
obtained by replacing every charged cold factor by its ground state.
Hot donors, fuel, zero-energy Gibbs factors and all information are left
unchanged. Because the cold factors are a diagonal independent product,
rho_th=q_c rho_0+(1-q_c)rho_bad for some normalized rho_bad. Thus

```text
eta=1-q_c=D(rho_th,rho_0)
   <=3N_h x^2+(2N_l+N_cq+K)x
   <=C_eff x<=2^(-k-1).                              (T12)
```

This decomposition is used to bound errors. No physical selection,
discarding or cooling to an exact zero-temperature state is performed.
In particular rho_bad contains multiple clock excitations and every
unfavorable thermal source, battery, donor and flag configuration.

## 3. Direct launch and retained thermal reset branches

On rho_0 the source coordinates and all ladders are in vacuum. The launch
couples the following two local basis configurations, acting as identity
on the old memory, setting, reference and all other sites:

```text
fuel1, four source h=0, ladder0, first cursor vacuum
  <->
fuel0, four source h=u2, ladder17632, first cursor charge3.
                                                               (T13)
```

The energy on either side is 17643 epsilon, excluding the common
2 epsilon of the old-memory code. This is a seven-site matrix element:
one fuel, four occupation sites, one ladder and one cursor site. It uses
a declared 26469-level ladder site and is not an adjacent-rung or
all-qubit launch claim. The clock construction supplies its full positive
partial-isometry term, including both diagonal projectors and its
complementary sectors.

For rho_0 the fuel-ground component, of weight 2/3, has no cursor, no
source excitation and no raised flag. It is dormant. The fuel-excited
component, of weight 1/3, generates one complete computational history.
No later programmed gate touches the fuel. At every history node after
the launch it is ground. Reverse launch requires the first cursor and
the fully restored launch output, so a second independent forward run
cannot start from that history. This does not prohibit coherent
backtracking or the finite return proved below.

For each zero-energy helper use r fresh donor pairs. The reset exchanges

```text
|1,0,1>_(hot,cold,helper) <-> |0,1,0>,                 (T14)
```

and is identity on the six other basis states. Equal donor gaps G make
this a complete energy-conserving unitary, including every counterbranch.
The two donor rails are fetched and returned as in the predecessor local
construction, costing 2r^2-r operations per helper. No donor is reused
for another reset. On the all-cold comparison the fresh cold donor is
zero, and tracing a fresh pair gives the exact helper/reference channel

```text
Phi=(2/3) id+(1/3) R_0,
Phi^r=(2/3)^r id+[1-(2/3)^r]R_0.                      (T15)
```

Here R_0 replaces the helper by zero and leaves the reference marginal.
The helper/donor input is actually a product of diagonal Gibbs states,
independent of C, old memory and R. Cooling is a permutation circuit on
this block. Its entire output, including every spent donor, is therefore
classical. If tau is that output and tau_D its actual donor marginal,

```text
D(tau, |0^M><0^M| tensor tau_D)
 =Pr(at least one helper is nonzero)
 <=xi:=M(2/3)^r<2^(-k-1).                             (T16)
```

The equality follows by resolving tau into its helper-zero and
helper-nonzero classical blocks. The mass removed from the zero block
and the total mass of the other blocks are both the bad probability.
The last inequality follows from (2/3)^2<1/2 and (T5). This is a linear
full donor-inclusive comparison because its input and permutation
structure are explicitly classical. Diagonal marginals alone or arbitrary
helper/reference correlations would not justify it.

The donor marginal in (T16) is changed and can be correlated with the
helpers. It is not the initial Gibbs product. After cooling, donors take
part only in reversible payload transport; no logical source gate uses
them. Contractivity under the subsequent complete unitary transports
propagates xi to the source, setting, old memory and reference at each
completed endpoint. The actual donors remain retained. Thermal cold
donor defects are already included in eta in (T12), so no second cold
reset error is added to xi.

## 4. The autonomous history and its exact clock distribution

Take the geometry's route lengths r1,r2 and outer row extent Y0, and fix

```text
B>=max(r1+1,r2+1,8192,32(k+3),4Y0+4),    K=12B.        (T17)
```

Identity padding places the source endpoint and A-raising edge at node
2B, the start of the second excursion at node 4B,
and the returned final endpoint and B_f-raising edge at node 6B. Between
nodes 2B and 4B-1 the source at its original physical location is held
fixed. At nodes 6B,...,K the completed output there is held fixed.

The cursor has charge 3 epsilon before A is raised, 2 epsilon between
the two flag-raising edges, and epsilon afterwards. Each flag has gap
epsilon. The corresponding edge lowers cursor charge by epsilon and
raises that flag. With the launch and all funded program gates, every
term commutes with the declared bare sum H0. The full law is
H=H0+H_prop, with a positive H_prop on the full raw Hilbert space.
Full-raw positivity and bounded geometric support belong to the
companion construction, not just to the following invariant sector.

For every admitted initial information state and every diagonal hot/helper
configuration in rho_0, the active sector is the same weighted path
0,...,K after conjugation by its complete prefix unitaries. Its restriction
is

```text
H_prop|history = g I - sum_(j=0)^(K-1)
                  a_j (|j+1><j|+|j><j+1|),
a_j=g sqrt((j+1)(K-j))/(K+1),    g>0.                  (T18)
```

The same statement includes cooling failures and dirty zero-energy
helpers: their later data word is different, but every gate is still a
unitary and the clock path is unchanged. No successful-reset subspace is
silently selected to obtain (T18).

Fix g before the circuit size and error parameter are used for padding.
The initial rho_0 and rho_th commute with H0: all hardware inputs are
diagonal Gibbs states, C has zero energy, and the old-memory information
code has constant energy. Since [H0,H_prop]=0, the bare free factor
cancels on their densities. On the ACTIVE COMPARISON branch of rho_0,
the path probabilities, including all reference correlations, are exactly

```text
Pr(J_t=j)=binom(K,j) p(t)^j [1-p(t)]^(K-j),
p(t)=sin^2(theta(t)),  theta(t)=g t/[hbar(K+1)],
T_h=pi hbar(K+1)/(3g).                                (T19)
```

This is the binomial transition law for the spin-K/2 matrix (T18),
started at node zero. Distinct virtual nodes are orthogonal cursor
states even when two colors share one physical qutrit. Tracing the
clock therefore gives the corresponding mixture of prefix channels.
The path law is independent of the unknown memory and setting input.
It is not asserted for the cold-defect component of rho_th.

## 5. Source-ready window with a physical first flag

Define

```text
I_src={t: 11/48<=p(t)<=13/48, 0<t<3T_h/2},
beta=exp(-3B/32)<2^(-k-3).                            (T20)
```

Equivalently the endpoints are
3T_h arcsin(sqrt(11/48))/pi and
3T_h arcsin(sqrt(13/48))/pi. This is a positive-width, predetermined
window, not a time selected after observing a favorable trajectory.

For t in I_src, Kp lies between 11B/4 and 13B/4. Its distance from each
edge of [2B,4B) is at least 3B/4. Hoeffding's binomial bound gives

```text
Pr(J_t<2B)<=beta,        Pr(J_t>=4B)<=beta.
w_A(t):=Pr(J_t>=2B)>=1-beta.                          (T21)
```

On rho_0 the probability of the physical event A=1 is exactly w_A/3.
Conditional on A=1, at most beta/w_A of that history weight has entered
the second program; all other admitted nodes hold the same source
endpoint on the original physical sites. Therefore, after tracing the
clock and unused hardware, the actual conditional source, setting,
old-memory and reference state satisfies

```text
p_A(t)>=w_A(t)/3-eta,
D(rho_actual|A=1, P_src(rho_info))
 <=xi+beta/w_A(t)+3eta/w_A(t)
 <=xi+beta/(1-beta)+3eta/(1-beta).                    (T22)
```

The eta term is a complete-instrument normalization bound. If normalized
states differ by at most eta before a success/failure instrument and the
comparison success probability is p0, their success-normalized states
differ by at most eta/p0 whenever eta<p0. Indeed the instrument bounds
the complete success/failure substates sigma_success, tau_success by
(||sigma_success-tau_success||_1+|p-p0|)/2<=eta, where p and p0 are
their success probabilities. The triangle inequality after normalization
then gives eta/p0. Here p0=w_A/3, not unity.

Flag A remains raised later. It is only an approximate source-ready
certificate in the prescribed window (T20), with the stated leakage.
It does not certify that the second program has never begun at arbitrary
later times. Without conditioning, the dormant source-vacuum component
has weight 2/3 in rho_0. It is orthogonal to the occupied source target,
so the unconditional source is not within the small error of (T22).

## 6. Completed output, setting contrast and measurement scope

For every t in the final interval [T_h,2T_h], p(t)>=3/4. The comparison
probability of the physical final flag B_f=1 is w(t)/3, where

```text
w(t)=Pr(J_t>=6B)
 >=1-(3/4)^(6B)>1-beta.                              (T23)
```

For example, exponential Markov with 3^(-J_t) gives
Pr(J_t<K/2)<=[sqrt(3)(1-p+p/3)]^K<=(3/4)^(K/2).
Every flagged node is a completed endpoint. Hence

```text
p_B(t)>=w(t)/3-eta,
delta_fin(t):=D(rho_actual|B_f=1, P_fin(rho_info))
 <=xi+3eta/w(t).                                     (T24)
```

The reduced comparison contains the actual original source, receiver,
retained C and reference, not a zero-energy substitute archive. The
physical query for the final receiver result is the joint instrument
with projectors B_f P_W, B_f(I-P_W), and I-B_f. All three outcomes remain
part of its complete state. A conditional state is not a supplied
detector, occurrence rule or permanently stored event.

Let z=2^(-k-1). Equations (T12), (T16), (T20), and k>=8 imply uniformly
on their respective windows

```text
p_A>1/4,       p_B>1/4,
delta_src<6z,  delta_fin<6z.                          (T25)
```

Here delta_src denotes the left-hand trace distance in (T22). The bounds
use beta<z/4 and w_A,w>1-z/4; they do not set any unsuccessful thermal
or cooling branch to zero. Choosing k=40 gives both errors below
6*2^(-41), in particular below 1/1000.

For the two separate admitted setting inputs C=0 and C=1, with arbitrary
old-memory/reference states in (T1), let p_actual,+ and p_actual,- be the
receiver probabilities conditional on B_f=1 in the final window. The
source supplement gives Delta_p=p_+-p_->1/50. Consequently

```text
p_actual,+ - p_actual,-
 >=Delta_p-delta_fin,+-delta_fin,-
 >1/50-12z >1/100                  (k=40).            (T26)
```

The unconditioned physical event B_f P_W also retains contrast between
these two separately supplied settings. Its probabilities obey

```text
Pr_+(B_f P_W)-Pr_-(B_f P_W)
 >=(w/3)Delta_p-2(w xi/3+eta).                        (T27)
```

An alternative all-Gibbs setting variant takes the ORIGINAL C initially
in I/2, independent of the old memory/reference. It retains C physically
and compares the two settings by a final joint query. The conditional-B_f
state in (T24) is within delta_fin of an ideal state with each C value of
probability 1/2. Thus the actual conditional probability of either setting
is at least 1/2-delta_fin. Conditioning a second time on C=s costs a
further normalization: each receiver conditional error is at most
2delta_fin. Its observed setting-conditioned contrast therefore obeys

```text
Pr(P_W|B_f=1,C=0)-Pr(P_W|B_f=1,C=1)
 >=Delta_p-4delta_fin >1/50-24z>1/100  (k=40).         (T28)
```

Equation (T28) is an analysis of one retained random setting, not a
claim to a freely chosen setting from a thermal bit. For arbitrary
coherent supplied settings the stronger joint channel comparison
(T24) applies, but probabilities of arbitrarily rare selected C branches
need their own success denominators. Tracing C is not coherent erasure.

The source and final windows are TWO SEPARATE CUTS of the unmeasured
autonomous evolution. An actual intermediate measurement of A generally
changes the clock state. Equations (T23)-(T28) have not been proved for
the evolution conditioned on such an earlier physical measurement.
They must not be concatenated as a sequential measured experiment.

## 7. Exact recurrence, consumed resources and physical scope

At t=3T_h, theta=pi. The weighted path in (T18) returns every active
input vector to its node-zero vector up to one common phase. K=12B is
even. The initially diagonal fuel mixture has no active/dormant cross
terms, and the initial state commutes with H0. Consequently the ENTIRE
comparison density returns exactly:

```text
exp(-iH 3T_h/hbar) rho_0 exp(iH 3T_h/hbar)=rho_0,
Pr_actual(A=1 at 3T_h)<=eta,
Pr_actual(B_f=1 at 3T_h)<=eta.                         (T29)
```

This includes the helper/reset failures, all used donors and arbitrary
memory/reference correlations; it does not require dropping their
branches. In particular the useful source and receiver outputs are
unwritten during the return. The thermal helpers and random setting
return to their original mixed states, not to pure ready states.

During either useful window the donor states are spent resources. The
apparatus has finite amounts of hot and cold material, finite transport
space, a fuel qubit and two physical flags. Exporting a record, measuring
a flag, replacing donors or changing a coupling modifies the complete
evolution, so the free-return identity cannot simultaneously serve as a
proof of exact reset after one of those interventions. No indefinite
storage, autonomous stopping or closed repeated use is established.

The initial product is stationary under the declared bare sum H0 but
not generally under H0+H_prop; the hot/cold launch populations supply
the explicit initial nonstationarity accounted for in ENERGY_ACCOUNT.
The full Hamiltonian is time independent. Fixing g before choosing k
and the route lengths means that improved accuracy increases the
counted resources and T_h. It is not paid for by an increasing clock
coupling.

The conserved energy here is the newly declared occupation, ladder,
donor, fuel, flag and clock sum, together with its complete interaction
Hamiltonian. It is not identified with the original spectral
Q=E0 f(U_rec). In fact the raw source vacuum before launch is outside
the original one-pair/one-carrier domain; Q has no automatic definition
on the whole launch space. Agreement of the prepared active-sector
occupation output with (T2)-(T4) neither specifies such an extension nor
proves conservation of that original Q. The original-Q stationarity
obstruction in the predecessor therefore remains intact at its stated
scope. Native six-pentit admission, achievable coupling precision and a
physical external read-and-retain apparatus remain separate obligations.
