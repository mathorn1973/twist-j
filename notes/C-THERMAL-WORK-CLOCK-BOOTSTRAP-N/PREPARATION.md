# Joint thermal preparation of the work head and the old master cursor

**Status: NON-CANONICAL, L1, conditional candidate-T.** This is an analytical
candidate with no new scientific execution or independent acceptance.
The physical law and raw-space completion are in
[HAMILTONIAN.md](HAMILTONIAN.md); the initial Gibbs states and energy account
are specified in [ENVIRONMENT.md](ENVIRONMENT.md).

The immutable predecessor is
[PR #1761 at 32c17259](https://github.com/mathorn1973/twist-j/tree/32c17259c4baf40bb6d08b521adc642956b57e94/notes/C-THERMAL-REGISTER-PREPARATION-N).
Its source, spectral and accepted-channel premises remain conditional on
[the forward-only candidate at 01acc42](https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md).
This note proves a joint preparation statement, not an inference from two
separate reduced marginals.

## 1. Full-rank thermal inputs and the retained good component

Keep the predecessor's physical work head with levels 0,...,2R and
Hamiltonian epsilon times its level. Its old master cursor has a completed
program at history L=4B_old and original length 2L. Extend its identity tail
to main sites m_0,...,m_(3L), and add loader sites t_0,...,t_(L-1). The new
active path has K=4L edges. There are K+1 cold main/loader cursor qubits.
The inherited B_old >= 8192 implies L >= 32768.

Introduce a hot system h with one ground state and D degenerate excited
states |a>, 1<=a<=D, of energy (R+3)epsilon. Introduce a cold sink c with
one ground state and D degenerate excited states of energy epsilon. Put

\[
 D=2^{84},\qquad
 b=84+\lceil\log_2(D+K+3)\rceil,\qquad z=2^{-b}.
                                                               \tag{P1}
\]

The hot inverse temperature obeys beta_h(R+3)epsilon=log 2. Its ground
weight is 2/(D+2) and each excited-state weight is 1/(D+2). The sink c,
the original work head, and every main/loader cursor qubit have the same
cold inverse temperature beta_c epsilon=b log 2. In particular none of
these cursor sites is supplied with an initial population inversion.
All these Gibbs density operators have full rank on their physical spaces.

The original payload, unused rows, and other head cells retain their
predecessor's common-temperature inputs at beta_0 epsilon=log 2. The only
arbitrary quantum input is the admitted fixed-charge logical code and its
passive reference. Thermal inputs are independent of that logical/reference
state. Thus three temperatures and the new level degeneracies are explicit
resources. They are not derived from the unchanged native law.

Let Q_good select an excited hot state, c in its ground state, the original
head in level zero, and every main/loader cursor in its ground state.
It is used to decompose the supplied density operator, not as an implemented
selection. Its exact weight is

\[
 q=\frac{D}{D+2}\frac1{1+Dz}
      \frac{1-z}{1-z^{2R+1}}(1+z)^{-(K+1)}.          \tag{P2}
\]

A union bound gives

\[
 \eta_{\rm th}:=1-q
 \leq\frac2{D+2}+(D+K+2)z
 <3\,2^{-84}<2^{-82}.                              \tag{P3}
\]

The work-head excitation probability is at most z, since its finite
geometric partition sum is at most 1/(1-z). The sink excitation probability
is at most Dz, and each cursor excitation probability is at most z.
These facts prove (P3) without treating the ladder as a two-level system.

The complete initial state and its evolution therefore have the exact
convex decompositions

\[
 \rho_{\rm in}=q\rho_{\rm good,in}+(1-q)\rho_{\rm bad,in},\qquad
 \rho(t)=q\rho_{\rm good}(t)+(1-q)\rho_{\rm bad}(t). \tag{P4}
\]

Every term follows the same Hamiltonian. All non-ground cold states, all
multiple-cursor sectors and the hot ground component are retained. No
claim that every bad component is dormant or rejected is needed.

## 2. The actual old head and cursor are prepared together

For each hot label a, the launch interaction is the resonant exchange

\[
 |a,0,0,0,0\rangle_{h,c,B,m_0,t_0}
 \longleftrightarrow
 |0,a,R,1,1\rangle_{h,c,B,m_0,t_0}.                 \tag{P5}
\]

Both sides have bare energy (R+3)epsilon. The sink stores a; different hot
labels have orthogonal output records. This is not an erasure of the hot
system's entropy. It charges the original work head and creates the
original master entry excitation as well as the new loader excitation.

The last loader hop is controlled by the old entry occupation, and the
old first master hop is controlled by occupation of the last loader site.
On Q_good the reached configurations form the following single path for
each a, with the same gate-labelled amplitudes:

- j=0: h carries a, c is ground, the head is zero, and all cursors are empty;
- 1<=j<=L: h is ground, c carries a, the head is R, m_0 is occupied,
  the remaining main cursor is empty, and t_(j-1) is occupied;
- j=L+r, 1<=r<=3L: the loader occupies its last site, the main cursor is
  at m_r, and the original program has applied its first r instructions.

In the last line the completed program is followed by its identity tail.
This is the gate word of the predecessor with retuned clock coefficients
and a controlled handoff. It is not the predecessor's unchanged Hamiltonian
acting independently after a separate external preparation step.

Let rho_DR denote the original payload, all other original rows/heads,
and the logical reference, excluding the distinguished head B and the
main cursor. On every history 1<=j<=L-1, that entire state is unchanged.
The old program has not begun, the last loader control is zero, and the
joint old target is exactly

\[
 \Omega_{\rm old}
 =|R\rangle\langle R|_B\otimes
   |1,0,\ldots,0\rangle\langle1,0,\ldots,0|_m
       \otimes\rho_{DR}.                          \tag{P6}
\]

Here m includes the added main-tail sites, all of which are empty.
Equation (P6) includes the reference and the joint head/cursor/payload
state. Its proof is the identical action of every good history on all
these factors. Product independence is not deduced from their marginal
states alone.

All stated physical initial densities commute with the additive H_0:
thermal factors are energy diagonal and the logical code has fixed charge.
Since [H_0,H_prop]=0, the free H_0 evolution cancels at the density-operator
level. The unchanged rho_DR in (P6) has precisely this input scope; it is
not an assertion for arbitrary cross-energy coherent hardware.

## 3. A finite window with a joint readiness bound

Write theta=gt/[hbar(K+1)] and p=sin^2 theta. The exact good-component
history weights are those of X distributed as Bin(4L,p). Use the first
rising interval with p in [1/16,1/8]. The good preparation indices are
1<=X<=L-1. Their excluded weight beta_load satisfies

\[
 \begin{split}
 \beta_{\rm load}(t)
   &=\Pr(X=0)+\Pr(X\geq L),\\
 \beta_{\rm load}(t)
   &\leq(15/16)^{4L}+(625/768)^L
    =:\delta_{\rm load}<2(5/6)^L<2^{-255}.
 \end{split}                                                   \tag{P7}
\]

For the upper tail, apply Markov's inequality to 3^X:
3^(-L) E(3^X)=3^(-L)(1+2p)^(4L)<=(625/768)^L.
The other term is (1-p)^(4L). Both bases, (15/16)^4 and 625/768, are less
than 5/6. Since (5/6)^4<1/2 and L>=1024, the last strict bound follows.

Let |chi(t)> be the normalized superposition of loader positions
0,...,L-2 with the good history amplitudes. Projection and normalization
of the good-component state onto these histories gives exactly

\[
 \rho_{\rm packet}(t)
 =|0\rangle\langle0|_h\otimes
     \frac1D\sum_{a=1}^D|a\rangle\langle a|_c
       \otimes|\chi(t)\rangle\langle\chi(t)|_t
       \otimes\Omega_{\rm old}.                  \tag{P8}
\]

The common amplitude profile is independent of a and of the admitted
logical input. Equation (P8) proves the joint factorization, including the
retained label record. An external purification of the thermal hot input,
if added, would retain its correlations with c and must not be replaced by
the product form for that larger reference. The logical reference in the
present contract is retained throughout.

With D(rho,sigma)=||rho-sigma||_1/2, a normalized full-state comparison obeys

\[
 D(\rho_{\rm good}(t),\rho_{\rm packet}(t))
       \leq\sqrt{\beta_{\rm load}(t)}.             \tag{P9}
\]

This follows from the overlap sqrt(1-beta_load) on a pure component and
convexity for the admitted mixture. No projection is physically performed.
The full actual state is within eta_th+q sqrt(delta_load) of (P8); if its
actual bad component is instead kept unchanged in the comparison mixture,
the bound is q sqrt(delta_load).

There is a stronger bound for the required joint old target. Trace only
the new h,c and loader from the full state, keeping B, every main cursor
site, the original payload and its logical reference. Good loader positions
0,...,L-2 are orthogonal to all bad-history loader configurations: the
vacuum at j=0 and the last loader site at j>=L. This trace therefore removes
all good/bad-history cross terms. Every good history leaves exactly (P6).
Consequently

\[
 \boxed{\quad
 D(\rho_{\rm old,red}(t),\Omega_{\rm old})
 \leq(1-q)+q\beta_{\rm load}(t)
 \leq\eta_{\rm th}+\delta_{\rm load}.
 \quad}                                                       \tag{P10}
\]

This is an unconditional joint preparation bound. It is not only a pair of
head and cursor marginal bounds, and it does not use independence inferred
from those marginals. It preserves correlations of the original logical
state with its reference.

The predecessor supplied mixed head/cursor seeds concentrated near the
same ideal factor (P6), with errors eta_B^old and eta_C^old. If those exact
mixed seed distributions are chosen as a comparison instead, the triangle
inequality adds at most eta_B^old+eta_C^old to (P10). The present law does
not claim to manufacture those exact distributions; it derives an explicit
joint approximation to their intended central-head/entry configuration.

The local mathematical readiness predicate
|R><R|_B n_(m_0)(1-n_(t_(L-1))) selects just these histories on Q_good.
On the actual full-rank input it may have false positives from bad sectors.
Their total weight is at most eta_th, and the conditional joint-state error
is at most eta_th/[q(1-beta_load)]. This is a comparison instrument, not
an implemented measurement or an occurrence rule.

## 4. The complete output channel uses the unmeasured history

The old program completes at main position r=L, hence new history j=2L.
Use the extended main-tail projector

\[
 \Pi_{\rm main,tail}
   =I-\prod_{r=L}^{3L}(I-n_{m_r}).                  \tag{P11}
\]

The extension to r=3L is essential: the predecessor's shorter tail stopped
at 2L and would miss the newly appended output histories. Retain the full
old physical predicate on the final data row: L_1758 is its completion
latch and F_old its accepted flag. The new complete read projector is

\[
 \Pi_{\rm read}=\Pi_{\rm main,tail}\,L_{1758}F_{\rm old}.
                                                               \tag{P12}
\]

The factors commute. On the good component, (P11) rejects all loader and
unfinished-program histories. The inherited completion latch rejects the
inactive old environment sectors. The raw projectors may also fire on bad
thermal inputs; no such contribution is silently dropped.

For theta in [pi/3,2pi/3], the exact completed-tail weight obeys

\[
 w(t)=\Pr(X\geq2L),\qquad
 1-w(t)\leq(3/4)^{2L}=:\delta_{\rm out}<2^{-255}.
                                                               \tag{P13}
\]

This is the usual exponential binomial bound at p>=3/4. The new read
window is governed by this new Hamiltonian, not by an old native-memory
interval.

Let sigma_th be the accepted physical/reference output of the complete
predecessor word when its distinguished head is exactly central and its
master cursor starts at the entry, with the original moderate-temperature
payload and rows. This includes the predecessor's reversible majority
preparation and its retained error xi<2^-80. Let D_out be the inherited
mathematical output reduction, also tracing the new thermal launch systems
and loader. On the actual full input there is the exact decomposition

\[
 \mathcal D_{\rm out}[\Pi_{\rm read}\rho(t)\Pi_{\rm read}]
    =q\,w(t)\,\sigma_{\rm th}+\sigma_{\rm bad}(t),
 \qquad \sigma_{\rm bad}(t)\geq0,\quad
 \operatorname{tr}\sigma_{\rm bad}(t)\leq1-q.       \tag{P14}
\]

The good output does not depend on which hot label a was transferred to c.
All accepted and rejected preparation histories remain physical systems;
D_out only defines the output comparison. It is not an added decoder gate.

Equation (P14) follows directly from the exact complete path, without a
read or collapse in the preparation window. One must not compose a
hypothetically postselected state from (P8) with an independently running
old clock to obtain this output.

## 5. Error after acceptance and retained thresholds

For an ideal comparator, replace the initial hot/cold launch mixture by
its normalized good component and replace the predecessor's cooled old
readiness pattern by its ideal pattern. Its accepted output is

\[
 \sigma_i(t)=w(t)q_0\sigma_{\rm cap}^{\rm ideal},
 \qquad q_0=\frac4{15},                            \tag{P15}
\]

where sigma_cap^ideal is the pinned forward-only accepted physical/reference
channel. The first replacement costs at most eta_th in input trace
distance, and the second costs xi on the reduced old apparatus. Its work
and garbage are subsequently idle for the charge-preserving endpoint
operator, as proved in the predecessor. Thus the accepted instrument,
including its reject record, differs by at most xi+eta_th. A common
conservative budget also covering the preparation-window comparison is

\[
 \varepsilon
   =\xi+\eta_{\rm th}+\delta_{\rm load}+\delta_{\rm out}
   <2^{-79}.                                       \tag{P16}
\]

There is no remaining supplied mixed-clock or mixed-work seed error in
the good component. Their role has been replaced by the actual thermal
launch error eta_th, including every retained cold defect and hot-ground
input.

For completeness, a fixed trace-nonincreasing accepted map with outputs
A,A_i and weights p_a,p_i from normalized inputs at distance at most
varepsilon satisfies

\[
 \frac{\|A-A_i\|_1+|p_a-p_i|}{2}\leq\varepsilon,
 \qquad
 D(A/p_a,A_i/p_i)\leq\frac{\varepsilon}{p_i}.       \tag{P17}
\]

Append a one-dimensional reject record to prove the first inequality by
trace-distance contractivity; the triangle inequality after normalization
proves the second. The proof is uniform in the logical reference. It
includes false accepted flags from bad thermal sectors.

The inherited exact margins are

\[
 p_0=\frac25\frac{1024}{15625}\frac{99}{50000},\qquad
 u_0<\frac{50000}{99\,2^{29}}<\frac{19}{20\cdot10^6}.
                                                               \tag{P18}
\]

Since (P13) gives w(t)>99/100,

\[
 p_i>p_{\rm floor}:=\frac4{15}\frac{99}{100}p_0
 =\frac{418176}{30517578125},\qquad
 p_{\rm floor}-\frac1{75000}>\frac1{3000000}.       \tag{P19}
\]

Therefore, for the actual full-rank thermal input,

\[
 \boxed{\quad p_{\rm acc}>\frac1{75000},\qquad
 D(\rho_{\rm acc},\rho_{\rm acc}^{\rm ideal})
 <75000\,2^{-79}<\frac1{20\cdot10^6},\qquad
 u_{\rm acc}<\frac1{10^6}.\quad}                   \tag{P20}
\]

For the success inequality subtract (P16) from (P19). For selectivity,
any projector's expectation changes by at most trace distance; add the
middle bound of (P20) to (P18). All comparisons are exact integer
inequalities. For example 75000*(20*10^6)<2^17*2^25<2^79.

The ideal accepted logical label/occupied-memory SWAP remains the reference
channel. The actual SWAP and receiver record have the error (P20), including
arbitrary logical references; they are not exact identities for the full
thermal input. No previous post-read retention interval is transferred to
this new Hamiltonian without a separate argument.

## 6. What has been prepared and what remains supplied

The original charged work head and original entry-polarized clock are now
outputs of the local resonant launch and loader motion, with the joint
bound (P10). No initially charged work head or initially inverted new
cursor is supplied. The cold hardware is genuinely finite-temperature and
full rank; its defects contribute to eta_th rather than being assigned
zero amplitude.

The new inputs are nevertheless nonequilibrium resources: three positive
temperatures, a large finite degeneracy, a cold entropy sink, manufactured
gaps, and the fixed interacting law. A nearly certain hot excitation comes
from its degeneracy, not a negative temperature. The label transferred to c
retains the corresponding entropy. The energy of the interaction and every
cold defect is part of the companion energy account.

The complete input commutes with its additive bare energy but generally
not with the full interacting Hamiltonian. On a paired launch configuration,
the reverse-to-forward Gibbs-weight ratio is exactly 2z^(R+3), which is
strictly below one. The specified thermal contrast therefore supplies a
nonzero population imbalance across the fixed resonant coupling. It is not
created from a globally stationary state.

If all physical factors were Gibbs at one common inverse temperature for
H_0, then [H,H_0]=0 would imply [H,exp(-beta H_0)]=0. That complete input
would not run. A Gibbs state of the full H is stationary as well. No finite
unitary turns a complete full-rank input into an exactly pure target; the
present statement remains approximate. Production of the temperature
contrast, the finite gap/degeneracy architecture, and an eventual reset
with records retained are not derived by this construction.
