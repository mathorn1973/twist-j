# A finite abstract source and occupied-archive model

**NON-CANONICAL, L1. Conditional analytical candidate; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

The finite ladder in [FINITE_BATTERY.md](FINITE_BATTERY.md) removes the
continuous battery, while its general theorem leaves the original system
infinite dimensional. This note also makes the system finite for a
restricted input contract: one fixed spatial source, arbitrary finite
logical registers and a passive reference, and one specified complete
source word. It preserves the ideal endpoint exactly on that input family
before the quantified battery approximation. It does not intertwine the
original spatial dynamics on every input or at every time.

The finite states are specified by spectral projections of the original
operator. Their physical confinement, preparation and local implementation
are not supplied. The result is a finite abstract model of the stated
source/output contract, with an explicit comparison to the original energy.

## 1. Fixed inputs and a finite invariant space for rounded energy

Use the original source word `U` and energy `Q` of INTERFACE.md (I1)-(I3),
at the fixed #1746 input revision recorded there. Split the source system as

    H_S = H_X tensor H_F,             dim H_F = d_F < infinity,
    Q = Q_X tensor I_F,               0 <= Q_X <= Delta I.

`X` contains the infinite spatial, coin, token/pulse-arrangement and bank
degrees of freedom on which that spectral energy acts. `F` contains all
26-valued logical carrier labels, the 26-valued receiver memory, and the
finite program, filter, work and flag registers. With the padded resource
bound used in INTERFACE.md one may take

    d_F = 26^2 * 5^327681 * 2^655392.                    (F1)

Unused registers can be added with identity dynamics. This number counts
the complete raw finite register, including failures, rather than only an
accepted code. The archive, new pointer and new clock are added below.

The spatial input is the source's fixed normalized pure vector `x_0`.
The actual source contract fixes its auxiliary readiness and permits
arbitrary logical/old-memory/reference states. For the next construction
we allow the larger family `x_0 tensor H_F`; hence it includes all of those
inputs and correlations. A supplied spatial state is still a resource.

Choose an energy resolution `d>0` and define

    m = ceil(Delta/d),
    Q_d = d floor(Q_X/d) = d sum_(j=0)^m j P_j,
    R = Q_X-Q_d,                    0 <= R <= d I.       (F2)

All functions are bounded Borel functional calculus on the unchanged
original carrier. Empty `P_j` sectors are allowed. In particular
`[P_j,Q_X]=0`, and `Q_X` is not replaced by a periodic-box logarithm.

Fix an orthonormal basis `f_1,...,f_(d_F)` of `F`. Define `X_f` as the span
of the following explicitly specified finite family of original vectors:

    P_j x_0,
    (I_X tensor <f_b|)(P_j tensor I_F) U(x_0 tensor f_a),
    0 <= j <= m,       1 <= a,b <= d_F.                 (F3)

Let `J:X_f -> H_X` be the inclusion, after choosing an orthonormal basis
of this span. Each vector in (F3) lies in one `P_j` eigenspace. Consequently

    dim X_f <= (m+1)(1+d_F^2),
    P_j X_f subset X_f,
    x_0 in X_f,
    U(x_0 tensor H_F) subset X_f tensor H_F.             (F4)

The third inclusion follows by summing the first family over `j`; the
fourth follows by expanding the second family over `j,b`. Thus they are
exact statements, independent of an approximation to spectral vectors.

Put `q_f=J^* Q_d J`. Since `X_f` is invariant under the self-adjoint `Q_d`,

    Q_d J = J q_f,                   0 <= q_f <= Delta I.

The restriction `U|_(x_0 tensor H_F)` is an isometry between two subspaces
of `X_f tensor H_F` of the same dimension `d_F`. Extend it to a unitary
`U_f` of the whole finite space by choosing any unitary between their
orthogonal complements. Such an extension exists because the complements
have equal finite dimensions. It satisfies

    (J tensor I_F) U_f(x_0 tensor f) = U(x_0 tensor f)
        for every f in H_F.                            (F5)

