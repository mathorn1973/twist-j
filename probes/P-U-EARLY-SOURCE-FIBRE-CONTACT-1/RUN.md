# First completed public native-contact run

pin_commit: 9754d85622844d40212288d2204fc240e6cd8e31
verifier_sha256: 58a9ce2a846572842927f2fb18307a30bd7fe216b16233af3c35f53e319191c4
command: python3 probes/P-U-EARLY-SOURCE-FIBRE-CONTACT-1/verify.py
platform: Windows 11
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: 613ac47b49187ee1e7b89f7587ca393d8b82c71815d7d55a20605fbf7756925e
stdout_bytes: 2377
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-03T23:24:38.773316+00:00
completed_utc: 2026-10-03T23:24:43.214726+00:00

The pin was committed, pushed and read back before this first scientific
execution. Staged and committed Git blobs matched INPUTS.sha256 exactly.
The canonical command above ran using the installed CPython interpreter
with -B; the wrapper invoked both frozen implementations. Optional evidence
retention was enabled for this same run. Full states and counterexamples
are retained under evidence/. The optional independent JSONL stream remains
in local run custody and is reproducible from the frozen code.

This record reports the actual Windows x86_64 execution. The public PR
workflow independently checks identical stdout on clean x86_64 and aarch64;
its live jobs are the authority for those architecture results.
