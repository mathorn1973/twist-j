# First formal run

pin_commit: 423c6f7488b35399ff40fcc30be01df526aba795
command: python3 probes/P-FIELD-CELL-SHEAR-CENSUS-1/verify.py
platform: Debian GNU/Linux 12 (bookworm)
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: 9a722d992c12eea57c9de5220c68b02877c688f92da5fd1a5801f15cf27107d3
stdout_bytes: 874
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
verifier_sha256: b863c54fc060aa8ced19a5a6b48f2b1445b6de8915b7da99a7f95e6d2faed2e5
prereg_sha256: b78143ea5a93915e5f6f6886c0076fea93fe22569d5af00c762477d8319fdf51
source_manifest_sha256: cbe7ca144d9e8822d92d375c5684a5826a8f9fedd25c91e817533c3b1d13e7cf
started_utc: 2026-10-16T21:05:36.424455+00:00
completed_utc: 2026-10-16T21:05:36.559939+00:00

The complete pin was pushed and read back before this first execution. A
new Linux checkout fetched the public branch, confirmed the exact pin and
clean state, and checked the PREREG, source-manifest and verifier hashes.
All six frozen files were unchanged and the checkout clean after execution.

Environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1. The process used the preregistered 600-second
timeout. Stdout and stderr were captured separately outside the checkout;
EXPECTED.txt is the exact original stdout, transferred without text editing.
This was the first execution of this verifier; no exploratory run preceded it.

The canonical input is the frozen minimal matrix excerpt in SOURCES.json,
whose checksum is verified at runtime. Historical full-file hashes are
provenance, not dependencies on future mutable Canon files.

The v102 release readback 38956254023, attempt 2, including published-asset
verification, was confirmed completed/success before execution. Both the
public pin receipt and its remote readback precede the timestamps above.

GitHub x86_64/aarch64 replay and independent RC review are separate evidence.
Their current states are recorded on the pull request and issue #1554; this
local run record does not claim those checks or independent review occurred.
