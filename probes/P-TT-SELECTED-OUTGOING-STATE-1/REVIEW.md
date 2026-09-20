# Independent mathematical and scope review

**PUBLIC; candidate-T assessment; L1; NON-CANONICAL.** This review concerns
the selected outgoing-state construction, not physical confirmation or a
change to the registered normalization owner. The reviewer read MODEL.md
and PROOF.md and independently read the public owner, Canon section 14,
the closure-input and K1 notes,
the selected-theory program and the competing incubation branches. The
reviewer did not read or execute this probe's `verify.py`, run a formal
scientific gate, or use numerical output to derive the results below.

## 1. What has actually been completed

The input is the unchanged ten-word K1 law and the already selected
isolated tensor history

```text
h_0=h_1=0,
h_(m+1)=(2I-L)h_m-h_(m-1)+1_(m=1) Phi(w),
Phi=H_1-H_0.
```

For each packet choose two independent fair signs once, independently of
the word. At every site and counter use

```text
a=sqrt(max(h,0)),     b=sqrt(max(-h,0)),
v=epsilon_+ a+i epsilon_- b,     I=|v|^2=|h|.
```

The square roots are the nonnegative real roots. They exist at every
finite counter, including zeros, and no division by the field occurs.
The finite source space has 40 labelled atoms. One draw specifies every
future slice and every joint moment; signs are not drawn afresh at later
times or independently at different sites. This is a complete selected
mathematical state law, rather than a covariance prescription with a
missing higher-moment closure.

The construction keeps the primary tensor equation. It does not assert
that the vector itself obeys the linear tensor recurrence, that the roots
remain in the native cyclotomic coefficient field, or that they define a
differentiable continuum field through zeros. All three would be extra
claims requiring their own proof.

## 2. Sign selection, symmetry and complete moments

Every nonzero, mean-zero tensor slice contains both positive and negative
entries. In the declared class of sign-coherent lifts, reflection flips
`epsilon_-` and the spin-one half-turn flips both signs. These operations
generate the four-element sign group and act transitively on the four
lifts of each active history. A probability law invariant under this
action is therefore uniform on those four lifts. This proves the claimed
conditional uniqueness only after the sign-coherent class and symmetry
requirement have been selected.

This is not a classification of all possible lifts: independently varying
signs across sites or counters are excluded by the chosen class, not by
the tensor observations. Nor is it spatial or rotational isotropy. The
selected tensor frame has a real plus component and zero cross component.
Transporting the frame transports the state and the square map; it does
not establish invariance of the fixed marked preparation under every
rotation. In particular, a globally single-valued spin-one-equivariant
square-root section cannot exist: rotation by pi fixes the square but
reverses every nonzero root. The probability construction does not rely
on such a section.

There is an additional exact symmetry of the word law. The involution

```text
w -> (1-w_3,1-w_2,1-w_1,1-w_0)
```

exchanges `u_0,u_1`, preserves the weights and sends the whole tensor
history to its negative. For arbitrary points `x=(r,m)`, `y=(s,n)`, sign
averaging consequently gives

```text
E[v_x]=0,
C_v(x,y)=E[a_x a_y+b_x b_y],
P_v(x,y)=E[a_x a_y-b_x b_y]=0.
```

The last equality holds for all point pairs, including unequal times,
because the word involution exchanges a and b simultaneously throughout
the history. Zero pseudo-covariance is not a Gaussian hypothesis. For
example, at the first emitted slice and site zero,
`E[v^4]=E[h^2]=1/8`, whereas a zero-mean Gaussian with `P_v=0` would have
`E[v^4]=0`. Thus an explicit fourth-order distinction survives even where
some other fourth-order contractions happen to match a Gaussian formula.

All moments follow from the same finite sum over the 40 labelled atoms.
For the quadratic readout the root signs cancel exactly; its connected
covariance is `E[h_x h_y]`, because `E[h_x]=0` at all counters. The
intensity covariance must instead subtract its generally nonzero mean.
Neither stationarity in the marked sites nor independent temporal
sampling is implied. Full Fourier covariance and pseudo-covariance
matrices, including off-diagonal entries when present, are the relevant
complete spectral data; diagonal mode powers alone are not the full law.

