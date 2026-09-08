# TT normalization: the observable data and the next source decision

**NON-CANONICAL. Definition and source audit, 2026-09-08.**

Owner: `TT-VECTOR-STATE-NORMALIZATION [O]`. This note supplies the exact
quadratic-observable contraction a candidate must determine and audits the
suggested TT/Born source. It selects no state, starts no formal probe, and
does not calculate a physical `r_T(k)` or close the owner.

Authority read: public v81 at
`82d536a71025032d6dd4093db61ecb9f31990250`, with content commit
`72863e7014a770eb19d5f54fee0fbf253a6a2cc9`. The local Canon is 568924 bytes,
SHA-256 `940e1d192f729c16fcb74b6e6ac1b8f02d1050326b6164affb276684c8696fbf`,
matching `STATUS.md`. Public release and collision checks belong to the
coordinating session; no formal scientific verifier was run for this note.

## 1. Exact owner, existing evidence, and a correction to the proposed route

The [registry](../canon/REGISTRY.tsv) closes the owner positively by a public
vector-doublet normalization yielding a numerical `r_T(k)`. Its negative
clause requires **every admissible normalization** to violate the registered
TT identities or require an extra free dimensionless input. Failure of one
candidate, or two admitted candidates with different predictions, does not
satisfy that universal clause. Without independent selection or equivalence,
different predictions leave the physical conclusion open under `POLICY.md`.

The earlier work is already incorporated. The
[public preregistration](../probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1/PREREG.md)
names issue #407 and branch `notes/c-tt-vector-moment-underdetermination-1`
at `09182ec9b7b4a7649cc3fda5d56c4703ed5a6b52` as the source of incubation
candidates -1 and -2. Its accepted verifier and the -2 verifier have the same
Git blob, `330eec9f8c959a1c1574b55da0f8c626e0d1e26c`. The public proof and
[result](../probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1/RESULT.md) already
establish the six-law comparison and fixed-modulus fourth-cumulant boundary.
Repeating them is not the next closure task. This audit uses that public
proof and result as its evidence for the incorporated comparison.

The supplied Czech closure plan and the exact referenced
`MAPA-OD-AXIOMU-K-FYZICE_2026-09-08_CZ.md` were read as proposals. Map section
10.8 describes K1 verbally as a monomial-verb/Born lift following TM-SYM2.
It names K2 and K3 but does not define them. Their missing definitions must
not be invented or replaced by the theorem's unrelated labels `A,B_m`.
The map's proposed `NONUNIQUE` closure for different surviving `r_T` values
does not match the current owner's decision clause. Its BK18 example is not
adopted here as a current measurement or a preregistered threshold.

## 2. The concrete contraction to be supplied

The registered square and `POL-READ` in
[Canon section 14](../canon/CANON.md) are

```text
q_+(v) = v_1^2 - v_2^2,       q_x(v) = 2 v_1 v_2,
h = q_+ + i q_x = (v_1 + i v_2)^2.
```

For a candidate classical real doublet field, write
`p=(x,t)`, `p'=(y,s)`, `v(p)=(v_1(p),v_2(p))`. The expectation below must
come from the candidate's declared state law or justified averaging rule;
the symbol `E` does not itself supply a physical ensemble. Define

```text
Q^+ = [[1,0],[0,-1]],          Q^x = [[0,1],[1,0]],
m_ij(p) = E[v_i(p) v_j(p)],
M_ij;lm(p,p') = E[v_i(p) v_j(p) v_l(p') v_m(p')],
mu_a(p) = sum_ij Q^a_ij m_ij(p),
Gamma_ab(p,p') = sum_ij,lm Q^a_ij Q^b_lm
                  [M_ij;lm(p,p') - m_ij(p) m_lm(p')].
```

These are elementary expansions of
`Gamma_ab = E[(q_a-mu_a)(q_b'-mu_b')]`, with `a,b in {+,x}`.
They assume neither zero mean of `v`, Gaussianity, stationarity, isotropy,
nor independence. Subtraction distinguishes fluctuation power from a
coherent mean or zero mode; a candidate must state which its observable uses.

**A sufficient observable-level input is `(mu_a,Gamma_ab)` on the points
actually consumed by the readout.** A complete law for `v`, or realizable
second and fourth raw moments giving that contraction, supplies it. The
whole fourth-moment tensor is more information than this observable needs:
different admissible tensors may have the same contraction. Equality of the
final normalized spectrum is the relevant equivalence, not uniqueness of
the full state. An arbitrary positive-semidefinite `Gamma` is insufficient
unless it is realizable by an admitted doublet and consistent with its other
moments and registered identities.

