# First exact pinned run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.

```text
pin_commit: 9af150e18d2c3749dbe44ff7a5c990b345cc1802
verifier_sha256: 964d7a59d76cc7ff13ec531d79e087dd77d067542fbb9b6548cf4416b3d4cffe
command: python3 probes/P-J-PHASE-PORT-SEPARATION-1/verify.py
platform: Linux 6.12.62+rpt-rpi-2712
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: 418ddd95da7a17c571d19b730f2f18ead763ef4d9b120fb45590d39ed26102d6
stdout_bytes: 1982
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Public pre-run pin/readback receipt: https://github.com/mathorn1973/twist-j/issues/1576#issuecomment-6234746649

Start UTC: 2026-10-17T13:57:36.799643+00:00
End UTC: 2026-10-17T13:57:43.030589+00:00

One first scientific run from the clean publicly pinned repository root,
with LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1. Both frozen runtime files were checked before
import and after execution. The accepted verifier is unchanged.
EXPECTED.txt contains exact captured stdout, not a reconstructed summary.
The run completed within the unchanged 600-second limit.

The five prepared trajectories comprise four ordered phase inputs and
one different second-source control. The existing decoder additionally
derives its fixed operators from its own four basis responses; that is
part of the unchanged source-derived reader. The exhaustive native check
covers 31250 selected steps.

This local aarch64 run does not itself satisfy the two-architecture
gate. The required public PR jobs will replay the same pinned verifier
and compare against these exact bytes. Same-session static review is
not an independent scientific author or a second architecture.
