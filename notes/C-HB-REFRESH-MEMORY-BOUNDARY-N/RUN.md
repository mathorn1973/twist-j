# First exact finite audit

NON-CANONICAL / L1 / candidate-C. Source-exposed, one x86_64 lane.
This is the first scientific execution after the public five-file pin and
byte readback in #1525. The prospective main-replay prerequisite was fulfilled
before this run, as recorded in #1525 comment 6198340478.

input_pin: 8ab77c73426a6a65a13ddb8798390df534e64814
source_main: b79143fb00839b870686f6cea34e174959060df1
verifier_sha256: 14efe377349b233d545b39f3160604fe28ee195a496335f6fb85be8cbb93b5e2
command: python3 notes/C-HB-REFRESH-MEMORY-BOUNDARY-N/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
started_utc: 2026-10-15T17:36:13.876809+00:00
finished_utc: 2026-10-15T17:37:15.810891+00:00
exit_code: 0
stdout_bytes: 533
stdout_lines: 1
stdout_sha256: 4c01c1dbe5e5dd4282d9c37543fe492c13c8835845a10d05e32ef9f77581a030
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
safety_timeout_seconds: 600

Environment: PYTHONHASHSEED=0, PYTHONUTF8=1, PYTHONDONTWRITEBYTECODE=1,
LC_ALL=C, LANG=C, TZ=UTC. No first-run failure, timeout, rerun, source repair
or threshold change occurred. EXPECTED.txt is the actual first stdout.
The complete input files remain byte-identical to the input pin.

The proof-derived targets and old kappa row were exposed before this audit.
The full-F coefficient transport and direct occupied-wave program have one
author; they are not independent-agent evidence. This notes audit does not
satisfy a formal two-architecture gate. Notes CI does not execute it.
