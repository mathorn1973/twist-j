# RUN

```text
probe:          P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1
formal pin:     7410a86613a5314fbfd5acbc071eaf246f18b40c
public issue:   #738
run date:       2026-09-01
platform:       Linux
architecture:   x86_64
python:         CPython 3.13.5
environment:    env -i PATH=/usr/local/bin:/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC
command:        python3 probes/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1/verify.py
exit code:      0
```

Pinned input integrity:

```text
verify.py bytes:   9533
verify.py sha256:  37cd038c1a9e6ff8bf5ba485d2a69ea0c7b735e9e224c117797b7740b12eb239
verify.py git blob: adb67f774fab855d74639fdd6ab46d419761f55c
PREREG.md bytes:  14298
PREREG.md sha256: 2d680f068c68b7ec653a630a454fb165a1fe5915b6445067d6ffe92a2f2b85b7
```

Output integrity:

```text
stdout bytes:   460
stdout sha256:  f7726dee73a3d29023220609c1dc5102cce63d59e0394243b95c4dc716144729
stderr bytes:   0
stderr sha256:  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
EXPECTED match: byte-identical
```

This is one exact x86_64 execution. The candidate-`T` ceiling is supplied by
the independent written proof in `PREREG.md`; the run is a finite certificate
audit. The pull-request checker must rerun the same pinned verifier and compare
exact bytes. No second architecture is claimed in this record.
