# P-QDD-COMMUTATOR-SATURATION-CLOSURE-1 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed only by the pull-request workflow, which reruns the pinned verifier on x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

```text
base_commit:      5e077db1a33924bbaaeb8498046605a21e1b0a0d
pin_commit:       c61d1e174b7bd4c167bbc86d7dccc52e822ac296
prereg_sha256:    f0d428cec1c6f0552e239be522a0f2a64decd20e538992c26f0efc18d4e25f96
prereg_bytes:     11796
prereg_lines:     372
prereg_blob:      7df9fa1e12578573660f2c874c1b4e996762294a
verifier_sha256:  6ae0622fba8a7a79709b30effd442a5b50687648045bbaa10b578cbc6f4bbbc8
verifier_bytes:   7914
verifier_lines:   274
verifier_blob:    d53fdf856634ba43c1dc8fcf600d36a0dbe875fd
command:           python3 probes/P-QDD-COMMUTATOR-SATURATION-CLOSURE-1/verify.py
platform:          Debian GNU/Linux 13
architecture:      x86_64
python:            CPython 3.13.5
start_utc:         2026-08-21T18:36:45Z
end_utc:           2026-08-21T18:36:46Z
exit_code:         0
stdout_sha256:     38340435f52f82fa29feb33883d413ecc9ce85faaf94bd57ad5f4f34c609b919
stdout_bytes:      824
stdout_lines:      27
stderr_sha256:     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes:      0
formal_runs:       1
```

## Pin audit

Both pinned files were fetched from the public branch after the pin and reconstructed locally from the readback. Their Git object hashes matched the public blob identities exactly before execution. No verifier import or execution occurred before the pin. The accepted verifier was executed once and was not rerun.

## Decision

```text
SATURATION-DICTIONARY-BOUNDARY
```

The machine audit is exact arithmetic only. The universal class-completeness and centralizer statements are carried by the written proof in `PREREG.md`. The architecture nonimplication is carried by direct comparison with the authoritative v59 decoder text and is not inferred from machine output.

```text
SAMPLING NOT PROVIDED
```
