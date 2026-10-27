# Fixed program, original ports and the complete inventory

**NON-CANONICAL, L1, conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. Apache-2.0.

This note instantiates the autonomous controller with the frozen local
original-port preparation word. All source identities remain conditional
inputs. No expanded circuit, numerical simulation or scientific executable
has been run. Integer counts below are conservative construction bounds.

## 1. Inherited target and energy-bearing factors

Use the six-file content package C-ORIGINAL-PORT-SOURCE-PREPARATION-N
with manifest SHA256
3d55cdf8236cf11347049415c31c563f7799f52e1345142fb97df701159a9470.
In particular [SOURCE_CIRCUIT](../C-ORIGINAL-PORT-SOURCE-PREPARATION-N/SOURCE_CIRCUIT.md)
specifies the full source preparation, and
[LOCAL_REALIZATION](../C-ORIGINAL-PORT-SOURCE-PREPARATION-N/LOCAL_REALIZATION.md)
specifies a local charge-conserving realization. No file of that package
is changed by this extension.

Keep its n=2208 data/control qubits and n-2=2206 synthesis scratch bits.
Its original 2204 occupation bits are grouped into 1102 FOUR-LEVEL sites,
one per integer coordinate h in the 29 original cells 83,...,111. Their
levels and energies are

```text
h=0,+1,-1,2;       E_h=epsilon*(0,2,2,8), epsilon>0.
```

The remaining data/control/scratch factors are 2210 zero-energy qubits:
three LCU helpers, one retained setting C, and 2206 scratch qubits.
The setting is an admitted information input, or the genuine Gibbs state
I/2 in the fully thermal setting variant. It is never reset as unknown
information. Thus M=2209 zero-energy helpers require preparation.

Keep 4414 same-spectrum reservoir-rail sites, each with levels
0,...,26468 and energy epsilon times the level. Their working level will
be b_0=17632. The initial working reservoir is now cold Gibbs, not
supplied sharply excited; the launch in Section 3 loads it.

Grouping the two bits of h is essential. Moving individual bits between
rows by an unfunded SWAP would not preserve 2h^2. The controller always
SWAPs an entire h site, entire ladder site, or entire qubit with an
identical-spectrum copy.

The occupation intertwiner is the actual Canon map
I_0=Emb Gamma^(-1)D_2*, D_2=diag(1,i,i,-1), with identities on memory and
reference. The receiver is the original 13-coordinate memory subbank at
coarse position100, not an archive decoded into a different register.
Its admitted information is the 26-dimensional code, restricted to
K=span(d1,...,d25) for the fresh-write contrast. The complete 13-site
block, together with C and a passive reference, is preserved as unknown
information. Its total native charge is exactly2.

## 2. Exact word and helper cooling

Fix an integer k>=8. Put

```text
r=2*(k+ceil(log2 M)+1),   M=2209,
G=17643*epsilon,
G_star=512*n^4*4^n,      n=2208.                     (P1)
```

For each helper supply r hot and r cold donor qubits. BOTH donor gaps
are G. This differs from using gap-epsilon donors: with beta_h*G=ln2,
their excitation probability is exactly1/3, not a substituted value.
The cold-ground comparison gives reset error

```text
xi=M*(2/3)^r < 2^(-k-1).                            (P2)
```

The complete reset is the same energy-conserving permutation exchanging
|1,0,1> and |0,1,0> on hot,cold,helper. All other six basis states remain.
For each helper, fetch donor j down its hot/cold rails by j-1 adjacent
SWAPs, apply reset, and reverse those fetch SWAPs. All used donors return
to their own slots in changed states. This is

```text
G_cool=M*(2r^2-r)
```

local gates, with exactly2Mr donor qubits. Neither an erased donor nor
a renewed bath is implicit in the reduced reset channel.

Program1 first performs this cooling word and then the complete source
preparation, including coherent choice of the plus/minus phase. The
old source compiler gives at most G_star funded local primitives; pad
with identities to exactly G_star. Program2 performs THREE successive
complete finite U_rec macrostep matrices, each separately compiled and
funded by the same method and padded to G_star primitives. Thus

```text
P1=G_cool+G_star,       P2=3G_star,       P=P1+P2.     (P3)
```

Both P1 and P2 are even: r is even, and G_star is even. This padding is
part of the fixed program, not a change to an error target.

Each primitive acts on at most seven nearby payload factors and commutes
with the sum of their stated onsite energies on the ENTIRE raw space.
Including the partners of every touched occupation bit before its
energy-fiber lift gives this statement after grouping each h pair.
All incomplete ladder energy fibers retain the identity completion.
On the good launch input the working ladder remains buffered and returns
to b_0 after each charge-preserving endpoint.

Program2 is the same U_rec^3 on the admitted causal cone, including its
absolute controlled phases and occupied-memory exchange. Its compiled
microhistory is not a continuous evolution under E0*f(U_rec). The
autonomous clock below implements the successive program operations;
it does not assign one original macrostep to each physical clock tick.

