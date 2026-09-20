# Result: complete selected outgoing TT state

**PUBLIC; candidate-T, L1, NON-CANONICAL.** The first formal run completed
all ten frozen gates with PASS. No scientific falsifier fired. The result is
the conditional effective profile **ETH-TT-1** defined in MODEL.md, supported
by the all-counter proof in PROOF.md and the independent mathematical review
in REVIEW.md. Public Canon remains v90; no Canon or registry file is changed.

**Public acceptance is pending at this record stage.** This record establishes
one completed x86_64 local run, not completed public architecture acceptance.
Any later ACCEPTANCE.md must bind the actual immutable public run and check
records. Final-head and merged-main checks belong to the public pull request;
they are not anticipated here.

The first public CI attempt, run 35535183741 on result head
`9a818bca959f7330c70c78249edcbfb98b576c05`, stopped before scientific
execution on the required literal command field (`python3` versus the
recorded `python`). RUN.md records the neutral correction and interpreter
identity check. This was a record-format failure, not a scientific
counterexample or an abandoned pin. All six frozen files and EXPECTED.txt
remain unchanged; subsequent acceptance requires fresh public checks.

## 1. Frozen execution and evidence

| Item | Recorded value |
|---|---|
| Public lock | #1097 |
| Immutable preregistration pin | `6257dfaae9132ef2a2a49ec06300775287d595db` |
| Verifier SHA-256 | `8cc1b45f70c71037cdade0046e4ae3d485cd5053293cf907ef14a66d66ff2002` |
| Exact stdout SHA-256 | `dc1e909f2934f7fe3095875d21b374fa79afde6aa6c104d263aa86b6e43c0fc4` |
| Stdout | 1125 bytes, 11 lines |
| Exit / stderr | 0 / 0 bytes |
| Local platform | Ubuntu 24.04.3 LTS, x86_64, Python 3.12.14 |
| Frozen gate result | G1-G10 PASS |

RUN.md records the neutral execution details and EXPECTED.txt contains the
exact completed transcript. The scientific verdict is

```text
SELECTED-OUTGOING-STATE;
conditional L1 law, persistent sign lift and intensity comparison adopted
```

The finite audit covers counters `m=0,...,10`, all ten source words, the four
persistent sign pairs, five labelled sites and five Fourier slots. Its
space-time domain has 55 points, and the second-moment and TT fourth-order
contraction checks cover all `55 x 55 = 3025` point pairs. The exact sign
algebra includes all 256 four-factor component/conjugation patterns. These
are the actual finite domains, not a surrogate for all counters or arbitrary
independent four-point locations.

The universal claims rest on the written recurrence, symmetry, finite-law,
algebraic-integer and cyclotomic arguments. The verifier audits their exact
ingredients and finite consequences. The independent review did not read
the new verifier or derive its conclusions from its execution.

## 2. The full selected state is specified

Retain the established K1 ten-word masses, unit source, plus frame, isolated
onset, complete radiative-channel transfer and planar propagator. Their
primary outgoing tensor equation is unchanged:

```text
Phi=H1-H0,
h0=h1=0,
h_(m+1)=(2I-L)h_m-h_(m-1)+delta_(m,1)Phi.
```

Choose two independent fair signs once per packet, independently of the word,
and retain them at every site and counter:

```text
v_m(r)=epsilon_+ sqrt(max(h_m(r),0))
       +i epsilon_- sqrt(max(-h_m(r),0)).
```

The nonnegative roots and the zero convention give exactly `v^2=h` and
`|v|^2=|h|` everywhere. The source word and two signs determine the entire
history, every finite prefix and every joint moment. No later branch decision
or fresh sign is omitted from the definition.

There are 40 labelled preparation atoms and exactly 25 distinct vector
histories: one zero history of mass `1/3`, sixteen histories of mass `1/48`
and eight histories of mass `1/24`. Squaring gives seven tensor histories.
The same 25-vector and seven-tensor support counts hold at every slice
`m>=2`. The zero preparation remains in the law; emission is not selected
by conditioning away its mass.

