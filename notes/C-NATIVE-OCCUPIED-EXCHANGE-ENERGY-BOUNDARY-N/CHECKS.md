# Source custody and repository validation

PUBLIC / NON-CANONICAL / L1. Authored conditional candidate-T.
Author: A. M. Thorn. Apache-2.0.
Claim [#1620][claim].

## Authority and immutable analytical pin

ACTIVE Public Canon v103 was verified from the public repository.
Main and peeled canon-v103 are
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, with tree
52048d642e988830fe280928e6297c5a565a7324. The content ancestor
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66 has tree
b61e7a10d098307e392840955618e7ed232f6c28.
The two trees were checked from both public Git objects and local Git.

The five normative SHA-256 checks passed. CANON.md has 1052518 bytes
and SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.
Tag/content ancestry and successful main required CI 39022927713 were
verified. Authority documents, current issues and explicit public branch
inventory were read; the remote scan contained 263 heads before this
new branch. Exact-identifier and semantic claim searches found no duplicate
of the scoped note. Existing neighbouring owners were retained.

The [source manifest](SOURCES.tsv) binds nine literal public files at
immutable commits by path, Git blob, byte count, SHA-256 and license.
The canonical native definitions and #1619 proof are the direct
mathematical premises; the remaining files supply the contextual
comparison of interfaces and limits. Their scientific programs were
not executed. Internal attachment numbering supplies no public authority
and no attachment is imported into this note.

The public analytical pin is:

~~~text
commit: 851c4ef0ef43690c245ef3208d436a924080bbb7
parent: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
tree:   fb0490d86aeee7063e44185d27695be424e1cd9c
branch: notes/C-NATIVE-OCCUPIED-EXCHANGE-ENERGY-BOUNDARY-N
~~~

It adds exactly CONTRACT.md and SOURCES.tsv. The public ancestry, tree,
both file blobs and their complete texts were read back and matched the
local index before final proof drafting. The [pin receipt][pin-receipt]
records that boundary. All mathematical reconnaissance and prior result
exposure are disclosed in the contract; this is not a prospective
scientific-verifier pin or a blind experiment.

## Frozen and reviewed files

| File | Bytes | SHA-256 |
|---|---:|---|
| CONTRACT.md | 17705 | 72eba4d08f4e390d9bbf0ad8b6141c5846476ac1f658cc5237b0ea3ec141b96e |
| SOURCES.tsv | 3223 | 76756b992f11b29a79489e17eb069a4f867d8697eae70cfba4e155fa4e87f607 |
| PROOF.md | 47783 | 2f295131f04ecbb26feef5a9b2f50819047488f10ba832d73ad9127cda5b7f98 |
| README.md | 9038 | 45325e602f36c239cecadc03a54c21d63289c464b3fa8e79db09915d9f2c283f |
| REVIEW.md | 7007 | 0d2c17459cba867106bc69010a28be503c1b0e37c91a810578271614f45d5112 |

The contract and source manifest remain byte-identical to the public pin.
The result descendant adds only PROOF.md, README.md, REVIEW.md and
CHECKS.md in the same sole note directory. This file contains no
self-referential checksum; the public result receipt binds all six
file hashes and Git blobs to the result commit and tree.

All three same-session collaborators confirmed their assigned scope on
the final proof hash; [REVIEW.md](REVIEW.md) records precise coverage,
result exposure and the three corrections made during review.
These checks are manual and not external independent scientific review.

## Local engineering checks actually run

The unchanged repository commands were run from the repository root on
Linux 6.18.55, x86_64, Python 3.12.14.

| Command | Observed result |
|---|---|
| python3 tools/check_policy.py | POLICY PASS |
| python3 -m unittest discover -s tools -p 'test_*.py' | 189 tests; OK |
| python3 tools/check_canon.py | CANON PASS v103; 530 claims |
| python3 tools/check_ledger.py | LEDGER PASS; 530 claims, 594 items, 1105 dependencies, 530 evidence rows, 1077 history rows, 26 gates, 7 programs |
| python3 tools/check_gate_contract.py | GATE CONTRACT PASS; 26 gates |
| python3 tools/check_verifier.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d | VERIFY NOT APPLICABLE |
| python3 tools/check_reproduce.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d | REPRODUCE NOT APPLICABLE |

The unit suite contains intentional negative fixtures that print
PROBES FAIL and REPRODUCTIONS FAIL. It completed with exit zero and
all 189 tests OK. Those fixture messages are not failed scientific
verifiers of this note.

The changed-path commands compare the base with Git HEAD. Their first
local executions used the analytical pin as HEAD. The exact result
descendant must repeat those two applicability checks after publication;
its only extra paths are four text files in this note. The delivery
receipt records that repeat, the base-to-head whitespace check and the
clean local tree. Ordinary file hashing is administrative, not evidence
of a scientific computation.

The public-content review covers the six plain-text files, public
immutable source links, authorship/license, scope and permitted paths.
No executable, secret, private address, private log, host identifier,
binary or imported attachment is included. The note changes no Canon,
registry, ledger, gate, old source, tool or workflow. The separate
documentation correction on #1615 is not part of this branch's diff.

## Exact result readback and CI boundary

The authorized delivery is one draft PR with base main and a direct
descendant of the analytical pin. Its public receipt will bind the
result commit and tree, unchanged pin files, complete six-file manifest,
public full-file readback, exact-head checks and required CI job IDs.
Later CI receipts do not change these proof or scope bytes.

The unchanged workflow runs repository checks on x86_64 and aarch64,
with their aggregate required check. Exact-head public CI is pending
when this file is committed; its actual result belongs in the public
delivery receipt and PR body. A running job must not be reported as
successful.

On this notes-only diff no scientific probe or reproduction is selected.
Passing both architectures is therefore repository validation, not a
scientific two-architecture replay, a new computation-grade result or
independent proof. No new scientific code was accepted, imported or run;
no EXPECTED.txt, RUN.md, numerical output or experimental evidence is
created.

The scientific ceiling remains authored conditional candidate-T at L1.
Native contact admission, energy-reading selection independent of the
target, the full reference/common-apparatus price and all physical
interpretations retain their stated open boundaries.
No merge, tag, release or Canon promotion is part of delivery.

[claim]: https://github.com/mathorn1973/twist-j/issues/1620
[pin-receipt]: https://github.com/mathorn1973/twist-j/issues/1620#issuecomment-6251236226
