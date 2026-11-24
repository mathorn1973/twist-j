# Formal run of the short Gauss word and clock

The preregistration, proof and accepted verifier were published in a single commit. Remote branch readback confirmed the exact commit before execution. The hashes below were checked on the three inputs immediately before launching the verifier from the repository root.

```text
pin_commit: a54d76bf8e3c4d78cf1b79dac0bebda54c0cd13e
public_base: 93c36089db57032a6cbca482ff62c95884567d0f
prereg_sha256: 1f14e00ab41ba800d594e531970d63ed60650400e5e2ef5b06aef380b35b9656
proof_sha256: 8f9ff8af354f7bbb75ba9940152398579c2fed260fb99781e122986a2e6c2409
verifier_sha256: 5d5962cca704b30c6ce3dd81b3ec37bea4689e7b0aadfff8d1382db7a8f1db15
command: python3 probes/P-QDD-SHORT-GAUSS-CLOCK-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 88d89de55a87e718d7f21de2f912e9ab2a4b16733048fa5a740aa92cc632574e
stdout_bytes: 286
stdout_lines: 4
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The first formal run used LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. EXPECTED.txt is a byte-for-byte copy of the process output. All inputs and forecasts were public at the pin.
