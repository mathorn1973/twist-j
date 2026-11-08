# Independent review of the v109 workbank proof scopes

NON-CANONICAL / L1. Review disposition for the three candidate proof scopes
of [PR1879](https://github.com/mathorn1973/twist-j/pull/1879), following the
review surface prepared in
[PR1881](https://github.com/mathorn1973/twist-j/pull/1881). No Canon fold,
registry entry, status change or release follows from this note. Current
authority remains Public Canon v108 at
`17de90b58f814238e151aac77badde6654b52627`.

## Reviewer, exposure and authorship

Reviewer: a Claude Code cloud session (Anthropic), opened by the project
author on 2026-11-03 for this review alone, session
`https://claude.ai/code/session_0138vAKtkRLoszroTmcmcbXw`.

Authorship relationship: this session authored none of C-BANK-COPY-WORD-1,
PR1879, PR1881 or the review supplied for PR1879, and was not consulted for
any of them. It has no memory of, or access to, any other session. It cannot
exclude that another session of the same model family took part in earlier
work; model-family independence is not claimed. The independence claimed is
session, authorship and code-path independence.

Prior exposure, in order:

1. Before any check was written: the PR1881 body and its two added files,
   the PR1879 body and both PR1879 comments (which disclose the successful
   run, counts and hashes), PROOF.md, PREREG.md, README.md, PROVENANCE.md and
   SOURCES.tsv at source pin `6f6570bbbddfc496131dd31c5fdacaaa9e1cd9e5`, the
   Canon v108 sections defining the integral relative contact and
   RELATIVE-CONTACT-COMMON-APPARATUS-OPEN, and the first and last lines of
   WORD535.txt (format only).
2. After `review.py` was written and its development runs for k<=2 had
   passed: RESULT.md and RUN.md at head
   `d6a5f77169d1027a22959c41aa5a45a783643a3e`.
3. After the final `review.py` run: EXPECTED.txt and a static reading of
   the target verify.py, used only for its JSON serialization so that the
   published digests could be compared.

The supplied PR1879 review report, its code and its stdout were not seen;
they are not in the repository. This is a result-exposed review of an
exposed public proof, not a blind discovery.

## Verdicts

| Scope (PR1881 CLAIMS.md) | Verdict |
| --- | --- |
| 1. Positional-bank copying | ACCEPT at the stated scope |
| 2. Four-place literal-copy obstruction | ACCEPT at the stated scope |
| 3. Finite reuse with retained archives | ACCEPT at the stated scope |
| Modulo-nine derivation of the read event table | CONFIRMED as exposition of the v108 table |

No narrowing is required and no falsifier fired. REVIEW.md gives the
step-by-step checks and three optional, non-blocking remarks: the rotated
copy corollary, a wider alphabet for the obstruction, and a closed formula
for the Hermitian account. Acceptance rests on the symbolic arguments of
PROOF sections 1-4 and 6-8, which were checked line by line. Section 5
restates the canonical v108 read construction; it was checked for agreement
with Canon v108 and replayed, not re-accepted as a new theorem.

## Independent computation

`review.py` is a new standard-library implementation written from the proof
text, without the target verifier. It uses a cyclic `Z[x]/(x^5-1)`
representation of O, cross-checked on every new contact entry against a
separately written j-basis map. It rebuilds the 535-contact word from the
block equations, checks it contact by contact against WORD535.txt, and
executes P_k exhaustively for k=1,2,3. For k=3 that is all 1000 triples,
403050000 literal contacts and 20000 swaps. Complete-state closed forms and
invariants are checked at every W, K, W^-1 and loading boundary. Samples at
k=4,5 are labelled as samples and are not proof.

`compare_after_run.py`, written after that run, serializes the independent
build in the target's JSON format. It reproduces all four PR1879 digests
exactly:

| Digest | Value | Result |
| --- | --- | --- |
| complete program | `a0e78fe4f4b430c76d4753fcbe7aed96cbfe43e340353cad2f4d1b8b56eeaeb6` | MATCH |
| complete literal inverse | `ccc21b191f368b4a2ae450cc6c5fd422f2edeb85f957a08d88348e43a000ed12` | MATCH |
| 1000 complete endpoints | `5fa52c61f2af6731eefcf9827cda7491e8fe9b2f54e420aa439c157a312755c1` | MATCH |
| decoded histories | `bff60f741c325dc5c3a27bc737c389c37466d93bb267f16ef2f9198b6e42e46c` | MATCH |

So the program built from PROOF.md alone equals the frozen PR1879 program
primitive for primitive, and both reach identical complete 101-slot
endpoints.

The scientific CI logs of
[run41680260019](https://github.com/mathorn1973/twist-j/actions/runs/41680260019)
were fetched again. Job 126071726358 (aarch64) and job 126071726630 (x86_64)
both print `VERIFY PASS P-RELATIVE-CONTACT-WORKBANK-REUSE-1` with verifier
`645ac080...bfb` and stdout `78d928c9...e3`; the aggregate job 126073366718
passed. This agrees with PR1881. These computations support the review; the
two-architecture gate was already discharged and is not re-earned here.

Reproduce from the repository root (the fixture on main has the same
SHA-256 as the PR1879 copy):

    python3 -I -B notes/C-WORKBANK-REUSE-INDEPENDENT-REVIEW-N/review.py probes/P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1/WORD535.txt
    python3 -I -B notes/C-WORKBANK-REUSE-INDEPENDENT-REVIEW-N/compare_after_run.py

Recorded on Linux x86_64 with CPython 3.13.18: exit 0, empty stderr, exact
stdout in REVIEW-OUTPUT.txt and COMPARE-OUTPUT.txt. A second run from these
repository paths was byte-identical. The
first command takes about two minutes and the second about fifteen seconds.
Every check raises SystemExit and none relies on `assert`, so `-O` cannot
disable them. The scripts were not preregistered or pinned before execution.
Three reviewer-side defects were fixed during development: an orbit cap on
the optional BFS, a clock test on a two-slot carrier, and a retention window
check that was too strict. None of them concerned a target claim.

## Custody

Reviewed target sources at pin `6f6570bb`, unchanged at head `d6a5f772`:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PROOF.md | 25373 | `7345b699f2f6f3dc2059318d0a526d15c32b05b72b3f36c6ffdae2b6ffc4c8f8` |
| PREREG.md | 9821 | `edd43e722ca7c407a904a6d9cc2c70fcc215c10830b0fa8de92a8f59fc9687e7` |
| PROVENANCE.md | 3337 | `65788bd17f31b98285e4d519e4a5a3d463d1caa80c6eb4cd9234aa939cda6bf8` |
| README.md | 3494 | `5363b41d734fb842a27d5818d8289d727fc02c36c0e8fb6ea34e0010144643ec` |
| SOURCES.tsv | 1906 | `27c5dea66524af0316ed66b94edd7f28dc7f97d824bc1a02651f2bb7a44e5fd7` |
| WORD535.txt | 4877 | `ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b` |
| verify.py | 30973 | `645ac0808feedcfd111cd54b80e1496202be36a142b5c317236496b8dda93bfb` |

PR1881 was reviewed at head `337bf93c2f59d4f34a6395ef36de51aa3959c24e`. The
review files in this directory are listed in SHA256SUMS.

## Consequence

Independent mathematical acceptance of the three scopes is now on record,
from a reviewer that authored neither the original copier nor the PR1879
construction. Whether this satisfies the project's independence requirement
is the author's decision. A v109 fold remains a separate content fold with
its own complete validation and reviewed release. This note changes no
probe, Canon text, registry, status, workflow, tag or release.
