# Run record: P-QDD-U-NATIVE-READBACK-1

```text
pin_commit: 82da7e5aba4d22fe570e5d8432cbcc325077d451
verifier_sha256: 3e8281942278b420c4406a7f848e8e8c568bf6beec9b9c694948ec760623b5f7
command: python3 probes/P-QDD-U-NATIVE-READBACK-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 2e1d4367ec647e32765a1e97784cfe7928c8a57b02e9fdfd5891ae4f1bce189b
stdout_bytes: 2323
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

## Pin audit

```text
pin_parent: a6e5e0fa21fbdb34213b035b889de12d9923a828
public_claim_lock: issue 859
formal_date: 2026-09-06
started_utc: 2026-09-06T09:17:51.108781+00:00
prereg_sha256: e6bae7c43a44990093a3170992d0a64af749a7d201441984d483b27788af090f
prereg_bytes: 15313
proof_sha256: 2df18b2118d0a2e483c8089976eda8485127951efa9e2f3364d38ac2aab0d76c
proof_bytes: 12710
verify_sha256: 3e8281942278b420c4406a7f848e8e8c568bf6beec9b9c694948ec760623b5f7
verify_bytes: 21468
```

The three accepted files were committed, pushed and read back through the
public GitHub Contents API before the first formal gate. Their exact hashes
and sizes matched the independently reviewed candidate. Public custody was
recorded in issue #859 before execution.

A separate clean Linux checkout fetched the exact pin, verified its parent,
Canon source hash and all three pinned file hashes, then ran the displayed
command once from its repository root. stdout and stderr were captured as
separate byte streams. The accepted verifier completed all nine groups with
1533811 exact checks, zero mismatches and no exception. EXPECTED is the
entire actual ASCII stdout, including its final LF. The checkout remained
clean and all pinned bytes were unchanged after execution.

This is one x86_64 run. It does not alone satisfy the two-architecture gate.
The required PR workflow must reproduce the same accepted bytes and the same
EXPECTED on clean GitHub x86_64 and aarch64 jobs with Python 3.12.

The written proof and prior private computations were disclosed before the
pin. This run audits exposed exact results; it is not a blind prediction.
No private logs, hostnames or execution paths are part of the public record.
