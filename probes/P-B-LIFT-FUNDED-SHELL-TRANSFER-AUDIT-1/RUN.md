# First independent audit run

PUBLIC / NON-CANONICAL / L1. One actual local execution before author
proof, code or results were opened. Numerical targets were exposed in
the frozen author specification; code and proof were independently written.

pin_commit: a914ce8e02055fb7640f821cd9bd87fadf835694
command: python3 probes/P-B-LIFT-FUNDED-SHELL-TRANSFER-AUDIT-1/verify.py
verifier_sha256: 5ea81d92648cf91f3dce69d5d0bd7b9d4361a49ac34bd5374188f344070a47bc
platform: Linux
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: 9a11517f7fa63fba8b468b1fae1f152c88bcc3890c5b427e85dbf4c34c3f809b
stdout_bytes: 771
stdout_lines: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-17T21:01:36.271432+00:00
completed_utc: 2026-10-17T21:01:37.080529+00:00

The complete independent proof and verifier were frozen at the pin,
pushed and downloaded byte-identically before this execution. The pin
receipt is #1593 comment6240975197. The original author implementation
was neither read nor imported. First execution used the environment and
600-second timeout of the repository checker. EXPECTED.txt is the actual
first stdout. Independent failure, if any, is retained rather than fixed.

Required PR replays are reported separately in the delivery receipt.
They rerun this independent reviewer implementation; they do not imply
further independent authors. The universal claims use PROOF.md.
