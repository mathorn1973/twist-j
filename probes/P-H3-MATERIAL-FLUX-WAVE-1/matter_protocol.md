# Localized matter, matched accounting, and the momentum gate

Use the unchanged two-color H3 matching on the width-eight, height-twelve torus. Take
the origin of the measured axis at row 4, so rows 3 through 5 are an
unwrapped interval. The controls use matter rails `(d,-d)`, zero
radiation, and no other occupied site.

* With `d=1`, an occupied/vacuum contact is refused by parity at both
  colors. B is inactive. The field is stationary, and the matching color
  returns after two steps.
* With `d=2`, the initially active bond splits the field between rows 4
  and 5. After k rotations on that bond, the positive rail's pair has
  values `(1+rho^k,1-rho^k)`; the negative rail has their negatives.
  Modulo two, rho has order five. This follows because its cyclotomic
  polynomial has neither a root nor a quadratic factor over F_2.
  Both split words are therefore odd for k=1 through 4 and refuse
  every intervening outward match into vacuum. At k=5 the field returns
  to row 4. The matching color is opposite at this cut, so the next
  step starts the same cycle on rows 3 and 4. After 18 steps the
  complete field and original color return. The field returns first
  at step nine, with the opposite color. Both exact trajectories have
  zero net displacement per full period. At the 18-step cut the checker
reports the modular displacement in both coordinates if the complete
singleton profile is an exact translate, and otherwise records no
translation. The matching color at that cut is the initial color.

For the collision comparison start at a prescribed post-C cut with resident
half-gap `d=2` and incident radiation half-gap `f=0, 2J, 2J^-1`.
Choose zero centers. Recover the preceding full cut using the native
backward C rule, then replay both steps and their inverses. In the zero arm
put both nonzero incident codes at distinct radiation-only sites in column
4. In each nonzero arm relocate its incident code from that spectator
column to the resident, leaving the other code in the spectator column.
Thus each preparation has the same complete input ledger, including
the exact Hermitian account. No spectator is in the resident's neighborhood
of the next C. The active B tags are respectively 0, 1, 2.

On the next C consider either orientation, with row 4 joined to row 5
or row 3. The matter Q weights in resident/new-site order are `(6,10)`,
`(14,10)`, and `(4,20)`. B changes the material total Q from 16 to
24 in both active arms; C redistributes that total within the bond.
The outward signed center-of-Q shifts, before multiplication by the
orientation, are respectively `5/8, 5/12, 5/6`. Relative to the
zero arm the two excesses are opposite, `-5/24` and `+5/24`.
The signs reverse when the orientation of the adjacent edge is reversed.
These are finite current and redistribution controls at one C cut.

## Restricted additive momentum obstruction

Consider an additive rational-linear readout of the native words, with a
fixed functional on each of the four rails, invariant under all spatial
translations, and conserved by each native substep for every state.
Write `a` for the matter rail-functional difference and `b` for the
radiation rail-functional difference. B1 is admissible for every nonzero
integral word d with zero centers and `f=+Jd` or `f=-Jd`.
For either choice, conservation requires
`a((J-1)d) +/- b((1-J)d)=0`. Adding and subtracting gives
`a((J-1)d)=b((J-1)d)=0` for every d. Multiplication by
`J-1=rho` is an integral automorphism, so `a=b=0`.
The remaining readout is a linear functional of the two rail-pair
totals M and U, each conserved by C and B. Such a readout is even
under pure row reflection acting on positions and keeping rail labels
and word coordinates fixed. Hence no nonzero readout in this class
can be odd for that reflection. Reflection here is a test on the
readout's orientation, with no asserted dynamical symmetry.

These two preparations and the linear obstruction leave the inertial
test open. To test an inertial relation one must separately establish
a translating isolated material packet, a conserved directional
quantity or an exact exchange law on the interacting carrier, and a
comparison of that quantity with independently measured motion across
prepared impulses. This preparation supplies a change of material Q and
its distribution on a specified bond. Nonlinear, position-dependent,
matching-color-dependent, topological and dressed momentum readings
are outside the obstruction.
