# Sharp source sectors and thermal batteries for the retained record

**NON-CANONICAL, L1. New analytical extension; independent mathematical
acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

This note develops the reduced-output alternative in
[PREPARATION.md](PREPARATION.md). Its main route uses a source seed at the
highest actual rounded charge and a cold battery near its vacuum. It
requires neither a coherent packet nor charged battery buffers. A second,
optional construction uses the degeneracy of a thermal qubit battery
directly. These are distinct finite implementations.

The retained contract is the archive/pointer/reference state and the
specified source effects commuting with rounded energy. It is not the
earlier uniform approximation to a full source/battery product state.
The twelve preceding files are unchanged. Preparation of the source
seed, information readies, clock and completion latch belongs to the
separate complete thermal construction; none is silently supplied by a
battery theorem.

## 1. Actual charge extrema and the main vacuum route

Use the finite source space X_f and complete source word U_f of
FINITE_MODEL.md. Let the actual nonzero charge sectors be

    q_f=d sum_(r=a)^b r P_r,
    a=min{r:P_r!=0},       b=max{r:P_r!=0},       v=b-a.

Empty intermediate sectors are allowed. In particular a need not be zero
and b need not equal the earlier ceiling m. The commuting compressed
residual is r_f, with 0<=r_f<=dI. Choose a specified common eigenvector
x_* of q_f,r_f in the highest sector:

    P_b x_*=x_*,             r_f x_*=r_* x_*.

Choose a complete finite unitary P_x satisfying P_x x_*=x_0. Let V be the
complete word U_f(P_x tensor I), optionally followed by the occupied-archive
writer. All information and reference factors are included through
identities in the charge projectors. The ideal input family is
x_* tensor F/reference, with the source word's stated auxiliary readiness.

Take N>=v physical gap-d qubits with

    B=d sum_(i=1)^N n_i,
    u_n=|1>^(tensor n) tensor |0>^(tensor (N-n)),  0<=n<=N.

Their complete raw dimension is 2^N. For every integer b<=z<=N+a put

    J_z psi=sum_(r=a)^b P_r psi tensor u_(z-r),
    P_good=sum_(z=b)^(N+a) J_z J_z^*,
    Gamma(V)=sum_(z=b)^(N+a) J_z V J_z^*+(I-P_good).      (T1)

Every z-r lies between zero and N. The J_z are isometries with orthogonal
ranges. Their completeness means that every source charge is represented
inside that unary fiber, not that other physical battery configurations
have disappeared. The identity complement includes all nonunary states
and every unused part of a boundary sector. Thus on the entire space,

    Gamma(V)^*Gamma(V)=I,
    [Gamma(V),q_f+B]=0,
    Gamma(V_2)Gamma(V_1)=Gamma(V_2 V_1).                 (T2)

The highest-charge seed and battery vacuum satisfy

    x_* tensor u_0=J_b x_*,
    Gamma(V)(x_* tensor f tensor u_0)=J_b V(x_* tensor f). (T3)

Therefore N=v is sufficient. No m excited buffer qubits are required.
If v=0, the battery may be absent. Energy released when the source moves
from b to r is stored as b-r battery excitations; the source seed supplies
that charge. Its preparation energy and purity must still be counted.

## 2. Exact retained outputs, with the reference

For an arbitrary density sigma on the ideal completed source, information
registers and passive reference, direct expansion gives

    Tr_(X_f,B)(J_z sigma J_z^*)=Tr_(X_f)(sigma).          (T4)

Tracing X_f kills P_r sigma P_s for r!=s. On a diagonal charge block the
battery state has norm one. This proves equality of the whole retained
joint state, including reference correlations, not only its marginals.

More generally, if a source effect A satisfies [A,q_f]=0, then for any
retained-register observable Y,

    Tr[(A tensor Y tensor I_B) J_z sigma J_z^*]
        =Tr[(A tensor Y) sigma].                       (T5)

