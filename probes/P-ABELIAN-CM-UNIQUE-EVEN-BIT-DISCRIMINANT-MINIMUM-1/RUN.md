# P-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM-1 formal run record

pin_commit: d0739111c7c83e558574525598673a1cb128c20b
base_commit: 61f33e61bdde5adf355fb605f620f1601e154fc2
prereg_sha256: 96e18d21b61aef4ecb3a93d30c9a833d2337c026376be2675be68692c7e36de3
prereg_bytes: 19099
prereg_git_blob: fc1ff211cdc62f9e9b9b2264d0d3f864d2d5d61b
verifier_sha256: 955ea322ff4f59904e6d216d8bcc61e6aae5f8cbe89c9136e33a2853b51c2e34
verifier_bytes: 11347
verifier_git_blob: 94d373e55af6015aeb8e34c5dea71f8057728ea9
command: python3 probes/P-ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
initial_capture_mtime: 2026-08-03T19:24:17.757810002+02:00
corrective_capture_mtime: 2026-08-03T19:39:35.389320033+02:00
pre_run_clean: yes
post_run_clean: yes
verifier_executions: 2
accepted_execution: corrective execution 2
exit_code: 0
stdout_sha256: b1547b0a0291466fa9927be4ec81f125a6449dafb1cc95f2af0a65dd347983b9
stdout_bytes: 928
stdout_lines: 9
stdout_cr_bytes: 0
stdout_final_byte: 0a
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result_transcript: 7/7 ALL PASS
formal_leg: ACCEPTED on the corrective x86_64 execution
architecture_gate: local formal x86_64 leg complete; required GitHub x86_64 and aarch64 replays pending
initial_attempt_integrity: STOP preserved; exit-code capture file contains byte 6e (`n`) instead of a numeric status
public_lock: issue 262

The verifier was executed twice from a clean detached checkout of the public
pin. Both complete stdout transcripts reached `RESULT 7/7 ALL PASS`, were
byte-identical, and had empty stderr. `EXPECTED.txt` preserves their exact
928-byte, LF-only stdout with a final LF.

The surrounding shell wrapper failed to preserve the verifier process status.
Its exit-code file contains only byte `6e` (`n`), caused by quoting across the
Windows-to-WSL command boundary. The wrapper itself then exited zero by design,
so that zero is not evidence of the verifier's exit status. Static inspection
shows that the frozen Python source returns normally after printing the final
line and contains no explicit nonzero exit path after it, but this inference is
not substituted for the directly observed `exit 0` required by the frozen
threshold. This first-attempt integrity failure remains preserved here.

The explicitly authorized corrective execution used a wrapper first checked
with `false -> 1` and `true -> 0`. It directly returned exit 0, produced empty
stderr, and reproduced `EXPECTED.txt` byte for byte. The local formal x86_64
leg is therefore accepted. Required GitHub x86_64 and aarch64 replays, owner
proof acceptance, and any public registration remain pending.
