# Run P-D3-ZWORK-VAR-BOUND-1

The public preregistration and verifier were pushed to
`origin/probe/P-D3-ZWORK-VAR-BOUND-1`, freshly fetched, and read back at the
pinned commit before the first formal invocation. Both file digests matched
exactly immediately before execution.

```text
pin_commit: c23c7b1e7c0f5cd71d1cdd74f2185653c61fe3d4
prereg_sha256: 7db2de85786d45adfa048162a2b97c0683e8069bb8044d46f4b837680c2496ed
prereg_bytes: 17769
verifier_sha256: faf10b8b933ce3975ec547c1d40fe5cd10320d17b421c568efb276073feeee09
verifier_bytes: 37915
command: python3 probes/P-D3-ZWORK-VAR-BOUND-1/verify.py
platform: Ubuntu 22.04, Linux-compatible WSL2
architecture: x86_64
python: 3.10.12
started_utc: 2026-11-20T16:26:05Z
exit_code: 0
stdout_sha256: aa47b896720474f252f510dbe614add4676ea740376d7fad05a747c918448057
stdout_bytes: 1785
stdout_lines: 20
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The environment fixed `LC_ALL=C`, `LANG=C`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1`, and `TZ=UTC`. Python optimization was disabled and
the 600-second guard did not fire (wall time ~9.7 s). `EXPECTED.txt` contains
the exact LF stdout bytes from this run (also cross-checked byte-identical
under Python 3.12.10 on Windows x86_64 with zero stderr bytes).

This is the local x86_64 run. Two-architecture reproduction is confirmed only
after both hosted GitHub Actions jobs (`architecture-x86_64` and
`architecture-aarch64`) pass on the same pull-request commit against the same
committed `EXPECTED.txt`.