Tensoring (F5) with an arbitrary passive reference preserves it exactly.
The same is true for mixed states by linearity. To specify one extension,
order the first family in (F3) by `j` and the second by `(j,a,b)`, and
apply Gram-Schmidt with zero residuals omitted. Take the resulting ordered
basis of `X_f` tensored lexicographically with the fixed basis of `F`.
Project this basis separately onto the input and output orthogonal
complements and apply the same ordered Gram-Schmidt procedure. Map their
ordered orthonormal bases to one another, in addition to the specified
action on `x_0 tensor H_F`. This fixes `U_f` before evolution without
assuming a uniqueness theorem. Its complete matrix and laboratory
synthesis have not been computed or supplied.

## 2. What is retained of the original energy

Define the finite bare energy by compression of the *original* observable,

    q_phys = J^* Q_X J = q_f + r_f,
    r_f = J^* R J,                   0 <= r_f <= d I.     (F6)

Both `J J^*` and `R` commute with the `P_j`. It follows that
`[q_f,r_f]=0`. For every finite-system density matrix, the expectation
of `q_phys` equals exactly the expectation of `Q_X` in its embedded
state. This defines the energy comparison rather than identifying two
inequivalent dynamics by their final output.

There are also quantitative operator comparisons:

    ||Q_X J - J q_f|| <= d,
    ||Q_X J - J q_phys|| <= d,
    0 <= J^* Q_X^2 J - q_phys^2 <= d^2 I.              (F7)

For the first, subtract the exact `Q_d` intertwiner and use `||R||<=d`.
For the second, apply `I-JJ^*` to `Q_XJ`; the `Q_d` term vanishes.
The last difference is exactly
`J^*Q_X(I-JJ^*)Q_XJ`, the square of that leakage operator. Thus compressed
and embedded second moments need not agree, but their difference is
bounded as displayed.

The inclusion is generally not invariant under `Q_X` or the actual walk.
For example the elementary Duhamel comparison gives only

    ||exp(-it Q_X/hbar)J - J exp(-it q_f/hbar)||
        <= min(2, |t|d/hbar).                            (F8)

To obtain it, differentiate
`exp[-i(t-s)Q_X/hbar] J exp[-is q_f/hbar]` in `s`, integrate, and use
(F7). The energy-observable estimate below is uniform in time, whereas
the comparison of these free state trajectories is not. Neither estimate
provides operator-norm approximation of every sharp spectral projector.

## 3. A complete finite apparatus and its actual interaction

Use the finite ladder theorem with system energy `q_f tensor I_F` and
the chosen complete `U_f`. Choose integers `L>=2` and `N=2m+L-2`, set

    H_B = C^(N+1),             B = d sum_(n=0)^N n |n><n|,
    eta_(m+r-1) = sqrt(2/L) sin(pi r/L), 1 <= r <= L-1,
    e_B = 2m sin(pi/(2L)) <= pi m/L.                    (F9)

The battery is independent and in the supplied pure sine state. Its
mean energy is `d N/2` and its capacity is `d N`. The complete lifted
unitary `Gamma(U_f)` conserves `E_d=q_f+B` on every raw state. Boundary
fibers are included with their stated identity action.

For every initial `x_0 tensor F/reference` input, the joint vector and
trace-distance comparison to the ideal `U` endpoint embedded through `J`,
with the initial battery retained, is at most `e_B`. Apply the finite
ladder bound to `U_f` and then use the exact identity (F5). The approximation
does not depend on how the orthogonal-complement extension was chosen.
It includes all source failures and their correlations.

Add the same 26-state occupied archive `A`, initially arbitrary and
possibly entangled with `F` and the passive reference, and the same
two-state pointer `P` initially zero. Use the full writer

    V = (I-Pi) + Pi X_P SWAP_(M,A),     Pi=|1><1|_Fflag. (F10)

It is an involutive unitary on all pointer inputs and rejected branches.
It acts only on finite information registers and hence preserves `X_f`
and commutes with both `q_f` and `q_phys`. The old archive is moved into
`M`. No state is cloned or erased. The ideal accepted logical permutation
remains `(L_label,M,A) -> (M,A,L_label)` with the same reference scope as
INTERFACE.md.

Use the 65-state ready clock with `K=64`, zero bare clock energy, and
history edges `U_0=Gamma(U_f)`, `U_1=V tensor I_B`, and `U_j=I` for
`j>=2`. Explicitly,

    a_j = (g/65) sqrt((j+1)(64-j)),
    H_hist = g I - sum_(j=0)^63 a_j
        (|j+1><j| tensor U_j + |j><j+1| tensor U_j^*),
    H = E_d + H_hist.                                   (F11)

