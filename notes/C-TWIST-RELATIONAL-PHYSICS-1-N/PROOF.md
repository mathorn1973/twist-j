# C-TWIST-RELATIONAL-PHYSICS-1-N: finite relational clock proof

**Status:** NON-CANONICAL analytical construction. No public authority and no
public status promotion. The physical identifications are proposed postulates,
not conclusions of the mathematical proof. This draft records no executed new
verifier, blind confirmation, laboratory observation, or native derivation.

**Frozen source proposed for the preregistration:** public TWIST-J v106,
`mathorn1973/twist-j` at
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`.

**Source contracts:** `canon/CANON.md`, the sections
`ACTIVE-ISOSPECTRAL-RECORD [T]` and
`COMPACT-ACTIVE-RECORD-APPARATUS [T]`, together with their explicitly cited
complete source word and compact apparatus construction. In particular, the
public compact model is a finite realization of an admitted source/readout
prefix of the homogeneous `U_rec` model. It is not the original six-pentit
update `U`, and it is not equality of the infinite and finite spectral
logarithms.

The result below supplies one finite, normalizable, stationary clock plus
apparatus state whose clock-conditioned predictions reproduce that complete
apparatus. It also supplies an explicit, positive two-setting joint-event
contrast. All Hamiltonians, states, clock effects, pointer effects, and
additional resources are on the one declared carrier.

## 1. Inherited apparatus and unambiguous notation

Let

\[
K=560,\qquad d=K+1=561,\qquad L=140.
\]

The data space is the public eleven-register space

\[
\mathcal D=
\mathbb C^{15}\otimes\mathbb C^{15}\otimes\mathbb C^{15}
\otimes\mathbb C^4\otimes\mathbb C^3
\otimes\mathbb C^{26}\otimes\mathbb C^{26}
\otimes\mathbb C^3\otimes\mathbb C^2\otimes\mathbb C^2
\otimes\mathbb C^2,
\qquad \dim\mathcal D=657072000.
\]

Its named registers are, in that order, `R,r,c,o,a,l,m,q,b,s,d` as in
the source. The last two-level register is the readout pointer; the symbol
`d` in that register name is not the integer dimension `d=561` used here.

Retain every scalar phase and every complete gate in the public word.
Write its 140 unitary gates as `G_1,...,G_L`, and set `G_m=I` for
`L<m<=K`. The public finite step inside that word is

\[
U_{\rm fin}=P_\beta\Gamma S_R S_r E_{\rm rec}Q_pM_2C.
\]

The contact phase is the dimensionless number
`theta_contact=2 pi/5`, and `beta=4 pi/5`. Neither is an energy scale.
Write `E_ctl>0` for the energy scale called `g` in the public compact
apparatus theorem. This renaming avoids identifying it with the contact
phase, or with an independently chosen spectral-energy scale `E0`.

Let `P` be the existing program-cursor register, with basis
`|m>_P`, `0<=m<=K`, and let

\[
\mathcal A=\mathbb C^d_P\otimes\mathcal D,
\quad A_0=I,\quad A_m=G_m\cdots G_1,
\quad \mathcal W=\sum_{m=0}^{K}|m\rangle\langle m|_P\otimes A_m.
\]

The letter `P` for the program register is distinct from the spectral
projectors `P_s` introduced below. Define the spin matrix on the cursor by

\[
S_x=\frac12\sum_{m=0}^{K-1}
\sqrt{(m+1)(K-m)}
\bigl(|m+1\rangle\langle m|+|m\rangle\langle m+1|\bigr).
\]

The inherited complete positive apparatus Hamiltonian is

\[
H_A=\mathcal W\left[
\left(E_{\rm ctl}I-\frac{2E_{\rm ctl}}{d}S_x\right)
\otimes I_{\mathcal D}\right]\mathcal W^\dagger.
\tag{1}
\]

This formula fixes the action on the full raw apparatus space, not just
on a selected computational path. Since the eigenvalues of `S_x` are
`K/2-s`, `s=0,...,K`, the distinct apparatus energies and their complete
spectral projectors satisfy

\[
E_s=\frac{E_{\rm ctl}(2s+1)}d,
\qquad H_A=\sum_{s=0}^{K}E_sP_s,
\qquad P_sP_r=\delta_{sr}P_s,
\qquad \sum_sP_s=I_{\mathcal A}.
\tag{2}
\]

Every eigenspace has data multiplicity `dim D`. This proof never replaces
those complete projectors by one arbitrarily chosen eigenvector.

For a data/reference input `rho_DR`, put

\[
\rho_{0,AR}=|0\rangle\langle0|_P\otimes\rho_{DR}.
\tag{3}
\]

The optional reference `R` is passive: every displayed map acts on it as
the identity. For the energy accounting in this model its Hamiltonian is
zero. Arbitrary additional matter with a nonzero Hamiltonian is not
silently included under the word "reference".

## 2. The additional reference clock and its resource cost

Add one explicitly declared `d`-level reference-clock register
`C`, with basis `|q>_C`, `q=0,...,K`, and Hamiltonian

\[
H_C=\frac{2E_{\rm ctl}}d\sum_{q=0}^{K}q|q\rangle\langle q|.
\tag{4}
\]

The complete carrier is

\[
\mathcal H=\mathbb C^d_C\otimes\mathcal A
=\mathbb C^{561}_C\otimes\mathbb C^{561}_P\otimes\mathcal D.
\tag{5}
\]

Thus there are **two different clock registers**. `P` is the program
cursor already counted by the public apparatus. `C` is the new reference
clock. The extra factor 561 is a real resource; it is not a relabeling of
the original cursor. Excluding a passive reference, the full dimension
is exactly `561^2 * 657072000`.

Use the positive total energy

\[
H_{\rm tot}=H_C\otimes I_A+I_C\otimes H_A,
\qquad E_* = \frac{(2K+1)E_{\rm ctl}}d
=\frac{1121E_{\rm ctl}}{561}.
\tag{6}
\]

No interaction term is hidden in (6). The correlations are supplied in
the prepared joint state below. The preparation is an additional boundary
resource, not a process furnished by the public source apparatus and not
a consequence of time-translation invariance.

## 3. Exact normalizable stationary preparation

Define the isometry

\[
V:\mathcal A\longrightarrow\mathcal C\otimes\mathcal A,
\qquad V\psi=\sum_{s=0}^{K}|K-s\rangle_C\otimes P_s\psi.
\tag{7}
\]

For any trace-one positive `rho_AR`, including mixed inputs correlated
with the passive reference, define

\[
R_{CAR}=(V\otimes I_R)\rho_{AR}(V^\dagger\otimes I_R).
\tag{8}
\]

**Isometry.** Orthogonality of the clock basis gives

\[
V^\dagger V=\sum_sP_s^\dagger P_s=\sum_sP_s=I_A.
\tag{9}
\]

Consequently (8) is positive, trace one, and normalizable on a finite
carrier. No improper energy eigenvectors or infinite uniform history
states are used.

**Constructive preparation as a supplied unitary operation.** There is
an explicit complete finite unitary extending this isometry on an
initially zero reference clock. Let `X_C|q>=|q+1 mod d>` and put

\[
U_V=\sum_{s=0}^{K}X_C^{K-s}\otimes P_s.
\tag{9a}
\]

The orthogonal spectral blocks prove
`U_V^dagger U_V=U_V U_V^dagger=I`; on `|0>_C tensor psi`, it equals
`V psi`. This is a full specified controlled unitary, including its
action on occupied clock states. In general it does not commute with
the chosen additive `H_tot`. Its work supply, coherent controls and
energy-selection implementation are therefore additional preparation
resources. Neither their physical implementation nor their energy cost
is supplied by the present theorem. The admitted boundary state (8)
must not be described as free preparation from a stationary product.

**Stationarity.** On the `s` term of (7),

\[
\frac{2E_{\rm ctl}(K-s)}d+\frac{E_{\rm ctl}(2s+1)}d=E_*.
\]

Therefore

\[
H_{\rm tot}V=E_*V,
\qquad H_{\rm tot}R_{CA}=R_{CA}H_{\rm tot}=E_*R_{CA},
\tag{10}
\]

and the joint density operator is stationary. The same identities hold
with the passive reference appended. One may equivalently write a
constraint `(H_tot-E_* I)R=0`. This is a zero value of a constraint,
not a claim that the physical positive energy `H_tot` is zero.

**Apparatus energy law.** Tracing out `C` dephases `rho_A` in the
`H_A` eigenspaces, while preserving its complete energy distribution:

\[
\operatorname{Tr}_C R_{CA}=\sum_sP_s\rho_AP_s,
\qquad \Pr_A(E_s)=\operatorname{Tr}(P_s\rho_A).
\tag{11}
\]

The clock has the complementary energy in every correlated component.
There is no negative clock energy and no unbounded energy capacity.

For the particular ready input (3), the inherited spin construction gives

\[
\Pr_A(E_s)=\binom Ks2^{-K},\qquad
\langle H_A\rangle=E_{\rm ctl},\qquad
\operatorname{Var}(H_A)=\frac{K E_{\rm ctl}^2}{d^2}.
\tag{12}
\]

These expressions are independent of the data/reference input. In the
stationary extension,

\[
\langle H_C\rangle=\frac{K E_{\rm ctl}}d,
\quad \operatorname{Var}(H_C)=\operatorname{Var}(H_A),
\quad \operatorname{Cov}(H_C,H_A)=-\operatorname{Var}(H_A),
\tag{13}
\]

so the variance of the total energy is exactly zero. The fixed total
energy is (6), not the independently chosen spectral reading of `U_rec`.

## 4. Clock effects and exact conditional evolution

Put

\[
|t_j\rangle_C=\frac1{\sqrt d}\sum_{q=0}^{K}
\exp\left(-\frac{2\pi i qj}{d}\right)|q\rangle_C,
\qquad j=0,\ldots,K,
\tag{14}
\]

and `C_j=|t_j><t_j|`. The finite geometric-sum identity gives

\[
\langle t_j|t_k\rangle=\delta_{jk},\qquad
\sum_{j=0}^{K}C_j=I_C.
\tag{15}
\]

Define the time calibration

\[
\Delta\tau=\frac{\pi\hbar}{E_{\rm ctl}},
\qquad \tau_j=j\Delta\tau.
\tag{16}
\]

This equation names the time unit of the selected model. It neither
derives an SI second from `J` nor identifies the original native
counter `n` with this time. Until calibration, one can use `j` and
dimensionless time `E_ctl tau/hbar` throughout.

The clock Hamiltonian acts as a cyclic shift at these calibrated times:

\[
e^{-iH_C\tau_k/\hbar}|t_j\rangle=|t_{j+k\bmod d}\rangle.
\tag{17}
\]

For the isometry (7), direct substitution gives

\[
(\langle t_j|\otimes I_A)V
=\frac{e^{iE_*\tau_j/\hbar}}{\sqrt d}
e^{-iH_A\tau_j/\hbar}.
\tag{18}
\]

Indeed the left side has coefficient
`d^(-1/2) exp(2 pi i (K-s)j/d)` on `P_s`, and the right side has the
same coefficient because `E_*-E_s=2 E_ctl(K-s)/d`.

Let `U_A(tau)=exp(-iH_A tau/hbar)`. For every mixed or reference-correlated
input, the unnormalized conditional state is therefore

\[
\langle t_j|R_{CAR}|t_j\rangle
=\frac1d(U_A(\tau_j)\otimes I_R)\rho_{AR}
(U_A(\tau_j)^\dagger\otimes I_R).
\tag{19}
\]

Its trace is `1/d`. The normalized conditional state is exactly the
ordinary apparatus evolution, including all helpers, cursor, old memory,
setting, pointer, and reference correlations. No normalization depends
on the source setting or on an unknown memory state.

For every joint apparatus/reference effect `0<=F<=I`, the complete
single-read joint law is

\[
p(j,F)=\operatorname{Tr}[(C_j\otimes F)R]
=\frac1d\operatorname{Tr}\left[
F(U_A(\tau_j)\otimes I_R)\rho_{AR}
(U_A(\tau_j)^\dagger\otimes I_R)\right].
\tag{20}
\]

Equations (15) and (20) retain every clock and pointer outcome. They
are a joint-measurement law, not a proof of an arbitrary sequence of
intervening clock measurements. A first-passage protocol, repeated
monitoring, or measurement followed by renewed evolution requires its
own instrument and cannot use (20) unchanged.

### 4.1 Effects on the fixed-energy physical sector

The uncompressed product effects `C_j tensor Pi_y`, where
`{Pi_y}` is a complete pointer projection family, generally do not
commute with `H_tot`. Their probability law does not by itself supply
an energy-preserving implementation of a projective measurement.

Let

\[
Q_*=VV^\dagger.
\tag{20a}
\]

It is the complete projector onto the energy `E_*` eigenspace of
`H_tot`: the energy equation `2q+2s+1=2K+1` holds exactly when
`q=K-s`. On that physical sector define

\[
E_{j,y}=Q_*(C_j\otimes\Pi_y)Q_*.
\tag{20b}
\]

Each effect is positive, and summing over all clock and pointer
outcomes gives `Q_*`, the identity on the physical sector. Since
`H_tot Q_*=Q_* H_tot=E_* Q_*`,

\[
[E_{j,y},H_{\rm tot}]=0.
\tag{20c}
\]

For every prepared state (8), `Q_* R Q_*=R`; hence compressed and
uncompressed effects give the same probabilities. Pulling back with
the isometry makes the coefficient explicit:

\[
V^\dagger E_{j,y}V
=\frac1d U_A(\tau_j)^\dagger\Pi_yU_A(\tau_j).
\tag{20d}
\]

This is a positive-operator-valued measure, generally not a
projection-valued measure. For a nonzero projection `Pi_y`, its
coefficient (20d) squares to `1/d` times itself and is not idempotent
because `d>1`. The compressed joint window effect is the sum of
`E_{j,1}` over the selected clock sector. All predictions below can
equivalently use that effect.

On the full carrier the complete outcome family also includes

\[
E_{\rm out}=I-Q_*.
\tag{20e}
\]

It is positive, commutes with `H_tot`, and completes the effects to the
full identity. Its probability on an ideal state (8) is zero, but an
imperfect preparation can have a nonzero outside outcome. That outcome
remains counted in the error budget and is not silently postselected
away.

The local conditional state (19) is not the post-state of an arbitrary
instrument implementing the compressed effects. For example, after
summing over the pointer, the compressed effect for one clock reading
is `Q_*/d`. The separate coarse square-root instrument for this effect leaves the
normalized joint state `R` unchanged. This is not the instrument obtained
by performing the fine `(j,y)` square-root instrument and then forgetting
`y`; those two instruments generally differ. Its apparatus marginal is then (11), which is
dephased between distinct energies. By contrast, local clock conditioning
of a coherent input gives the coherent evolved input in (19). A
superposition of two distinct energy sectors is an exact counterexample
to identifying these two post-state prescriptions.

An energy-commuting effect is not a complete measurement instrument.
Its physical coupling, outcome record, helpers and energy cost remain
explicit realization resources. The physical outcome postulate can
adopt the compressed effects without claiming that this proof has
implemented their measurement.

## 5. The two clocks have different roles

For a pure data input, (1) gives, up to one common phase,

\[
U_A(\tau)(|0\rangle_P\otimes\psi)
=\sum_{m=0}^{K}\sqrt{\binom Km}
\bigl(i\sin x\bigr)^m\bigl(\cos x\bigr)^{K-m}
|m\rangle_P\otimes A_m\psi,
\qquad x=\frac{E_{\rm ctl}\tau}{d\hbar}.
\tag{21}
\]

Hence, conditional on reference-clock outcome `j`, the program cursor
has the binomial law

\[
\Pr(P=m\mid C=j)=\binom Km p_j^m(1-p_j)^{K-m},
\qquad p_j=\sin^2\left(\frac{\pi j}d\right).
\tag{22}
\]

Conditional on any cursor value of nonzero weight, the data/reference
state is exactly `(A_m tensor I_R) rho_DR (A_m^dagger tensor I_R)`.
This follows for mixed inputs directly by linearity of (21).

The reference clock is the finite relational time observable. The
program cursor measures progress through the specified gate word.
Neither is an unbounded monotonically increasing counter. The same
joint stationary state contains the forward computation, the completion
window, and the return in its correlations.

The clock projectors have period `d Delta_tau`, and

\[
U_A(d\Delta\tau)=-I_A.
\tag{23}
\]

Consequently apparatus density operators return after that period.
The additional minus sign is a scalar phase, not a persistent record.
No cycle number is present in the state. An unbounded elapsed time or
a record of repeated cycles would require further memory and energy
resources not included here.

## 6. Exact selected read window and pointer contrast

Let `Pi_1` be the public final pointer-one projection, with identity
on all other apparatus and passive-reference registers. The public word
changes that initially zero pointer only at its final, 140th gate. Every
subsequent padded gate is the identity.

Let `rho_0,+` and `rho_0,-` be the two admitted ready inputs of the public
source comparison. Old memory may be arbitrary and correlated with a
passive reference, but fresh-write recognition requires its support in
`K_mem=span(d_1,...,d_25)`. All those data remain in the state.

The inherited endpoint difference is

\[
\Delta=\frac{65536(48533-10985\sqrt5)}
{5^9(39521+154\sqrt5)}>\frac1{50}.
\tag{24}
\]

This is an exact mathematical source-model value, not an experimentally
observed contrast. It depends on the stated source, coupling, contact
phase, finite-prefix agreement, and pointer word.

Define the completion weight

\[
B_j=\sum_{m=L}^{K}\binom Km p_j^m(1-p_j)^{K-m}.
\tag{25}
\]

Because the pointer is zero on every earlier gate prefix and every
completed prefix gives the same endpoint, (21) proves the exact law

\[
p_+(\Pi_1\mid C=j)-p_-(\Pi_1\mid C=j)=B_j\Delta.
\tag{26}
\]

There are no off-diagonal cursor interference terms in this probability:
`Pi_1` is the identity on the program cursor, whose basis states are
orthogonal. This observation is also why the result is valid for
arbitrary admitted mixed inputs and reference correlations.

Select the clock sector

\[
\mathcal J=\{187,188,\ldots,374\},\qquad |\mathcal J|=188,
\qquad C_{\mathcal J}=\sum_{j\in\mathcal J}C_j.
\tag{27}
\]

It is exactly the public apparatus window `[T_h,2T_h]` on the reference
clock grid, where `T_h=561 pi hbar/(3 E_ctl)`. Its unconditional
probability is

\[
p(C\in\mathcal J)=\frac{188}{561}.
\tag{28}
\]

For every `j` in that sector, `p_j>=3/4`. If `M` has the binomial law
(22), then

\[
\mathbb E(3^{-M})=(1-p_j+p_j/3)^K\le2^{-K}.
\]

On `M<L`, `3^{-M}>3^{-L}`. Markov's inequality therefore gives

\[
1-B_j=\Pr(M<L)<3^L2^{-K}
=\left(\frac3{16}\right)^{140}
<2^{-280}<\frac12.
\tag{29}
\]

Combining (24), (26), and (29) gives, at each admitted clock reading,

\[
p_+(\Pi_1\mid C=j)-p_-(\Pi_1\mid C=j)>\frac1{100}.
\tag{30}
\]

Most importantly, use the **unconditional joint event**

\[
F_{\mathcal J,1}=C_{\mathcal J}\otimes\Pi_1.
\]

Its exact setting contrast is

\[
\delta_{\rm joint}
=p_+(F_{\mathcal J,1})-p_-(F_{\mathcal J,1})
=\frac{\Delta}{561}\sum_{j=187}^{374}B_j
>\frac{188}{56100}=\frac{47}{14025}.
\tag{31}
\]

No unsuccessful clock reading or pointer result is discarded in (31).
The complementary event remains part of the normalized probability
space. The prediction is not inferred from the incoming-unbound
scattering-capture theorem; it is the selected active-source comparison
of the complete compact apparatus.

### 6.1 Fixed sufficient error budget

Use the compressed full-carrier joint event
`E_J,1=sum_(j in J) E_j,1`. Let the trace distances of actual normalized
joint preparations from the ideal `R_+` and `R_-` be at most
`epsilon_+` and `epsilon_-`, where trace distance is half the trace
norm. Suppose the actual joint-event effect is an effect and differs
from `E_J,1` in operator norm by at most `eta`.

For either setting, the change in a probability is at most the sum of
that preparation error and `eta`: the effect expectation changes by at
most trace distance when the state changes, and by at most operator-norm
distance when the effect changes. Thus

\[
|\widetilde\delta_{\rm joint}-\delta_{\rm joint}|
\le\epsilon_++\epsilon_-+2\eta.
\tag{32}
\]

The predeclared sufficient budget

\[
\epsilon_+=\epsilon_-=\eta=\frac1{10000}
\]

therefore preserves

\[
\widetilde\delta_{\rm joint}
>\frac{47}{14025}-\frac1{2500}>\frac1{400}.
\tag{33}
\]

This is an unconditional bound on normalized full-carrier preparations.
The outside outcome `E_out` is retained; no conditioning on a successful
energy-shell projection is allowed to remove its cost. These inequalities
state sufficient mathematical requirements. They do not report achieved
clock accuracy, an implemented instrument, or preparation precision.

## 7. What must be adopted to make this a physical model

The preceding finite mathematics does not choose its physical meaning.
A concrete first physical model can adopt the following five premises,
with each premise visible in the claim ledger.

1. **Physical carrier and law.** The two clock registers and the eleven
   data registers are the degrees of freedom of the selected model, with
   the exact gate word, Hamiltonians (1), (4), and total energy (6).
   Register locality in the compact source is not silently identified
   with the physical occupation locality of the infinite homogeneous
   `U_rec` construction.
2. **Allowed preparation.** The joint state (8), on the ready source
   inputs (3), is an admitted preparation. This includes its exact
   energy correlations, old-memory restriction for fresh-write
   recognition, and the complete source-setting preparation. No
   energy-conserving preparation procedure from an uncorrelated clock
   and apparatus is asserted by this premise.
3. **Operational clock.** The basis (14)-(15) defines the reference-clock
   labels. The adopted physical read uses the global compressed effects
   (20b), completed by (20e), rather than an implemented local clock PVM.
   A clock outcome means `tau_j` modulo `561 Delta_tau`; it is not the
   original native `n`, a universal cosmic foliation, or unbounded elapsed time.
4. **Outcome law.** A simultaneous clock/pointer read has the Born
   probabilities (20), implemented in the physical interpretation by
   the compressed effects (20b) and the outside outcome (20e), with
   complete outcomes retained. This is an
   explicit physical probability postulate, not a derivation of Born's
   rule or of outcome occurrence from integer arithmetic.
5. **Calibration and applicability.** `E_ctl Delta_tau/hbar=pi` fixes one
   time/energy calibration relation. An SI value and a laboratory
   preparation/instrument realization require a specified independent
   calibration. Until then, the finite joint probabilities and the
   dimensionless contrast (31) are the model's exact predictions.

These premises turn a selected mathematical apparatus into a sharply
specified physical candidate. They do not have to be uniquely forced by
the original axiom in order to define a candidate. Their status must,
however, remain physical postulates subject to realization and testing.
The model does not earn a no-free-parameter or one-electron-anchor claim
merely by choosing dimensionless units.

## 8. Scope boundaries that follow from the construction

- The original autonomous `U` on `N_0 x F_5^6` is not used as the quantum
  time evolution and is not proved to realize this carrier, Hamiltonian,
  preparation, clock, or measurement. Its noninjectivity is not repaired
  by renaming `U_rec`.
- A bound eigenphase of contact `W` alone is not a readable clock: its
  rank-one density operator is stationary. The present clock has a
  specified reference carrier and effects.
- The Fourier variable of the continuous spectral-energy battery is not
  used as a clock operator. That battery theorem and the compact
  apparatus have different carriers and energy operators.
- `H_A` and `H_tot` are not silently identified with a chosen scalar
  logarithm `E0 f(U_rec)`, a charge count, or the energy of the classical
  declared-boost model.
- The result is a finite relational quantum model. It supplies no
  general-relativistic proper-time functional, gravitational redshift,
  Lorentz invariance of the full apparatus, species identification, or
  gravity-matter coupling.
- The total state is stationary. The directional preparation and the
  read-window convention specify the computation's orientation. No
  thermodynamic arrow, irreversible permanent memory, or perpetual
  renewable apparatus follows. The public compact recurrence remains.
- Arbitrary repeated observations, clock resets, different horizon
  lengths, independently realizable preparations, and tolerances for
  the new clock and its correlations require separately stated
  protocols. The public compact apparatus tolerances alone do not
  certify the new joint stationary preparation.

## 9. Proposed mathematical falsifiers and independent proof obligations

The preregistration can freeze the following exact failure conditions
before a new verifier is run:

1. Failure of complete-projector orthogonality, completeness, or the
   inherited arithmetic energy spectrum (2).
2. Failure of the isometry (9) or of exact energy matching (10).
3. Nonorthogonality of the finite clock effects or failure of their
   completeness (15).
4. Failure of the operator identity (18), which would also invalidate
   the uniform clock law and mixed/reference conditional predictions.
5. Failure of the inherited full gate-prefix Hamiltonian conjugation
   (1), cursor law (21)-(22), or the premise that only gate 140 first
   changes the pointer.
6. Failure of the exact endpoint contrast (24) on any admitted old
   memory/reference input, or failure of the exact contrast formula
   (26).
7. A clock index in the frozen sector (27) violating the exact tail
   bound (29), or failure of the complete joint bound (31).

The new finite verifier should certify algebraic identities and sharp
integer/rational inequalities at their stated scope; it should not
pretend to enumerate the full `561^2 * 657072000` matrix. The general
operator proof above, and the inherited full-word source proof, carry
the arbitrary-data/reference statements. A small toy apparatus can
check an implementation but cannot replace either proof.

The physical premises have different tests: inability to realize the
frozen preparation or effects, failure of their independent calibration,
or reproducible joint frequencies outside predeclared uncertainty after
the apparatus is independently characterized. No observed frequency or
empirical threshold is asserted in this analytical draft.
