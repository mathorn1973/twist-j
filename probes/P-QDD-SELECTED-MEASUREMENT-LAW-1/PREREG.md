# Preregistration: selected ordered measurement law

PUBLIC; NON-CANONICAL; P-QDD-SELECTED-MEASUREMENT-LAW-1.
Owner: A. M. Thorn / selected-theory session 2026-09-20.
Lock: https://github.com/mathorn1973/twist-j/issues/1093.
Base: 822ae98c63545d9e800b4d145c0eec8c7bca29a6; Public Canon v90 ACTIVE.
The author authorizes the connected GitHub contributor identity and the
explicit theoretical choice program. This is not a blinded model selection.

## 1. Equation and claim

Freeze ETH-QDD-1 in MODEL.md. Its source is C^4 with G=I-11^T/5,
R the displayed multiplication-by-j matrix, P_0=11^T/4 and
P_k=R^k P_0 R^-k, Q_k=I-P_k for k=0,...,4. The instrument components
are I_(k,L)(X)=P_k X P_k and I_(k,H)(X)=Q_k X Q_k.

Their selection uses the declared sharp effects, ordinary repeatability,
complete positivity and the inherited three-attenuation condition on the
rank-three branch. Born occurrence, source adoption, record persistence,
context controls and replacement preparation are explicit chosen inputs.
The conditional target is a complete normalized ordered history law,
including post-states, zero handling, adaptive settings and resource bounds:

    rho_h=I_(k_N(h_<N),o_N) ... I_(k_1,o_1)(rho_0),
    Pr(h)=tr(rho_h).

No claim that these probabilities or controls are derived from J or U is
permitted. The native comparison is restricted to the Galois code, whose
free pushforward is isometric; global U unitarity is not assumed.

## 2. Code, carrier and immutable inputs

The new verifier uses only Python standard-library Fraction arithmetic.
It reads no runtime Canon or predecessor code and no experimental data.
All 16 rational operator matrix units are audited where full linear-map
equality is claimed; complex-linear extension is proved in PROOF.md.
The representative positive-state checks are not a complete census of
all physical densities. Universal and all-time conclusions rest on proofs.

Before first scientific execution freeze and publicly read back:

    probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/PREREG.md
    probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/MODEL.md
    probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/PROOF.md
    probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/REVIEW.md
    probes/P-QDD-SELECTED-MEASUREMENT-LAW-1/verify.py
    notes/canon/SELECTED-THEORY-PROGRAM-2026-09-20.md
    notes/canon/SELECTED-MEASUREMENT-FOLD-PROPOSAL.md

Only static syntax checks and written analysis are permitted before pin.
An independent agent reviews the written arguments before reading verify.py.
There is no claim that the already exposed candidate is a blind discovery.

## 3. Frozen audit gates

G1. Exact metric, inverse, sharp-adjoint identities, R^5=I, all five
G-orthogonal projector pairs, sum_k P_k=5I/4 and
tr(P_k P_l)=1 for k=l and 1/16 otherwise.

G2. The specified Kraus maps have their declared effects, their sum is
trace-preserving, and same-setting branch repeatability and opposite-branch
zero hold on all 16 operator units for every context. Check both effect
and channel equations; no claim that a matrix-unit input is a density.

G3. For every context, the explicit 12-dimensional controlled pointer
V_k=P_k tensor S_L+Q_k tensor S_H is unitary in G tensor I3. For every
source operator unit its BLANK-input outcome blocks give exactly the
registered instruments. The pointer input is independently BLANK; dirty
pointer equivalence to the older five-state writer is not claimed.

G4. Recheck the inherited H,A,B_t attenuation certificate: three rank-one
differences, the three-vector independence/nonorthogonality, commutant
rank eight, and the rational two-pass channel which fixes B1,B2 but not
B3. Preserve the depolarizing nonselection witness. This audit does not
claim a new discovery of the inherited three-pass theorem.

