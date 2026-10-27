# Finite thermal preparation and conditional-output error

**Status: NON-CANONICAL, L1, candidate-T.** This is an analytical candidate,
not an independent acceptance or an occurrence law. The construction uses the
local static Hamiltonian in [HAMILTONIAN.md](HAMILTONIAN.md). Resource and
energy preparation are specified in [RESOURCES.md](RESOURCES.md).
No scientific executable was run to obtain the inequalities below.

The inherited physical channel is the one in
[PR #1758 at its immutable input](https://github.com/mathorn1973/twist-j/blob/243379459e3c7493368473cbae1a17eb99ee8316/notes/C-ENVIRONMENT-SOURCE-PREPARATION-N/PREPARATION.md).
Its capture and selectivity premises remain conditional on
[the forward-only candidate](https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md).
The present proof does not independently accept that complete source or
spectral argument. Public main remains the authority at
[`892a0b1`](https://github.com/mathorn1973/twist-j/tree/892a0b11089d34e241e1eb76d2c03247022d18e6).

## 1. What finite full-rank inputs cannot do exactly

Let a closed finite preparation have input density matrix rho on
H_T tensor H_E, with dimensions d_T and d_E. Suppose rho is strictly
positive on this declared physical Hilbert space. For every unitary U,
U rho U* is strictly positive, and so is its reduced state on T. In
particular, a nontrivial target cannot become exactly pure.

More quantitatively, write the eigenvalues of rho in decreasing order as
lambda_1,...,lambda_(d_T d_E). A nominated pure-target projector has rank
d_E. Expanding a rank-d_E projector in an eigenbasis gives coefficients in
[0,1] whose sum is d_E. Therefore, for every U,

\[
 \operatorname{tr}\big[(|0\rangle\langle0|_T\otimes I_E)U\rho U^*\big]
 \leq\sum_{i=1}^{d_E}\lambda_i,
 \qquad
 1-p_0\geq\sum_{i>d_E}\lambda_i>0.                 \tag{P1}
\]

This is an unconditional unitary statement. A selected outcome of a
nonunitary instrument has different premises. A pure fuel state, an exact
code-support promise, or an omitted pure controller also changes the
premises and must be counted as an additional resource. Full rank on an
abstract code is not full rank on a larger raw implementation.

For comparison, if n maximally mixed dirty qubits are initially independent
of a finite sink E, exact reset also requires
log(dim E)-S(rho_E) >= n log 2: unitarity preserves the joint entropy, and a
pure target leaves all of it in E. This entropy-capacity statement has those
specific independence and maximally mixed-input hypotheses. It does not
supply an energy-only reset mechanism.

## 2. A finite common-temperature source of approximate readiness

Use one inverse temperature with beta epsilon = log 2. Independent Gibbs
qubits of gaps epsilon and 2 epsilon then have excitation probabilities
1/3 and 1/5. The environment preparation uses these two donor types to
populate the old gap-3-epsilon h register and gap-epsilon c register.
The gap-changing swaps are funded, and their donors, dirty-value records,
and work correlations remain in the physical system.

For each of the m >= 1 nominated basis-ready target bits, take a disjoint
ternary tree of gap-epsilon Gibbs bits. No logical input bit is reset.
The reversible three-bit permutation exchanges 100 and 011 and fixes the
other six basis strings. Its first output bit is the majority bit. For
independent excitation probability p,

\[
 f(p)=3p^2-2p^3,\qquad p_0=\frac13,\qquad p_1=\frac7{27}.
                                                               \tag{P2}
\]

The other two outputs are retained garbage. At each level use roots from
disjoint trees. Thus p_(r+1)=f(p_r), and, for r >= 1,

\[
 p_r\leq\frac13\left(\frac79\right)^{2^{r-1}}.       \tag{P3}
\]

Indeed f(p) <= 3p^2, and (P3) is equality at r=1 before this upper-bound
iteration. Let

\[
 b=\lceil\log_2m\rceil+80,\qquad
 k=3+\lceil\log_2b\rceil,\qquad N_{\rm th}=m3^k.
                                                               \tag{P4}
\]

These are finite integer specifications; N_th counts all initial cooling
bits, not only the retained roots. Since 2^(k-1) >= 4b and
(7/9)^4 = 2401/6561 < 1/2,

\[
 \xi:=1-(1-p_k)^m\leq mp_k
 <\frac{m}{3}2^{-b}\leq\frac13\,2^{-80}<2^{-80}.
                                                               \tag{P5}
\]

Complement a root when its target's nominated ready value is one, funding
that operation too. An equal-gap SWAP then places the root in the target
and moves the target's complete previous state to the former root wire.
For arbitrary dirty-register/reference correlations this is a reversible
transfer of information, not deletion. The majority operations and the
root complements occur before these dirty-target swaps and act on the
independent donor/work resources. Energy-changing primitives use the
funded implementation, not an uncharged majority gate.

With the good central work seed, the reduced prepared old apparatus is
exactly

\[
 \rho_{\rm prep,red}
 =\tau_h\otimes\tau_c\otimes\omega_{\rm ready}
       \otimes\rho_{\mathcal L R},\qquad
 \tau_h=\operatorname{diag}(2/3,1/3),\quad
 \tau_c=\operatorname{diag}(4/5,1/5).                \tag{P6}
\]

Here L denotes the retained logical input, R its arbitrary reference,
and omega_ready is the product of the complemented cooled-root
marginals. The reduction traces the old-value sinks, thermal garbage,
work and unused row registers. Initial dirty-target correlations with L R
are retained in those sinks; rho_(L R) is their original marginal.

To verify (P6), expand the independent thermal donors in their energy
basis. All preparation primitives are basis permutations with energy
records. Each donor string has the same probability before and after the
permutation. The new h,c values are the two independent donor values, and
each ready target receives its own tree root. Tracing old-value registers
kills off-diagonal old-value terms, while tracing the normalized work
records does not change any diagonal donor weight. Summing the old values
returns rho_(L R). The two environment replacements may retain correlations
with their donors and work; (P6) does not assert their absence globally.

In trace-distance convention D(rho,sigma)=||rho-sigma||_1/2, (P5)-(P6) give

\[
 D\!\left(\rho_{\rm prep,red},
 \tau_h\otimes\tau_c\otimes|\mathrm{ready}\rangle
  \langle\mathrm{ready}|\otimes\rho_{\mathcal L R}\right)=\xi.
                                                               \tag{P7}
\]

This probability bound, rather than its square root, applies to the stated
reduction. An external purification of the Gibbs donors is physically
preserved if supplied, but is not part of the comparison output L R in
(P6)-(P7). A global comparison retaining that purification need not have
error xi; a generic normalized good-subspace comparison has error sqrt(xi).
No factorized global thermal/work/garbage output is claimed.

## 3. The work and clock seed errors are explicit

Let the integer payload-energy range be 0,...,Q, take R_w=2Q, and use a
physical work qudit with levels 0,...,2R_w. Its specified seed is

\[
 \rho_B=(1-\eta_B)|R_w\rangle\langle R_w|
 +\frac{\eta_B}{2R_w}\sum_{n\ne R_w}|n\rangle\langle n|,
 \qquad \eta_B=\frac{2^{-80}}{Q+1}.                \tag{P8}
\]

The local dimension 2R_w+1 is a physical resource, not an implicit bounded
qubit dimension. The master cursor seed is a diagonal full-rank product
whose nominated one-cursor configuration has weight at least 1-eta_C,
where eta_C <= 2^-80. All other cursor sectors and work levels are kept.
Replacing both seeds by their nominated configurations changes the full
input trace distance by at most eta_B+eta_C, even with arbitrary logical
references. The same bound holds after the full dynamics or any fixed
instrument by contractivity.

For the good work seed, every funded primitive implements its intended
payload gate with the compensating work shift. At any prefix the work
level is R_w+e_initial-e_current, with both payload energies between zero
and Q. It therefore remains in [R_w-Q,R_w+Q], away from the ladder ends.
The funded word telescopes on this whole initial subspace, including
coherent superpositions of payload energies. No separate fresh battery
is assumed for successive gates.

Let P be the preparation word and T the charge-preserving extension of
the old complete endpoint channel specified in HAMILTONIAN.md. The old
legal-history part is its phase-adjusted reflection; the complement and
inactive sectors have the declared unitary extension. This implements the
old endpoint channel at the promised clean input, not its old time path.
Since [T,H_payload]=0, its funded action on all buffered sectors is exactly
T tensor I_B. Consequently previously created work/trash correlations do
not invalidate applying the reduced-state bound (P7) to T. Local boundary
extensions on bad work sectors are not presumed to be the identity or to
follow this telescoping formula.

For all physical-time statements below, retain HAMILTONIAN.md's admitted
input contract: nonlogical hardware is diagonal in its physical energy
basis, and the logical input has fixed bare charge, with an arbitrary
passive reference. Hence [rho_in,H_0]=0. Since [H_0,H_prop]=0, free evolution
by H_0 cancels at the density-operator level throughout the dynamics. The
broader dirty-reference algebra in (P6) does not silently extend this
physical-time contract to arbitrary cross-energy coherent hardware.

The master clock's low-entropy input distribution and the work seed (P8)
remain supplied resources. This prefix does not prepare its own initial
clock inversion. New row registers may start as full-rank Gibbs junk: the
complete transfer moves the active row and permutes the junk, without a
clean-row assumption.

## 4. A finite preparation window under the same Hamiltonian

Use the master schedule of HAMILTONIAN.md. Let B_pad be an integer at least
8192 and at least each compiled preparation and endpoint word length.
There are K=8B_pad cursor edges. Preparation is finished by history index
B_pad; histories B_pad,...,3B_pad hold the same complete prepared active
row. The endpoint word runs from 3B_pad to 4B_pad, followed by an identity
tail through 8B_pad. All helpers remain in the model.

For the nominated master/work seeds, the legal-history probabilities are
those of X distributed as Bin(8B_pad,p), where

\[
 p=\sin^2\theta,\qquad
 \theta=\frac{gt}{\hbar(8B_{\rm pad}+1)}.
                                                               \tag{P9}
\]

Take p in [3/16,1/4] on the first rising part of the oscillation. The good
preparation indices are B_pad <= X <= 3B_pad. Markov's inequality applied
to 2^(-X) and 2^X gives

\[
 \begin{aligned}
 \Pr(X<B_{\rm pad})&\leq
       [2(29/32)^8]^{B_{\rm pad}},\\
 \Pr(X>3B_{\rm pad})&\leq
       [(5/4)^8/8]^{B_{\rm pad}},\\
 \delta_{\rm pre}&\leq
       [2(29/32)^8]^{B_{\rm pad}}
       +[(5/4)^8/8]^{B_{\rm pad}}
       <2(31/32)^{B_{\rm pad}}<2^{-255}.
 \end{aligned}                                                 \tag{P10}
\]

The two bracketed bases are each less than 31/32 by integer comparison.
Also (32/31)^32 > 1+32/31 > 2, so (31/32)^32 < 1/2;
B_pad >= 8192 = 32*256 proves the last strict inequality.

Within the good indices the full normalized history state factors into
one cursor packet and the same completed preparation output, with its
work and garbage correlations. There is no physical postselection in
this statement. Tracing the master cursor removes cross-history terms,
so for the physical prepared old apparatus and logical reference,

\[
 D(\rho_{\rm old,red}(t),\rho_{\rm ready}^{\rm ideal})
 \leq\xi+\eta_B+\eta_C+\delta_{\rm pre}.            \tag{P11}
\]

The target on the right is (P7)'s ideal old input, including h,c and every
old basis-ready bit. A full normalized packet comparison instead incurs
sqrt(delta_pre), and is not the claim of (P11). The comparison identifies
the active row of this holding interval; it does not interpret incomplete
transfer histories as an already prepared apparatus.

## 5. Completion herald, success margin and accepted-state error

Let the all-raw-space completion projector be

\[
 \Pi_{\rm tail}
 =I-\prod_{j=4B_{\rm pad}}^{8B_{\rm pad}}(I-n_j).
                                                               \tag{P12}
\]

On the legal one-cursor history it is exactly the indicator X >= 4B_pad.
Retain the complete old read predicate from the pinned #1758 Section 6:
Pi_old,read = L_old F_old, the old completion-latch projector AND the old
accepted-flag projector, both transported to the fixed final row. The new
read projector is Pi_new,read = Pi_tail Pi_old,read. These factors commute.
The old completion latch is one of the approximately prepared targets; no
initially pure new completion latch is assumed. On bad cursor sectors
(P12) can also fire; their entire contribution is included in eta_C.

For theta in [pi/3,2pi/3], p >= 3/4 and the usual binomial exponential
bound gives

\[
 w(t)=\Pr(X\geq4B_{\rm pad}),\qquad
 1-w(t)\leq(3/4)^{4B_{\rm pad}}=:\delta_{\rm out}<2^{-255}.
                                                               \tag{P13}
\]

For example, using the Markov factor (1-p)/p gives the bound
[4p(1-p)]^(4B_pad), whose maximum on this interval is (3/4)^(4B_pad).
The displayed strict estimate also follows from (3/4)^4 < 1/2 and
B_pad >= 8192.

Let sigma_cap^ideal be the subnormalized accepted physical/reference
output of the pinned forward-only candidate, before the old environment
activation weight. The mathematical output reduction traces cursors,
energy tallies, auxiliary histories, work, fuel and donor/dirty sinks as
specified for that inherited channel. It is not an extra physical decoder.
For exact readiness the new master instrument has output

\[
 \sigma_{\rm acc}^{\rm ideal}(t)=w(t)q\sigma_{\rm cap}^{\rm ideal},
 \qquad q=\frac4{15}.                              \tag{P14}
\]

This uses T's complete endpoint action and the identity output tail. At
ideal readiness the old completion latch stays false in every inactive
environment sector, where T is the identity, so Pi_old,read annihilates
those sectors. It is true at the active completed endpoint, leaving the
old accepted flag. This proves the factor q using the complete inherited
predicate. It does not inherit the old intermediate source-loading trajectory.
The actual cooled input and seed errors change the accepted instrument
by at most xi+eta_B+eta_C in input trace distance. The tail factor is
already exact in (P14). For one convenient conservative budget covering
both the preparation and output comparisons, set

\[
 \varepsilon_{\rm tot}
 =\xi+\eta_B+\eta_C+\delta_{\rm pre}+\delta_{\rm out}
 <2^{-76}.                                         \tag{P15}
\]

Here and below no square root of a rare success probability is used.
To prove the conditioning bound, let a trace-nonincreasing completely
positive accepted map give A and A_i from two normalized inputs at trace
distance at most epsilon, with weights p_a and p_i. Adjoin a one-dimensional
reject record to obtain a trace-preserving channel. Then

\[
 \frac{\|A-A_i\|_1+|p_a-p_i|}{2}\leq\varepsilon,
 \qquad |p_a-p_i|\leq\varepsilon.                  \tag{P16}
\]

Applying the triangle inequality with either normalization denominator,
for nonzero weights,

\[
 D(A/p_a,A_i/p_i)
 \leq\frac{\varepsilon}{\max(p_a,p_i)}
 \leq\frac{\varepsilon}{p_i}.                     \tag{P17}
\]

The bound is reference-uniform and includes false acceptance from bad
seed sectors. The stronger denominator in (P17) is optional; the final
inequality alone suffices here.

The inherited sharper capture lower bound and selectivity bound are

\[
 p_0=\frac25\frac{1024}{15625}\frac{99}{50000},\qquad
 u_0<\frac{50000}{99\,2^{29}}<\frac{19}{20\cdot10^6}.
                                                               \tag{P18}
\]

By (P13), w(t)>99/100. Put

\[
 p_{\rm floor}=\frac4{15}\frac{99}{100}p_0
 =\frac{418176}{30517578125},\qquad
 p_{\rm floor}-\frac1{75000}>\frac1{3000000}.       \tag{P19}
\]

The last inequality is a direct comparison of positive integers, not an
inference from a rounded decimal. Equations (P15)-(P19) give

\[
 p_{\rm acc}^{\rm actual}>\frac1{75000},\qquad
 D(\rho_{\rm acc}^{\rm actual},\rho_{\rm acc}^{\rm ideal})
 <75000\,2^{-76}<\frac1{20\cdot10^6},\qquad
 u_{\rm actual}<\frac1{10^6}.                     \tag{P20}
\]

Indeed 2^(-76) < 1/3000000 and
75000*(20*10^6) < 2^17*2^25 < 2^76. Measurement of the unwanted-output
projector changes its probability by at most the trace distance, proving
the final inequality with (P18).

The accepted logical label/old-memory SWAP, and the d_1 record for incoming
label one, are exact properties of the ideal comparison channel. For the
actual full-rank preparation they hold within the trace-distance error
in (P20), including arbitrary logical references. They are not exact
identities merely because the error is small. This note also does not
transfer a previous post-read retention interval to the new Hamiltonian
without a separate timing argument.

## 6. Remaining initial resources and stationarity boundary

All donor qubits used for cooling and environment loading are members of
one finite Gibbs preparation at the common specified temperature. This is
not a Gibbs state of the complete interacting Hamiltonian. The work qudit's
central population peak and the master cursor's near-one-excitation input
remain nonthermal, full-rank supplied states, with their energies and errors
counted. No pure majority scratch, clean new row, or fresh completion latch
is hidden in the preparation argument. The admitted logical input/code
interface remains a separate promise, as in the inherited candidate.

For any fixed finite H, [H,rho_0]=0 implies rho(t)=rho_0 for all t. A static
closed Hamiltonian cannot generate nonstationarity from a stationary total
input. Likewise tr(P exp(-itH/hbar) rho_0 exp(itH/hbar)) is a finite analytic
exponential sum. If it equals one on an open interval, it equals one at
all times, including the initial time. Thus a newly reached exact pure
ready subspace cannot have an exact finite plateau in this model.
The finite, approximate preparation window (P10)-(P11) makes neither claim.
