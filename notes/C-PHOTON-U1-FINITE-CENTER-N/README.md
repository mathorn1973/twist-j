# Exact U(1) source functions from seven link values

**PUBLIC-source, NON-CANONICAL; no authority.**
Candidate `C-PHOTON-U1-FINITE-CENTER-N`, owner issue
[#1715](https://github.com/mathorn1973/twist-j/issues/1715).
Author: A. M. Thorn. Date: 2026-10-23. Apache-2.0.

For the plaquette weight `w(theta)=2+2 cos(theta)`, the complete finite
plaquette-source partition function in four dimensions is exactly the
same for U(1) and Z_N whenever N>=7. Seven is globally sharp on even
four-tori. This gives an exact finite alphabet for the selected U(1)
flux-response problem, with an algebraic reader and no angular
discretization error. It does not determine its phase.

The written results are **candidate-T**. The prospectively pinned finite
audits are **candidate-C**, with all three first executions passing. No
canonical status, computation-grade T gate, thermodynamic limit or
physical photon is asserted. The existing Z5 experiment #1116 is separate.

## Finite-source theorem

Let B be the oriented face-to-edge boundary matrix. Sum every edge with
normalized Haar measure and retain every topological sector. For any real
plaquette source a and integer edge insertion J,

\[
Z_G[a,J]=\mathbb E_A e^{i\langle J,A\rangle}
\prod_p[2+2\cos((B^TA)_p+a_p)].
\]

The character expansion has n_p in {-1,0,1}, with coefficient
`2^(|P|-|supp n|)`. It selects `Bn+J=0` for U(1) and the same equation
modulo N for Z_N. Therefore

\[
N>\max_e\bigl(\sum_p|B_{ep}|+|J_e|\bigr)
\quad\Longrightarrow\quad Z_{\mathbb Z_N}[a,J]=Z_{U(1)}[a,J].
\]

A four-dimensional cubical edge meets at most six plaquettes. Thus N>=7
suffices at J=0, on free boxes with all boundary links summed and periodic
tori of side lengths at least two. Nontrivial homology is included.
For the full insertion class `||J||_infinity<=1`, N>=8 suffices and is sharp.
Neither statement identifies arbitrary primal link observables.

The local incidence input is inherited from
[C-CURRENT-PRIME-GATE-N](../C-CURRENT-PRIME-GATE-N/PROOF.md), issue #1196.
The binary-pair interpretation is inherited from #1111. The present
contribution is the complete source-function extension, global witnesses
for every N=2,...,6, the insertion distinction, and the exact source reader.

## Flux response without a continuous-angle estimator

For a chosen orientation mu,nu let a source stack select faces with
`x_mu=x_nu=0`. For every integer-closed n,

\[
W=\langle n,\mathrm{stack}\rangle\in\mathbb Z,
\qquad \sum_x n_{\mu\nu}(x)=L_\mu L_\nu W.
\]

Consequently a stack source alpha and a uniform source
`alpha/(L_mu L_nu)` have identical full partition functions in U(1) and
Z_N for N>=7. At zero source,

\[
h=\left.\frac{d^2}{d\alpha^2}
\left[-\log\frac{Z(\alpha)}{Z(0)}\right]\right|_{\alpha=0}
=\operatorname{Var}(W).
\]

Write `x=2 cos(2 pi/7)`, so `x^3+x^2-2x-1=0`, and
`r=(2-x)/(2+x)`. On a primal Z7 configuration f=dA define
`G(k)=tan(pi k/7)/tan(pi/7)`. Its seven values lie in Q(x), and

\[
H_{\mu\nu}(A)=
\frac{V/2+(r/2)\sum_xG(f_{\mu\nu}(x))^2
      -r(\sum_xG(f_{\mu\nu}(x)))^2}{(L_\mu L_\nu)^2},
\qquad \mathbb E_7 H_{\mu\nu}=h.
\]

This reader has no pole on its sampled alphabet and uses only exact cubic
arithmetic. Its finite-volume bound need not be uniform in volume. A
sampled H may be negative. The expectation identity does not assign dual
W to a primal configuration, and seven discrete twists alone do not
recover the full winding variance.

The sampler implements exact local heat-bath probabilities. Its positive
weights give finite irreducibility and aperiodicity. They give no useful
mixing bound at growing volume. A seeded stream is deterministic engineering
input; the exact sampling-law proof assumes ideal independent fair bits.

## Frozen checks and their scope

Contract pin: `b7be3d00495330e4ac00441b865f9009e54a6299`.
Complete source pin, publicly read back before execution:
`9a74d03fb8f2c8086eff0f326446352f0f628082`.
The independent breaker was written without reading the primary module,
verifier or output. It uses a six-coordinate cyclotomic implementation,
while the primary uses rational cubic triples.

| Check | Exact result |
|---|---|
| Local words, degrees 0 through 6 | 1093 words, no alias at N=7,8,13 |
| Full-lattice sharpness | Every N=2,...,6 at L=4,6; inserted N7 witness |
| Topology at L=4 | Six wrapping sheets, 1024 cube boundaries, all stack positions |
| Conditional weights | 924 count vectors, 6468 masses, identical independent SHA-256 |
| 2x2 torus | 343 assignments, Z=18, h=1/9 |
| 3x2 torus | 16807 assignments, Z=66, h=1/33 |
| Three-cube boundary and disk | Z=66 and Z=2 |
| Sampler operation | Two sweeps at L=2,3, cold/hot starts; cache and readers consistent |

The common conditional-mass digest is
`04ef99ab864b0240d3d8b0039e538eaf18d79d999aeadf89a8cb624ae84a4e5b`.
The operation exercise has **zero phase decision weight**. Notes CI does
not rerun these scientific audits; its ordinary green checks do not supply
a two-architecture scientific gate.

## Review and next obligation

[PROOF.md](PROOF.md) contains the written argument;
[PREREG.md](PREREG.md) and [SOURCE-MANIFEST.json](SOURCE-MANIFEST.json)
freeze the finite audit. [RUN.md](RUN.md) binds commands and exact outputs;
[RESULT.md](RESULT.md) separates proof, computation and unearned claims.
[BREAKER_REVIEW.md](BREAKER_REVIEW.md) records the independent source
boundary. [POSTPIN_REVIEW.md](POSTPIN_REVIEW.md) and
[SAMPLER_REVIEW.md](SAMPLER_REVIEW.md) record subsequent review.
[MEASUREMENT.md](MEASUREMENT.md) specifies the observable and prospective
production obligations. [PROMO.md](PROMO.md) requests mathematical review.

The next unresolved experimental task is full-measure sampling with a
separately frozen qualification, size law and uncertainty contract. The
next mathematical task is a thermodynamic response bound with its correct
observable consequence. Stability back to Z5 remains a further obligation.
This package closes none of those by finite positivity: already in two
dimensions `h=2/(2^A+2)>0` at each finite area but tends to zero.
