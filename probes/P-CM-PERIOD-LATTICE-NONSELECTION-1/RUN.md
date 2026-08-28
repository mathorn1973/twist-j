# P-CM-PERIOD-LATTICE-NONSELECTION-1 run

## Immutable pin

```text
claim_issue:       644
base_commit:       399e82af532580262fdb2d68eabe1d958fd521c2
pin_commit:        225f1b162f42a7aa1522841ab3df9997f153d848
prereg_blob:       3d164f963b5b9868eb71d3cce6f2f58b2d56a61b
prereg_sha256:     6eda2cc507656c50096a7fdeccb09a0d83dd094c7e5f4f06a8c5317172c6523f
prereg_bytes:      10610
prereg_lines:      347
verifier_blob:     204d09dd0fd8b3a40e546f0fb6dde04468f6f48e
verifier_sha256:   df3cc662b90cc4505b3eb319bd4f5cea4ea240cd012923afc59ecc89f05599bd
verifier_bytes:    9246
verifier_lines:    342
line_endings:      LF
final_LF:          yes for both pinned files
```

Both pinned files were fetched from the public remote at the exact pin before
the first formal execution. The returned Git blob SHAs equal the Git blob
hashes recomputed from the accepted source bytes. Therefore the remote bytes
are byte-identical to the accepted bytes. The displayed SHA-256 values, byte
counts, LF counts and final LF are those exact accepted bytes.

## Formal local execution

```text
platform:          Debian GNU/Linux 13
architecture:      x86_64
python:            Python 3.13.5
working_directory: isolated exact-pin verifier directory
environment:       LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
command:           python3 probes/P-CM-PERIOD-LATTICE-NONSELECTION-1/verify.py
local_command:     python3 verify.py
exit_code:         0
stderr_bytes:      0
stderr_sha256:     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stdout_bytes:      580
stdout_lines:      7
stdout_sha256:     de9393e0d0b2f2156e997d226d862b7afe99429733376c95f05509602567eeac
expected_bytes:    580
expected_lines:    7
expected_sha256:   de9393e0d0b2f2156e997d226d862b7afe99429733376c95f05509602567eeac
```

The `command` field is the canonical repository-root replay command required
by the public checker. The actual first local execution used the byte-identical
pinned verifier in an isolated directory and is recorded separately as
`local_command`.

The verifier process was executed once after remote readback. Its stdout was
captured byte for byte as `EXPECTED.txt`; its captured stderr was empty.

The outer interactive container harness emitted a post-command terminal
cleanup warning, `TERM environment variable not set`, after the captured
verifier output had completed. That message was not written by `verify.py`,
is absent from the verifier stderr file, and is not part of `EXPECTED.txt`.
No verifier rerun was performed to hide or replace that harness diagnostic.

The local lane is one x86_64 reproduction only. It does not satisfy the public
two-architecture gate. Native aarch64 and the GitHub x86_64 replay must
reproduce `EXPECTED.txt` byte for byte and the aggregate `check` must pass.
