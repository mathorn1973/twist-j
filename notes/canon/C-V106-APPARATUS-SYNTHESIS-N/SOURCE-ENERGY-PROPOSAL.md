# Proposed source, apparatus and energy statements

**NON-CANONICAL / L1 / PROPOSED CONDITIONAL T.**
Author: A. M. Thorn. Date: 2026-10-27. Reservation: issue #1802.
This is proposed wording for a later reviewed fold, not a registry entry,
source acceptance, Canon promotion or release. Public Canon v105 at
`892a0b11089d34e241e1eb76d2c03247022d18e6` remains the authority.

The four nominations below use source texts, not merely their review
summaries. PR #1777 is frozen at
`191ab035be823bd9d6fdc9effba81528fa026e49`; PR #1779 is frozen at
`c2b06d3ee52778f804da1f84ba9f963bae1ad46e`.
The separate [PASS 24/24 review of PR #1779][R79] covers that source's
conditional scope. It does not accept all predecessor premises.
In particular PR #1772 at
`3abf054e435e31c51e6e50528b09fe3cf7cffe13` is not independently accepted
by this synthesis. Its premises are exposed in nomination 4, which is
held as **nomination-with-open-premise-disposition**, outside the proposed
accepted core until their disposition is resolved.

## 1. ACTIVE-ISOSPECTRAL-RECORD

**Proposed conditional T, L1.**

### Definitions and exact scope

Fix the Public Canon v105 homogeneous capture-current-record unitary
`U_rec`, its receiver at coordinate 100, the calibrated carrier/memory
label exchange, and the active-contact definitions in [A, §0][A].
These include contact angle `g=2pi/5`, scalar phase `beta=4pi/5`, contact
rotation `[[3/5,-4/5],[4/5,3/5]]`, and the stated object and pulse steps.
Keep their scalar phases also in controlled operations.

The source seed is
`chi_s=|R=97,r=0,iB; y=97,token,label=0>`, where
`B=(e2-e3)/sqrt(2)`. For any normalized old-memory/reference vector `Xi`,
put `chi=chi_s tensor Xi` and define

```text
D = U_rec^2-U_rec^(-2),
Z = (39521+154 sqrt(5))/15625,
psi_± = (I±D)chi/sqrt(Z).
```

The source preparation and equal-spectrum identity admit all 26 receiver
labels and arbitrary passive references. The fresh-write conclusion
below requires the old memory to lie in
`K_mem=span(d1,...,d25)` and uses
`P_W=I tensor |d0><d0|_mem tensor I_ref`.
The exact finite-source identities and complete gate actions are those
in [A, §§1–5][A] and [S, §§1–4][S]; they are the stated construction data
and source proof obligations, not an admission of every predecessor claim.

### Proposed statement

For every such normalized input, both preparations have norm one,
identical initial configuration probabilities, and exactly equal complete
spectral measures of `U_rec`:

```text
dmu_psi+(z) = dmu_psi-(z)
           = (3-z^4-z^(-4)) dmu_chi(z)/Z.
```

Consequently every fixed real Borel reading `f(U_rec)` has the same
distribution in both states; all its existing moments agree. This
includes a chosen bounded positive scalar logarithm but does not select
that logarithm as the physical energy. Both states have an active contact
already at their first forward step. For old memory in `K_mem`, their
receiver is initially unwritten.
After exactly three unchanged forward steps, for every input in `K_mem`
and every reference correlation, the fresh-write probabilities satisfy

```text
Delta = ||P_W U_rec^3 psi_+||^2-||P_W U_rec^3 psi_-||^2
      = 65536(48533-10985 sqrt(5))
        /[5^9(39521+154 sqrt(5))] > 1/50.
```

The statements extend to mixed inputs by purification. Complete fixed
preparation gates and a coherent two-setting selector act on the source
and helpers without an oracle for the unknown memory state. The word
`W_prep=-Aop R_in Aop* S_good Aop` in [S, §3][S] prepares the plus source
exactly and restores the helpers and old memory at its endpoint. The
selector `|0><0| tensor I+|1><1| tensor (-F)` retains its relative phase
on coherent setting inputs. This is a supplied-gate result; the six-pentit
rule has not been shown to synthesize those gates.

**Proof route.** Skew-adjointness of `D` and
`|1+d(z)|^2=|1-d(z)|^2` prove the spectral identity. The conserved exchange
symmetry and the exact source return `12/25` show that `Dchi` vanishes
on the two occupied seed ports, proving equal configuration populations.
Finite propagation makes the three-step receiver difference the single
cross term in [A, (A4)–(A5)][A]. The complete contact-path decomposition
gives (A8), while the four-step return gives (A8b); substitution proves
(A10). The subspace identity `P Aop* Pi Aop P=P/4` proves the preparation
word on the whole 26-dimensional memory input subspace.

**Falsifiers and limit.** A missing controlled scalar phase, a missing
contact history, a wrong normalization, or a memory-dependent source
gate defeats the corresponding claim. Equal spectral law does not mean
identical state or identical readout. This does not prove outcome
occurrence, an incoming-unbound capture experiment, permanent retention,
or the thermal preparation of the supplied gates.

## 2. THERMAL-ORIGINAL-PORT-APPARATUS

**Proposed conditional T, L1.**

### Implementation premises and finite inventory

Assume the complete energy-fiber gate lifts and routed finite occupation
implementation of [L, §§1–3][L], the source word of [S][S], and the
explicit instantiation of [P, §§1–5][P]. These are substantive supplied
implementation premises. Their native origin is not inferred from
nomination 1. The fixed occupation intertwiner, including its gauge,
is retained. Both completed programs return their payload to the original
physical ports; future transport copies are restored without tracing them
away. Reference systems need not have finite dimension.

For every integer `k>=8` and fixed scales `epsilon,g>0`, use

```text
n=2208, M=2209, r=2(k+ceil(log2 M)+1),
G_star=512 n^4 4^n,
P1=M(2r^2-r)+G_star, P2=3G_star, P=P1+P2,
S=7726+2Mr, G=17643 epsilon.
```

Program 1 resets the helpers and prepares the source, including the
retained phase choice. Program 2 applies the three original forward steps.
Each payload row has 1102 four-level occupation sites with energies
`epsilon*(0,2,2,8)`, 4414 ladder sites with levels `0,...,26468`,
2210 zero-gap qubits, and `2Mr` donor qubits of gap `G`.
There are `P+1` payload rows. With outward route counts `r1,r2` and layout
extent `Y0` fixed by [C, §§1–4][C], choose

```text
B>=max(r1+1,r2+1,8192,32(k+3),4Y0+4), K=12B.
N_total=S(P+1)+K-r1-r2+3.
```

The last three sites are fuel and two flags; `K-r1-r2` is the physical
cursor-site count, while `K` counts its nonvacuum levels. Shared qutrit
colors are not independent qubits. The ladder dimension 26469 and its
direct `0 <-> 17632` launch transition are counted local resources.

All noninformation inputs are the stated independent Gibbs factors,
including future rows, seed occupations, ladders and cursors. The old
memory/reference and an optional coherent zero-gap setting are information
inputs. The original `M` helpers initially have state `I/2`, not zero.
Hot fuel and reset donors have `beta_h G=ln 2`. After fixing the complete
inventory, set

```text
C_eff=3(1089+1102P)+2*4414(P+1)+Mr(1+2P)+K+2,
beta_c epsilon=(k+1+ceil(log2 C_eff)) ln 2.
```

### Proposed statement

For that fixed inventory there is one explicitly specified, positive,
time-independent Hamiltonian `H=H0+H_prop` on the entire finite raw space,
with `[H0,H_prop]=0`. Each displayed term has at most nine physical sites,
Manhattan radius at most 1024, incidence at most 64, and norm at most
`J=max(26468 epsilon,g)`, in the declared three-dimensional layout.
These are termwise bounds, not a norm bound `||H||<=J`.

`H0` includes every occupation, donor, ladder, fuel, flag and cursor
energy. Launch conserves it by the exact identity `17643=8+17632+3`.
The full raw-space terms, including multiple cursors and dirty helpers,
are those of [C, (S15)–(S21)][C]. All of `H0,H_prop,H` are conserved.
The initial product commutes with `H0`, but generally not with `H`:
the hot/cold population imbalance at launch is the explicit resource.
Its full interaction energy is included, rather than discarded as a
switching cost. Preparing this boundary state for an already interacting
apparatus is itself a supplied initial-state contract.

Let `D(rho,sigma)=||rho-sigma||_1/2`, `z=2^(-k-1)`,
`T_h=pi hbar(K+1)/(3g)`, and
`p(t)=sin^2(g t/[hbar(K+1)])`. Define the predetermined source window
by `11/48<=p(t)<=13/48` on the first outward half-period. For every
admitted setting/memory/reference input, the first physical flag has
probability `>1/4` there, and the conditional source channel at the
original ports differs from the ideal source isometry by `<6z`.
For every `t in [T_h,2T_h]`, the separate final flag has probability
`>1/4`, and its conditional source/receiver/setting/reference output
differs from `Ad_(U_rec^3) o P_src` by `<6z`.
At `k=40` the receiver contrast between the two separately supplied
settings is `>1/100`, for old memory supported in `K_mem`.

Both windows are cuts of the same unmeasured evolution. This statement
does not assert the final bound after measuring the first flag. All
dormant, unsuccessful-reset and cold-defect branches remain in the full
state. The source-preparation channel admits all 26 memory labels; only
recognition of a fresh write uses the 25-label restriction.

The finite energy account includes exact initial means and variances.
With the complete diagonal and hopping parts `H=M0-A` of [E, §5][E],

```text
<H>=<M0>, Var(H)=Var(M0)+Tr(rho_th A^2).
```

The full square keeps overlapping-edge cross terms. For any counted
thermal bank with initial product `tau_D`, its unconditional output
`sigma_D` obeys

```text
sum_(i in D) beta_i Delta<E_i>
 = S(sigma_D)-sum_(i in D)S(tau_i)+D_rel(sigma_D||tau_D).
```

These are finite identities, not a report of enumerating the apparatus.
The cold-ground comparison state returns exactly at `3T_h`; the actual
thermal state returns within trace distance `<=z`. That return also
undoes the source and new record. No retained-output renewal follows.

**Proof route.** Complete energy-fiber lifts and matched-spectrum whole-site
SWAPs conserve `H0`. Two colored excursions restore arbitrary future-row
states at both endpoints. Positive edge blocks and potentials establish
full-space positivity. On the comparison history the generator is the
spin-`K/2` tridiagonal matrix, hence has the binomial clock law. Cold
defects cost `eta<=z`; the donor-inclusive helper reset costs `xi<z`.
The two binomial tails and complete-instrument normalization yield
[T, (T20)–(T26)][T]. Conservation and the finite Gibbs identity give
the energy account; the same clock law proves the stated return. For the
actual thermal return use the source's positive mixture
`rho_th=(1-eta)rho_0+eta rho_bad`: the first component returns exactly,
so the trace distance to the initial mixture is at most `eta<=z`.

**Falsifiers and limit.** An uncounted donor, incorrect whole-site SWAP,
incomplete positive edge, missing thermal color, or omitted conditioning
denominator defeats the corresponding statement. The conserved energy
is this apparatus's `H`, not `Q=E0 f(U_rec)`. Exact couplings, thermal
banks and the declared geometry remain supplied. This is not a compact
device, a derivation from six pentits, outcome selection or permanent
storage. Improved accuracy increases inventory and time at fixed `g`.

## 3. COMPACT-ACTIVE-RECORD-APPARATUS

**Proposed conditional T, L1.**

Assume nomination 1's exact source and contrast identities, the complete
source word, and its admitted-prefix period-15 agreement in [S, §7][S].
This agreement is not equality of infinite and finite spectral logarithms.
Use the eleven data register dimensions
`15,15,15,4,3,26,26,3,2,2,2`, respectively for
`R,r,c,o,a,l,m,q,b,s,d`, of total dimension `657072000`.
The pointer `d` starts at zero; old memory and its reference are arbitrary.
Fresh-write contrast retains `K_mem`.

### Proposed statement

The eight complete factors in [M, §2][M] exactly implement the finite step:

```text
U_fin=P_beta Gamma S_R S_r E_rec Q_p M2 C.
```

Expanding all twelve controlled forward/inverse source calls gives
`12*8+17+2+3*8+1=140` complete register gates. The last gate is
`|d0><d0|_m tensor X_d+(I-|d0><d0|_m) tensor I_d`.
The full word implements source preparation, coherent setting, three
original steps and the pointer isometry, retaining both outcomes and
all reference correlations. No controlled scalar phase is dropped.

Pad to `K=560` edges and add one 561-level clock, initially at zero.
For every fixed `g>0`, the history construction [M, (C5)][M] is positive
on the full raw space. Put the twelve register sites at `0,...,11`.
Each Hamiltonian term touches at most nine sites and has diameter at
most 11, norm at most `g`; the clock has incidence 1121. These are
register-site bounds in this declared placement, not nearest-neighbor
occupation locality, twelve qubits or two-qubit gates.

The total Hamiltonian spectrum is exactly
`{g(2s+1)/561: s=0,...,560}`, with data multiplicity `657072000`.
For the supplied zero clock and every data/reference input its full
energy law has weights `binom(560,s)/2^560`, hence
`<H>=g` and `Var(H)=560g^2/561^2`.

For every `t in [T_h,2T_h]`, where `T_h=561pi hbar/(3g)`, the unfinished
weight is `<epsilon_c=(3/16)^140<2^(-280)`. Conditional completion gives
the exact full endpoint, including the pointer. Unconditioned reduced
data are within trace distance `epsilon_c` of that endpoint. Since no
earlier gate changes the zero pointer, its unconditioned two-setting
contrast is `Pr(done)*Delta>1/100`, without clock postselection.
The full unmeasured input density returns at `3T_h`, undoing the output.

The strict contrast survives either sufficient error budget of [M, §6][M]:
initial joint trace-distance error `<=1/8000` and either complete unitary
gate errors `<=1/1120000` per program gate with exact clock, or complete
static generator error `<=3g/(64000*561)`. A final pointer-effect error
`<=1/4000` is also allowed. These are sufficient mathematical tolerances,
not achieved fabrication precision or per-term allowances in the second case.

**Proof route.** Receiver conjugation changes only the pulse edge factor,
giving the eight-factor identity. The exact word count includes inverses,
selector correction and pointer coupling. Prefix conjugation reduces the
full history operator to `gI-(2g/561)S_x`, proving positivity, spectrum and
the binomial law. The padded tail gives the uniform read window. Zero
pointer weight before the final gate proves unconditioned contrast.
Telescoping or Duhamel bounds control the two stated error budgets.

**Falsifiers and limit.** A missing factor, extra required register,
boundary crossing on an admitted prefix, or failure of full-space
conjugation defeats the construction. Source, helpers, pointer and clock
readiness are supplied here; nomination 2's thermal preparation and
incidence-64 theorem do not transfer to this changed encoding. The new
`H` is not an extension of `Q`, and `g` is not identified with `E0`.
The final instrument, physical outcome and replenishment remain open.

## 4. ORIGINAL-ENERGY-LOCAL-ERROR-FLOOR

**PROPOSED CONDITIONAL T, L1; nomination-with-open-premise-disposition.**
This item is not placed in the proposed accepted core while its specific
PR #1772 premises remain unresolved. Naming the energy below does not
turn those proof-dependent premises into accepted definitions.

### Frozen target and open predecessor premises

Use the original full one-pair/one-carrier sector, all carrier and memory
labels, and its actual product occupation isometry `V_occ`, including the
fixed object gauge and receiver calibration. Let `E0>0` and
`Q=E0 f(U_rec)`, with `f(exp(-i theta))=theta` for `0<=theta<2pi`.

The following are explicit open-premise dependencies from [B, §§2,4–5][B]:
(i) the complete original spectrum is the full unit circle, and
(ii) under `S_N:(R,r,c)->(R,r+N,c-N)`,
`S_N* Q S_N -> E0 f(U_f)` strongly for the specified free operator.
The second statement uses strong convergence of the steps and their
adjoints **and absence of a free spectral atom at the cut**; polynomial
functional calculus alone does not establish it. Premise (i) is used for
sharp attainment, while (ii) is used in the lower-bound proof.

### Proposed statement, conditional on those premises

For every finite integer `rho>=0` and every selfadjoint raw interaction
`Q_tilde` made from physical-site terms of diameter at most `rho`, suppose
its compression `K=V_occ* Q_tilde V_occ` is bounded and its coded matrix elements
are limits of finite partial sums. Then

```text
||K-Q|| >= pi E0,
||Q_tilde V_occ-V_occ Q|| >= pi E0
```

whenever the latter uniform action norm is defined. The bound holds on
the entire original sector, not just on the prepared source family.
It needs neither translation invariance, positivity, charge conservation
nor a fixed interaction strength. Additional such restrictions narrow
the comparison class. Uniform passive-reference extensions inherit the
bound by compression to any fixed normalized reference vector.

In the bounded comparison class allowing scalar zero-displacement terms,
the floor is sharp: `K=pi E0 I` attains `||K-Q||=pi E0`.
This is not a claim that the scalar reproduces the dynamics. A raw
zero-vacuum extensive comparison requires the separate domain qualification
in [G, §4][G]; no globally bounded raw realization is inferred from it.

**Proof route.** Disjoint pulse occupation subbanks force every compressed
matrix element moving the pulse more than `rho` sites to vanish. Use the
assumed strong free-energy limit, then weak compactness and translation
averaging. The comparison becomes a finite trigonometric polynomial in
pulse momentum, continuous there for almost every other momentum. The
specified free energy has a transverse jump `2pi E0` on an open momentum
neighborhood. Fubini and the two one-sided limits force error at least
half that jump. Full-circle spectrum supplies sharp attainment.
See [G, §§1–4, (E1)–(E11)][G].

**Falsifiers and limit.** A false strong Borel limit, an unaccounted cut atom,
failure of the physical displacement zero, or a crossing only on a
measure-zero slice defeats the proof route. This excludes uniform
approximation of this scalar branch in this encoding, even with arbitrary
finite diameter. It does not exclude source-specific approximation,
another branch, explicit branch registers or changed encodings.
The sharper prepared-source diameter-two certificate in PR #1791 is
not nominated here: correction of its external synopsis remains pending.
No assertion that diameter three suffices is made.

## Dependency and disposition table

| Proposed registry identifier | Required source/dependency scope | Proposed disposition |
| --- | --- | --- |
| ACTIVE-ISOSPECTRAL-RECORD | v105 capture-current-record operator; PR1777 [A] and [S], including exact phases and source normalization | Proposed conditional T, pending acceptance of this wording and its dependency map |
| THERMAL-ORIGINAL-PORT-APPARATUS | Previous nomination; PR1777 [L], [P], [C], [T], [E]; declared geometry, levels, full gates and Gibbs boundary data | Proposed conditional T; own energy and implementation only |
| COMPACT-ACTIVE-RECORD-APPARATUS | First nomination; PR1777 [S, §7]; PR1779 [M] | Proposed conditional T; distinct compact register encoding |
| ORIGINAL-ENERGY-LOCAL-ERROR-FLOOR | v105 occupation code; PR1779 [G]; explicitly open PR1772 [B] full-spectrum and strong-Borel-limit premises | nomination-with-open-premise-disposition; outside proposed accepted core |

The four identifiers were checked against the current v105 public registry
without a collision. They are nominations only. No registry, Canon,
frontier, predecessor file or scientific executable is changed by this note.

[A]: https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-FINITE-PHASE-OCCUPIED-RECORD-N/ACTIVE_EQUAL_SPECTRUM.md
[S]: https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-ORIGINAL-PORT-SOURCE-PREPARATION-N/SOURCE_CIRCUIT.md
[L]: https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-ORIGINAL-PORT-SOURCE-PREPARATION-N/LOCAL_REALIZATION.md
[P]: https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-AUTONOMOUS-ORIGINAL-PORT-SOURCE-N/PROGRAM_RESOURCES.md
[C]: https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-AUTONOMOUS-ORIGINAL-PORT-SOURCE-N/STATIC_CONTROLLER.md
[T]: https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-AUTONOMOUS-ORIGINAL-PORT-SOURCE-N/THERMAL_CHANNEL.md
[E]: https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-AUTONOMOUS-ORIGINAL-PORT-SOURCE-N/ENERGY_ACCOUNT.md
[M]: https://github.com/mathorn1973/twist-j/blob/c2b06d3ee52778f804da1f84ba9f963bae1ad46e/notes/C-COMPACT-ENERGY-RECORD-N/COMPACT_MODEL.md
[G]: https://github.com/mathorn1973/twist-j/blob/c2b06d3ee52778f804da1f84ba9f963bae1ad46e/notes/C-COMPACT-ENERGY-RECORD-N/ENERGY_BRIDGE.md
[B]: https://github.com/mathorn1973/twist-j/blob/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N/SPECTRAL.md
[R79]: https://github.com/mathorn1973/twist-j/pull/1779#pullrequestreview-5648760727
