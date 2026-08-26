# C-JIPC-MELLIN-LADDER-N — Mellin ladder drafts (WP3D-QPOS, WP3F)

Status: NOTES LANE / NON-CANONICAL / UNREGISTERED. No claim, no pin,
no run. Nothing here changes the Canon, the registry, or any gate.

Two working drafts on the JIPC Mellin ladder, deposited after the
Public Canon v65 activation and the merge of
`P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1` (PR #569, merge commit
`9a4b479b0a7a9ce39772f77f16dd363602ec72c7`):

- `WP3D_QPOS_MELLIN_PROOF_CONTRACT_DRAFT_v3.md` — rational-slice
  Mellin contract: seeds `C, B, E, O` on `Q_{>0}` with algorithmic
  tail moduli, the product identity `C(p)C(q) = C(p+q)B(p,q)`, the
  square-root-free duplication
  `C(p)C(p+1/2) = 2^(1-2p) C(1/2) C(2p)`, and the dressed slice
  `Ehat(s)Ohat(s) = Chat(s)` on `Q_{>0}`, typed to `pi_atan` via
  `C(1/2)^2 = pi_atan`. Two internal governance rounds applied
  (v1 -> v3); freeze (kernel, validator, fixtures) is pending and is
  a maintainer step.
- `WP3F_EOC_HOLOMORPHIC_PREREG_DRAFT_v2.md` — preregistration draft
  for `E(s)O(s) = C(s)` on `Re(s) > 0`: rational witness (WP3D-QPOS)
  + effective holomorphic names (WP3E) + one new TCB rule
  (identity theorem on disks), plus the `MACHIN_BRIDGE` node
  identifying the WP3E Machin name of `pi_atan` with the WP3B
  arctan-integral name. One internal red-team round applied
  (v1 -> v2). Pin conditions in its §6 are not met yet; the
  public-vs-internal regime decision (§0.0) is a maintainer step.

Provenance: drafted 2026-08-26 with multi-agent adversarial review;
review rounds and their repairs are summarized in each file's header.
These files are discovery context in the sense of the probe
discipline: they are not evidence, not a premise, and not an
instruction for any probe.
