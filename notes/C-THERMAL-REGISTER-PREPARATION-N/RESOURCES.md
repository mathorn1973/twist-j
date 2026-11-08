# Thermal preparation, work and retained entropy

Status: **NON-CANONICAL, L1, conditional candidate-T**. This is an analytical
construction, not an independently accepted theorem or an executed scientific
reproduction. It uses the physical law and finite geometry specified in
[HAMILTONIAN.md](HAMILTONIAN.md). The ready apparatus to be prepared is the
one nominated in [README.md](README.md); the new preparation resources are
not assumed to be derived from Canon v105.

The construction prepares the old ready registers to an explicit error and
prepares the nominated hot/cold marginal exactly on the buffered central
work component. It retains every donor, displaced old register, work level,
clock sector and correlation. For the actual full-rank work and clock input,
the resulting preparation statement is approximate. No L6 occurrence law is
inferred from the density operators or their weights.

## 1. Common-temperature inputs and the remaining resources

Fix a positive energy unit \(\epsilon\) and

\[
 \beta_0={\log 2\over\epsilon}.
 \tag{R1}
\]

A two-level site of gap \(d\epsilon\), for positive integer \(d\), has the
supplied Gibbs density operator

\[
 \tau_d={\operatorname{diag}(1,2^{-d})\over1+2^{-d}},
 \qquad p_d={1\over1+2^d}.
 \tag{R2}
\]

These are finite mixed resource states, initially independent of one another
and of the admitted logical input and its passive reference. The Gibbs
density operators themselves are an input condition. Their production from
an earlier universe, a thermalization apparatus or a measured sample is not
claimed.

Let \(m\geq1\) count the old known readiness bits, excluding the two
hot/cold sites and the unknown logical input. Their desired values form a
fixed word \(v\), with \(m_1\) entries equal to one. Each old readiness site
starts in \(\tau_1\), as do the ordinary preparation donor bits. The two old
environment sites start at the same temperature: the gap-\(3\epsilon\) hot
site in \(\tau_3\), and the gap-\(\epsilon\) cold site in \(\tau_1\).

Two additional donor sites have gaps \(\epsilon\) and \(2\epsilon\). They
start in \(\tau_1\) and \(\tau_2\). Thus they have different populations at
one common temperature. The nominated final hot/cold states are produced by
moving populations between unequal physical gaps and paying the work cost
below.

Every unused head ladder and every new transport-row site is also supplied
in its common-temperature Gibbs state for its actual on-site Hamiltonian.
Those rows need not be empty: a SWAP transports the working state into a
new row and retains that row's old state in the previous row. Their energy,
entropy and physical sites remain in the complete system.

There are two separately declared non-Gibbs resources:

1. A finite physical work ladder concentrated near a charged energy level.
2. A full-rank polarized master-cursor input concentrated near the single
   entry excitation.

Their density operators, energy moments and failure weights are given
below. They are not outputs of the thermal preparation being proved. All
their raw physical sectors have positive weight. There is no supplied pure
vacuum of the new master clock.

The admitted unknown logical state, including an arbitrary passive reference,
is preserved by the preparation word. Its purity is not available for cooling.
No arbitrary purification of the thermal environment is silently appended;
such a purification would be a different input resource requiring its own
Hamiltonian and energy account.

## 2. A bounded-arity entropy compressor

The three-bit permutation \(C\) exchanges the two words

\[
 |100\rangle\longleftrightarrow|011\rangle
 \tag{R3}
\]

and fixes every other word. The first output bit equals the majority of the
three input bits. If those bits have independent excited population \(p\),
its output population is

\[
 f(p)=3p^2-2p^3.
 \tag{R4}
\]

The other two bits are retained. Repeating this operation on a ternary tree
gives

\[
 p_0={1\over3},\qquad p_{r+1}=f(p_r),\qquad N=3^k
 \tag{R5}
\]

