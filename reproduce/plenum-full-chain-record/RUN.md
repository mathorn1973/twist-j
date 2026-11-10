<!-- SPDX-License-Identifier: Apache-2.0 -->
# First public-source reproduction

Source pin: dc6db4a6adf0c02f952f7bf4ba714ab1a91c42a6.
The public branch was fetched and its exact source bytes read back before
execution. The checkout was clean before and after this run.

    command: python3 reproduce/plenum-full-chain-record/verify.py
    working directory: repository root
    platform: Linux
    architecture: x86_64
    Python: 3.10.12
    started UTC: 2026-11-10T11:34:50.734758+00:00
    elapsed seconds (measured): 1.571995
    timeout seconds: 120
    exit code: 0
    stdout bytes: 328
    stderr bytes: 0

Environment: LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. Python integers are unbounded.

| Object | SHA-256 |
|---|---|
| verify.py | 6d96fb462a869f832948083810272f5ec3e10adcc46cfc4233cf8b5d26992dcd |
| certificate.json | 80a21b34b74b8c0bc5bf9e1c92782f8a4fdc2bc41c289029184d2ce33be2182c |
| stdout and EXPECTED.txt | 5fb4c907ac3a372a2d9c943a61009891a4d507872cd4619fb3af350948bd5986 |
| empty stderr | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

The actual stdout is byte-identical to the exposed prediction frozen in
EXPECTED.txt at the source pin. No source, fixture, guard or expected byte
changed after execution. The computed canonical reference digest is
6c8b7aee1a9f955d7bb9b5edf4c37034079957cb674355bbf185e983837de69c.

This is the first execution of this public Python implementation. Historical
author runs and a narrower independent endpoint check are separate evidence.
Static internal review is part of this preparation session and is neither
an execution nor external acceptance. Public acceptance additionally requires
the unchanged verifier and stdout to pass the required PR-head x86_64 and
aarch64 jobs with Python 3.12; their workflow logs are the architecture receipts.
