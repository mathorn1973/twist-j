# Finite energy compensation, retained output and consumptive reuse

**NON-CANONICAL. L1. Proposed conditional theorem text for a later v106
fold; no active Canon claim or registry status is changed.**
Author: A. M. Thorn. License: Apache-2.0. Reservation: #1802.

The three statements below have different carriers and control contracts.
R1 is a general finite-battery theorem. R2 is an endpoint channel identity,
with a separately stated driven storage realization. R3 is one specific
finite autonomous implementation of two uses of the frozen thermal core.
None identifies that core with the original-port apparatus of PR #1777,
the original six-pentit rule, or the later rotor-clock construction.
Proposed status is **T for the explicit conditional mathematical statement**,
subject to the synthesis review and normal public fold, not physical admission.

## R1. Finite coherent compensation and a nonaccumulating energy bound

Let Q be a bounded self-adjoint operator on a Hilbert space H, with
`0 <= Q <= Delta I`, Delta>0. H need not be finite dimensional.
Fix d>0, put `F=floor(Q/d)`, `Q_d=dF`, `m=ceil(Delta/d)`, and let
`P_r=1_{r}(F)` for `0<=r<=m`, including any zero projections.
For any integer N>=2m introduce a battery with levels `n=0,...,N`,
`B=d sum_n n|n><n|`, and rounded total energy `K_d=Q_d+B`.

For `m<=k<=N`, define `J_k psi=sum_r P_r psi tensor |k-r>` and
`P_good=sum_{k=m}^N J_k J_k^*`. For every unitary U on H set

```text
Gamma(U)=sum_{k=m}^N J_k U J_k^*+(I-P_good).
```

Then Gamma(U) is unitary on the complete system/battery space,
`[Gamma(U),K_d]=0`, and `Gamma(U)Gamma(V)=Gamma(UV)`.
On every incomplete total-energy sector it is exactly the identity.
No out-of-range battery shift or rejected sector is discarded.

Put `L=N-2m+2` and prepare the normalized battery vector

```text
eta_n=sqrt(2/L) sin(pi(n-m+1)/L),   m<=n<=N-m,
eta_n=0 otherwise.
```

For every normalized system/reference vector psi, and every unitary U,
with identity action on the arbitrary passive reference,

```text
||Gamma(U)(psi tensor eta)-(U psi) tensor eta||
  <= 2m sin(pi/(2L)) <= pi m/L.                       (R1.1)
```

The same upper bound, capped at one, holds in trace distance for every
mixed system/reference input, retaining the battery and reference.
For any finite word `U_s...U_1`, first use the representation identity;
(R1.1) applies once to its complete product, with the same battery.
No intermediate restoration or independent replacement of eta is assumed.

Let `E=Q+B`. For every unitary Z commuting with K_d,

```text
-d I <= Z^* E Z-E <= d I.                             (R1.2)
```

In particular, if a specified autonomous Hamiltonian commutes with K_d,
this bound holds at all times and between every two times, without a
factor proportional to elapsed time or word length. It concerns the
unconditioned state and does not transfer through successful-outcome
conditioning without a further argument. It is not exact conservation of E.

For any prescribed `0<epsilon<1`, choose
`L=max(2,ceil(pi m/epsilon))` and `N=L+2m-2` before evolution.
The battery has dimension `L+2m-1`, capacity dN and mean energy dN/2;
(R1.1) is at most epsilon. This is finite battery size, not a claim that
the original system has finite dimension or that the spectral gates are local.

**Proof.** Complete total-charge sectors are orthogonal copies of H,
which proves the full-space representation identities. Extend eta by
zero on the integer line. Its one-step overlap is cos(pi/L), hence
`||(T_1-I)eta||=2 sin(pi/(2L))`. Factor the compensating shift into
m threshold-controlled one-step shifts. In their commutator expansion
each term has norm at most this number because `||[Pi,U]||<=1` for an
orthogonal projection Pi. The shift difference commutes through every
other controlled shift, proving (R1.1), also with arbitrary references.
Purification gives the mixed-state statement. Finally
`E=K_d+D`, `0<=D=Q-Q_d<=dI`; both `Z^*DZ` and D belong to that interval,
proving (R1.2). See [S1], Sections 1-5, equations F1-F15.

The pure coherent eta and the exact spectral couplings are supplied
resources. Stationary additive-energy preparation cannot silently supply
eta: [S1], Section 7 proves the corresponding coherence obstructions.
R1 uses no unaccepted TWIST-specific source theorem.

