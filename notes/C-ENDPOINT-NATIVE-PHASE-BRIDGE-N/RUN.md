# First exact phase/native audit

NON-CANONICAL, one architecture only. Candidate-C finite arithmetic; native Hamiltonian bridge NOT DERIVED. No corrective execution.

The complete contract, proof and source were pushed and publicly read back by Git blob and byte count before this first execution.

Command: `python -I -B audit.py` from the note directory, through an external subprocess with an enforced 45-second timeout. Environment: `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`. Source has explicit LF byte output.

```json
{
  "architecture": "AMD64",
  "elapsed_seconds": 0.765,
  "exit_code": 0,
  "passed": true,
  "pin": "effe7a6a1c08b6925f9308f4f7e29c8266c64c19",
  "platform": "Windows 11",
  "python": "3.12.10",
  "source_sha256": {
    "CONTRACT.md": "338f4b2879f879bad19ffc1a20b418115035782b3b526900ccce4162b27a8144",
    "PROOF.md": "62eabf248b6dc4cda8abe6e7dc6910ea8c3491104889e06697db96f80ceebda8",
    "audit.py": "d3633815e6dd68a9859dddfae3e46667cb47d13e4abde0472dfb3b8c66fe1cbf"
  },
  "started_utc": "2026-10-07T21:01:07.892813+00:00",
  "stderr_bytes": 0,
  "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "stdout_bytes": 2346,
  "stdout_sha256": "b78b4200d71037163aadde1fbc2d103e2f5c346765d6b80791259f27c7a89842",
  "timed_out": false,
  "timeout_seconds": 45
}
```

No formal public P-probe, second architecture, experiment or physical acceptance is claimed. Ordinary repository CI does not execute this notes audit. The source files remain unchanged from the public pin.