Every term commutes with `E_d`. The history conjugation in RECORD.md
therefore proves positivity, boundedness and a complete time-independent
finite generator. Its dimension and spectral bounds are

    dim H_total <= 3380 (N+1)(m+1)(1+d_F^2)d_F,
    0 <= H <= [Delta+d N+129g/65] I.                     (F12)

Here `3380=26*2*65` counts the archive, pointer and clock. The passive
reference is not apparatus hardware. The bound is an existence bound,
not a feasible device size or a count of local gates.

If the prescribed bare energy is the compression of the original reading,
the actual decomposition of this generator is

    E_phys = q_phys+B = E_d+r_f,
    H = E_phys + H_int,        H_int=H_hist-r_f.          (F13)

The spectral correction `-r_f` is part of the supplied interaction. It
cannot be omitted while retaining the same law. `H_int` need not be
positive, although the complete `H` is positive. Its norm is at most
`129g/65+d`; it is generally global. The full conserved Hamiltonian
energy, the exactly conserved rounded bare energy, and the approximately
conserved original compressed bare energy are three distinct observables.

For `Z_t=exp(-itH/hbar)` and every real `t`,

    Z_t^* E_d Z_t = E_d,
    -d I <= Z_t^* E_phys Z_t - E_phys <= d I.             (F14)

Indeed the latter difference is `Z_t^*r_f Z_t-r_f`, and both positive
operators lie between zero and `d I`. This controls every state and every
interval between two times, including correlations and defective inputs.
It does not assert `[H,E_phys]=0`, bound a sharp energy-event probability,
or make the complete embedded spatial trajectory exact. Under the
isometric embedding, the same mean-energy bound compares the original
`Q+B` on the two embedded states.

This is a bound for the complete unconditioned evolution. Selection of an
accepted subensemble can change its energy distribution relative to the
initial whole ensemble; (F14) does not remove that conditioning effect.

With the initially independent ready clock and battery, the complete
energy moments are

    <H> = <q_f> + d N/2 + g,
    Var(H) = Var(q_f)+Var(B)+64g^2/65^2.                 (F15)

The clock off-diagonal terms have zero initial mean and covariance with
`E_d`; their square contributes `a_0^2=64g^2/65^2`. This also explains why
one cannot replace `<q_f>` by `<q_phys>` while ignoring the interaction
correction. An occupied archive has degenerate bare energy in this model;
its dimension and initial state remain counted resources.

## 4. Accepted archive throughout a prescribed interval

The free factor in `exp(-itH/hbar)` is `exp(-itE_d/hbar)`. It acts only on
`X_f` and the battery, so it disappears exactly when reducing to the
archive, pointer and passive reference. It is not discarded in a claim
about the full spatial state. This argument works even when these factors
are entangled, because partial trace is invariant under a unitary on its
traced factors.

Let `Sigma_e` be the accepted archive/reference output of the completed
finite lifted word followed by the writer, and `Sigma_0` the ideal
original source word followed by the same writer. Put `p_e=Tr Sigma_e`
and `p_0=Tr Sigma_0`. Equations (F5), (F9), contractivity, and the
accepted-plus-rejected instrument give

    |p_e-p_0| <= e_B,
    D(Sigma_e/p_e,Sigma_0/p_0) <= e_B/p_0,              (F16)

for `e_B<p_0`, with `D=||.||_1/2`. The ideal denominator and the reference
are included. The finite source-space construction itself adds zero
endpoint error on the specified initial family.

For the unmeasured autonomous law, the clock calculation is unchanged:

    sigma_rec,acc(t) = w(t) Sigma_e,
    w(t) = Pr[Bin(64,sin^2 theta)>=2],
    theta = gt/(65hbar).                                (F17)

This notation denotes exact squared-norm weights, not an individual-event
occurrence law. The pointer is zero in both prewriter histories, so its
read does not consult the clock. Every later history has the same written
archive. All branches remain in the complete state and its accepted and
complementary outputs.

For any prescribed finite `T_h>0`, choose

    g = 65 pi hbar/(3T_h).

