# Finite-chain first delivery: result and local validation

NON-CANONICAL / candidate-T by conditional proof / L1. Local analytical
follow-up, not a public formal probe or Canon promotion. Public authority
remains v95. Date: 2026-10-01.

## Result

The known candidate induction supplied by the user is valid under the exact
four-layer law of PR #1310, pinned at
`dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2`. Two separate read-only audits of
the inherited definitions found no counterexample, indexing error or omitted
full-state condition. [PROOF.md](PROOF.md) makes the complete argument explicit:

- For every integer N>=2 and every integer w with H(w)=1, the first target
  boundary delivery is N-1 and the first target reaction is step N.
- The displayed formula specifies all 32N-1 stored coordinates through
  boundary N. Initial total energy is41, independent of N; the stored
  architecture grows with N.
- For each of the N-1 single-channel cuts, both contacts are replaced by
  identity and the cut channel remains stored. The complete downstream
  prepared component is fixed for all future steps.
- Every fixed finite-N law retains the inherited inverse, conservation,
  fixed four-layer depth, radius-two contact support and finite-shell
  recurrence. The proof does not establish a common period.

The N=2 case uses #1310's reaction-before-contact schedule: arrival1,
reaction2. It does not reuse the target-after-contact schedule of #1308.
Repeating the source field phase after five steps never funds its reverse:
its active energy stays1 and its resource stays0 through the first reaction.

The target activation is temporary. Its zero-field AM state releases two
units at the next G layer; at boundary N+1 the target has returned to R and
the last channel stores those units. This analytical continuation is included
to delimit first work, not to add a permanent-record claim. There is no charge
transport, infinite-chain construction, physical light-speed identification,
or selection of this architectural law by J.

## Actual local audit

[SCOPE.md](SCOPE.md) and the four input hashes in [SHA256SUMS](SHA256SUMS)
were written before execution. No input changed during execution; hashes
were checked before and after. This is a local content freeze, not a public
preregistration commit. The mathematical target was already exposed.

The two generic-N adapters reuse the separately authored, hash-guarded local
arithmetic from the predecessor. Their network evolution is new and genuinely
parameterized; the old three-cell runners are not invoked. Full coordinate
equality is compared against a separately written closed-form oracle, rather
than only checking a resource trace or several longer examples. Source reuse
is disclosed; no fresh clean-room independence is claimed.

The complete H=1 seed set is checked using the proved containing box in
SCOPE.md. A separate static reviewer derived 20 seeds before the first run;
the program found20. The proof for arbitrary w and N does not depend on
either count. Connected lengths are2 through16,31,32,33,64. Cut lengths are2
through16 and32, with every individual cut and boundaries0 throughN+2.
Occupied contact tests use every N from2 through64, including every cut.

From the root of this checkout:

```text
python -B notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/audit.py
```

Actual environment and receipt:

| Item | Value |
| --- | --- |
| Platform | Windows11 |
| Architecture | AMD64 (x86_64) |
| Python | CPython3.12.10 |
| Duration | 18.219 seconds |
| Exit code | 0 |
| stderr | 0 bytes |
| stdout | 561 bytes, seven CRLF-terminated lines |
| stdout SHA-256 | `8c68fec8078aa5fc19747f824325004a50d2621f058f3379fea2bb358cd9eafd` |
| Source hashes before/after | identical |

The captured stdout, rendered below with ordinary Markdown line endings:

```text
LOCAL AUDIT PASS: NON-CANONICAL candidate-T L1; no public computation gate
H=1 seeds: 20; connected lengths: 19; full boundaries: 6280
single-cut cases: 151; cut boundaries: 2805; occupied contact cases: 2079
first boundary arrival=N-1; first target reaction=N; energy=41; coordinates=32N-1
two generic full-state adapters agree; layer invariants and both inverse identities pass
connected full-state SHA-256: 8f12d371b479257b992c78ea97d8c70a816d521aca05e0d31b14966f7a03ad36
All-N and all-time cut conclusions rest on the proof, not these finite checks.
```

The full-state digest hashes the ASCII repr of each (N,w,k,full_state) tuple
with a literal LF separator, in the deterministic audit loop order. It is
independent of the platform's stdout newline translation. No byte-identical
second-architecture output is asserted.

Every checked layer preserves total energy, actual node charges, pointwise
Gauss defects, all spectators and each cell's reacting-vector sum. It is
not asserted that each individual reacting-register charge is conserved.
Both inverse identities are checked separately in both representations.
Distinct occupied resource values and symbolic labels detect overwritten
contents. Multi-digit indices are numerical throughout; the predecessor's
fixed-three-cell label parser is not generalized or used.

## Review and repository state

Static Python parsing passed before execution. Independent mathematical
review covered contact equations, N=2, arbitrary field phases, all cuts,
complete energy and all stored coordinates. A separate code review checked
the H=1 box, closed oracle, account shapes, four layers, inverse checks and
the declared counts before execution. No scientific mismatch occurred.

Repository checks passed: policy, Canon (v95,484 claims), ledger and gate
contract. The initial gate-check invocation used the nonexistent filename
`tools/check_gates.py`; it ran no check. The correct existing
`tools/check_gate_contract.py` was then run successfully, with25 gates.

Only this new notes directory is added on local branch
`codex/field-finite-chain-first-delivery-n`, based on the exact #1310 head.
No predecessor, Canon, registry, public branch, workflow or reproduction
record is changed. There is no new commit, public issue, push, PR or new
x86_64/aarch64 public gate for this follow-up. The predecessor's public
architecture receipts support its own frozen scope only. Any formal public
continuation must reserve and pin its own lane before formal execution.