using \(N\) original donor bits and \((N-1)/2\) compressor gates per final
target. At each level, the three retained child bits come from disjoint
subtrees. Their marginals are independent, even though each is correlated
with its own retained trash. This proves the recurrence without discarding
those correlations.

The exact values and inequalities

\[
 p_1={7\over27},\qquad
 p_2={3283\over19683}<{1\over5},\qquad
 p_{r+1}\leq3p_r^2
 \tag{R6}
\]

give, for \(k\geq3\),

\[
 p_k\leq{1\over3}\left({3\over5}\right)^{2^{k-2}}
       <2^{-2^{k-3}},
 \tag{R7}
\]

because \((3/5)^2<1/2\). Choose

\[
 b=\lceil\log_2m\rceil+80,\qquad
 k=3+\lceil\log_2b\rceil,\qquad N=3^k.
 \tag{R8}
\]

Then the product of \(m\) independently prepared retained bits has total
wrong-pattern weight

\[
 \delta_{\rm tree}=1-(1-p_k)^m\leq mp_k<2^{-80}.
 \tag{R9}
\]

For every desired value one, apply a bit complement to the retained bit.
SWAP it into the corresponding old readiness site. Both sites have the
same gap, so the SWAP has zero bare-energy cost. The old site's entire
thermal state moves into the donor block. It is not erased.

The retained target marginal is diagonal. Its trace distance, with the
convention \(D(\rho,\sigma)=\|\rho-\sigma\|_1/2\), from
\(|v\rangle\langle v|\) is exactly \(\delta_{\rm tree}\). This is a statement
about the target marginal, not about its product independence from all
retained trash.

### Exact compressor work

For a compressor with independent input population \(p\), the two exchanged
words have probabilities \(p(1-p)^2\) and \((1-p)p^2\). Their charges differ
by one. Its mean payload-charge increase is therefore

\[
 c(p)=p(1-p)(1-2p).
 \tag{R10}
\]

There are \(3^{k-r-1}\) such gates at level \(r\) per prepared bit. Define
the exact rational number

\[
 C_{\rm tree}
   =\sum_{r=0}^{k-1}3^{k-r-1}p_r(1-p_r)(1-2p_r).
 \tag{R11}
\]

Every summand is nonnegative, since \(0<p_r<1/2\). A complement on a retained
bit costs an additional mean charge \(1-2p_k\). The compression and pattern
preparation cost for all \(m\) old readiness bits is consequently

\[
 \epsilon\,[mC_{\rm tree}+m_1(1-2p_k)].
 \tag{R12}
\]

This includes the changes in the donor trash. It is not obtained by counting
only the energy of the prepared target bits.

## 3. Preparing the old hot/cold environment

Perform an energy-funded SWAP of the hot site \(h\) with the gap-\(\epsilon\)
donor \(d_h\), and of the cold site \(c\) with the gap-\(2\epsilon\) donor
\(d_c\). The exact reduced output is

\[
 \rho_{hc}^{\rm nom}
  =\operatorname{diag}(2/3,1/3)_h
       \otimes\operatorname{diag}(4/5,1/5)_c.
 \tag{R13}
\]

It is independent of the prepared readiness marginal at the level of those
retained marginals. The work store may be correlated with their joint
classical energy values. The displaced old hot and cold states remain in
the two donor sites.

For the hot SWAP, the mean total energy of the two swapped sites changes by

\[
 (3\epsilon-\epsilon)(1/3-1/9)={4\epsilon\over9}.
 \tag{R14}
\]

For the cold SWAP, it changes by

\[
 (\epsilon-2\epsilon)(1/5-1/3)={2\epsilon\over15}.
 \tag{R15}
\]

Thus the two SWAPs cost \(26\epsilon/45\). The full four-site account is