The sign-coherent class requires one common sign on all positive tensor
entries and one common sign on all negative entries throughout the packet.
Within that declared class, reflection and the vector half-turn act freely
and transitively on the four lifts of each active packet. Invariance fixes
the conditional law uniquely to four equal masses. Four is also the minimum
nonempty finite support under these two symmetries when both real and
imaginary root entries are present. Sign coherence itself remains a chosen
restriction, not a consequence of the tensor observations.

The common-polarization-line family is O(2)-covariant under explicit frame
transport. This is not isotropy of the fixed plus-frame ensemble, spatial
translation invariance, or a globally single-valued equivariant root section.

## 3. Temporal moments and the fourth-order closure are complete

For `p=(r,m)`, write `a_p=sqrt(h_p^+)`, `b_p=sqrt(h_p^-)`. The same word and
signs are used in every factor. The complete moment rule retains precisely
the monomials with an even total number of each sign and averages their root
coefficients over the unchanged word law. Consequently

```text
E[v_p]=0,
C_v(p,q)=sum_w nu(w)[a_p a_q+b_p b_q],
P_v(p,q)=0
```

for all equal-time and unequal-time point pairs. The zero pseudo-covariance
uses the equal-mass source pairing `h -> -h`; it does not invoke independence
of the two points. Full Fourier covariance matrices retain their off-diagonal
entries. A diagonal spectrum alone would not describe this state.

With `d1=(e0-e2)/2`, `d2=(e4-e1)/2` and `h_m=A_m Phi`,

```text
C_Phi=(d1 d1^T+d2 d2^T)/6+(d1+d2)(d1+d2)^T/3,
C_h(m,n)=A_m C_Phi A_n^T,
E[v_p^2 conjugate(v_q^2)]=E[v_p^2 v_q^2]=C_h(p,q).
```

The nonzero source covariance eigenvalues are exactly `5/12` and `1/12`.
Every tensor prefix containing onset and every tensor slice `m>=2` has
covariance rank two. This rank statement is about the tensor field, not
the nonlinear vector or intensity covariance.

Gaussian closure is explicitly false at a point with nonzero variance:
`V1_p V2_p=0` identically while each real component has variance
`E|h_p|/2>0`. The corresponding Gaussian fourth cross moment would be
`(E|h_p|)^2/4`, whereas the selected law gives zero. The finite source law
therefore supplies fourth moments directly, rather than guessing them from
the two-point data. The older fixed-modulus obstruction retains its separate
hypotheses and is not overextended to this source-dependent modulus.

## 4. All-counter persistence is proved, not extrapolated

For every nonzero Fourier slot, the transfer from impulse to slice `m` is

```text
t_m(k)=sin((m-1)omega_k)/sin(omega_k),
2 cos(omega_k)=(413-/+18sqrt(5))/324.
```

The displayed conjugate numbers have field trace `413/162`, not an integer.
They cannot be algebraic integers, whereas a root of unity plus its inverse
is integral. Therefore the transfer numerator cannot vanish for an integer
`m>=2`. The transfer is invertible on the mean-zero spatial subspace at every
such counter.

It follows that each active packet has a nonzero tensor slice at every
`m>=2`, with both positive and negative entries. This is nonreturn to the
zero slice, not a theorem about irreversible radiation, monotonic amplitude,
physical propagation distance or a uniform positive amplitude bound.

## 5. Action normalization and the exact finite comparison

The inherited tensor action coefficient remains `lambda=216*pi`. Its free
TT action is `1/(4 lambda)` times the displayed quadratic kinetic-minus-
spatial expression. The canonical readings are

```text
q_T=h/sqrt(2 lambda),
v_can=v/(2 lambda)^(1/4),
q_I=|v_can|^2=|h|/sqrt(2 lambda).
```

The scalar intensity is the explicitly chosen norm-square observable
`s=|v|^2`, with coefficient one. Its common scale then follows from the same
vector rescaling; no relative coefficient is fitted. This does not give an
independent scalar action or identify the intensity with a cosmological
scalar perturbation.

