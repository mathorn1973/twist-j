# C-J-UNIT-STRIP-DECODER-N run record

Status: NON-CANONICAL incubation audit only.

## Frozen source

- Public issue: #1269
- Branch: `notes/j-unit-strip-decoder-20260928`
- Pin commit: `4149687700e2c022176b1b5a7d11e81ff9d3304d`
- Parent main: `b648e2dfb8ea8f1519e8e0a6e139c0bb49676ade`
- `PREREG.md` Git blob: `d9b1e3251bb42d1574cc5fac2b4150851405cbdc`
- `PROOF.md` Git blob: `ab16a046daee6ab0de23b739115b4545be6d74db`
- `verify.py` Git blob: `39bd19cfcec6ede6de439e9d402586228b27950f`
- `break.py` Git blob: `a6a06c1850cdd7df0dce7f150666a29df9ec2364`

GitHub public readback of all four frozen files matched these blobs before the
accepted execution.

## Custody note

One earlier local attempted execution is explicitly excluded from evidence:
the local `verify.py` and `break.py` bytes did not match the public pin.
No scientific conclusion was recorded from that attempt and no pinned file,
scope, threshold or equation was changed. The accepted run below was rebuilt
from the public pinned bytes and their Git blob hashes were rechecked before
execution.

## Accepted verifier run

Command:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 notes/C-J-UNIT-STRIP-DECODER-N/verify.py
```

Neutral local environment:

```text
platform:     Linux
architecture: x86_64
python:       3.13.5
```

Result:

```text
exit code:      0
stdout bytes:   470
stdout SHA-256: 6ba93a2bf47821bc103fc6d484dd7920fb9e81e689d1bf3d3ca9f9e436dfd6b4
stderr bytes:   0
stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Stdout is preserved byte for byte in `EXPECTED.txt`.

## Breaker run

The breaker is a separately implemented same-session attack. It is **not**
blind independent confirmation because the same authoring session had already
seen the verifier and result.

```text
exit code:      0
stdout bytes:   306
stdout SHA-256: 54f7fd3271d49dc3de2759bc804164294b0d18a54bcedee8c68f502d1966f8dd
stderr bytes:   0
stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Stdout is preserved in `BREAK_EXPECTED.txt`.

## Evidence ceiling

This is one x86_64 local lane in a notes-only, result-exposed incubation.
It does not satisfy the repository two-architecture computation gate and is
not a formal public probe. The finite numerical counts remain candidate-C.
Written universal arguments remain candidate-T until a separately reviewed
promotion path accepts them.