| Subsystem | Before preparation | After preparation | Increase |
|---|---:|---:|---:|
| Old hot/cold sites | \(2\epsilon/3\) | \(6\epsilon/5\) | \(8\epsilon/15\) |
| Their two donor sites | \(11\epsilon/15\) | \(7\epsilon/9\) | \(2\epsilon/45\) |
| Both pairs | \(7\epsilon/5\) | \(89\epsilon/45\) | \(26\epsilon/45\) |

The nominated hot site has effective inverse temperature \(\beta_0/3\) and
the cold site has effective inverse temperature \(2\beta_0\). That
temperature difference has been prepared using work.

In the subsequent environment-source construction, the old hot/cold pair
can lose \(8\epsilon/15\) of bare energy to the two moving excitations.
Here that amount was first added to the pair by the work-funded preparation.
The final pair can have the same mean energy \(2\epsilon/3\) as its original
common-temperature state while having a different density operator. No
cycle or one-bath work extraction has been established.

Combining all preparation gates, put

\[
 C_{\rm prep}
  =mC_{\rm tree}+m_1(1-2p_k)+{26\over45}.
 \tag{R16}
\]

This is the exact mean payload-charge gain on the buffered central work
component. It is a finite rational expression in explicitly fixed integers.

## 4. The physical ladder and the actual local completion

Let \(E_{\rm pay}\) be the dimensionless nonnegative payload charge used by
the local compiler, with

\[
 0\leq E_{\rm pay}\leq Q,\qquad R=2Q.
 \tag{R17}
\]

The head ladders are excluded from \(Q\). The physical head is an actual
on-site qudit with \(2R+1\) levels and Hamiltonian

\[
 H_B=\epsilon\sum_{n=0}^{2R}n|n\rangle\langle n|.
 \tag{R18}
\]

It is not a thermometer code inside an uncounted qubit bank. This construction
therefore explicitly allows an on-site dimension growing with \(R\), with
capacity \(2R\epsilon\) per head. Every transported copy of a head is counted
in the geometry and total on-site energy.

For a primitive gate acting on finitely many payload sites, the compiler
extends that gate energy-conservingly on its own complete local
energy sectors, and uses the identity on its incomplete local sectors.
The construction in [HAMILTONIAN.md](HAMILTONIAN.md) is a full unitary on the
raw local space.

Starting from head level \(R\), a prefix whose payload charge changes from
\(q_0\) to \(q\) leaves the working head at

\[
 n=R+q_0-q,\qquad R-Q\leq n\leq R+Q.
 \tag{R19}
\]

Since \(R=2Q\), this interval supplies the buffer required by every primitive
local gate. Every prefix therefore implements the intended preparation
permutation on its payload populations, without error accumulating by gate
count. This also holds with an arbitrary passive logical reference.

The same conclusion does not apply to every other initial ladder level.
Different primitive local completions can perform a partial word on those
inputs. In particular, their product is not asserted to be the identity on
every incomplete *global* energy sector. No global sector guard or
simplified uniform-tail formula is assumed.

The supplied work density operator is

\[
 \omega_B=(1-\eta_B)|R\rangle\langle R|
       +{\eta_B\over2R}\sum_{n\ne R}|n\rangle\langle n|,
 \qquad
 \eta_B={2^{-80}\over Q+1}.
 \tag{R20}
\]

It is full rank on the entire physical head, and has no coherence between
eigenvalues of \(H_B\). Its exact moments and entropy are

\[
 \langle H_B\rangle=\epsilon R,\qquad
 \operatorname{Var}(H_B)
   =\epsilon^2\eta_B{(R+1)(2R+1)\over6},
 \tag{R21}
\]

\[
 S(\omega_B)=h_2(\eta_B)+\eta_B\log(2R),
 \qquad h_2(x)=-x\log x-(1-x)\log(1-x).
 \tag{R22}
\]

This nearly sharp charged distribution is a supplied low-entropy work
resource. Its being diagonal does not make it a Gibbs state or a free
resource.

