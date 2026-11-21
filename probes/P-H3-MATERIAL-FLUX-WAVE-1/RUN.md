# Exact execution

The clean public preregistration checkout was compared with all eleven blobs returned by the remote Git tree before execution. Inputs below are SHA-256 of the pinned bytes.

```text
pin_commit: 57db6748e672440aae43abf944c88a6e29867d95
command: python3 probes/P-H3-MATERIAL-FLUX-WAVE-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 2c6efe6820c6be9ed0db48b7e4da8de6dbe3106272b788aa9b29f59f22f37a18
started_utc: 2026-11-18T17:14:13.247775+00:00
ended_utc: 2026-11-18T17:14:13.905207+00:00
exit_code: 0
stdout_bytes: 19534
stdout_lines: 5
stdout_sha256: 30837c1d016697ee572afb5652e1c6bb18fb59820e64cc323845a75e350d00bc
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Frozen inputs

```text
41f4fab61563d3d53087706c735af8b2cf8a8a3e800d29189ea667bf1c9b3e8b  PREREG.md
6ae22c9f5347dfc822e3c9bc572d3a1c2d669cac549e04d0f8adae1432395c94  flux.py
545f091a853936c474e5a43c7a59c0a96e3644f26fabf483631ffa803879e37d  flux_protocol.md
5b8006bb04ecfb2c42b5af2f3fcf52609011c4fec087700c8ee1f938f90496f9  matter.py
80693f2662cb6c59b110dc0654663c2e17c8f375e01c418d62ef4e5b2e994988  matter_protocol.md
43993ffb88ba678df0b4ca75fc5ec3549943276aa9872eb88438449eee294b09  native.py
856cd0df0d573531da605b4cea394b8f6daf54a9afce5297f545f2e0354fa2a3  packet.py
b39e9511e6241aac78ff4fd9cf98972b5f3a93b6560f1931bb0496fe39931d5d  packet_protocol.md
9b957d920f43de300f13d6b936f1e5017294bea51cc7f3ae825520b5f5993f95  recoil.py
c4ab986f9ad82962cbe71f32701432f11f1c8019136226affc6b1cdf97921f9b  rigid_packet.md
2c6efe6820c6be9ed0db48b7e4da8de6dbe3106272b788aa9b29f59f22f37a18  verify.py
```

The five exact JSON records correspond to the directed current, wave packet, independent sign, localized matter and momentum tests.
