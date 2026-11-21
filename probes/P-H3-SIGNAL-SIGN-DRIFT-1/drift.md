# Finite compact cold material drift census

Use one vertical column in phase 0, with initial lower support endpoint
at unwrapped y=0 or y=1. The two exact rail representations are
`(u,0,0,0)` and `(u,-u,0,0)`. Every other cell is vacuum. B is inactive
in this sector. C acts railwise, and the simultaneous global sign
symmetry and absence of all other words keep the single-rail reduction
exact. The fast checker uses the public transport pair on each matching
in the unwrapped line, including both live-vacuum boundary contacts.
Absolute support and every zero between its extrema enter the state.

The alphabet is zero and both signs of
`1, 2, J, conjugate(J), 2J, 2 conjugate(J), rho, rho^-1`.
For widths two through four, enumerate all nonzero-endpoint profiles with
zero total word. In a separate nonzero-total class enumerate all nonzero
alphabet endpoints with interior empty, `(0)`, `(1)`, or `(-1)`. The latter
is an explicit bounded sample of nonzero-total preparations. Each total
and width has its own count. Both signs are present in the census.
The matching has one bit of clock state; initial anchoring distinguishes
the two layouts without changing the initial clock color.

Search the first compatible marked relative return through 24 native
steps. A return at p with signed displacement d requires equality of
the entire profile after multiplication by a single element of
`{+/-rho^j:0<=j<5}`, translation by d, and `p=d mod 2`. The last condition
means that the translated starting matching has the same bit as the
actual p-cut. Since the evolution is equivariant under combined
translation/color change and common unit multiplication, such a
return would generate exact unwrapped periodic drift with velocity d/p.
Raise the phase to its finite order and, when needed, additionally
restore the original matching color by taking an even multiple of p.
The first marked return divides the same profile into stationary fields,
exact zero-shift internal returns, phase-only zero-shift internal returns,
and nonzero shifts. A seed with no observed marked return belongs to a
separate bounded category. Nontrivial refusals count pairs of unequal
words of different parity through the first return or through the horizon.
Stationarity is checked by literal field equality at all preceding cuts.

For every proposed nonzero shift, replay its p steps through the full
native two-dimensional update on two padded rectangular tori.
Independently replay three fixed controls at the full horizon:
`(1,-1)` anchored at 0, `(-2,0,2)` anchored at 1, and
`(2J,-2J,rho,-rho)` anchored at 0. The first embedding uses width 4 and
the single rail. The second uses width 8, six extra height rows,
antipodal rails and the spatial reflection `y -> 1-y`. Reflection sends
a lower matching endpoint p to -p. The contact matrix is symmetric under
the interchange of its two endpoints, so the reflected contact remains
forward. Padding
excludes any wrap. The replay checks whole fields at C and B, the full
native inverses and the complete native accounts. Absolute support is
retained at launch and at the terminal cut. A site outside the launch
support is listed with its first occupied cut and exact local matter Q.
The fixed controls test visible transport away from the launch support
even in the absence of rigid translation of the entire packet.

A nonzero matched shift is a falsifier of the compact-vacuum no-drift
decision, even with no parity refusals. Emit it with its signed speed,
exact full period, full shift and native replay results. Any alternate
execution of a frozen replay or native conservation/inversion failure
is diagnosed separately. The independent compact-state residue
obstruction and its interacting scope are stated in the main probe.
The census supplies exact finite controls for that result and does
not classify internal periods above 24, other alphabets, background
states, or motion of a selected part of a profile.
