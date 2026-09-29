# Prospective exact audit record

PUBLIC / NON-CANONICAL. One-architecture evidence. Issue: #1281.
Author: A. M. Thorn. Action layer: L1.

Preregistration commit: 821090bc4daa55bb9974e3ec5a8e6af4d391a07a.
Frozen tree: 5e5d2f1c1c5f519099ac275f40a402796eb1774e.
Basis: d708d887f3dbf92ae02115d92ecf12d581db72b5 (canon-v93).
The six preregistered files were publicly read back before execution and
remain unchanged. The checked-out tree was clean.

## Environment

platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
Python: 3.13.5
PYTHONHASHSEED=0
LC_ALL=C
TZ=UTC
PYTHONDONTWRITEBYTECODE=1
per-script timeout: 120 seconds

No random sampling, floating-point arithmetic or external Python packages.
Both scripts were executed once after the pin; neither failed or timed out.
The code and all checks ran on one architecture. Python 3.12 two-architecture
scientific replay is not asserted by this record.

## Primary implementation

Command, from repository root:

    python3 notes/C-J-TWO-TRACE-RESIDUE-DECODER-N/verify.py

exit code: 0
stdout file: VERIFY.txt
stdout bytes: 752
stdout SHA-256: 404690c130f1a93295f8469ddd38b19704079d0410101622f84485709c3f3113
stderr bytes: 0
stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

## Same-author adversarial implementation

Command, from repository root:

    python3 notes/C-J-TWO-TRACE-RESIDUE-DECODER-N/break.py

exit code: 0
stdout file: BREAK.txt
stdout bytes: 634
stdout SHA-256: 2f735b48fdcfa0ea75874f4c39d6a9a00ef6cce6c2e5e3eb72afac7fe7507d62
stderr bytes: 0
stderr SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

The CENSUS lines match byte for byte. The entire sorted strip is committed to
by SHA-256 6a08d7de33b4cadb615f942b37202540dd6dea0f59f2412ffb822389c7c1cdab.
The serialization is compact Python json.dumps of the sorted four-coefficient
list, with separators comma and colon, encoded as UTF-8 without a newline.
The two implementations use different coefficient boxes and arithmetic paths.
Same-author method separation is not independent-agent confirmation.

SHA256SUMS binds the exact six frozen inputs and the result package. GitHub's
authorized connector created the public commit under A. M. Thorn's account;
its commit email is connector-controlled, not a runner-supplied identity.
