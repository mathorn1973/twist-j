# P-ENTROPY-MACKEY-OBSTRUCTION pre-pin consolidation

```text
STATUS:        NON-CANONICAL PREPARATION BUNDLE
AUTHORITY:     NONE
PUBLIC CLAIM:  issue #241
FORMAL PIN:    NONE
FORMAL RUN:    NONE
PUBLIC EFFECT: NONE
```

This directory consolidates the five loose preparation artifacts that existed
across the main, entropy-probe, and target-predecessor worktrees.  The files
are retained byte for byte under explicit draft or provenance names.  Their original
SHA-256 values and byte counts are recorded in `SHA256SUMS` and below.

The bundle is RESULT-EXPOSED: expected values and predecessor outcomes were
known before any future public pin.  It is stored only as a temporary public
prep/archive ref on `codex/entropy-mackey-consolidation`, based on public
`main` commit `e2e05d080cbd4ee1ed97d47b760febd1cef4e4cf`.  It must not be
merged into `main`, and the formal probe must not be based on this branch.

Nothing in this directory is a public probe, accepted verifier, run record,
scientific result, or Canon input.  In particular, neither Python file may be
executed from this bundle.  A later formal probe must be rebuilt under
`probes/P-ENTROPY-MACKEY-OBSTRUCTION/`, reviewed again, committed and pushed as
its own immutable pin, and only then executed.

## Consolidated artifacts

| role and original surface | consolidated file | bytes | original SHA-256 | disposition |
| --- | --- | ---: | --- | --- |
| v28-to-v30 applicability audit; untracked `notes/canon/...` on `main@e2e05d0` | `provenance/APPLICABILITY_AUDIT_V28_V30.md` | 12495 | `6de06529ffe6bfeabd720d9bab996479074925baf711974efde4ea37e87cf956` | provenance only; never a pin input or evidence |
| source-side draft; untracked `notes/entropy_selection/...` on `main@e2e05d0` | `provenance/SOURCE_PREREG_PREDECESSOR.md` | 19366 | `f6d4fb7a061b7488efdfeabd9f7894957e8478a947be1fdf1037505c4ad5cc32` | superseded by the combined direction; do not revive |
| public preregistration draft; untracked formal-path candidate on `probe/P-ENTROPY-MACKEY-OBSTRUCTION@b8d4d58` | `PREREG_DRAFT.md` | 18165 | `c84c4b16bb538853b826014d6c72efa38c719ec1291755e466760d5f4afaaff9` | review source only; must be retyped and finalized on current main |
| combined verifier candidate; same untracked formal-path surface | `verify_draft.py` | 71794 | `b75fa653c89ecb58bf5ca725e1a7407df9a182c77e01486d4d4d5382203fa9dd` | never formally executed; harden and review before any adoption |
| target predecessor; untracked on `codex/mackey4-cocycle-prepin@258b40b` | `provenance/TARGET_BREAKER_PREDECESSOR.py` | 48471 | `c00a2897f6dc5038e0e08a4c22e310bae0e219206cf0200636dbf168584038e4` | four synthetic-only runs, zero evidence; provenance only |

The source-side draft and target predecessor have zero breaker credit.  The
combined public draft is the only live direction, through issue #241, but it
is not ready for a formal pin.

`MANIFEST.tsv` also pins three already tracked v28 predecessor documents by
public commit, path, hash, and byte count.  They are referenced, not copied;
the old 64-file entropy history is not imported.

## Required hardening before a formal pin

1. Start the formal probe branch from the then-current public `main` and repeat
   authority, collision, tag, hash, and required-check readback.  Public Canon
   v30 remains the scientific basis; this prep branch creates no authority.
2. Replace draft-only and mutable freeze-record wording with timeless formal
   preregistration text and record the exact current branch base.
3. Type the tested bundle explicitly, including the target carrier, target
   action, maps `p_kappa`, the factorization through `pi_5`, equivariance, and
   the common four-edge cocycle.  Define the narrow class as
   `A_Mackey subseteq A_A`; a positive obstruction may establish only
   `A_Mackey = empty`, never `A_A = empty`.
4. Treat `s_TM` only as the finite audit level of the dyadic Kronecker factor.
   The declared source is the full two-sided Thue-Morse system; the scientific
   conclusion must not present `s_TM` as a parameter of the map class.
5. Separate public-input reconstruction failures (`STOP_INPUT`), instrument or
   control failures (`STOP_INSTRUMENT`), and candidate-specific scientific
   falsifiers (`ROUTE_FALSIFIED`).
6. Preserve exact deterministic witnesses on every G3/G4 failure: the
   reference and first differing cocycle tuples for non-common data, and the
   observed common tuple for invariant-shape failures.
7. Describe the Haar/pushforward calculation as a conditional mathematical
   marginal audit.  It constructs no physical measure and earns no general L6
   statement.
8. Perform a fresh full static, adversarial, proof, and security review of the
   final two bytes before the pin.  Compilation or synthetic checks may occur
   only where the final preregistration permits them; no real claim carrier may
   be touched before the remote pin readback.

## Intended lifecycle

```text
issue #241
  -> current-main formal branch
  -> final PREREG.md + accepted verify.py pin
  -> remote byte/hash readback
  -> one formal local run
  -> EXPECTED.txt + RUN.md + RESULT.md
  -> one-probe pull request
  -> x86_64 + aarch64 gate
  -> merge commit
  -> optional later sealed registry/Canon fold
```

At every stage `ENTROPY-LAYER-BRIDGE` remains `O / STOP`.  The strongest
possible result of this instrument is at most `C` for the exact fixed-depth
`A_Mackey` subclass.
