# Acceptance of the completed decoder/contact evidence

NON-CANONICAL evidence acceptance, 2026-10-04. The three preceding pull
requests were merged under the author's request after the exact-head
security/custody review in PRIOR-EVIDENCE-REVIEW.md and successful required
checks. All merges preserve history and the original pre-execution pins.

| PR | Accepted head | Merge commit | Final required workflow |
| --- | --- | --- | --- |
| #1350 | `32c8ffe2fa4d08f2b74b6af5d1f42fe68382c0b8` | `582038e210e769dacb7424159b47f3481050e746` | [37161612071](https://github.com/mathorn1973/twist-j/actions/runs/37161612071) |
| #1351 | `9caf18aa12de20e1b595708d9774e78709da6e62` | `77ed73639adcd9428051f2b109f9efb0e0c81a87` | [37164734824](https://github.com/mathorn1973/twist-j/actions/runs/37164734824) |
| #1352 | `7a505c5cb8d776171f267048d677c97136cb5413` | `540b5cee02bb09a899a00cfbd723e26552210273` | [37164840986](https://github.com/mathorn1973/twist-j/actions/runs/37164840986) |

Each listed workflow completed x86_64, aarch64 and the aggregate `check`
successfully before its merge. The publication job is intentionally skipped
for pull requests. The heads were guarded by exact expected-SHA merge calls.

After #1350 moved main, GitHub classified the remaining heads as behind.
Accepted main was merged into #1351, preserving every byte of its own probe
and authority context, and its required jobs passed again. The successive
accepted main commits were then merged into #1352; every byte of its own
probe and authority context likewise remained unchanged and its jobs passed
again. These were ordinary merge commits, without rebasing or amending a pin.
They added no new mathematical scope, changed verifier or fresh exploratory
run. The earlier static review remains applicable by exact file identity.

The final evidence-only main is
`540b5cee02bb09a899a00cfbd723e26552210273`. Its Canon and authority files
are unchanged from the earlier main `5e872c22a18043c8126945a982efad55472cea82`.
Public Canon v97 remains authoritative, with 897762 Canon bytes and SHA-256
`257f83a386aad7d309f7017bd719b6212e3cffea60e4986caa5169d6543f108d`.
The resulting main push workflow
[37164954816](https://github.com/mathorn1973/twist-j/actions/runs/37164954816)
also completed successfully.

The decoder and early native-contact results remain candidate-T outside
Canon. The abandoned ID1 remains ABANDONED and its identifier consumed; its
byte-custody defect before scientific execution is not a mathematical
falsification. The historical absence of a documented pre-commit public
issue reservation remains disclosed in PRIOR-EVIDENCE-REVIEW.md. Present
acceptance does not rewrite that chronology or represent full historical
administrative compliance. New issue #1353 was reserved prospectively.

The separate proposal under notes/canon prepares a later declared fold. No
Canon promotion, release or tag is performed by this acceptance or this note.
