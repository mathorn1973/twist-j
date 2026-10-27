# A common spectral-energy and finite-record extension

**NON-CANONICAL, L1. Conditional analytical candidate; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

This note combines the continuous compensation in [ENERGY.md](ENERGY.md)
with the fixed archive and clock in [RECORD.md](RECORD.md). It supplies
one explicit enlarged model with both a common spectral-energy account
and a finite record window. Its object, carrier and battery Hilbert spaces
are infinite dimensional and its programmed interactions can be global.
It does not retain #1766's finite local hardware or thermal preparation.
The separate finite extension of #1766 is proved in RECORD.md.

## 1. A complete word on the original object and carrier

Take the complete source-loader, two native steps, forward filter and
reversible acceptance-flag word from [#1746 at
01acc42b78f75095587765e9a5b91ee70dc28f37](https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md).
Call this full unitary `U`. Keep its actual infinite object and
token/pulse-position spaces; do not use a periodic finite-box replacement.

The recipe is a finite word of total unitaries. Its loader uses disjoint
transpositions and diagonal phases with identity on the complement; its
controlled object walks and center translations use the original full
unitaries; its finite Boolean computations are reversible XOR/permutation
extensions; and the finite-position/bank tests are spectral predicates
controlling those permutations. Holding the carrier during the filter is
the identity on that factor, as explicitly supplied by that source.
These definitions act on every rejected branch. No accepted-only partial
operator is being called `U`.

The finite auxiliary registers and their specified pure initial states
remain supplied. In particular the source uses 327680 five-state filter
registers, one further five-state loader register, and at most 655392
binary work/flag registers. The complete actual loader includes its
unsuccessful branches; the factor 2/5 is retained in the success bound.
The initial spatial/coin basis state is the source's stated preparation,
not a preparation from equilibrium proved by this note.

Let `F` be the final binary acceptance flag computed by this word, and
`Pi=|1><1|_F` its projector. It includes the source-mark, front and filter
tests through that reversible computation. Its input is zero. The
source's accepted operation transfers all 26 carrier labels to the
receiver memory `M`, retaining the previous memory in the outgoing
carrier, uniformly over their joint logical/reference input.

Add a 26-state archive `A`, which may already be occupied and correlated
with the logical input, and a new pointer `P` initially zero. Neither is
touched by `U`. The full writer is

    V = (I-Pi) + Pi X_P SWAP_(M,A).                       (I1)

Thus the ideal accepted logical map on initial labels (L,M,A) is the
permutation `(L,M,A) -> (M,A,L)`. This is an identity on arbitrary joint
states and references, not copying a label or erasing an old archive.
The complete rejected branch is retained as well.

## 2. Actual object and carrier spectral energies

Use the canonical one-carrier spectral operator

    h_car = beta I_token direct-sum (beta I+i Log_pi V_car)_pulse,
    beta=4*pi/5,                 a=2*arctan(2),
    spec(h_car) subset [beta-a,beta+a].                    (I2)

Here `V_car` in the pulse summand means the unphased two-bank pulse walk;
it is unrelated to the archive writer `V` in (I1). The operator is
identical on all 26 carrier labels. The source and precise cut are in
Public Canon v105's
`notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CAPTURE_SCATTERING.md`,
Section 1.2, at `892a0b11089d34e241e1eb76d2c03247022d18e6`.

For an admitted energy scale `E0>0`, put

    Q = E0 [(H_W+3*pi/10 I) tensor I
            + I tensor (h_car-(beta-a)I)],
    0 <= Q <= Delta I,       Delta=E0(2*pi+2*a).           (I3)

Tensor `Q` with identities on memory, archive, reference and every finite
auxiliary register. All these added information registers have degenerate
bare energy in this selected extension. Their purity, dimensions and
control couplings are still resources. A scalar shift in (I3) makes the
energy nonnegative without changing its object or carrier differences.
The conversion scale and these spectra are admitted, not derived from J.

This is the original object-plus-carrier spectral reading on its complete
one-carrier space, without a safe-window restriction. The unchanged
contact fails to conserve it, by ENERGY.md E1. We now change the joint
contact/program by coupling an explicit compensator; adding a spectator
energy would not suffice.

The receiver's position-dependent label/memory calibration need not
commute with this bare carrier energy. Thus (I3) is not silently
identified with a receiver-conjugated asymptotic energy. Compensation
below applies to the entire word, including that calibration and all
source/control operations, rather than only to the elementary contact.

## 3. Compensation, complete law and free motion

Choose an accuracy `0<e<1` before evolution. Add the battery of ENERGY.md,
with energy multiplication `B` on `L^2([0,L_b])`, where

    L_b >= 2*Delta + pi*Delta/e.                           (I4)

Prepare its normalized sine wavefunction on `[Delta,L_b-Delta]` as in
ENERGY.md (11). Its exact mean energy is `L_b/2`. Its finite capacity
does not make its Hilbert dimension finite. Its purity and energy
coherence are supplied and are not obtained from the thermal bank of #1766.

Let `Gamma(U)` be the complete total-energy-fiber lift defined in
ENERGY.md (8)-(12), and put

    E_tot = Q+B,        U_0=Gamma(U),       U_1=V tensor I_B,
    U_j=I for j>=2.                                      (I5)

The pointer predicate and memory exchange commute with `Q` because their
energies are degenerate. Therefore every operator in (I5) commutes with
`E_tot` on the entire raw space, including the battery boundary fibers.
The initial sine support lies entirely in complete total-energy fibers.
No failed battery shift is discarded. The full word, rather than each
gate independently, has reference-uniform joint error at most `e` from
the ideal `VU` and the initial battery. This is the controlled-translation
estimate, followed by the same exact writer.

