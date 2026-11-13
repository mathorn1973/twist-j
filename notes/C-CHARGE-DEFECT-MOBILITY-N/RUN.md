# First exact execution

NON-CANONICAL, candidate-C only. One x86_64 lane, no independent reviewer.
Reservation #1408, predecessor #1406/#1407 unchanged.

## Frozen public input

Base: 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc (Public Canon v100).
Pin: a763c9c481058d8b41692112c4392df5bdbad070.
Pin tree: 351209c867403ccaae46cd1d8353849992e6f192.
Branch: notes/c-charge-defect-mobility-n.

The complete CONTRACT.md, PROOF.md and audit.py were published and their
three public blob IDs and byte counts were read back before execution.
Pre-run public receipt: issue #1408, comment 6042955624.
All three files remain unchanged.

| File | Bytes | Git blob | SHA-256 |
|---|---:|---|---|
| CONTRACT.md | 7480 | 14a92cba968fb3ae188dacde6dcedb5595f4f446 | c8abb3a423b398cd6c210c02f1fbecec7a679aaf9ddb6693a34d2126eabd103b |
| PROOF.md | 16715 | da3edf2a329362533752db099911a7d6c6baa084 | 4f1c9d504a74c79713eaeaa18784a4105a98adffccfbe161fe9f1d6ac2055388 |
| audit.py | 11864 | 0f4042f3f07c073eec672962294ffe6f23302df1 | ce61a71df8bb6fb0c6919be2c4c16e23ab80c9cd2d6b4c9c22dff7040fba23b6 |

No new scientific code was run before the pin. The proof and analytical
expectations were exposed before the audit, not independently predicted by
another agent. This is a prospective check of disclosed formulas, not a
blind discovery or independent implementation confirmation.

## Command and enforcement

The isolated interpreter was invoked on the unchanged audit file in the
working container with this equivalent command:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
python3 -I notes/C-CHARGE-DEFECT-MOBILITY-N/audit.py
```

The actual wrapper used the absolute mounted path and Python subprocess.run
with capture_output=True and timeout=45. The audit reads no repository file,
attachment, network, environment setting or external scientific data. It
writes only stdout/stderr. The wrapper checked all three input SHA-256
values and absence of an existing first-run receipt/output before launch.

```text
start UTC:          2026-10-07T17:14:42.055613+00:00
end UTC:            2026-10-07T17:14:44.088965+00:00
platform:           Debian GNU/Linux 13 (trixie)
architecture:       x86_64
Python:             CPython 3.13.5
enforced timeout:   45 seconds
timeout fired:      no
exit:               0
stderr bytes:       0
stdout bytes:       24138
wall time:          2.033057222 seconds (engineering observation only)
stdout SHA-256:     5610a4d783b28445770f3928678901d032c9f1a3af055448a3d6041076d3ddbb
empty stderr SHA:   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
EXPECTED Git blob:  136812711f7464638254adeba0dcf7db930d2b9d
```

EXPECTED.txt is the exact first stdout, created only after this run.
No corrective execution, source edit or second scientific run occurred.
Subsequent parsing of the saved JSON confirmed both hop sequences are
2,0,0,...,0 through step24 and every post-first charge profile is identical.
It did not execute the model again or choose a favorable subsequence.

## Integrity and meaning

The named-file static inspection found standard-library imports fractions,
itertools and json only; no external executable or input dependency,
credentials, private host names, binary or third-party source. All files are
original English prose or exact code, below the repository size ceiling.
The author's temporary GitHub noreply-email authorization is in force.
Original prose/code: Apache-2.0.

No local full-repository replay is claimed. Source-main CI is not CI for
this note. PR CI, if passing, checks policy/unit/Canon/ledger/gates; it does
not execute this audit or furnish its second scientific architecture.
Public result-head and PR checks belong in the final issue/PR receipt, not
in this pre-publication run record.

The code PASS includes expected negative results. The new hop fails marked
continuity analytically and its frozen finite trajectory does not continue
moving after step one. None of the audit, algebraic charge permutation or
fixed-charge infimum establishes a physical current carrier.
