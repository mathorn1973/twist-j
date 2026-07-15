# Entropy selection recon

Status: **NON-CANONICAL LOCAL ANALYSIS**

This note starts the successor analysis to the finite entropy bridge and
mirror work. It is not a preregistration, verifier record, or evidence bundle.
No target below is frozen and no claim status is earned.

## Public inputs

The analysis uses only already public finite facts, plus the still-unmerged
mirror result as a clearly separated working input:

- the recurrent core has 6250 states and two living halves of 3125 states;
- each branch restricts bijectively between living halves;
- living trajectories over a fixed driver word number 3125;
- `|O/lambda^5| = 3125` and multiplication by `J` has orbit spectrum
  `{1: 1, 4: 1, 20: 156}`;
- every living half has 625 canonical pentagons of five states;
- the finite-cylinder selector route is already falsified;
- the coherent-gauge block cocycle is affine and periodic on the tested
  dyadic levels;
- working mirror input: one-tick cell maps are reflections and the two own-half
  maps have a unique singlet fixed state.

The sought equation is

```text
Psi_(S kappa)(J y) = F_(theta(kappa))(Psi_kappa(y)),
```

with `Psi_kappa` a bijection from `O/lambda^5` to the living fiber appropriate
to `kappa`. A fiberwise bijection turns the question into conjugacy of two
finite permutation cocycles over the Thue--Morse base.

## First diagnostic: repeated dyadic supertiles

`notes/ENTROPY-SELECTION-RECON.py` compares, for `L = 2^n`, the monodromy
cycle type of `J^L` on `O/lambda^5` with the living-kernel monodromy obtained
by repeating the length-`L` Thue--Morse prefix.

For every tested `n = 2..10`, the source type is

```text
{1: 5, 5: 624}.
```

The target types are

```text
n = 2,3,4,6,7,8,10:  {5: 625}
n = 5,9:              {1: 3125}
```

Therefore no tested repeated-supertile model admits a fiber conjugacy to
`J^L`. This is not a no-go for the desired measurable family: the Thue--Morse
subshift is aperiodic, so these periodic repetitions are diagnostics rather
than points of the actual base system.

Two features are nevertheless informative:

1. On the non-identity levels, all 312 size-20 component-halves split into two
   five-cycles. This exactly accounts for the source's 624 nontrivial
   five-cycles. The residual mismatch is concentrated in the five-state
   singlet sector: five source fixed points versus one target five-cycle.
2. At levels `n = 1 mod 4` in the tested range, the target block map is the
   identity on the whole living fiber while `J^(2^n)` is not. A stationary
   block dictionary cannot absorb this. Any viable transfer must depend on
   the unbounded 2-adic phase/carry of `kappa`.

This agrees with the earlier finite-cylinder no-go but is a different
observation: it identifies where a naive lambda-digit/living-state dictionary
breaks at dyadic renormalization scales.

## Structural reduction to attempt

Use the canonical decomposition

```text
living state = (recurrent component, pentagon cell, q in F_5).
```

On the target, one tick acts by a component-preserving cell permutation and
an affine reflection `q -> -q + b`. Longer dyadic blocks act by translations
in the tested coherent gauge. On the source, represent `O/lambda^5`
explicitly by five lambda digits and separate the carry induced by `J`.

The transfer family should then be solved in layers:

1. component label;
2. pentagon-cell label;
3. within-cell `F_5` coordinate;
4. singlet correction;
5. compatibility under refinement of the 2-adic phase.

The objective is a cohomological transfer equation over the 2-adic factor,
not a lookup table on a bounded Thue--Morse window.

## Next exact local tests

1. Construct a canonical quotient model of `O/lambda^5` and print the full
   `J` permutation, valuations, digit carries, and centralizer orbits.
2. Extract the full target permutation cocycle on components, cells, and
   `F_5` coordinates without choosing new cellwise gauges.
3. For truncated 2-adic phases of depth `r`, solve the transfer equations and
   count solutions modulo the source and target centralizers.
4. Require compatibility from depth `r` to `r+1`; record the first empty
   level or the surviving inverse system.
5. If solutions survive, test whether at least two inequivalent families do.
   Existence alone does not establish canonicity.
6. Only after existence and canonicity, prove the regularity class and derive
   the pushforward of Haar measure. Do not infer the measure clause from the
   cardinality match alone.

## Stop conditions for the recon

- A failed truncated compatibility equation closes only the named transfer
  ansatz, not `ENTROPY-LAYER-BRIDGE` globally.
- Two inequivalent compatible inverse systems are a candidate negative result
  for canonicity.
- Dependence on an unregistered gauge, private data, or a post-hoc cell
  orientation stops the construction.
- A measure mismatch is retained even if an equivariant bijection exists.
- No public issue or preregistration should be created until the local work
  yields a stable decision surface with an honest scope ceiling.
