# Nonlinear origin-zero native receiver

PUBLIC / NON-CANONICAL / L1. Original work Apache-2.0, A. M. Thorn.
Owner issue #1532. This result-exposed candidate changes only the fixed
coordinate reading of the original six-coordinate U, not its dynamics.

The candidate is a two-coordinate receiver and four-coordinate complement
with a global inverse. Twenty-five independently labelled initial source
pairs have one common receiver. The first three actual native steps should
read BLANK, first message, BLANK, second message; the second persists by a
closed invariant. The complete checkpoint returns at n=2, not the counter.

PROOF.md gives the exact map, inverse, invariant, all-time argument and
source-access boundary. PREREG.md freezes equations, coverage and failures.
verify.py contains no copied verifier import or data lookup for outputs.
SOURCES.tsv binds the exact primary definitions and neighboring boundaries.
INPUTS.sha256 binds the five other initial files before the first run.

After the published pin/readback, run from repository root:

    python3 probes/P-U-NONLINEAR-ORIGIN-RECEIVER-1/verify.py

No execution result is asserted by this pre-execution README. A later
RESULT.md and RUN.md record the actual outcome. Scientific false targets
are preserved even when a deterministic FAIL report exits zero.

The mathematical comparison class permits nonlinear re-coordination. It is
not a physical selection rule or a license to read the old raw source port.
In fact (q,r) remains common across every message. Both labels were present
initially; no new message is injected later, no source is emptied, no energy
law or repeatable late-start procedure is asserted. All older affine and
synchronized negative results remain at their original scopes.
