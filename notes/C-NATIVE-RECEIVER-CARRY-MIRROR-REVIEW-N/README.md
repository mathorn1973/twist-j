# Independent review of the native receiver and marked carry mirror

**NON-CANONICAL / L1.** Target:
[PR #1884](https://github.com/mathorn1973/twist-j/pull/1884), probe
P-NATIVE-RECEIVER-CARRY-MIRROR-1, exact head
`c9bd0bc5ac97ad034be399e6619695c7fc2c4a61`. Review lock:
[issue #1885](https://github.com/mathorn1973/twist-j/issues/1885).

This is the independent mathematical review requested before any v109
fold. Its outcome:

- **No mathematical error was found.** All four declared review scopes are
  accepted at their stated scope.
- **Nine wording corrections, E1 to E9, should enter any Canon text.**
  Three matter most:
  - **E2:** the opposite paired carry character is the single fact
    (2/5)=-1. Its "agreement" with the native readers is a convention.
  - **E8:** the next-precision discriminator is minimal only among readers
    of the carry alone, because the two-digit device's own (output letter,
    carry) pair separates J and J^-1 already in F5.
  - **E4:** the compiled "inverse multiplier" is the literal reverse of the
    forward word.
- **A code-independent checker passes every frozen check, R1 to R11.**
  These include checks stronger than the target audit:
  - trace closure on all 5^6 states;
  - the compiled occupied circuit on all 625 states, with a literally
    executed second pass;
  - the 125 zero-trace controls through the full 62-cell device.

## Files

| File | Content |
| --- | --- |
| PREREG.md | Exposure, source boundary, frozen checks R1 to R11, failure rules. Frozen at `5ea45c5` before the checker existed. |
| review.py | Code-independent checker, pinned at `c6855cb` and read back publicly before its only execution. |
| EXPECTED.txt | Exact stdout of that execution. |
| RUN.md | Pin, readback, command, environment, exit, byte counts and hashes. |
| MATHEMATICAL-REVIEW.md | Code-free section-by-section review with verdicts, E1 to E5, and the post-run addendum E6 to E9. |
| CI-AUDIT.md | The target's actual x86_64/aarch64 science-job logs, the merge-tree identity and the runner pass conditions. |
| RESULT.md | Verdict table, execution summary, post-run comparison and limits. |
| SHA256SUMS | Hashes of the files above. |

## Replay

The target is not merged into this branch. Obtain a clean checkout of the
target scientific pin `aaf3ec7e925c2c0261604179ee4166d542233e14`. Then run,
from the repository root:

```sh
python3 notes/C-NATIVE-RECEIVER-CARRY-MIRROR-REVIEW-N/review.py \
  --compiler PATH/TO/probes/P-NATIVE-RECEIVER-CARRY-MIRROR-1/arithmetic_compiler.py
```

Once #1884 is merged, the default path works and `--compiler` can be
omitted. The checker hash-binds the compiler bytes, so the path does not
affect the result. It uses only the Python standard library and reads no
other target file. Its stdout must equal EXPECTED.txt byte for byte.

The review changes no probe, registry, Canon or release. Accepting it, and
any v109 fold, are decisions for the Canon owner.