G5. For all 125 context triples, all eight outcome words and the six
states P0,P2,I/4,rho(e0),rho(e0-e1),rho(e0+e1), audit the 6000 ordered
branch laws, normalization and prefix consistency. Also audit the
depth-four causal policy k(h)=(len(h)+sum_(i=0)^(len(h)-1)(i+1) bit(h_i))
mod5, with bit(LOW)=0, bit(HIGH)=1, on the same six states. Zero branches
must never be normalized. This finite family audits, not replaces, the
general causal-policy proof.

G6. For each context and registered state, same-context repetitions of
lengths 1 through 5 have only the all-LOW and all-HIGH supported words.
Full replacement before each new trial gives the product law at fixed
preparation and settings. Verify joint reset on an explicit correlated
reference witness, its unchanged reference marginal and removed correlation.
Resetting only a pointer is not source renewal. Adaptive settings retain
their explicit dependence on the recorded past.

G7. Preserve the prospective exact diagnostic: initial rho=P0, followed
by settings 1 and 0, has Pr(LOW,LOW)=1/256 and
Pr(HIGH,LOW)=225/256, hence final LOW probability 113/128 when the
intermediate label is ignored, versus one without that intermediate
measurement. Check typed ZERO_SUPPORT and zero branch handling.

G8. Frozen negative controls: omit an outcome and lose normalization;
use an incorrect setting conjugation and fail the registered map;
replace coarse HIGH recording by a fine record and lose HIGH coherence;
reset only the pointer and fail fresh-source independence. A failed
alternative is a boundary witness, not a refutation of the chosen model.

Print deterministic G1-G8 result lines and the exact verdict
SELECTED-MEASUREMENT-LAW with an explicit conditional-theorem caveat.
Save first completed stdout byte for byte as EXPECTED.txt.

## 4. Systematics and failure threshold

One admitted exact counterexample refutes the corresponding registered
mathematical identity. A written-proof gap blocks theorem-grade acceptance
even if the finite verifier passes. Confusing covariance and density,
omitting source/reference correlations, hiding an environment reset,
normalizing a zero branch, claiming iid without fresh preparation or
identifying R with native U are scientific scope failures.

No mathematical target, choice, program, threshold or frozen file may
change after pin. Runtime failure or incomplete first gate consumes the
identifier and requires ABANDONED disposition under POLICY. A pin/readback
or architecture-byte mismatch is STOP, not permission to repair the pin.

This theoretical probe contains no acquired experimental data, physical
uncertainty fit, random trials, laboratory access, device waveform or
empirical occurrence test. Its positivity claims are exact mathematical
ones in the declared model. Numerical hardware tolerances and future
statistical rejection rules require a separately frozen empirical task.

## 5. Action layers, choice and disposition

The scientific payload consists of conditional finite-dimensional operator
and history theorems, plus the explicit owner-selected model. Model roles
are L1 source data, L4 support/channels, L5 ordered record and L6 occurrence
measure. The prospective bridges are separately named:

    GATE-L1-L4-SELECTED-QDD-SOURCE
    GATE-L4-L5-SELECTED-QDD-RECORD
    GATE-L5-L6-SELECTED-QDD-BORN

No formal mathematical identity is represented as passing a physical
cross-layer gate. A future fold must register the dictionary choices and
their dependencies explicitly, separately from conditional T statements
and physical-adequacy hypotheses. The selected Born law is an adopted
statistical input, not a generated random source or a native reduction.

After the first completed local exact-pin run add EXPECTED.txt, RUN.md,
RESULT.md and, after the public checks, ACCEPTANCE.md. Require byte-identical
verifier/output on x86_64 and aarch64, aggregate check and final-head/main
readback. Preserve the pin in a merge commit.

The existing QDD apparatus, terminal and class-completeness owners keep
their registered broader obligations. #539 and the read-only decoder
architecture remain unchanged. No alteration of canon/, STATUS, release,
or empirical authority is included in this probe. The notes propose the
next coherent Canon transaction; they do not perform it.