The compressed unwanted-band effect A_bad in FINITE_MODEL.md has this
commutation property. Commutation with r_f is neither required nor
inferred. Its joint statistics with the output record are preserved.
Equation (T5) is an observable comparison, not a material detector design.

After the lifted P_x alone, the source marginal is generally

    sum_r P_r |x_0><x_0| P_r,

and is correlated with the battery. The standalone coherent spatial
state x_0 has not been prepared. At the completed word, the source and
battery likewise need not approximate an independent product. Coherence
between source charges is represented inside a fixed total-charge sector.
This is the precise scope difference from the coherent-packet theorem.

## 3. Mixed batteries and the role of a fixed seed

For the top seed, every unary battery level

    0<=n<=N-v

lies in a useful fiber z=b+n. The reduced-output identity extends to an
arbitrary battery density supported on these levels. To see the stronger
operator statement, for any source/information/reference operator tau,

    Tr_(X_f,B)(J_z tau J_(z')^*)=0       if z!=z',

because tracing the source first forces equal source charges, after which
the battery levels differ. Hence off-diagonal battery entries disappear
from the retained output. A coherent phase is unnecessary. Even initial
battery correlations with the information/reference are allowed on this
good support: the result is the ideal channel applied to their reduced
information/reference input.

For an independent diagonal battery, let q be its total weight on the
good unary levels. On this weight the same ideal retained channel is
implemented. The complementary input with source x_* lies in the identity
block of (T1). Its entire state and entropy remain in the evolution.
The general unconditioned retained-channel error is therefore at most
1-q in trace distance.

There is a stronger accepted-output statement when the source acceptance
flag and new pointer have their specified zero readiness. The identity
complement executes no source program, so its acceptance flag remains
zero and the subsequent writer rejects it. If the writer is included in
V, that complement instead leaves the zero pointer directly unchanged.
Thus, for an independent diagonal battery,

    Sigma_actual,acc=q Sigma_ideal,acc.                 (T6)

For q>0 and positive ideal acceptance, the normalized accepted
archive/reference state and its commuting-band statistics are exact.
Bad battery sectors reduce success rather than contaminate this
conditional state. This conclusion depends on the declared readies.
Errors in their thermal preparation, or a different read instrument,
must be handled by the complete construction rather than omitted here.

A mixture of source labels is different from a mixture of battery levels.
The fixed P_x maps the specified x_* to x_0; it does not map every other
thermal source eigenvector to the same prepared vector. Equation (T4)
does not assert that V has the same output on different source inputs.
Unwanted label occupations therefore remain defects unless an additional
entropy-preserving source-reset construction proves otherwise. The main
thermal implementation must create the designated one-label seed and
retain its launch probability, rather than substitute a thermal label
mixture into (T3).

## 4. Ladder Gibbs states and physical qubit Gibbs states

First consider an actual nondegenerate (N+1)-level ladder, as a different
hardware choice. At inverse temperature beta let t=exp(-beta d).
For the top seed, its good probability is

    q_ladder=(1-t^(N-v+1))/(1-t^(N+1)),        0<t<1.    (T7)

At beta=0 this becomes (N-v+1)/(N+1). With a chosen seed of another
charge j and a corresponding P_x, the complete unary interval is
b-j<=n<=N+a-j and the right side acquires the factor t^(b-j).
This shows why the top seed is especially useful for a cold battery.

Equation (T7) is not the Gibbs distribution of N independent physical
qubits. For those qubits put

    p=1/(1+exp(beta d)).

The probability of a particular unary string u_n is
p^n(1-p)^(N-n), without its charge-sector binomial multiplicity.
Therefore the physical product Gibbs state has exact useful weight

    q_unary=sum_(n=0)^(N-v) p^n(1-p)^(N-n)
           >=(1-p)^N>=1-Np.                            (T8)

The main route uses only this vacuum lower bound. For N>0 and desired
battery defect bound delta_B, choosing

    beta d>=ln(N/delta_B)

suffices because p<=exp(-beta d). Its initial energy moments and capacity
are

    <B>=Ndp,       Var(B)=Nd^2 p(1-p),       capacity=Nd. (T9)

Every nonunary thermal configuration remains present; it is not called a
unary code state. At high temperature q_unary=(N-v+1)/2^N, which is very
different from (T7). No entropy compression into a pure auxiliary memory
is used to identify these two Gibbs distributions.

The complete device also has charge padding, future rows, label sites,
cursor sites and a completion latch. Their populations, energies and
dimensions are separate from the N-qubit battery in (T8)-(T9). A cold
vacuum approximation for the battery alone does not prepare those sites.

## 5. Optional direct use of raw thermal degeneracy

There is another exact construction which uses all low-charge
configurations of a product thermal battery. It changes the lift (T1)
and does not require a unary compression.

Let H_n be the N-qubit charge-n space, with an ordered computational basis
|n,gamma> and dimension D_n=binom(N,n). Set

    n_good=floor(N/2)-v.

Assume n_good>=0. For n<=n_good and every actual source charge r,

    n<=n+b-r<=floor(N/2),       D_(n+b-r)>=D_n.          (T10)

The inequality follows from the successive binomial ratio
D_(k+1)/D_k=(N-k)/(k+1), which is at least one on this range.
Choose a fixed injection iota_(n,r) from the D_n basis indices into the
charge-(n+b-r) basis. At r=b choose the identity injection. Define

    J_(n,gamma) psi
        =sum_r P_r psi tensor |n+b-r,iota_(n,r)(gamma)>. (T11)

Each map is an isometry of the whole source/information space. Distinct
n have different total charges n+b. At a fixed n, distinct gamma are
orthogonal in every source charge block by the injection property.
Consequently their ranges are mutually orthogonal. Put

    P_multi=sum_(n=0)^n_good sum_(gamma=1)^D_n
                     J_(n,gamma) J_(n,gamma)^*,
    Gamma_multi(V)=sum_(n,gamma) J_(n,gamma) V J_(n,gamma)^*
                                      +(I-P_multi).   (T12)

This is a complete raw unitary, conserves q_f+B, and is multiplicative in
V. Every basis input x_* tensor |n,gamma> with n<=n_good is exactly
J_(n,gamma)x_*. The proof of (T4)-(T5) applies in each copy, and cross-copy
terms vanish under the retained trace. The battery's degeneracy index is
retained in orthogonal output states. Its entropy has not been erased.

For an independent product Gibbs battery, all n<=n_good therefore give
the same exact retained channel. Higher initial charge sectors with the
top seed lie in the identity complement. Under the same zero-flag/pointer
premise as (T6), the exact accepted map is again q_multi times the ideal
accepted map, where q_multi=Pr[X<=n_good] and X~Bin(N,p).

An elementary finite-temperature parameter choice is

    beta d=ln 3,       p=1/4,
    N=8L,             integer L>=max{v,512}.

Then n_good=4L-v>=3L. Markov's inequality for 2^X gives

    1-q_multi
       <=E[2^X]/2^(3L)
        =(390625/524288)^L
        <(3/4)^L<2^-128.                              (T13)

The exact integer comparisons are 390625<393216 and
(3/4)^4=81/256<1/2. The initial moments are

    <B>=Nd/4,       Var(B)=3Nd^2/16,       capacity=Nd. (T14)

This optional route needs no pure battery or pure entropy register.
It still requires the top source seed and the other information readies.
Its specified temperature is an additional entry in that option's ledger;
compatibility with the main construction's two temperatures is not assumed.
Its exact finite target is generally global before compilation. The
conserving local compiler can be applied to its complete raw unitary
because the target preserves charge and has the specified one-label
source action. The new injections, larger target, gate count and local
resource ledger must be declared if this option is chosen. The main cold
vacuum construction does not silently rely on this additional target.

## 6. What stationarity and full rank actually rule out

The previous coherence obstruction is consistent with both sharp routes.
They create no independent battery state with coherence between bare
energies. Their source coherences are correlated with compensating
battery charges. Degenerate logical/reference information can still be
transferred under such a stationary additive-energy input.

There are two distinct exact stationarity statements:

1. If all independent preparation factors are Gibbs states at a common
   inverse temperature beta for the same additive energy H_0, their
   product is exp(-beta H_0)/Z. Every complete static H satisfying
   [H,H_0]=0 leaves this density unchanged.
2. A normalizable Gibbs state exp(-beta H)/Z of the complete static
   Hamiltonian H is stationary under its evolution, regardless of a
   decomposition into bare and interaction terms.

These statements concern the complete specified preparation input.
An apparatus marginal at equilibrium can still have nontrivial
correlations with an external reference, and a conserving unitary can
move such correlations. Thus no general impossibility of information
transfer from an arbitrary referenced logical input follows from the
stationarity of that marginal alone. When the logical input is itself
the independent maximally mixed state of degenerate factors, it can be
included in the first statement.

At different temperatures, a product of Gibbs factors still commutes
with H_0 but need not be a function of H_0. A conserving interaction can
then redistribute energy and entropy inside degenerate H_0 sectors.
Bare-energy stationarity alone does not prevent that process.

The original prescribed bare energy in the finite model is a different
operator E_phys=H_0+R_total, while the complete law includes the
interaction correction -R_total. Gibbs factors of E_phys need not form a
stationary density for H. The common-temperature theorem for H_0 cannot
be relabeled as a theorem for E_phys without checking the relevant
commutator. An initial Gibbs state for a different bare Hamiltonian and
its interaction boundary are additional physical information.

For the proposed thermal launch, this distinction can be kept explicit.
With common label offset d, the top source has physical excitation
(b+1)d+r_*. A fuel bit of physical gap (b+4)d+r_* can fund that source,
a cursor of gap 2d and a cold sink of gap d. Its rounded gap is (b+4)d.
The corresponding residual and occupation budget are

    R_total=R_X+r_* n_h,
    C=N_X+n_h,
    0<=R_total<=d C.                                  (T15)

The launch exchanges a fuel excitation for one source-label excitation,
so it preserves C; subsequent label-preserving gates do as well.
The launch itself transfers the residual r_* from fuel to the source.
Whenever the complete generator conserves H_0 and C, the full-raw bound is

    -d C<=U_t^* E_phys U_t-E_phys<=d C.                 (T16)

Its mean bound uses the actual initial <C>, including thermal label
defects and fuel occupation. It does not reuse conservation of N_X alone
through a preparation stage that creates that label. The complete launch
law, thermal probabilities and all remaining resources are established
by the separate assembly, not by (T15) alone.

Finally, a finite full-rank closed input stays full rank under unitary
evolution, and every nontrivial marginal remains full rank. A product of
finite-temperature, finite-dimensional Gibbs states therefore cannot
produce an exactly pure nontrivial ready marginal unconditionally.
This does not exclude approximate readiness, conditional pure branches,
supplied pure stock, or a limiting cold bath. Conditioning retains its
probability and complementary branches in the account.

## 7. Scope and failure conditions

The main result reduces the battery requirement to a cold vacuum resource
by choosing the highest actual source charge and using the exact retained
output contract. Mixed useful fibers preserve that contract, and the
independent ready acceptance identity (T6) makes the remaining battery
weight an explicit success loss. The optional degeneracy construction
provides a different finite-temperature implementation with the tail
bound (T13).

Failure of an entire-space extension in (T1) or (T12), a trace identity
(T4)-(T5), rejection of the claimed identity-complement input, the
multiplicity comparison (T10), or the stated thermal tail bound would
invalidate its corresponding assertion. Applying the source theorem to
an unspecified thermal label mixture or replacing Gibbs(H_0) by
Gibbs(E_phys) without the commutator check changes its hypotheses.

A completion latch is useful only with its complete funded dynamics and
declared read instrument. No finite detector, permanent record, reusable
thermal reset cycle, original spatial confinement or individual-outcome
law follows from these battery results. No scientific executable,
expanded matrix calculation or simulation was run.
