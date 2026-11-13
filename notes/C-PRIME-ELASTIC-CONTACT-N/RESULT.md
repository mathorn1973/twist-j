# Local result and exact limitations

Candidate: C-PRIME-ELASTIC-CONTACT-N
Author: A. M. Thorn
Date: 2026-10-30
Status: NON-CANONICAL / L1.
Analytical statements: candidate-T in the declared comparison model.
Finite computation: candidate-C, one local x86_64 execution.

## Actual result

The three inputs in FROZEN.sha256 were frozen and checked before the first
scientific execution. The first execution passed all assertions with exit 0
and empty stderr. No post-run source, range or threshold change occurred.

- 72 positive one-body input values and all 5184 ordered pairs.
- 32 odd positions per pair and each of two selected contact laws.
- 331776 extended states audited in total.
- Exact inverse in both orders, conservation and sampled injectivity pass.
- Under kappa=0: 165888 distinct sampled outputs; 57858 transmissions.
- Under kappa=1: 165888 distinct sampled outputs; 8900 reflections and
  48958 transmissions. Non-crossing steps are not counted as collisions.
- The explicit naive crossing rule remains noninjective.
- All 64 fixed-modulus negative controls and the variable-modulus guard pass.
- The oriented norm-209 factorization agrees with the supplied discussion.
- The complete decomposition fibre at z=3+2phi has four ordered states.
- Its inelastic (1,4)->(1,5) example is integral in momentum but gives the
  exact residual position 3/2 under the selected common beta-stream tick.
- The physical COM relative-speed ratio is separately -8/15, not -1/2.

Environment: Debian GNU/Linux 13 (trixie), x86_64, Python 3.13.5.
Command: python3 -I verify.py, 120-second process limit.
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. Integer and Fraction arithmetic only.
Stdout: 731 bytes, SHA-256
6170ec64df9d8b7f77050f4c4953402a1e3ed1573c85e757b0a6a949ddd4b40d.

## What the result does not mean

This is not an independently reviewed result, a public probe, or the pinned
repository two-architecture computation gate. The earlier PR #1837 has its
own separate run record. No architecture credit is transferred from it.
The universal statements rest on PROOF.md, not finite sampling.

The scattering rule, odd position carrier and stream law are declared
choices. Adding position does not force reflection instead of transmission.
No native U, universal clock, finite physical propagation range, detector,
interaction Hamiltonian, nonzero-beta bound orbit, bound-state spectrum,
probability law, physical chirality or L1-to-L6 bridge has been derived.
The inelastic lattice failure applies to the specified common-tick rule;
it does not exclude other complete reversible inelastic constructions.

No GitHub issue, branch, file, PR, Canon or registry was changed in this
continuation. These local files are review material, not Git authority.
