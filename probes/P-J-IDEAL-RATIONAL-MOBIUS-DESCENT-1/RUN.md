# P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1 formal run record

Date: 2026-08-27

Status: local accepted formal record. The public two-architecture gate is
pending the repository pull-request workflow, which reruns the unchanged
pinned verifier on x86_64 and aarch64 and compares stdout byte for byte against
the single committed EXPECTED.txt.

The flat fields below are the machine-readable record required by the public
repository checks.

\`\`\`text
pin_commit: 5248dda1c0607570895e38ef733a3cdecb2cd600
verifier_sha256: 9b81162e6ef04c749d905f543e7012f148c900b4afbf75a61987bf067a89dd88
command: python3 probes/P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1/verify.py
platform: macOS 26.5.2
architecture: aarch64
python: CPython 3.9.6
exit_code: 0
stdout_sha256: 9bc90581679a6bb19fd0439224790a91050b0b9ae1d59b19189c96076b9359b0
stdout_bytes: 517
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
\`\`\`

## Pin audit

\`\`\`text
PREREG sha256: cf2407bdb4dad82f284cb0766a997899257911bc0dcf17b264e730280f19805f
PREREG bytes:  17301
PREREG blob:   37c46c85bc338c4d1b47641a6ddcbe22385c773d
verify bytes:  23564
verify blob:   63fc0118e3f0ba6454ed0dd4d9b9e238f052f2dc
public pin comment: issue #581, comment 5436078434
\`\`\`

The verifier was executed once, formally, from a fresh clone of the public
repository at the pushed pin commit. Before execution, the full commit,
SHA-256, byte count, and Git blob of both pinned files were read back and
matched the public pin comment. EXPECTED.txt is the exact raw stdout of that
execution, with LF line endings and a final LF. The process exited zero and the
verifier wrote no stderr.

Accepted environment:

\`\`\`text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
\`\`\`

No external data were opened. Before the public pin, the accepted verifier was
only parsed and statically reviewed; it was neither imported nor executed.
Earlier incubation computations were disclosed reconnaissance and are not
evidence for this formal record.

## Accepted result

\`\`\`text
checks: 8/8 PASS
positive result: exact L1 descent theorem package survives
negative controls:
  principal-character substitution: FIRED at n=2
  inert-as-split substitution:       FIRED at n=2
  omitted ramification:              FIRED at n=5
  sign-only associate reduction:     FIRED at n=1
  nonintegral equal-norm B4 pair:    FIRED at norm 11
  open coefficient bound:            FIRED at n=4
\`\`\`

The pinned PREREG.md and verify.py were not changed after the pin.
