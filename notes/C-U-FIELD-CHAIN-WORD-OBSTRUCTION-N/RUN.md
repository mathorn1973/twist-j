# Pinned finite self-audit

NON-CANONICAL / candidate-C. One scientific architecture.
This run audits the written identities at its declared finite scope.
It is not an independent proof, blind confirmation, or a formal P-probe.

## Source custody

pin_commit: dfbe4ef237e9fbf07f5e1886a5af9721a7b869a9
verifier_sha256: bfdb5a3fdfd6f47cc55fd5f7c37e4c645b8da04ab248052487968253973f11ae
verifier_bytes: 7681
contract_sha256: 0a8c7ffaa3956bf1e902492ad846542bcdd6115d85faddfad0dc5dfb9d34d547
prereg_sha256: 8ce88a53af227786805cfa2e5d80065e90d23b1cca4dd34277be1aaa9401e280

All six pinned files were downloaded from their immutable public GitHub
URLs and compared byte for byte before the first scientific execution.
The pin receipt is issue #1590 comment 6240686403. The remote branch
matched the pin and public main remained dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.

## Actual execution

platform: Linux
architecture: aarch64
python: 3.11.2
started_utc: 2026-10-17T20:41:53.078049+00:00
completed_utc: 2026-10-17T20:41:54.208239+00:00
exit_code: 0
stdout_bytes: 343
stdout_lines: 6
stdout_sha256: 98ad401f1f49d8fa6ca0fb8c533a7885ed00f6f9ef92da3c74040d972d929f87
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

From the repository root, using the unchanged repository runner:

```python
from pathlib import Path
from tools.check_reproduce import reproduce
reproduce(Path('notes/C-U-FIELD-CHAIN-WORD-OBSTRUCTION-N').resolve())
```

The runner emitted:

```text
REPRODUCE PASS C-U-FIELD-CHAIN-WORD-OBSTRUCTION-N bfdb5a3fdfd6f47cc55fd5f7c37e4c645b8da04ab248052487968253973f11ae 98ad401f1f49d8fa6ca0fb8c533a7885ed00f6f9ef92da3c74040d972d929f87
```

The successful runner requires exit zero, empty stderr and scientific
stdout byte-identical to EXPECTED.txt. Its deterministic environment and
timeout are defined by the pinned tools/check_reproduce.py, not duplicated
as a new runner policy. The outer timestamps are administrative metadata,
not part of the scientific stdout.

No code, target, finite scope or expected output changed after this run.
There was one scientific execution, with zero assertion failures. Ordinary
notes-only pull-request checks do not select this notes verifier; passing
such checks must not be described as a two-architecture scientific replay.

## Exact scope of the finite evidence

The audit checks the field certificates, zero-origin native prefix,
all 25 gate residues under all five field phases, all twenty canonical
unit seeds, and 5760 complete continuing forward fixture steps, each with
its exact inverse and full energy/charge/defect accounts. The fixtures
cover two chain lengths, three common occupied-state preparations and two
cut settings, for twelve contexts, with 24 steps per unit per context.
It checks full nonsource equality, not just a first output. The differing
energy control returns receiver resources 2 and 14. The outside-alphabet
signed exchange is labeled as a control only.

Universal all-word and all-time conclusions rest on PROOF.md. The finite
PASS alone does not quantify over all words, energies or preparations.