The following cost is the cost of the completed preparation word on the
nominated master history, including the actual mixed work seed. It is not
the unconditional cost at a physical time after averaging unfinished
histories and bad master-cursor sectors. The latter are governed by the
whole-system conserved-energy account in Section 8, including (R38)--(R39).
For an energy observable \(0\leq O\leq E_{\rm cap}I\), a state error at
most \(\eta_C\) bounds its mean error by \(E_{\rm cap}\eta_C\), not by an
energy-independent small number. At a finite preparation window one must
also include the unfinished-history error from [PREPARATION.md](PREPARATION.md).
No such capacity factor is omitted from a claimed energy approximation.

Let \(\widetilde P\) denote the actual finite product of the local
energy-conserving preparation gates, including the specified head routing.
All routing partners and displaced payload states are retained. Define the
tail input by replacing the distinguished head in the stated preparation
input with

\[
 \omega_B^{\rm tail}={1\over2R}\sum_{n\ne R}|n\rangle\langle n|.
\]

The exact tail cost is the finite matrix expression

\[
 C_{\rm tail}
  =\operatorname{Tr}\!\left[
    E_{\rm pay}^{\rm out}\widetilde P\rho_{\rm tail}\widetilde P^*\right]
       -\operatorname{Tr}[E_{\rm pay}^{\rm in}\rho_{\rm tail}],
 \qquad |C_{\rm tail}|\leq Q.
 \tag{R23}
\]

The two charge observables refer to the initial and final locations of the
transported working payload. Both have spectrum in \([0,Q]\).
Equal-energy row SWAPs are accounted separately as transfers of location.
Equivalently one may include the retained row sites in both terms and
cancel the unchanged transported thermal contributions. This is an exact
finite-word definition, not an assertion that the tail is fixed.

Thus the actual mean preparation cost is

\[
 \epsilon\bigl[(1-\eta_B)C_{\rm prep}
                       +\eta_B C_{\rm tail}\bigr].
 \tag{R24}
\]

Conservation of the total on-site energy makes this the corresponding
decrease in the transported work head, with location transfers treated in
the same convention. In particular,

\[
 |\eta_B\epsilon C_{\rm tail}|<\epsilon\,2^{-80}.
 \tag{R25}
\]

All terms, including the tail term, remain in the complete energy account.

After tracing preparation trash and head, the actual prepared old payload is
a convex mixture of its exact central-head preparation and its actual tail
preparation. Consequently its distance from the ideal readiness pattern
and nominated hot/cold state is at most

\[
 \delta_{\rm pay}\leq\delta_{\rm tree}+\eta_B<2^{-79}.
 \tag{R26}
\]

Equation (R13) is exact for the central component. The actual full-rank seed
has only the approximation (R26), unless an additional statement about its
tail is proved. Correlations with the retained head and trash are not
discarded from the full state.

## 5. The full-rank master-cursor boundary

There are \(K+1\) physical master-cursor qubits in the geometry. Set

\[
 \eta_C=2^{-80},\qquad r={\eta_C\over K+1}.
 \tag{R27}
\]

Their initial density operator is a product: the entry qubit has excited
population \(1-r\), and every other cursor qubit has excited population
\(r\). This is full rank on the entire \(2^{K+1}\)-dimensional raw cursor
space. It includes vacuum and all multi-excitation sectors.

The component with exactly the desired entry excitation and no others has
weight

\[
 w_C=(1-r)^{K+1}\geq1-\eta_C.
 \tag{R28}
\]

It is a component of a supplied density operator, not a selected or
postselected physical occurrence. Every other component follows the same
static Hamiltonian.

For the cursor bare number \(N_C\),

\[
 \langle N_C\rangle=1+(K-1)r,\qquad
 \operatorname{Var}(N_C)=(K+1)r(1-r).
 \tag{R29}
\]

