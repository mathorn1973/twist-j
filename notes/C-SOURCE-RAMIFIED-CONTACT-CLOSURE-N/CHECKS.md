# Analytical custody and repository validation

PUBLIC / NON-CANONICAL / L1. Authored conditional candidate-T.
Author: A. M. Thorn. Apache-2.0. Claim [#1614][claim].

## Authority and public pin

Public Canon v103 was ACTIVE when this work was claimed and remained the
public base at delivery preparation. Both main and peeled canon-v103 were
`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`. The v103 content ancestor was
`01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`, with tree
`52048d642e988830fe280928e6297c5a565a7324`.
The status, policy, live coordination, all 260 then-public heads, current
main CI run 39022927713 and exact/semantic claim collisions were checked
before the new claim. The named neighbouring owners were retained.

The six literal source files in [SOURCES.tsv](SOURCES.tsv) were read at
their immutable Git objects and checked for byte count and SHA-256.
The Canon and #1612 work proof are the direct mathematical inputs; the
remaining four files supply contextual scope only. They were not replayed.

The public analytical pin is

```text
commit: c47f97f0a35d4cffce412ac48150ae6ef80d3963
parent: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
tree:   a86726902cf56813d1756d48ac77af3874712e70
branch: notes/C-SOURCE-RAMIFIED-CONTACT-CLOSURE-N
```

It adds exactly CONTRACT.md and SOURCES.tsv in the sole note directory.
Their exact public bytes and commit ancestry were read back before the
final proof was drafted; see the [public pin receipt][receipt].
This pin is an analytical scope/custody boundary, not a prospective
scientific-verifier pin. Manual reconnaissance and result exposure before
it are explicitly disclosed in the contract.

## Frozen and reviewed bytes

| File | Bytes | SHA-256 |
|---|---:|---|
| CONTRACT.md | 13185 | `90e7a25dad9708c75c77d983c6ef10b23e8e0887b6ed658b532deb50ecfbe8ae` |
| SOURCES.tsv | 2060 | `f6b63f06e5381a053b076d2128110c9e80471ebe08c86573a220a77a3237b9eb` |
| PROOF.md | 28492 | `14abf3d58def56ef0522ea64de6081329e15af75f7e3923efbd78eba77e5f012` |
| README.md | 6520 | `8942303442cebafc33d76c8de89c1c3e2458e0f843afdd89e11a7623b7fa505e` |
| REVIEW.md | 8129 | `081a2dc884aec835b81d9c3714eae0bc42bf04ed1ee73c868992ae7508ebfc3e` |

The contract and manifest have an empty diff against the analytical pin.
The result descendant adds only PROOF.md, README.md, REVIEW.md and this
CHECKS.md. This file does not include a self-referential checksum; the
public delivery receipt binds all six file blobs and hashes to the result
commit and tree.

The proof review in [REVIEW.md](REVIEW.md) is manual, result-exposed and
from the same session. All three collaborators confirmed their assigned
coverage on the final proof hash. It is not independent external review.

## Local repository validation

The following ordinary engineering checks were run from the repository
root on Linux 6.18.55, x86_64, Python 3.12.14. They do not constitute
execution of the new mathematical claims.

| Command | Observed result |
|---|---|
| `python3 tools/check_policy.py` | POLICY PASS |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | 189 tests; OK |
| `python3 tools/check_canon.py` | CANON PASS v103; 530 claims |
| `python3 tools/check_ledger.py` | LEDGER PASS; 530 claims, 594 items, 1105 dependencies, 530 evidence rows, 1077 history rows, 26 gates, 7 programs |
| `python3 tools/check_gate_contract.py` | GATE CONTRACT PASS; 26 gates |
| `python3 tools/check_verifier.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d` | VERIFY NOT APPLICABLE |
| `python3 tools/check_reproduce.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d` | REPRODUCE NOT APPLICABLE |

The two changed-path commands compare the base with Git HEAD. Their local
pre-publication executions used the analytical pin as HEAD. The result
descendant must repeat those two applicability checks against its exact
HEAD; its only additional paths are four Markdown files in this note.
The delivery receipt records that repeat and the final whitespace/path
checks, without rewriting these analytical evidence bytes afterward.

The unit suite includes intentional negative fixtures that print PROBES
FAIL and REPRODUCTIONS FAIL. Its process returned zero with all 189 tests
OK; those fixture messages are not failed note verifiers.

The public-content review covers the six named plain-text files: the
mathematical scopes, public immutable source links, author/license notices,
and absence of executable additions, private material or imported logs.
No old source, Canon, ledger, gate, tool or workflow is changed.

## Exact public delivery boundary

The authorized delivery is one draft PR with a descendant of the public
analytical pin. Before reporting completion, read back its parent/tree,
the exact six public file blobs and bytes, and the unchanged pinned files.
The public PR and claim receipt record its result SHA and tree, path set,
complete file manifest, required workflow run and architecture job IDs.
Those later receipts do not change the proof or its scope.

The unchanged workflow runs repository checks on x86_64 and aarch64 and
requires their aggregate check. On this notes-only diff, scientific probe
and reproduction execution are not applicable. A green pair of architecture
jobs is therefore **repository validation, not a scientific two-architecture
replay or independent proof**. Exact-head public CI is pending at the time
this file is committed; its eventual result belongs in the delivery receipt.

No scientific executable was accepted, imported or run for this note.
No EXPECTED.txt, RUN.md, numerical result, new candidate-C, Canon fold,
merge, tag or release is part of this delivery. The retained scientific
ceiling is authored conditional candidate-T pending independent review.

[claim]: https://github.com/mathorn1973/twist-j/issues/1614
[receipt]: https://github.com/mathorn1973/twist-j/issues/1614#issuecomment-6248985664
