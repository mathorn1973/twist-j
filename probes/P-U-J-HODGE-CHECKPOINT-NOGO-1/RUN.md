# RUN: P-U-J-HODGE-CHECKPOINT-NOGO-1

pin_commit: c87aa8e40b9d1fccc7eae91675fc46dbede351a9
verifier_sha256: cc433c0394801ebb5dd069a2f1f1f79d519d2db1a573d13343168dc418aaf38f
command: python3 probes/P-U-J-HODGE-CHECKPOINT-NOGO-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: b08c1aef7d6277a5451037b7d3a95ea68345f16ab0dd5181ae445adb2c638ef7
stdout_bytes: 418
stdout_lines: 14
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

prereg_sha256: 3144e1ec1ebdf9a880610536a558fa18b5a908507f0f5c076c14894059dc23e5
proof_sha256: 05271631e84f7260bf0afb41e011ca7a44fe70f4cf18b34e7c86aaaa97b07eb0

The first scientific execution followed the public three-file pin and
Git blob/size readback. This is a sparse self-contained local runtime,
not a full Git checkout. The prescribed repository-relative command was
executed with LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0 and TZ=UTC. EXPECTED.txt contains its actual stdout.

This record witnesses one x86_64 lane only. No independent-agent review
or two-architecture acceptance is claimed here. The required clean GitHub
x86_64/aarch64 jobs must run tools/check_verifier.py on the unchanged
source and compare this output. Full repository checks were not run locally.
