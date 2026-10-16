# First exact geometry execution

pin_commit: a96646c22267d59179a5a96a161c5f6f95ba6255
command: python3 probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/verify.py
platform: Linux 6.6.87.2-microsoft-standard-WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 7850a1ef320738aed5966cad4d9f1f4663b3ae3cabfd328895ce1ebb29d8c8a8
stdout_bytes: 5799
stdout_lines: 718
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
verifier_sha256: 2fcdec303d95782d1b779283eb6aaf238b3ec884b99a8d3aae6142dfb9caf95d

First run started 2026-10-15T10:55:57.144344+00:00 and ended 2026-10-15T10:55:57.427190+00:00.

Clean public pin and prior public readback were verified. The unchanged
600-second limit and deterministic environment from PREREG.md were used.
Exact stdout was captured without filtering; stderr was empty. DOMAIN.tsv
is the literal byte block between the preregistered delimiters in stdout.
No earlier scientific execution occurred in this probe. This first local
run is one x86_64 reproduction lane, not two-architecture evidence.
