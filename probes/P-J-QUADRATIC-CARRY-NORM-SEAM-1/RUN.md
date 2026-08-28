# Run record

Probe: `P-J-QUADRATIC-CARRY-NORM-SEAM-1`

The flat fields below record the sole completed local execution. This record does **not** certify the probe scientifically: post-run review found a frozen verifier-integrity defect described in `RESULT.md`.

```text
pin_commit: 5efc0beed470118fd2648951d1002b2af195048b
verifier_sha256: 4f8ef488c8fd9af84096bed6a775f69a22d31b9022f1845cdf810f1c4edee580
command: python3 probes/P-J-QUADRATIC-CARRY-NORM-SEAM-1/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: ba6dec1bb3b1ade8a2e65069260e1e6069ff3dc3374b666cd87d6a63b1f36073
stdout_bytes: 1556
stdout_lines: 32
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: 603478498540a9175476afd61416ffa76840ce92377a826bac0382cf2fdfa794
prereg_bytes: 10039
prereg_blob: befb3859bda208973ce4a416803a2f77c9714ad2
verify_bytes: 10701
verify_blob: 898b05c82ea1e401692e581a8e91d5cbed7af4e6
expected_sha256: ba6dec1bb3b1ade8a2e65069260e1e6069ff3dc3374b666cd87d6a63b1f36073
public_claim_lock: issue 620
formal_date: 2026-08-28
formal_start_utc: 2026-08-28T12:07:05Z
formal_end_utc: 2026-08-28T12:07:06Z
```

The execution occurred only after the public pin had been pushed and both accepted blobs had been read back with matching Git object identities. `EXPECTED.txt` is the complete raw stdout from that execution; standard error was empty.

After the run, source review found that the frozen `G4 multiplicativity factor` audit assigned the expected coefficient tuple literally and compared it to the same literal tuple instead of deriving those coefficients from the preceding exact witness data. That violates the preregistered verifier obligation to audit the factor. The identifier is therefore stopped and is not eligible for a two-architecture scientific gate. The stdout is preserved only because the execution completed and policy requires completed-run provenance to remain auditable.