## R2. Exact export, replacement and the retained N-use channel

Fix a finite core `D=T tensor I`, with S qubits and fifteen specified
information-input qubits I. Let Omega_T be its supplied hardware state,
independent of the information and reference, and let U be its complete
one-use unitary. In the frozen application [S2], U is the propagator at
the stated completion time of the core in [S3]. Its input code is the
tensor product of the three fixed 26-label injections into five-qubit
blocks for logical label, old memory and archive. "Admitted" means
support in this `26^3`-dimensional code, with arbitrary correlations.
The output B comprises
seven specified physical sites, initially in T: five archive qubits,
a pointer P and a completion latch L. Define the complete channel

```text
E(sigma_I)=Tr_(D\B)[U(Omega_T tensor sigma_I)U^*].
```

E includes dormant, rejected and defective components. It is not the
normalized accepted branch. Physical input sites and physical output
sites are distinct even when they carry the same logical data at
different stages.

For every integer N>=1, supply N full S-qubit cartridges F_j with
identical corresponding spectra and fresh hardware Omega_T, and N
seven-qubit equal-spectrum output slots O_j. Hardware in all N+1
packages is independently supplied. The information inputs I_0,...,I_N
may have any joint admitted valid-code density rho with a passive
reference R; they need not be independent. Slots initially have arbitrary
independent occupied states. They are destinations, not passive references.
For each j, run U on D, SWAP B with O_j, then SWAP all of D with F_j,
including after every rejected or dormant attempt.

After the word, tracing only the spent cartridges and keeping the core,
all outputs and R gives exactly

```text
rho_final = Omega_(T_D) tensor
            (E^(tensor N) tensor id_(I_N,R))(rho),    (R2.1)
```

with I_N relabelled as the original physical I sites. Fresh hardware is
independent of all retained systems, also after a positive-probability
selection on the tape. The next information input can remain correlated
with earlier outputs and R. Their displaced contents, old core states
and all their correlations remain in the spent cartridges. The count is
`(N+1)S+7N` stock qubits, including N+1 information inputs; a controller
and any routing are additional resources. The final cartridge provides
the final reset; omitting it changes the stated endpoint.

**Proof.** A full SWAP transfers the joint B:R state to O:R without
cloning. A subsequent full-core SWAP replaces only the independently
prepared hardware factor and relabels the possibly correlated next input.
Iterating this identity proves (R2.1), before and after any retained
reference. It adds no error to the one-use channel. See [S2], Sections
1-4, U1-U12. A selected multi-use estimate must normalize its complete
joint event, not multiply separately normalized marginal fidelities.

**Storage and work contract.** With `E_O=d n_L` and accepted effect
`Pi_O=n_L n_P`, exact maintained isolation preserves the accepted
archive/reference density for arbitrarily long time, since E_O is dI
on that accepted subspace. The entire output is retained up to its known
free evolution. A driven realization uses equal-spectrum pair SWAP
pulses `lambda sum_k(I-SWAP_k)` for duration `pi hbar/(2lambda)`.
It retains their explicit free-energy factors, switching work and
transport requirements. This does not assert permanence under the
unchanged coupled writer. See [S2], Section 6, U16-U22.

R2 is an algebraic channel theorem for supplied U, Omega_T and slots.
Interpreting E as the particular accepted source instrument additionally
requires the frozen core premises listed below. Regenerating spent stock
is a separate operation, not a consequence of restoration of T_D.

## R3. A bounded local two-attempt realization with a finite read window

Fix the exact S-qubit core H_D, its valid input code and its complete
thermal channel E in [S3] and [S4], Section 1. Its three hardware packages
use the actual two temperatures chosen for the successor; a colder
choice is not equated with the earlier numerical hardware state.
Let `E_*` be the largest physical core onsite gap, g_D its fixed
propagation scale and d its energy-bin width. Fix
`J_*=E_*+g_D+d` and `g_out=J_*/4` before enlarging the construction.

There is one finite, positive, time-independent Hamiltonian H_local on
qubits at distinct points of the three-dimensional integer lattice,
specified in [S5]. Every displayed summand has support on at most nine
sites, Manhattan radius at most 256, norm at most J_*, and each site
belongs to at most 64 summands. Positivity and conservation hold on the
full raw space, including invalid data and multiple-cursor sectors.
No exact pure routing bank is supplied. The two temperatures apply to
all specified hardware factors; unknown information is a separate input.

