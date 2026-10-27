# Independent post-run scope and custody review

**NON-CANONICAL. Accepted for the stated conditional ideal-model local
result.** This review reads the first recorded run and its exact output;
it is not another scientific execution or a physical validation.

## Custody and observed record

The reviewed preregistration pin is
`b1b2019f35fc2cc3bc5b3d364f9d6ad8c2051a11`. All nine frozen files were
compared with their Git objects at that pin and remained byte-identical.
The seven support-file lengths and SHA-256 values agree with INPUTS.json.
The manifest hash agrees with the primary's embedded constant:
`66691a0298ed37e8e56dfaa6ffd9db9468b863fd430eab404dca2f8e2d65f3a5`.
The unchanged primary hash is
`0a12e3ff056638ee4b9c373f7848b338b7a7c335ea5876c620ea0d0b2a530eee`.

[RUN.md](RUN.md) records public readback at 14:23:45 UTC, followed by the
first Linux execution at 14:24:02--14:24:05 UTC on 2026-10-04. It records
exit zero, empty stderr and neither timeout reached. These lifecycle facts
are reviewed from the run record; no new execution was used to recreate
them. The independently inspected [EXPECTED.txt](EXPECTED.txt) is exactly
767 bytes, with ten LF-terminated lines and no CR bytes, and has SHA-256
`baa2242ce69f4d28872a88048697e3447acb5ac60e48e26150649861fe7106fd`.
Its independent-checker stdout hash agrees with the recorded value.

The neutral RUN record received machine-readable keys after an initial
infrastructure parser rejection of its table-only format. This is a record
format correction: no frozen file or scientific output was changed. It is
not a failed scientific execution or a repaired scientific candidate.

## Counts and target

Both observed contact entries contain 240 completed LS loops, 1771 common
star carrier pulses and total positive carrier angle 1766*pi. The disclosed
72 forward permutation pulses give 144 pulses per echo, hence

```text
LS loops       = 12 * 20 = 240;
star pulses    = 12 * 144 + 40 + 3 = 1771 <= 2923;
angle / pi     = 12 * 144 + 32 + 6 = 1766 <= 2918.
```

Thus the tighter time and incident-energy coefficients in
[RESULT.md](RESULT.md) are consequences of the accepted word, not changed
thresholds. Its 2012 switching-boundary intervals equal
`240 + 1771 + 1`; the two-use totals 480 and 3542 also agree. No numerical
rate, intensity, latency, energy or physical fidelity is inferred from
these exact counts. The independent compiler's alternate pulse counts
are correctly excluded from the published primary count.

The observed five successful coherent columns per contact are stronger
than the compulsory basis-label target, within the declared interaction
frame. Known laboratory phases remain declared. Failure to implement full
SWAP on arbitrary pair inputs is neither hidden nor treated as a failure
of the local target. The omitted-LS control has one successful input per
contact, as frozen. No candidate failure or class-level no-go is claimed.

## Scope of acceptance

The result remains a finite local construction in the frozen fixed-profile,
single-mode effective model. It supplies neither calibrated physical error
nor implementation of the whole preparation-to-n=9 history. Operatorial
motion closure does not assert that the actual inherited apparatus lies in
the chosen comparison domain. Archive protection, additional modes, actual
inherited resources, the conjugated native law and finite quantum
laser/controller output accounting remain open.

Canon v97, the earlier physical HOLD and the same-dictionary exclusion are
unchanged. The local x86_64 record is not represented as an independently
completed two-architecture gate; the required same-head CI replays remain
a separate condition. No public scientific status or conclusion from J is
earned by this review.

No blocking custody, target or scope discrepancy was found. This post-run
review performed zero scientific executions and zero verifier imports.
