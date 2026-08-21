# FOLD record: the TM Hankel k = 3 arc enters the Canon as Public Canon v43

DATE 2026-08-11 (UTC). FINAL. The seven-row fold decided by the owner is
ACTIVE on the public line as Public Canon v43. The v42 designation was
consumed by a fired activation gate and has no release; the full firing
record is below, kept per falsification-first practice.

## Final public state

```text
STATE            ACTIVE, Public Canon v43
main             981aa1b9c8bc7ecd084346e099f014f3fc78847c (merge of PR 341)
tag              canon-v43 -> 981aa1b, publication readback SUCCESS
release          https://github.com/mathorn1973/twist-j/releases/tag/canon-v43
                 assets activation-manifest.json + SHA256SUMS attached from
                 the successful tag job, downloaded back byte-identical,
                 manifest PASS, release-event validation run SUCCESS
CONTENT_COMMIT   320324f0def8ac9af89d0f128dbd7ab6548df55b
CANON_SHA256     a52d0c266024dd492b56f6ad3a1121e3bccd0a0563b86176cab0118bc8e4991c
CANON_BYTES      207795
registry         234 claims; T 129, D 41, C 26, H 2, O 23, F 13; live 25
```

## The seven rows (owner's epistemic split, verbatim intent)

```text
TM-HANKEL-DIVISOR-BRIDGE                       T
TM-HANKEL-SQUAREFUL-RANK-NOGO                  T
TM-HANKEL-EXTREMAL-WITT-SKELETON               T
TM-HANKEL-K2-TRANSFER                          T
TM-HANKEL-K3-UNIVERSAL-TRANSFER                F   fired: 147965 = 5.101.293,
                                                   NEG 5 ZERO 0 POS 3, det -3840
TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION         C   FAIL iff det G_6 < 0 and det K <= 0
TM-HANKEL-K3-QUADRATIC-INVARIANT-SUFFICIENCY   C   factors through the invariant map
evidence: probes/P-TM-HANKEL-K3-TRANSFER-1, bundle sha256 364f459a...
canon section 9; no dependencies, no gates, no frontier queue entries
```

## Release chain and the fired activation gate

```text
issue #338       claim lock for the fold
PR #339 MERGED   release/canon-v42: content 6d42c26 + activation b8309c6;
                 both architecture jobs and aggregate check SUCCESS
tag canon-v42    FIRED at the publication readback: canon/CHANGELOG.md
                 carried the generated count marker pair twice (the v41
                 entry kept its markers). Blocker text: "lacks the
                 generated current count block". The repository rule
                 protect-canon-releases (deletion, update, non_fast_forward
                 denied, no bypass actors) makes the tag permanent; it
                 points at d7751ee as the archived record of the firing.
                 No v42 release exists and none can.
PR #340 MERGED   readback repair attempt inside the v42 designation:
                 correct content, but the tag could not move, so v42 could
                 not activate under its declared tag.
DECISION         do not weaken the tag ruleset; the machine-enforced
                 immutability is part of the public commitment. Re-release
                 the identical content under the next integer.
PR #341 MERGED   release/canon-v43: content 320324f (title v43, CHANGELOG
                 entry retitled with a plain record of the consumed v42
                 tag, seven HISTORY events on canon-v43, views, SUMS) +
                 activation e97291b (exactly STATUS, README, CITATION).
tag canon-v43    publication readback SUCCESS; draft release assembled
                 from the tag-job manifest, assets validated byte-identical
                 after download, published; release-event validation
                 SUCCESS.
```

Lesson pinned for future folds: the local dress rehearsal must include
`tools/check_activation.py --full` (the only check not covered by policy,
canon, ledger, labels, unit tests, and the probe sweep), and an outgoing
changelog entry hands its generated-counts markers to the new entry.

## Canon text location

CANON.md section 9, subsections "The Hankel divisor block of c_TM" through
TM-HANKEL-K3-QUADRATIC-INVARIANT-SUFFICIENCY; changelog entry
"Public Canon v43". Probe and note unchanged on main:
probes/P-TM-HANKEL-K3-TRANSFER-1 and notes/C-TM-HANKEL-XOR-DEFECT-1.md.

## Open lane, now unblocked

The k = 4 successor C-TM-HANKEL-K4-SUBSTRATE-1 was held until the fold was
fixed on the public line. That condition is met: the freeze can now target
Public Canon v43 rows TM-HANKEL-K2-TRANSFER [T],
TM-HANKEL-K3-UNIVERSAL-TRANSFER [F], TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION
[C] directly, with no incubation-note dependency. Frozen first question per
the owner: the minimal invariant information needed to decide the k = 4
transfer on the 65-cell substrate with its S_4 decomposition
10[4] + 12[31] + 5[22] + 3[211]; no inherited two-scalar or rigidity
hypothesis.