In the complex notation the corresponding data are the connected kernels
`E[delta(v(p)^2) conjugate(delta(v(p')^2))]` and, if the component-resolved
readout consumes it, `E[delta(v(p)^2) delta(v(p')^2)]`. The latter is a
fourth-order pseudo-covariance of the **square**. A zero pseudo-covariance of
the original vector does not set it to zero. A frozen polarization trace may
need only the first kernel; that reduction must follow from the output map.

### Equal time versus two times

For a translation-invariant spatial law and an equal-time direct reading,
the tensor input is the spatial transform of `Gamma_ab((x,t_*),(y,t_*))`
at the declared epoch. Equal-time **spatial fourth moments at that epoch**
can suffice. It would be incorrect to demand unequal-time moments for every
possible direct `h=v^2` output.

If the prediction evolves or time-filters the quadratic field, it consumes
two-time data. For example, **conditional on a separately supplied linear
readout** `H_lambda(k)=sum_(a,t) R_(lambda,a)(k,t) delta q_a(k,t)`, expansion
gives

```text
E[H_lambda(k) conjugate(H_lambda'(k))]
 = sum_(a,b,t,s) R_(lambda,a)(k,t)
     conjugate(R_(lambda',b)(k,s)) Gamma_ab(k;t,s).
```

This is an accounting identity for a supplied map, not an asserted TWIST-J
propagation law. The continuum analogue needs its declared integration
measure and convergence assumptions. An initial equal-time law plus a
complete deterministic evolution can derive these two-time moments;
equal-time marginals at each time alone do not specify their coupling.
A full four-independent-time law is unnecessary for this instantaneous
quadratic source; the needed degree-four data have the two-pair form above.
If a different readout consumes a wider law, it must name that dependence.

The existing finite theorem instead supplies
`S_w(k)=sum_r E[w_r conjugate(w_0)] zeta_5^(-kr)` on `X=Z/5`.
The labels `r,k` there are finite sites and characters. They are not a
physical time, cosmological wave number, propagation rule, or evaluation
epoch. A numerical finite `S_w` is not yet a numerical physical `r_T`.

## 3. Normalization that does not disappear in the ratio

After the field/readout contraction, a candidate must give a total conversion
to its dimensionless physical tensor power `P_T(k)` and the scalar power
`P_S(k)` in the **same** declared convention, and then

```text
r_T(k) = P_T(k) / P_S(k),      P_S(k) > 0 on the claimed domain.
```

The conversion fixes the action and field normalization, Fourier convention,
polarization sum, spatial and temporal coordinates, evaluation epoch and
mode/pivot correspondence. If an action is used to determine a state, its
boundary/initial state and its state-selection rule also have to be supplied.
An action coefficient alone is not a stochastic or preparation law.

The amplitude issue is visible before dynamics: `v -> a v` gives
`q -> a^2 q` and quadratic fluctuation power `-> a^4` times its original
value. A normalized Born distribution fixes relative weights; it does not
by itself fix `a` relative to the scalar perturbation. A candidate may show
that a scale cancels between tensor and scalar sectors, but may not assume
the cancellation. Every surviving dimensionless coefficient needs a source
independent of the target `r_T`, not a fit that repairs it afterwards.

The Canon's `Z_L2=1/2` and `mu=1` in `TT-QUADRATIC-GERM [D]` are explicit
Stage B inputs; that row expressly supplies no action-germ or pullback
derivation. `CONFORMAL-PREFACTOR [D]` fixes `K_chi5=1/(864 pi)` only at the
homogeneous L5 scope; `FRW-INHOM [O]` still owns the inhomogeneous extension.
`NS-TILT [H]` is a tilt, not a scalar fluctuation amplitude or state law.
None of these can be substituted for `P_S(k)` without a separately justified
bridge. The future candidate must either supply that bridge at its claimed
scope or state an independently sourced scalar comparison and the resulting
conditional scope. No observed scalar amplitude is silently adopted here.

## 4. Does an existing source already fill the input?

