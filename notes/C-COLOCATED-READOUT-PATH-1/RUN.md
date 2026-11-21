<!-- SPDX-License-Identifier: Apache-2.0 -->

# Exact first-run custody

NON-CANONICAL / L1 / one local Linux x86_64 architecture, Python 3.12.14.
Each named source was run once. Failed sources were not overwritten or rerun.
This is incubation with local Git pins, not a formal public probe.

Preregistration commit: d8c7a28f. Original code/proof pin:
`c84ee2ba587fbad2fb72015c2f1753df3d1d3e7d`.
Reader-boundary correction pin: `9441c431f5e8b01cc9ae5676f5304e231bb11a05`.
Explicit-trace correction pin: `6bdb19a89eaf186e491478c03f2116b07865581d`.
All correction sources and their disclosures were pinned and announced in
issue 1955 before their first respective executions. All first outputs remain.

## verify.py

Command: `python notes/C-COLOCATED-READOUT-PATH-1/verify.py`.
Pin: `c84ee2ba587fbad2fb72015c2f1753df3d1d3e7d`.
Start UTC: `2026-11-07T23:49:53.221778+00:00`.
End UTC: `2026-11-07T23:50:12.641925+00:00`.
Exit code: 0.
Stdout bytes: 42507; stderr bytes: 0.
Stdout SHA256: `6844216c60c4473e85448179704f4ab76b142c4ff4501d55de4803abc66483d8`.
Stderr SHA256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## break.py

Command: `python notes/C-COLOCATED-READOUT-PATH-1/break.py`.
Pin: `c84ee2ba587fbad2fb72015c2f1753df3d1d3e7d`.
Start UTC: `2026-11-07T23:49:53.231625+00:00`.
End UTC: `2026-11-07T23:49:56.202071+00:00`.
Exit code: 1.
Stdout bytes: 171; stderr bytes: 53.
Stdout SHA256: `14f81c48660cab5293618a6a307f2541c7662f2a3da37ae3bf9e1114ad8d4599`.
Stderr SHA256: `ebaee4d89d6f905d6ea507235a08cdcac242166a868bd2855dd4424520bac22c`.

Deterministic stderr: `Independent frozen checker stopped at first failure.`
The complete first failure JSON is retained in its corresponding EXPECTED file.

## break_reader_boundary.py

Command: `python notes/C-COLOCATED-READOUT-PATH-1/break_reader_boundary.py`.
Pin: `9441c431f5e8b01cc9ae5676f5304e231bb11a05`.
Start UTC: `2026-11-07T23:54:07.363683+00:00`.
End UTC: `2026-11-07T23:54:37.312417+00:00`.
Exit code: 1.
Stdout bytes: 163; stderr bytes: 53.
Stdout SHA256: `c2c34de7f7448896732c60ecae934d9a1f395c05e2020a4bfa7ef817a0ca6ee9`.
Stderr SHA256: `ebaee4d89d6f905d6ea507235a08cdcac242166a868bd2855dd4424520bac22c`.

Deterministic stderr: `Independent frozen checker stopped at first failure.`
The complete first failure JSON is retained in its corresponding EXPECTED file.

## break_explicit_trace.py

Command: `python notes/C-COLOCATED-READOUT-PATH-1/break_explicit_trace.py`.
Pin: `6bdb19a89eaf186e491478c03f2116b07865581d`.
Start UTC: `2026-11-07T23:57:30.140303+00:00`.
End UTC: `2026-11-07T23:58:00.035192+00:00`.
Exit code: 0.
Stdout bytes: 25562; stderr bytes: 0.
Stdout SHA256: `51984633bb364e1ee241156fb6ebf2c73ec19f53dcbb59141b8a59d7f484a24c`.
Stderr SHA256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Source hashes

- PREREG.md: 10505 bytes; `c0b21f5889c20afd89152957cdf8464f5917f83d2f107f7d6ccc0a67e4b9888a`.
- verify.py: 12323 bytes; `1dfcfc8a9c469a23bec64479ff5285a27639ea9ff2b00311f2e6ff15696d31c0`.
- break.py: 22220 bytes; `fabd061f908caad1125502c47df4644e7db393efdbf8650ad24b3daac258295c`.
- break_reader_boundary.py: 22241 bytes; `4ddb722421d5596079d1b7bbe6edd1c4e4f8c232d681704fad76a3f17ee8563e`.
- break_explicit_trace.py: 22749 bytes; `fe4cf5d7c2eb6d89debb1452ed559291b900ec1dde7a6ef12fe7dd5de7e6981c`.

## Saved-output comparison and repository integrity

`python notes/C-COLOCATED-READOUT-PATH-1/compare_results.py` reports:

```text
PASS: 962 common result comparisons; 125 paid cases and 6 path/control cases agree.
Original and reader-boundary checker STOP outputs remain preserved; comparison uses the disclosed explicit-trace revision.
```

The comparison was written after all outputs and does not rerun the science.
It compares current coordinates, phase responses, norms, accounts, path areas,
counts and determinant coordinates. Distinct JSON serialization is retained.

`python tools/check_policy.py`: POLICY PASS.
`python tools/check_canon.py`: CANON PASS v109 claims=609.
No two-architecture scientific execution or notes-CI science gate is claimed.
