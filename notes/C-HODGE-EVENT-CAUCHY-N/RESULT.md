# Result: stable scalar Cauchy evolution on actual Hodge events

Status: PUBLIC NON-CANONICAL.
Ceiling: candidate-T proofs, candidate-D choices, candidate-C exact audits.
Owner: #1239. Author: A. M. Thorn <thorn@twistj.com>.

## Constructed

An injective marked Z x Z^3 grid is embedded into actual events of the
existing windowed Hodge spacetime, at scale n>=3. Equal-time marked slices
are spacelike; consecutive same-site events are future timelike.
The field lives on this selected subcarrier, NOT all of M/n^4.

The exact scalar law is

    f_(m+1)-2f_m+f_(m-1)+K f_m=delta^2 j_m,
    K=sum_i alpha_i(2I-shift_i-shift_-i),
    alpha=((5+2sqrt5)/16,(5+2sqrt5)/48,(5+2sqrt5)/60).

Its stability margin is positive, with

    sum alpha=1/2+sqrt5/5<1.

Written all-class consequences:

- unique forward continuation and reverse step for finite-support data;
- self-adjoint positive spatial K and a strictly positive conserved
  two-slice energy on every nonzero finite-support pair;
- exact source-work identity, retarded Green recursion and finite
  marked-stencil dependence;
- O(n^-2) finite-time smooth-solution convergence to Box_g f=0;
- O(n^-2) local finite-time comparison of the registered principal D3 modes
  with genuine exact solutions on the selected event subcarrier.

The last statement is stronger than the predecessor's small-residual mode
comparison, but it uses a DIFFERENT selected field operator and subcarrier.
It does not establish stability of the old all-event rounded Box_n.

## Important negative result

Character group speeds in the ideal orthonormal Hodge frame obey |v|<=1.
Nevertheless the exact one-step impulse has a nonzero coefficient at an
actual rounded event outside the source event's Lorentz cone (n=8).
Thus the scheme is retarded in its marked time but does NOT have exact
microscopic Lorentz-cone support. The two claims must be quoted together.

## Reproduction

The unchanged prospective model/audit sources were run on arm64 and x86_64.
Both passed, with empty stderr and identical 715-byte stdout. This is
reproduction, not independent-agent confirmation or Canon promotion.

## Remaining boundary

This completes one explicitly selected flat mathematical spacetime PLUS a
stable propagating scalar field. It does not derive E+, the window, the
marked mesh or its field law from native Omega,U. It does not prove Galois
physical equivalence, full-event dynamics, exact finite-scale J/C5 symmetry,
global D3 action/measure transfer, vector polarization, a physical massless
phase, SI scales or matter-curved geometry. Canon v92 and all public
frontier owners remain unchanged.
