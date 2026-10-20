# P-RELATIONAL-MASS-JOINT-ACTION-1

**NON-CANONICAL, NEW_DECLARED L1.** This probe puts the relational source
energy from #1685 and a dynamical planar inverse metric in one Hamiltonian
action. Its first pinned run passed; required x86_64/aarch64 acceptance is
a separate gate recorded in the PR receipts. Canon authority is unchanged.

The declared carrier is a symmetric positive-definite matrix G, symmetric
momentum Pi, and continuously varied positions x_k and nonzero covectors
p_k. Positive integer multiplicities n_k are fixed labels; pentagonal momenta are initial
data, not a restriction on variation. The action uses

    theta = tr(Pi dG) + sum n_k p_k^T dx_k,
    H = K + E,
    K = (1/2) tr(G Pi G Pi),
    E = sum n_k sqrt(p_k^T G p_k).

The positive metric kinetic term, with coefficient one, is a new explicit
choice. It replaces the old scalar kinetic carrier in this question;
no old-field-to-G identification or inherited lapse/Ward law is supplied.
Variation yields a reciprocal source T_G/2 = partial_G E in Pidot and
xdot_k = G p_k/epsilon_k, with pdot_k = 0. The mass-square response
E T_G - P P^T is a different derivative and is not substituted for this
energy source.

[PROOF.md](PROOF.md) establishes the following universal statements for
this declared finite-dimensional model:

- The continuous flow is unique for all real time and G remains positive
  definite at every finite time. Total H, the matter momenta and the full
  coordinate charge J = 2 G Pi + sum n_k x_k p_k^T are conserved.
- Matter and metric exchange energy: Edot = tr(T_G Gdot)/2 = -Kdot.
  The dilation C = tr(G Pi) obeys Cdot = -E/2. For nonempty matter,
  E tends to zero at both time infinities, K tends to H, and
  D_G = E^2 - P^T G P tends to zero. If occupied momenta span the plane,
  G tends to the zero matrix. This is an inverse-metric boundary result,
  not a statement of physical spatial collapse or a supplied binding law.
- A free lapse multiplying H alone excludes nonempty matter. Adding a
  canonical clock pair gives the separately declared constraint p_t+H=0.
  Sampling the exact continuous flow at integer times gives a symplectic,
  energy-preserving map, but does not provide a finite exact evaluator,
  integer-valued states or a native implementation.

The proof also studies a separate symmetric discrete-gradient (DG)
relation. It preserves total energy and has a local second-order branch
near step zero. An exact positive-metric endpoint witness exchanges
E: 6 -> 5 and K: 0 -> 1 at h=1100/1921. Its charge defect is
Delta J = -(792/1921) I, and the induced isotropic step's Jacobian determinant is
528275/341526 rather than one. Full implicit regularity and the restricted
canonical form prove that this admitted branch is nonsymplectic. The
witness is not identified with the branch continued from step zero;
a separate cubic charge defect also rules out exact-flow identity on
that local branch. No global DG solver or unique step-one update is claimed.

The finite audit uses exact arithmetic in Q(phi), with no floating point:
32 binary preparations times seven metric momenta, FLOW and DG series
through degree four, six coordinate transformations, one finite witness
and eight negative controls. Two isolated implementations independently
agree on the 2,550-record payload hash and the raw certificate bytes. These
finite checks support the analytical proof; they do not replace its
universal arguments.

Replay from the repository root:

```sh
python3 probes/P-RELATIONAL-MASS-JOINT-ACTION-1/verify.py
```

The primary launches the independent breaker and requires byte-identical
certificates. [PREREG.md](PREREG.md) fixes the domain and protocol;
[SOURCE.md](SOURCE.md) records authority and provenance;
[FROZEN.sha256](FROZEN.sha256) binds the five prospective files.
[RUN.md](RUN.md), [RESULT.md](RESULT.md), [REVIEW.md](REVIEW.md) and
[EXPECTED.txt](EXPECTED.txt) record the first run at pin
`f19fa98dc1634ce1e17b9dec402c51920d2bea8d` and its exact output.

The next gravity claim must supply an explicit bridge to the existing or
native carrier and justify the new kinetic choice. Persistent source
energy would additionally require a declared mechanism that changes the
proved long-time limitation, with its own conservation audit. This probe
supplies no local density, spatial propagation, scattering, stable
particles, physical calibration or equality of inertial and gravitational
mass. Any computable discrete replacement must separately establish its
energy, charge and symplectic properties.
