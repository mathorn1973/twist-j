# Conditional local instrument: result and exact evidence

**PUBLIC, NON-CANONICAL. Accepted conditional L1 mathematics; candidate-T
proof and finite candidate-C audit evidence. Physical Stage C and the
Stage-D occurrence law remain open.**

Owner: A. M. Thorn. Original work, Apache-2.0. Result recorded 2 October
2026 for [issue #1329](https://github.com/mathorn1973/twist-j/issues/1329)
and draft [PR #1330](https://github.com/mathorn1973/twist-j/pull/1330).

## Result

The actual funded Stage-B packet permutation supports a conditional complex
instrument with full source/apparatus post-states and finite retained
histories. This requires an explicitly chosen complex Hilbert extension,
coherent pointer preparation, equal-energy source controls and a finite
externally scheduled archive protocol. None of those added structures is
derived from the classical transport law alone.

The exact preparation matters. A coherent uniform even pointer realizes
the prescribed parity Lüders instrument, including coherence inside its
three-dimensional HIGH branch. A blank pointer or an incoherent uniform
even mixture loses that coherence after pointer reduction, even though the
latter has the same pointer-position populations as the coherent state.
For the fixed reader and four specified source labels, with no additional
postcompensator, the coherent even state is the unique independent pointer density giving the target
instrument. This is a target-matching theorem, not a physical preparation
or occurrence mechanism.

The fresh independent reviewer accepted every frozen claim group F1-F7.
The separate proof and implementation were publicly frozen and executed
before that reviewer saw the author's C proof, code or output. The
[immutable per-claim review](https://github.com/mathorn1973/twist-j/blob/c3e31a5a201285c1d47c8f15520e7204e845a884/notes/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/REVIEW.md)
records **ACCEPT at the frozen conditional L1 scope**. No mathematical
falsifier or implementation discrepancy was found. No scientific source
changed after either freeze, and neither audit required a rerun.

## Construction and boundaries

The complete Stage-B carrier is unchanged. Its full basis permutation,
including dirty and unsupported states, extends to a unitary on the
complex space with that orthonormal basis. It preserves the full diagonal
energy. This extension does not identify complex amplitudes with integer
field labels. The admitted source controls act inside the specified
equal-energy shells; they are additional operations, not native B steps.

For N >= 2, T = 2N-1 and pointer modulus M = 1226, the actual clean B
evolution sends each supported label y and pointer p to the transported
label and p + w(n)c(y), modulo M, where

```text
w(n) = 0                            for n < N,
w(n) = 1 + floor((n-N)/(2T))        for n >= N.
```

The first funded WRITE is step N; RELEASE is step N+T. A 2T round returns
packet position, reserve and latch, retaining the pointer shift. For a
general joint input, each source ket/bra block X_ab is translated on both
pointer sides; apparatus correlations and untouched references remain in
that block. For an independent pointer density sigma and reader partition
Pi_o, the reduced branch coefficients are exactly

```text
gamma_o(a,b) = Tr[Pi_o S_c(a) sigma S_c(b)^*].
```

Agreement of all ordered coefficients is necessary and sufficient for
equality of the reduced instrument. It is not sufficient for equality of
the retained apparatus or every future protocol. Initially correlated
inputs require the full joint map, rather than a channel determined by
the source marginal alone.

Let E and O be the normalized coherent sums over the even and odd pointer
positions. Code translations act on their span by code-parity XOR. With
E readiness, parity reading gives the exact coarse parity instrument.
An added block Fourier unitary can map pointer basis states 0 and 1 to E
and O; it is reversible preparation control, not a reset of unknown dirty
states. Basis permutations and diagonal mixtures alone do not supply E.

The four literal H=1 labels have codes 395, 788, 648 and 620. Their
G-isometric complex encoding and declared pre/post source controls give
P_k rho P_k and Q_k rho Q_k for all five specified contexts and every
source operator, with finite references preserved. This checks all sixteen
matrix units, including HIGH off-diagonals. It does not infer a coherent
source vector from one classical packet. The fixed-reader uniqueness
argument uses positivity and the even fixed space of S_28, which is the
one-dimensional E line because gcd(28,1226)=2. O works only with its
declared reader relabeling.

Each of K archive cells contains a pointer and flag, with total added
energy 2K. The all-state append operation swaps the active pointer with
the chosen cell and flips that cell's flag. It is an energy-preserving
involution. On a fresh (E,0) cell it stores the actual old pointer and its
correlations, returns active E, and records flag one. On an occupied or
dirty cell it exchanges the actual data and toggles the actual flag;
readiness need not return. A flag can be flipped without a prior WRITE,
so the flag is not an unrestricted provenance certificate.

The positive record theorem therefore has a declared domain: clean
geometry, prepared source support, independent ready pointers, a funded
interaction and an unused cell selected by the finite protocol. Context,
epoch and invocation metadata are externally supplied. Operative resources
are renewed; the source density is not reset and can stay entangled with
earlier records. Exhausting K cells gives the external typed
RESOURCE_EXHAUSTED status with the state retained. It does not implement
an autonomous reversible absorbing halt. Source replacement would require
an additional accounted reservoir protocol.

For an admitted finite causal tree, composing the actual round gives
ordered branch operators K_w and complete conditional states
(K_w tensor I_R) rho_SR (K_w^* tensor I_R), tensored with the full K-cell
archive snapshot and ready operative factors. The snapshot includes
unused cells; adaptive cell allocation must not factor them out as one
common branch-independent state. Admitted coherent programs retain all
cross terms before declared parity dephasing. Arbitrary coherent stopping
or controlled append is not silently added.

Positive branch traces obey normalization and prefix consistency, with
zero branches left unnormalized. These are formal operator trace
identities, not a law selecting actual outcomes. Repeated fixed-context
readings of a retained source are correlated, not independent trials.
Passive archive marginals survive trace-preserving operations on their
complement. After record dephasing, admitted feedback preserves old labels
and prefix traces; before dephasing it can change archive off-diagonals.
Inverse rounds, reuse and direct archive controls lie outside passive
retention.

Whole-family equality compares retained joint maps for every admitted
finite protocol and input. In a finite energy sector with a fixed finite
operation alphabet it reduces to a paired reachable operator span of
dimension at most d1^2+d2^2. An effective algorithm additionally requires
effective exact coefficients. No algorithm for arbitrary unspecified
complex data, an uncountable alphabet or all unbounded sectors is claimed.

## Frozen sources and actual executions

The accepted B predecessor is
`05e2f457e9f7d69f6f6649e9ec4094f4ebb08eaa` in draft PR #1328.
The public C custody chain is:

| Role | Immutable commit |
|---|---|
| Specification before independent design | `0ca0605bee475ed3ab86f9a7c1129ea00a09d86d` |
| Complete author proof and verifier | `61a98eb1732ddf3effff0b386953e2fa7844f15e` |
| Independent proof and breaker before author exposure | `79d4d3ece7e473921e96634facdf8653e210a9b3` |
| Independent run records and final per-claim review | `c3e31a5a201285c1d47c8f15520e7204e845a884` |

All required source blobs were publicly read back before execution.
The specification already disclosed the construction, known target labels
and proposed claims; independence concerns the subsequent proof and
implementation, not blindness to that specification. The coordinator and
author's timing coauthor are not counted as independent reviewers.

The independent program ran first at its exact clean public pin. The
author program then ran at its own exact clean public pin. Each used
Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12, the recorded deterministic
environment, and a 600-second external timeout. Dates in RUN.md are UTC
1 October 2026, corresponding to local 2 October 2026.

| Audit | Exact command | Seconds | Exit / stderr |
|---|---|---:|---|
| Independent | `python3 notes/C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/break.py` | 18.102 | 0 / empty |
| Author | `python3 notes/C-FIELD-J-LOCAL-INSTRUMENT-N/verify.py` | 7.132 | 0 / empty |

Exact stdout is preserved separately, not fabricated as expected output.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Author PREREG.md | 36265 | `66f6df4102a5c88295926ea1c1afb8cbac56848d3ab19be7b84fea9e26ac8c2c` |
| Author PROOF.md | 42028 | `e9fb15931ce121a5face104c627663a48ead164c409d64b17945fffa3dc82baa` |
| Author verify.py | 38296 | `76f92f9b8fe0501f58d25bb16f3d066e3a0e5a39e01e80a1939657c88bd6bbcc` |
| Independent break.py | 28097 | `da26e40b9bbfd2534d0bc3e530d88fa505d9143d0d0c9542bb0e4493aeea69fd` |
| Independent stdout | 816 | `49bc7306bedebd523a7cfa7f886e4ab854c631cb7e7a31045f7bd4f4339b13b7` |
| Author stdout | 590 | `5ba56f3fa9036a0d5cc1fe13dba06250362850c3fbe38c6779c78fe106b694b1` |

Full environment, hashes and counts are in [author RUN.md](RUN.md) and
[independent RUN.md](../C-FIELD-J-LOCAL-INSTRUMENT-REVIEW-N/RUN.md).
Both implementations passed 3,006,152 append basis cases and 1,111 history
branches on 17,776 source units, as well as their separately specified
transport, pointer, context, reference, adaptive, capacity and family
checks. They use distinct exact algebra and audit domains; their stdout
is intentionally different. The universal result rests on the two
proofs and per-claim review, not on finite trajectory extrapolation.
These runs cover one architecture. Notes-only repository CI does not
execute these scientific programs and does not supply a two-architecture
scientific computation gate.

## Physical handoff and the Stage-D premise

The completed milestone is conditional instrument and history mathematics
on the specified carrier. The physical task still requires an independently
motivated preparation and apparatus mechanism that supplies the complex
structure, coherent ready state and context controls, plus a law and
semantics for actual terminal records. The deterministic funded WRITE
predicate supplies interaction timing; it does not select one parity
outcome. Substituting the proved branch traces as externally supplied Born
sampling would not derive that missing occurrence law.

A Stage-D proposal must specify those additional inputs and the complete
trial/record lifecycle, including correlations, zero support, exhaustion
and renewal. It must produce the realized finite-history law on this same
carrier and protocol; the established operator traces are the comparison
law, not its independently derived source.
The absence of such a proposal is an open premise, not a universal
sampling-impossibility theorem or a physical refutation. No empirical
comparison is claimed by this result.

Public authority remains canon-v96 at
`44423153eee6259c7277eec5f5adbed9679f9146`, with CANON.md 873495 bytes and
SHA-256 `eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2`.
QDD-INSTRUMENT-APPARATUS, QDD-TERMINAL-EVENT-SEMANTICS and
QDD-INSTRUMENT-CLASS-COMPLETENESS remain open; the existing selected-law,
ordered-history and native-law statuses are unchanged. This notes-only
proposal changes no Canon, registry, policy, gate, workflow, tag or release.
