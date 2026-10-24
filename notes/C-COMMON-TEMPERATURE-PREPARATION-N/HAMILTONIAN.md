# Common-temperature preparation with one specified fuel input

**NON-CANONICAL, L1, conditional candidate-T.** This is an analytical finite
construction. It is not an executed compiler, independent mathematical
acceptance, or a native-law derivation.

The fixed predecessor is [#1764 at `6670ac27`](https://github.com/mathorn1973/twist-j/tree/6670ac274888927be3429a463966da41ca8d2e8b/notes/C-THERMAL-WORK-CLOCK-BOOTSTRAP-N).
The new law prepares its actual joint thermal input from common-temperature
Gibbs factors and then implements its complete endpoint operator. A supplied
nonthermal fuel population replaces the supplied temperature contrast.
Every new clock and counter starts Gibbs, not in an exactly clean or
inverted state. Its finite defect weight remains in the proof.

## 1. Actual target spectra and the two finite words

Fix `beta_0 epsilon=ln(2)`. Retain the predecessor's physical onsite spectra
on its target register factors. For every target `i` whose required inverse
temperature `beta_i` differs from `beta_0`, add an independent donor of the
same Hilbert-space dimension with onsite energies

\[
 E^{\rm donor}_{i,a}={\beta_i\over\beta_0}E^{\rm target}_{i,a}.
 \tag{H1}
\]

All energies here are integer multiples of `epsilon`: the old cold targets
use the old integer multiplier `b_old`, and the donor for the old hot
manifold has gap `epsilon` instead of its target gap `(R_old+3)epsilon`.
The moderate-temperature old factors need no replacement. Initially every
nonlogical target and donor is Gibbs at the same `beta_0` for its actual
onsite Hamiltonian. The unknown logical input and its passive reference
retain the inherited fixed-charge interface.

Let `P` be the product of SWAPs between the indicated target/donor pairs.
It transfers the donor populations into the actual target spectra. After
tracing the donor and work records, its target output is exactly the joint
Gibbs product required by #1764, with the admitted logical/reference state.
This is an implemented population transfer, not a new name for the
high-gap donor's temperature. Unequal-gap SWAPs are funded below.

Let `H_prior` be the complete raw Hamiltonian of the immutable predecessor,
and let `tau_prior` be its exact endpoint time. Define

\[
 T=\exp(-i\tau_{\rm prior}H_{\rm prior}/\hbar)\otimes I_{\rm donors}.
 \tag{H2}
\]

This uses its entire raw space, including its original thermal defects.
Since the predecessor proves \([H_{\rm prior},H_{0,\rm prior}]=0\), `T` preserves the
retained target onsite energy. The new apparatus compiles (H2). The old
interaction terms are NOT also added to the new physical Hamiltonian.
Only the specified onsite spectra are retained as actual additive energy;
(H2) is the target matrix for the new local program. The old continuous
trajectory and old wall-clock times are not the new trajectory or times.

There are `N` information sites, comprising these targets and donors, of
physical dimensions `d_1,...,d_N`. Put `d=product_i d_i`. In particular the
old multilevel sites are actual qudits, not silently truncated binary codes.

## 2. A finite qudit compiler with an explicitly imperfect counter

Place one counter copy of dimension `N+1` at each information cell. The
logical compiler uses one distinguished counter factor. For a controlled
one-site unitary, increment this counter modulo `N+1` once for each of the
`N-1` other information sites that matches its specified control symbol.
Apply the target unitary only when the counter equals `N-1`, then undo the
increments. On counter input `|0>` this is exactly the fully controlled
unitary and restores `|0>`. It uses `2N-1` one-/two-site operations. No
other counter copy needs a special state. A basis phase on one full
information word similarly uses `N` increments, a phase at counter value
`N`, and `N` inverse increments.

For completeness, QR elimination decomposes an arbitrary `d x d` unitary
into fewer than `d^2` two-level rotations and basis phases. A Gray path in
the product basis has length at most `N`. It expresses a two-level rotation
using at most `2N-1` fully controlled one-site gates. Thus each QR factor
uses at most `4N^2` counter primitives, including the basis-phase case.
This is a constructive finite algorithm with specified raw unitaries; no
clean binary scratch register is assumed.

Route the distinguished counter factor to a cell and back by SWAPs of
identical counter copies. Conjugation makes every such trip the identity
on all original other counter factors, even when they are dirty or
correlated. Route the distinguished work factor in the same way through
identical work copies when funding a gate. The physical primitive count
per counter primitive is at most `4N`, including both trips and the local
funded gate. Consequently each macro admits the conservative bound

\[
 J_P\le16N^3d^2,\qquad J_T\le16N^3d^2,
 \qquad J=J_P+J_T\le32N^3d^2.
 \tag{H3}
\]

Use the actual finite lengths produced by a fixed QR/Gray ordering. The
matrix (H2), those algorithms, and the count bound specify a finite word;
its gates have not been numerically enumerated or scientifically executed.
The exact elementary matrices, including their precision, are added
physical assumptions.

The counter algorithm has a specified unitary action on every raw counter
input. Its intended interpretation is proved on `|0>` only. Bad initial
counter values are retained and bounded, not asserted to implement the
same logical word. In particular a raw compiled extension need not preserve
information energy on those bad counter values.

## 3. Noncircular parameter order and physical funding

The following order fixes all quantities without a size/temperature loop.
First fix the information dimensions, the counter dimension, both words
and routes in Section 2, and the row width `W=3N`. Then choose

\[
 B\ge\max\{J_P(W+3)-1,J_T(W+3)-1,8192\},
 \quad L=4B,\quad K=4L=16B.
 \tag{H4}
\]

There will be `K+1` new main/loader cursor qubits. Now fix

\[
 \ell=96+\lceil\log_2(K+2)\rceil,\qquad
 \Delta=\ell\epsilon.
 \tag{H5}
\]

Each counter copy has levels `0,...,N` with energy `k Delta`. Every new
cursor qubit has gap `Delta`. These systems are Gibbs at `beta_0`; their
small excitation weights arise from their actual large gaps at that same
temperature. Only the distinguished counter's ground value is needed for
the compiler. All other counter copies are allowed their complete Gibbs
contents and are restored by the routing identities.

Let `Q_info` be the sum of the maximum information-site charges in units
`epsilon`. Define the one-row nonwork charge bound

\[
 Q=\max\{128,Q_{\rm info}+N^2\ell\}.
 \tag{H6}
\]

The `N^2 ell` term includes all `N` physical counter copies, each of
capacity `N Delta`. Work sites are excluded from `Q`. Every work copy is
an actual onsite system of dimension `4Q+1`, with levels `b epsilon`,
`0<=b<=4Q`. Initially all work copies, including the distinguished one,
are Gibbs at `beta_0`. No charged peak is supplied. Increasing this work
capacity changes gate matrices but not the primitive count or site count
already used in (H4), so the order is noncircular.

For a primitive `U` on nonwork subset `A`, let `q_A` be its maximum charge.
On each complete local charge sector `q_A<=t<=4Q`, define

\[
 J_{A,t}|x\rangle=|x\rangle|t-e_A(x)\rangle,
 \qquad \Gamma_A(U)|_t=J_{A,t}UJ_{A,t}^{\dagger},
 \tag{H7}
\]

and use the identity on each incomplete local sector. This is a full
unitary preserving the actual local additive energy. Work-routing SWAPs
preserve energy because the work spectra are identical.

The launch below raises any initial work level `b in [0,Q]` to `b+2Q`.
For such an input, total nonwork-plus-work charge lies in `[2Q,4Q]`.
Every local gate is therefore within its complete sector, and the lifts
telescope throughout both macros. At a prefix,

\[
 b_{\rm work}=b+2Q+e_{\rm initial}-e_{\rm current},
 \qquad Q\le b_{\rm work}\le4Q.
 \tag{H8}
\]

The excursion bound depends on `Q`, not the number of gates. The argument
includes the counter charge and all routed counter factors.

On distinguished counter input zero, the compiled `P` and `T` restore the
counter. For `T`, the net information energy is unchanged; other counter
factors and donors are unchanged. Hence the complete funded `T` acts as
`T tensor I_work` on this buffered initialized-counter subspace, even when
the work is already correlated with the prepared targets and donors. No
such factorization is claimed on every bad raw counter or work sector.

## 4. Rows, fixed preparation row, and local geometry

A row has the repeating physical columns

```text
information_i at 3i-2; counter_i at 3i-1; work_i at 3i.
```

Use `J+1` rows at heights `2t`, `0<=t<=J`, with the same spectrum and
dimension at each repeated column. The original active row is row zero;
all other rows are common-temperature Gibbs junk. A primitive is either
a funded information/counter/work gate on three sites in one cell or a
counter/work transport SWAP between neighboring cells, spanning at most
four consecutive columns.

Transfer a complete row by individual equal-spectrum site SWAPs. Apply
its one primitive on the destination row as soon as its last operand has
arrived. This stage is exactly a whole-row SWAP followed by that primitive.
Induction gives the original row-zero state acted on by the intended word
in the final row, while every original junk row is merely permuted
backwards. This identity holds for arbitrary row contents and correlations;
there is no clean-row prerequisite.

Alternating cursor rails at `y=2t+1`, with guard columns `0,W+1`, give a
block of `j` primitive stages `j(W+3)-1` edges. The count is one initial
entry edge, `j(W+1)` horizontal edges, and two vertical connector edges
for each of the `j-1` transitions between rails. The entry edge is an
identity guard. The preparation block finishes by main vertex `B`. An
identity-only detour places the start of the `T` block at main vertex `3B`.
It finishes by `4B=L`. All remaining main edges through `3L` are identity
edges without row transfer. Thus one fixed row holds the complete prepared
target during main indices `B,...,3B`; one fixed final row holds the output
for every main index at least `L`.

For the detour use coordinates relative to the preparation block's final
guard, with the positive horizontal direction pointing outside the data
strip. That guard is `(0,0)` and the outward next-block source is `(1,2)`:
go out to `(s,0)`, vertically to
`(s,2)`, then back to `(1,2)`. Its length is `2s+1` with two unit vertical
edges or `2s` with one length-two edge, so it realizes the required padding
length. Mirror the horizontal coordinate when the outward side is left.
No data moves on this detour or the final tail.

The main entry is `m_0=(-1,1)` and first guard `m_1=(0,1)`; its initial
work site is at `(3,0)`. Add a fuel qubit at `(1,-1)` and loader sites

\[
 t_j=\begin{cases}(-1,-1-j),&0\le j<L/2,\\
                   (0,j-L),&L/2\le j<L.
       \end{cases}
 \tag{H9}
\]

The loader lies below the rows. Its first and last sites are `(-1,-1)` and
`(0,-1)`. The four-site fuel reaction lies in radius 3 about `(1,0)`;
the guarded handoff terms below lie in radius 2. A row edge has at most
four data sites and two cursor sites. A conservative uniform statement is
at most seven sites in Manhattan radius 4 and interaction degree at most
32 other physical sites. Local dimensions grow and are counted separately.
A containing rectangle has width `W+12B+6` and height `2J+L/2+1`.

The full Hilbert-space dimension is

\[
 \dim\mathcal H=d^{J+1}(N+1)^{N(J+1)}(4Q+1)^{N(J+1)}2^{K+2}.
 \tag{H10}
\]

There are `N(J+1)` information, counter, and work sites of each type,
`K+1` cursor/loader qubits, and one fuel qubit. Work-bank capacity is
`4Q epsilon N(J+1)` and counter-bank capacity is
`N^2 Delta(J+1)`. Empty-looking or unused copies are not omitted.

## 5. Fuel, launch and the full positive Hamiltonian

The one new nonthermal input is the full-rank fuel population

\[
 \rho_f=(1-\delta_f)|1\rangle\langle1|+\delta_f|0\rangle\langle0|,
 \quad\delta_f=2^{-96},\quad H_f=E_f n_f,
 \quad E_f=2Q\epsilon+2\Delta.
 \tag{H11}
\]

Its location, inversion and energy are specified resources. It is not
claimed to be Gibbs at `beta_0`. Every other new factor is Gibbs at that
one temperature, apart from the unchanged admitted logical input.

With `s^+` the qubit raising operator, the local launch is

\[
 X_0=|0\rangle\langle1|_f\otimes
       \sum_{b=0}^{Q}|b+2Q\rangle\langle b|_{\rm work}
             \otimes s_{m_0}^{+}s_{t_0}^{+}.
 \tag{H12}
\]

It raises the thermal work level by `2Q` and creates both the main entry
and loader excitation. Its energy cost is exactly `E_f`. Put
`P_in=X_0^dagger X_0`, `P_out=X_0 X_0^dagger`, `D_0=P_in+P_out`.
The two projectors are orthogonal. The initial work offset `b` is retained,
not erased or assumed zero.

For loader edges `j=0,...,L-2`, let `C_j=I` except
`C_(L-2)=n_(m_0)`, and define

\[
 X_{j+1}=C_js_{t_{j+1}}^+s_{t_j}^-,\qquad
 D_{j+1}=C_j(n_{t_j}+n_{t_{j+1}}).
\]

For the first main edge use

\[
 X_L=n_{t_{L-1}}s_{m_1}^+s_{m_0}^-G_0,\qquad
 D_L=n_{t_{L-1}}(n_{m_0}+n_{m_1}),\qquad G_0=I.
\]

For `r=1,...,3L-1`, use the scheduled row instruction `G_r`:

\[
 X_{L+r}=s_{m_{r+1}}^+s_{m_r}^-G_r,\qquad
 D_{L+r}=n_{m_r}+n_{m_{r+1}}.
 \tag{H13}
\]

Define vertex projectors

\[
 V_0=P_{\rm in},\quad V_{j+1}=n_{t_j}\ (0\le j<L-1),\quad
 V_L=n_{m_0}n_{t_{L-1}},\quad V_{L+r}=n_{m_r}\ (1\le r\le3L).
 \tag{H14}
\]

Let `H_D` include every information, counter and work onsite term in every
row. For any `g>0`, set

\[
 a_i={g\over K+1}\sqrt{(i+1)(K-i)},\quad a_{-1}=a_K=0,
 \quad v_i=g-a_{i-1}-a_i\ge0,
\]
\[
 H_0=H_D+\Delta\left(\sum_rn_{m_r}+\sum_jn_{t_j}\right)+E_fn_f,
\]
\[
 H_{\rm prop}=\sum_{i=0}^{K-1}a_i(D_i-X_i-X_i^{\dagger})
                              +\sum_{i=0}^{K}v_iV_i,
 \qquad H=H_0+H_{\rm prop}.
 \tag{H15}
\]

This is one time-independent full-space operator. The reaction is a direct
sum of positive `a_0 [[1,-1],[-1,1]]` blocks. Ordinary hopping terms have
blocks zero on `00`, `2a_i I` on `11`, and
`a_i [[I,-G_i^dagger],[-G_i,I]]` on `10/01`. Commuting projector guards
preserve positivity. Every edge has norm at most `2a_i<=g`; every vertex
potential is positive. Each gate conserves `H_D` by its funded completion,
and the reaction is resonant. Therefore

\[
 H\ge0,\qquad [H_0,H_{\rm prop}]=0,
\]
\[
 H\le\{\epsilon[(J+1)Q(1+4N)+2Q+\ell(K+3)]+(K+1)g\}I.
 \tag{H16}
\]

The bound counts all physical copies. The reverse operators are part of
the Hamiltonian. There is no strictly forward microscopic generator,
absorbing halt, or external activation switch.

## 6. Good history, all retained defects, and no second launch

Let `z=2^(-ell)`, `Z_W=sum_(b=0)^(4Q)2^(-b)`, and
`Z_A=sum_(k=0)^N z^k`. The good initial component has excited fuel,
work level in `[0,Q]`, the distinguished counter in zero, and every main
and loader qubit empty. Its exact weight is

\[
 q=(1-\delta_f)\,{\sum_{b=0}^{Q}2^{-b}\over Z_W}
                   {1\over Z_A}(1+z)^{-(K+1)}.
 \tag{H17}
\]

No condition is placed on the other counter copies or row junk. The
work-tail weight is less than `2^(-Q)`, and the distinguished counter and
cursor defects have total weight at most `(K+2)z`. Hence

\[
 \eta:=1-q<2^{-96}+2^{-128}+2^{-96}<3\,2^{-96}.
 \tag{H18}
\]

Every thermal resource factor and the fuel are full rank; the admitted logical/code factor retains its separate promise. These are components of a supplied density,
not physically selected runs. The actual evolution is exactly
`q rho_good(t)+(1-q)rho_bad(t)` under the same raw Hamiltonian.

For each initial work offset `b<=Q`, the good history consists of:

- vertex 0: excited fuel, work level `b`, main/loader vacuum;
- vertices `1,...,L`: ground fuel, work level `b+2Q`, occupied main entry,
  loader at its successive site, with the information and counters unchanged;
- vertex `L+r`, `1<=r<=3L`: ground fuel, loader at its last site, main at
  `m_r`, and the programmed prefix acting on the charged row.

The potential (H14) equals one at just the corresponding vertex on this
subspace. Incident diagonal terms plus its potential equal `g` everywhere.
The last loader hop requires the occupied main entry; the first main hop
requires the final loader. Consequently the loader cannot retreat by
itself after the main program starts. The span is a single invariant path
for every offset and every admitted information/reference input.

A second independent forward reaction is impossible on this path: fuel is
ground after the first reaction, and no later instruction touches it.
The reverse reaction occurs only after the same path has coherently
returned to its first loader configuration and restored the needed work
level. Raw defective states may have other transitions; their entire
weight is included in (H18), not asserted to be trigger-free.

## 7. Finite target-preparation and output windows

The history gauge on each good path gives
`H_prop = gI-2g J_x/(K+1)`. Its exact weights are

\[
 p_j(t)={K\choose j}\sin^{2j}\theta\cos^{2(K-j)}\theta,
 \qquad \theta={gt\over\hbar(K+1)}.
 \tag{H19}
\]

This is the standard finite spin-chain transfer construction, not a
statistical independence premise about observed events. All initial
physical densities commute with `H_0`; because of (H16), their free density
phases cancel for all times. No calibration relation between `g` and
`epsilon` is needed. The logical/reference scope remains fixed-charge.

The desired old three-temperature target has been prepared after main
index `B`, and the old endpoint macro has not begun before main index
`3B`. Thus good target-preparation indices are

\[
 5B\le j\le7B.
 \tag{H20}
\]

On this interval the entire prepared row is fixed. Counter zero has been
restored; donor and work correlations remain present. In the first rising
window with `p=sin^2(theta) in [23/64,25/64]`, exponential Markov bounds give

\[
 \Pr(X<5B)\le[(5/4)^5(297/320)^{16}]^B,
\]
\[
 \Pr(X>7B)\le[(4/5)^7(281/256)^{16}]^B,
 \qquad X\sim\operatorname{Bin}(16B,p).
 \tag{H21}
\]

Both bracketed bases are less than `31/32`. For the first use
`(297/320)^4<3/4`, obtaining `253125/262144<31/32`. For the second use
`(281/256)^4<16/11` and `(4/5)^7(16/11)^4<31/32`. Therefore

\[
 \delta_{\rm prep}<2(31/32)^B<2^{-255}.
 \tag{H22}
\]

Tracing the new cursor removes cross-history terms. On every good history
the full old target/reference marginal is the required product of Gibbs
factors and the original logical/reference state. The unconditional joint
reduced preparation error is at most `eta+delta_prep`. This is not merely
agreement of separate thermal marginals. A comparison retaining a normalized
full clock packet instead has a square-root history error.

The complete word has finished at main index `L`, global index `2L`.
For `theta in [pi/3,2pi/3]`,

\[
 w(t)=\Pr(X\ge2L),\qquad1-w(t)\le(3/4)^{2L}=:\delta_{\rm out}.
 \tag{H23}
\]

The final data row is fixed on this tail. The complete read predicate is

\[
 \Pi_{\rm new}=
 \left[I-\prod_{r=L}^{3L}(I-n_{m_r})\right]\Pi_{\rm prior,read},
 \tag{H24}
\]

where `Pi_prior,read` is the ENTIRE transported #1764 read projector,
including its old main-tail condition and inherited completion latch and
acceptance flag, acting on the final information row. It is not replaced
by a flag alone. On the good component, the reduced output is exactly
`w(t)` times the full pinned predecessor endpoint channel at its actual
thermal input. Its original defects and activation factors are already
included in that channel because (H2) acts on the entire old raw space.
The new bad components add a positive accepted contribution of trace at
most `eta`. Detailed conditional errors are in [PREPARATION.md](PREPARATION.md).

There is no physical intermediate projection, reset or independently
restarted old Hamiltonian. The result follows from the complete unmeasured
history. The mathematical read observable is not a detector construction.
At `tau=pi hbar(K+1)/(2g)` transfer to the last vertex is exact on the good
paths, with propagation phase `-i`; later reversal and recurrence remain.
No old physical retention interval is automatically inherited.

## 8. Complete energy moments and the remaining fuel resource

Define the raw diagonal operator and hop decomposition

\[
 A=\sum_i a_iD_i+\sum_i v_iV_i,\qquad M=H_0+A,
 \qquad H=M-\sum_i a_i(X_i+X_i^{\dagger}).
\]

On the actual product input, with its admitted fixed-charge logical block,

\[
 \langle H\rangle=\langle M\rangle,\qquad
 \operatorname{Var}(H)=\operatorname{Var}(M)
 +\sum_i a_i^2\langle X_i^{\dagger}X_i+X_iX_i^{\dagger}\rangle.
 \tag{H25}
\]

Every off-diagonal hop has zero initial expectation. Two distinct edges
cannot return the same fuel/cursor basis configuration in two hops;
same-edge returns cancel their data unitaries. This proves (H25) including
all raw defects. `Var(M)` includes the covariance of additive energy with
its diagonal interaction part. All row, counter, donor, work, fuel and
cursor energies are present; no ideal-history variance replaces them.
[ENVIRONMENT.md](ENVIRONMENT.md) evaluates these as explicit finite sums
and identifies the paid-SWAP and fuel free-energy accounts.

Let `r=z/(1+z)` and `p_le=Pr_Gibbs(work<=Q)`. The local forward and reverse
reaction populations are

\[
 \pi_{\rm in}=(1-\delta_f)p_{\le}(1-r)^2,
 \qquad
 \pi_{\rm out}={\delta_f\over1-\delta_f}
                    2^{-2Q-2\ell}\pi_{\rm in}.
 \tag{H26}
\]

Tracing the initial commutator over every other site isolates the reaction
blocks, because all other hops have a traced cursor endpoint. Thus

\[
 \|[H,\rho_{\rm in}]\|_1
 \ge2a_0(\pi_{\rm in}-\pi_{\rm out})>0.
 \tag{H27}
\]

This is a reference-uniform lower bound on full-H nonstationarity. There
may be additional contributions on defective clock sectors. The inversion
of the one fuel site is precisely an admitted nonthermal initial resource;
it is neither manufactured by this process nor disguised as a prepared
clock. Its energy creates the working head and both new cursor excitations.
All those cursor and counter registers initially have common-temperature
Gibbs states at their actual spectra.

A complete common-temperature Gibbs state of `H_0` would be stationary
under (H15), as would a Gibbs state of `H`. The admitted fuel state avoids
that premise; it does not refute it. Manufacturing its inversion, the
large gaps and dimensions, the product/contact boundary and exact local
couplings remains outside this theorem. The canonical transfer law does
not supply these additional interactions, an occurrence law, a reusable
reset, or a permanent halt.
