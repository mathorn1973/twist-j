# Exact execution and source custody

PUBLIC / NON-CANONICAL, L1. No Canon status or authority is created.

## Pins and pre-execution conditions

- Public base: `b8ba1a07ad776cdd8d878fe0a407e07312c0e263`.
- Preregistration: `9a6f128172c9efa37f77ca05e1861a9d6f241845`.
- Joint proof/code/reproduction pin: `a3ed51b35ba472f200946227ebf2efc2ec43d349`.
- Both pins were pushed and their remote heads read back before scientific
  execution. Public main remained the stated base at the code-pin readback.
- No pre-pin scientific execution, import, dry run or scratch calculation
  occurred. Only symbolic derivation, static reviews, administrative hashes
  and AST parsing preceded the joint pin.
- Immediately before launch the checkout was clean and all seven pinned
  files matched their committed blobs byte for byte.

## Frozen scientific/input files

The first four filenames are in this notes directory. The final three refer
to the matching standard reproduction directory.

| file | bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 18507 | b3ad38c5af85519c8cdc9e8dbbd1a5549c6d6c28046caf85b9f3e2be48c39fc4 |
| verify.py | 17957 | afbeac83be5fd7b51a57fac1172f3d0be9a4680ec2376756940a166eccb8ad77 |
| break.py | 23106 | 563a194210deeca40dccf170a90cca1880cbeac88af8b1c60293ddb89e5735ab |
| PROOF.md | 22475 | 3b5889395b39c1699c362b3ee26a61a8870a25f291be2d4057841aa69ebb9e09 |
| reproduce verify.py | 1001 | d30a30d1c68e5aff399ea97e691f0016a25a5ea0e99117621be7337a4ada7a43 |
| reproduce EXPECTED.txt | 288 | 7aa6e086bf3fd7c43ffea5ac4eae27940a1ceee644231ac4ee7d2fcec922c4e1 |
| reproduce README.md | 1841 | 8ece55a99450c5c80136987e0cdfc7f077e0d9f0053538716c28080dbdda7fa1 |

## First local run

Started 2026-10-01 07:50:57 UTC. Fresh environment readback confirmed Ubuntu
22.04.5 LTS, x86_64, Python 3.10.12 standard library, WSL. From the clean
joint code-pin root, the unchanged repository command was:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

The runner set LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1 and enforced its 120-second limit for the entire
bridge. It executed BOTH independent programs and observed exit 0, empty
stderr and exactly 288 scientific stdout bytes matching EXPECTED.txt.
This is the first observed agreement with the prospectively frozen target;
the target was not labelled measured before this run.

The enclosing command exited0 with empty stderr in 8.017 seconds. Its exact
stdout is RUNNER.txt, 178 bytes, SHA-256
`10800334e971836c16497bf5b3d899763f69b18d16bcec02e4072aabf146eb3a`.
Empty stderr SHA-256:
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The five scientific lines are preserved in the reproduction EXPECTED.txt.
RUNNER.txt preserves the unchanged checker's exact PASS receipt with wrapper
and expected-output hashes. No scientific source, proof, target or scope was
changed after pinning or after this execution.

## Public computation gate

PASS: [PR #1308](https://github.com/mathorn1973/twist-j/pull/1308),
[run 36833055038](https://github.com/mathorn1973/twist-j/actions/runs/36833055038),
head `66ed5056f21852f8fe17ecf268cc3f6c31827993`. This head adds only the
run/result/review/custody records after the unchanged joint source pin.

| job | Python | conclusion |
| --- | --- | --- |
| [x86_64 / 110273867352](https://github.com/mathorn1973/twist-j/actions/runs/36833055038/job/110273867352) | CPython 3.12.14 | success |
| [aarch64 / 110273867154](https://github.com/mathorn1973/twist-j/actions/runs/36833055038/job/110273867154) | CPython 3.12.14 | success |
| [aggregate check / 110274044092](https://github.com/mathorn1973/twist-j/actions/runs/36833055038/job/110274044092) | n/a | success |

Both actual architecture logs were read after completion. Each contained
exactly the same scientific receipt:

```text
REPRODUCE PASS FIELD-TWO-CELL-ENERGY-TRANSFER-N d30a30d1c68e5aff399ea97e691f0016a25a5ea0e99117621be7337a4ada7a43 7aa6e086bf3fd7c43ffea5ac4eae27940a1ceee644231ac4ee7d2fcec922c4e1
```

Thus both required architectures executed BOTH pinned implementations with
exit 0, empty stderr and the same 288 scientific stdout bytes. This is actual
scientific replay, not an inference from green documentation checks. The
publication job was correctly skipped; no release was requested or performed.
The subsequent reporting update leaves all seven pinned inputs unchanged.

This uses the ordinary ACTIVE repository reproduction workflow, not a
GENESIS staging lane or a fabricated formal probes/P-* run record.
