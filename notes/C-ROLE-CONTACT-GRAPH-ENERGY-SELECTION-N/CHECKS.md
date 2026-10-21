# Checks and custody

**PUBLIC / NON-CANONICAL / L1.** Claim #1624.

## Authority and immutable pin

Base/main and peeled public tag canon-v103:
`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`.
All five normative hashes matched the public declaration; the tag and
declared content commit are ancestors of main. Required main run
39022927713 is successful. No authority file is changed here.

Contract/source pin: `ecfb13823a43243dbdb09c5d3879d323dc2deea6`.
Pin tree: `c10f1aa1fa2370f361f8965ebe202eb7ec5eba0b`.
Public Git metadata confirms its sole parent is the stated main and
its author and committer are A. M. Thorn. The two complete files were
fetched at this exact public commit and compared with local bytes and
Git blobs before drafting PROOF.md.

| Frozen file | Bytes | Git blob | SHA-256 |
| --- | ---: | --- | --- |
| CONTRACT.md | 10743 | 5336335e2df83fe2ceec4ef92caaa5ed9357dc76 | 1c7305a7eeeef8e9d8e8cb33ea3cc72d75091d06a8f27e3b88d2ffe6b4eb34bf |
| SOURCES.md | 5940 | 4d372a8c6da8d028d87351a17ebd2abdc29b00da | a2d865c4c5f2aaaef3b437b6c48efb8ab11bdcf446bf91213dd513919ec027be |

Pin custody is recorded in
[#1624, comment 6252469466](https://github.com/mathorn1973/twist-j/issues/1624#issuecomment-6252469466).
These files remain unchanged in the result descendant.

## Analytical evidence

The mathematical evidence is the self-contained PROOF.md and exact-file
analytical review recorded in REVIEW.md. The contact graph, ranks,
state counts, word length and energy tables were derived by hand.
No new scientific executable was run, imported or compiled, and no
state/word search or enumeration was performed. The existing source
verifier was only read. Reviews are same-session and result-exposed,
not blinded or external confirmations.

## Local repository checks

The following unchanged infrastructure commands were run from the
repository root under Linux with Python 3:

```text
python3 tools/check_policy.py
python3 -m unittest discover -s tools -p 'test_*.py'
python3 tools/check_canon.py
python3 tools/check_ledger.py
python3 tools/check_gate_contract.py
```

Results:

- POLICY PASS.
- All 189 infrastructure unit tests passed. The suite's intentional
  negative fixtures print PROBES FAIL and REPRODUCTIONS FAIL; the
  completed suite ends OK with exit zero.
- CANON PASS v103, 530 claims.
- LEDGER PASS: 530 claims, 594 items, 1105 dependencies, 530 evidence
  rows, 1077 history rows, 26 gates and 7 programs.
- GATE CONTRACT PASS, 26 gates.

Named-file staging and whitespace checks accompany the result commit.
The public delivery receipt records their final result, repeats the
changed-path applicability checks on the actual result Git HEAD, and
confirms the exact six-file diff and a clean dedicated worktree:

```text
git diff --cached --check
git diff --check dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d...HEAD
python3 tools/check_verifier.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
python3 tools/check_reproduce.py --base dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
```

Those applicability tools compare committed Git heads. A run while the
result is merely unstaged or staged is not described as a check of the
result commit. This notes-only package adds no scientific replay target.

Manual public-file review covers the six Markdown files: no private
source text, credentials, private infrastructure, binary output,
workflow change, Canon change, or modification of a sealed probe is
included. Scientific scopes and supplied-gate assumptions are explicit.

## Public delivery and CI

The result is a non-forced descendant of the public pin. Its delivery
receipt on #1624 and the draft PR records the result commit/tree,
complete six-file byte/hash readback, unchanged frozen files, exact
reviewed proof hash and the required CI outcome on both architectures.
That receipt is recorded after publication; this file does not claim
that an unpublished result had already passed public CI.

The required workflow uses x86_64 and aarch64 architecture jobs and
their aggregate check. If it checks out a synthetic PR merge, the
receipt distinguishes that checkout from the PR head and verifies
equality of its tree to the reviewed result tree. Infrastructure CI
does not prove the mathematics or constitute a scientific replay.

No merge, release, Canon promotion, physical-admission closure or
changed bank/clock law follows from these checks.
