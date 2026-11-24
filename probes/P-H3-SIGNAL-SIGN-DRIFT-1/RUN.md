# Exact execution

A clean public checkout was checked against all fourteen blob IDs in the remote Git tree before the Linux run. The verifier emitted six deterministic JSON records.

```text
pin_commit: 24c0428adf37b937c42ea90594eaa562d5eb9fc6
command: python3 probes/P-H3-SIGNAL-SIGN-DRIFT-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: c3b3215a0e86fc0918c51f067db436467e9b6852890e27c6c203d518ff3a2bf2
started_utc: 2026-11-18T17:30:50.755936+00:00
ended_utc: 2026-11-18T17:30:54.471630+00:00
exit_code: 0
stdout_bytes: 48483
stdout_lines: 6
stdout_sha256: 537ff0f5fbf205d6ac87b234ea9338f94e5bfe50caf34ce417e16f1cd0456914
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Frozen inputs

```text
2c328a4a41b314851e692a5016975adfb119d58e24dd3176eeee85de1ff74f8d  PREREG.md
29b43625468c78904fa28d88807d424f1adc3b13c42ed5aa327461f8b1e9edf9  anchor.md
763d3470b06d24c3710bf5bce4815ae756c906622629f240b4a86f58e244f427  anchor.py
4ed8d364f4ed77c7c5f970343b8d1eaf4752cd82775c596773b580c6ed4d0873  bulk.py
131fd34da56e0f526b05de17fb24912d2d8416b5cd73947bf15c676da51233ec  calibrated.md
1822e46485ac5c8b621d6628e330088e87d255f8929b0704828ba80a561a6f46  calibrated.py
c78273b2b181574e036b5a87198e2c90368a74bda5fbdf4901d3deb8c9c57a0a  charge.md
cf3eb3935a161f2aa0a0562dc51fe4d9e6074fed0089ef48affb18c176bd5f20  charge.py
93b03400d189674b7827615f374d2aad8ec6caa5ff45b6b22f269a321e9aac4e  drift.md
4b9fea26af9c9a244d744b3890569040067972fb1d37aef995bd3cdc76c5e493  drift.py
29da7166e1adb9434541bcea60abd37cca3e9e9b8150805adb4ca366c191c0f8  light.md
5f98a07673fe6ea6a443cbbeaffbbc077b2ea47ba8e894ba57929c81a66c262a  light.py
43993ffb88ba678df0b4ca75fc5ec3549943276aa9872eb88438449eee294b09  native.py
c3b3215a0e86fc0918c51f067db436467e9b6852890e27c6c203d518ff3a2bf2  verify.py
```

The preserved result contains the complete finite observations, including unsuccessful transfer tests and bounded-horizon cases. The secondary changed-resident calculation in the results is a separate algebraic consequence.
