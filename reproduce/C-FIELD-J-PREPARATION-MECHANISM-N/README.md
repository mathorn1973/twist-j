# Preparation mechanism: exact finite audit

**PUBLIC, NON-CANONICAL. Conditional L1 candidate. Scientific execution
is pending the complete public source pin and its readback.**

This reproduction accompanies
`notes/C-FIELD-J-PREPARATION-MECHANISM-N/PROOF.md`. Its immutable
specification is `notes/C-FIELD-J-PREPARATION-MECHANISM-N/PREREG.md` at
`7809098069d4c4ff9f362048cf92c3e8b4714493`, SHA-256
`c164cfaf7cf24537d899760e06304a9f94d269e4f376810d67c856d86cdc9b2d`.
The inherited Stage-C reference is
`024936502544c2ec45acc8890a052c7b3aca26be`. No predecessor script is imported.

The model supplies fresh basis-state bath qubits and a phase-aligned local
reflection on adjacent modes of a newly declared even-pointer ring. Every
bath output is retained. It replaces independently supplied coherent E
pointers with a finite approximate loader; it does not derive physical
controls, pure baths, source preparation, a Born rule or actual occurrence.
Locality refers to the added internal mode graph, not an inferred B-chain
spatial implementation. Flat-energy conservation is the stated scalar
ledger, not a physical work-cost calculation.

## Execution and custody

After the complete proof and source have been publicly frozen and read
back, run from the repository root on Linux or a Linux-compatible system:

```text
python3 reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/verify.py
```

The script requires Python 3.10 or later and only the standard library.
It reads no files, makes no network calls, imports no predecessor code,
uses no randomness, and writes only deterministic summaries to stdout.
All scientific calculations use integers and `fractions.Fraction`.
Square roots in normalized vectors are handled by rational unnormalized
amplitudes with an explicit density weight. No floating-point spectral
calculation or numerical trace norm is used.

The registered limit is 120 seconds, exit status zero and empty stderr.
No performance result or scientific PASS is claimed before execution.
`EXPECTED.txt` must be populated from the actual pinned run, and RUN.md
must record its exact source, environment, stdout bytes and hash. Neither
file is an author-generated guessed result. The existing
`tools/check_reproduce.py` will replay this directory and compare stdout
byte for byte. Successful x86_64 and aarch64 runs must be observed; notes
checks or mathematical portability alone do not establish them.

## Frozen finite domains

| Group | Exact domain and principal checks |
|---|---|
| Local dilation | L=3,4,5,7, every edge; full 2L-pointer times two-state bath; 396 inverse basis cases and 2,236 fresh-bath source matrix units. Reflection/generator identities, odd-sector identity, flat energy, Q/J completeness and dirty-bath loss. |
| Contraction | L=3,...,12, restricted L-by-L even-sector matrices; telescoping no-jump loss, wrap-around overlap rows, row/column norm bounds and exact positive-semidefinite certificates for the registered inequalities. |
| Reduced preparation | L=3,4,5; every basis density and I/L, P_E, P_d0, P_s0; four sweeps, 120 state/boundary cases and 392 edge collisions. Trace, positivity, contraction, bath-mark identity, dyadic closure on dyadic inputs and equal-population controls. |
| Retained environment | Two L=3 pointers and six distinct bath bits; one correlated source/reference state and one basis product. Complete sparse amplitudes, inverse recovery, untouched reference marginal, reduced-channel agreement and joint projection/marginal identities. |
| Phase/exact boundary | All 184 edge-sign patterns at L=3,4,5,7; common-kernel rank, compatible dark line, local stationarity, and distinction from E. Exact non-dyadic entry 1/613. |
| Handoff | Nine budget descriptors K=0,1,2 and n=0,1,2 at L=613; all four abstract source units and both parity outcomes at the 120 reduced boundaries, giving 960 composition cases. Complete read traces, passive rereads, no hidden normalization and finite resource addresses. |

The positive-semidefinite routine uses exact symmetric Schur complements:
a zero pivot requires an exactly zero remaining row. Retained-state
partial traces are exact Gram sums, including all unmeasured bath and
reference coherences. The two-pointer union remainder and the positive
remaining-marginal decomposition are checked on both retained states.
The source-unit handoff checks act on their full pointer blocks; retaining
the source matrix unit makes their treatment equivalent to the complete
two-label controlled shift, including off-diagonal source operators.

The budget audit concerns explicitly classical finite-script descriptors.
It neither simulates the large sufficient cooling budget at L=613 nor
creates an autonomous resource counter, readiness validator or flag-reset
gate. The primitive's identity action on spectator flags and the absence
of an actual measurement occurrence are part of the stated proof scope.

There is one PASS summary per group, then the fixed resource formula and
the scope line `approximate pointer preparation; occurrence NOT DERIVED`.
The script stops at the first failed assertion. It performs no searches
outside the frozen domains and no output-driven adjustment of a constant.

## What the audit does and does not establish

The universal L>=3 even-sector convergence rate, arbitrary correlated
bank approximation, and all-finite-horizon C interface are analytic proof
claims. The small finite matrices are audits of those proofs, not an
extrapolation to L=613. The bound compares the prepared bank jointly with
its **actual remaining output marginal**, including all baths. Subsequent
C protocols keep these baths as untouched references. One fixed bank
contributes one joint error bound; no factor proportional to the number
of subsequent reads is introduced. Rare normalized branches can amplify
error, and an ideal zero branch may receive a small nonzero weight.

The rationality obstruction applies to a dyadic initial pointer marginal
and the declared zero-phase operations. In particular, basis-blank
pointers remain covered even if their untouched source/reference density
has non-dyadic or complex entries. It excludes exact finite E preparation
by this unconditional loader; it does not exclude different interactions,
postselection, already supplied E, or an initial non-dyadic pointer.

The verifier was authored by algebra_builder. An author-side
preparation_proof coauthor prepared the companion proof from the frozen
specification; coordinator paper feedback is disclosed there and in the
specification. This assistance is not the separate fresh review. No fresh
review derivation, code, branch or output was inspected by this author.

Original work, Apache-2.0. Owner: A. M. Thorn.