| Audited source | What it supplies | Exact missing TT connection |
| --- | --- | --- |
| Native `Omega,U`, Canon core and section 2 | A complete deterministic state update | A typed field map `V(source,x,t)->(v_1,v_2)`, the relevant initial/averaging law, physical coordinates and normalization; deterministic evolution alone does not choose these |
| The six finite laws `A,B_0,...,B_4`, section 14 | Complete equal-time finite laws, with different fourth moments and squared spectra | Independent admission/selection as a physical doublet, temporal coupling or justified direct epoch law, action and scalar comparison; the six laws are not an exhaustive admissible TT class |
| `Law_W`, Canon section 3 | A frozen finite-window marginal predicate on a typed Route A target, with no larger-window or limiting claim | It neither gives a TT doublet map nor the required joint fourth-order field law; the associated entropy bridge remains open |
| `TM-SYM2-PHYSICAL-MEASURE [D]`, section 13 | A specific monomial lift and total word measure with a common pushforward across 48 selector charts | No TT field/source map or TT fourth-order temporal law; its physical dictionary is bound to its own source and lift |
| TT square, polarization and Stage B bookkeeping | Polynomial identities and declared dictionary inputs | No state/action normalization or scalar power; the text states this explicitly |

The K1 analogy has a precise type gap. In the TM-SYM2 source,
`v_t=delta_t+delta_(t+1)` is a five-component **coefficient vector** and
`F(v_t)_k=zeta_5^(tk)(1+zeta_5^k)` is its finite Fourier transform.
The TT `v=(v_1,v_2)` is a **real doublet** whose complex square is read as
plus/cross. Reusing the letter `v` does not identify these objects. A K1
candidate must explicitly specify which object supplies the doublet, how
the translation label `t`, Fourier slot `k`, and native word time enter it,
and how multiple points are jointly read. The stationary W3 marginal and
the Born conditional `(1/2,1/2)` do not fill that map.

The TM-SYM2 negative control already shows why that gap matters: equal
Fourier moduli admit a different phase lift with different coefficient Born
weights. TT similarly cannot import a chosen lift from modulus data alone.
TM-SYM2 is a precedent for an explicit, bounded dictionary adoption with
output invariance, not permission to transport its measure to another type.

The fixed-modulus boundary must retain its hypotheses: zero mean,
`P_xx=0`, deterministic `|v_x|^2=a^2` with `a>0` imply fourth moment `a^4`
and cumulant `-a^4`, contradicting the Isserlis value `2a^4`. Wick closure
is inadmissible **in that class**. This is not a theorem excluding all
Gaussian states in every enlarged class. An enlargement still needs its
own independently justified admission and may not erase the old result.

## 5. Next bounded decision and routing

The required **typed source-and-field decision for K1**, before
an `r_T` computation, must name an existing source law or explicitly propose a
new dictionary input; give the actual `V` map with point/time semantics;
derive `(mu,Gamma)` on its consumed domain; and show where the amplitude,
action/readout conversion and scalar comparison come from. A generic
instruction to take a Born square is not that deliverable. If K2/K3 are to
be compared, obtain their exact source definitions first; no three-way class
is currently specified by the supplied map.

The subsequent [finite K1 construction](V81-TT-K1-SOURCE-MAP-1.md) now
supplies one actual map and complete two-window moment law, using an
explicit unitary Fourier normalization. It resolves that finite construction
task; admission as a physical TT normalization still requires the action,
coordinate/readout and scalar comparison at the candidate's claimed scope.

Candidate admission is decided before target values are inspected:

1. Its source, map, joint law and parameter provenance fill the concrete
   contraction above and obey the registered square, double-cover,
   determinant and propagation identities at their stated scope.
2. Its physical and cross-layer identifications are explicit. The current
   owner is `NOT_APPLICABLE` in `NORMATIVE.tsv`; the map's shorthand
   `L5 -> L6` cannot assign the whole candidate's layers. Each actual lift
   needs its named typed gate under policy before formal work.
3. Its scalar denominator and output convention are defined and nonzero on
   the frozen domain; nuisance choices either provably cancel from `r_T`,
   are independently selected, or remain visible open inputs.
4. A claimed comparison family has an explicit membership and completeness
   scope. Same-output alternatives may survive. Inequivalent outputs with
   no selection stay open; a failed member rejects only that member.

An admitted, normalized public physical reading with a definite `r_T(k)`
can be proposed for positive closure at its supported status after the
required public review and gates. An exact identity violation rejects the
candidate. A new ungrounded free coefficient prevents a claim that the
normalization is closed. Only a proof covering **every admissible**
normalization can meet the current owner's negative clause. Missing source,
temporal coupling, action, denominator, or selection is `STOP`, not a new
no-go theorem. A fresh public claim and immutable preregistration/verifier
pin are required before any formal scientific gate execution.

This decision is now narrower than "find fourth moments": specify and
justify the actual source-to-doublet map. No audited current source already
provides that complete TT normalization, and no law has been chosen here
to manufacture a preferred tensor ratio.
