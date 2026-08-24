# P-QDD-COMMUTATOR-READOUT-FORK-2 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed by
the pull-request workflow, which reruns the pinned verifier on x86_64 and
aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

```text
pin_commit: ba1c4bd9efa2df3ea38084ac3f734c9b15754eac
verifier_sha256: 1b0f98e434567643b8504e41bc3137e4a71b35bb4538c48e45cf3d5d31ed0657
command: python3 probes/P-QDD-COMMUTATOR-READOUT-FORK-2/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 7fd381ffd04ecc55663c62d59f537bcd159dc64fcbc8133361424639c4a5983e
stdout_bytes: 636
stdout_lines: 21
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 9d06e5386d2481890eedcb13b0fe02ba1386da0b
prereg_sha256: cda91edb2c19e189e6dd609a66818aed8535937a7e753e60ad6984024eb6be58
prereg_bytes: 5604
prereg_lines: 147
prereg_blob: 15ee3f0f3c3e7d436e444be8c83ba0420a884d43
verify_bytes: 4594
verify_lines: 81
verify_blob: 5925ea019bf0d50fa74f8a2c717f031b1200b6ba
public_pin_comment: issue 493 comment 5371489240
predecessor_stop: issue 492, no scientific conclusion and no reused evidence
```

Both fresh accepted files were read back from the exact public pin before
execution. Their Git object IDs, SHA-256 values, byte counts, LF endings, final
LF and UTF-8 decoding matched. Static AST parsing passed before pinning. The
successor verifier bytes had never been executed.

The verifier was executed exactly once from a repository-shaped root under:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

The process began at `2026-08-21T14:52:07Z` and ended at
`2026-08-21T14:52:09Z`, within the frozen 120-second limit. It returned zero
and wrote zero stderr bytes. `EXPECTED.txt` is its complete raw stdout, with LF
endings and final LF. A surrounding execution service emitted `TERM environment
variable not set` only after the verifier process, capture files and exit record
were complete. That service warning is outside the verifier process and is not
part of `EXPECTED.txt` or captured stderr. The verifier was not rerun.

```text
checks: 14/14 PASS
decision: EQUALITY-FORK
centralizer: signs only
event_readout: complete for event equality and blind to internal commutators
quadratic_readout: sign-complete and faithful to nonzero internal commutators
public_boundary: common ordered-composition decoder domain not supplied
scope: O2 unchanged; O1 untouched; SAMPLING NOT PROVIDED
```
