# C-JIPC-MELLIN-LADDER-N — Mellin ladder drafts (WP3D-QPOS, WP3F, WP3G)

Status: NOTES LANE / NON-CANONICAL / UNREGISTERED. No claim, no pin,
no run. Nothing here changes the Canon, the registry, or any gate.

Governance disposition after public review:

```text
NOTES_LANE_MERGE        = PASS
WP3D_PUBLIC_FREEZE      = BLOCKED_AS_WRITTEN
WP3F_REGIME             = A_SELECTED
WP3F_PRIVATE_ROUTE_B    = CLOSED
WP3F_PUBLIC_PIN         = BLOCKED
```

Two working drafts on the JIPC Mellin ladder, deposited after the
Public Canon v65 activation and the merge of
`P-JIPC-WP3E-EFFECTIVE-MELLIN-SEEDS-1` (PR #569, merge commit
`9a4b479b0a7a9ce39772f77f16dd363602ec72c7`), then audit-amended
before the notes-lane merge:

- `WP3D_QPOS_MELLIN_PROOF_CONTRACT_DRAFT_v3.md` — the mathematical
  core of the rational-slice Mellin contract is retained as discovery
  context, with the compact-domain witnesses, residual detectors and
  dependency DAG repaired. Public freeze remains blocked: a public
  WP3D probe must be self-contained, may not use the private WP3C/WP2
  lineage as a premise, and needs its own public claim, pin, verifier,
  fixtures, run, two-architecture confirmation and merge.
- `WP3F_EOC_HOLOMORPHIC_PREREG_DRAFT_v2.md` — public route A is
  selected and private route B is closed. The route combines public
  WP3E, a future public WP3D, a typed disk identity interface and a
  positive-root interface, with two explicit proposed TCB additions:
  `IT-SEGMENT` and `POW-EXPLOG-ID`. The audit amendment corrects
  the segment typing, extends `A(x)` to real interval arguments,
  records the `N4 -> N5` dependency, removes the unproved
  `SHRINK` step and separates scientific `FIRED` from integrity
  `STOP`. Its §6 public prerequisites remain unmet, so no WP3F pin
  or run is authorized.

Provenance: drafted 2026-08-26 with multi-agent adversarial review;
the public-review disposition and repairs are recorded in these
audit-amended v3/v2 notes. These files are discovery context in the
sense of the probe discipline: they are not evidence, not a premise,
and not an instruction for any probe.

## Public probe draft deposit (route A, step 1)

Added after the governance review above, as preparation for the
selected public route A:

- `WP3D_QPOS_PUBLIC_PREREG_DRAFT_v1.md` — a self-contained draft
  preregistration for the future public probe
  `P-JIPC-WP3D-QPOS-MELLIN-1` (identifier NOT claimed). The bridge
  is public: `C(1/2)^2 = p_I` via the Beta-midpoint route inside the
  primary graph, with the public Machin bridge `p_I = p_M` consuming
  only the merged WP3E name (well-definedness of `A_q` re-proven
  internally). All freeze blockers FZ1-FZ6 are resolved with
  concrete values; full written proofs Q1-Q8 are carried in the
  draft itself; FIRED is separated from STOP with the WP3E exit
  contract and a BOUNDED-AUDIT-C fallback.
- `wp3d_qpos_public_verify_draft.py` — the matching draft verifier:
  exact `Fraction`-only audit (ring `Q[g,g^-1]`, `p_hat = g^2`;
  lattice `N_input=6`, `N_value=12`, EOC on `s in {1,2,3}`; modulus,
  Machin, form-identity and residual gates; 23 negative controls
  wired to the same guards the PASS path consumes). Static audit
  only: `py_compile` plus an AST scan (zero `ast.Div`, zero float
  literals, single import). **Never executed** — `DEV_EXECUTION =
  NONE`; the first run is the formal run after claim lock and pin.

Both files are notes-lane drafts: no claim, no pin, no run, no
gate change. Claim lock, move to `probes/`, pin, and the formal run
are maintainer steps.

## Route A package (2026-09-01, Public Canon v74)

Deposited after the Canon moved from v65 to v74 while the drafts sat
unpinned; every file below is NOTES LANE / NON-CANONICAL and claims
nothing.

- `WP3D_QPOS_PUBLIC_PREREG_DRAFT_v1.md` — basis tuple refrozen to v74
  (repin record kept); reading-family discipline stated as
  NOT_APPLICABLE with the two mathematical uniqueness classes named;
  verifier hygiene, transcript rule, preflight, attempt ref and
  neutral run metadata added (FZ7, FZ8; seven-step formal order).
- `CLAIM_LOCK_DRAFT_P-JIPC-WP3D-QPOS-MELLIN-1.md` — the prepared
  claim-lock issue text in the current house form (authority
  readback, disposition, collision scan, lock block, frozen scope,
  integrity requirements, firewalls, decision rule, formal order).
  **Not posted**; posting is a maintainer act after a fresh readback.
- `WP3F_EOC_HOLOMORPHIC_PREREG_DRAFT_v3.md` — supersedes v2: one
  lifting lemma `LIFT_QPOS_TO_D` applied to five identities in
  dressed currency (`EOC-D`; `REC-D: Chat(s+1) = s Chat(s)/(2 p_M)`;
  `DUP-D: Chat(s) Chat(s+1/2) = 2^(3/2-2s) Chat(2s)`;
  `EPULL-D: Ehat(s) = 2^(s/2-1) Chat(s/2)`; `JOIN-D: Ohat(s) =
  Ehat(s+1)`), WP3D as a public merged-probe parent (Machin bridge
  cited, not re-proven), a frozen half-integer table of `Chat(k/2)`
  in the replay ring, uniqueness classes in the reading-family
  vocabulary, and the current verifier obligations. v2 is kept as
  history.
- `WP3G_CONTINUATION_PREREG_DRAFT_v1.md` — skeleton of the successor:
  recurrent meromorphic continuation of `Chat, Ehat, Ohat` via
  `REC-D`, poles and residues `Res_(s=-k) Chat = 2 (2 p_M)^k (-1)^k / k!`,
  and the three identities as global meromorphic identities by the
  identity theorem — no Fourier needed; the functional equation is
  explicitly out of scope (it would first require identifying the
  period of `exp_C` with `2 p_M`, a separate future probe).

State of the queue at this deposit: PR #572 carries the v72 version
of the WP3D draft; this branch carries the v74 refreeze and the route-A
package and supersedes #572 (one notes-lane PR should remain).
Ladder order: merge the v74 notes-lane PR -> claim lock -> pin ->
formal run -> merge WP3D -> WP3F claim lock -> ... -> WP3G.