Throughout `[T_h,2T_h]`, `1-w<=193/2^128<2^-120`. At `3T_h` the history
propagator is `-I`, and the archive/pointer marginal returns exactly to its
initial state. Its correlations with the passive reference also return.
This is finite availability, not a permanent halt or postmeasurement
retention guarantee. The enlarged window changes coupling and latency.

Choose, for example, `e=2^-100` and

    L = ceil(pi m/e),              N=2m+L-2.             (F18)

Then `e_B<=e`. The inherited source margin
`p_0>(2/5)(1024/15625)(99/50000)>1/20000+1/1000000`
therefore gives throughout the window

    p_rec > 1/20000,
    D(rho_rec,acc,rho_rec,acc^ideal) < 20000*2^-100.      (F19)

These bounds require the original source's specified auxiliary readiness,
with arbitrary admitted logical/old-memory/archive/reference correlations.
They do not apply to arbitrary raw `F` states merely because (F5) does.
These are the original-source resources, not #1766's thermal activation
factor. The selected `d` controls energy resolution separately
from the record error. For any requested positive energy tolerance `delta`,
one may take `d=delta`, `m=ceil(Delta/delta)` and (F18). Equations (F12),
(F14) and (F19) then give finite explicit dimension, a uniform energy drift
bound `delta`, and the stated accepted record accuracy.

There is also a precise finite reading of the original unwanted-band test.
Let `P_bad` be its projector in INTERFACE.md and put

    A_bad = J^* P_bad J,            0 <= A_bad <= I.      (F20)

Tensor identities on the finite registers are implicit. This is generally
an effect, not a projector, because `P_bad` need not preserve `X_f`.
It reproduces the original test's expectation on embedded states. Since
`[P_bad,Q_d]=0` and `Q_d J=J q_f`, one has `[A_bad,q_f]=0`. It therefore
commutes with the rounded free motion; it also commutes with the flag and
writer, which act on separate finite registers. The joint completed-word
bound, followed by the same accepted instrument and this effect, gives
throughout the window

    u_rec <= 50000/(99*2^29) + e_B/p_0 < 1/10^6         (F21)

for the choice (F18), using the source margin stated in INTERFACE.md.
This is a pullback of one specified commuting test. It does not identify
every original spectral projector with a finite projector, or supply a
material implementation of this generally global effect.

## 5. Boundaries of the finite realization

The supplied resources are the spectral span (F3), the chosen complete
unitary extension, finite but potentially enormous registers, pure sine
battery and ready clock/pointer/program, degenerate information-register
energies, and global controlled couplings with the correction in (F13).
No theorem here confines the original walk to a finite spatial box or
prepares these spectral vectors thermally. The stationary-resource
obstruction in FINITE_BATTERY.md shows why the coherent sine preparation
cannot be silently supplied by an energy-invariant thermal input alone.

Its stronger bounded-source result applies even if this one source is
allowed to supply its initial coherence: if its preparation energy has
width at most `md`, all other resources are initially independent and
stationary, and the preparation conserves their additive energy, then

    D(sigma_B,|eta><eta|) >= max(0,1-(4m+2)/L).          (F22)

The finite `q_f` source has that energy-width bound. For (F18),
`(4m+2)/L<=6e/pi<2e`, so every such unconditional preparation output is
at distance greater than `1-2e` from the required packet. The source
may be consumed in this argument; requiring its return is unnecessary.
Additional sources with wider aggregate energy coherence, correlated
initial resources, an external phase reference or a different energy
contract change the hypotheses. No general impossibility of preparation
with those extra resources is claimed. Clock and pointer purity in
degenerate sectors is a separate entropy resource, not ruled out merely
by this energy-coherence argument.

The exact finite-invariant-carrier obstruction in ENERGY.md is preserved:
(F5) is an equality on one source family for one complete word, whereas
(F7)-(F8) explicitly permit failure of invariance under original spectral
evolution. The universal finite-battery counterexample likewise concerns
exact original-energy conservation; this model declares the nonzero
resolution `d` and the interaction correction.

Falsifiers within this note's hypotheses include failure of a dimension
or span inclusion in (F4), failure of the endpoint/reference identity (F5),
failure of a bounded-operator comparison (F7) or (F14), or violation of the
accepted archive bounds for an admitted prepared source. A local material
implementation, thermodynamic readiness, reusable reset, postmeasurement
continuation and individual-event occurrence remain separate obligations.
No new scientific executable or expanded matrix calculation was run.
