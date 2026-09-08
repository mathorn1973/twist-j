# Canon proposal: selected K1 linear metric completion

**NON-CANONICAL / PROPOSED INLINE THEOREM / NO FORMAL RUN / NO ACTIVATION**

```text
object: C-K1-LINEAR-METRIC-CANON-PROMOTION-N
lock: #913
basis_main: f198220abf3b764dba680f76b97f226d212ce85f
authority: ACTIVE Public Canon v81
tag: canon-v81
content_commit: 72863e7014a770eb19d5f54fee0fbf253a6a2cc9
canon_sha256: 940e1d192f729c16fcb74b6e6ac1b8f02d1050326b6164affb276684c8696fbf
canon_bytes: 568924
source_head: 9da8f5c60f2fb7b3cb513ba02d51126798721b71
source_merge: f198220abf3b764dba680f76b97f226d212ce85f
proposed_definition: DEF-K1-LINEAR-METRIC, L1
proposed_claim: K1-LINEAR-METRIC-COMPLETION, T, L1
original_H_O_closures: 0
```

## Decision and evidence route

This proposal promotes one conditional mathematical result, not a physical
metric identification. The selected K1 initialization and continuation
become an explicit definition; its unique rational outputs, all-time matrix
signature and full linear field equations become one theorem.

