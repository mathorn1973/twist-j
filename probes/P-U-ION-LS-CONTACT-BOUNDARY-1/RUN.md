# P-U-ION-LS-CONTACT-BOUNDARY-1 formal run

2026-10-04. This is the first formal execution of the publicly pinned
candidate. It is an exact mathematical audit in an adopted effective model,
not a laboratory run or a full fourteen-ion numerical simulation.

```text
pin_commit: 88464d909304a02082c3bae8ec1156c7aec824b1
verifier_sha256: 6974d58afcd62b1aef64e55c5195622bb7affcc4fa57ddeeb91e6fee743156b9
command: python3 probes/P-U-ION-LS-CONTACT-BOUNDARY-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: CPython 3.10.12
exit_code: 0
stdout_sha256: 166826f72f5e61bc70dee1b447d55fa46b0c4a34a290d43bfb9c3f38cddd2754
stdout_bytes: 936
stdout_lines: 69
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Prospective pin and custody

Reservation [#1360](https://github.com/mathorn1973/twist-j/issues/1360)
preceded the first commit. The accepted candidate is public at
[88464d909304a02082c3bae8ec1156c7aec824b1](https://github.com/mathorn1973/twist-j/commit/88464d909304a02082c3bae8ec1156c7aec824b1),
whose parent is `2973a432303e046aacb2cee3cea97254ea3ab8eb`.

Before execution the coordinator checked the remote branch SHA, fetched
the public recursive Git tree and every one of its nine new file blobs,
and compared their raw decoded bytes with the local files and committed
Git blobs. The accepted tree was clean, and neither EXPECTED.txt nor RUN.md
existed. No scientific program had been imported or run. Static source
inspection and AST parsing are recorded in REVIEW-PREREG.md.

| Accepted file | Bytes | SHA-256 |
| --- | ---: | --- |
| INPUTS.json | 1815 | edab37410cb23c571a46cf25fe2e70778abbf4566351fcb00697f7490ed8cafa |
| MODEL.md | 13716 | 616b83d313d051f327809b9618258a6b3362edca973acd68cb9437860b6a860f |
| PREREG.md | 10515 | 470d7d1099503fb3fcaaae692b2b2a8b7c2022164b01e5103492ae2e3772fed3 |
| PROOF.md | 13008 | 259c7165d240a899fc33ea406dedd41ae21ea4e052922afb852e1d3081558a95 |
| README.md | 2471 | f22a641159f8fdfc63db1dff9de330178a7eb1977200ff42dc7250f62750f4ac |
| REVIEW-PREREG.md | 8792 | 96216c7bed3303c3577a60b8a263b8b3632ed7a38b97a7b8db622ca251ec5e6a |
| SOURCES.md | 7101 | 90d79b8a3af46192fd71f1ee432c1b94230bc85cccf552f39f9f9a83c39b79a0 |
| verify.py | 8426 | 6974d58afcd62b1aef64e55c5195622bb7affcc4fa57ddeeb91e6fee743156b9 |
| verify_independent.py | 10031 | 5e9c39d927163980cfe00b026d7e0c9be0c821051655104a115688f5d99d5194 |

INPUTS.json binds the supporting texts, independent program and three
predecessor source files. Its hash is anchored in the primary verifier.
The manifest does not hash itself or the primary program; the public pin
and the identities above bind those two files without a circular hash.

## Actual process

Public byte readback completed at `2026-10-04T11:42:37.511762+00:00`.
The formal process began at `2026-10-04T11:42:48.181953+00:00` and ended at
`2026-10-04T11:42:48.249929+00:00`. It ran from the repository root on Linux
with the environment

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

The capture wrapper checked all nine accepted local file identities again
before launching the declared command. It captured raw subprocess stdout
and stderr, recorded the process exit and environment, and copied stdout
unchanged to EXPECTED.txt only after exit zero and empty stderr. The
wrapper did not compute, repair or replace any scientific result.

The primary and separately authored independent audit agreed. The actual
decision is `SYMMETRIC-ISOLATED-CONTACT-EXCLUDED-BELOW-1/2`. The same output
explicitly reports `physical_realization: NOT_PROVIDED` and
`model_error_bound: NOT_CALIBRATED`. Repository/CI replays are subsequent
validation runs; they do not replace this first execution or move its pin.
The public two-architecture gate is established only by successful CI
readback, separately from this local record.
