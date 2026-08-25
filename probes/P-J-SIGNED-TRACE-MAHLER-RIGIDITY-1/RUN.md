# P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1 formal run record

Date: 2026-08-25

Status: local formal record. The public two-architecture gate will be complete
only after the repository pull-request workflow reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 95b3faf0b257f649e64e1adf728b6982719a6e59
verifier_sha256: 6b87128ed41fe3880f1fcb004553bdfe206aece983f5bb77d13282cad807c58c
command: python3 probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: b0cea58dafdab31e9e688e6e1d5c0bcbaee2fe72d291d4ff46ee294c53eb99a2
stdout_bytes: 520
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 0b7182b865a5abb8d114d0361f8e2f8c9f9a0d9c
prereg_sha256: 9de1ce0558a1778c476ab626b1c34e3e3bcafd9aef85fc378b767f640b5c14b5
prereg_bytes: 19326
prereg_lines: 559
prereg_blob: 80badd146e5402e8fe6a65e962c65350976ec075
verify_bytes: 20740
verify_lines: 665
verify_blob: 97585019536f539019fa48da1d92c4884bc2ce0c
public_claim_lock: issue 562
```

`PREREG.md` and `verify.py` were committed together and pushed before any
formal execution. They were fetched from the public remote into a second clean
checkout at the exact full pin. The remote branch, pin, parent, worktree
status, two changed paths, Git blobs, SHA-256 values, byte counts, LF-only
endings, final LF, and UTF-8 decoding all matched the pinned source bytes.

Before the pin, the accepted verifier was never imported or executed. Static
reading and syntax compilation were allowed by policy. Three separate static
reviews found and repaired, before the pin, an even-polynomial Bezoutian
calibration defect, fired-path labels, candidate-surface wording, and output
integrity details. No pinned byte changed after publication.

## Formal execution

The accepted verifier was executed exactly once from the repository root of
the clean public readback checkout.

```text
start_utc: 2026-08-25T11:26:20.2390231Z
end_utc: 2026-08-25T11:26:20.4045102Z
elapsed_ms: 161
```

`elapsed_ms` is the monotonic process-wrapper stopwatch; the UTC values are
the independently sampled wall-clock envelope and need not differ by exactly
that integer after timestamp and scheduler rounding.

The interpreter was started from an emptied environment carrying only:

```text
PATH=/usr/bin:/bin
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

The command followed those assignments exactly. Standard output and standard
error were captured separately outside the repository. `EXPECTED.txt` is the
complete raw standard output, 520 bytes, nine LF-terminated lines, with no CR.
Standard error was empty. The verifier was not rerun, and the pinned checkout
remained clean.

The local interpreter is a compatibility witness. The required pull-request
jobs independently run the same pin under Python 3.12 on x86_64 and aarch64;
their byte identity against this one committed `EXPECTED.txt` is the public
two-architecture computation gate. Only those Python 3.12 workflow jobs and
their aggregate `check` constitute the acceptance gate; the local Python 3.10
record does not.

## Accepted result

```text
binary_controls: p_L and p_R irreducible with exact root order 15
target: f_J has a 2/2 split, equals Phi_5(X-1), and carries the H(3) factor
A0: false by exact strict-lower and two orientation controls
A1: false by exact strict-lower and non-target equality controls
A2 surface: 165 pre-admissibility candidates audited; unique at-or-below-tau
            admissible survivor (4,-2)
A3 surface: 11 pre-admissibility candidates audited; unique admissible
            survivor (4,-2)
decision: J-SIGNED-TRACE-MAHLER-RIGIDITY-CONFIRMED
scope: L1 characteristic-polynomial algebra only
sampling: not provided
```

The universal A2 theorem and negative-sign gap rest on the written proof in
`PREREG.md`. The finite carrier is an exact audit, not their quantifier.
