# RESULT: failed first audit

**Status: FAILED FIRST AUDIT. NON-CANONICAL. No candidate-C earned.**

The frozen verifier at
`b98c4a8710b641e20f05b33de612d776d02a707c` exited nonzero in the
second multi-edge gluing fixture. The pin is preserved and is not reused.

## Exact diagnosis

The failing fixture used face amplitudes

`
(1,1,2,2)
`

and the two edge equations, for face signs `x_i in {+1,-1}`,

`
x0 + x1 + 2 x2 + 2 x3 = 0 mod 5,
x0 - x1 + 2 x2 - 2 x3 = 0 mod 5.
`

Adding them gives

`
2 x0 + 4 x2 = 0 mod 5,
`

hence `x2 = 2 x0 mod 5`. This is impossible for
`x0,x2 in {+1,-1}`. Therefore that fixture has no admissible global sign
assignment. The assertion that its direct solution list was nonempty was a
fixture-design error.

This diagnosis does **not** falsify the local projector, the completion law or
the conditional-thinning route. The run terminated before the preregistered
four-cup and torus-witness tests, so none of those receives computational
status from this pin.

## Preserved diagnostic findings

Before the fixture failure the frozen program exactly checked:

- all nine face pairs;
- all 153 allowed one-copy edge stars and 23,409 ordered replica-star pairs;
- 18,862 labelled charge-faithful partitions and all 8,191 token sign
  assignments, with 1,719 admissible assignments;
- 12,616 abstract exterior signed-relation cases;
- an exact abstract conditional charged fraction equal to one.

Because the whole audit failed, these are diagnostics, not a successful
candidate-C package.

## Next action

A successor must use a new candidate identifier and a new preregistration.
It may replace only the defective gluing fixture and must retain the scientific
scope and route threshold. It must again be frozen publicly before execution.

Uniform `Xi_L`, `Xi_L^(2)`, infinite-volume decay, a massless phase and P1
remain OPEN.
