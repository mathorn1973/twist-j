# Exact local validation record

**NON-CANONICAL incubation; one local x86_64 lane.** This is not a formal
public probe run or a two-architecture computation gate.

Authority base: Public Canon v89, main
`911481e735b57cbf66cbf3ba47e2e21adcfc6d94`.
All five normative hashes were checked against canon/SHA256SUMS. The
declared content commit and tag are ancestors, and the base main has
successful architecture-x86_64, architecture-aarch64 and aggregate check
in [run 35473905890](https://github.com/mathorn1973/twist-j/actions/runs/35473905890).
Those checks establish the input authority, not execution of this new note.

## Prospective freezes

The mathematical contract was publicly committed and read back before
scientific computation:

```text
PREREG commit c083513a8f00ea1f66a72c54e7e1c8e24bb3342e
PREREG SHA256 9cc9d91e2d10d6bb72be056e7900c4d05550839c4fd57899c48852fadbd74f77
PREREG bytes 6836
```

Both exact implementations, proofs and scope notes were subsequently frozen
in a public descendant before execution:

```text
source commit b13fb785c43143115087b01de9c9495b5b264b76
verify.py SHA256 e138027556b938005098368fc9d6b1b964779764ed203502e789664f249ba8ff
verify.py bytes 5548
break.py SHA256 91fc6713d17025a3deeaf82cf606138381ed0f7bbb897cc1eca3d8432a1e446f
break.py bytes 15915
```

Both remote source files were read back byte for byte. The local checkout
was clean at the source commit immediately before the authorized first
runs. Only static parsing/compilation and hashing preceded execution.

## Builder execution

```text
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
Python: 3.12.14
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
timeout: 120 seconds
command: python3 notes/C-U-SELECTOR-READING-STRUCTURE-N/verify.py
exit: 0
stderr bytes: 0
stdout bytes: 678
stdout SHA256: 68f9e15af77382350e52440a70ba242d96e2451928c054b6471a16f0af1660ae
```

The committed EXPECTED.txt is the exact output of this first successful
execution. The audit checks all 15625 checkpoints, 31250 selected edges,
all transient-path identities, fibre and quadratic-image counts, and the
finite premises of the all-n selector proof. No scientific falsifier fired.

The separate breaker record is [BREAKER.md](BREAKER.md). It uses another
implementation and the same local architecture. The previously exposed
count and conjecture are disclosed in PREREG.md; neither run is described
as blind discovery or as the first formal run of #1069.

## Reproduction

Run the two scripts separately under the recorded environment and compare
their output with EXPECTED.txt and BREAKER-EXPECTED.txt respectively. The
outputs have different formats because the attacks were independently
written. Agreement concerns the mathematical statements, not equal stdout
between the two implementations.

No claim is made that passing PR policy jobs replays either note audit on
two architectures. A future formal probe needs its own repository runner
and prospective source pin. No existing sealed probe record was modified.
