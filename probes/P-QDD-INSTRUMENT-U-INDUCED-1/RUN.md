# P-QDD-INSTRUMENT-U-INDUCED-1 run record

The flat fields below are the machine-readable local leg required by
`tools/check_verifier.py`.

```text
pin_commit: 45cad3384c69d7f2e187d88e63c10ecbad965f0d
verifier_sha256: 991e648fee113117b4028d3776f997f9e2725da04b1d856bc61f7adc2171e3b4
command: python3 probes/P-QDD-INSTRUMENT-U-INDUCED-1/verify.py
platform: Linux 6.18.35
architecture: x86_64
python: 3.12.13
exit_code: 0
stdout_sha256: 652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c
stdout_bytes: 3441
stdout_lines: 33
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
github_platform: GitHub Actions ubuntu-24.04-arm
github_architecture: aarch64
github_python: 3.12.13
github_verifier_sha256: 991e648fee113117b4028d3776f997f9e2725da04b1d856bc61f7adc2171e3b4
github_stdout_sha256: 652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c
github_exit_code: 0
github_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
github_stderr_bytes: 0
github_status: PASS
github_verdict: VERIFY PASS
github_byte_identity: PASS
github_replay: PASS
```

The local leg is not the public two-architecture gate by itself. Pull-request
workflow run `31961611319` independently reproduced the same pinned verifier
and exact stdout on aarch64 (job `95200329536`) and x86_64 (job
`95200329591`). Aggregate job `95200657530` printed
`TWO-ARCHITECTURE CHECK PASS`. The machine-readable GitHub leg above records
the aarch64 run, which is architecture-independent evidence relative to the
local x86_64 leg.

## Authority and immutable pin

- Public base: Canon v49.
- Activation merge: `8e38bb773c0c9a375440eef23f764efcaa07ab5c`.
- Canon content commit: `dc80228522a4ccb9495550dfbef8ba73b33b2157`.
- Canon SHA-256: `d456c42575375774200b08dafc3b4225643f526f5f1826292f1255f39d332f9e`.
- Claim-lock issue: `#395`, `P-QDD-INSTRUMENT-U-INDUCED-1`.
- Pin commit: `45cad3384c69d7f2e187d88e63c10ecbad965f0d`.
- PREREG commit preceding the verifier commit: `84888d086dff15b59c88fa69ff9a840761cfd082`.
- The public files were fetched back from the pin commit before execution and matched the local bytes.

| Pinned file | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `PREREG.md` | 26800 | `95782b2195ccaa6cd8a7bf56cb8cf9fd7a8574631aa0c3bd5ae893ec68ad2ca2` | `853a84dd7a71f75c9310ebd151c9350f00e5badb` |
| `verify.py` | 57695 | `991e648fee113117b4028d3776f997f9e2725da04b1d856bc61f7adc2171e3b4` | `913679a1fa401a99c4bc73b4671d90aafb4a9f48` |

The pin was public before the first verifier execution. The issue comment recording the pin and the zero-execution state is comment `5308634552`.

## Pre-run audit

Three independent static reviews inspected the frozen PREREG and verifier without importing or executing the verifier. They checked the exact generator transcription, target firewall, sign/orientation handling, zero and missing post categories, global-family parameter logic, seed quantifiers, packed arithmetic bounds, serialization, and bounded storage. All three ended with `PASS` and no remaining pin blocker.

## Accepted verifier executions

Environment:

```text
Python 3.12.13
Linux 6.18.35 x86_64
```

First execution:

```text
python probes/P-QDD-INSTRUMENT-U-INDUCED-1/verify.py
exit=0
wall=106.54 s
```

The exact stdout from this first accepted execution is `EXPECTED.txt`.

Second local reproduction:

```text
diff -u probes/P-QDD-INSTRUMENT-U-INDUCED-1/EXPECTED.txt \
  <(python probes/P-QDD-INSTRUMENT-U-INDUCED-1/verify.py)
exit=0
wall=102.02 s
diff output: empty
```

Accepted-verifier local execution count at publication: **2**.

| Result artifact | Bytes | SHA-256 |
|---|---:|---|
| `EXPECTED.txt` | 3441 | `652baf70e75600fa80fb685c36435b19cdaae6e8f519e207e0d0a646bb7f5d5c` |

The canonical table root printed in both executions is:

```text
0baacabc9d94a824c6a9480695c7a37f2762a3a2e773d1161c26816a2dbdee15
```

## Independent blind breaker

An independent checker was derived from `PREREG.md` only. Before freeze it did not inspect `verify.py`, `EXPECTED.txt`, any run/result output, or another agent file.

| Blind artifact | Bytes | SHA-256 | Pre-freeze executions/imports |
|---|---:|---|---:|
| `blind_break.py` | 26103 | `bae54c4df9b48bc28cb693ab70514fd91ec074181b7a1cc26e75203ecda000a6` | 0 / 0 |

Syntax-only compilation passed before freeze. One attempted wrapper invocation failed with exit 127 before Python started because `/usr/bin/time` was absent; it is not a checker execution. The first actual blind execution then completed:

```text
python blind_break.py
exit=0
wall=28.184 s
user=28.175 s
sys=0.008 s
```

The breaker independently reproduced every decisive tag in its declared scope:

```text
CHANNEL-PASS
REAL-SINGLE count=0
REAL-LONG count=0
REAL-CENSUS count=0
INFO count=150
SEED-DEPENDENT-271350
ORIENTATION-DEPENDENT-22500
BREAKER-COMPLETE decisive-tags-and-C1-C3-only
```

The breaker intentionally does not audit induced post objects, the family test, the accepted verifier's serialization hashes, or repository authority gates. Its independent scope and exact output are recorded in `BLIND_RUN.md`.

## Accepted stdout headline

```text
PASS C1 ...
PASS C2 ...
PASS C3 ...
PASS C4 ...
PASS C5 ...
PASS C6 ...
PASS C7 ...
PASS C8 ...
PASS C9 ...
RESULT 9/9 ALL PASS
```

`9/9 ALL PASS` means that the verifier completed and correctly classified all frozen alternatives. It does not mean that the positive QDD-instrument claim passed; the scientific result is stated in `RESULT.md`.
