# Composite inertia: a precise boundary and a finite-time response

NON-CANONICAL, L1. Ownership: [#1690](https://github.com/mathorn1973/twist-j/issues/1690).
Continuation of the accepted rest-sector binding proof in #1689; no Canon
change and no repeated audit of that predecessor.

The full action already specifies nonzero-momentum motion. What fails is
the proposed continuation of its stable minimum into a moving inertial
energy branch. At fixed full elliptic charge and nonzero total momentum
there is no constrained local energy critical point or affine relative
equilibrium. For the old witness charge, the global energy infimum jumps
from ten at zero momentum to zero, unattained, at every nonzero momentum.

The immediate response is still computable. Its energy Hessian at the
fixed rest preparation is diag(1/6,0). Across charge-exact preparation
sections with the same rest point it can have any quadratic coefficient.
For one explicitly chosen preparation and one old orbit period, the
center displacement derivative is instead diag(1/12,1/24).
This finite-time observable is not a bound-state mass or dispersion law.

- [PROOF.md](PROOF.md): exact theorems, counterexamples, response and limits.
- [PREREG.md](PREREG.md), [FIXTURES.md](FIXTURES.md): immutable task and audit.
- [RESULT.md](RESULT.md): conclusions and remaining physical distinction.
- [RUN.md](RUN.md), [EXPECTED.txt](EXPECTED.txt): first exact PASS, aarch64.
- [REVIEW.md](REVIEW.md): same-session analytical and source review.
- [SOURCE.md](SOURCE.md): pinned sources and authority boundary.

Run from repository root:

    python3 -I probes/P-RELATIONAL-MASS-INERTIAL-RESPONSE-1/verify.py

The standalone standard-library verifier is exact and needs no external
data. Required PR CI replays its committed stdout on x86_64 and aarch64.
Universal nonexistence and limiting statements rest on the written proof.
Other kinds of moving bound trajectories remain open.
