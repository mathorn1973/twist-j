# PROMO-PHOTON-SUCCESSORS-V72-STATUS-SEPARATION-AMENDMENT

Status: **NON-CANONICAL / NO AUTHORITY / PROMOTION AMENDMENT ONLY.**

Public lock: [issue #705](https://github.com/mathorn1973/twist-j/issues/705).

This note amends only the exact content-commit file surface frozen by
`PROMO-PHOTON-SUCCESSORS-V72` and its test-surface amendment. It creates no
claim, status, Canon version, Registry row, Frontier row, gate, evidence,
probe, tag or release, and it changes none of the four frozen scientific
scopes.

```text
basis main:                         fe7c5d4f654c58ae5da35d7b3c49c9c934670645
parent promotion package:          notes/canon/PROMO-PHOTON-SUCCESSORS-V72.md
parent promotion commit:           8727e6dabf8ff4bbd5532715a0eacb50fdc7f4e8
parent promotion PR / merge:       #701 / c862642a41fe798b6c510f3c4f817d258f75afec
parent package git blob / bytes:   113bfa98f3e2c00ff96593a617802ebc9b26659c / 36112

first amendment:                   notes/canon/PROMO-PHOTON-SUCCESSORS-V72-TEST-SURFACE-AMENDMENT.md
first amendment commit:            4dd9d686ccca72836a7b76d8300056c725c0bea1
first amendment PR / merge:        #703 / fe7c5d4f654c58ae5da35d7b3c49c9c934670645
first amendment blob / bytes:      7826b81a927be9f170c293212ef1512fc0d8fda5 / 6986

failed immutable content commit:   8f8c76e333235950e3f69bb5822ceefba096936e
failed release-form commit:        4ae7e3587ee1ddbfb58131e9c2d37acbbc5f0325
failed release PR / workflow:      #704 / 33322092692
failed x86_64 job:                 99285732111
failed aarch64 job:                99285732009
```

PR #704 is closed as a failed sealed candidate. Its remote branch and both
commits remain preserved as divergent evidence. They must not be amended,
rebased, force-pushed, deleted or merged.

## Reason for the amendment

The first amendment correctly added the architecture-map fixture needed by
the 142-test gate, but it also froze every reproduction byte. A Canon change
widens `tools/check_reproduce.py` to all public minimal reproductions. On the
exact two-commit v72 head, both required Linux architecture jobs passed:

```text
policy
142 unit tests
Canon
ledger
gate contract
every public probe
```

Both then failed identically at `reproduce/status-separation` before any
stdout comparison. Direct execution on that head isolated exactly three stale
checks:

```text
FAIL 01 COUNTS
FAIL 62 V69-CM
FAIL 63 V70-QDD-SPLIT
RESULT 60/63 FAIL
```

The audit still pinned the v70 aggregate counts, the pre-v72 complete
`GATES.tsv` hash in two historical checks, and a 29-row live Frontier. Public
Canon v72 legitimately has four more rows, seven more dependencies, three new
gates and two new live roots. All four new scientific rows, their scopes,
evidence and public probes had already passed. This is therefore a mandatory
conformance-surface repair, not a scientific failure and not permission to
skip or weaken the reproduction gate.

## Exact authorized postimages

Only the following three files may change. The raw SHA-256 hashes apply to the
file bytes; the git blob hashes include the normal git blob header.

```text
path                                          preimage blob                              preimage bytes  preimage raw SHA-256
reproduce/status-separation/verify.py         e3f81c9edf79564a28433b703adfe492b15af886    239975          51720a29208ce57da8c7adab0eae8133345776339b9cc3763e91c69133f8cf05
reproduce/status-separation/EXPECTED.txt      c12ab4a862f41919d56865155b0c22eb464f8628      9890          73d92895d10119b65b0c7041ab693f122f65cfbe4f51f20875614bd82aa0036a
reproduce/status-separation/README.md         b4fd66cd034bb0ffbbb4884516302ab81fa86d4e     22456          654134dda20189c9affa561e46a31d9d7079aa31c9e8e5d8890cd3e9389f5bc1

path                                          required postimage blob                     postimage bytes  postimage raw SHA-256
reproduce/status-separation/verify.py         36c2ceed16343e15055af6147d706bd945d15238    254689           d7a74e7d379b0ed49b2ae2df5e377f74a3e9a94f79503bb98acc076a0a92c57b
reproduce/status-separation/EXPECTED.txt      0ba58f7bb9b02e04ff6065e428d0662b8227b8d9     10036           e4bd9d1ac17b417bad8728a73250d38485c5030ed0b4a27e023f4bb8b4a5c9bc
reproduce/status-separation/README.md         ae9f73a611fe1e29665831206f5d85713014a44b     24115           f83163b316c4c71f1a2c989d9f5b2ab47ccc19843bee775bafe2d7b923c9b261
```

The standard LF-only zero-context diff produced by

```text
git diff --unified=0 --no-ext-diff -- \
  reproduce/status-separation/verify.py \
  reproduce/status-separation/EXPECTED.txt \
  reproduce/status-separation/README.md
```

is frozen at exactly:

```text
bytes:   22096
SHA-256: 8098b640baba3279718f2f06d995df6a02f69b694203315034a9f9ffd4ceae9c
files:   3
delta:   365 insertions, 34 deletions
numstat: EXPECTED.txt 3/2; README.md 31/6; verify.py 331/26
```

The required postimage blobs are authoritative if prose in this amendment is
ever read ambiguously. No alternative formatting, refactor or equivalent
output is authorized.

## Exact conformance delta

The verifier changes only as follows.

1. The current aggregate contract becomes Public Canon v72:

```text
claims:                         346
status partition:               T221 D44 C33 H2 O29 F17
NORMATIVE rows:                 392
DEPENDENCIES rows:              639
EVIDENCE rows:                  346
two-architecture evidence:      259
HISTORY rows:                   875
GATES rows:                     14
FRONTIER_PROGRAMS rows:         31
distinct program ids:           8
CORE_SELECTION rows:            30
minimal reproductions:          23
```

2. `V69-CM` and `V70-QDD-SPLIT` stop hashing the complete pre-v72
   `GATES.tsv`. Their claim-specific no-gate checks remain. The duplicate
   v70 live-Frontier count of 29 is removed while the structural equality
   between all live H/O rows and all program rows remains. The unchanged
   complete `CORE_SELECTION.tsv` hash
   `eee121dd437d06fc2b0fda5377ea6c2e6e01b220e5f1bfb9aa09727885d03d4e`
   remains pinned once, and the historical rows retain targeted
   non-ownership checks.

3. A new `V72-PHOTON` check pins exactly:

```text
2 theorem rows:                 FCC-WEIGHTED-SHELL-SYMBOL T/L2
                                PHOTON-WILSON-VILLAIN-FINITE-COUPLING-NONMEMBERSHIP T/L4
2 obligation roots:             PHOTON-CONE-CONVERGENCE O/MULTI
                                PHOTON-MASSLESS-PHASE O/MULTI
dependency rows:                7, including every full basis string
incoming consumers:             FCC -> Cone only, BOUNDED_BY
                                Wilson/Villain -> Massless only, BOUNDED_BY
                                no consumers of either O root
gates:                          3 exact full rows, all OPEN_LIFT
program rows:                   both O roots PHOTON_CONTINUUM/ROOT/STOP/FORMAL
evidence:                       2 exact two-architecture public bundles
                                2 exact inline scope hashes
lifecycle:                      4 exact DECLARE rows including rationales
Normative source:               exact section-9 source for all four rows
```

The check also preserves the exact Registry row hashes and scope hashes,
requires the Canon prose to keep the displayed L2 symbol unselected, keeps
finite Wilson/Villain nonmembership as boundary information rather than
massless-phase closure, leaves `PHOTON-KAPPA-LEMMA` and
`PHOTON-WINDOW-PROOF` terminal at F, keeps both theorem rows out of Frontier,
keeps all four rows out of CORE selection, admits no registered identifier
containing `ROUGHEN`, and admits no roughening, uncited Froehlich-Spencer,
Lorentz, continuum-propagator or physical-photon promotion.
The complete Canon insertion delimited by
`### FCC-WEIGHTED-SHELL-SYMBOL [T]` and the following `The electron:` paragraph
is additionally frozen at 4569 UTF-8 bytes and SHA-256
`ee5ce5e018d80fc97a1edb7e041fce0734922ff4507255969bbebf82de9c2277`;
required negative phrases cannot conceal added positive prose.

4. `EXPECTED.txt` changes only the v70 count label to v72, appends
   `PASS 64 V72-PHOTON`, and ends with `RESULT 64/64 ALL PASS`.

5. The reproduction README describes the same 64-check contract and retains
   its historical sections as historical rather than global current-state
   locks.

## Amended exact content surface

The complete later v72 replacement content commit may change exactly these
seventeen files relative to the public merge of this amendment:

```text
canon/CANON.md
canon/CORE.md
canon/FRONTIER.md
canon/REGISTRY.tsv
canon/CHANGELOG.md
canon/SHA256SUMS
canon/NORMATIVE.tsv
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
canon/HISTORY.tsv
canon/GATES.tsv
canon/FRONTIER_PROGRAMS.tsv
canon/STATUS_COUNTS.tsv
tools/test_architecture_map_report.py
reproduce/status-separation/verify.py
reproduce/status-separation/EXPECTED.txt
reproduce/status-separation/README.md
```

The separate release-form commit remains exactly:

```text
STATUS.md
README.md
CITATION.cff
```

Every other parent-package instruction remains binding. In particular,
`canon/CORE_SELECTION.tsv`, every scientific scope, status, dependency,
evidence row, lifecycle row, gate row, Frontier row, probe byte and every
other reproduction byte remain exactly as already frozen. `canon/CANON.md`
remains exactly 374406 bytes with SHA-256
`39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70`.

## Verification and STOP conditions

The frozen postimages already satisfy locally:

```text
status-separation verifier:      exit 0
stderr:                          0 bytes
stdout:                          byte-identical to EXPECTED.txt
result:                          64/64 ALL PASS
stdout bytes / SHA-256:          10036 / e4bd9d1ac17b417bad8728a73250d38485c5030ed0b4a27e023f4bb8b4a5c9bc
python tools/check_policy.py:     PASS
142 unit tests:                  PASS
python tools/check_canon.py:      CANON PASS v72 claims=346
python tools/check_ledger.py:     LEDGER PASS claims=346 items=392 dependencies=639 evidence=346 history=875 gates=14 programs=8
python tools/check_gate_contract.py: GATE CONTRACT PASS gates=14
git diff --check:                PASS
line endings / final newline:    LF only / present
```

Native Windows full-sweep byte comparison remains non-authoritative because
unrelated older verifiers emit CRLF there. The replacement release candidate
must still pass both required Linux architecture jobs, including the full
public-probe and minimal-reproduction sweeps, and the aggregate check.

The replacement release branch must be based on the public merge of this
amendment and must contain exactly two commits after that basis: one immutable
seventeen-file content commit and one three-file release-form commit. The
failed commits may be used only as read-only patch sources; neither failed
commit may appear as a separate release commit.

STOP on any different preimage, postimage, diff byte, output byte, count,
assertion, Canon SHA-256 or byte count, additional content file, change to
another reproduction or any probe, changed scientific scope or ledger row,
third release commit,
amend/rebase/force-push of the failed branch, or release branch not based on
the public amendment merge. If an intervening Canon content fold lands first,
the entire v72 package must be re-gated rather than silently rebased.