Multiplication by \(\epsilon\) and \(\epsilon^2\) gives its bare-energy
mean and variance. The seed has entropy

\[
 S_C=(K+1)h_2(r).
 \tag{R30}
\]

There is no bare-energy coherence in this product. It is nevertheless not
a common-temperature Gibbs distribution: the entry is inverted and the
other cursor sites strongly favor their ground state. Its nonstationarity
relative to the interacting Hamiltonian is a remaining physical boundary
condition. It is not prepared by the process being proved.

On the central one-entry component, the intended history is exact. On the
other cursor components, the full raw Hamiltonian governs the evolution.
One must not infer from the central component that the whole mixed input
has an initial commutator only on its first propagation bond. The other
clock sectors and the non-Gibbs head can contribute elsewhere. The complete
initial energy and its moments use the actual product density operator.

## 6. Entropy remains in the apparatus

Compression reduces the entropy of the retained readiness bits by moving
information into correlations and discarded *locations*, all of which
remain physical subsystems. It is not a trace-out in the law. On the central
head component, the entropy of the reduced old readiness and environment
registers after preparation is

\[
 S_T^{\rm central}
    =m h_2(p_k)+h_2(1/3)+h_2(1/5).
 \tag{R31}
\]

If \(T\) is the subsystem being prepared and \(A\) denotes all retained
donors, work, controller and other apparatus, then any complete preparation
unitary from an initially independent \(T,A\) satisfies

\[
 S_A({\rm final})-S_A({\rm initial})
  =S_T({\rm initial})-S_T({\rm final})
       +I(T:A)_{\rm final}.
 \tag{R32}
\]

This follows directly from preservation of \(S_{TA}\). It applies to the
actual mixed input, with its actual final marginal. The term \(I(T:A)\)
cannot be omitted by declaring the trash to have no cost. The entropy of a
passive reference and its initial logical correlations is handled by
including that reference in the appropriate retained subsystem; the
preparation acts identically on the logical input.

Subsequent experimental gates act identically on the stored preparation
trash. Hence a reduced-payload trace-distance bound is sufficient for a
comparison of subsequent output channels on the original logical input
and its reference. It does not establish a product interface relative to
every newly retained preparation subsystem.

The compression is finite and imperfect. No resetting protocol, thermal
refresh, unlimited repetition or reusable work source has been proved.

## 7. Exact-purity and stationary-source obstructions

If a finite preparation resource state \(\rho\) is full rank, a unitary
preserves that rank. For a nontrivial target subsystem \(T\) and retained
system \(A\),

\[
 \rho\geq\lambda_{\min}I
 \quad\Longrightarrow\quad
 \operatorname{Tr}_A(U\rho U^*)\geq
          (\dim A)\lambda_{\min}I_T.
 \tag{R33}
\]

Thus its target marginal cannot be exactly pure. More sharply, if the
eigenvalues of \(\rho\) are listed in decreasing order, the probability of
any prescribed pure target is at most

\[
 \sum_{i=1}^{\dim A}\lambda_i(\rho)<1.
 \tag{R34}
\]

This is the maximum trace in a projector of rank \(\dim A\); the inequality
is strict for a full-rank input and \(\dim T>1\).

This obstruction concerns the preparation resources. A supplied pure
logical input is not silently included as consumable purity: the present
preparation acts identically on that input. A claim uniform over arbitrary
logical inputs must also hold for a full-rank logical input on its admitted
Hilbert space. If one instead adds a pure reset ancilla or lets a controller
absorb entropy from a fixed pure initial state, that is an additional
purity resource and must be counted.

The common-temperature payload alone cannot provide the stated process
under an energy-conserving closed law. If every factor, including work and
clock, were supplied in the Gibbs state at \(\beta_0\) for the additive
Hamiltonian \(H_0\), then

\[
 \rho_{\beta_0}\propto e^{-\beta_0 H_0},
 \quad [H,H_0]=0
 \quad\Longrightarrow\quad [H,\rho_{\beta_0}]=0.
 \tag{R35}
\]

