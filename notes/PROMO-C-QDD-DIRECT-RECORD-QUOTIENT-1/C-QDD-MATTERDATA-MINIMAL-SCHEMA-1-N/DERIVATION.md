# Derivation

Status: candidate-T, NON-CANONICAL incubation.

Write the five top-level direct record fields as

```text
S support_state,
M total_weight,
B branch_weights,
R density_state,
N normalized_weight_state.
```

A field subset is record-complete when its equality is exactly full direct-record equality on `K_QDD`.

## Sufficiency

`{M,R}` is complete. On the supported branch,

```text
A=v v^T = M rho G^-1.
```

The density tag handles the zero branch. Thus `{M,R}` reconstructs the quadratic class, and the direct record is fixed on that class.

`{B,R}` is complete because the raw ordered branch weights satisfy

```text
M=w_low+w_high.
```

It therefore reconstructs `{M,R}`.

Every superset of either pair is complete.

## Necessity of density

The exact vectors

```text
v =(1,0,0,1),
v'=(1,1,0,0)
```

have equal

```text
S,
M=6/5,
B=(1/5,1),
N=(1/6,5/6),
```

but distinct quadratic matrices and distinct density fields. Hence no subset omitting `R` is complete.

## Necessity of a raw scale field

The vectors `e_0` and `2e_0` have equal support, density and normalized weights, but different total weights and different quadratic matrices. Hence a subset containing `R` but neither `M` nor `B` is incomplete.

Therefore a subset is complete exactly when it contains `R` and at least one of `M` or `B`. Among five fields there are

```text
2^4 - 2^2 = 12
```

such subsets. The inclusion-minimal complete subsets are exactly

```text
{M,R},
{B,R}.
```

The classification concerns equality information only. It does not authorize deleting fields, changing ownership, or altering downstream types.
