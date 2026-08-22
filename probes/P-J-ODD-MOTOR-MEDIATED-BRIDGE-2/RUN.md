# P-J-ODD-MOTOR-MEDIATED-BRIDGE-2 formal run

Status: **LOCAL FORMAL RUN COMPLETE. GITHUB TWO-ARCHITECTURE GATE PENDING.**

```text
claim issue:          #527
branch:               probe/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2
pin commit:           835d68c9c451cc1a8a62f6ff1437450b909d24d5
pin parent:           7a0fb56e44e652879aec1cc188a8867c63f39577
layer:                L1 exact arithmetic only
result exposure:      RESULT-EXPOSED
```

## Pin and public readback

The two accepted blobs were created before the pin and their Git blob IDs were required to equal local `git hash-object` before either was referenced by the pin commit.

```text
PREREG.md
  git blob:           98e4906240edfeb3c62dc4ddf52ba1bdf04d16bf
  sha256:             6a6b28d9a6d304bcb082726a5e5fb9b27adc2e0953642b97978a35efcb60b05e
  bytes:              7332
  LF lines:           206
  final LF:           yes

verify.py
  git blob:           475e17e347b66cf8e0328b47a1976753e5456c70
  sha256:             78b5ae47fbede9449e0a7c706dc12e00661a0d3d63227c57ee6a35de84f3ef42
  bytes:              6686
  LF lines:           148
  final LF:           yes
```

Both files were read back from public GitHub at the exact pin. The returned blob IDs matched the pre-pin accepted blobs. The verifier executed below was reconstructed from those exact accepted bytes and rechecked to the same Git blob and SHA-256 before execution.

The predecessor identifier `P-J-ODD-MOTOR-MEDIATED-BRIDGE-1` stopped before execution on a readback mismatch and supplied no evidence to this run.

## Environment

```text
platform:             Debian GNU/Linux 13
architecture:         x86_64
Python:               3.13.5
```

No machine nickname is recorded.

## Command

Executed exactly once after pin and readback, in an emptied deterministic environment:

```text
env -i PATH="$PATH" PYTHONHASHSEED=0 LC_ALL=C LANG=C TZ=UTC \
  python3 probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2/verify.py
```

## Outcome

```text
exit code:            0
stderr bytes:         0
stdout bytes:         499
stdout lines:         15
stdout sha256:        6d81ea8c28b55912d63e6a35b3aa19ded5bb3648dc82925bf0026e41fbb4a072
stdout git blob:      9284faaab4a6fa94345df6cdd9e8d0dd265e1e88
decision:             MEDIATED-BRIDGE-CERTIFIED
```

`EXPECTED.txt` is the exact stdout of this single formal local execution.

This x86_64 run alone does not satisfy the public two-architecture computation gate. The pull-request workflow must reproduce the same pinned verifier hash and byte-identical `EXPECTED.txt` on x86_64 and aarch64, then pass aggregate `check`.