This single H_local implements the complete endpoint word
`R_2 X_2 V R_1 X_1 V`, where `V=exp(-i tau H_D/hbar)` at its frozen
completion time, X_i exports the seven-site output and R_i replaces
the whole core. It simulates these endpoints rather than retaining the
old continuous H_D trajectory as an additional simultaneously running law.

For every joint admitted input on I_0,I_1,I_2 and every passive R,
define Xi by the right side of (R2.1) with N=2. The construction is
fixed independently of that input. Let K_out be its finite outer path
length and set `T_hold=pi hbar(K_out+1)/(3g_out)`. For every
`t in [T_hold,2T_hold]`, condition on its physical final-completion
latch F. The joint state of both fixed output blocks, hardware at the
original D sites, next input and R satisfies

```text
D_tr(rho_actual|F=1(t), Xi) < 2^-96.                 (R3.1)
```

Completion probability is at least `p_out w(t)-eta`, where
`p_out>=1/3`, `w(t)>=1-(3/4)^(K_out/2)` and eta is the explicitly
counted outer cold-defect bound. After fixing the complete inventory,
choose `beta_c d >= [120+ceil(log_2 C_new)] ln 2`, where C_new is the
number of cold positive-gap sites in [S5], L18. Then `eta<2^-120`.
No high unconditional success
probability is inferred from an active-history tail estimate.

For output acceptances `Q_i=n_(O_i,L)n_(O_i,P)`, let A_id be the
complete ideal-ready accepted one-use map of [S4], Section 8. Put
`J_id=(A_id tensor A_id tensor id)(rho)`, `q_id=Tr J_id`.
The frozen uniform one-use premise gives `q_id>=(1/60000)^2`, even
for correlated inputs. For the actual event `F Q_1 Q_2` at every t
in the same window,

```text
Pr(F=1,Q_1=1,Q_2=1) > 1/12000000000,
D_tr(rho_actual|F Q_1 Q_2,
     Omega_T tensor J_id/q_id) < 2^-67.              (R3.2)
```

The ideal-ready target is the prescribed sharp-fiber source-output
instrument, not a separately prepared coherent spatial source or a
product of the two normalized output marginals. One shared outer
activation appears once. No one-use unwanted-band estimate is imported
after the stronger two-output selection.

The first output has a positive-width availability interval before
the first reset, and every subsequent forward instruction preserves
its fixed physical sites. Its completed-export weight in the active
comparison history exceeds `1-2^-128` throughout
`[T_hold/2,2T_hold]`. The clean outer history returns at `3T_hold`
and reverses export and reset as well. This is a finite retention
statement, not permanent storage or an intervention-invariant recurrence.

With P instruction layers, the physical inventory is exactly
`(3S+14)(P+1)+K_out+3` qubits; the forty-five information qubits are
included. Two cartridges, both occupied outputs, all transport copies,
clock sites, thermal donors and cold defects are counted. Writing
`E_phys=Q+R_payload` and `U_t=exp(-it H_local/hbar)`, the construction obeys

```text
H_local=Q+H_hist >= 0,
H_int=H_hist-R_payload,
[H_local,Q]=[H_local,C_all]=0,
0<=R_payload<=d C_all,
-d C_all<=U_t^* E_phys U_t-E_phys<=d C_all.           (R3.3)
```

For its prepared input, `<C_all><1+2^-120`. This energy statement is
unconditioned and retains every copied source/fuel residual. It is not
an intertwining theorem for the original full spatial energy Q of a
different model. Reset consumes stock; it renews neither the tape,
cartridges, thermal banks nor the whole outer controller.

**Proof route.** [S6], Sections 1-4 gives the full-raw product formula,
including onsite phases, with per-use error `<2^-120`; the two-use word
has error `<2^-119`. Exact matched-spectrum SWAPs give R2's channel
identity. [S5], Sections 1-8 proves the distinct-site routing, separate
transfer/program edges, full-space positivity, incidence bounds and
thermal inventory; the working core and both cartridges return to their
original sites. [S4], Sections 5-8 uses the exact binomial history,
the complete accepted-plus-rejected instrument inequality and its
joint success denominator to prove (R3.1)-(R3.2). [S5], Sections 6-10
supplies (R3.3), the full energy moments and finite capacities.

## Exact sources, review scope and unresolved dependencies

All source URLs below pin immutable bytes. [S1]-[S3] are at the frozen
#1768 head; [S4]-[S6] are at the frozen #1770 head. Their publication-time
"pending" notices do not supersede the later exact-revision reviews.

