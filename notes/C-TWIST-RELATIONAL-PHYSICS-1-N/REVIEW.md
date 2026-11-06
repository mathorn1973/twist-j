# Analytical review and required physical distinctions

**NON-CANONICAL.** This review was performed by a separate analytical agent
within the same authoring session. It is not external peer acceptance and
does not promote a public scientific status. No new scientific checker was
executed for this pre-freeze review.

## Mathematical assessment

Under the pinned complete apparatus and source assumptions, the reviewer
found the prefix conjugation, full degenerate spectral projectors,
complementary positive clock energy, isometry, Fourier sign, uniform clock
probabilities and arbitrary mixed/passive-reference extension consistent.
The 188-index clock window, strict Markov bound and complete joint-event
contrast follow with the declared signs and endpoints.

The complete fixed-energy shell has exactly one clock partner for each
apparatus energy, with full data multiplicity. It is precisely the range of
`V`, not a selected rank-one code. Consequently the compressed effects are
positive, sum to the shell identity, and commute with total energy. `E_out`
is necessary to complete the POVM on imperfect full-carrier inputs.

## Physical interpretation that the result actually permits

The carrier, ready correlations, Hamiltonian, clock labels, complete POVM,
square-root instrument, Born law and applicability are specified physical
postulates. With those choices, a finite effective physical theory is
well defined. The following distinctions are part of its statement.

1. Fourier clock projectors define conditional slices. Physical constrained
   outcomes use the global compressed POVM. The latter is generally neither
   local nor projective.
2. A local conditional apparatus density is not its postmeasurement density
   under the adopted global instrument. Every shell-supported state has an
   apparatus marginal diagonal between distinct apparatus energies.
3. The square-root instrument for the coarse clock effect `Q_*/561` differs
   from the fine `(j,y)` square-root instrument with `y` forgotten.
4. An isometry's complete unitary extension is not a proof of an energy-
   conserving, thermal or native preparation. Its spectral controls can
   contain the full computational complexity of the apparatus word.
5. The robustness result bounds implemented probabilities. Sample frequencies
   require a separately fixed statistical rejection rule.
6. The finite carrier count excludes any passive reference and any physical
   implementation resources not supplied for preparation/readout. A passive
   reference can be infinite-dimensional and has zero Hamiltonian here.
7. The chosen time step is `Delta_tau=pi hbar/E_ctl`; the zero clock label
   has `tau_0=0`. The clock is cyclic and has no unbounded cycle register.

The independent checker in `break_check.py` was developed separately from
the builder implementation, using the fixed contract and pinned source
definitions. Its execution and arithmetic outcome belong in the subsequent
validation record; they are not claimed by this pre-freeze review.

## Separate known physical obstruction

The naive common frequency/wavevector reading of the fixed `mu=0,2` walks
does not give ordinary common Lorentz dispersion. The rest and curvature
masses differ by `mu/atan(mu)`. `PHYSICS_BOUNDARY.md` keeps this analytical
obstruction separate from the finite apparatus Hamiltonian.

No derivation from native `U`, species identification, proper-time law,
gravity, irreversible archive, laboratory realization or fundamental
empirical success follows from this review.
