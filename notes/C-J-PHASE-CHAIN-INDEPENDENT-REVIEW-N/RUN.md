# First exact pinned run (`C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N`)

PUBLIC / NON-CANONICAL / L1.
Reviewer session: `Antigravity-phase-chain-review-20261018` (`A. M. Thorn <thorn@twistj.com>`, Apache-2.0).

```text
pin_commit: 80d6814a6b7c871b2b46d8e52f764c78c26810b4
base_commit: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
sources_tsv_sha256: a7645b749f3c9c2d8ea43d7d1a098b889f84be3ec75707e5269675bdd22a875c
sources_tsv_bytes: 3703
prereg_sha256: b018beb45c3d9ed92c350889ce698481303634bb1e61e1d56c9242a27ca64a3c
prereg_bytes: 16666
proof_sha256: 01af8ea2b5252730166ac141af6d63d5262eb2c130c33114fb70969be81368c4
proof_bytes: 20751
verifier_path: notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/break.py
verifier_sha256: 9f6dfb3f9bc726dafa5592c0bb49b5037381cd50857a97ab57e1685244b4f928
verifier_bytes: 59496
command: python3 notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/break.py
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
platform: Darwin 27.0.0
architecture: aarch64
python: 3.13.13
exit_code: 0
stdout_sha256: 244903d606fc5767966791bfd9004bed0282d9a04a34a39374a25e18140f34fb
stdout_bytes: 909
stdout_lines: 2
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
elapsed_seconds: 8.103
```

## Execution notes

- The Phase-1 pin (`80d6814a6b7c871b2b46d8e52f764c78c26810b4`) was committed, pushed to `origin/notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N`, and read back before running `break.py` and before opening any target `PROOF.md`, `verify.py`, `RESULT.md`, `EXPECTED.txt`, or `RUN.md` on PRs `#1577`, `#1579`, or `#1581`.
- An initial wrapper invocation picked up the system stub Python 3.9.6 (`AttributeError` on Python 3.10+ `int.bit_count`); no scientific assertion ran to completion and `break.py` was not modified. Running the unmodified pinned `break.py` (`9f6dfb3f9bc726dafa5592c0bb49b5037381cd50857a97ab57e1685244b4f928`) under Python 3.13.13 from the clean repository root exited `0` with `0` stderr bytes in `8.103` seconds and wrote the exact `909`-byte `EXPECTED.txt` (`244903d606fc5767966791bfd9004bed0282d9a04a34a39374a25e18140f34fb`).
