# Run record: P-ZETA5-RESIDUE-STRIP-DECODER-2

Status: completed first formal local execution.

## Immutable source

Pin commit:

    7f993b5f6375a1d97d705a0bcb42eab12a8dddc8

Frozen file records, publicly read back before execution:

    PREREG.md
      Git blob: e6d0d09888b6c2bcdcfa6e83c063793715e8e69a
      SHA-256: 8b89a068ae2c2831f23614e8872a46c7dabe76ba5e69a568110d441439ae0b43
      bytes: 7254

    PROOF.md
      Git blob: 4bd134d3c86e2f8be5efaa39e659207423e63f5c
      SHA-256: 16001f3c557569474772a4064df28d993063757f3fd1c1d3f6a8105e6b950ea3
      bytes: 8852

    verify.py
      Git blob: 3e352a97f8c85a8f9fe75a1215eda160d655dab9
      SHA-256: 57dfd43f717f008feff825698e2eddb5a5995086bebe2f8c66e2bc1327e5b7da
      bytes: 6877

Before execution the local verifier had exactly the same Git blob and SHA-256
as the public pin and passed Python compilation.

## Command

From the pinned verifier bytes:

    LC_ALL=C
    LANG=C
    PYTHONDONTWRITEBYTECODE=1
    PYTHONHASHSEED=0
    TZ=UTC
    python3 verify.py

The repository-relative formal command is

    python3 probes/P-ZETA5-RESIDUE-STRIP-DECODER-2/verify.py

## Neutral environment

    platform: Debian GNU/Linux 13
    architecture: x86_64
    Python: 3.13.5

## Result

    exit code: 0
    stdout bytes: 962
    stdout SHA-256: 54d5a041141c7e7e50508dca1f286ca5414c9bb3be3bb9991f8ff9456e92bbd2
    stderr bytes: 0
    stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

EXPECTED.txt is the exact first formal stdout, including the final LF.
No frozen source, equation, threshold, carrier or falsifier was changed after
the pin.

This local x86_64 run alone does not satisfy the required two-architecture
computation gate. The pull-request workflow must replay the unchanged verifier
against this same EXPECTED.txt on x86_64 and aarch64.
