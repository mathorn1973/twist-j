# Independent written proof review

**PUBLIC; candidate-T, L1, NON-CANONICAL.** Review for
P-QDD-AFFINE-ENERGY-CONTROL-1, public lock
[#1089](https://github.com/mathorn1973/twist-j/issues/1089).

The reviewer read PREREG.md, NETLIST.md, CONTROL-MODEL.md and ENERGY.md,
and compared the imported target with the accepted preceding
NATIVE-ROUTING.md. This review was completed without reading verify.py
and without executing any scientific gate or numerical calculation. It is
an independent attack on the written arguments, not an independent
experiment or architecture reproduction. Public execution and acceptance
belong to the separate run records.

No mathematical gap remains in the conclusions at their stated scope.
The qualifications below are necessary parts of that assessment.

## 1. Affine words and the coherent lift

The potentially troublesome feature of the nineteen-instruction word is
its reuse of changed values, not just its coefficients. I tracked the
current registers symbolically. Before either exchange, they are exactly

```text
(B_c, B_a, B_b, B_d, B_q, B_r).
```

In particular, B15 uses the already changed `r`, while B16 uses the
already changed `c`. The resulting first component before the exchanges
is `19a0+15c0+17r0+8`, which reduces to `4a0+2r0+3` in F5.
The two exchanges give the required order. The direct inverse agrees
with this argument. The five-instruction word for A follows immediately
because its four source registers are unchanged.

There are twelve fixed-gain additions, two nonzero scalings, three
shifts and two exchanges in B. Expanding those twelve additions into
positive unit-gain repetitions gives twenty-six additions. These are
counts in the declared operation family, not optimality or duration
claims. The determinant is `3*4*(-1)^2=2` in F5. The comparison with
determinant-one fixed native generator words is valid and does not
classify circuits containing the native selector or auxiliary systems.

The declared elementary lifts have coefficient +1 on every basis
transition. Thus equality of the complete point permutations proves
equality on arbitrary amplitudes and matrix units, including an untouched
reference. This argument would not justify ignoring relative phases in
a different physical implementation. CONTROL-MODEL.md supplies the
required phase account for its conditional implementation.

## 2. Hamiltonian signs, finite pulses and exchanges

With the stated positive-sign Fourier transform and
`H_ij=-hbar g N_i N_j`, the Schrödinger propagator has phase
`omega^(kxy)`, not its conjugate. Fourier transformation of the target,
the diagonal pulse, and inverse Fourier transformation therefore give

```math
\frac15\sum_{m=0}^4\omega^{m(y+kx-z)}
   =\delta_{z,y+kx}.
```

This checks both the direction of addition and the absence of a
label-dependent residual phase. The positive duration is
`2 pi k/(5g)` for nonzero `k`. The zero coefficient requires no pair
pulse. An actual inverse Fourier unitary cancels its own global phase;
otherwise a known schedule-wide phase remains. Such a common phase
does not become a relative phase between the four code inputs.

The exchange is not silently supplied as a one-register control. The
four stated operations take `(x,y)` through

```text
(x,x+y), (-y,x+y), (-y,x), (y,x).
```

They use only the admitted additions and local negation. The direct
formula for A is also consistent: the constant two contributes the
diagonal factor for a shift by two. Its optional simultaneous pulse
explicitly requires the twice-strength local term. Sequential access
does not require that additional simultaneous-control assumption.

Connected local x and y rotations provide the local special unitary
operations, with their remaining determinant phase accounted for as a
common phase. The sign convention and the requirement `Omega>0` make
the selective-projector pulse durations positive. For nonzero `k,a,b`
the residue `[kab]_5` is nonzero; the sixteen projectors are orthogonal
and their phase product is exactly the number-product phase. Local
conjugations and their durations remain part of this construction.

The cited primary-source abstract supports the connected-transition
and selective-interaction precedent and identifies its rubidium example
as eight-level:
[Brennen, O'Leary and Bullock, Criteria for Exact Qudit Universality](https://arxiv.org/abs/quant-ph/0407223).
That precedent does not identify the present native coordinates with
physical five-level systems. The note correctly treats the carrier,
calibrated coupling, drift treatment and pulse controls as added premises.

## 3. Arbitrary environments do not defeat the energy lemma

I specifically checked the use of unbounded environment energy. The
proof does not differentiate an energy characteristic function or use
an expectation value. Strong conservation of the bounded exponentials
and a product input and output give

```math
e^{itE_i}\chi_{\rm in}(t)
  =e^{itE'_i}\chi_{\rm out}(t).
```

Normalization and strong continuity make the characteristic functions
nonzero on some interval about zero. Comparing two labels on that
interval forces their real energy changes to be identical. Neither
infinite dimension nor a divergent mean energy invalidates this step
for a normal state. An improper shift-invariant resource is outside
the stated preparation class.

The mixed-state extension is also valid. A purification with an
untouched zero-energy reference preserves the conservation hypothesis.
An exact pure system output for each basis input factors its purified
joint output. Preservation of every off-diagonal code matrix unit then
forces every pair of environment vectors to have inner product one,
and hence to coincide. This establishes the required common environment
without assuming that the consumed resource returns to its input state.

These hypotheses cannot be replaced by correct basis populations alone.
In particular, preserving coherence only inside HIGH would not suffice
for the equal-gap contradiction: all three HIGH labels already have
the same energy change. The theorem uses the stated exact coherent
target on the full four-dimensional code, including LOW--HIGH matrix
units. Allowing the environment to distinguish LOW from HIGH changes
that target and the tested class.

## 4. Code obstruction and its energy-encoding boundary

Ordinary representative arithmetic gives port energy coefficient
changes `(4,1)` on LOW and `(-2,2)` on every HIGH input. For equal
positive gaps these are respectively `5 Delta` and zero. The lemma
therefore excludes every implementation in the declared conserved-energy
class, regardless of the chosen decomposition or intermediate work
stores. This is a code-level conclusion and does not require global B.

Conversely, equality of the four changes for independent port gaps
requires exactly `Delta_r=6 Delta_q`, with common transfer
`10 Delta_q`. This removes this particular necessary-condition
contradiction; it proves neither a realization nor physical selection
of that ratio. The explicit escape is essential: preservation of a
field sum is not preservation of an ordinary real energy, and the
equal-gap encoding is a comparison premise rather than a native law.

## 5. The global-B Fourier argument has a different domain

For a clean implementation of B on every checkpoint basis vector, the
lemma first makes `E(Bx)-E(x)` constant. Summing over the finite
permutation forces that constant to vanish. No infinite iteration or
energy boundedness assumption is used here.

For additive diagonal local energies, the nonconstant Fourier support
of `E` lies on the six coordinate axes. Every row of B's invertible
linear matrix has at least two nonzero entries. Its six row lines are
distinct and avoid all coordinate axes. Thus the twenty-four
nonconstant frequencies in `E composed with B` cannot match any of
those in `E`, and cannot cancel one another. Each nonconstant local
Fourier coefficient must vanish. This proves flatness of all six local
spectra, for arbitrary real level values.

The proof allows more general spectra than the equal-gap theorem but
demands a larger target domain. It does not exclude a different global
operation agreeing only with the four-point entrance, nor a
nonadditive checkpoint Hamiltonian. These limitations are explicitly
retained in ENERGY.md.

The proposed modular-rank audit is logically sound independently of
the Fourier proof. The thirty-column equation matrix has integer
entries and six independent constant-local-energy kernel vectors.
If its rank modulo 101 is 24, a nonzero modular minor supplies rational
rank at least 24, while those exact kernel vectors supply rank at most
24. The same integer matrix then has real rank 24. This review does
not claim that the proposed enumeration or rank computation has run.

## 6. Physical disposition

The positive control construction and the conserved-energy exclusions
are compatible. Prescribed external pulses omit the controller's full
state from the system-only description; they do not establish the
closed conservation and clean-output hypotheses. Conversely, the
energy theorem does not exclude every physical encoding or apparatus.
A constant microscopic Hamiltonian alone is not the specified
additive cut-energy conservation law when interaction energy changes.

Finite pulse duration does not establish synchronization with native
ticks or a complete physical implementation of the selected native
map. The Bell-pair calibration consequence is a mathematical prediction
of the admitted model, not an executed experiment. None of these
results supplies physical archive persistence, an occurrence law or
reset. No L1-to-L5 gate or closure of QDD-INSTRUMENT-APPARATUS follows.

Within those boundaries the written arguments support the stated
conditional mathematical results. The finite verifier audits their
concrete premises and constructions; it cannot replace the universal
energy proof or establish the missing physical assignment.
