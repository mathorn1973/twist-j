# Thermal charging, clock loading, and one complete static Hamiltonian

**Status: NON-CANONICAL, L1, conditional candidate-T.** This is an analytical
construction, not an independent acceptance, a scientific execution, or a
derivation of this hardware from the native law.

The fixed input is [PR #1761 at `32c17259`](https://github.com/mathorn1973/twist-j/tree/32c17259c4baf40bb6d08b521adc642956b57e94/notes/C-THERMAL-REGISTER-PREPARATION-N).
Its finite payload, exact funded gate word, row compiler, and output
predicate are retained. Its initially charged work distribution and
polarized master cursor are replaced by positive-temperature Gibbs inputs
and the local thermal loading mechanism below. Its clock coefficients and
first propagation edge are changed. This is one new law, not an unchanged
old Hamiltonian preceded by an uncounted external switch.

## 1. Fixed old word and new physical sites

Use the predecessor's notation `n,Q,R=2Q,J,W=2n`. There are `J+1` rows,
each containing `n` payload qubits and `n` physical work sites of dimension
`2R+1`. The distinguished work site is denoted `B_work`; its onsite
Hamiltonian is `epsilon sum_(b=0)^(2R) b |b><b|`. All these sites, including
thermal junk in unused rows, remain in the apparatus.

Write `B_old` for the old padding parameter and put

\[
 L=4B_{\rm old},\qquad K_{\rm old}=2L,\qquad K=4L.
 \tag{H1}
\]

The old master instruction sequence is `G_0,...,G_(2L-1)`, with `G_0=I`.
The old completed output is fixed after instruction `L-1`. Extend it by
`G_r=I` for `2L <= r < 3L`. Thus the main cursor has physical sites
`m_0,...,m_(3L)`. Add `L` loader qubits `t_0,...,t_(L-1)`. All main and
loader qubits have gap `epsilon`. There are `K+1=4L+1` such qubits.

Add two genuine multilevel sites `h,c`, each with basis
`|0>,|1>,...,|D>`, where

\[
 D=2^{84},\qquad
 H_h=(R+3)\epsilon\sum_{a=1}^D|a\rangle\langle a|,
 \qquad H_c=\epsilon\sum_{a=1}^D|a\rangle\langle a|.
 \tag{H2}
\]

The degeneracy is physical and is counted. These sites are not abstract
labels placed inside uncounted qubit codes. The maximum local dimension is
`max(2R+1,D+1)`, so a uniform small onsite-dimension claim is not made.

The initial hot distribution is Gibbs at
`beta_h (R+3) epsilon=ln(2)`. Its total excited weight is

\[
 q_h={D\over D+2},\qquad
 \Pr(h=a)={1\over D+2},\quad\Pr(h=0)={2\over D+2}.
 \tag{H3}
\]

The sink, distinguished work site, every main qubit, and every loader qubit
start in their full-rank Gibbs distributions at the common cold temperature

\[
 z=e^{-\beta_c\epsilon}=2^{-b},\qquad
 b=84+\lceil\log_2(D+K+3)\rceil.
 \tag{H4}
\]

The other old row sites retain their specified moderate-temperature Gibbs
inputs, with `beta_0 epsilon=ln(2)`, except the unchanged admitted logical
input of fixed charge and its arbitrary reference. There is no initially
inverted clock site and no initially sharply charged work head. The hot,
cold, and moderate-temperature inputs are nevertheless supplied physical
resources, not a Gibbs state of the complete coupled Hamiltonian.

## 2. Reaction, loader and guarded handoff

Let `s_x^+` raise a qubit and `n_x=s_x^+s_x^-`. Define the five-site partial
isometry

\[
 X_0=\sum_{a=1}^{D}
 |0_h,a_c,R_B,1_{m_0},1_{t_0}\rangle
 \langle a_h,0_c,0_B,0_{m_0},0_{t_0}|.
 \tag{H5}
\]

Its initial and final projectors are `P_in=X_0^dagger X_0` and
`P_out=X_0 X_0^dagger`. They are orthogonal. The reaction converts one hot
excitation into the sink excitation, charge `R` in the actual old work
site, one excitation at the actual old master entry, and a loader
excitation. Both sides have bare energy `(R+3) epsilon`.

All later gates leave `h,c` untouched. For loader edges `j=0,...,L-2`, set

\[
 C_j=\begin{cases}I,&j<L-2,\\n_{m_0},&j=L-2,\end{cases}
\]
\[
 X_{j+1}=C_j s_{t_{j+1}}^+s_{t_j}^-,\qquad
 D_{j+1}=C_j(n_{t_j}+n_{t_{j+1}}).
 \tag{H6}
\]

The first main edge is guarded by the loader endpoint:

\[
 X_L=n_{t_{L-1}}s_{m_1}^+s_{m_0}^-G_0,
 \qquad D_L=n_{t_{L-1}}(n_{m_0}+n_{m_1}).
 \tag{H7}
\]

Here `G_0=I`, so this guarded edge has no distant work operand. For
`r=1,...,3L-1`, use

\[
 X_{L+r}=s_{m_{r+1}}^+s_{m_r}^-G_r,
 \qquad D_{L+r}=n_{m_r}+n_{m_{r+1}}.
 \tag{H8}
\]

Finally put `D_0=P_in+P_out` and define the local vertex potentials

\[
 Q_0=P_{\rm in},\qquad
 Q_{j+1}=n_{t_j}\quad(0\le j<L-1),
\]
\[
 Q_L=n_{m_0}n_{t_{L-1}},\qquad
 Q_{L+r}=n_{m_r}\quad(1\le r\le3L).
 \tag{H9}
\]

These projectors are not mutually orthogonal on the full raw space. They
need not be: their one-vertex property is used only on the invariant
histories proved below. Their positivity holds everywhere.

The two guards have different purposes. Before the loader reaches its last
site, the old master entry cannot leave. Once it leaves, the last loader
hop is disabled because `n_(m_0)=0`. This prevents the loader from leaving
its endpoint and producing a second independent traversal of the main path.

## 3. Geometric placement and complete hardware count

Keep the predecessor's row geometry. Row-zero payload and work positions
are at `y=0`, with the first work head at `(2,0)`. Its old master source is
`m_0=(-1,1)` and first guard `m_1=(0,1)`. Put

\[
 h=(1,-1),\qquad c=(2,-1),
\]
\[
 t_j=\begin{cases}
 (-1,-1-j),&0\le j<L/2,\\
 (0,j-L),&L/2\le j<L.
 \end{cases}
 \tag{H10}
\]

The loader is a unit-edge U-shaped path. In particular `t_0=(-1,-1)`,
`t_(L-1)=(0,-1)` and `t_(L-2)=(0,-2)`. It lies below the old rows and has
no collision with them, the main cursor, or the two new multilevel sites.
The five reaction sites lie in a Manhattan-radius-3 ball about `(0,0)`.
Both guarded handoff terms lie in radius-2 balls. Extend the old final
outward straight identity tail by `L` main sites; these do not meet the
loader below the data rows.

The old row terms still use at most seven physical sites in radius 4.
Every new term also fits these bounds. A safe upper bound on the number of
other sites sharing an interaction with one site is 32: the old bound was
24, and the reaction adds at most four neighbors to its old work site.
The entry site has the reaction, initial potential, final-loader guard,
first-main guard, loader-end potential, and its onsite term; none has
support growing with `D` or `L`. Local matrix dimension, onsite energy, and
number of terms are separate resource measures.

The full physical inventory is

\[
 N_{\rm payload}=(J+1)n,\quad N_{\rm work}=(J+1)n,\quad
 N_{\rm main+loader}=K+1,
\]
\[
 \dim\mathcal H=
 2^{(J+1)n+K+1}(2R+1)^{(J+1)n}(D+1)^2.
 \tag{H11}
\]

The work-bank capacity remains `2R epsilon (J+1)n`, not that of the
single head being loaded. A conservative enclosing rectangle has width
`W+12B_old+6` and height `2J+L/2+1` lattice units. No new clean row or
polarized auxiliary timer is supplied. All loader sites initially have the
same cold Gibbs population, and its excitation is created by (H5).

## 4. A positive Hamiltonian on every raw state

Let `H_D` be the full old data-row onsite Hamiltonian, including every work
copy and the distinguished head, with its changed initial state. Define

\[
 H_0=H_D+\epsilon\left(\sum_{r=0}^{3L}n_{m_r}
                         +\sum_{j=0}^{L-1}n_{t_j}\right)+H_h+H_c.
 \tag{H12}
\]

For an arbitrary energy scale `g>0`, set

\[
 a_i={g\over K+1}\sqrt{(i+1)(K-i)},\quad
 a_{-1}=a_K=0,\quad v_i=g-a_{i-1}-a_i\ge0.
\]
\[
 H_{\rm prop}=\sum_{i=0}^{K-1}a_i(D_i-X_i-X_i^{\dagger})
                         +\sum_{i=0}^{K}v_iQ_i,
 \qquad H=H_0+H_{\rm prop}.
 \tag{H13}
\]

For the reaction, the nonzero blocks of `D_0-X_0-X_0^dagger` are
`[[1,-1],[-1,1]]`, one for each thermal label. It is positive with norm 2.
For an ordinary hop, the cursor `00`, `11`, and `10/01` blocks are zero,
`2I`, and `[[I,-G^dagger],[-G,I]]`. Each is positive with norm at most 2.
A loader or first-main guard is a commuting projector, which preserves this
property. Each edge term therefore has norm `2a_i<=g`. Each potential is
positive because `a_i<=g/2` and `Q_i>=0`.

Every `X_i` preserves the physical additive energy (H12). This follows from
the exact resonance of (H5), the equal gaps of the cursor hops, and the
predecessor's raw-space conservation `[G_r,H_D]=0`. The projectors in (H9)
commute with `H_0`. Consequently

\[
 H\ge0,\qquad[H_0,H_{\rm prop}]=0.
 \tag{H14}
\]

The sum of main and loader excitation numbers is not conserved by the
reaction, which creates two. Its energy comes from the hot site. Since
`2 sum_i a_i+sum_i v_i=(K+1)g`, the raw-space bound is

\[
 0\le H\le\left\{
 \epsilon[(J+1)(Q+2Rn)+K+R+5]+(K+1)g\right\}I.
 \tag{H15}
\]

All thermally wrong inputs, multiple cursors and unexpected work levels
follow this same finite Hermitian operator. No sector is removed from the
law. The adjoints in (H13) are physical reverse matrix elements. There is
no one-way Hamiltonian, absorbing halt, or externally timed switch.

## 5. The invariant active paths and the retrigger boundary

First consider a cold reference input with sink, head, every main qubit,
and every loader qubit in their ground states. For each hot label `a`, its
active path has these `K+1` orthogonal configurations:

- vertex 0: `h=a,c=0`, work level 0, and all main/loader sites empty;
- vertex `j=1,...,L`: `h=0,c=a`, work level `R`, main entry occupied,
  loader at `t_(j-1)`, and all other main sites empty;
- vertex `L+r`, `r=1,...,3L`: `h=0,c=a`, loader fixed at its last site,
  main cursor at `m_r`, with the old data prefix through main index `r`.

The data at the first `L` vertices are identical except for the charged
head. At later vertices they are the old prefix acting on that charged
input. The encoded logical input and its reference remain arbitrary within
the inherited fixed-charge promise.

Equations (H5)-(H9) make this span invariant: there is exactly one legal
forward edge and its reverse at each interior vertex. On vertex 0 only the
reaction and `Q_0` contribute. At a loader interior vertex only its two
incident edges and its corresponding `Q` contribute. At the loader endpoint
`Q_L=n_(m_0)n_(t_(L-1))` replaces the simple loader occupation. After entry
leaves, the final loader edge and `Q_L` vanish; only the two incident main
edges and the current main `Q` remain. The diagonal is exactly
`a_(i-1)+a_i+v_i=g` at every vertex.

There is no independent second launch on this active path. After reaction,
`h` is ground and the sink label is occupied; no subsequent data instruction
touches either. The forward reaction requires an excited `h` and an empty
sink. The reverse reaction also requires the occupied entry, the first
loader site and work level `R`; it is available only after the same legal
path returns to its first loader vertex. That reverse event is coherent
reabsorption, not an omitted failure or a new free activation. The guards
prevent a loader-only retreat after main propagation has started.

This is a reachable-sector proof, not a global assertion that arbitrary
thermally defective raw states cannot have extra transitions. Those states
are kept and bounded by their full input weight below. The complete model
does not silently assume that a local trigger remains unused on every
possible surrounding configuration.

The label `a` is transferred from hot to sink without erasure. The `D`
active paths are orthogonal and identical in their action on the old
apparatus. The hot-ground reference input is dormant: every propagation
term annihilates it, and its density is stationary under `H_0`.

## 6. Exact dynamics and finite loading/output windows

On each active path the history gauge transforms (H13) into

\[
 H_{\rm prop}|_{\rm path}\simeq gI-{2g\over K+1}J_x.
 \tag{H16}
\]

For a pure input of definite bare energy, the exact amplitudes, apart from
the common bare-energy and `g` phase, are

\[
 b_j(t)=\sqrt{\binom Kj}(i\sin\theta)^j(\cos\theta)^{K-j},
 \qquad\theta={gt\over\hbar(K+1)}.
 \tag{H17}
\]

The formula follows from the spin-`K/2` rotation, the standard engineered
perfect-transfer construction of [Christandl et al.](https://arxiv.org/abs/quant-ph/0309131v2).
At `tau=pi hbar(K+1)/(2g)` transfer to the last vertex is exact, with
propagation phase `-i`. The actual initial density, including arbitrary
admitted reference correlations, commutes with `H_0`. Its free density
phases therefore cancel for all times by (H14); no relation between
`epsilon` and `g` is required. Mixed thermal energies are not replaced by
one fictitious sharp energy.

Use `X~Bin(K,p)`, `p=sin^2(theta)`, only as notation for the exact norm
weights in (H17). For `p in [1/16,1/8]` on the first rising traversal,
the good loading vertices are `1,...,L-1`. They give the actual old work
head `|R>`, the actual old master entry `|1>`, all other old master sites
empty, and the unchanged old data input. The loader has not yet reached
the handoff site. The excluded active weight satisfies

\[
 \delta_{\rm load}\le(15/16)^{4L}+(625/768)^L
 <2(5/6)^L<2^{-255}.
 \tag{H18}
\]

The first term bounds vertex 0. The second follows from
`Pr(X>=L)<=3^(-L)(1+2p)^(4L)`. The inherited `B_old>=8192` makes `L`
more than sufficient for the final inequality. On the good vertices the
uniform sink-label mixture and normalized loader packet factor from the
old charged-head/entry-ready apparatus. Full-state trace distance to that
normalized packet comparison is at most `sqrt(delta_load)`. After tracing
only the new hot/sink/loader systems, the reduced old-apparatus error is at
most `delta_load`: the good loader positions are orthogonal to the vacuum
and final-loader positions of the excluded histories. This comparison does
not discard those histories from the physical state.

The old word has completed by main index `L`, hence by global vertex `2L`.
For `theta in [pi/3,2pi/3]`,

\[
 w_{\rm out}(t)=\Pr(X\ge2L),\qquad
 1-w_{\rm out}(t)\le(3/4)^{2L}=:\delta_{\rm out}.
 \tag{H19}
\]

Every such good history has the same output on the old fixed final row.
A mathematical full-space completion observable is

\[
 P_{\rm main,tail}=I-\prod_{r=L}^{3L}(I-n_{m_r}).
 \tag{H20}
\]

The range extends through `3L`; using only the predecessor's old sites
through `2L` would incorrectly reject the newly appended output tail.
The read projector is (H20) times the transported complete old read
predicate in the final row: its inherited completion latch AND acceptance
flag. This retains the earlier environmental factor `4/15` inside the
capture channel and excludes unfinished compiler flags. There is no new
pure read latch. The actual raw thermal defects can also fire (H20); their
entire contribution is included in the preparation-error estimates.

These are new continuous windows of (H13). They do not transfer the old
clock's physical times or its exact post-read retention claims. The old
row/funded gate word, preparation of its data, and completed channel are
preserved. A physical implementation of the read projector or a law for
individual observed outcomes is not supplied by the projector itself.

## 7. Actual thermal input and retained defect sectors

Put `Z_B=sum_(b=0)^(2R) z^b` and `r_c=z/(1+z)`. The probability that all
specified cold registers are in their reference ground configuration is

\[
 \alpha_c={1\over1+Dz}\,{1\over Z_B}\,(1-r_c)^{K+1}.
 \tag{H21}
\]

Its complementary weight obeys the union bound

\[
 1-\alpha_c\le Dz+{z\over1-z}+(K+1)z
 \le(D+K+3)z\le2^{-84}.
 \tag{H22}
\]

The total active-reference weight is `q=alpha_c q_h`, and

\[
 1-q\le(1-\alpha_c)+(1-q_h)<3\,2^{-84}<2^{-82}.
 \tag{H23}
\]

The actual state is exactly a retained convex mixture of: the `D` active
reference evolutions with total weight `q`; the dormant hot-ground cold
reference with weight `alpha_c(1-q_h)`; and the entire evolved cold-defect
state with weight `1-alpha_c`. No microscopic branch is declared to have
zero cost. Unitarity preserves this decomposition at every time.

It follows that reduced joint charging/loading error is at most
`1-q+delta_load` relative to the central old ready state. A full packet
comparison uses `1-q+sqrt(delta_load)` instead. Comparison to the
predecessor's slightly mixed charged work/polarized cursor product adds its
explicit old seed distance. The subsequent channel/error estimates are
spelled out in [PREPARATION.md](PREPARATION.md); they retain both the cold
bad sectors and the old imperfect compression.

## 8. Inclusive generator energy and nonstationarity

For the actual input define the diagonal operator

\[
 A=\sum_{i=0}^{K-1}a_iD_i+\sum_{i=0}^{K}v_iQ_i,
 \qquad M=H_0+A,
 \qquad H=M-\sum_i a_i(X_i+X_i^{\dagger}).
 \tag{H24}
\]

The exact whole-state energy moments are finite expressions

\[
 \langle H\rangle=\langle M\rangle,
\]
\[
 \operatorname{Var}(H)=\operatorname{Var}(M)
       +\sum_i a_i^2\langle X_i^{\dagger}X_i+X_iX_i^{\dagger}\rangle.
 \tag{H25}
\]

Expectations are with the full actual product of the thermal hardware and
the admitted logical/reference input. The logical block has fixed bare
charge. A hopping term has zero diagonal expectation. Two different edges
cannot return the same cursor/environment basis configuration in two hops,
so their cross terms vanish. A hop and return cancel their data unitaries.
This proves (H25), including thermal defects. Variance in `M` includes its
covariances; it is not replaced by the active path's variance `a_0^2`.

All factors are finite and explicit in [ENVIRONMENT.md](ENVIRONMENT.md): every
old row and work copy, the cold work distribution, the hot gap and
multiplicity, sink entropy, and every loader/main site contribute. The
physical interaction energy is included in `A` and the off-diagonal terms.
Its expectation and that of `H_0` are separately conserved by (H14).
A small defect probability alone does not justify dropping its energy.

There is still nonzero initial commutator with the coupled Hamiltonian.
For one reaction label define

\[
 p_{\rm in}={1\over(D+2)(1+Dz)Z_B(1+z)^2},\qquad
 p_{\rm out}=2z^{R+3}p_{\rm in}.
 \tag{H26}
\]

These are its actual local initial/final configuration probabilities.
Tracing the initial commutator over all other sites isolates the reaction
blocks: every other off-diagonal edge has a traced cursor endpoint. Thus

\[
 \|[H,\rho_{\rm in}]\|_1
 \ge2a_0D(p_{\rm in}-p_{\rm out})>0.
 \tag{H27}
\]

The bound uses trace-norm contraction on the Hermitian multiple of the
commutator and holds with mixed logical inputs and references. It is a
lower bound, not a statement that later bonds contribute no commutator.
The hot/cold occupation ratio is incompatible with detailed balance for
this coupled reaction. All inputs are diagonal in bare onsite energies,
but they are not stationary for the full `H`.

No further polarized master clock has been inserted. The reaction creates
both the old entry and the new loader excitation. The remaining assumptions
are the three specified thermal resource distributions, their product
preparation relative to the permanently coupled Hamiltonian, the manufactured
spectra/degeneracies, and the exact local interactions. A common Gibbs state
of `H_0` would be stationary because `[H,H_0]=0`; a Gibbs state of `H` would
also be stationary. This construction does not produce nonstationarity from
either state, nor derive the thermal contact or these additions from the
unmodified native TWIST-J dynamics.
