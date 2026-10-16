# First accepted execution

**NON-CANONICAL / conditional L1.** Date: 2026-10-13.

## Exact mathematical controls

```text
pin_commit: e801d1dc546127db2f065c212b7830938f734045
verifier_sha256: 49d2000bbb6ed2dc1e2c2c0a6f68c6bd4463b42ddf8bcf411d5415101a6e0820
command: python3 probes/P-DP5-ENDPOINT-RESTORATION-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 1ac3f44b3cc1275eaf7052b5e5403b1314def12db4655f7054e8150c09f62ff6
stdout_bytes: 449
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

The source was fetched from the public Git branch into a separate clean
Linux checkout at the exact pin. All eight source-file hashes and the
624-byte source manifest were read back before execution. The manifest's
SHA-256 is `e1647ea06244a2bcbf9c15575de848a97691cc2d12beef360499717efbf6ae8f`.
The coordinator separately checked the public API preregistration and
manifest before accepting the pin.

The machine-readable `command` field uses the repository validator's required
replay form. The actual first invocation used
`python3 -I -B probes/P-DP5-ENDPOINT-RESTORATION-1/verify.py`, under the
same external timeout supervisor. The first verifier began at
`2026-10-13T15:47:51.722414+00:00` and ended at
`2026-10-13T15:47:53.489727+00:00`, elapsed 1.7673448640853167 seconds.
The interpreter was isolated with `-I -B`; the dispatch additionally set
`PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`.
Its exact first stdout is preserved as `EXPECTED.txt`. It ran no production
overlap or propagation. No accepted source byte was changed after the pin.

The repository's architecture jobs replay only these mathematical controls.
They must not be described as two-architecture restoration of the external
74-MB endpoint payload.

## First production restoration

After the first exact controls passed, the same clean accepted checkout
executed the single frozen production invocation. The command was the
README's `timeout --signal=TERM --kill-after=5s 610s python3 -I -B` supervisor
form, followed by `restore.py`, the full accepted candidate, the immutable
offline campaign and a new output directory outside both source and input.
Private transport paths and process identifiers are not public evidence.

| Receipt field | First observed value |
|---|---|
| Candidate | `e801d1dc546127db2f065c212b7830938f734045` |
| Start UTC | `2026-10-13T15:47:53.597141+00:00` |
| End UTC | `2026-10-13T15:56:59.398838+00:00` |
| Bounded invocation seconds | 545.7959707044065 |
| External supervisor seconds | 545.975156256929 |
| Exit | 0 |
| Standard error bytes | 0 |
| Production attempts | 1 |
| Distinct completed overlaps | 720 |
| Complete pairs | 6 |
| Source clean after dispatch | true |

The scientific stdout equals the first `result.json` byte for byte. Its
899553 bytes are preserved as `RESTORATION.json`, SHA-256
`59f2d0d9386842c5914eab566f33059c67541b0c1c7031f8cf79326feb56fa70`.
Timing and neutral environment metadata are separate in
`PRODUCTION_RUN.json`, SHA-256
`90a99243ac82c457bf761a92add1261028ee67f83f88beef23733ba959231d11`.
Both the implementation and its external supervisor observed exit zero.
The accepted scientific source files, source manifest and input binding
remain byte-identical to their pin. No first output was replaced.

## Supplemental Windows control replay

The repository verifier was also invoked on Windows after the first outcome.
The control process exited zero with empty stderr, but byte comparison failed:
Windows emitted a CRLF line ending, giving 450 bytes and SHA-256
`bc060af94b2ecda76f1609805561055ea3e8f9e5bc3a60f73eddcc9f4be61a27`.
Replacing the sole LF in the 449-byte first output with CRLF produces exactly
that hash. This is a recorded portability limitation of the text stdout, not
a passing byte-identity replay. The accepted source and first Linux output
remain unchanged. The prescribed architecture jobs use Linux. No production
restoration was repeated by this supplemental control replay.
