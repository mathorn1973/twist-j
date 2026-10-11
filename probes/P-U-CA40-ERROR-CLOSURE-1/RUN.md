# First completed exact run

PUBLIC NON-CANONICAL. Original text Apache-2.0.

```text
pin_commit: 3440928c77239bd26907a52810db7ec611f134d8
verifier_sha256: 40619b06663d814657391a81b490a83733b75472d544155db3abf3a2f20e32af
command: python3 probes/P-U-CA40-ERROR-CLOSURE-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 4f0de0441229a6f869ce766e339b2ca34cde7c30dba7f570af3a41a457308dff
stdout_bytes: 1044
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

All twelve source/manifest files were publicly read back byte for byte at
2026-10-11T11:33:19.986774+00:00, before scientific execution.
The preregistration SHA-256 is
`0f35e9cf6a5b813fb754e95102a8a467dcd9b3b65c7114cfa41d208eae8efb26`.
The execution system fetched a clean sparse checkout of this exact public
pin and verified every source hash. No scientific source changed afterward.

The first exact run started at 2026-10-11T11:35:01.349101+00:00 and
finished at 2026-10-11T11:35:01.664652+00:00. Its observed wall time was
0.315559700 seconds. EXPECTED.txt is the original 1044-byte ASCII stdout,
including its explicit LF, copied from the preserved first-run evidence.

This standard-library gate audits the exact supporting identities and
counterexamples listed in EXACT-DESIGN.md. It does not execute the interval
propagator. The separate enlarged-space numerical campaign, error account,
decisions and limitations are recorded in NUMERICAL.md and RESULT.md.
Architecture CI replays the exact verifier and byte comparison; it does
not independently reproduce the large numerical campaign or validate
physical hardware.
