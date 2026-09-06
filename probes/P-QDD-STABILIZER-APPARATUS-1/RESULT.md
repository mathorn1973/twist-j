# P-QDD-STABILIZER-APPARATUS-1 result

Status: PROVED AND LOCALLY AUDITED IN THE FROZEN CLASS / CANON UNCHANGED.

The first formal run followed public issue 854 and immutable pin
`515bdf33f04bd43cbe5e48e0522d844fd6135f37`, including public byte readback of
all seven accepted files. It returned eight PASS gates, exit zero and empty
stderr. EXPECTED.txt contains the exact 292-byte, nine-line stdout. No pinned
file changed. Independent x86_64/aarch64 replays are required by the PR workflow.

## Mathematical decision

The exact circuit and independent system-map audit agree at the preregistered
scope:

- The direct 40-mode rational split/controlled-permutation/recombination
  circuit is orthogonal and preserves the 32-dimensional zero-cell-sum carrier.
  The production builder contains no P/Q gate.
- Recording only the binary path flag and coherently undoing the path
  interaction returns all auxiliary paths to zero and induces precisely
  `rho -> P rho P` and `rho -> Q rho Q` on prepared system inputs.
- Retaining the fine paths instead induces LOW `P rho P` and HIGH
  `T_k(rho)-P rho P`, a generally mixed idempotent map. It has the same first
  weights as coherent uncompute and a different complete post-state map.
- These two coarse maps are invariant throughout the stated class of balanced
  rational orthogonal mixers and permutations of the four stabilizer powers.
  Fine path amplitudes are not identified. The class is not all physical apparatuses.
- Every ordered pair of settings and E/R variants, all four binary branch
  histories and the complete sixteen-element operator basis agree with the
  independent reference. The analytic discriminators give `0` versus `5/16`
  and joint `225/256` versus `75/256` in their frozen preparations.
- A single default setting has an invariant full-rank lattice. Two distinct
  default settings on the same common carrier have none: their product contains
  the irreducible reflection-plane factor `lambda^2+(7/4)lambda+1` with roots
  that are not algebraic integers. Variable-denominator arithmetic does not
  turn this into a common fixed-lattice dynamics.
- The selected terminal account preserves complete signed storage, all
  lifetime ordinals and energy through append, reread, END and archival
  counter reset. The old store survives reset; new pulses carry explicit
  new energy. Periodicity and the two-half-quantum control remain exact.

The universal statements rely on the direct proofs in PROOF.md and the
induction in RECORD-CONTRACT.md. The finite audit verifies their matrix
identities and fixed controls; it is not an enumeration of O(3,Q), all
possible histories or physical apparatuses.

## Falsifiers and remaining boundary

No preregistered mathematical falsifier fired in this run. The common-lattice
impossibility is an intended proved negative conclusion, not a runtime failure
and not a falsification of all larger architectures or of TWIST-J.

The chosen coherent uncompute architecture supplies a concrete realization
of the conditional projection maps. It does not establish why Nature chooses
this architecture. Both flagged components remain in the linear output;
there is no occurrence rule for one exclusive photon outcome. The terminal
threshold model may emit zero, one or multiple marks and is not a physical
event-completion principle. Its archival reset is not a reset of the old
decoder wave or a discharge of #539.

The beta source-label comparison is a fixed mathematical transport, not an
accepted L1-to-L4 physical gate. Carrier realization, preparation, physical
scale, phase ownership, detector law, complete physical family and all
L1-to-L5/L6 obligations remain unresolved. No QDD parent or child O is closed.

## Public disposition

This one-probe PR supplies the proof, exact verifier, full pin custody and
local record for independent replay and review. It changes no Canon, registry,
frontier, workflow or existing scientific pin. The maximum later fold is the
proved conditional circuit/post-state result and its fixed-carrier lattice
boundary, together with the supporting selected account at this scope.
No new scientific status is earned merely by creating the reservation or PR.
