# Common-temperature preparation: energy, entropy and the fuel resource

**NON-CANONICAL, L1, conditional analytical candidate-T.** Independent
mathematical acceptance is pending. This note gives exact analytical
resource identities for [HAMILTONIAN.md](HAMILTONIAN.md). No scientific
executable, simulation or gate enumeration was run.

The fixed target is
[#1764 at 6670ac274888927be3429a463966da41ca8d2e8b](https://github.com/mathorn1973/twist-j/tree/6670ac274888927be3429a463966da41ca8d2e8b/notes/C-THERMAL-WORK-CLOCK-BOOTSTRAP-N).
Its thermal states are prepared on their actual physical target sites.
The previous interaction Hamiltonian is represented only inside the
compiled endpoint unitary \(T\); it is not added again to the energy of
the new apparatus.

Every new nonlogical factor except one fuel bit starts in a Gibbs state
at the same inverse temperature \(\beta_0\), with
\(\beta_0\epsilon=\log2\). The fuel inversion is the remaining supplied
nonthermal resource. The logical input and its reference retain their
separate admitted interface; they are not called thermal.

## 1. Fixed-gap donors and the target thermal product

For an integer-spaced spectrum with degeneracies \(d_j\), define

\[
 Z(a)=\sum_jd_j2^{-aj},\qquad
 \mu(a)={\sum_jj\,d_j2^{-aj}\over Z(a)},\qquad
 \tau_a={1\over Z(a)}\sum_{j,\lambda}2^{-aj}|j,\lambda\rangle
                                  \langle j,\lambda|.
 \tag{E1}
\]

The physical gap scale of this Gibbs site is \(a\epsilon\). A donor with
scale \(a_{\rm d}\) and a target with scale \(a_{\rm t}\) have matching
Hilbert-space labels but different on-site spectra. They both initially
have temperature \(\beta_0\). An exact funded SWAP gives the target the
donor populations, while its former complete state moves to the donor.

The target output is thus Gibbs at
\(\beta_{\rm out}=\beta_0a_{\rm d}/a_{\rm t}\) for the target's own,
unchanged Hamiltonian. This is a statement about the actual target
density operator, not a renaming of the donor Hamiltonian.

Use a star to mark predecessor parameters. Its new hot and cold systems
have \(D=2^{84}\) degenerate excited states; the hot gap is
\(d_h\epsilon=(R_\star+3)\epsilon\). The predecessor cold inverse
temperature satisfies \(\beta_{c,\star}\epsilon=b_\star\log2\).
Its old charged-head target has levels \(0,\ldots,2R_\star\), and it has
\(K_\star+1\) main/loader qubits to be cold. The paid replacements are:

| Actual target | Target gap scale | Matching donor gap scale |
|---|---:|---:|
| Predecessor hot site, dimension \(D+1\) | \(d_h=R_\star+3\) | \(1\) |
| Predecessor cold sink, dimension \(D+1\) | \(1\) | \(b_\star\) |
| Predecessor work ladder, levels \(0,\ldots,2R_\star\) | \(1\) | \(b_\star\) |
| Each of its \(K_\star+1\) main/loader qubits | \(1\) | \(b_\star\) |

All these targets initially have their own common-\(\beta_0\) Gibbs
states, rather than their required output states. Every matched donor
also has its own common-\(\beta_0\) Gibbs state. The other old payload and
row sites already require \(\beta_0\) and remain unchanged by this prefix.
All donor sites, including their large physical gaps, remain counted.

On the buffered, valid-counter component, the exact preparation
permutation \(P\) produces the whole nominated target thermal product.
The independent donor labels supply independent target marginals. The
shared work head can record their joint energy transfer, but does not
change their diagonal weights. Every displaced target value and every
reference correlation moves to its retained donor or sink. The reduction
used to compare the target input traces those retained systems; the law
does not erase them.

The required cold distribution has therefore not been moved into an
abstract code or assumed on the target. High-gap Gibbs donors at the
common temperature are an explicit hardware/resource choice, and the
energy required to warm those donors after the SWAP is paid below.
Manufacturing their spectra is not derived by this model.

## 2. Exact work of the paid SWAP prefix

For one pair, the mean total on-site energy increase is

\[
 W_{\rm pair}
 =\epsilon(a_{\rm t}-a_{\rm d})
                  [\mu(a_{\rm d})-\mu(a_{\rm t})]\geq0.
 \tag{E2}
\]

The sign follows because \(\mu(a)\) decreases with \(a\); differentiating
the finite Gibbs sum gives
\(\mu'(a)=-(\log2)\operatorname{Var}_{\tau_a}(j)\leq0\).
Equation (E2) includes both target and donor, rather than only the desired
target's energy change.

Put

\[
 p_D(a)={D\over D+2^a},\qquad
 p_1(a)={1\over1+2^a},\qquad
 \mu_M(a)={\sum_{j=0}^M j2^{-aj}\over\sum_{j=0}^M2^{-aj}}.
 \tag{E3}
\]

The exact completed-prefix work for the displayed target family is

\[
 \begin{aligned}
 {W_P\over\epsilon}={}&
 (d_h-1)[p_D(1)-p_D(d_h)]\\
 &+(b_\star-1)\bigl[
      p_D(1)-p_D(b_\star)
      +\mu_{2R_\star}(1)-\mu_{2R_\star}(b_\star)\\
 &\hspace{37mm}
      +(K_\star+1)(p_1(1)-p_1(b_\star))\bigr].
 \end{aligned}
 \tag{E4}
\]

Each term is nonnegative. In particular the cold targets' removed entropy
ends up in high-gap donors whose old warm populations now have a large
energy cost. No already-cold sink with zero cost is substituted.

This protocol is finite and explicit, not a minimum-work construction.
For example, cooling one cursor from population \(1/3\) to
\(1/(1+2^{b_\star})\) by this SWAP costs
\((b_\star-1)\epsilon[1/3-1/(1+2^{b_\star})]\). Its thermodynamic lower
bound can be much smaller.

For one spectrum, the exact relative entropy is

\[
 {\cal D}(\tau_{a_{\rm d}}\Vert\tau_{a_{\rm t}})
 =(a_{\rm t}-a_{\rm d})(\log2)\mu(a_{\rm d})
                 +\log{Z(a_{\rm t})\over Z(a_{\rm d})}.
 \tag{E5}
\]

The pairwise identity

\[
 \beta_0W_{\rm pair}
  ={\cal D}(\tau_{a_{\rm d}}\Vert\tau_{a_{\rm t}})
      +{\cal D}(\tau_{a_{\rm t}}\Vert\tau_{a_{\rm d}})
 \tag{E6}
\]

charges both the desired target's nonequilibrium free-energy increase and
the donor's. The swapped target/donor marginal remains a product and has
unchanged total entropy. Correlations with the funded head are retained;
they do not turn (E6) into free cooling.

Equation (E4) is the cost of the completed preparation word on its
buffered, valid-counter component. It is not the unconditional transfer
at an arbitrary physical time of the actual noisy clock. Raw defects,
unfinished histories and their energy remain in Sections 5 and 7.

## 3. Noncircular hardware choices and common-temperature helpers

The compiler in HAMILTONIAN.md has \(N\) information sites per line,
including the old apparatus and its matched donors, with finite
dimensions \(d_i\). Each cell also has a counter site of dimension \(N+1\)
and a work site. The actual primitive counts \(J_P,J_T\), their sum
\(J\), and the clock geometry are fixed from information dimensions before
the helper energy gaps are chosen. In particular the stated bound

\[
 J_P+J_T\leq32N^3\left(\prod_i d_i\right)^2
 \tag{E7}
\]

does not depend on the subsequently chosen counter gap or work capacity.
These are finite specifications of a compiler, not reported executed
counts.

There are \(J+1\) rows, each with \(N\) information, \(N\) counter and
\(N\) work sites. Put \(W=3N\), choose the prescribed padding \(B\), and
set

\[
 L=4B,\qquad K=4L,\qquad
 \ell=96+\lceil\log_2(K+2)\rceil,\qquad
 \Delta=\ell\epsilon .
 \tag{E8}
\]

There are \(K+1\) new outer-master/loader qubits, all of gap \(\Delta\).
Every counter has levels \(k\Delta\), \(0\leq k\leq N\).
If \(Q_{\rm info}\) is the maximum information charge of one row in units
\(\epsilon\), choose

\[
 Q=\max\{128,Q_{\rm info}+N^2\ell\}.
 \tag{E9}
\]

It bounds the entire active information-plus-counter charge. The term
\(N^2\ell\) counts all \(N\) counter copies, not just the one used as
the distinguished conjunction counter. The work head has levels
\(0,\ldots,4Q\), with spacing \(\epsilon\); its dimension is \(4Q+1\).

All work sites, all counters and all outer/loader qubits start at the same
\(\beta_0\) as the information and donor sites. Write

\[
 z_A=2^{-\ell},\qquad
 Z_W=\sum_{b=0}^{4Q}2^{-b},\qquad
 Z_C=\sum_{k=0}^N z_A^k,\qquad
 r={z_A\over1+z_A}.
 \tag{E10}
\]

The work population is \(2^{-b}/Z_W\), the counter population is
\(z_A^k/Z_C\), and every new cursor qubit has excited population \(r\).
None is supplied in a concentrated charged state or an inverted-entry
state. The high gap makes the controller vacuum and distinguished
counter ground likely at the same temperature; it is not an additional
cold-temperature input.

Only the distinguished counter must be near its ground state. Its routed
factor is swapped out and back through the other counter copies, restoring
those copies for arbitrary initial contents. All unused row, counter and
work contents remain as Gibbs junk and are included in the physical count.

## 4. One nonthermal fuel bit and the charging reaction

The sole newly added nonthermal input is a full-rank fuel bit \(f\), with

\[
 E_f=(2Q+2\ell)\epsilon,\qquad
 \rho_f=\delta_f|0\rangle\langle0|
          +(1-\delta_f)|1\rangle\langle1|,\qquad
 \delta_f=2^{-96}.
 \tag{E11}
\]

Its population inversion is explicitly supplied. Its physical energy is
not a relabelled ground-state charge. It has mean
\(E_f(1-\delta_f)\), variance \(E_f^2\delta_f(1-\delta_f)\), and entropy
\(h_2(\delta_f)\), where
\(h_2(x)=-x\log x-(1-x)\log(1-x)\).

The local launch partial isometry is

\[
 X_0=|0\rangle\langle1|_f\otimes
      \left(\sum_{b=0}^{Q}|b+2Q\rangle\langle b|_{\cal B}\right)
                 \otimes s_{m_0}^+s_{t_0}^+ .
 \tag{E12}
\]

It shifts the actual working head, creates the outer-master entry, and
creates the loader excitation. The bare-energy change is exactly

\[
 -E_f+2Q\epsilon+2\Delta=0.
 \tag{E13}
\]

All paired head levels are orthogonal, so \(\|X_0\|=1\).
Its input/output projectors are

\[
 \begin{aligned}
 P_{\rm in}
  &=n_f P_{{\cal B},[0,Q]}(1-n_{m_0})(1-n_{t_0}),\\
 P_{\rm out}
  &=(1-n_f)P_{{\cal B},[2Q,3Q]}n_{m_0}n_{t_0}.
 \end{aligned}
 \tag{E14}
\]

The positive full-space reaction edge is
\(a_0(P_{\rm in}+P_{\rm out}-X_0-X_0^*)\), of norm \(2a_0\).
The guarded loader and subsequent compiled word are part of the same
static Hamiltonian. There is no separately prepared running timer.

The nominated input component additionally has the distinguished counter
at zero and every new cursor empty. Its exact weight is

\[
 q=(1-\delta_f)\,
       {\sum_{b=0}^Q2^{-b}\over Z_W}\,
       {1\over Z_C}\,(1+z_A)^{-(K+1)} .
 \tag{E15}
\]

The work-tail weight is less than \(2^{-Q}\), and the counter excited
weight is less than \(z_A\). Therefore

\[
 1-q\leq\delta_f+2^{-Q}+(K+2)z_A
       <3\,2^{-96}<2^{-94}.
 \tag{E16}
\]

Every omitted component in this decomposition is still evolved by the
full Hamiltonian. Equation (E16) is not a postselection or a deletion.

On the nominated component, the charged head levels range from \(2Q\)
to \(3Q\); no single pure head level is needed. For any input payload
charge \(e_0\) and a prefix charge \(e\), both in \([0,Q]\),

\[
 b_{\rm current}=b+2Q+e_0-e,\qquad 0\leq b\leq Q.
 \tag{E17}
\]

The conserved complete-sector total lies in \([2Q,4Q]\), which is inside
the global complete-sector interval \([Q,4Q]\). Every local funded gate
therefore has enough range. The primitive energy shifts telescope without
a separate boundary error per gate.

The preparation counter is returned to zero on the promised input.
The compiled old endpoint acts correctly on that counter-zero subspace
and leaves the funded head unchanged there when the old target charge is
preserved. No such assertion is made about an arbitrary counter defect or
a product of local extensions on incomplete global sectors.

On the completed good preparation word the head loses exactly the mean
work \(W_P\) in (E4). The fuel deliberately supplied the larger amount
\(2Q\epsilon\) to that head, leaving the unused part stored in it.
The two created controller excitations hold another \(2\Delta\).
Neither the surplus charge nor the subsequent work/entropy correlations
are discarded.

## 5. Actual source energy and the initial commutator

For the local reaction projectors, with all other registers unrestricted,
put

\[
 \pi_{\rm in}=(1-\delta_f)
       {\sum_{b=0}^{Q}2^{-b}\over Z_W}(1+z_A)^{-2},
 \qquad
 \pi_{\rm out}=
    {\delta_f\over1-\delta_f}\,2^{-(2Q+2\ell)}\pi_{\rm in}.
 \tag{E18}
\]

Every paired head level has this same reverse-to-forward probability
ratio. The factor \(2^{-(2Q+2\ell)}\) is the exact common-temperature
weight of the energy gained by work and cursors.

The input commutes with its additive on-site energy. Its reaction
commutator nevertheless gives the exact witness

\[
 \|[H,\rho_0]\|_1
       \geq2a_0(\pi_{\rm in}-\pi_{\rm out})>0.
 \tag{E19}
\]

Tracing other sites, or using the norm-one witness \(i(X_0-X_0^*)\),
isolates these blocks. Later bonds may contribute further commutators,
especially for an arbitrary admitted logical/code input. Only the lower
bound is claimed.

If the fuel instead had its Gibbs distribution at \(\beta_0\), its
ground-to-excited ratio would be \(2^{2Q+2\ell}\), cancelling the thermal
factor in (E18). A complete Gibbs input of the additive \(H_0\) would
commute with the energy-conserving interaction. A Gibbs state of the
full \(H\) is stationary as well. The inversion in (E11) is a precise
remaining population resource relative to the fixed coupled law.

A positive inclusive source/interface partition is

\[
 H_{\rm in}=E_fn_f+
       a_0(P_{\rm in}+P_{\rm out}-X_0-X_0^*)
       +(g-a_0)P_{\rm in}.
 \tag{E20}
\]

Its complement in \(H\) is positive. This includes an interaction shared
with the work and cursor sites; it is not a separate thermodynamic fuel
subsystem. Its exact actual initial mean is

\[
 \langle H_{\rm in}\rangle_0
    =E_f(1-\delta_f)+g\pi_{\rm in}+a_0\pi_{\rm out}.
 \tag{E21}
\]

On the nominated path, whose norm weights are \(p_j(t)\),

\[
 \langle H_{\rm in}\rangle_{\rm good}(t)
      =(E_f+g)p_0(t)+a_0p_1(t).
 \tag{E22}
\]

The real off-diagonal reaction expectation vanishes because adjacent
engineered-path amplitudes have relative phase \(i\). At the path endpoint
this partition has zero expectation on that component. Its initial
\(E_f+g\) is transferred into work, cursor and propagation energy.

For the actual input
\(\rho_0=q\rho_{\rm good}+(1-q)\rho_{\rm bad}\), the corresponding exact
mean is

\[
 q\langle H_{\rm in}\rangle_{\rm good}(t)
 +(1-q)\operatorname{Tr}[H_{\rm in}e^{-itH/\hbar}
                 \rho_{\rm bad}e^{itH/\hbar}].
 \tag{E23}
\]

The second term is retained. For example
\(0\leq H_{\rm in}\leq(E_f+g+a_0)I\) bounds the state-comparison energy
error by \((E_f+g+a_0)(1-q)\). Small probability alone is not a capacity-
independent energy estimate.

## 6. Free-energy lower bounds with the correct resource scope

Let \(S\) denote any collection initially in its common-\(\beta_0\) Gibbs
state \(\tau_S=e^{-\beta_0H_S}/Z_S\). Let \(A\) contain **all** other
initially nonthermal resources, with arbitrary state \(\omega_A\).
Assume finite-dimensional \(S,A\), the initial product
\(\tau_S\otimes\omega_A\), a unitary \(U\), and
\([U,H_S+H_A]=0\). Define

\[
 W=\operatorname{Tr}[H_A(\omega_A-\rho_A')],\qquad
 \Delta S_A=S(\rho_A')-S(\omega_A).
\]

Energy and total entropy conservation give the exact identity

\[
 \boxed{
 \beta_0W+\Delta S_A
   ={\cal D}(\rho_S'\Vert\tau_S)+I(S:A)' .
 \ }
 \tag{E24}
\]

Indeed
\({\cal D}(\rho_S'\Vert\tau_S)=\beta_0\Delta E_S-\Delta S_S\),
\(\Delta E_S=W\), and
\(\Delta S_S+\Delta S_A=I(S:A)'\).
For any target subset of \(S\), relative-entropy contraction then gives

\[
 W+\beta_0^{-1}\Delta S_A
 \geq\beta_0^{-1}{\cal D}(\rho_{\rm target}'\Vert\tau_{\rm target}).
 \tag{E25}
\]

Thus a mean-work-only lower bound requires control of resource entropy.
A battery or controller that absorbs entropy can supply free energy
through that capacity too. Equation (E25) counts this explicitly.

For a genuinely spectator logical input during acquisition, so that the
only nonthermal factor of that operation is the fuel, this specializes to

\[
 {\cal D}(\rho_f\Vert\tau_f)
  -{\cal D}(\rho_f'\Vert\tau_f)
  ={\cal D}(\rho_S'\Vert\tau_S)+I(S:f)'.
 \tag{E26}
\]

Here \(\tau_f\) is the Gibbs state of the fuel's actual gap at \(\beta_0\).
Writing \(d_f=2Q+2\ell\), the initial fuel excess is exactly

\[
 {\cal D}(\rho_f\Vert\tau_f)
  =(1-\delta_f)d_f\log2-h_2(\delta_f)
                             +\log(1+2^{-d_f}).
 \tag{E27}
\]

Multiplication by \(\beta_0^{-1}\) gives its excess free energy.
This quantity, not an uncounted temperature gradient, bounds what such
an acquisition can create from the common thermal bank. The fuel's
remaining energy, entropy and correlations belong on the right side of
the complete resource balance.

There is an essential scope qualification for the full apparatus.
The admitted logical/code input can be pure, correlated with a reference,
or nonthermal on its raw carrier. The later endpoint and bad raw sectors
need not leave every such factor a spectator. For a global identity at
arbitrary physical times, include those nonthermal factors and their
reference in \(A\) in (E24), with their actual energy and entropy changes.
One must not assert a universal fuel-only identity for that complete
evolution merely by calling the logical information unconsumed.

On the nominated acquisition prefix, the paid replacements leave the
logical/reference input intact and produce the desired target thermal
product. Equation (E4) is its independently exact protocol cost, and
(E6) quantifies the thermodynamic cost of its target/donor population
exchange. The actual imperfect preparation still retains its controller,
counter and work defects. No equality between the paid protocol cost,
the best possible work cost, and the energy used to manufacture the
hardware or prepare the inverted fuel is asserted.

## 7. Exact complete energy, including all thermal row contents

All \(J+1\) rows are physical. For an information site \(i\) with
dimensionless spectrum \(e_{i,a}\), define

\[
 \mu_i={\sum_a e_{i,a}2^{-e_{i,a}}\over\sum_a2^{-e_{i,a}}},
 \qquad
 \nu_i={\sum_a e_{i,a}^{\,2}\,2^{-e_{i,a}}\over\sum_a2^{-e_{i,a}}}-\mu_i^2.
 \tag{E28}
\]

Define \(\mu_W,\nu_W\) by the same finite sums for levels \(0,\ldots,4Q\),
and \(\mu_C,\nu_C\) for levels \(0,\ell,\ldots,N\ell\). A complete thermal
row has dimensionless moments

\[
 \mu_{\rm row}=\sum_i\mu_i+N\mu_C+N\mu_W,\qquad
 \nu_{\rm row}=\sum_i\nu_i+N\nu_C+N\nu_W.
 \tag{E29}
\]

Let \({\cal L}\) be the replaced row-zero logical sites, of admitted fixed
charge \(q_{\cal L}\). The actual entire data-row Hamiltonian \(H_D\)
has moments

\[
 {\mu_D\over\epsilon}
 =(J+1)\mu_{\rm row}+q_{\cal L}-\sum_{i\in{\cal L}}\mu_i,\qquad
 {\nu_D\over\epsilon^2}
 =(J+1)\nu_{\rm row}-\sum_{i\in{\cal L}}\nu_i.
 \tag{E30}
\]

The logical charge variance is zero on the stated input, including its
passive reference. These sums count every donor, counter, unused head
and row. There is no nonthermal work-head replacement in (E30).

For the raw-space moment formulas, separate just the distinguished
head from \(H_D\):

\[
 \mu_{\rm bg}=\mu_D-\epsilon\mu_W,\qquad
 \nu_{\rm bg}=\nu_D-\epsilon^2\nu_W .
 \tag{E31}
\]

The static law has the form

\[
 H=H_0+A-\sum_{e=0}^{K-1}a_e(X_e+X_e^*),\qquad
 H_0=H_D+E_fn_f+\Delta N_{\rm cursor},
\]
\[
 A=\sum_ea_eD_e+\sum_{j=0}^Kv_jV_j,\qquad
 a_e={g\sqrt{(e+1)(K-e)}\over K+1}.
 \tag{E32}
\]

Every diagonal projector and edge is specified on the full raw space in
HAMILTONIAN.md. In particular \(D_0=P_{\rm in}+P_{\rm out}\).
The final loader edge \(e=L-1\) is guarded by the outer-master entry,
the first main edge \(e=L\) by the loader endpoint, and
\(V_L=n_{m_0}n_{t_{L-1}}\). These controls are retained when evaluating
thermal defects.

For an entirely explicit finite sum, let \(s\in\{0,1\}\) be the fuel bit,
\(b\in\{0,\ldots,4Q\}\) the distinguished head, and
\(\xi\in\{0,1\}^{K+1}\) all master/loader bits. Put

\[
 w(s,b,\xi)=p_f(s)\,{2^{-b}\over Z_W}
                     r^{|\xi|}(1-r)^{K+1-|\xi|},
\]
\[
 F(s,b,\xi)=E_fs+\epsilon b+\Delta|\xi|+A(s,b,\xi),
 \qquad
 M_j=\sum_{s,b,\xi}w(s,b,\xi)F(s,b,\xi)^j .
 \tag{E33}
\]

The input probabilities are those actually supplied, not a central
reference approximation. The initial counter states are already
included in \(\mu_{\rm bg},\nu_{\rm bg}\); \(A\) does not test them.
All sums have the displayed finite limits and exact coefficients.

The complete mean is

\[
 \boxed{\ \langle H\rangle_0=\mu_{\rm bg}+M_1
      =\mu_D+E_f(1-\delta_f)+\Delta(K+1)r+\mu_A,\ }
 \tag{E34}
\]
\[
 \mu_A=g\pi_{\rm in}+a_0\pi_{\rm out}
       +r(Kg-a_0)+(r^2-r)(g+a_{L-1}+a_L).
 \tag{E35}
\]

For the variance, different edges cannot undo each other's cursor/fuel
transition in two hops. Same-edge returns cancel their data unitaries.
Hence the exact full-input variance is

\[
 \boxed{\ \operatorname{Var}_{\rho_0}(H)
       =\nu_{\rm bg}+M_2-M_1^2+\kappa,\ }
 \tag{E36}
\]
\[
 \kappa=a_0^2(\pi_{\rm in}+\pi_{\rm out})
       +2r(1-r)\sum_{e=1}^{K-1}a_e^2
       -2r(1-r)^2(a_{L-1}^2+a_L^2).
 \tag{E37}
\]

The two guarded edges have return probability \(2r^2(1-r)\); the
other nonreaction edges have probability \(2r(1-r)\).
All covariances between the bare diagonal energy and \(A\) are included
inside \(M_2-M_1^2\). These formulas do not replace the actual mixture by
a single sharp bare energy or the active-path variance \(a_0^2\).

Since \(H\) is time independent and \([H,H_0]=0\), these complete energy
moments and the expectation of \(H_0\) are conserved. The interaction
energy is present in \(A\) and the hopping terms. The old target's former
interaction generator appears only through its compiled endpoint
operation and is not counted as a second simultaneous interaction.

## 8. Entropy, full rank and the remaining physical boundary

All nonlogical initial factors except \(f\) are full-rank Gibbs factors
of their actual on-site Hamiltonians at \(\beta_0\); \(f\) is also full
rank, but inverted. The high-gap donors, counters and cursor sites have
low entropy because of their specified spectra at that temperature.
Their gaps, physical dimensions, copies and stored energies are counted,
while the manufacturing cost of those spectra is not derived.

The exact complete entropy is preserved. If an initially independent
target \(T\) is compared with all its retained remainder \(A\), then

\[
 \Delta S_A=S_T(0)-S_T(t)+I(T:A)_t.
 \tag{E38}
\]

The donor heating, work records and all timing histories remain in \(A\)
when they are not part of \(T\). No bath refresh, discard, free reset or
unlimited reuse is part of the law.

A unitary acting on a complete finite full-rank input cannot produce an
exactly pure nontrivial marginal. The good-component error (E16), the counter
promise, and the finite timing windows are therefore retained in the
actual preparation and accepted-output bounds. The admitted logical
code is a separate input promise and is not mislabeled as a Gibbs state
of its whole raw carrier.

The construction acquires the predecessor's temperature contrast on its
fixed target Hamiltonians from a common-temperature bank, by paid local
operations. It replaces that temperature contrast as an initial resource
with an openly specified inverted fuel bit and new engineered spectra.
It does not prepare that inversion from equilibrium, derive the physical
gaps or couplings from the native law, or make a globally stationary
state begin working. Those are the remaining initial and physical
obligations.

No scientific program was executed for this derivation. Same-session
review is not independent mathematical acceptance.