[The source proof](../V81-K1-LINEAR-METRIC-DECODER-1.md) was reviewed and
merged in [#912](https://github.com/mathorn1973/twist-j/pull/912). The
insert below is self-contained: it supplies the entire ten-word input,
weights, action, derivative, exact first variation and all five amplitude
cases. It needs no unmerged text from #910. In particular it makes no
quadratic coefficient-field or staggering-uniqueness claim.

POLICY section 4 permits a self-contained exact proof in the Canon and
states that independent proof may earn T. This is that route. Neither
the earlier notes CI nor any repository CI on this proposal is described as
a new two-architecture scientific probe. The exact rational checks made
during review audit the displayed proof; they do not infer an all-time
result from a sampled trajectory.

The new definition and theorem are both L1: the output consists of rational
matrices with a proved inertia. No L1-to-L2 physical geometry lift is adopted.
There is no new D or H reading claim. A separate physical identification
would need its own typed scope and gate.

All T/O/D badges within the proposed insert and ledger blocks below are
**proposed fold content**. This file itself grants no public claim status.

## Exact Canon insert

Insert the following complete block at the end of section 14, immediately
before `## 15. Couplings, instruments, and metrology`. Existing section 14
text remains unchanged.

<!-- BEGIN K1 CANON INSERT -->
### DEF-K1-LINEAR-METRIC

This is a definition of one selected L1 mathematical construction. Its
source alphabet, normalization, marked coordinates, initial square and
continuation are explicit inputs, not conclusions derived from the axiom.

Let

```text
W={0010,0011,0100,0101,0110,1001,1010,1011,1100,1101},
r in Z/5,  n in N_0,  w=(w_0,w_1,w_2,w_3).
```

For the optional finite weighted law set
`nu(0110)=nu(1001)=1/6` and `nu(w)=1/12` for each other word. These
positive weights sum to one and are part of the declared K1 input. No
physical preparation or occurrence law is supplied by this declaration.
For `t=0,1` fix

```text
u_t=w_(t+2)-w_t,
b_t(r)=[delta_(r,u_t)+delta_(r,u_t+1)]/sqrt(2),
h_t(r)=b_t(r)^2=[delta_(r,u_t)+delta_(r,u_t+1)]/2.
```

All positions are reduced modulo five; `sqrt(2)>0`. This is the unit
amplitude `a=1` convention. The joint input, which is not replaced by
independent draws, is

| w | nu(w) | (u_0,u_1) |
| --- | --- | --- |
| 0010 | 1/12 | (1,0) |
| 0011 | 1/12 | (1,1) |
| 0100 | 1/12 | (0,-1) |
| 0101 | 1/12 | (0,0) |
| 0110 | 1/6 | (1,-1) |
| 1001 | 1/6 | (-1,1) |
| 1010 | 1/12 | (0,0) |
| 1011 | 1/12 | (0,1) |
| 1100 | 1/12 | (-1,-1) |
| 1101 | 1/12 | (-1,0) |

For `S f(r)=f(r+1)` fix

```text
L=[188I-29(S+S^-1)-65(S^2+S^-2)]/324,
h_(n+1)=(2I-L)h_n-h_(n-1),  n>=1,
H_n(r)=diag(h_n(r),-h_n(r),0),
gamma_n(r)=I3+H_n(r),
g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1).
```

The selected function and finite prefixes are

```text
D_K1: W x N_0 -> (Sym_4(Q))^(Z/5),
D_K1(w,n)=(g_n(r))_r,
P_N(w)=((n,D_K1(w,n)))_(0<=n<=N).
```

Equality is literal equality of all marked matrix entries and counter
labels. The context is fixed: five labelled sites, the plus polarization
displayed above, zero cross component, two initial slices, unit forward
counter and the specified `L`. No source, Fourier-slot, polarization,
position or time average is implicit.

The domain begins with an available four-bit packet. The first output
needs its first three bits and the second and later outputs may use the
whole packet. The counter does not assert a physical acquisition clock.
For `n>=2` the outputs are evolved matrices of this initial packet, not
fresh squares of later native windows. No output feeds the update `U`.
This defines neither a total native-orbit `D_geom` nor a selected physical
reading among all admissible alternatives.

For the comparison action use the Euclidean spatial inner product on
`R^(Z/5)`, the unitary transform
`F_kr=exp(2 pi i k r/5)/sqrt(5)`, and the positive real roots

```text
s=sqrt(5),
lambda_0=0,
lambda_1=lambda_4=(235+18s)/324,
lambda_2=lambda_3=(235-18s)/324,
kappa=(0,sqrt(lambda_1),sqrt(lambda_2),-sqrt(lambda_2),-sqrt(lambda_1)),
D=F^dagger diag(i kappa) F.
```

The marked Fourier slots fix this derivative branch. Conjugate pairing
makes `D` real, `D^T=-D`, and `-D^2=L`. Its entries are real
algebraic numbers; a quadratic coefficient field is not asserted.
Only the rational `L` occurs in `D_K1`.

Write `ell_0` for the lapse perturbation, `N_i` for the shift,
`Delta=E-1`, and `Delta_c^2=E+E^-1-2`. All six independent entries of
the symmetric `H` and `ell_0` are on integer slices. The shift and
`K_ij` are on half slices. The displayed placement is a choice, with no
uniqueness theorem. Only the spatial derivative in direction 3 is
nonzero. Set

```text
K_11=Delta H_11/2,  K_22=Delta H_22/2,  K_12=Delta H_12/2,
K_13=(Delta H_13-D N_1)/2,  K_23=(Delta H_23-D N_2)/2,
K_33=(Delta H_33-2D N_3)/2,  K=Tr(K_ij),

G2(H)=1/2 <D H_3j,D H_3j>-1/2 <D H_33,D Tr H>
      +1/4 <D Tr H,D Tr H>-1/4 <D H_ij,D H_ij>,
R1(H)=D^2 H_33-D^2 Tr H,

A2=sum_n {<K_ij,K_ij>-<K,K>+G2(H)+<ell_0,R1(H)>}.
```

Repeated spatial indices run from 1 to 3, so off-diagonal terms in an
`ij` sum occur twice. The full variables `H,ell_0,N` remain present
until variation. There is no prescribed source. Variation has finite time
support in the interior `n>=1`; the first two slices are initial data.
The sum denotes a local variational principle, not a convergent infinite
action value. Multiplying `A2` by the common nonzero constant
`1/(2 lambda)`, including the convention `lambda=216 pi`, does not
change its stationary equations or fix a scalar-to-tensor normalization.

### K1-LINEAR-METRIC-COMPLETION [T]

For the selected construction `DEF-K1-LINEAR-METRIC`, every word and
counter has one rational output, finite prefixes restrict consistently,
and `mean(h_n)=1/5`. At every site and counter,

```text
-59/100<h_n(r)<99/100.
```

Thus every eigenvalue of `gamma_n(r)` exceeds `1/100`, and
`g_n(r)` has signature `(-,+,+,+)`. The representative
`H=diag(h,-h,0), ell_0=0, N_i=0` solves every interior field equation
of the full displayed quadratic action. The optional finite law `nu`
has exactly one deterministic history pushforward, consistent under all
prefix restrictions. These are L1 algebraic conclusions at the selected
scope.

**Existence, uniqueness and prefix proof.** The initial pair is rational.
A multiplication by `2I-L` and subtraction give exactly one rational
successor. Induction proves the assertion for every finite counter.
Equivalently,

```text
T_L=[[2I-L,-I],[I,0]],
(h_(n+1),h_n)^T=T_L^n(h_1,h_0)^T.
```

The construction has no horizon-dependent choice, proving prefix
restriction. Since `1^T L=0` and both initial sums are one, the scalar
recurrence for `sum h_n` has constant solution one. No spatial zero mode
has been removed. For any finite prefix set `A` the pushed weight is
`sum_{w:P_N(w) in A}nu(w)`. Fibres partition `W`, and prefix
restriction partitions the same fibres, proving normalization and
consistency. This finite weighted-sum fact is not an occurrence theorem.

**Full first variation.** At the stated representative, `Tr H=K=0`,
`H_3j=0`, and `R1=0`. The kinetic first variation is

```text
(1/2) sum_n <Delta h,Delta(delta H_11-delta H_22)>.
```

The spatial first variation is
`-(1/2)sum_n <Dh,D(delta H_11-delta H_22)>`. All terms linear in
`delta ell_0`, `delta N_i` and the other field variations vanish
before any restriction on those variations. Spatial
`D^T D=L` and time summation by parts therefore give

```text
delta A2=-(1/2)sum_n <(Delta_c^2+L)h,delta H_11-delta H_22>.
```

The recurrence makes this zero for every independent, compactly
supported interior variation. It proves the lapse and three momentum
constraints together with all six metric equations. It proves a solution
in the chosen representative, not uniqueness modulo gauge of the full
unrestricted constrained system. Restricting the action afterwards gives
`A2_TT=(1/2)sum_n [<Delta h,Delta h>-<h,Lh>]`.

**Uniform signature proof.**
We prove for every source word, site and `n>=0` that

```text
-59/100 < h_n(r) < 99/100.
```

Consequently every eigenvalue of `gamma_n(r)` exceeds `1/100`, and
`g_n(r)` has one negative and three positive eigenvalues at all times.
This is an all-time analytic bound, not a finite-horizon check.

**Fourier solution.**

The four nonzero eigenvalues listed above lie strictly between 0 and 4.
For `k=1,2`, define `omega_k in (0,pi)` by
`cos omega_k=1-lambda_k/2`, and write `t_k=lambda_k/4`.
Let `Delta_u=u_1-u_0` and

```text
theta_k=2 pi k (u_0+Delta_u/2+1/2-r)/5,
delta_k=pi k Delta_u/5.
```

The paired `k,-k` contribution `y_(k,n)(r)` to the real inverse transform
is exactly

```text
(2/5) cos(pi k/5) [
  cos(theta_k) cos(delta_k) cos((n-1/2)omega_k)/cos(omega_k/2)
 -sin(theta_k) sin(delta_k) sin((n-1/2)omega_k)/sin(omega_k/2)].
```

It agrees with both initial slices and solves their scalar recurrence,
which proves the formula for all `n`. Since the sine and cosine share the
same time argument, its absolute value is bounded by `A_kr`, where

```text
A_kr^2=(4/25) cos^2(pi k/5) [
 cos^2(theta_k) cos^2(delta_k)/(1-t_k)
 +sin^2(theta_k) sin^2(delta_k)/t_k].
h_n(r)=1/5+y_(1,n)(r)+y_(2,n)(r).
```

**Complete amplitude bound.**

Put

```text
F1=(3+s)/50, F2=(3-s)/50,
C_plus=(3+s)/8, C_minus=(3-s)/8,
S_plus=(5+s)/8, S_minus=(5-s)/8,     s=sqrt(5).
```

Here `Fk=(4/25)cos^2(pi k/5)`;
`C_plus+C_minus=3/4`, and `1-C_plus=S_minus`, `1-C_minus=S_plus`.
The elementary bounds `20/9<s<9/4` imply

```text
t1>7/33, 1-t1>3/4, t2>3/20, 1-t2>4/5,
F1<21/200, F2<2/125.
```

Translations and sign reversal of `Delta_u` do not change the set of
angle classes. All nine possible `(u_0,u_1)` pairs are therefore covered
by `|Delta_u|=0,1,2`. The following strict rational bounds cover every site:

| Class | Upper bound for `A_1r^2` | Upper bound for `A_2r^2` | Hence `A_1r+A_2r` is less than |
| --- | --- | --- | --- |
| `Delta_u=0` | `7/50 < (2/5)^2` | `1/50 < (3/20)^2` | `11/20` |
| `|Delta_u|=1` | `693/4000 < (21/50)^2` | `29/300 < (8/25)^2` | `37/50` |
| `|Delta_u|=2`, `(cos^2 theta_1,cos^2 theta_2)=(1,1)` | `7/500 < (3/25)^2` | `21/1600 < (3/25)^2` | `6/25` |
| `|Delta_u|=2`, pair `(C_plus,C_minus)` | `523/3200 < (21/50)^2` | `83/2400 < (1/5)^2` | `31/50` |
| `|Delta_u|=2`, pair `(C_minus,C_plus)` | `782313/1920000 < (16/25)^2` | `10397/480000 < (3/20)^2` | `79/100` |

For `Delta_u=0`, drop `cos^2 theta<=1` in the first term. For
`|Delta_u|=1`, the bracket is a convex combination; bound it by the larger
of its two terms, using `cos^2 delta_1=C_plus`,
`sin^2 delta_1=S_minus`, `cos^2 delta_2=C_minus`,
`sin^2 delta_2=S_plus`.

For `|Delta_u|=2`, `theta_1` is an odd multiple of `pi/5` and
`theta_2=2 theta_1`, giving exactly the three pairs in the table. The
middle pair uses `C_plus C_minus=1/16` and `S_plus S_minus=5/16`.
For the last, most restrictive pair, use

```text
C_minus^2<1/100, S_plus^2<105/128,
C_plus^2<55/128, S_minus^2<49/400.

A_1r^2 < (21/200)[1/75+495/128] = 782313/1920000,
A_2r^2 < (2/125)[275/512+49/60] = 10397/480000.
```

The gaps to `(16/25)^2` and `(3/20)^2` are respectively
`4119/1920000` and `403/480000`, both positive. For clarity, the preceding four rows follow from these explicit substitutions:

```text
Delta_u=0:
 A_1r^2 < (21/200)/(3/4) = 7/50,
 A_2r^2 < (2/125)/(4/5) = 1/50.

|Delta_u|=1:
 C_plus/(1-t1) < 7/8 < 33/20,
 S_minus/t1 < (7/20)/(7/33) = 33/20,
 C_minus/(1-t2) < 1/8 < 145/24,
 S_plus/t2 < (29/32)/(3/20) = 145/24.
 Hence A_1r^2 < (21/200)(33/20) = 693/4000
 and A_2r^2 < (2/125)(145/24) = 29/300.

|Delta_u|=2, pair (1,1):
 A_1r^2 < (21/200)(1/10)/(3/4) = 7/500,
 A_2r^2 < (2/125)(21/32)/(4/5) = 21/1600.

|Delta_u|=2, pair (C_plus,C_minus):
 A_1r^2 < (21/200)[(1/16)/(3/4)+(5/16)/(7/33)] = 523/3200,
 A_2r^2 < (2/125)[(1/16)/(4/5)+(5/16)/(3/20)] = 83/2400.
```

All displayed square comparisons are strict rational inequalities. Thus `A_1r+A_2r<79/100`
uniformly. Adding the unchanged zero mode `1/5` proves the stated interval.

**Boundary of the result.** The map and its continuation are selected
mathematical data. Positive matrices at the chosen amplitude do not
control a perturbative remainder or solve nonlinear gravitational
constraints. The lapse equation here has no second-order TT self-source;
that source needs higher-order action terms and a compatible homogeneous
response. In particular a constant retained mean in this linear vacuum
solution does not solve the source obstruction on a flat compact
background.

The theorem supplies no physical realization of the source or geometry,
no total map on native `U`-orbits, no general three-dimensional manifold,
no physical clock or scale, no Schwarzschild/RW comparison, and no
classification or unique selection of all reading families. The linear
scalar representative is zero; `det(gamma)=1-h^2` is not thereby a
cosmological scalar. No `P_S` or `r_T`, including zero or infinity,
follows. `FRW-INHOM [O]`, `TT-SOURCE [O]` and
`TT-VECTOR-STATE-NORMALIZATION [O]` keep their full registered
decision clauses. The theorem neither adopts nor promotes a physical
reading in `TT-SQUARING-DECODER [D]` or
`PHOTON-SPATIAL-TEMPORAL-TRANSFER [D]`.
<!-- END K1 CANON INSERT -->

## Exact companion-ledger additions

Append the following rows to the respective existing tables. Headers are
included for review only and must not be duplicated during the fold.

### canon/REGISTRY.tsv

```tsv
claim_id	status	scope	canon_section	evidence	falsifier
K1-LINEAR-METRIC-COMPLETION	T	at L1, conditional on DEF-K1-LINEAR-METRIC: for every word in the declared ten-word K1 set at the fixed amplitude a=1, the two local initial squares and h_(n+1)=(2I-L)h_n-h_(n-1) define exactly one rational labelled matrix history for all n>=0, consistent under prefix restriction, with mean(h_n)=1/5 and -59/100<h_n(r)<99/100 for every site and counter; hence gamma_n=diag(1+h_n,1-h_n,1) has every eigenvalue greater than 1/100 and g_n=diag(-1,gamma_n) has signature (-,+,+,+); H=diag(h,-h,0), lapse perturbation zero and shift zero satisfy every interior Euler-Lagrange equation of the displayed full quadratic lapse/shift action after variation; the declared finite K1 law has a unique deterministic prefix-consistent pushforward; the initial square, unit amplitude, marked sites, counter, propagator and output convention are choices, and no global reading uniqueness, physical geometry, native-U decoder completion, nonlinear gravitational solution, 3D manifold, scalar comparison or numerical r_T is supplied	14. The gravitational wave program	inline	fires on an admitted word and counter with no unique rational prefix-consistent output, a spatial mean other than 1/5, a site violating either strict bound, a non-Lorentz emitted matrix, a nonzero interior first variation at the selected solution, or failure of the finite-law pushforward to restrict consistently; physical realization and other readings are outside this conditional L1 theorem
```

### canon/NORMATIVE.tsv

```tsv
item_id	item_type	claim_id	status	layer	gate_ids	statement_source
DEF-K1-LINEAR-METRIC	DEFINITION			L1		canon/CANON.md::DEF-K1-LINEAR-METRIC
K1-LINEAR-METRIC-COMPLETION	THEOREM	K1-LINEAR-METRIC-COMPLETION	T	L1		canon/CANON.md::K1-LINEAR-METRIC-COMPLETION
```

The definition is inventoried here and is not a second Registry claim.

### canon/DEPENDENCIES.tsv

```tsv
item_id	depends_on	relation	basis
DEF-K1-LINEAR-METRIC	DEF-ARCHITECTURE	REQUIRES	the complete K1 word packet, unit normalization, marked coordinates, square, recurrence and output are explicit added mathematical choices within the declared architecture; they are not derived from J
K1-LINEAR-METRIC-COMPLETION	DEF-K1-LINEAR-METRIC	REQUIRES	the theorem is conditional on exactly the fully displayed mathematical input, action and literal output equality
K1-LINEAR-METRIC-COMPLETION	TT-SQUARING-DECODER	BOUNDED_BY	the local algebraic square is fixed in the definition; its use does not inherit or promote the physical tensor dictionary
K1-LINEAR-METRIC-COMPLETION	PHOTON-SPATIAL-TEMPORAL-TRANSFER	BOUNDED_BY	the planar L and recurrence are explicit mathematical choices; no physical photon interpretation or additional lift is imported
K1-LINEAR-METRIC-COMPLETION	FRW-INHOM	BOUNDED_BY	the linear vacuum action supplies no higher-order TT source or homogeneous nonlinear gravitational response
K1-LINEAR-METRIC-COMPLETION	TT-SOURCE	BOUNDED_BY	an initial packet-to-matrix map is not a derived physical emission map or source realization
K1-LINEAR-METRIC-COMPLETION	TT-VECTOR-STATE-NORMALIZATION	BOUNDED_BY	fixed a=1 and a complete finite input law supply no physical scalar comparison, action-unit identification or numerical r_T
```

The BOUNDED_BY edges preserve the lower-status readings and open owners;
they are not logical premises used to prove T. No L1-to-L2 gate is silently
closed by naming a metric matrix.

### canon/EVIDENCE.tsv

```tsv
claim_id	evidence_id	evidence_kind	location	sha256	hash_mode	architecture_requirement
K1-LINEAR-METRIC-COMPLETION	EV-K1-LINEAR-METRIC-COMPLETION	INLINE_CANON	inline	fccb3c0857cb84865abcc9dfd84199d25dc905c361a541bf664104ebe99697f1	registry-scope-sha256-v1	none
```

The evidence digest is the UTF-8 SHA-256 of the Registry scope field,
without a terminating newline:

```text
fccb3c0857cb84865abcc9dfd84199d25dc905c361a541bf664104ebe99697f1
```

The release hash manifest separately pins the full inline proof. There is
no new reproduction directory and no fictitious EXPECTED.txt or RUN.md.

### canon/HISTORY.tsv

If the next sealed fold is v82, append:

```tsv
event_id	event_sequence	event_date	release	claim_id	event_type	previous_status	new_status	scope_sha256	evidence_id	evidence_location	evidence_sha256	rationale
CANON82-DECLARE-K1-LINEAR-METRIC-COMPLETION	1	2026-09-08	canon-v82-candidate	K1-LINEAR-METRIC-COMPLETION	DECLARE	-	T	fccb3c0857cb84865abcc9dfd84199d25dc905c361a541bf664104ebe99697f1	EV-K1-LINEAR-METRIC-COMPLETION	inline	fccb3c0857cb84865abcc9dfd84199d25dc905c361a541bf664104ebe99697f1	Declare the selected K1 rational matrix construction on its self-contained induction, first-variation and uniform Fourier-envelope proofs; no new formal scientific run, physical dictionary adoption or original H/O status change.
```

If another release is activated first, use the actual next release number
and fold date in this new event. The definition, theorem and evidence scope
must be rechecked against that new authority. This is not permission to
rewrite an already committed History event.

## Fold delta and validation

The intended fold has one new T and one new definition, with no existing
scope or status changes. Relative to v81, if folded alone:

| Field | Before | After |
| --- | ---: | ---: |
| Registered claims | 406 | 407 |
| T | 274 | 275 |
| D | 45 | 45 |
| C | 39 | 39 |
| H | 2 | 2 |
| O | 28 | 28 |
| F | 18 | 18 |
| Live H/O | 30 | 30 |

No row changes in `GATES.tsv`, `FRONTIER_PROGRAMS.tsv` or the live
Frontier are proposed. No selection of a new core badge is required.

Suggested changelog text for the new release:

> One new L1 theorem records the explicitly selected K1 linear matrix
> construction. The complete inline proof establishes unique rational
> prefix-consistent output, a retained spatial mean, an all-time Lorentz
> signature bound at the fixed unit amplitude, and all field equations
> of the stated quadratic lapse/shift action. The construction choices
> remain explicit; no physical geometry, nonlinear gravitational
> solution, scalar comparison or numerical r_T is established. All
> existing H/O scopes and statuses remain unchanged.

The separate sealed fold must apply the exact insert and ledger rows,
update the release identity, regenerate the derived Canon views and
`SHA256SUMS`, and pass the existing Canon, ledger, status, gate, policy
and full two-architecture replay checks. A release uses the two frozen
commits permitted by AGENTS section 6: complete content, then the release
form naming that content commit. Authority changes only through the normal
reviewed release and public activation readback.

## Review record

Review of the source at its pinned head checked:

- both initial slices and the mode eigenvalues;
- the complete five-case rational envelope and every strict square margin;
- first variation of the full action, with lapse and shift retained;
- the exact domain, literal equality, finite-prefix restriction and mean;
- the difference between a matrix signature theorem and a nonlinear or
  physical geometric solution.

The source PR changed two Markdown files only and passed the manual
security review and repository CI on both required architectures.
This proposal changes one Markdown file only. It introduces no executable,
measurement payload, external code, secret, workflow, or scientific run.

The nonlinear construction remains the separate
[#911](https://github.com/mathorn1973/twist-j/issues/911) work item.
This promotion does not authorize a new run there or narrow its task.