It would be stationary. More generally \([H,\rho]=0\) implies that the
closed state does not begin any preparation under that fixed \(H\).

The charged non-Gibbs head and the polarized cursor avoid this hypothesis;
they do not disprove it. The input has no \(H_0\)-coherence, but can have
coherence and nonstationarity relative to the full interacting \(H\).
Production of these two seed distributions, their diagonal population
boundary relative to the fixed interaction, and an eventual reset remain
explicit obligations. A closed apparatus in its full ground state cannot
fund the positive on-site energy increases claimed here.

## 8. Whole-system energy, including unused rows

For a site type \(i\) with dimensionless on-site charge spectrum
\(\{e_{i,a}\}\), define its exact common-temperature moments by

\[
 Z_i=\sum_a2^{-e_{i,a}},\qquad
 \mu_i={\sum_a e_{i,a}2^{-e_{i,a}}\over Z_i},\qquad
 \nu_i={\sum_a e_{i,a}^2 2^{-e_{i,a}}\over Z_i}-\mu_i^2.
 \tag{R36}
\]

A gap-\(d\epsilon\) qubit has
\(\mu_i=d/(1+2^d)\) and
\(\nu_i=d^2 2^d/(1+2^d)^2\). An unused physical head has spectrum
\(0,\ldots,2R\), so (R36) is a finite exact rational sum for that head,
not a zero contribution.

There are \(n\) payload qubits with weights \(w_i\in\{1,2,3\}\) per
active line, \(Q=\sum_iw_i\), and \(n\) physical head ladders per line.
If \(J_p,J_T\) are the actual routed primitive counts for preparation and
the subsequent experiment, put \(J=J_p+J_T\). There are \(J+1\) rows, hence

\[
 N_{\rm payload}=(J+1)n,\qquad
 N_{\rm ladder}=(J+1)n.
 \tag{R36a}
\]

Every ladder has capacity \(2R\epsilon\), so the total physical ladder-bank
capacity is \(2R\epsilon(J+1)n\). This is distinct from the capacity of the
single transported work head.

Index every actual payload and head site in every row by its physical
location \(i\). Sum (R36) over all the common-temperature locations.
For the distinguished work head use (R21), for the master cursor use
(R29), and for the admitted logical input use its specified constant
bare charge. These prescriptions give the exact initial mean and variance
of the positive additive Hamiltonian \(H_0\); product independence removes
cross-covariances except the explicitly admitted logical/reference block,
whose charge is fixed.

This sum includes thermally occupied later rows, all head copies and the
old apparatus before it is prepared. Following a transported state is a
bookkeeping convention; it does not remove its old or new location from
the Hamiltonian.

For a closed form of these sums, let \(\mu_B^{\rm th},\nu_B^{\rm th}\)
be the dimensionless head moments (R36), and put

\[
 \begin{aligned}
 \mu_{\rm row}^{\rm th}
    &=\sum_{i=1}^n{w_i\over1+2^{w_i}}+n\mu_B^{\rm th},\\
 \nu_{\rm row}^{\rm th}
    &=\sum_{i=1}^n{w_i^2\,2^{w_i}\over(1+2^{w_i})^2}
                                      +n\nu_B^{\rm th}.
 \end{aligned}
 \tag{R36b}
\]

Let \({\cal L}\) be the payload sites of the supplied logical input in row
zero. Its admitted encoding has fixed dimensionless charge \(q_{\cal L}\).
For \(i\in{\cal L}\), let \(\mu_i,\nu_i\) be the thermal baseline values
(R36) which are being replaced. If \(H_D\) is the total on-site Hamiltonian
of all payload and head rows, its exact mean and variance are