## 3. A local thermal launch into the actual seed

The original basis source u2 at coarse position97 has the four nonzero
integer coordinates

```text
h2=-1, h3=-1, h5=+1, h12=-1.
```

The first two carry the object e2; the last two are the Canon token t0.
Their total charge is8. The phase-zero intertwiner on u2 contributes
only the known scalar -i*exp(2*pi*i/5). Include it in the launch matrix
element or the common history gauge; it is independent of unknown data.

Place the working ladder home next to these four source factors. A hot
qubit of gap G exchanges its excitation with these four occupations,
the ladder level b_0, and the first cursor state of gap3epsilon:

```text
fuel1, source(0,0,0,0), ladder0, cursorvac
  <-> fuel0, source(-1,-1,+1,-1), ladder17632, cursorF.
```

Both endpoints have energy (8+17632+3)*epsilon=G. The edge has only
seven physical factors. It is identity on every other source factor,
old memory and setting. In particular its projector is NOT a projector
onto the vacuum of all29 cells. The remaining vacua are supplied by the
counted cold comparison component. Thermal defects elsewhere stay in
the actual input and its error bound.

This uses a single26469-level ladder site with a specified transition
between levels0 and17632. It is neither an all-qubit launch nor a proof
that nearest-rung native couplings synthesize this transition. The large
but fixed local dimension and its matrix element are declared resources.

Two cold qubit flags A and B have gap epsilon. All cursor states before
A cost3epsilon, those after A and before B cost2epsilon, and those after
B cost epsilon. Raising each flag consumes the released cursor energy.
No pure clock or initially charged working reservoir is supplied.

## 4. An explicit planar payload layout

Here is one layout meeting the controller's fixed-radius hypothesis.
Start from the old fine qubit-line indices i=1,...,4414. For each h pair
(2j-1,2j), put its whole four-level factor at (8(2j-1),4). Put the
unpaired qubits i=2205,...,4414 at (8i,4). Put ladder rail site i at
(8i,0). The fine-line labels are a fixed implementation of the original
occupation ports; their position labels and the I_0 reading do not vary
with the program or setting.

For a helper at index i, put hot donor j at (8i-2,4j+4) and cold donor j
at (8i+2,4j+4). The setting index2208 has no reset rails. The helper
indices are2205,2206,2207 and2209,...,4414. These sites are distinct and
have mutual distance at least two. Take

```text
X0=8*4414+2,       Y0=4r+4.                          (P4)
```

Every routed computation primitive, its full occupation partners and
working ladder lie in a Manhattan-radius128 ball. Adjacent rail swaps
have fixed spacing8 or4. The reset uses the near donor endpoints, not
the remote j-th pair directly. The four launch occupations in one cell
span20 original bit indices, so their enclosing ball, the nearby ladder
and fuel/cursor fit in the same radius128 bound. Select the working
ladder home at the h2 pair of cell97; allowing this home instead of a
line endpoint does not increase the old2N_q routing bound.

The controller scales this planar layout by4, supplies positive and
negative copy towers, and returns every payload factor to its original
row-zero position after each program. This preserves the nominated
original ports at both windows. It is a fixed finite microscopic
representation with a declared geometry; no unproved metric identity
to the original six-pentit checkpoint space is asserted.

## 5. Exact inventory before choosing the cold temperature

Each payload row contains

```text
1102 h sites of dimension4,
4414 ladder sites of dimension26469,
2210 zero-gap qubits,
2Mr donor qubits of gap G,
S=7726+2Mr total payload sites.                     (P5)
```

There are P1 positive-copy rows, P2 negative-copy rows, and the common
row0. Every copy has the same spectrum as its corresponding row0 factor.
All future copies, including the future information-register locations,
start in Gibbs states; only row0 contains the admitted memory and setting.

Let r1,r2 be the two physical outward-raster vertex counts fixed in
[STATIC_CONTROLLER](STATIC_CONTROLLER.md), let B_buf be its padding
integer, and put K=12B_buf. To avoid confusing this B_buf with the ladder
maximum26468, the latter is always written explicitly in this note.
There are r1+r2 qutrit cursor sites and K-2(r1+r2) qubit cursor sites.
The count of nonvacuum cursor levels is exactly K. Including the one
hot fuel and two flags gives

```text
N_total=S*(P+1)+K-r1-r2+3.                          (P6)
```

Equivalently the raw dimension is

```text
4^[1102(P+1)] *26469^[4414(P+1)] *3^(r1+r2)
 *2^[(2210+2Mr)(P+1)+K-2(r1+r2)+3].                 (P7)
```

The 13 original memory sites and original setting are admitted
information, not missing factors in this dimension. Their actual input
is restricted to the nominated information code and may be correlated
with an arbitrary passive reference. No finite dimension for that
reference is asserted.

The cold counts relevant to the comparison are

```text
N_h,c=1089+1102P,
N_lad,c=4414(P+1),
N_donor,c=Mr(1+2P),
C_eff=3N_h,c+2N_lad,c+N_donor,c+K+2.                (P8)
```

