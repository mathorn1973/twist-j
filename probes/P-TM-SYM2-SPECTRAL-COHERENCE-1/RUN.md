# RUN. P-TM-SYM2-SPECTRAL-COHERENCE-1

Local formal leg. Exactly one deterministic execution on a clean detached
checkout of the public pin, from the repository root. The cross-architecture
gate is separate and runs at pull-request time.

pin_commit: e4a2ef01c2050b50763f72176133c04ed050d4d6
base_commit: bff109aa0272cb61e33df60682f2e30358dc9765
public_lock: issue 278
prereg_sha256: 4b67a5b5848867d9fcbb7adbe0c434ed4c4b2519915e03178acfacfcc0a2d55c
prereg_bytes: 12044
prereg_git_blob: d810c1164bcafab2f60ed40a7fed8308cb0e04c7
verifier_sha256: 43be70746bdbf9a005e96143152d1506b543f91ca594e3a75df81a89b0690652
verifier_bytes: 13528
verifier_git_blob: ef1038cc1d4e1674a4b51203d522242404e11b68
command: python3 probes/P-TM-SYM2-SPECTRAL-COHERENCE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: 3.12.3
run_started_utc: 2026-08-06T05:56:37Z
run_finished_utc: 2026-08-06T05:56:41Z
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 410679552c329e420f7e7196e039c04e57708d5c9ff0975b260a2352c070b255
stdout_bytes: 1826
stdout_lines: 29
stdout_cr_bytes: 0
stdout_final_byte: 0a
stdout_git_blob: 479aa551bcc81aac93c36a5909d86f60aa73ee4e
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
route: exit zero with the terminal line RESULT: PASS (19 certificates green)
result: POSITIVE
architecture_gate: pending, the required check reruns the pinned verifier on
  the x86_64 and aarch64 runners at pull-request time and must exit zero with
  empty stderr and stdout byte-identical to EXPECTED.txt

## Integrity notes

The checkout was made by fresh clone and detached checkout of the exact
public pin; the working tree was clean before and after the execution. No
file was read by the verifier at run time. Exactly one formal execution was
performed under this probe id, as preregistered. The transcript committed as
EXPECTED.txt is the raw byte stream of that execution.
