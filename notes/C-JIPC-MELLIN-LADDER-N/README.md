# C-JIPC-MELLIN-LADDER-N — Mellin ladder drafts (WP3D-QPOS, WP3F)

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
