# Public acceptance of the selected measurement law

PUBLIC; NON-CANONICAL; P-QDD-SELECTED-MEASUREMENT-LAW-1.

The exact audit and independent written review support the conditional
candidate-T conclusions of RESULT.md. Both public architectures reproduce
the one committed output. This accepts the probe at its declared scope;
it does not activate a Canon release or establish physical adequacy.

## Immutable result-stage evidence

- Public lock: [#1093](https://github.com/mathorn1973/twist-j/issues/1093).
- Pull request: [#1094](https://github.com/mathorn1973/twist-j/pull/1094).
- Public preregistration pin: `f1a25f6a51cf167094eb95b8a37a5cb7e8dcc368`.
- Accepted result head: `de63fda8ded9bc7e17cf372f64b29d40e6a3f8e4`.
- Accepted result tree: `578f0940d8fc7b021a31d82d8dd41857465920e7`.
- Public workflow: [35528620831](https://github.com/mathorn1973/twist-j/actions/runs/35528620831).

| Job | Conclusion | Evidence |
| --- | --- | --- |
| architecture-x86_64 | success | [106125101483](https://github.com/mathorn1973/twist-j/actions/runs/35528620831/job/106125101483) |
| architecture-aarch64 | success | [106125101673](https://github.com/mathorn1973/twist-j/actions/runs/35528620831/job/106125101673) |
| aggregate check | success | [106125164407](https://github.com/mathorn1973/twist-j/actions/runs/35528620831/job/106125164407) |

Both architecture logs were read back and contain the exact verification
line binding these two hashes:

```text
verifier_sha256: cf6b9ca76a9d0914ce9af181e3d173e1b6f55adab2319673c55608c20ace31e2
stdout_sha256: 92c8c4e8f8e0dcf463c2e274a746fd2e279b829df8b0c86818466165c99cc641
stdout_bytes: 702
stdout_lines: 9
```

The existing verifier runner requires exit zero, empty stderr and exact
stdout identity with EXPECTED.txt. Both jobs use Python 3.12.14 and also
pass policy, all 172 tool tests, Canon v90 with 437 claims, ledger and gate
contracts. No workflow, parser or acceptance threshold was changed.

This record binds the result head above. Its own addition is a neutral
descendant requiring the same public checks before merge. The pull-request
record carries the final-head and merged-main readbacks, avoiding a
self-referential claim that this file already contains its own commit hash.

## Review and unchanged scientific input

REVIEW.md records independent written review before execution without
reading the new verifier. A separate post-run review approved RESULT.md,
RUN.md and EXPECTED.txt, independently checked all seven frozen input
hashes and byte counts, and found no scope or metadata inconsistency.

The complete seven-file pin inventory is in RUN.md. PREREG.md, MODEL.md,
PROOF.md, REVIEW.md, verify.py and both selected-theory notes remain byte
identical to that public pin. EXPECTED.txt is the actual first completed
stdout, unchanged. The verifier reads no mutable runtime Canon context.

The first public workflow
[35528548843](https://github.com/mathorn1973/twist-j/actions/runs/35528548843)
stopped in the tool tests before scientific replay because the new RUN.md
used human-readable bullets instead of the existing parser's field names.
The append-only correction at the accepted result head changed only RUN.md
presentation and supplied the derived nine-line count. It changed neither
the completed run nor a frozen input, result, threshold or output. The
original first scientific execution had completed successfully, so this
metadata correction is not an abandoned scientific pin.

## Scientific disposition

The selected assumptions imply the declared coarse instruments, exact
ordered history law, zero handling, finite record and reset accounting,
and restricted free-code transport. Universal claims rest on the written
proof; the finite rational audit does not replace it. The Born occurrence
law and the other seven CH inputs remain adopted physical assumptions.
The 113/128 interference diagnostic is a mathematical consequence of the
chosen theory, not an empirical result or blinded discovery.

The broader apparatus, terminal-event and class-completeness owners retain
their scopes. No feeds_U=false contract or physical cross-layer gate is
reported passed. Public Canon remains v90; canon/, STATUS and release
authority are unchanged. The two notes propose a later, separately sealed
fold distinguishing conditional theorems, selected dictionaries and
physical-adequacy hypotheses.