- [S1: FINITE_BATTERY.md](https://github.com/mathorn1973/twist-j/blob/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/FINITE_BATTERY.md), Sections 1-7.
- [S2: REUSE_RESET.md](https://github.com/mathorn1973/twist-j/blob/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/REUSE_RESET.md), Sections 1-7.
- [S3: THERMAL_RESOURCES.md](https://github.com/mathorn1973/twist-j/blob/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/THERMAL_RESOURCES.md) and [THERMAL_CLOCK.md](https://github.com/mathorn1973/twist-j/blob/811daddc3b2f085ee5bc6f50261ac95a4c11fe44/notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/THERMAL_CLOCK.md), the specified raw core, input-code, thermal and retained-output contracts.
- [S4: TWO_USE_CHANNEL.md](https://github.com/mathorn1973/twist-j/blob/e23b0a08ed24667dfbedf948588211f977428d8e/notes/C-LOCAL-TWO-ATTEMPT-REUSE-N/TWO_USE_CHANNEL.md), Sections 1-9, C1-C25.
- [S5: LOCAL_CONTROLLER.md](https://github.com/mathorn1973/twist-j/blob/e23b0a08ed24667dfbedf948588211f977428d8e/notes/C-LOCAL-TWO-ATTEMPT-REUSE-N/LOCAL_CONTROLLER.md), Sections 1-10, particularly L14-L17.
- [S6: LOCAL_COMPILATION.md](https://github.com/mathorn1973/twist-j/blob/e23b0a08ed24667dfbedf948588211f977428d8e/notes/C-LOCAL-TWO-ATTEMPT-REUSE-N/LOCAL_COMPILATION.md), Sections 1-4.

The finite-battery/source-family layer has [review 5642195943](https://github.com/mathorn1973/twist-j/pull/1768#pullrequestreview-5642195943)
at d138517; its files remain unchanged at 811daddc. The local, thermal
and reuse layers have [review 5642715718](https://github.com/mathorn1973/twist-j/pull/1768#pullrequestreview-5642715718)
at 811daddc. The two-attempt successor has [review 5642782034](https://github.com/mathorn1973/twist-j/pull/1770#pullrequestreview-5642782034)
at e23b0a08. Each accepts its stated conditional L1 mathematics, not an
unqualified acceptance of all predecessors or a Canon promotion.

The following inherited source dependencies are **not independently
accepted wholesale by those reviews**. At this synthesis readback their
PRs have no separately submitted mathematical review. Retain them as
explicit frozen premises of the particular core instantiation:

| Dependency | Exact frozen input | Role |
| --- | --- | --- |
| #1746 | [01acc42b](https://github.com/mathorn1973/twist-j/tree/01acc42b78f75095587765e9a5b91ee70dc28f37) | Complete forward source/filter contract. |
| #1761 | [32c17259](https://github.com/mathorn1973/twist-j/blob/32c17259c4baf40bb6d08b521adc642956b57e94/notes/C-THERMAL-REGISTER-PREPARATION-N/HAMILTONIAN.md), Sections 3-5 | Local history template; adaptations are proved in #1768. |
| #1764 | [6670ac27](https://github.com/mathorn1973/twist-j/tree/6670ac274888927be3429a463966da41ca8d2e8b) | Thermal work/clock predecessor. |
| #1766 | [d978a455](https://github.com/mathorn1973/twist-j/tree/d978a455ef01506a9b8eb68c296e6ca89703710a) | Common-temperature endpoint and its supplied resource contract. |

No proposed theorem supplies original-rule synthesis, material calibration,
an autonomous detector of individual events, replenished unlimited use,
or permanent closed finite memory. Repository CI is integrity evidence;
these claims are analytical. No new scientific execution supports this file.

## Suggested registry scopes, for the coordinator's separate proposal

| Label | Proposed narrow mathematical scope | Failure witness |
| --- | --- | --- |
| R1 | Finite coherent battery: reference-uniform whole-word compensation, exact rounded conservation and all-time unconditioned original-energy drift at most d. | An admitted input violating R1.1, or a K_d-conserving unitary violating R1.2. |
| R2 | Exact occupied-output export and N-use channel with complete consumptive hardware replacement; isolated accepted storage under its stated driven contract. | A valid correlated input violating R2.1, omitted waste information, or change of the accepted isolated output under its stated free Hamiltonian. |
| R3 | The frozen finite two-attempt local thermal device: stated joint channel/acceptance bounds, fixed-site finite retention and residual-inclusive resource account. | Violation of R3.1-R3.3 or the fixed support/radius/incidence/strength bounds, omitted stock, or a later forward instruction acting on the saved first output. |