\[
 \begin{aligned}
 {\mu_D\over\epsilon}
  &=(J+1)\mu_{\rm row}^{\rm th}
      +R-\mu_B^{\rm th}+q_{\cal L}-\sum_{i\in{\cal L}}\mu_i,\\
 {\nu_D\over\epsilon^2}
  &=(J+1)\nu_{\rm row}^{\rm th}
      +\eta_B{(R+1)(2R+1)\over6}
      -\nu_B^{\rm th}-\sum_{i\in{\cal L}}\nu_i .
 \end{aligned}
 \tag{R36c}
\]

The logical replacement has zero charge variance even with an arbitrary
passive reference. The distinguished head is the only non-Gibbs work-site
replacement. All other row sites use their stated Gibbs inputs.
Thus \(\mu_D,\nu_D\) already include the entire thermal row inventory;
they are not merely active-row quantities.

The conserved physical generator is

\[
 H=H_0+H_{\rm prop},\qquad
 H_0=H_D+\epsilon N_C,\qquad
 H_{\rm prop}=gN_C-\sum_{j=0}^{K-1}a_j\,{\cal T}_j,
 \tag{R37}
\]

where \(g>0\), \(a_j=g\sqrt{(j+1)(K-j)}/(K+1)\), and \({\cal T}_j\)
is the Hermitian, gate-dressed nearest-cursor hop in
[HAMILTONIAN.md](HAMILTONIAN.md). Its positive local decomposition includes
the specified node potentials. No potential is omitted from (R37).

For the actual full-rank product cursor, independent of all initial rows,
the exact full-energy moments are

\[
 \boxed{\ \langle H\rangle_0
  =\mu_D+(\epsilon+g)[1+(K-1)r]\ },
 \tag{R38}
\]

\[
 \boxed{\begin{aligned}
 \operatorname{Var}_{\rho_0}(H)
  ={}&\nu_D+(\epsilon+g)^2(K+1)r(1-r)\\
     &+a_0^2(1-2r)^2
       +{g^2K(K+2)\over3(K+1)}r(1-r),
 \qquad a_0^2={g^2K\over(K+1)^2}.
 \end{aligned}}
 \tag{R39}
\]

The mean of a hop vanishes because the cursor density is diagonal.
In the square of the hop sum, different edges have zero diagonal
expectation, and each same-edge pair contributes the identity on its data
sites. The edge contribution is
\(a_j^2[p_j(1-p_{j+1})+(1-p_j)p_{j+1}]\).
Using \(p_0=1-r\), \(p_j=r\) for \(j>0\), and
\(\sum_j a_j^2=g^2K(K+2)/[6(K+1)]\) gives (R39).
This does not require a sharp total on-site charge or a pure logical input.

The propagation energy is therefore not set to zero because the input is
diagonal in the on-site basis. All invalid and multi-cursor raw sectors
are already included in (R38)--(R39).

Since the full law is time independent and \([H,H_0]=0\), the complete
expectations of \(H\), \(H_0\) and \(H_{\rm prop}\) are separately conserved.
All energy losses in one location or work head are gains elsewhere in the
same system. Equations (R12)--(R25) identify the preparation transfer inside
that conserved total. They do not add an external time-dependent charging
pulse or a hidden switch to the law.

## 9. Scope of the construction

The result replaces the old exact readiness inputs by a concrete finite
common-temperature compression program with a quantified preparation error.
It prepares the old temperature contrast by paid unequal-gap swaps. It
accounts for the full-rank work seed, master cursor, all unused rows and
all retained entropy.

The remaining input is a specified finite mixed resource state with an
explicit charged work distribution and an explicit polarized master
cursor. It is not a Gibbs state of the complete interacting Hamiltonian.
The finite local ladder is new hardware of growing on-site dimension.
Neither this hardware nor its resource distributions have been derived from
the unmodified native TWIST-J law.

No scientific program was executed to obtain the equations in this note.
The derivation and same-session cross-review do not constitute independent
mathematical acceptance.
