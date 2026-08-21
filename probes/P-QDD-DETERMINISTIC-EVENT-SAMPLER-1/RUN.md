# P-QDD-DETERMINISTIC-EVENT-SAMPLER-1 formal run record

Date: 2026-08-21

Status: accepted local formal record. The public two-architecture computation
gate is completed only by the repository pull-request workflow, which reruns
the pinned verifier on x86_64 and aarch64 and compares stdout byte for byte
against `EXPECTED.txt`.

```text
base_commit:       307e872d529ed053c972a726c2f456378850e92a
pin_commit:        2be3c0426791921a258e9354c4694c49d03f607a
command:           python3 probes/P-QDD-DETERMINISTIC-EVENT-SAMPLER-1/verify.py
verifier_sha256:   407b73fa434ffbfafae9b8b097a78f427b573c3db5fa6bc0cdcbc5c3abea9dd2
pin_tree:          8e971ca7b60c308a60d5b0e95bb32c96ee442466
prereg_blob:       982e93282537fd77bbd094f194bcc595f3cd56d9
verify_blob:       48b8864f61a2dd95e7a32250ffbb368c28b8699e
prereg_sha256:     105eca3a7cd091dca3c09980b23acafc4734d79df32f1735ea4805ed679bed17
verify_sha256:     407b73fa434ffbfafae9b8b097a78f427b573c3db5fa6bc0cdcbc5c3abea9dd2
prereg_bytes:      17127
prereg_lines:      490
verify_bytes:      8949
verify_lines:      260
formal_execution_count: 1
```

## Mandatory pin readback

The final pin was two commits ahead of the exact public base and added exactly
`PREREG.md` and `verify.py` in this probe directory. Before execution, the
public commit and both Git blobs were fetched independently. Their Git object
IDs, SHA-256 hashes, byte counts, LF line counts, absence of CR bytes, final LF,
and bytes matched the accepted local files exactly.

Static compilation was the only pre-pin code check. The accepted verifier was
not executed or imported before the pin. The pin was recorded publicly in
issue #512 comment `5374146578` with formal execution count zero.

## Accepted execution

```text
actual_command:    python3 /tmp/probe_build/verify.py
platform:          Debian GNU/Linux 13 (trixie)
architecture:      x86_64
kernel:            Linux 6.18.35
python:            CPython 3.13.5
exit_code:         0
stdout_sha256:     4e68c88fd00f2da1e5d8dc8d317795b242e7dc5aeb374824caf624f9ce61cdcf
stdout_bytes:      1579
stdout_lines:      20
stderr_sha256:     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:      0
transcript_match:  byte-identical to frozen PREREG transcript
checks:            14/14 ALL PASS
decision:          MECHANICAL-SAMPLER-BOUNDARY
```

The temporary path is only the execution location. The executed bytes had Git
blob `48b8864f61a2dd95e7a32250ffbb368c28b8699e`, identical to the public pinned
`verify.py`. No input, file read, network, randomness, floating point,
subprocess, or environment-dependent output was used by the verifier.

The accepted verifier was executed exactly once and was not rerun. The public
run record was posted to issue #512 comment `5374156579`.

## Formal result

```text
result:       14/14 ALL PASS
decision:     MECHANICAL-SAMPLER-BOUNDARY
O1 status:    OPEN
sampling:     NOT PROVIDED by the current public architecture
O2 status:    UNTOUCHED
layer:        L1 exact arithmetic plus the named L1 to L5 protocol
L6 measure:   NONE
```