Retaining the primary tensor equation is essential. The derivative of the
square map vanishes at `v=0`, so the Euler equation obtained only from
`S_T[v^2]` loses the forced tensor equation there and admits a silent branch.
The selected roots are readings of the independently evolved tensor field,
not a claimed regular autonomous vector-only action.

For the unitary marked transform `F_kr=zeta_5^(kr)/sqrt(5)`, define unscaled
ensemble-connected powers `T_k=E|Fh_k|^2` and
`I_k=E|F(s-E s)_k|^2`. The selected finite ratio is `R_TI=T_k/I_k`, with
both normalized powers divided by `2 lambda`. At first emission:

| Slots | `T_k(2)` | `I_k(2)` | `R_TI(k,2)` |
|---|---|---|---|
| 0 | 0 | 2/15 | 0 |
| 1,4 | `(3+sqrt(5))/24` | `(7-2sqrt(5))/240` | `10(31+13sqrt(5))/29` |
| 2,3 | `(3-sqrt(5))/24` | `(7+2sqrt(5))/240` | `10(31-13sqrt(5))/29` |

The total unscaled connected powers are `sum_k T_k=1/2` and
`sum_k I_k=1/4`. The intensity mean is nonzero, so replacing its connected
power by its raw second moment would change the result. The large derived
mode ratios remain exactly as obtained; they are not tuned to observations.

Every intensity denominator is strictly positive in every slot at every
`m>=2`. The proof uses rationality of `h`, the fifth cyclotomic minimal
polynomial and the impossibility of a nonzero constant-modulus zero-sum real
vector on five sites. Together with the retained zero atom this forces
positive connected intensity variance. Tensor power is zero at slot zero
and strictly positive in each other slot. Thus all these finite ratios are
defined for every emitted counter. At `m=0,1` both powers vanish and the
ratio is undefined, not zero.

The position covariance kernels of h and s are rational. Diagonal Fourier powers and the
ratios belong to `Q(sqrt(5))` at each finite counter; full off-diagonal
Fourier kernels need not lie in that real subfield. Normalized powers also
include the explicitly inherited action factor. No claim that all vector
roots or moments belong to the original cyclotomic field is made.

## 6. Boundary controls and chosen inputs

The frozen audit distinguishes the selected state from renewed signs,
biased signs, a silent singular-pullback branch, Fourier transformation
before pointwise squaring, and uncentered intensity power. These controls
passed; none is substituted for the selected model or hidden as a harmless
normalization change.

The following choices remain mandatory parts of every statement of the
result:

- the inherited K1 source amplitude, ten-word law, marked frame, isolated
  impulse, onset, full transfer and planar propagator;
- CH-TT-ROOT-COHERENCE: signs persist on their two sign sectors over the
  entire packet;
- CH-TT-DECK-LAW: conditional reflection/half-turn symmetry and independence
  from the source word;
- CH-TT-INTENSITY-COMPARISON: the unit norm-square observable, connected
  ensemble reading and the declared Fourier and canonical conventions.

The theorem does not derive these choices from J or native U. It specifies
their exact consequences without a fitted continuous parameter. No physical
sign generator or repeated-source preparation law is supplied.

## 7. Disposition and remaining physical task

The selected outgoing vector state and all its temporal moment data are
mathematically complete at the frozen L1 scope. The prospective disposition
is the two conditional theorems and explicit selected dictionary described
in `notes/canon/SELECTED-TT-STATE-FOLD-PROPOSAL.md`, after public acceptance
and a separate reviewed fold. This result record does not perform that fold.

`TT-VECTOR-STATE-NORMALIZATION [O]` keeps its identifier and full decision
condition. `R_TI` is a finite tensor/intensity comparison, not physical
`r_T(k)`. A cosmological comparison still needs its declared physical scalar
carrier, dynamics and state, relative units, coordinate/epoch/mode mapping
and typed physical reading gates. None is supplied by renaming the intensity.
The proposed L1-L4, L4-L5 and L5-L6 gates remain UNPASSED.

No physical apparatus, detector, SI scale, nonlinear geometry, experimental
confirmation or classification of every admissible vector normalization is
claimed. These remaining tasks do not reopen the outgoing state or fourth
moments already specified within ETH-TT-1.
