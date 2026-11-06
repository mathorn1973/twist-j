# First-run record

**PUBLIC, NON-CANONICAL. Failed prospective audit.**
Owner issue: #1164
Author: A. M. Thorn
Date: 26 September 2026

## Frozen input

Candidate pin:

`b98c4a8710b641e20f05b33de612d776d02a707c`

Files read back from that exact commit before execution:

- `PREREG.md`
  - Git blob: `bd5546d5faeb92891f6cad52e63ea4e9c664384a`
  - SHA-256: `74621f957163807a84f548aedb69d8edc8da293a72b4ada022b542e31e5d46b8`
- `verify.py`
  - Git blob: `db3374cd099ee15998c9e6c9e44094f8ec145cae`
  - SHA-256: `b03dcfa6539b1d0c89734346f6094c1b1bee2c81a2654a95827614128df6c7c5`

The local byte readback of both files matched the GitHub blobs before the
scientific execution.

## Environment

```text
platform: Linux
architecture: x86_64
python: 3.13.5
```

No second architecture claim is made.

## Command

```text
python3 verify.py
```

## First execution

```text
exit_code: 1
elapsed_ns: 2037968427
stdout_bytes: 386
stderr_bytes: 381
```

Exact stdout:

```text
FACE_TABLE PASS ordered_pairs=9
ACTUAL_STARS PASS states=153 ordered_pairs=23409
STAR_CENSUS 0:0=153 2:0=2160 4:0=6930 5:1=2304 6:0=7360 7:1=1080 8:0=2970 10:0=360 10:2=72 12:0=20
TOKEN_PROJECTOR PASS partitions=18862 signs=8191 admissible=1719
EXTERIOR_COMPLETIONS PASS cases=12616 inadmissible=5192
CONDITIONAL_CHARGE_MAX exact=1 witness_faces=3 doubled_faces=2 admissible_signings=2
```

Exact stderr:

```text
Traceback (most recent call last):
  File "/tmp/photon_replica_completion_verify.py", line 656, in <module>
    main()
    ~~~~^^
  File "/tmp/photon_replica_completion_verify.py", line 648, in main
    gluing_audit()
    ~~~~~~~~~~~~^^
  File "/tmp/photon_replica_completion_verify.py", line 328, in gluing_audit
    assert direct_vectors
           ^^^^^^^^^^^^^^
AssertionError
```

## Disposition

The preregistered PASS condition required exit code zero and empty stderr.
Therefore the first audit **FAILED**. No retry under this pin is allowed.

The already printed checks are retained as diagnostic output only. They do not
earn candidate-C status because the complete frozen audit failed.