## 3. All-counter claims have analytic support

The two nonzero eigenvalues of the rational planar L are
`lambda_+=(235+18 sqrt(5))/324` and
`lambda_-=(235-18 sqrt(5))/324`, each with multiplicity two. They lie
strictly between zero and four. Write

```text
2 cos(omega_+/-)=2-lambda_+/-=(413-/+18 sqrt(5))/324.
```

The field trace of either displayed value is `413/162`, not an integer.
Neither value is therefore an algebraic integer. A root of unity and
its inverse are algebraic integers, so `exp(i omega_+/-)` cannot be a
root of unity. Starting with the prescribed zero pair and impulse, the
transfer from Phi to slice m has eigenvalue

```text
sin((m-1) omega_+/-)/sin(omega_+/-),     m>=2.
```

Its numerator cannot vanish for an integer m>=2, since that would make
the exponential a root of unity. Thus the transfer is invertible on the
four-dimensional mean-zero spatial subspace at every such counter.
This proves that the six active tensor slices remain nonzero and
distinct. Together with the static slice there are exactly seven tensor
states, and exactly 25 distinct vector states, at every m>=2. The four
static words collapse to the same zero history. The 40 labelled atoms
must not be confused with 40 distinct physical or mathematical outputs.

The initial tensor covariance has rank two, and invertible deterministic
transfer preserves that rank at each m>=2. The entire tensor history is
linear in that same two-dimensional source support; every finite tensor
prefix containing m=2 therefore also has covariance rank two. These are
statements about the tensor covariance, not a transfer of the same rank
to the nonlinear root-vector covariance or to other enlarged states.
Any additional onset-only rank or norm certificate must retain its
specified counter and operator domain.

There is also a useful exact positivity argument. For a rational
five-vector, vanishing of one nontrivial Fourier coefficient forces all
five entries to be equal: its degree-at-most-four polynomial must be a
multiple of the fifth cyclotomic polynomial. A nonzero mean-zero tensor
slice therefore has no vanishing nontrivial Fourier coefficient. Its
absolute-value vector cannot be constant either, because a positive
constant modulus together with zero mean would require equal counts of
positive and negative entries on an odd number of sites. Consequently
every nontrivial intensity Fourier coefficient is nonzero, and its zero
mode is positive.

The static atom has total weight 1/3 and every active atom has positive
weight. At every m>=2 and every mode, the intensity Fourier variable thus
takes both zero and a nonzero value. Its connected variance is strictly
positive. Tensor power is strictly positive at the four nonzero modes
and zero at the constant mode. These are pointwise all-counter results;
no uniform positive lower bound over all counters is asserted.

Recurrence induction, this algebraic-integer argument and the finite-law
formulas establish the universal time quantifiers. A finite verifier
prefix only audits their ingredients. It cannot replace these arguments
by extrapolation from an arbitrarily long run.

## 4. Independent first-emission calculation

This calculation uses the unitary five-point Fourier transform. Define
`P_T(k)=E[|Fh(k)|^2]` and
`P_I(k)=E[|FI(k)-E[FI(k)]|^2]` at m=2, with
`R_TI=P_T/P_I`. Here P_I denotes the chosen finite intensity comparison,
not a cosmological scalar power spectrum.

The intensity law is particularly simple:

| Intensity five-vector | Probability |
|---|---:|
| 0 | 1/3 |
| `(delta_4+delta_1)/2` | 1/6 |
| `(delta_0+delta_2)/2` | 1/6 |
| `(delta_4+delta_0+delta_1+delta_2)/2` | 1/3 |

Each nonzero tensor profile has its opposite with equal weight. For a
nonzero mode put `q=zeta_5^k`, `t=q+q^-1`; then `t^2+t=1`. Direct Fourier
expansion of those profiles gives

```text
P_T=(3+t)^2/60,
E[|FI|^2]=(t^2+1)/60,
|E[FI]|^2=1/80,
P_I=(5-4t)/240.
```

The resulting complete table is