Add a 65-state clock in the supplied pure state `|0>`, with zero bare
energy. For `K=64` use the complete history Hamiltonian (R7), with the
edges (I5), and define the actual law

    H = E_tot + H_hist.                                  (I6)

It is positive, bounded and time independent on its whole Hilbert space.
It conserves both `E_tot` and its own complete energy, with

    0 <= H <= [Delta+L_b+129*g/65] I.                    (I7)

The interaction `H_hist` is part of the energy; it is not assumed zero at
the beginning or end. In the initially independent ready clock/battery
state, its full moments are

    <H> = <Q> + L_b/2 + g,
    Var(H) = Var(Q)+Var(B)+64*g^2/65^2.                  (I8)

All finite registers remain in the generator's target word and Hilbert
space, even where their selected bare energies vanish. The first edge
contains the complete compensated word. It is a global interaction
specified by that unitary, not a demonstrated local elementary coupling,
nor an efficient implementation of a long computation in one laboratory
step. No bound on interaction support from #1766 is imported.

Unlike the finite predecessor input, the spatial source and battery need
not commute with `E_tot`. Their free evolution is not omitted:
after tracing the clock, each history is conjugated by
`exp(-it E_tot/hbar)`. This unitary acts only on the object, carrier and
battery. It is the identity on their logical labels, `M,A,P,F`, and the
passive reference. Thus it disappears exactly upon reduction to the
record `A,P` and reference. The full object/carrier endpoint does not
remain fixed, and no such claim is needed for the stored logical record.

## 4. Quantitative accepted record for a prescribed interval

Let `Sigma_e` be the subnormalized accepted archive/reference output of
the completed compensated word, and let `p_e=Tr Sigma_e`. Let `Sigma_0`
and `p_0` denote the corresponding ideal source-word output followed by
the exact exchange (I1). Allow arbitrary initial entanglement of `L,M,A`
with a disjoint passive `R`; `A` is passive only during `U`.

The two-outcome accepted-plus-rejected instrument and the compensation
bound give

    |p_e-p_0| <= e,
    D(Sigma_e/p_e, Sigma_0/p_0) <= e/p_0,                (I9)

provided `e<p_0`. This is the reference-uniform trace-distance convention
of ENERGY.md; the ideal denominator is retained explicitly.

All histories before the writer have `P=0`. Its measurement therefore
rejects those histories without consulting the clock. For the complete
unmeasured evolution and reduction to the archive/reference, exactly

    sigma_rec,acc(t) = w(t) Sigma_e,
    p_rec(t) = w(t) p_e,
    w(t)=Pr[Bin(64,sin^2 theta)>=2],
    theta=g*t/(65*hbar).                                 (I10)

The binomial weights are exact squared norms of a coherent history.
They are not an occurrence law. No intermediate read or postselection
is used in (I10). The normalized accepted archive is independent of `w`
where `w>0`, and obeys (I9). Without conditioning, the complete reduced
record instrument differs from the ideal completed instrument by at
most `e+1-w` in trace distance.

For any chosen finite duration `T_h>0`, fix

    g=65*pi*hbar/(3*T_h).                                (I11)

Throughout `[T_h,2*T_h]`, the exact calculation (R14) gives

    1-w <= 193/2^128 < 2^-120.                           (I12)

For a concrete error choice, take `e=2^-100`. The source's basis-input
acceptance has the explicit margin

    p_0 > p_src = (2/5)(1024/15625)(99/50000)
                > 1/20000 + 1/1000000.                  (I13)

Hence (I9)-(I13) imply throughout this interval

    p_rec > 1/20000,
    D(rho_rec,acc,rho_rec,acc^ideal) < 20000*2^-100.      (I14)

These are bounds for this enlarged source-word model. They do not use
#1766's activation factor 4/15 or its thermal error budget, and must not
be advertised as an improvement with the same resources. Every failed
source and filter branch is included in `U` and in (I9)-(I10).

The source's exact bound `50000/(99*2^29)` on the ideal unwanted
object-band fraction is less than `19/(20*10^6)`. Apply the same uniform
compensation estimate and accepted-plus-reject contraction before
reducing away the object. Its unwanted-band projector commutes with
`Q`, since it is defined spectrally from `W` and center momentum; the
carrier and battery energies act on other factors. Thus its full
accepted-output probability may be compared despite the free motion,
and its actual value remains below `1/10^6` after adding the same
`20000*2^-100` error. This conclusion uses the full-state bound, not
merely the reduced archive estimate (I14). It concerns a commuting
observable, not a stationary complete object output.

At `3*T_h` the history propagator is `-I`. The record marginal returns
exactly to its initial archive and `P=0`, although object/carrier/battery
free phases need not return. Thus the new record still has finite
retention. An external measurement changes the continuation contract.

## 5. What is and is not combined

The enlarged construction supplies actual chosen spectral-energy
compensation, all branches of the complete source program, an occupied
archive exchange and a reference-uniform finite record window in one
static law. It requires a coherent continuous battery, pure auxiliary
readiness, selected degenerate register spectra and global interactions.

The finite construction in RECORD.md instead keeps the entire actual
#1766 input and all its thermal defects, adds only finite archive/pointer/
clock factors, and preserves its declared onsite energy. It does not
identify that energy with `H_W`. The two constructions cannot be silently
spliced into a finite, spatially local, thermally prepared implementation
of the original spectral-energy model.

Decisive failure conditions are a wrong full-word extension of the pinned
source, any nontrivial action of (I3) on the declared logical archive or
pointer, a failure of total-energy conservation by (I5), an accepted
prewriter history with a ready pointer, or a normalized admitted
reference input violating (I9)-(I14). Spatial locality, preparation of
the sine state and new pure seeds, calibrated material realization,
reusable reset, postmeasurement retention and individual-event occurrence
remain unproved. No scientific executable was run.
