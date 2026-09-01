# RUN

## Immutable pin

```text
pin_commit: 7410a86613a5314fbfd5acbc071eaf246f18b40c
verifier_sha256: 37cd038c1a9e6ff8bf5ba485d2a69ea0c7b735e9e224c117797b7740b12eb239
```

## Command

```text
command: python3 probes/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1/verify.py
```

## Local execution record

```text
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: f7726dee73a3d29023220609c1dc5102cce63d59e0394243b95c4dc716144729
stdout_bytes: 460
stdout_lines: 15
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Environment

```text
environment: env -i PATH=/usr/local/bin:/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC
run_date: 2026-09-01
public_issue: #738
```

## Pinned input integrity

```text
verifier_bytes: 9533
verifier_git_blob: adb67f774fab855d74639fdd6ab46d419761f55c
prereg_bytes: 14298
prereg_sha256: 2d680f068c68b7ec653a630a454fb165a1fe5915b6445067d6ffe92a2f2b85b7
```

## Output integrity

```text
expected_match: byte-identical
```

This is one exact x86_64 execution. The candidate-`T` ceiling is supplied by
the independent written proof in `PREREG.md`; the run is a finite certificate
audit. The pull-request checker reruns the same pinned verifier and compares
exact bytes. No second architecture is claimed in this record.
