# First exact author execution

NON-CANONICAL / L1.

pin_commit: 3b01199e8dd6ce6837e2a59bd4d6e6b06f1b3c7b
prereg_sha256: c30b72f3d210a527772703d42609d2f325e9fa43181cc489327c4abe99b25aa7
verifier_sha256: ff9f203cb60cdfe4d1caf375d86f4dbaff82a5e6830b19cc7c8b869b6ee3a96c
command: python3 probes/P-U-PAIR-PHASE-WORK-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 51dc5857a995177a05a640d6e6942e61ff9c61d796747cc4772d3281ac9a296c
stdout_bytes: 488
stdout_lines: 8
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The three source files were publicly committed and read back at pin_commit
before execution. Each matched its local bytes and Git blob identity.
Execution started from a clean checkout of that exact source pin.
The first stdout above is preserved verbatim in EXPECTED.txt.
The deterministic environment was LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC. Timeout: 600 seconds.
This is the x86_64 author run. Same-session static review is authoring QA.
