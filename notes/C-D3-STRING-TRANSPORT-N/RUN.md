# First execution and custody record

NON-CANONICAL. Reservation #1410. One scientific run only.

Public pre-execution pin: `56d0baaa08d92691582c7372905c680e1757417e`.
Pinned tree: `834e3c6cdc0bf870be1d6c84da4598d9906a550a`.
Base: `7d7f588c42422c2cf37b04d76ebc13ca55eb96dc`.
The public directory readback confirmed all three pre-run Git blobs and byte
counts. Pre-execution receipt: issue #1410 comment 6045220210.
CONTRACT.md, PROOF.md and audit.py remain byte-identical to the pin.
Only static py_compile was run before the pin; it did not execute the audit.

## Environment and command

- Platform: Debian GNU/Linux 13 (trixie).
- Architecture: x86_64.
- Python: CPython 3.13.5.
- Start: 2026-10-07 19:26:26.524555 UTC.
- Command from this note directory:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 -I audit.py
```

A parent subprocess.run enforced timeout=45 seconds. The engineering elapsed
time was 1.943839533 seconds. Exit code 0; no timeout; stderr empty; stdout
2944 bytes, retained byte-for-byte as EXPECTED.txt. No retry occurred.
The empty stderr SHA-256 is
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
Only original English prose and standard-library integer code are published;
no private infrastructure, secret, binary, or third-party archive is included.

## Byte identities

| File | Bytes | SHA-256 |
|---|---:|---|
| CONTRACT.md | 6230 | `a808f670ae499828e6192766560071203c51037bf532cc35b6e62f7e8c2f0585` |
| PROOF.md | 13265 | `955c62029282ea3d7d8334f7e7be9e6459fae46942140f045915f1a75ac23525` |
| audit.py | 9558 | `0ebd81fdc06b9e71cd14f2f5f5cfc4009da6423e772353b42155f2dc30218780` |
| EXPECTED.txt | 2944 | `66825e554fa2a323aa42620154b6f995ba55b758e8f2bbb9fc2ff69facafde99` |

The actual stdout is the result, not a pre-computation claimed success.
Its domain and negative controls were specified by the unchanged contract.
The mathematical proof was complete and public before the first audit.
Code route agreement is same-author reproduction, not independent review.

## Evidence boundary

No external machine, independent reviewer, or second architecture executed
this scientific code in this session. Repository policy/Canon/ledger/gate
CI is separate and does not execute scripts under this notes path. Such
CI must not be counted as a second scientific run of the candidate.
New-PR CI will be recorded in the PR/issue publication receipt, without
rewriting this immutable first-run record.

Original text and code: Apache-2.0. The author's temporary GitHub noreply
commit-email authorization is used. No Canon or physical status is promoted.
