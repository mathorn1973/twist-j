# Joint preparation from a common-temperature bank

**Status: NON-CANONICAL, L1, conditional candidate-T.** This analytical
construction has not received independent mathematical acceptance. No new
scientific executable or gate-enumeration run was used.

The fixed target is the entire raw apparatus of
[PR #1764 at 6670ac27](https://github.com/mathorn1973/twist-j/tree/6670ac274888927be3429a463966da41ca8d2e8b/notes/C-THERMAL-WORK-CLOCK-BOOTSTRAP-N).
Its source, spectral and accepted-channel premises remain inherited
conditions. The present proof uses the complete Hamiltonian and compiler
specified in [HAMILTONIAN.md](HAMILTONIAN.md), and the resource/energy
account in [ENVIRONMENT.md](ENVIRONMENT.md). It does not infer a joint input
from agreement of separate marginals.

## 1. The actual input and the only nonthermal resource

Fix beta_0 epsilon=log 2. Every nonlogical information site, donor,
transport-row site, unused head, counter and cursor starts in its Gibbs
state at this one inverse temperature for its actual fixed onsite spectrum.
The admitted logical state has its inherited fixed-charge code and an
arbitrary passive reference. It is not consumed as cooling fuel.

There is one exception: a fuel qubit f with gap 2Q epsilon+2Delta has the
full-rank diagonal input

\[
 \rho_f=\delta_f|0\rangle\langle0|
       +(1-\delta_f)|1\rangle\langle1|,\qquad
 \delta_f=2^{-96}.                                  \tag{P1}
\]

This population inversion is a supplied nonequilibrium resource. It is
not a positive-temperature Gibbs state, and it is not produced by the
program whose operation it enables.

Use the finite counts of HAMILTONIAN.md. Each row has N information cells,
N physical counter copies of dimension N+1, and work cells with levels
0,...,4Q. There are J+1 physical rows, with J=J_p+J_T. Only one
distinguished counter must be initialized at zero for
the promised compiler action; all other counters are restored by routing
and may contain their Gibbs junk. The line width is W=3N. With the actual
primitive counts J_p,J_T, choose

\[
 B\geq\max\{J_p(W+3)-1,J_T(W+3)-1,8192\},\quad
 L=4B,\quad K=4L=16B,                              \tag{P2}
\]
\[
 \ell=96+\lceil\log_2(K+2)\rceil,\qquad
 \Delta=\ell\epsilon,\qquad
 Q=\max\{128,Q_{\rm info}+N^2\ell\}.               \tag{P3}
\]

The unfunded information dimensions and primitive counts are fixed before
ell is chosen. Q then bounds the energy of all information and counter
cells in units epsilon. The genuine physical work dimension 4Q+1 can grow
without introducing another compiled information register.

Every outer main/loader cursor qubit has gap Delta. Every counter has
spectrum 0,Delta,...,N Delta. Their small ground-state error follows from
the high physical gap at beta_0, not a separately supplied cold temperature.
The main sites are m_0,...,m_(3L), and the loader has t_0,...,t_(L-1):
there are K+1 such cursor qubits.

The distinguished work head also starts at beta_0, with probabilities
proportional to 2^(-b) on b=0,...,4Q. The local launch exchanges

\[
 |1,b,0,0\rangle_{f,\mathcal W,m_0,t_0}
 \longleftrightarrow
 |0,b+2Q,1,1\rangle_{f,\mathcal W,m_0,t_0},
 \qquad 0\leq b\leq Q.                            \tag{P4}
\]

The fuel energy exactly pays for the head increase and two Delta
excitations. After a good launch f is ground and later gates leave it
untouched. The same legal path can reverse and reabsorb the excitation;
there is no second independent forward launch on that path.

Let q_new be the weight of the component with excited fuel, initial head
b<=Q, distinguished counter zero, and all new main/loader sites empty.
Writing s=2^(-ell), its exact weight is

\[
 q_{\rm new}
 =(1-\delta_f)
  \frac{\sum_{b=0}^{Q}2^{-b}}{\sum_{b=0}^{4Q}2^{-b}}
  \frac1{\sum_{c=0}^{N}s^c}(1+s)^{-(K+1)}.          \tag{P5}
\]

The head's excluded tail is less than 2^(-Q); the distinguished counter's
excitation probability is less than s, independently of N; each cursor
excitation probability is less than s. Hence

\[
 \eta_{\rm new}:=1-q_{\rm new}
 <2^{-96}+2^{-Q}+(K+2)2^{-\ell}<3\,2^{-96}.         \tag{P6}
\]

All excluded head, counter and cursor sectors remain under the same raw
Hamiltonian. The decomposition into a nominated component and its
complement is an exact decomposition of the input density operator, not
an implemented measurement or discarded failure branch.

## 2. Paid swaps produce the complete old thermal product

Let A denote the complete old #1764 apparatus. Initially its nonlogical
sites are Gibbs at beta_0 for their actual old onsite energies. Prepare the
following independent donors at that same beta_0, using the displayed
fixed spectra. The desired old cold exponent b_old, old central level
R_old and degeneracy D_old are the immutable predecessor's parameters.

| Old target spectrum | Donor spectrum at beta_0 | Target distribution after SWAP |
| --- | --- | --- |
| Hot manifold, gap (R_old+3)epsilon with degeneracy D_old | same degeneracy, gap epsilon | the old hot Gibbs state |
| Cold entropy sink, gap epsilon with degeneracy D_old | same degeneracy, gap b_old epsilon | the old cold Gibbs state |
| Old distinguished head, levels j epsilon, 0<=j<=2R_old | levels j b_old epsilon | the old cold head Gibbs state |
| Each old main/loader qubit, gap epsilon | gap b_old epsilon | the old cold cursor Gibbs state |

All other old information factors already have the required moderate
Gibbs input and are left unchanged. The logical input and its reference
are left intact. These are different physical donor gaps, not a change
of temperature label for the target Hamiltonian. Each unequal-gap SWAP is
funded, and every displaced target state stays in its donor site.

Let P be the product of these swaps, with the routing and explicit-counter
qudit construction specified in HAMILTONIAN.md. The distinguished counter
returns to zero after each completed fully controlled gate or basis-phase
macro. On that initialized
counter subspace, the completed preparation acts as the exact permutation
P on the information registers. No corresponding promise for an arbitrary
initial counter value is assumed.

For every nominated initial head value b in (P5), launch gives b+2Q.
For a payload energy e in [0,Q], the complete payload/head charge lies in
[2Q,4Q], inside complete sectors of the work ladder. Every funded gate
therefore agrees with the same global lift throughout the word. Its head
level after a prefix is

\[
 b+2Q+e_{\rm initial}-e_{\rm current}.              \tag{P7}
\]

The range is contained in [Q,4Q]. This is a uniform bound in b and in the
input state, rather than a per-gate approximation.

For an explicit joint-state proof, write x for the original target values,
y for the independent donor values, and let p(x),d(y) be their diagonal
Gibbs weights. Suppress untouched factors and denote the total information
energy before and after their swaps by E(x,y) and E(y,x), in units epsilon.
On the buffered component the completed funded permutation has the action

\[
 |x,y,0,b+2Q\rangle
 \longmapsto
 |y,x,0,b+2Q+E(x,y)-E(y,x)\rangle.                  \tag{P8}
\]

Thus the entire old apparatus, after tracing donors, work and helper
systems at the checkpoint, has exactly its specified joint input:

\[
 \boxed{\quad
 \operatorname{Tr}_{\rm new\ helpers}\rho_{\rm after\ P}
   =\rho_{1764,\rm in}(\rho_{\mathcal L R}).\quad} \tag{P9}
\]

Indeed, for each b, tracing the orthogonal old-value records x and the
normalized work record leaves sum_y d(y)|y><y| on the targets. This is the
product of their prescribed old Gibbs factors, independent of the
unchanged admitted logical/reference state. The mixture over b cannot
reweight y. The same argument applies to all target sites together;
(P9) is not obtained by multiplying separately derived marginals.

The full state need not be a product of the old apparatus with donors and
work. Its work level records the energy transfer in (P8), and all such
correlations remain physical. The bound is uniform in the logical
reference admitted by the inherited input contract. A purification of
the thermal bank, if added, has its own retained donor/reference
correlations and is not silently identified with that logical reference.

## 3. Correlated work needs no energy coherence for this endpoint

Let H_old be the entire raw-space Hamiltonian pinned in #1764, and let
its exact endpoint time be tau_old. The target operator is

\[
 T=\exp(-i\tau_{\rm old}H_{\rm old}/\hbar)
       \otimes I_{\rm new\ donors}.                \tag{P10}
\]

It includes every old thermal defect sector. It is not a legal-history
reflection with an arbitrary complement substituted for the old dynamics.
Its finite exact matrix entries are specified by (P10); a claim that every
entry is algebraic is unnecessary and is not made.

The pinned law conserves the old additive bare Hamiltonian, so
\( [T,H_{{\rm old},0}]=0 \). Equivalently every nonzero target-energy
matrix element of T
connects equal bare energies. The compiler's promised counter identity is

\[
 U_T(|\psi\rangle\otimes|0\rangle_C)
       =(T|\psi\rangle)\otimes|0\rangle_C.         \tag{P11}
\]

Its extension on other counter inputs need not commute with payload
energy. On the initialized-counter subspace, however, the completed
funded lift of (P11) has zero net head shift. Therefore it acts exactly
as T on the old apparatus and as the identity on the work factor, even
when those factors are correlated by (P8). Tracing the idle donors/work
before or after this completed action gives the same reduced old output.

No coherence between different work-energy levels is needed. P is a
basis permutation of diagonal Gibbs inputs, so energy records do not
change its desired reduced distribution. T preserves old bare energy,
so it creates no new work-energy record. Coherence within the admitted
logical and degenerate-energy sectors, including reference correlations,
is preserved by the same argument.

The new autonomous Hamiltonian compiles (P10) as an endpoint word. It
replaces the old interactions during this experiment; it does not assert
an unchanged old continuous trajectory beginning at an externally sharp
handoff time. All actual initial factors commute with the new additive
H_0, including the diagonal fuel and the logical fixed-charge block.
Since the complete new law conserves H_0, its free density phases cancel
throughout the physical-time statements below.

## 4. The preparation window is a joint physical statement

After thermal launch, a guarded loader holds the charged head and entry
before handing off to the new main program. The preparation P completes
by main index B. The main histories B,...,3B hold the same complete
prepared row, including donors, work and their correlations. T completes
by main index L=4B. Global history is offset by the loader length L;
therefore the good preparation indices are 5B<=j<=7B, and complete output
begins at j=8B=K/2.

On the nominated component, X distributed as Bin(16B,p), where
p=sin^2 theta and theta=gt/[hbar(K+1)], denotes the exact history norm
weights. Choose the first rising interval

\[
 \frac{23}{64}\leq p\leq\frac{25}{64}.             \tag{P12}
\]

Markov bounds using (4/5)^X and (5/4)^X give

\[
 \Pr(X<5B)\leq
   \left[(5/4)^5(297/320)^{16}\right]^B,
\]
\[
 \Pr(X>7B)\leq
   \left[(4/5)^7(281/256)^{16}\right]^B.            \tag{P13}
\]

Both bracketed bases are below 31/32. For the first use
(297/320)^4<3/4 and (5/4)^5(3/4)^4=253125/262144<31/32.
For the second use (281/256)^4<16/11 and
(4/5)^7(16/11)^4<31/32. These are exact integer comparisons. Thus

\[
 \delta_{\rm prep}:=\Pr(X<5B)+\Pr(X>7B)
 <2(31/32)^B<2^{-255}.                              \tag{P14}
\]

The final inequality uses B>=8192 and (31/32)^32<1/2.

Within these histories the full new data state is identical, so the
normalized history packet factors from that state. Tracing the new main
and loader cursors removes cross-history terms. Using (P9), and then
restoring every excluded input component, proves the joint reduced bound

\[
 \boxed{\quad
 D(\rho_{\rm old,red}(t),\rho_{1764,\rm in})
 \leq\eta_{\rm new}+\delta_{\rm prep}.
 \quad}                                                       \tag{P15}
\]

Trace distance is one half of the trace norm. The output in (P15) is the
whole old apparatus and its logical reference in the fixed preparation
row. It includes the old hot site, cold sink, old work and every old
cursor jointly. No independence from the new work/donor trash is claimed.
A full normalized-packet comparison instead costs sqrt(delta_prep).
No physical selection is performed in deriving (P15).

## 5. Direct composition and the complete read predicate

Let Pi_old be the complete physical read projector of the pinned #1764
apparatus at its endpoint. It includes that apparatus's extended main-tail
projector and its inherited #1758 completion latch AND accepted flag.
Transport every one of these factors to the final information row.
For the new outer main cursor define

\[
 \Pi_{\rm outer,tail}=I-\prod_{r=L}^{3L}(I-n_{m_r}),\qquad
 \Pi_{\rm read}=\Pi_{\rm outer,tail}\Pi_{\rm old}.   \tag{P16}
\]

The new outer tail is a different register from the old main-tail factor
inside Pi_old. Both are retained. The complete raw projector can fire on
bad new input sectors; their total initial weight is eta_new and is
included below.

For theta in [pi/3,2pi/3], the completed-tail weight satisfies

\[
 w(t)=\Pr(X\geq8B),\qquad
 1-w(t)\leq(3/4)^{8B}=:\delta_{\rm out}<2^{-255}.   \tag{P17}
\]

Let sigma_1764 be the actual subnormalized accepted physical/reference
output of the pinned old apparatus at tau_old, with its specified thermal
input. It includes all of that note's thermal and imperfect-compression
components. Tracing the retained new helper systems gives the exact
unconditional decomposition

\[
 \sigma_{\rm new,acc}(t)
   =q_{\rm new}w(t)\sigma_{1764}
       +\sigma_{\rm new,bad}(t),\qquad
 \sigma_{\rm new,bad}(t)\geq0,\quad
 \operatorname{tr}\sigma_{\rm new,bad}(t)\leq\eta_{\rm new}.
                                                               \tag{P18}
\]

This uses (P9)-(P11) and the complete unmeasured history. It does not
compose an imagined postselection at (P15) with an independently running
old apparatus. The reductions and read projectors are mathematical
comparison maps, not newly implemented detector operations.

For the comparison with the ideal inherited capture channel, retain the
old cold-launch error eta_old<2^-82 and its readiness compression error
xi<2^-80. A conservative common budget for old and new window comparisons is

\[
 \varepsilon_{\rm total}
 =\xi+\eta_{\rm old}+\eta_{\rm new}
       +\delta_{\rm old,load}+\delta_{\rm old,out}
       +\delta_{\rm prep}+\delta_{\rm out}
 <2^{-78}.                                         \tag{P19}
\]

The two old history errors are each below 2^-255. They can be omitted for
an exact endpoint comparison, but retaining them makes this common bound
more conservative. No seed or reference error is silently set to zero.

For an accepted trace-nonincreasing map, outputs A,A_i of weights p_a,p_i
from normalized inputs at distance at most varepsilon obey

\[
 \frac{\|A-A_i\|_1+|p_a-p_i|}{2}\leq\varepsilon,
 \qquad D(A/p_a,A_i/p_i)\leq\frac{\varepsilon}{p_i}.
                                                               \tag{P20}
\]

Append a one-dimensional reject record and apply trace-distance
contractivity, then normalize by the triangle inequality. This proves
(P20) with arbitrary admitted logical references and includes false
acceptance in all bad sectors.

At the old exact endpoint the ideal comparison has the inherited
activation weight q_0=4/15, without an old clock-window loss. The new tail
has w(t)>99/100. Using the fixed margins

\[
 p_0=\frac25\frac{1024}{15625}\frac{99}{50000},\qquad
 u_0<\frac{50000}{99\,2^{29}}<\frac{19}{20\cdot10^6},
\]
\[
 p_i>\frac4{15}\frac{99}{100}p_0
   =\frac{418176}{30517578125}
   >\frac1{75000}+\frac1{3000000},                 \tag{P21}
\]

(P19)-(P21) imply for the actual complete new input

\[
 \boxed{\quad p_{\rm acc}>\frac1{75000},\qquad
 D(\rho_{\rm acc},\rho_{\rm acc}^{\rm ideal})
    <75000\,2^{-78}<\frac1{20\cdot10^6},\qquad
 u_{\rm acc}<\frac1{10^6}.\quad}                   \tag{P22}
\]

The final inequality follows by measuring the unwanted-output projector
and adding the trace-distance error to u_0. These are exact rational
margins, not rounded estimates. The ideal occupied-memory/reference SWAP
and receiver record remain comparison identities; their actual versions
have the error (P22) and must not be reported as exact. No old post-read
retention interval is automatically inherited by the new Hamiltonian.

## 6. The stationary boundary has not disappeared

All nonlogical hardware except the single fuel qubit is initially Gibbs
at beta_0 for its own fixed onsite Hamiltonian. High gaps make the new
counters and cursor sites nearly empty at that same temperature. Scaled
donor spectra provide the desired old Gibbs populations only after the
paid state transfers. The changed temperatures are therefore derived as
a joint reduced output, with energy and retained entropy accounted for;
they are not separately supplied cold or hot density operators.

The initial fuel inversion, manufactured gaps and degeneracies, exact
couplings, and initial product/contact condition remain inputs. Fuel has
no bare-energy coherence, but its non-Gibbs populations create full-H
nonstationarity across the energy-conserving launch. For a paired launch
configuration the reverse-to-forward initial-weight ratio is

\[
 \frac{\delta_f}{1-\delta_f}\,2^{-2Q-2\ell},       \tag{P23}
\]

independently of b. The resource proof gives the corresponding energy,
entropy and commutator account. No work is inferred from equilibrium alone.

If the fuel were also Gibbs at beta_0 and the complete admitted input
were Gibbs for H_0, then [H,H_0]=0 would imply [H,exp(-beta_0 H_0)]=0.
That state would be stationary. More generally any [H,rho_in]=0 forbids
change under the same fixed closed H. The nonthermal fuel avoids this
hypothesis; it does not disprove it. Preparing that inversion from a
stationary whole, resetting the used apparatus with records retained,
and implementing the specified material couplings remain open.