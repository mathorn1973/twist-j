# Completed parity certificate: insufficient remainder bound

**NON-CANONICAL. L1. Exact finite result under the pinned source premises.**
A. M. Thorn. 2026-10-26. Apache-2.0.
Reservation: [#1788](https://github.com/mathorn1973/twist-j/issues/1788).

Status: INCONCLUSIVE

The first execution completed with exit zero, empty stderr and integrity
PASS. Both original settings have `d<0`, so neither passes the fixed
necessary-and-sufficient algebraic comparison for this sufficient physical
certificate. The positive values of e do not overcome the failed d guard.

| Setting | Sign of d | Sign of e | Gap versus 1/1800 | Disposition |
|---|---|---|---|---|
| Original plus | -1 | +1 | LT | INCONCLUSIVE |
| Original minus | -1 | +1 | LT | INCONCLUSIVE |

The unchanged [EXPECTED.txt](EXPECTED.txt) contains all exact norm and
comparison expressions in Q(sqrt(5)), the complete common spatial support
and the forward/backward support counts through power twelve. Both full
remainder norms agree exactly, as required by the equal source spectral
laws. Every iterate norm, support, parity and inverse-step check passed,
together with both source normalizations, seed moments, coefficient
identities and exact-comparison boundary checks.

## What the result does and does not establish

The conservative common projection in PROOF.md excludes matrix elements
of every physical term of diameter at most two. The parity identity and
degree-nine approximation give the rigorous lower bound

    error/E0 >= (pi/2)(sqrt(W_sigma)-sqrt(R_sigma)),
    W_sigma=||F p4(A)psi_sigma||²,
    R_sigma=||C^10 psi_sigma||².

This finite bound does not reach E0/1200 for either source. The full
remainder is too large for this comparison. It is essential that R is
the unprojected norm: projecting it onto the opposite-parity subspace
would give a false zero remainder and an invalid positive result.

The result is not an upper bound on the actual forbidden energy tail.
It proves neither a diameter-two realization nor the impossibility of
one. In particular this result does not establish that higher-degree
approximations fail. The earlier stopping rule for the different filtered
carrier test in [PR1787](https://github.com/mathorn1973/twist-j/pull/1787)
does not apply to this parity method. The conditional diameter-one
obstruction in [PR1785](https://github.com/mathorn1973/twist-j/pull/1785)
remains unchanged.

Further progress needs a stronger controlled estimate, for example one
that bounds the error against a selected forbidden output vector rather
than its full norm. Any new scientific execution requires its own fixed
equations, identifiers, program and public pin. This probe's degree,
projection, sources, thresholds, verifier and output remain unchanged.

## Custody and acceptance

Prospective public pin: `55b6472d8b3081dd22f26439f09eb31d2e8dba69`.
Verifier SHA-256:
`43b2f564b97833d1d222d5a06c429d5f9ebee51f929828af67cd48a95a246aad`.
The three pinned files were publicly read back before execution. The first
stdout is 3099 bytes and 29 lines, SHA-256
`49001f332e87d27caa8bc286c8804a8a998d663c3d18ef73a6ec434f1d6e74d2`.
[RUN.md](RUN.md) records the local run. Required two-architecture replay
evidence belongs in the pull request once earned.

Two other same-session agents statically reviewed the complete proof,
program and final preregistration before the pin. These checks found no
substantive defect; they are not external independent scientific acceptance.
The twelve proof obligations remain available for that external review.
Only this probe directory changes. Public Canon v105 remains the authority.