| Mode | P_T | P_I | R_TI |
|---|---|---|---|
| 0 | 0 | 2/15 | 0 |
| 1,4 | `(3+sqrt(5))/24` | `(7-2sqrt(5))/240` | `10(31+13sqrt(5))/29` |
| 2,3 | `(3-sqrt(5))/24` | `(7+2sqrt(5))/240` | `10(31-13sqrt(5))/29` |

Parseval independently gives `sum_k P_T=1/2` and `sum_k P_I=1/4`.
The ratio of those sums is two; it is not an average of the individual
mode ratios. Subtracting the intensity mean matters: retaining its raw
power would give another comparison. Discarding the zero mode also
changes the integrated comparison and must not be done silently.

All entries were derived from the source law, not fitted to a desired
tensor ratio. Some are large. Their size is not a reason to insert an
unregistered suppression factor or reinterpret the finite mode labels as
a chosen observational scale.

## 5. Action, scalar comparison and owner boundary

The primary h action and source normalization remain those of the adopted
isolated TT construction. Choosing roots of its solution is a state
reading. It is not a proof that varying the pulled-back action `S[v^2]`
selects that solution. Its chain-rule covector vanishes at v=0 even when
the original tensor covector does not. The conservative-exchange
incubation in #929/#930 exhibits the resulting silent/emitting ambiguity
for its own two-field action. That scoped obstruction is respected here
by retaining the h equation as a primary law, not evaded by renaming a
root an independently derived vector dynamics.

The comparison `I=|v|^2` is the natural local O(2)-invariant quadratic
readout, unique only up to a coefficient in the stated real quadratic
class. Choosing coefficient one is an additional convention. It makes
the comparison completely calculable and avoids a new fitted number;
it does not derive its physical identification. A common rescaling of
v rescales both readouts quadratically and both powers quartically, so
it cancels in R_TI. An independent relative rescaling of the intensity
readout would not cancel and must not be hidden as a unit conversion.

No scalar action, cosmological curvature perturbation, physical wavelength
map, observational epoch or pivot follows from this local invariant.
Nor must I be assumed to solve an independently propagating spin-zero
equation. The marked site and integer counter inputs completely specify
this finite model; they are not already spatial distances and times in a
cosmological perturbation calculation.

Accordingly the suitable future disposition is two conditional L1
theorems, for the complete selected state/moments and the exact composite
comparison, plus at most a D adoption of this explicitly chosen profile.
`TT-VECTOR-STATE-NORMALIZATION [O]` retains its full positive and negative
decision clauses. Its remaining physical comparison and cross-layer
requirements are not replaced by the finite ratio R_TI. Equally, the
genuine completion of the mathematical outgoing state and its moments
should be recorded rather than continuing to describe those slots as
unspecified within this selected profile.

## 6. Collision and provenance audit

- Public Canon v90 already adopts the isolated emission dictionary as
  `TT-SOURCE [D]`; that source and recurrence remain unchanged here.
- Open #929/#930, branch `notes/c-tt-source-conservative-exchange-n`,
  describes another source/trial-field pair with chosen exchange 1/5.
  This probe neither takes over that lane nor imports its coefficient,
  physical claims or unpublished evidence grade.
- Open #910, branch `notes/C-TT-SHIFT-CONSTRAINT-N`, concerns a separate
  linear lapse/shift constrained action. It provides no complete outgoing
  vector state or scalar normalization. Its relevant authoritative
  successors are already in Canon section 14.
- The branch `notes/c-tt-vector-moment-underdetermination-1` contains the
  previously promoted six-law and fixed-modulus theorem. It is a boundary
  to preserve, not a new calculation or new closure to claim here.
- The working-map branch last merged main on 2026-09-20, but the map text
  remains its dated v81 assessment. The later owner-authorized selected
  theory program permits explicit choices; it does not turn those choices
  into necessary consequences of J or weaken the existing owner's scope.

This review finds no mathematical obstruction in the stated selected
construction. The reviewed MODEL.md and PROOF.md retain these choices
and limits; their all-counter arguments and onset formulas agree with
the independent derivations above. Acceptance remains conditional on the independent formal
audit passing its frozen contract. Neither a proof review nor the
eventual architecture checks establish physical adequacy.
