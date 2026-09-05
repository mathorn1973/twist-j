# Born rule: conditional derivation and the occurrence boundary

**NON-CANONICAL / ANALYTICAL DERIVATION / RESULT-EXPOSED / NO FORMAL RUN.**

Owner: [issue #844](https://github.com/mathorn1973/twist-j/issues/844).
Basis: public main `079a26c1d7649145584bfdd739322edc8b42d6e8`, ACTIVE Public
Canon v76; content `07910adb8418742bf52a0d204577b84b38009b18`, Canon SHA-256
`c151a19997dba95d78836c46f38463ab2735ae1c98674f87888d519d7a500112`, 420539 bytes.
No Canon, registry, gate, completed probe or physical owner status changes.
No new scientific program, verifier, formal gate or experimental payload was
executed or opened for this note. Its derivations precede any formal probe pin.

The result of this attempt is a conditional theorem: **an independently
realized, normalized and effect-noncontextual additive measurement law, with
certainty on its independently identified pure preparation, must have the
Born form.** The proof derives the quadratic response rather than assuming it.
It does not derive those physical premises from J or U. A separate exact
current-to-count argument explains when deterministic counts inherit quadratic
weights and why the present cold apparatus does not yet provide the complete
event law.

This is a specialization of the standard effect-additivity route, not a claim
of a new general derivation of quantum mechanics. [Busch](https://arxiv.org/abs/quant-ph/9909073)
obtains the density-operator form from probabilities on effects.
[Caves, Fuchs, Manne and Renes](https://arxiv.org/abs/quant-ph/0306179), sections I
and III, explicitly cover rational fields and distinguish measurement
noncontextuality as an assumption. The self-contained proof below uses rational
symmetric forms in the actual QDD metric; no assertion about a physical complex
Hilbert space or an all-projector Gleason theorem is imported into the finite
registered piston domain.

## 1. Existing inputs and the additional premise

The relevant [Canon](../canon/CANON.md) supplies, at its exact algebraic scope,

```text
G = I_4 - e e^T/5,     e=(1,1,1,1)^T,
m(z)=z^T G z,         P_LOW=e e^T/4,     P_HIGH=I-P_LOW,
rho_z=z z^T G/m(z),   z != 0.
```

G is positive definite, with eigenvalues 1/5 on span(e) and 1 on its
orthogonal complement. The finite balanced carrier has 624 supported sources
and one zero source. LOW has rank one and HIGH rank three: two labels do not
make this carrier a qubit. Rational extensions below are mathematical domains,
not an extension of the adopted decoder or physical apparatus class.

The [reservoir partition result](../probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/RESULT.md)
gives one explicit positive partition of G including the residual energy. It
does not supply every effect or its realized occurrence. The following are
also insufficient as premises of a derivation from the architecture:

- MEASURE-BORN-VERB is a dictionary, not a proof of occurrence.
- J-SIMPLEX-QUADRATIC-SUPPORT-RIGIDITY assumes a quadratic positive response;
  its conclusion cannot justify that same assumption.
- QDD-MECHANICAL-EVENT-SAMPLER and QDD-EVENT-CONTEXT-BANK construct exact
  words from supplied weights; they do not select the weights or a physical
  sampler.
- The [A/U5 freeze](canon/C-J-A-U5-COINCIDENCE-OWNER-FREEZE.md) keeps finite
  pair cardinalities separate from physical realization and self-location.

The new premise tested logically here is stronger than additivity of subsets
of an already given record set. It concerns the same independently identified
effect across different complete measurement implementations, including
equivalent refinements of an outcome. No Born-calibrated state/effect
tomography is allowed to certify that premise independently.

## 2. Exact conditional theorem on rational effects

Fix any nonzero z in Q^4 and m=z^T G z. Define the entire, infinite rational
form interval

```text
E_G(Q) = {M in Sym_4(Q): 0 <= M <= G}.
```

Inequalities are positive-semidefinite inequalities of real quadratic forms.
The associated G-self-adjoint operator is E=G^(-1)M. A complete measurement
in this abstract class is any finite tuple (M_1,...,M_k) in E_G(Q) whose sum
is G. Repeated equal effects and zero effects are admitted. Equality of effects
is literal equality of M, not an equality inferred from outcome frequencies.
M and E are different types and are never interchanged in a trace formula.

Suppose one scalar assignment f_z:E_G(Q)->[0,1] satisfies:

1. **Normalization:** f_z(G)=1.
2. **Effect noncontextuality and refinement additivity:** the same M has the
   same value in every admitted complete tuple, and
   f_z(M+N)=f_z(M)+f_z(N) whenever M,N>=0 and M+N<=G.
3. **Independent pure-preparation certainty:** for
   M_z=G z z^T G/m, one has f_z(M_z)=1.

The assignment may be proposed as a probability or as an existing limiting
frequency. That interpretation and its existence are additional physical
inputs. For now it is only a bounded scalar function. The theorem assumes no
quadratic form for f_z, no continuity, no random seed, no source ensemble and
no law of large numbers. It applies pointwise to each supported balanced
source without asserting ownership of every rational preparation.

Then, for every M in E_G(Q),

```text
f_z(M) = z^T M z / (z^T G z)
       = tr(rho_z E),       E=G^(-1)M.                    (1)
```

### 2.1 Additivity forces a positive linear functional

First f_z(0)=0. Splitting an effect M into n identical effects M/n gives
f_z(M/n)=f_z(M)/n. For any rational positive-semidefinite A choose a positive
integer n with A<=nG; such n exists because G is positive definite. Put

```text
L(A)=n f_z(A/n).
```

This is independent of n. If another integer r also works, comparison through
A/(nr) gives n f_z(A/n)=nr f_z(A/(nr))=r f_z(A/r).
For positive A,B choose n with A+B<=nG and apply partial additivity after
division by n. Thus L(A+B)=L(A)+L(B). Subdivision and repeated addition give
homogeneity for all nonnegative rational multipliers.

For any rational symmetric X choose integer k large enough that X+kG>=0
and define L(X)=L(X+kG)-k. Independence of k follows by adding multiples of
G and using L(G)=1. This extends the same L to a positive Q-linear functional
on Sym_4(Q).

The ten rational coordinate matrices are a basis, so there is a unique real
symmetric S with L(X)=tr(SX) for every rational symmetric X. For every rational
column v, positivity gives v^T S v=L(vv^T)>=0. Rational columns are dense;
continuity of this finite quadratic polynomial then gives S>=0 over the reals.
This last step is continuity of a matrix polynomial already obtained from
linearity, not an extra continuity assumption about experimental frequencies.
Normalization is tr(SG)=1. Without the pure-certainty premise, every such S
defines an admitted law; the preparation has not yet been identified.

### 2.2 Certainty selects the source ray

The form M_z is rational and lies between 0 and G by the G-Cauchy-Schwarz
inequality. For this proof only, introduce real coordinates

```text
u=G^(1/2)z/sqrt(m),       u^T u=1,
C=G^(1/2) S G^(1/2),     C>=0, tr(C)=1.
```

These coordinates are not a physical field extension. Certainty gives
u^T C u=f_z(M_z)=1. Consequently the trace of C on u-perp is zero.
Positivity makes each of those diagonal entries zero and then kills their
cross entries: a positive matrix obeys |C_ij|^2<=C_ii C_jj. Hence C=uu^T.
Returning to the original coordinates yields S=zz^T/m, proving (1).

Equivalently, normalization and f_z(G-M_z)=0 give the same certainty premise.
Its physical content is darkness of the complement to the independently
prepared ray. The choice of that ray cannot be read back from the desired
Born probabilities.

### 2.3 QDD and the usual square formula

Let s=sum_i z_i and r=sum_i z_i^2. Apply (1) to
M_LOW=G P_LOW and M_HIGH=G P_HIGH. Their probabilities are forced to be

```text
p_LOW  = (s^2/20)/(r-s^2/5),
p_HIGH = (r-s^2/4)/(r-s^2/5) = 1-p_LOW.                 (2)
```

Thus the already registered algebraic weights become the unique possible
values of a law satisfying these new premises. For z=(1,0,0,0), m=4/5 and
p_LOW=1/16. At z=0 normalization is undefined; this note supplies no vacuum,
no-click or ZERO_SUPPORT occurrence convention.

The proved matrix S has a unique real-linear extension
bar_f_z(M)=tr(SM) on Sym_4(R); restricted to 0<=M<=G it is positive and
normalized and agrees with f_z on rational effects. This is a mathematical
extension, not a physical enlargement of the admitted measurements.
For a G-unit real vector a, the rank-one projector P_a=a a^T G has effect
M_a=G a a^T G, which need not be rational. In this extended domain,

```text
p_a = bar_f_z(M_a) = |a^T G z|^2/(z^T G z).
```

The familiar complex formula follows by the corresponding Hermitian-effect
argument only after a complex state/effect carrier and its conjugation have
been independently supplied. QDD's rational real theorem alone does not
derive that physical complex structure, general preparations or entanglement.

## 3. Exact controls: why the weaker routes fail

### 3.1 Two branch weights do not determine their occurrence

Put t=w_LOW/m and define, for this two-outcome context only,

```text
h(t)=t^2/(t^2+(1-t)^2),       candidate law=(h(t),1-h(t)).
```

It is nonnegative, normalized, rational on rational t, invariant under source
sign and nonzero scaling, symmetric under exchange of the two labels, and
has the same certain/zero endpoints as t. For z=(1,0,0,0), however, h(t)=1/226
instead of 1/16. For fixed source it is also an ordinary additive measure on
the two-label event set. Therefore none of those weaker properties proves
Born, and ordinary record-set additivity must not be substituted for premise 2.

An explicit refinement exposes the missing consistency. In a complete tuple
(M,G-M) with Born evaluation t, the normalized-square alternative above gives
h(t). Split M into M/2,M/2 without changing its declared coarse effect. Applying
the same normalized-square rule to the three fine labels gives coarse value

```text
2(t/2)^2/[2(t/2)^2+(1-t)^2]
    = t^2/[t^2+2(1-t)^2],
```

which at t=1/16 is 1/451, not 1/226. This family cannot define one
context-independent f_z on the declared full effect interval. Physical
admissibility and equivalence of that refinement remain premises, not findings
about a detector. A rational amplitude version is equally explicit: splitting
the first component of (1,1) into (3/5,4/5) preserves its quadratic coarse
weight 1/2, whereas fourth powers give 337/962.

### 3.2 Additivity alone does not select the prepared state

The law f_mix(M)=tr(G^(-1)M)/4 is normalized, positive and additive on the
entire interval. It has f_mix(M_z)=1/4, so it violates the pure-certainty
premise. This demonstrates why a state/effect identification independent of
the desired probabilities is indispensable.

Nor can the premises be imposed on deterministic individual yes/no responses
without qualification: additivity forces f_z(G/2)=1/2. The f_z in the theorem
is a proposed aggregate law, not a per-run value in {0,1}. A deterministic
microscopic apparatus may have contextual responses while its observed
aggregate is noncontextual. The proof neither constructs that apparatus nor
rules out all deterministic dynamics.

## 4. Quantitative conditional bound for imperfect preparation

Keep the effect-domain, positivity, normalization and additivity exact, but
weaken certainty to f_z(M_z)>=1-epsilon, where 0<=epsilon<=1. Then for every
M in E_G(Q),

```text
|f_z(M)-z^T M z/m| <= sqrt(epsilon).                    (3)
```

To see the constant, set B=G^(-1/2) M G^(-1/2), so 0<=B<=I, and use the
positive trace-one C from section 2. Write its spectral decomposition as
C=sum_i p_i v_i v_i^T with unit v_i. The difference
D_i=v_i v_i^T-uu^T has its possible nonzero eigenvalues
+sqrt(delta_i),-sqrt(delta_i), where delta_i=1-|u^T v_i|^2.
Thus |tr(BD_i)|<=sqrt(delta_i). Weighted triangle and Cauchy-Schwarz give

```text
|tr(B(C-uu^T))| <= sum_i p_i sqrt(delta_i)
                  <= sqrt(sum_i p_i delta_i)
                  = sqrt(1-u^T C u) <= sqrt(epsilon).
```

This is a bound on the scalar law. A limit-frequency interpretation still
requires existence and identification of that limit. It is not a finite-sample
confidence interval, a certificate of epsilon, or a robustness theorem for
approximately additive measurements. Those additional error and sampling
premises must be supplied separately. No numerical tolerance is selected here.

## 5. Deterministic current-to-count route: what it does prove

There is a separate route that needs no external initial measure. Suppose
k finite channels have nonnegative cumulative currents H_j(T), a common
fixed threshold q>0, and counters that preserve all remainders:

```text
N_j(T)=floor(H_j(T)/q),       S(T)=sum_j H_j(T).
```

Then 0<=H_j-qN_j<q and 0<=S-q sum_j N_j<kq. For zero initial remainders,
when S>kq an explicit bound is

```text
|N_j/sum_i N_i - H_j/S| < (k+1)q/(S-kq).              (4)
```

It follows by writing H_j=qN_j+r_j and S=qN+r with 0<=r_j<q,
0<=r<kq: the numerator |H_j r-S r_j| is less than (k+1)qS and
S-r>S-kq. Therefore if S(T) tends to infinity and H_j(T)/S(T) tends
to p_j, the count ratio tends to p_j. Bounded initial remainders change only
bounded errors. No stochastic seed, ensemble measure or ergodicity is used.
Different thresholds generally change the limiting weights in proportion
to their inverse thresholds; equality of q is a material apparatus premise.

For example, let independently specified linear branch maps B_j and positive
output metrics G_j satisfy sum_j B_j^T G_j B_j=G. If a declared repeated
preparation supplies deposits

```text
d_j(t)=a_t (B_j z)^T G_j(B_j z)/2,
a_t>=0,       sum_t a_t=infinity,
```

the common-threshold counts have limiting proportions

```text
p_j = z^T B_j^T G_j B_j z/(z^T G z).
```

Here linear branch response and the energy form produce the square;
thresholding transfers it into counts. Choosing B_j from desired probabilities
would defeat the derivation. The repeated source, energy supply, mode
orthogonality or interference law, channel calibration, equal thresholds
and persistence must be specified independently. This is not an amendment
of the adopted A/U5 count port or the TRC1 initial-ensemble route.

### 5.1 Why this does not close the present apparatus

The [cold reservoir proof](../probes/P-DECODER-RESERVOIR-COUPLING-1/PROOF.md)
has one finite-energy preparation and

```text
E(P_T)+sum_j H_j(T)=E(P_0),
sum_j N_j(T)<=floor(E(P_0)/q).
```

Its fresh zero incoming slots supply no new energy. Thus S(T) cannot diverge.
Repeated preparations require a new explicit source law; superposing a new
amplitude with a surviving wave generally creates interference terms.
Resetting detector remainders at every exposure changes counts to sums of
individual floors and can retain permanent bias.

The [quadratic partition](../probes/P-DECODER-RESERVOIR-QUADRATIC-PARTITION-1/PROOF.md)
also retains a residual form R_n. Renormalizing absorbed energy uses denominator
z^T(G-R_n)z, when positive, instead of z^T G z. At zero absorbed energy that
ratio is undefined. Finite threshold counts additionally retain their floor
errors; under the repeated-current premises their limits inherit the absorbed
energy proportions. An algebraic residual is not a measured output channel.
One must independently capture it or prove the required complete-absorption limit.
The same result's origin-port obstruction excludes recovery of both sharp QDD
weights by the stated uniform nonnegative complete processing. Vanishing
floor error cannot change those underlying forms or cancel the obstruction.

Finally, exact count proportions do not imply one event per preparation.
Two channels receiving q/2 per pulse, with zero initial remainders, have
N_1(T)=N_2(T)=floor(T/2). Odd pulses give no crossing and even pulses give two
simultaneous crossings. Their aggregate proportions are exactly 1/2,1/2
whenever nonempty, yet no pulse produces exactly one result. Serializing
these tokens changes timing and pointer semantics; it is not a detector proof.
The already registered carry sampler can generate exclusive words, but it
consumes a supplied p and has its own persistent-context requirements.

## 6. Exact remaining physical contract

The [measurement contract](NIST-MEASUREMENT-CONTRACT-1.md) and
[realization/occurrence contract](TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md)
now let the remaining premises be named without inserting them into Canon:

| Required premise | What the current project supplies | Still needed |
|---|---|---|
| Physical source and metric | Exact G and declared signed preparation maps | Independent source/metric identification, not fitted Born tomography |
| Effect family and equality | One explicit reservoir partition and restricted mathematical QDD instruments | An independently admitted full effect class, or a proved sufficient smaller class, with operational equality and refinements |
| A normalized law f_z | Archived record packets; TRC1's explicitly imported ensemble option | Actual outcome semantics and a justified probability or existing frequency law |
| Effect noncontextuality | No physical theorem from U | Same-effect equality of aggregate laws across equivalent apparatus contexts, including memory and preparation compatibility |
| Pure-preparation certainty | Algebraic M_z | Independent certainty/darkness principle or calibrated epsilon for (3) |
| Ordered instrument and repetition | Persistent mathematical records and proposed wrappers | Physical post-state, reset, admissible schedules and the joint/conditional event law |
| L5-to-L6 interpretation | Explicit STOP boundaries | A separately named and satisfied measure gate |

These requirements do not demand global uniqueness of every decoder. They
concern a declared measurement family with its actual context/equality. A
finite collection of successful measurements does not by itself establish
the all-effect premise. Likewise, one observed failure rejects only the
specific admitted contract and its scope, not every possible apparatus.

The effect-additivity proof makes no assertion that the equation layer of
J or U forces this contract. The conditional count proof makes no assertion
about independence of successive observations. Neither fixes Lueder
post-states, proves COMM-SAT or classifies the complete apparatus family.
Ordinary normalization, conservation, phase symmetry or unitary evolution
alone cannot fill those gaps, as the explicit controls show.

The useful next derivation is therefore precise: obtain operational effect
equality and refinement-invariant aggregate reading from an independently
specified physical apparatus and its occurrence mechanism, without putting
the target Born probabilities into either construction. At the theorem
boundary above, the Born formula would then be forced; that bridge has not
yet been derived here.

## 7. Disposition and preserved boundaries

This note delivers a complete conditional proof, its imperfect-certainty
bound, counterexamples to weaker premises, and an exact audit of the
deterministic threshold route. It is analytical exploration with no formal
probe result or newly earned public claim. A later formal probe must have a
new named reservation and immutable preregistration before any new gate run;
it must disclose the formulas and witnesses already exposed here.

The note neither repeats PR #812's raw-arrival incidence attack nor introduces
a probability or temporal ensemble into the frozen A/U5 port. Raw J and B
remain excluded there; residual tokens remain fresh per cut.
COINCIDENCE-RECORD-FREQUENCY stays candidate-H / UNTESTED / STOP outside the
registry. QDD-INSTRUMENT-APPARATUS, both O2 children, Bell causal accounting
and all photon obligations remain unchanged. The TRC1 ensemble option and
NIST conditional contract are not modified or relabeled as a Born derivation.
