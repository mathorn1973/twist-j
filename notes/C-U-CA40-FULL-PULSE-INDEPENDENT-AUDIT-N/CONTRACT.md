# Offline audit contract

**PUBLIC / NON-CANONICAL / L1. Design fixed before audit execution.**
Reservation: [#1473](https://github.com/mathorn1973/twist-j/issues/1473).

## 1. Scientific and execution boundary

The reviewed source is the immutable commit
`bca348445715c03f4cdc3af6079207024dd40332`, not the changing head of a branch.
The coordinator must commit, push and publicly read back this note's complete
source set before executing `verify.py` or `audit_saved.py`. Static source
review, parsing and syntax checks may precede that pin. No live numerical
outputs are read in this preparation lane.

The auditor operates on a stable, closed offline copy. Its required
`summary.json` must record the original scope, ended time, at most one attempted
and launched child, no retry/resume, and either a complete outcome or
`NOT_CERTIFIED`. A complete outcome requires exactly one attempted and launched
child; an incomplete attempt can fail before launch. The auditor does not infer
closure from a progress percentage.
The auditor does not invoke, import, emulate or resume the propagator.

## 2. Fixed model and layout

The production CLI has a fixed contract: six cases, 120 initial thermal
columns, seven modes, L8 dimension 6435, guard G10, 80 original segments,
384 cells per occupied segment, batches of eight columns, and final time
1/2000 second. Labels in each angle are (4,3), (4,4), (1,1). Segment activity
is recomputed from the labels and the segment's five-loop index.

Each committed checkpoint has a JSON marker and an 824448-byte binary payload:
eight lane-major complex endpoint vectors (823680 bytes), then twelve
lane-major binary64 fields (768 bytes). State data are little-endian IEEE
binary64. Checkpoint markers identify boundary, rational time, cell count,
active count, CPU/place and field order. The sequence must start at zero and
contain no holes. A markerless binary or temporary file remains uncommitted
evidence; it is never a successful checkpoint.

For a complete outcome there must be 90 complete tasks, 7290 snapshots, 5280
inactive byte-identical carries, final endpoint/component files with exact
declared sizes, and byte equality with every terminal snapshot. The initial
payload is checked against the exact declared Fock basis state, not merely
its norm. The full basis must equal the independently generated graded,
ascending-first-coordinate seven-mode compositions through total occupation 8.

## 3. Checks and exact arithmetic

All copied state artifacts are rehashed against the saved inventory; paths
must remain inside the offline directory, contain no symlinks and have no
unsafe or duplicate inventory keys. Duplicate JSON keys and nonfinite
numbers are rejected. The complete inventory must match the actual tree.
Incomplete inventory is reported as unauthenticated partial evidence and
cannot earn a saved-account audit PASS.

Every component row must have nonnegative finite entries, ordered norm
endpoints, and the exact required binary64 upward-sum total. Ten cumulative
fields must not decrease between committed boundaries. Inactive boundaries
must preserve all payload bytes. Terminal endpoint squared norms are
recomputed exactly from their IEEE bit patterns and checked against the
reported interval. Optional all-snapshot norm checks strengthen this scope.
Default hashing alone is not a norm/finite-value re-audit of every active
intermediate endpoint.

Exact initial thermal weights are (20/21)^7(1/21)^N without renormalization;
their missing mass is 680046581/794280046581. Reported weighted error,
component RMS and endpoint-norm upper bounds are checked by exact squared
inequalities. The pair Gram minimum, thermal allowance, rectangle-magnitude
enclosure, arithmetic halfwidth, outward clipped final interval and strict
1/1000 decisions are independently checked with rational arithmetic. No
comparison tolerance, phase fit or state normalization is introduced.

The final JSON/raw component correspondence, original lifecycle/progress
inventories, source-hash declarations and complete worker/task coverage are
checked separately. Source hashes are compared with the reviewed pin's fixed
manifest values. A copied binary can additionally be checked with `--binary`;
without it its recorded hash is a declaration, not a rehashed executable.

## 4. Outcomes and failure semantics

`SAVED_FULL_ACCOUNT_AUDIT_PASS` means these saved-data consistency and exact
aggregation checks passed for a recorded complete campaign. Precision and
nonlinear discrepancy are reported separately, even on a wide valid account.
It does not mean independently validated node enclosures or numerical replay.

With `--allow-incomplete`, `SAVED_COMMITTED_PREFIX_AUDIT_PASS` requires internally
consistent nonempty committed prefixes, complete copied inventory, valid model/basis
metadata, available lifecycle/progress prefixes linked to committed payloads,
and a matching available final custody declaration. Lifecycle phases must be
an ordered prefix. Every logged checkpoint must exist and its saved error
maximum must match; at most the newest committed boundary per task may lack
its subsequently written log row. It carries no final precision or discrepancy
conclusion. Missing prelaunch/setup state directory, metadata or either log,
no committed checkpoint, an incomplete inventory,
missing custody, or an unterminated final log line yields
`PARTIAL_EVIDENCE_ONLY`, never either PASS. Corrupt committed JSON or misordered
available log records are rejected, even in incomplete mode. Existing members
of a partial metadata set are still parsed and validated; missing peers do not
permit corrupt available evidence. Summary and inventory completeness flags
must match as JSON booleans. Integer identities/counters and numeric components
reject boolean impersonation. A truncated last
line is retained in the input but is not accepted as a log record.
Any failed required check produces `SAVED_AUDIT_REJECTED`, exit 2 and a named
reason. The input evidence remains untouched. A missing/invalid conclusion
is never converted into a physical failure or an abandoned exact verifier.

## 5. What the saved data cannot establish

Boundary snapshots do not retain every cell's six quintic coefficients,
Gauss-node interval evaluations or internal stage states. They cannot
independently prove every cell's actual incoming polynomial, intermediate
arithmetic enclosure, defect integral, node placement or source continuity
between boundaries. Runtime assertions and source review remain distinct
evidence. Full independent reconstruction would require a separately
authorized deterministic replay, which this lane neither supplies nor runs.

Likewise this auditor verifies the algebra of the saved complex coherence
rectangles but does not recompute displacement/restoration intervals or the
MPFR force model from endpoint vectors. The exact dyadic endpoint norm check
does not close that gap. Hash agreement detects altered copied bytes relative
to receipts; it does not authenticate the original machine or execution.

No apparatus, all-input channel norm, all 25 active labels, complete motional
state, energy/work account, imperfect spectator protection or native physical
bridge follows. Unknown complete-source no-imprinting remains unchanged.
