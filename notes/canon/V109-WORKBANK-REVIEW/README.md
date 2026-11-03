# v109 workbank proposal: review disposition

NON-CANONICAL / L1. No Canon promotion, fold or release.
Current authority remains Public Canon v108 at
17de90b58f814238e151aac77badde6654b52627.

This note records the supplied review of
[PR1879](https://github.com/mathorn1973/twist-j/pull/1879), exact head
`d6a5f77169d1027a22959c41aa5a45a783643a3e`, and gives a concrete next-review
surface in CLAIMS.md. The frozen probe and its output are not changed.

A later separate computational and mathematical review is now available in
PR1882. [Its exact disposition](REVIEW_1882_DISPOSITION.md) records the new
evidence, the limited public-freeze chronology, all proof clarifications and
the forward-only retention correction. The earlier copier-author report
below remains a distinct historical input; it is not relabelled independent.

## Authorship and the supplied verdict

The supplied report describes a separate implementation of the workbank
program and reports agreement on all 1000 complete endpoints. It labels its
session a third independent session, but also refers to its own earlier
check in C-BANK-COPY-WORD-1. On clarification, the author confirmed that the
reviewing session also authored that original witness package.

Consequently this is an additional implementation check by the original
copier author, separate from the PR1879 implementation. It is NOT a third
independent mathematical review of the copier's existence proof. Code-path
diversity, architecture diversity and independence from authorship are
separate properties. The supplied files retain their original hashes; this
disposition corrects their attribution without rewriting them.

The report accepts PROOF sections 1-4 and 6-8 at candidate-theorem scope,
and treats the section 5 ten-input read identity as a finite exhaustive
computation. These are that supplied reviewer's judgments, not newly earned
Canonical statuses. They originally left the new proof scopes awaiting a
fresh reviewer; the later PR1882 assessment and its specific findings are
recorded separately in REVIEW_1882_DISPOSITION.md.

## Custody

The supplied files match these full byte identities:

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| REVIEW-PR1879-WORKBANK-REUSE_2026-11-03_CZ.md | 8588 | e1ecad03ec9f0bc10df157bf6cb954ab60cc9b2823c2729fe92e8fc51be11f27 |
| review_pr1879_workbank_2026-11-03.py | 21934 | 280f68424ada4a38b5d13fea0273358b3ce42d3f1775d054cbb44ec58c6a52f5 |
| review_pr1879_workbank_2026-11-03.stdout | 3035 | 3490582e48960afcbdd315ba5e3114558cabd3b8524af88555b80f154237dcd4 |

The report claims two identical runs of its own code: 28/28 PASS,
417882731 contacts and 21800 swaps, including complete k=1,2 families and
samples at k=4,5. Its supplied endpoint digest is
`5fa52c61f2af6731eefcf9827cda7491e8fe9b2f54e420aa439c157a312755c1`,
identical to PR1879. This integration inspected the complete supplied code
and output and checked their hashes, but did not execute that new code or
independently verify its reported runtime or two-run history. The raw review
archive is not imported and is not a new normative dependency.

The inspected code uses the standard library and reads its WORD535 fixture;
no network, subprocess, dynamic execution or file writes were found. Its
contact uses an output-integrality guard, its account uses Tr(a*bar(a))/2,
and it constructs the words and decoder separately from PR1879.

Two coverage qualifications must survive any summary. First, the supplied
report says full invariants are checked at every checkpoint. The code
explicitly checks them initially, after each complete cycle, and after the
full inverse. After W it compares the 31-slot core to its closed formula;
after both copies it checks that core, the two new archives and freshness
of future archives. Complete 101-slot equality is checked at the final
endpoint and after the full inverse. The full Hermitian invariant is not
separately summed at the W and copy checkpoints. This is narrower direct
instrumentation, not an observed counterexample.
Second, assertions can be disabled by an optimized invocation because the
script has no unconditional optimization guard. The reported command
`python3 -I` without `-O` does not disable them. No optimized run is accepted
as evidence. Neither qualification alters PR1879's stricter frozen verifier.

## The two-architecture obligation is already discharged

The actual science logs were fetched again from
[run41680260019 attempt1](https://github.com/mathorn1973/twist-j/actions/runs/41680260019),
which completed SUCCESS at the exact reviewed PR head. The architecture jobs
are [aarch64 job126071726358](https://github.com/mathorn1973/twist-j/actions/runs/41680260019/job/126071726358)
and [x86_64 job126071726630](https://github.com/mathorn1973/twist-j/actions/runs/41680260019/job/126071726630);
aggregate job126073366718 also passed.

Both logs contain the actual VERIFY ARCHITECTURE and VERIFY PASS lines for
P-RELATIVE-CONTACT-WORKBANK-REUSE-1, with verifier SHA-256
`645ac0808feedcfd111cd54b80e1496202be36a142b5c317236496b8dda93bfb`
and identical 2083-byte stdout SHA-256
`78d928c9303732b501bfab0b52c159c2fed4fcb0857c24cac59341aad3ec36e3`.
Both also passed all 218 tool tests and the required repository checks.
These are scientific replays, not notes-only integrity jobs. The reviewer's
inability to access the API does not require another architecture run.

POLICY says that the workflow can discharge the two-architecture computation
gate. It does not make every two-architecture result a theorem automatically.
Independent proof acceptance, exact scope and the reviewed Canon fold remain
separate requirements. The new PR1882 review supplies an additional proof
assessment; its findings are addressed explicitly in REVIEW_1882_DISPOSITION.md.
Neither the older report nor missing CI access is used as a substitute.

## Next review and fold

Review the exact public PR1879 source pin
`6f6570bbbddfc496131dd31c5fdacaaa9e1cd9e5` at the stated head. Record reviewer
identity, prior exposure and any authorship relationship explicitly. Use the
three claim scopes and falsifiers in CLAIMS.md; accept, narrow or reject each.
No blind-discovery claim is required for reading an exposed public proof.

The section 5 exposition can be clarified in a later fold with the explicit
modulo-nine event derivation in CLAIMS.md. It need not rewrite the frozen
probe. The same complete read identity is already part of the canonical
v108 common-apparatus construction; it is not a new unbounded read theorem.

After accepted independent review, a separate v109 content fold can integrate
only earned scopes, preserve the v108 finite theorem and unrelated open
obligations, and undergo the normal complete validation and reviewed release
procedure. This proposal performs none of those authority-changing actions.