The last two are the flags. Clock colors are counted by K, not treated
as independent qubits at a shared qutrit. There are Mr+1 hot qubits.
The zero-gap Gibbs qubits number2210(P+1)-1 when the original setting
is admitted information; add one when that setting is itself I/2.

Only after these integers are fixed choose

```text
beta_h*G=ln2,
beta_c*epsilon=(k+1+ceil(log2 C_eff))*ln2.            (P9)
```

The independent product of these states prepares all noninformation
inputs, including the seed's four factors, ladders, all raw copies and
every clock. No site or temperature is selected after conditioning on a
favorable outcome. The cold defect bound and the complete output
instrument are proved in [THERMAL_CHANNEL](THERMAL_CHANNEL.md).

For k=40, r=106, Mr=234154, 2Mr=468308 and S=476034.
These are just the row0 payload counts; the P copy rows and K cursor
levels are additional and vastly larger. The generator scale stays
fixed as those counts grow. This is an existence result with an explicit
cost, not an economical architecture.

## 6. What returns and what is consumed

At the first ideal completed program, the source is psi_s,±, the old
receiver/reference is unchanged, the source-preparation helpers are
ready, the sharp work level is b_0, and spent reset donors are retained.
At the second completed program the original receiver has the full
three-step output, including its old-content/reference continuation.
Both return sweeps put ALL payload factors, including spent donors, at
their row0 ports and restore the arbitrary future-copy contents to
their original order.

This does not restore the original source vacuum, fuel excitation,
thermal donor product or flags during the read window. Exact reversal
at the later clock recurrence restores those resources only while
undoing the record as well. Keeping an output and renewing the device
requires additional storage and a separate regeneration process.
There is one launch for both programs, not two independent probabilities
to be multiplied.

The admitted static couplings, finite local levels, thermal boundary
condition and original information inputs remain physical premises.
The construction closes their mathematical autonomous scheduling at
the stated scope, not material realization, robustness to uncontrolled
perturbations, original six-pentit gate admission or empirical occurrence.

## 7. Sufficient finite-time tolerance, not an achieved calibration

The exact static coefficients are physical premises. Their sufficient
accuracy can be bounded without constructing or enumerating the enormous
matrix. Let H'=H+V with V=V* on the same finite physical space. Suppose
the actual initial state, including its admitted reference, differs from
the nominal thermal/information input by at most zeta_in in trace
distance. Suppose the implemented complete readout instrument differs
by at most zeta_read in half-diamond norm. For the random-setting variant
this must cover the complete JOINT flag/setting/readout instrument.

Duhamel's formula and unitary invariance give a reference-uniform bound
on the complete output instrument:

```text
zeta(t)<=zeta_in+|t|*||V||/hbar+zeta_read.             (P10)
```

Indeed ||exp(-iH't/hbar)-exp(-iHt/hbar)||<=|t| ||V||/hbar,
and the half trace-distance of conjugated states is bounded by the same
unitary norm difference. This includes all correlations and all branches.
It assumes no stochastic independence or favorable cancellation of errors.

The displayed law has at most N_term=N_total+2K+1 summands: one onsite
term per physical site, K propagation terms and K+1 potentials. Counting
zero onsite terms is harmless. If V is the sum of Hermitian perturbations
to these terms, each of norm at most nu, then ||V||<=N_term*nu. A simple
uniform sufficient condition for all stated useful times t<=2T_h is

```text
zeta_in+zeta_read<1/4000,
nu <= hbar*(1/4000-zeta_in-zeta_read)/(2T_h*N_term).  (P11)
```

Thus zeta(t)<=1/4000. Extra undescribed couplings must be counted in V;
they are not covered merely because the intended terms satisfy (P11).

Write z=2^(-k-1). A nominal completion probability p>1/4 becomes at
least p-zeta. The complete-instrument normalization inequality in
THERMAL_CHANNEL bounds the conditional shift by zeta/p<4zeta.
For two separately supplied settings at k=40, the final contrast obeys

```text
Delta_perturbed > 1/50-12z-8zeta >1/100.              (P12)
```

For the random-setting Gibbs variant, nominal conditional setting mass
is at least1/2-6z. The nominal joint event (B_f=1,C=s) therefore has
probability greater than (1/4)(1/2-6z)>1/9. Its conditional shift is
less than9zeta. Its nominal per-setting target error is at most12z, so

```text
Delta_random,perturbed >1/50-24z-18zeta >1/100
                                           (k=40).  (P13)
```

These are sufficient worst-case finite-time continuity bounds. They do
not establish that material couplings attain (P11), preserve H>=0 or
the exact bare-energy conservation under an arbitrary V, or supply an
indefinite-time stability theorem. They expose the precision cost:
increasing the programmed time and the number of terms tightens the
allowed error of each term. Finite mathematical existence is not a
demonstration of affordable calibration or fault tolerance.
