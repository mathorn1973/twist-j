# Local formal replay

NON-CANONICAL / L1 / result-exposed confirmation.

pin_commit: 77575d506ab28c1d3024b5212ede7b1bb87220da
verifier_sha256: a3658ac23fa287940781d00fe9dc9dff090df43773debcc58e01f285c67ce879
command: python3 probes/P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 4a03a48056bc18e724627eef17dd79ac518ee7bdb3e00a014e1b7da05e705dc0
stdout_bytes: 7940
stdout_lines: 441
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-11-02T18:37:46.916103+00:00

The six pinned scientific files were fetched through GitHub at the exact
pin and compared byte for byte before this first public-protocol execution.
Assertions were enabled. Deterministic environment: LC_ALL=C, LANG=C,
TZ=UTC, PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1.

## Pinned scientific file custody

| File | SHA-256 | Bytes |
|---|---|---:|
| PREREG.md | `f8814317d8a781ba4643f0deabaed1cd50c683c359ddffe3b8d17058d1792412` | 9610 |
| verify.py | `a3658ac23fa287940781d00fe9dc9dff090df43773debcc58e01f285c67ce879` | 12315 |
| WORD535.txt | `ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b` | 4877 |
| CONTRACT.md | `bdec717bbdf47926f2f2e3f5a2a47d943ce31afea6bafa7ebca8e8c79667e1f9` | 10870 |
| PROOF.md | `7559991666d237ed859286e8dd96adf9a27e62e1b9800da38024359eb5988b45` | 8534 |
| PROVENANCE.md | `acef673c45605fbe1202d7963c6647e83ccd9c1f76a6153029b7355cc8a636c1` | 4036 |

This record describes the local x86_64 execution only. The required GitHub
x86_64 and aarch64 jobs independently replay the same verifier against the
same EXPECTED.txt. Their actual outcomes are available on the pull request.
